from app.ai.interviewer import (
    analyze_candidate,
    create_interview_plan,
    evaluate_turn_and_generate_next,
    generate_ai_feedback,
    generate_first_question,
)
from app.ai.llm import LLMError, LLMService, get_llm_service
from app.ai.schemas import CurrentQuestion
from app.config import get_settings
from app.interview.constants import (
    MAX_CONSECUTIVE_FOLLOW_UPS,
    MAX_QUESTIONS,
    MIN_QUESTIONS,
    MIN_UNIQUE_DAYS,
)
from app.schemas.interview import Candidate, Feedback, InterviewResponse
from app.services.candidate import (
    get_difficult_missions,
    get_first_name,
    get_first_try_missions,
    get_mission_days,
    get_skipped_missions,
)
from app.services.curriculum import get_all_days, get_day, title_for_day
from app.services.session import InterviewSession, SessionState


def _deterministic_offset(candidate_id: str) -> int:
    return sum(ord(character) for character in candidate_id)


def plan_interview_days(candidate: Candidate) -> list[int]:
    """Build a deterministic 8-day plan tailored to the candidate's mission history."""
    skipped_days = [mission.day for mission in get_skipped_missions(candidate)]
    difficult_days = [mission.day for mission in get_difficult_missions(candidate)]
    first_try_days = [mission.day for mission in get_first_try_missions(candidate)]
    mission_days = get_mission_days(candidate)
    curriculum_days = [day.day for day in get_all_days()]

    priority: list[int] = []
    for day in skipped_days + difficult_days + first_try_days + mission_days + curriculum_days:
        if day not in priority:
            priority.append(day)

    if not priority:
        priority = curriculum_days

    rotate_by = _deterministic_offset(candidate.member.id) % len(priority)
    priority = priority[rotate_by:] + priority[:rotate_by]

    planned: list[int] = []
    unique_days: set[int] = set()

    for day in priority:
        if day not in unique_days:
            planned.append(day)
            unique_days.add(day)
        if len(unique_days) >= MIN_UNIQUE_DAYS and len(planned) >= MIN_UNIQUE_DAYS:
            break

    index = 0
    while len(planned) < MIN_QUESTIONS:
        planned.append(priority[index % len(priority)])
        index += 1

    return planned[:MIN_QUESTIONS]


def _question_for_day(day_number: int, candidate: Candidate, question_index: int) -> str:
    day = get_day(day_number)
    if day is None:
        return (
            f"Curriculum day {day_number}: describe a key concept you learned "
            "and how you would apply it."
        )

    objective_index = question_index % len(day.objectives)
    tool_index = question_index % len(day.tools) if day.tools else 0
    objective = day.objectives[objective_index]
    tool = day.tools[tool_index] if day.tools else "the relevant tools"

    templates = [
        (
            f"Regarding Day {day.day} ({day.title}): {objective} "
            "How would you explain your approach in a technical interview?"
        ),
        (
            f"On {day.title}, we used {tool}. "
            "Walk me through how you would apply it in a real project."
        ),
        (
            f"For curriculum day {day.day} ({day.type}), "
            f"what is the most important takeaway from: \"{objective}\"?"
        ),
    ]
    template_index = (_deterministic_offset(candidate.member.id) + question_index) % len(templates)
    return templates[template_index]


def _generate_feedback(session: InterviewSession) -> Feedback:
    candidate = session.candidate
    first_name = get_first_name(session.candidate)
    skipped = get_skipped_missions(candidate)
    difficult = get_difficult_missions(candidate)
    first_try = get_first_try_missions(candidate)

    unique_days = list(dict.fromkeys(session.planned_days))
    highlighted = ", ".join(title_for_day(day) for day in unique_days[:3])

    summary = (
        f"{first_name} completed an {MIN_QUESTIONS}-question interview covering "
        f"{len(unique_days)} curriculum areas, including {highlighted}."
    )

    strengths: list[str] = []
    if first_try:
        strengths.append(
            f"Strong first-try performance on {title_for_day(first_try[0].day)}"
        )
    strengths.append(f"Completed {candidate.signals.missionsCompleted} curriculum missions")
    if candidate.signals.missionsFirstTry >= 10:
        strengths.append("Consistent first-attempt success across missions")
    if not strengths:
        strengths.append("Engaged thoughtfully across all interview questions")

    gaps: list[str] = []
    if skipped:
        gaps.append(f"Skipped mission: {title_for_day(skipped[0].day)}")
    if difficult:
        gaps.append(
            f"Multiple attempts needed on {title_for_day(difficult[0].day)}"
        )
    gaps.append("Practice articulating trade-offs with concrete examples")

    next_steps: list[str] = []
    if skipped:
        next_steps.append(
            f"Review curriculum day {skipped[0].day}: {title_for_day(skipped[0].day)}"
        )
    if difficult:
        next_steps.append(f"Deepen understanding of {title_for_day(difficult[0].day)}")
    next_steps.append("Practice explaining retrieval and RAG concepts with a real use case")

    return Feedback(
        summary=summary,
        strengths=strengths[:3],
        gaps=gaps[:3],
        next=next_steps[:3],
    )


