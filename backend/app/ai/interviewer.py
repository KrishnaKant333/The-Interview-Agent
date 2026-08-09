from __future__ import annotations

import json
import logging
from typing import Any

from app.ai.llm import LLMError, LLMService, generate_with_retry
from app.ai.prompts.adaptive_turn import (
    ADAPTIVE_TURN_SYSTEM,
    ADAPTIVE_TURN_USER_TEMPLATE,
)
from app.ai.prompts.candidate_analysis import (
    CANDIDATE_ANALYSIS_SYSTEM,
    CANDIDATE_ANALYSIS_USER_TEMPLATE,
)
from app.ai.prompts.final_feedback import (
    FINAL_FEEDBACK_SYSTEM,
    FINAL_FEEDBACK_USER_TEMPLATE,
)
from app.ai.prompts.first_question import (
    FIRST_QUESTION_SYSTEM,
    FIRST_QUESTION_USER_TEMPLATE,
)
from app.ai.prompts.planning import PLANNING_SYSTEM, PLANNING_USER_TEMPLATE
from app.ai.schemas import (
    AnswerEvaluation,
    CandidateProfile,
    CurrentQuestion,
    FocusArea,
    InterviewPlan,
    InterviewTurnResult,
    PlannedQuestion,
)
from app.interview.constants import (
    MAX_CONSECUTIVE_FOLLOW_UPS,
    MIN_QUESTIONS,
    MIN_UNIQUE_DAYS,
)
from app.schemas.interview import Candidate, Feedback
from app.services.candidate import (
    get_completed_days,
    get_difficult_missions,
    get_first_name,
    get_first_try_missions,
    get_mission_days,
    get_skipped_missions,
)
from app.services.curriculum import get_all_days, get_day, title_for_day

logger = logging.getLogger(__name__)

APPLICATION_PURPOSES = {"application", "scenario"}
REASONING_PURPOSES = {"reasoning", "trade-off"}


def experience_level_from_years(years: int) -> str:
    if years <= 2:
        return "junior"
    if years <= 5:
        return "mid"
    if years <= 9:
        return "senior"
    return "lead"


def build_candidate_facts(candidate: Candidate) -> dict[str, Any]:
    """Extract deterministic facts from the raw candidate — no inference beyond supplied data."""
    skipped = get_skipped_missions(candidate)
    difficult = get_difficult_missions(candidate)
    first_try = get_first_try_missions(candidate)
    completed_days = get_completed_days(candidate)
    mission_days = get_mission_days(candidate)

    return {
        "id": candidate.member.id,
        "name": candidate.member.name,
        "role": candidate.member.jobRole,
        "years_experience": candidate.member.yearsExperience,
        "education": candidate.member.education,
        "status": candidate.member.status,
        "signals": {
            "commit_days": candidate.signals.commitDays,
            "missions_completed": candidate.signals.missionsCompleted,
            "missions_first_try": candidate.signals.missionsFirstTry,
        },
        "missions": [
            {
                "day": mission.day,
                "title": mission.title or title_for_day(mission.day),
                "passed": mission.passed,
                "skipped": mission.skipped,
                "attempts": mission.attempts,
            }
            for mission in candidate.missions
        ],
        "completed_days": completed_days,
        "mission_days": mission_days,
        "skipped_missions": [
            {"day": mission.day, "title": mission.title or title_for_day(mission.day)}
            for mission in skipped
        ],
        "high_attempt_missions": [
            {
                "day": mission.day,
                "title": mission.title or title_for_day(mission.day),
                "attempts": mission.attempts,
            }
            for mission in difficult
        ],
        "first_try_missions": [
            {"day": mission.day, "title": mission.title or title_for_day(mission.day)}
            for mission in first_try
        ],
    }


def build_curriculum_summary() -> str:
    lines: list[str] = []
    for day in get_all_days():
        objectives_preview = "; ".join(day.objectives[:2])
        if len(day.objectives) > 2:
            objectives_preview += "; ..."
        lines.append(f"Day {day.day}: {day.title} ({day.type}) — {objectives_preview}")
    return "\n".join(lines)


