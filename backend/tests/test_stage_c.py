from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.ai.interviewer import analyze_candidate, create_interview_plan, generate_first_question
from app.ai.llm import FakeLLMService, LLMError
from app.ai.schemas import (
    CandidateProfile,
    CurrentQuestion,
    FocusArea,
    InterviewPlan,
    PlannedQuestion,
)
from app.config import get_settings
from app.interview.engine import start_interview
from app.main import app
from app.schemas.interview import Candidate
from app.services.curriculum import get_day
from app.services.session import InterviewSession, session_store

CANDIDATES_PATH = Path(__file__).resolve().parent.parent / "app" / "data" / "candidates.json"


@pytest.fixture(autouse=True)
def clear_state() -> None:
    session_store.clear()
    get_settings.cache_clear()
    yield
    session_store.clear()
    get_settings.cache_clear()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def sarah_candidate() -> Candidate:
    data = json.loads(CANDIDATES_PATH.read_text(encoding="utf-8"))
    return Candidate.model_validate(data["candidates"][0])


@pytest.fixture
def sample_candidate_raw() -> dict:
    data = json.loads(CANDIDATES_PATH.read_text(encoding="utf-8"))
    return data["candidates"][0]


def _build_fake_profile() -> CandidateProfile:
    day_29 = get_day(29)
    assert day_29 is not None
    return CandidateProfile(
        role="Senior Data Engineer",
        experience_level="senior",
        strengths=["First-try completion on Day 7"],
        potential_weaknesses=["Skipped Day 29: Monitoring, Logging & Observability"],
        high_effort_topics=["Day 12: Prompt Engineering Fundamentals"],
        skipped_topics=["Day 29: Monitoring, Logging & Observability"],
        completed_topics=["Day 7: Embeddings Explained"],
        recommended_focus_areas=[
            FocusArea(day=29, title=day_29.title, reason="skipped"),
        ],
    )


def _build_fake_plan() -> InterviewPlan:
    day_numbers = [29, 10, 12, 22, 16, 23, 28, 11]
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
    questions: list[PlannedQuestion] = []
    for index, day_number in enumerate(day_numbers):
        curriculum_day = get_day(day_number)
        assert curriculum_day is not None
        questions.append(
            PlannedQuestion(
                question_number=index + 1,
                curriculum_day=day_number,
                topic=curriculum_day.title,
                objective=curriculum_day.objectives[0],
                purpose=purposes[index],  # type: ignore[arg-type]
                difficulty="intermediate",
            )
        )
    return InterviewPlan(
        total_questions=len(questions),
        curriculum_days=sorted(set(day_numbers)),
        questions=questions,
    )


def _build_fake_question() -> CurrentQuestion:
    day_29 = get_day(29)
    assert day_29 is not None
    return CurrentQuestion(
        text="How would you approach configuring alert thresholds for monitoring pipeline health on Day 29?",
        curriculum_day=29,
        objective=day_29.objectives[0],
        purpose="concept",
        difficulty="intermediate",
        is_follow_up=False,
        source="planned",
    )


def _make_fake_llm() -> FakeLLMService:
    return FakeLLMService(
        responses={
            CandidateProfile: _build_fake_profile(),
            InterviewPlan: _build_fake_plan(),
            CurrentQuestion: _build_fake_question(),
        }
    )


