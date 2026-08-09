from __future__ import annotations

import json
from pathlib import Path

import pytest

from app.ai.interviewer import (
    analyze_candidate,
    build_candidate_facts,
    create_interview_plan,
    validate_interview_plan,
)
from app.ai.llm import FakeLLMService, LLMError, generate_with_retry
from app.ai.schemas import (
    MIN_PLAN_CURRICULUM_DAYS,
    MIN_PLAN_QUESTIONS,
    CandidateProfile,
    InterviewPlan,
    PlannedQuestion,
)
from app.schemas.interview import Candidate
from app.services.curriculum import get_day, title_for_day

CANDIDATES_PATH = Path(__file__).resolve().parent.parent / "app" / "data" / "candidates.json"


@pytest.fixture
def sarah_candidate() -> Candidate:
    data = json.loads(CANDIDATES_PATH.read_text(encoding="utf-8"))
    return Candidate.model_validate(data["candidates"][0])


@pytest.fixture
def alex_candidate() -> Candidate:
    data = json.loads(CANDIDATES_PATH.read_text(encoding="utf-8"))
    return Candidate.model_validate(data["candidates"][1])


def _sample_profile(candidate: Candidate) -> CandidateProfile:
    return analyze_candidate(candidate, llm=None)


def _build_fake_plan(candidate: Candidate, profile: CandidateProfile) -> InterviewPlan:
    """Build a valid plan aligned with curriculum for FakeLLMService."""
    day_numbers = [7, 10, 12, 22, 16, 23, 28, 11]
    questions: list[PlannedQuestion] = []
    purposes = [
        "concept",
        "application",
        "reasoning",
        "trade-off",
        "scenario",
        "explanation",
        "concept",
        "application",
    ]
    focus_day = 29 if profile.skipped_topics else day_numbers[0]

    for index, day_number in enumerate(day_numbers):
        curriculum_day = get_day(day_number)
        assert curriculum_day is not None
        effective_day = focus_day if index == 0 and profile.skipped_topics else day_number
        effective_curriculum_day = get_day(effective_day)
        assert effective_curriculum_day is not None
        questions.append(
            PlannedQuestion(
                question_number=index + 1,
                curriculum_day=effective_day,
                topic=effective_curriculum_day.title,
                objective=effective_curriculum_day.objectives[0],
                purpose=purposes[index],  # type: ignore[arg-type]
                difficulty="intermediate",
            )
        )

    return InterviewPlan(
        total_questions=len(questions),
        curriculum_days=sorted({question.curriculum_day for question in questions}),
        questions=questions,
    )


class TestCandidateFacts:
    def test_build_candidate_facts_uses_real_mission_data(self, sarah_candidate: Candidate) -> None:
        facts = build_candidate_facts(sarah_candidate)

        assert facts["role"] == "Senior Data Engineer"
        assert facts["years_experience"] == 9
        assert len(facts["missions"]) == len(sarah_candidate.missions)
        assert any(mission["skipped"] for mission in facts["missions"])
        assert facts["skipped_missions"][0]["day"] == 29

    def test_facts_do_not_invent_missions(self, sarah_candidate: Candidate) -> None:
        facts = build_candidate_facts(sarah_candidate)
        mission_days = {mission.day for mission in sarah_candidate.missions}
        assert set(facts["mission_days"]) == mission_days


class TestCandidateAnalysis:
    def test_fallback_analysis_derives_strengths_from_data(self, sarah_candidate: Candidate) -> None:
        profile = analyze_candidate(sarah_candidate, llm=None)

        assert profile.role == "Senior Data Engineer"
        assert profile.experience_level == "senior"
        assert profile.strengths
        assert any("first-try" in strength.lower() or "First-try" in strength for strength in profile.strengths)

    def test_fallback_analysis_identifies_skipped_topics(self, sarah_candidate: Candidate) -> None:
        profile = analyze_candidate(sarah_candidate, llm=None)

        assert profile.skipped_topics
        assert any("29" in topic for topic in profile.skipped_topics)
        assert profile.potential_weaknesses
        assert any("29" in weakness or "Monitoring" in weakness for weakness in profile.potential_weaknesses)

    def test_fallback_analysis_identifies_high_effort_topics(self, alex_candidate: Candidate) -> None:
        profile = analyze_candidate(alex_candidate, llm=None)

        assert profile.high_effort_topics
        assert len(profile.high_effort_topics) >= 1

    def test_llm_analysis_returns_structured_profile(self, sarah_candidate: Candidate) -> None:
        fake_profile = CandidateProfile(
            role="Senior Data Engineer",
            experience_level="senior",
            strengths=["First-try on Embeddings Explained"],
            potential_weaknesses=["Skipped Monitoring, Logging & Observability"],
            high_effort_topics=["Day 12: Prompt Engineering Fundamentals"],
            skipped_topics=["Day 29: Monitoring, Logging & Observability"],
            completed_topics=["Day 7: Embeddings Explained"],
            recommended_focus_areas=[
                "Day 29: Monitoring, Logging & Observability",
                "Day 12: Prompt Engineering Fundamentals",
            ],
        )
        llm = FakeLLMService(responses={CandidateProfile: fake_profile})
        profile = analyze_candidate(sarah_candidate, llm=llm)

        assert profile.role == "Senior Data Engineer"
        assert profile.recommended_focus_areas
        assert len(llm.calls) == 1
        assert llm.calls[0][0] is CandidateProfile

    def test_llm_failure_falls_back_gracefully(self, sarah_candidate: Candidate) -> None:
        llm = FakeLLMService(responses={})
        profile = analyze_candidate(sarah_candidate, llm=llm)

        assert profile.role == sarah_candidate.member.jobRole
        assert profile.strengths