def build_curriculum_detail(day_numbers: list[int] | None = None) -> str:
    days = get_all_days()
    if day_numbers is not None:
        allowed = set(day_numbers)
        days = [day for day in days if day.day in allowed]

    blocks: list[str] = []
    for day in days:
        objectives = "\n".join(f"  - {objective}" for objective in day.objectives)
        tools = ", ".join(day.tools) if day.tools else "none"
        blocks.append(
            f"Day {day.day}: {day.title}\n"
            f"  Type: {day.type}\n"
            f"  Tools: {tools}\n"
            f"  Objectives:\n{objectives}"
        )
    return "\n\n".join(blocks)


def _fallback_candidate_profile(candidate: Candidate, facts: dict[str, Any]) -> CandidateProfile:
    """Rule-based profile when LLM is unavailable."""
    strengths: list[str] = []
    if facts["first_try_missions"]:
        first = facts["first_try_missions"][0]
        strengths.append(f"First-try completion on Day {first['day']}: {first['title']}")
    if candidate.signals.missionsFirstTry >= 10:
        strengths.append(
            f"Strong first-attempt rate ({candidate.signals.missionsFirstTry} first-try missions)"
        )
    if facts["completed_days"]:
        strengths.append(f"Completed {len(facts['completed_days'])} recorded curriculum missions")
    if not strengths:
        strengths.append("Engaged with the curriculum across multiple mission areas")

    weaknesses: list[str] = []
    for mission in facts["skipped_missions"]:
        weaknesses.append(f"Skipped Day {mission['day']}: {mission['title']}")
    for mission in facts["high_attempt_missions"][:2]:
        weaknesses.append(
            f"Multiple attempts on Day {mission['day']}: {mission['title']} "
            f"({mission['attempts']} attempts)"
        )

    high_effort = [
        f"Day {mission['day']}: {mission['title']}" for mission in facts["high_attempt_missions"]
    ]
    skipped_topics = [
        f"Day {mission['day']}: {mission['title']}" for mission in facts["skipped_missions"]
    ]
    completed_topics = [
        f"Day {day}: {title_for_day(day)}" for day in facts["completed_days"]
    ]

    focus_areas: list[FocusArea] = []
    if facts["skipped_missions"]:
        skipped = facts["skipped_missions"][0]
        focus_areas.append(
            FocusArea(day=skipped["day"], title=skipped["title"], reason="skipped")
        )
    if facts["high_attempt_missions"]:
        difficult = facts["high_attempt_missions"][0]
        focus_areas.append(
            FocusArea(
                day=difficult["day"],
                title=difficult["title"],
                reason="high_attempt",
            )
        )
    if not focus_areas and facts["completed_days"]:
        day_number = facts["completed_days"][0]
        focus_areas.append(
            FocusArea(
                day=day_number,
                title=title_for_day(day_number),
                reason="other",
            )
        )
    if len(focus_areas) < 2 and facts["mission_days"]:
        extra_day = facts["mission_days"][-1]
        if not any(area.day == extra_day for area in focus_areas):
            focus_areas.append(
                FocusArea(
                    day=extra_day,
                    title=title_for_day(extra_day),
                    reason="other",
                )
            )

    return CandidateProfile(
        role=candidate.member.jobRole,
        experience_level=experience_level_from_years(candidate.member.yearsExperience),
        strengths=strengths[:4],
        potential_weaknesses=weaknesses[:4],
        high_effort_topics=high_effort[:4],
        skipped_topics=skipped_topics[:4],
        completed_topics=completed_topics[:6],
        recommended_focus_areas=focus_areas[:4],
    )