def start_interview(
    session: InterviewSession,
    llm: LLMService | None = None,
) -> InterviewResponse:
    settings = get_settings()
    is_ai = settings.ai_enabled or llm is not None

    if is_ai:
        if llm is None and settings.ai_enabled:
            try:
                llm = get_llm_service(settings)
            except LLMError:
                llm = None

        profile = analyze_candidate(session.candidate, llm)
        plan = create_interview_plan(session.candidate, profile, llm)
        first_question = generate_first_question(session.candidate, profile, plan, llm)

        session.candidate_profile = profile
        session.interview_plan = plan
        session.current_question = first_question
        session.used_curriculum_days = [first_question.curriculum_day]
        # planned_days is populated for backward compatibility with existing mock/session code only
        session.planned_days = [question.curriculum_day for question in plan.questions]
        session.plan_cursor = 1  # index of the next unused planned question
        session.question_count = 1

        first_name = get_first_name(session.candidate)
        welcome = f"Welcome, {first_name}. Let's begin your personalized technical interview."
        reply = f"{welcome}\n\n{first_question.text}"

        session.append_message("interviewer", welcome)
        session.append_message("interviewer", first_question.text)

        return InterviewResponse(reply=reply, done=False)

    # Mock mode
    first_name = get_first_name(session.candidate)
    welcome = f"Welcome, {first_name}. Let's begin your personalized technical interview."

    day_number = session.planned_days[0]
    question = _question_for_day(day_number, session.candidate, 0)
    reply = f"{welcome}\n\n{question}"

    session.append_message("interviewer", welcome)
    session.append_message("interviewer", question)
    session.question_count = 1

    return InterviewResponse(reply=reply, done=False)


def continue_interview(
    session: InterviewSession,
    message: str,
    llm: LLMService | None = None,
) -> InterviewResponse:
    if session.state == SessionState.COMPLETED:
        raise ValueError("Interview is already completed.")

    session.append_message("candidate", message)

    settings = get_settings()
    is_ai = settings.ai_enabled or llm is not None or session.interview_plan is not None

    if is_ai:
        if llm is None and settings.ai_enabled:
            try:
                llm = get_llm_service(settings)
            except LLMError:
                llm = None

        unique_days_count = len(set(session.used_curriculum_days))
        should_complete = (session.question_count >= MAX_QUESTIONS) or (
            session.question_count >= MIN_QUESTIONS and unique_days_count >= MIN_UNIQUE_DAYS
        )

        if should_complete:
            session.state = SessionState.COMPLETED
            closing = "Interview completed."
            session.append_message("interviewer", closing)
            feedback = generate_ai_feedback(session, llm)
            return InterviewResponse(
                reply=closing,
                done=True,
                feedback=feedback,
            )

        turn_result = evaluate_turn_and_generate_next(session, message, llm)
        session.evaluations.append(turn_result.evaluation)

        is_follow_up = turn_result.is_follow_up
        if is_follow_up:
            if session.consecutive_follow_ups >= MAX_CONSECUTIVE_FOLLOW_UPS:
                is_follow_up = False
                session.consecutive_follow_ups = 0
            else:
                session.consecutive_follow_ups += 1
        else:
            session.consecutive_follow_ups = 0

        curr_day = turn_result.curriculum_day
        curr_obj = turn_result.objective
        curr_purpose = turn_result.purpose
        curr_diff = turn_result.difficulty

        if len(set(session.used_curriculum_days)) < MIN_UNIQUE_DAYS:
            if not is_follow_up and curr_day in session.used_curriculum_days:
                uncovered_q = None
                if session.interview_plan:
                    for q in session.interview_plan.questions:
                        if q.curriculum_day not in session.used_curriculum_days:
                            uncovered_q = q
                            break
                if uncovered_q is not None:
                    curr_day = uncovered_q.curriculum_day
                    curr_obj = uncovered_q.objective
                    curr_purpose = uncovered_q.purpose
                    curr_diff = uncovered_q.difficulty

        next_question = CurrentQuestion(
            text=turn_result.question_text,
            curriculum_day=curr_day,
            objective=curr_obj,
            purpose=curr_purpose,
            difficulty=curr_diff,
            is_follow_up=is_follow_up,
            source="adaptive" if is_follow_up else "planned",
        )

        session.current_question = next_question
        if curr_day not in session.used_curriculum_days:
            session.used_curriculum_days.append(curr_day)
        session.question_count += 1
        if not is_follow_up:
            session.plan_cursor += 1

        session.append_message("interviewer", next_question.text)
        return InterviewResponse(reply=next_question.text, done=False)

    # Mock mode
    if session.question_count >= MIN_QUESTIONS:
        session.state = SessionState.COMPLETED
        closing = "Interview completed."
        session.append_message("interviewer", closing)
        return InterviewResponse(
            reply=closing,
            done=True,
            feedback=_generate_feedback(session),
        )

    next_index = session.question_count
    day_number = session.planned_days[next_index]
    question = _question_for_day(day_number, session.candidate, next_index)
    session.append_message("interviewer", question)
    session.question_count += 1

    return InterviewResponse(reply=question, done=False)