class TestInterviewPlanning:
    def test_fallback_plan_has_minimum_questions(self, sarah_candidate: Candidate) -> None:
        profile = _sample_profile(sarah_candidate)
        plan = create_interview_plan(sarah_candidate, profile, llm=None)

        assert plan.total_questions >= MIN_PLAN_QUESTIONS
        assert len(plan.questions) >= MIN_PLAN_QUESTIONS

    def test_fallback_plan_covers_minimum_curriculum_days(self, sarah_candidate: Candidate) -> None:
        profile = _sample_profile(sarah_candidate)
        plan = create_interview_plan(sarah_candidate, profile, llm=None)

        unique_days = {question.curriculum_day for question in plan.questions}
        assert len(unique_days) >= MIN_PLAN_CURRICULUM_DAYS
        assert len(set(plan.curriculum_days)) >= MIN_PLAN_CURRICULUM_DAYS

    def test_plan_questions_grounded_in_curriculum(self, sarah_candidate: Candidate) -> None:
        profile = _sample_profile(sarah_candidate)
        plan = create_interview_plan(sarah_candidate, profile, llm=None)

        for question in plan.questions:
            curriculum_day = get_day(question.curriculum_day)
            assert curriculum_day is not None
            assert question.topic == curriculum_day.title
            assert question.objective in curriculum_day.objectives

    def test_plan_includes_required_question_types(self, sarah_candidate: Candidate) -> None:
        profile = _sample_profile(sarah_candidate)
        plan = create_interview_plan(sarah_candidate, profile, llm=None)

        purposes = {question.purpose for question in plan.questions}
        assert purposes & {"application", "scenario"}
        assert purposes & {"reasoning", "trade-off"}

    def test_weaknesses_influence_fallback_plan(self, sarah_candidate: Candidate) -> None:
        profile = analyze_candidate(sarah_candidate, llm=None)
        plan = create_interview_plan(sarah_candidate, profile, llm=None)

        assert profile.skipped_topics
        first_question = plan.questions[0]
        assert first_question.curriculum_day == 29
        assert "Monitoring" in first_question.topic

    def test_llm_plan_generation(self, sarah_candidate: Candidate) -> None:
        profile = _sample_profile(sarah_candidate)
        fake_plan = _build_fake_plan(sarah_candidate, profile)
        llm = FakeLLMService(responses={InterviewPlan: fake_plan})

        plan = create_interview_plan(sarah_candidate, profile, llm=llm)

        assert plan.total_questions >= MIN_PLAN_QUESTIONS
        validate_interview_plan(plan)
        assert len(llm.calls) == 1

    def test_llm_plan_failure_uses_fallback(self, sarah_candidate: Candidate) -> None:
        profile = _sample_profile(sarah_candidate)
        llm = FakeLLMService(responses={})

        plan = create_interview_plan(sarah_candidate, profile, llm=llm)

        assert plan.total_questions >= MIN_PLAN_QUESTIONS
        validate_interview_plan(plan)


class TestPlanValidation:
    def test_rejects_invalid_curriculum_day(self, sarah_candidate: Candidate) -> None:
        profile = _sample_profile(sarah_candidate)
        plan = create_interview_plan(sarah_candidate, profile, llm=None)
        invalid = plan.model_copy(
            update={
                "questions": [
                    question.model_copy(update={"curriculum_day": 999})
                    if question.question_number == 1
                    else question
                    for question in plan.questions
                ]
            }
        )

        with pytest.raises(ValueError, match="invalid curriculum day"):
            validate_interview_plan(invalid)

    def test_rejects_missing_question_types(self, sarah_candidate: Candidate) -> None:
        profile = _sample_profile(sarah_candidate)
        plan = create_interview_plan(sarah_candidate, profile, llm=None)
        invalid_questions = [
            question.model_copy(update={"purpose": "concept"}) for question in plan.questions
        ]
        invalid = plan.model_copy(update={"questions": invalid_questions})

        with pytest.raises(ValueError, match="application/scenario"):
            validate_interview_plan(invalid)


class TestLLMRetry:
    def test_generate_with_retry_reraises_after_exhausted_attempts(self) -> None:
        class FailingLLM(FakeLLMService):
            def generate_structured(self, prompt, schema, *, system_instruction=None):
                raise LLMError("always fails")

        with pytest.raises(LLMError, match="after retries"):
            generate_with_retry(
                FailingLLM(),
                "prompt",
                CandidateProfile,
                retries=1,
            )