def validate_candidate_profile(profile: CandidateProfile, facts: dict[str, Any]) -> None:
    """Ensure LLM profile curriculum references are grounded in deterministic facts."""
    valid_days = _valid_curriculum_days()
    skipped_days = {mission["day"] for mission in facts["skipped_missions"]}
    high_attempt_days = {mission["day"] for mission in facts["high_attempt_missions"]}
    first_try_days = {mission["day"] for mission in facts["first_try_missions"]}
    mission_days = set(facts["mission_days"])
    missions_by_day = {mission["day"]: mission for mission in facts["missions"]}

    for area in profile.recommended_focus_areas:
        if area.day not in valid_days:
            raise ValueError(f"Focus area references invalid curriculum day: {area.day}")

        curriculum_day = get_day(area.day)
        if curriculum_day is None:
            raise ValueError(f"Curriculum day not found: {area.day}")

        if area.title != curriculum_day.title:
            raise ValueError(
                f"Focus area title must match curriculum title for day {area.day}."
            )

        if area.day not in mission_days:
            raise ValueError(
                f"Focus area day {area.day} is not supported by candidate mission data."
            )

        if area.reason == "skipped":
            if area.day not in skipped_days:
                raise ValueError(
                    f"Focus area reason 'skipped' unsupported for day {area.day}."
                )
        elif area.reason == "high_attempt":
            if area.day not in high_attempt_days:
                raise ValueError(
                    f"Focus area reason 'high_attempt' unsupported for day {area.day}."
                )
        elif area.reason == "low_first_try":
            if area.day in skipped_days:
                raise ValueError(
                    f"Focus area reason 'low_first_try' unsupported for skipped day {area.day}."
                )
            if area.day in first_try_days:
                raise ValueError(
                    f"Focus area reason 'low_first_try' unsupported for day {area.day}."
                )
            mission = missions_by_day[area.day]
            attempts = mission.get("attempts") or 1
            if not mission.get("passed") or attempts <= 1:
                raise ValueError(
                    f"Focus area reason 'low_first_try' unsupported for day {area.day}."
                )
        elif area.reason != "other":
            raise ValueError(f"Unknown focus area reason: {area.reason}")


def analyze_candidate(candidate: Candidate, llm: LLMService | None = None) -> CandidateProfile:
    facts = build_candidate_facts(candidate)
    if llm is None:
        return _fallback_candidate_profile(candidate, facts)

    prompt = CANDIDATE_ANALYSIS_USER_TEMPLATE.format(
        candidate_facts=json.dumps(facts, indent=2),
        curriculum_summary=build_curriculum_summary(),
    )
    for validation_attempt in range(2):
        try:
            profile = generate_with_retry(
                llm,
                prompt,
                CandidateProfile,
                system_instruction=CANDIDATE_ANALYSIS_SYSTEM,
            )
            validate_candidate_profile(profile, facts)
            return profile
        except LLMError:
            logger.warning("Candidate analysis LLM failed; using rule-based fallback.")
            return _fallback_candidate_profile(candidate, facts)
        except ValueError as exc:
            logger.warning(
                "Candidate profile validation failed (attempt %s): %s",
                validation_attempt + 1,
                exc,
            )
            if validation_attempt == 1:
                break

    logger.warning("Candidate profile invalid after retry; using rule-based fallback.")
    return _fallback_candidate_profile(candidate, facts)


def _valid_curriculum_days() -> set[int]:
    return {day.day for day in get_all_days()}


def _plan_has_required_question_types(questions: list[PlannedQuestion]) -> bool:
    purposes = {question.purpose for question in questions}
    has_application = bool(purposes & APPLICATION_PURPOSES)
    has_reasoning = bool(purposes & REASONING_PURPOSES)
    return has_application and has_reasoning


def validate_interview_plan(plan: InterviewPlan) -> None:
    valid_days = _valid_curriculum_days()
    unique_plan_days = set(plan.curriculum_days)
    if len(unique_plan_days) < MIN_UNIQUE_DAYS:
        raise ValueError(
            f"Plan must cover at least {MIN_UNIQUE_DAYS} distinct curriculum days."
        )

    question_days = {question.curriculum_day for question in plan.questions}
    if len(question_days) < MIN_UNIQUE_DAYS:
        raise ValueError("Planned questions must span at least 4 distinct curriculum days.")

    for day_number in plan.curriculum_days:
        if day_number not in valid_days:
            raise ValueError(f"Invalid curriculum day in plan: {day_number}")

    for question in plan.questions:
        if question.curriculum_day not in valid_days:
            raise ValueError(f"Question references invalid curriculum day: {question.curriculum_day}")
        curriculum_day = get_day(question.curriculum_day)
        if curriculum_day is None:
            raise ValueError(f"Curriculum day not found: {question.curriculum_day}")
        if question.topic != curriculum_day.title:
            raise ValueError(
                f"Question topic must match curriculum title for day {question.curriculum_day}."
            )
        if question.objective not in curriculum_day.objectives:
            raise ValueError(
                f"Question objective not found on curriculum day {question.curriculum_day}."
            )

    if not _plan_has_required_question_types(plan.questions):
        raise ValueError("Plan must include application/scenario and reasoning/trade-off questions.")