class TestStageCAIEngineWiring:
    def test_ai_session_stores_candidate_profile(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-ai-profile", candidate=sarah_candidate)
        llm = _make_fake_llm()
        start_interview(session, llm=llm)

        assert session.candidate_profile is not None
        assert isinstance(session.candidate_profile, CandidateProfile)
        assert session.candidate_profile.role == "Senior Data Engineer"

    def test_ai_session_stores_interview_plan(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-ai-plan", candidate=sarah_candidate)
        llm = _make_fake_llm()
        start_interview(session, llm=llm)

        assert session.interview_plan is not None
        assert isinstance(session.interview_plan, InterviewPlan)
        assert len(session.interview_plan.questions) == 8

    def test_ai_session_stores_current_question(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-ai-q", candidate=sarah_candidate)
        llm = _make_fake_llm()
        start_interview(session, llm=llm)

        assert session.current_question is not None
        assert isinstance(session.current_question, CurrentQuestion)
        assert session.current_question.source == "planned"
        assert session.current_question.is_follow_up is False

    def test_current_question_contains_real_question_text(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-ai-text", candidate=sarah_candidate)
        llm = _make_fake_llm()
        start_interview(session, llm=llm)

        assert session.current_question is not None
        assert len(session.current_question.text) > 10
        assert "monitoring" in session.current_question.text.lower()

    def test_current_question_references_valid_curriculum_day(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-ai-day", candidate=sarah_candidate)
        llm = _make_fake_llm()
        start_interview(session, llm=llm)

        assert session.current_question is not None
        assert get_day(session.current_question.curriculum_day) is not None
        assert session.current_question.curriculum_day == 29

    def test_used_curriculum_days_contains_first_question_day(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-ai-used-days", candidate=sarah_candidate)
        llm = _make_fake_llm()
        start_interview(session, llm=llm)

        assert session.used_curriculum_days == [29]

    def test_first_question_counted_correctly(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-ai-count", candidate=sarah_candidate)
        llm = _make_fake_llm()
        start_interview(session, llm=llm)

        assert session.question_count == 1
        assert session.plan_cursor == 1

    def test_candidate_analysis_happens_once_at_initialization(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-ai-analysis-once", candidate=sarah_candidate)
        llm = _make_fake_llm()
        start_interview(session, llm=llm)

        profile_calls = [call for call in llm.calls if call[0] is CandidateProfile]
        assert len(profile_calls) == 1

    def test_planning_happens_once_at_initialization(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-ai-plan-once", candidate=sarah_candidate)
        llm = _make_fake_llm()
        start_interview(session, llm=llm)

        plan_calls = [call for call in llm.calls if call[0] is InterviewPlan]
        assert len(plan_calls) == 1

    def test_first_question_generation_happens_once_at_initialization(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-ai-q-once", candidate=sarah_candidate)
        llm = _make_fake_llm()
        start_interview(session, llm=llm)

        q_calls = [call for call in llm.calls if call[0] is CurrentQuestion]
        assert len(q_calls) == 1

    def test_gemini_failure_uses_safe_fallback(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-ai-fallback", candidate=sarah_candidate)
        # Empty FakeLLMService raises LLMError for all schemas
        llm = FakeLLMService(responses={})
        response = start_interview(session, llm=llm)

        assert response.done is False
        assert response.reply
        assert session.candidate_profile is not None
        assert session.interview_plan is not None
        assert session.current_question is not None
        assert session.question_count == 1
        assert session.plan_cursor == 1
        assert session.used_curriculum_days == [session.current_question.curriculum_day]

    def test_ai_disabled_follows_existing_mock_behavior(
        self, monkeypatch: pytest.MonkeyPatch, client: TestClient, sample_candidate_raw: dict
    ) -> None:
        monkeypatch.setenv("AI_ENABLED", "false")
        get_settings.cache_clear()

        response = client.post(
            "/api/interview",
            json={"sessionId": "test-mock-start", "candidate": sample_candidate_raw},
        )

        assert response.status_code == 200
        body = response.json()
        assert body["done"] is False
        assert "Welcome, Sarah." in body["reply"]
        assert "feedback" not in body

        session = session_store.get("test-mock-start")
        assert session.candidate_profile is None
        assert session.interview_plan is None
        assert session.current_question is None

    def test_ai_enabled_public_api_response_shape(
        self, monkeypatch: pytest.MonkeyPatch, client: TestClient, sample_candidate_raw: dict
    ) -> None:
        monkeypatch.setenv("AI_ENABLED", "true")
        get_settings.cache_clear()

        # Without API key set, start flow uses rule-based fallback gracefully
        response = client.post(
            "/api/interview",
            json={"sessionId": "test-ai-api-start", "candidate": sample_candidate_raw},
        )

        assert response.status_code == 200
        body = response.json()
        assert "reply" in body
        assert body["done"] is False
        assert "feedback" not in body
        assert "api_key" not in json.dumps(body).lower()

    def test_stage_d_adaptive_evaluation_not_implemented(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-stage-d-check", candidate=sarah_candidate)
        llm = _make_fake_llm()
        start_interview(session, llm=llm)

        assert session.evaluations == []
        assert session.consecutive_follow_ups == 0
