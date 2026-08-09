from __future__ import annotations

import json
import logging
from typing import Any

from app.ai.llm import LLMError, LLMService, generate_with_retry
from app.ai.prompts.candidate_analysis import (
    CANDIDATE_ANALYSIS_SYSTEM,
    CANDIDATE_ANALYSIS_USER_TEMPLATE,
)
from app.ai.prompts.planning import PLANNING_SYSTEM, PLANNING_USER_TEMPLATE
from app.ai.schemas import (
    CandidateProfile,
    FocusArea,
    InterviewPlan,
    PlannedQuestion,
)
from app.interview.constants import MIN_QUESTIONS, MIN_UNIQUE_DAYS
from app.schemas.interview import Candidate
from app.services.candidate import (
    get_completed_days,
    get_difficult_missions,
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