def _priority_days(candidate: Candidate) -> list[int]:
    """Deterministic day ordering reused from mock engine logic."""
    skipped_days = [mission.day for mission in get_skipped_missions(candidate)]
    difficult_days = [mission.day for mission in get_difficult_missions(candidate)]
    first_try_days = [mission.day for mission in get_first_try_missions(candidate)]
    mission_days = get_mission_days(candidate)
    curriculum_days = [day.day for day in get_all_days()]

    priority: list[int] = []
    for day in skipped_days + difficult_days + first_try_days + mission_days + curriculum_days:
        if day not in priority:
            priority.append(day)
    return priority or curriculum_days


def _fallback_interview_plan(candidate: Candidate, profile: CandidateProfile) -> InterviewPlan:
    """Rule-based plan when LLM is unavailable."""
    priority = _priority_days(candidate)
    valid_days = _valid_curriculum_days()

    selected_days: list[int] = []
    for day in priority:
        if day in valid_days and day not in selected_days:
            selected_days.append(day)
        if len(selected_days) >= MIN_UNIQUE_DAYS:
            break

    while len(selected_days) < MIN_UNIQUE_DAYS:
        for day in sorted(valid_days):
            if day not in selected_days:
                selected_days.append(day)
            if len(selected_days) >= MIN_UNIQUE_DAYS:
                break

    purposes_cycle: list[str] = [
        "concept",
        "explanation",
        "application",
        "reasoning",
        "trade-off",
        "scenario",
        "concept",
        "application",
    ]
    difficulty = (
        "foundation"
        if profile.experience_level == "junior"
        else "advanced"
        if profile.experience_level in {"senior", "lead"}
        else "intermediate"
    )

    questions: list[PlannedQuestion] = []
    for index in range(MIN_QUESTIONS):
        if index < len(selected_days):
            day_number = selected_days[index % len(selected_days)]
        else:
            day_number = selected_days[index % len(selected_days)]

        if index == 0 and profile.recommended_focus_areas:
            day_number = profile.recommended_focus_areas[0].day

        curriculum_day = get_day(day_number)
        if curriculum_day is None:
            continue

        objective_index = index % len(curriculum_day.objectives)
        purpose = purposes_cycle[index % len(purposes_cycle)]
        questions.append(
            PlannedQuestion(
                question_number=index + 1,
                curriculum_day=day_number,
                topic=curriculum_day.title,
                objective=curriculum_day.objectives[objective_index],
                purpose=purpose,  # type: ignore[arg-type]
                difficulty=difficulty,  # type: ignore[arg-type]
            )
        )

    return InterviewPlan(
        total_questions=len(questions),
        curriculum_days=selected_days,
        questions=questions,
    )


def create_interview_plan(
    candidate: Candidate,
    profile: CandidateProfile,
    llm: LLMService | None = None,
) -> InterviewPlan:
    facts = build_candidate_facts(candidate)
    if llm is None:
        plan = _fallback_interview_plan(candidate, profile)
        validate_interview_plan(plan)
        return plan

    prompt = PLANNING_USER_TEMPLATE.format(
        profile_json=profile.model_dump_json(indent=2),
        candidate_facts=json.dumps(facts, indent=2),
        curriculum_detail=build_curriculum_detail(),
        min_days=MIN_UNIQUE_DAYS,
    )
    try:
        plan = generate_with_retry(
            llm,
            prompt,
            InterviewPlan,
            system_instruction=PLANNING_SYSTEM,
        )
        validate_interview_plan(plan)
        return plan
    except (LLMError, ValueError) as exc:
        logger.warning("Interview planning failed (%s); using rule-based fallback.", exc)
        plan = _fallback_interview_plan(candidate, profile)
        validate_interview_plan(plan)
        return plan


def validate_current_question(
    question: CurrentQuestion,
    plan: InterviewPlan,
    target_planned_q: PlannedQuestion,
) -> None:
    valid_days = _valid_curriculum_days()
    if question.curriculum_day not in valid_days:
        raise ValueError(f"Question references invalid curriculum day: {question.curriculum_day}")
    if question.curriculum_day != target_planned_q.curriculum_day:
        raise ValueError(
            f"Question curriculum_day ({question.curriculum_day}) does not match planned question day ({target_planned_q.curriculum_day})."
        )
    curriculum_day = get_day(question.curriculum_day)
    if curriculum_day is None:
        raise ValueError(f"Curriculum day not found: {question.curriculum_day}")
    if question.objective not in curriculum_day.objectives:
        raise ValueError(
            f"Question objective not found on curriculum day {question.curriculum_day}."
        )
    if not question.text or not question.text.strip():
        raise ValueError("Question text must be a non-empty string.")
    if question.is_follow_up:
        raise ValueError("First question must not be a follow-up.")
    if question.source != "planned":
        raise ValueError("First question source must be 'planned'.")


def _fallback_first_question(candidate: Candidate, planned_q: PlannedQuestion) -> CurrentQuestion:
    curriculum_day = get_day(planned_q.curriculum_day)
    day_title = curriculum_day.title if curriculum_day else f"Day {planned_q.curriculum_day}"
    text = (
        f"Regarding Day {planned_q.curriculum_day} ({day_title}): "
        f"{planned_q.objective} How would you explain your approach in a technical interview?"
    )
    return CurrentQuestion(
        text=text,
        curriculum_day=planned_q.curriculum_day,
        objective=planned_q.objective,
        purpose=planned_q.purpose,
        difficulty=planned_q.difficulty,
        is_follow_up=False,
        source="planned",
    )


def generate_first_question(
    candidate: Candidate,
    profile: CandidateProfile,
    plan: InterviewPlan,
    llm: LLMService | None = None,
) -> CurrentQuestion:
    planned_q = plan.questions[0]
    if llm is None:
        question = _fallback_first_question(candidate, planned_q)
        validate_current_question(question, plan, planned_q)
        return question

    prompt = FIRST_QUESTION_USER_TEMPLATE.format(
        profile_json=profile.model_dump_json(indent=2),
        curriculum_day=planned_q.curriculum_day,
        topic=planned_q.topic,
        objective=planned_q.objective,
        purpose=planned_q.purpose,
        difficulty=planned_q.difficulty,
        curriculum_detail=build_curriculum_detail([planned_q.curriculum_day]),
    )

    for validation_attempt in range(2):
        try:
            question = generate_with_retry(
                llm,
                prompt,
                CurrentQuestion,
                system_instruction=FIRST_QUESTION_SYSTEM,
            )
            validate_current_question(question, plan, planned_q)
            return question
        except LLMError:
            logger.warning("First question LLM failed; using fallback question.")
            return _fallback_first_question(candidate, planned_q)
        except ValueError as exc:
            logger.warning(
                "First question validation failed (attempt %s): %s",
                validation_attempt + 1,
                exc,
            )
            if validation_attempt == 1:
                break

    logger.warning("First question invalid after retry; using fallback question.")
    return _fallback_first_question(candidate, planned_q)


def validate_turn_result(result: InterviewTurnResult) -> None:
    valid_days = _valid_curriculum_days()
    if result.curriculum_day not in valid_days:
        raise ValueError(f"Turn question references invalid curriculum day: {result.curriculum_day}")
    curriculum_day = get_day(result.curriculum_day)
    if curriculum_day is None:
        raise ValueError(f"Curriculum day not found: {result.curriculum_day}")
    if result.objective not in curriculum_day.objectives:
        raise ValueError(
            f"Turn question objective '{result.objective}' not found on day {result.curriculum_day}."
        )
    if not result.question_text or not result.question_text.strip():
        raise ValueError("Turn question_text must be non-empty.")


def _fallback_turn_result(
    session: InterviewSession,
    candidate_answer: str,
) -> InterviewTurnResult:
    words = candidate_answer.strip().split()
    score = min(10, max(4, len(words) // 5))
    evaluation = AnswerEvaluation(
        correctness=score,
        depth=score,
        reasoning=score,
        clarity=score,
        strengths=["Engaged thoughtfully with the technical prompt"],
        weaknesses=[] if score >= 7 else ["Could provide deeper architectural details"],
        misconception=None,
        should_follow_up=False,
        follow_up_focus=None,
        recommended_difficulty="intermediate",
    )

    plan = session.interview_plan
    if plan and session.plan_cursor < len(plan.questions):
        planned_q = plan.questions[session.plan_cursor]
        curriculum_day = get_day(planned_q.curriculum_day)
        topic = curriculum_day.title if curriculum_day else f"Day {planned_q.curriculum_day}"
        question_text = (
            f"Regarding Day {planned_q.curriculum_day} ({topic}): "
            f"{planned_q.objective} Walk me through your approach."
        )
        return InterviewTurnResult(
            evaluation=evaluation,
            question_text=question_text,
            curriculum_day=planned_q.curriculum_day,
            objective=planned_q.objective,
            purpose=planned_q.purpose,
            difficulty=planned_q.difficulty,
            is_follow_up=False,
        )

    day_number = session.used_curriculum_days[0] if session.used_curriculum_days else 7
    curriculum_day = get_day(day_number)
    topic = curriculum_day.title if curriculum_day else f"Day {day_number}"
    obj = curriculum_day.objectives[0] if curriculum_day and curriculum_day.objectives else "Explain core concept"
    return InterviewTurnResult(
        evaluation=evaluation,
        question_text=f"Regarding Day {day_number} ({topic}): {obj} How would you apply this in practice?",
        curriculum_day=day_number,
        objective=obj,
        purpose="application",
        difficulty="intermediate",
        is_follow_up=False,
    )


def evaluate_turn_and_generate_next(
    session: InterviewSession,
    candidate_answer: str,
    llm: LLMService | None = None,
) -> InterviewTurnResult:
    if llm is None:
        return _fallback_turn_result(session, candidate_answer)

    current_q = session.current_question
    current_day = current_q.curriculum_day if current_q else 1
    curriculum_day = get_day(current_day)
    current_topic = curriculum_day.title if curriculum_day else f"Day {current_day}"
    current_obj = current_q.objective if current_q else "General technical objective"
    current_text = current_q.text if current_q else ""
    current_purpose = current_q.purpose if current_q else "concept"
    current_difficulty = current_q.difficulty if current_q else "intermediate"

    planned_q = (
        session.interview_plan.questions[min(session.plan_cursor, len(session.interview_plan.questions) - 1)]
        if session.interview_plan and session.interview_plan.questions
        else None
    )
    planned_day = planned_q.curriculum_day if planned_q else current_day
    planned_day_obj = get_day(planned_day)
    planned_topic = planned_day_obj.title if planned_day_obj else f"Day {planned_day}"
    planned_objective = planned_q.objective if planned_q else "General objective"

    recent = session.conversation[-4:] if session.conversation else []
    recent_history = "\n".join(f"{msg.role}: {msg.content}" for msg in recent)

    profile_json = (
        session.candidate_profile.model_dump_json(indent=2)
        if session.candidate_profile
        else "{}"
    )

    prompt = ADAPTIVE_TURN_USER_TEMPLATE.format(
        profile_json=profile_json,
        current_day=current_day,
        current_topic=current_topic,
        current_objective=current_obj,
        current_text=current_text,
        current_purpose=current_purpose,
        current_difficulty=current_difficulty,
        candidate_answer=candidate_answer,
        recent_history=recent_history,
        question_count=session.question_count,
        covered_days=len(set(session.used_curriculum_days)),
        consecutive_follow_ups=session.consecutive_follow_ups,
        max_follow_ups=MAX_CONSECUTIVE_FOLLOW_UPS,
        planned_day=planned_day,
        planned_topic=planned_topic,
        planned_objective=planned_objective,
        curriculum_detail=build_curriculum_detail(),
    )

    for validation_attempt in range(2):
        try:
            result = generate_with_retry(
                llm,
                prompt,
                InterviewTurnResult,
                system_instruction=ADAPTIVE_TURN_SYSTEM,
            )
            validate_turn_result(result)
            return result
        except LLMError:
            logger.warning("Adaptive turn LLM failed; using fallback turn result.")
            return _fallback_turn_result(session, candidate_answer)
        except ValueError as exc:
            logger.warning(
                "Adaptive turn validation failed (attempt %s): %s",
                validation_attempt + 1,
                exc,
            )
            if validation_attempt == 1:
                break

    logger.warning("Adaptive turn invalid after retry; using fallback turn result.")
    return _fallback_turn_result(session, candidate_answer)


def _fallback_ai_feedback(session: InterviewSession) -> Feedback:
    first_name = get_first_name(session.candidate)
    evals = session.evaluations
    unique_days = list(dict.fromkeys(session.used_curriculum_days))
    highlighted = ", ".join(title_for_day(day) for day in unique_days[:3])

    summary = (
        f"{first_name} completed a personalized technical interview covering "
        f"{len(unique_days)} curriculum areas, including {highlighted}."
    )

    strengths: list[str] = []
    gaps: list[str] = []

    if evals:
        high_scores = [e for e in evals if e.correctness >= 7]
        low_scores = [e for e in evals if e.correctness < 7]
        for e in high_scores:
            strengths.extend(e.strengths)
        for e in low_scores:
            gaps.extend(e.weaknesses)

    if not strengths:
        strengths.append(f"Completed {len(evals)} evaluated interview turns with active engagement.")
        strengths.append(f"Demonstrated solid familiarity with curriculum day {unique_days[0] if unique_days else 1}.")
    if not gaps:
        gaps.append("Practice articulating architectural trade-offs with concrete examples.")

    next_steps: list[str] = []
    if session.candidate_profile and session.candidate_profile.recommended_focus_areas:
        for area in session.candidate_profile.recommended_focus_areas[:2]:
            next_steps.append(f"Review Day {area.day}: {area.title}")
    next_steps.append("Build hands-on project examples to reinforce retrieval and system design concepts.")

    return Feedback(
        summary=summary,
        strengths=strengths[:3],
        gaps=gaps[:3],
        next=next_steps[:3],
    )


def generate_ai_feedback(
    session: InterviewSession,
    llm: LLMService | None = None,
) -> Feedback:
    if llm is None:
        return _fallback_ai_feedback(session)

    evals_summary_lines: list[str] = []
    for idx, eval_item in enumerate(session.evaluations, 1):
        evals_summary_lines.append(
            f"Turn {idx}: correctness={eval_item.correctness}/10, depth={eval_item.depth}/10, "
            f"strengths={eval_item.strengths}, weaknesses={eval_item.weaknesses}, misconception={eval_item.misconception}"
        )
    evaluations_summary = "\n".join(evals_summary_lines) if evals_summary_lines else "No structured evaluations recorded."

    full_conversation_lines = [f"{msg.role}: {msg.content}" for msg in session.conversation]
    full_conversation = "\n".join(full_conversation_lines)

    profile_json = (
        session.candidate_profile.model_dump_json(indent=2)
        if session.candidate_profile
        else "{}"
    )

    prompt = FINAL_FEEDBACK_USER_TEMPLATE.format(
        profile_json=profile_json,
        total_questions=session.question_count,
        covered_days=len(set(session.used_curriculum_days)),
        evaluations_summary=evaluations_summary,
        full_conversation=full_conversation,
    )

    try:
        feedback = generate_with_retry(
            llm,
            prompt,
            Feedback,
            system_instruction=FINAL_FEEDBACK_SYSTEM,
        )
        return feedback
    except (LLMError, ValueError) as exc:
        logger.warning("Final feedback LLM failed (%s); using fallback feedback.", exc)
        return _fallback_ai_feedback(session)


