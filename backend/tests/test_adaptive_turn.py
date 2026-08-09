from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.ai.llm import FakeLLMService
from app.ai.schemas import (
    AnswerEvaluation,
    CandidateProfile,
    CurrentQuestion,
    FocusArea,
    InterviewPlan,
    InterviewTurnResult,
    PlannedQuestion,
)
from app.config import get_settings
from app.interview.engine import continue_interview, start_interview
from app.main import app
from app.schemas.interview import Candidate, Feedback
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


def _build_fake_first_q() -> CurrentQuestion:
    day_29 = get_day(29)
    assert day_29 is not None
    return CurrentQuestion(
        text="How would you approach configuring alert thresholds on Day 29?",
        curriculum_day=29,
        objective=day_29.objectives[0],
        purpose="concept",
        difficulty="intermediate",
        is_follow_up=False,
        source="planned",
    )


def _build_fake_turn_result(
    day: int = 10,
    is_follow_up: bool = False,
) -> InterviewTurnResult:
    curriculum_day = get_day(day)
    assert curriculum_day is not None
    return InterviewTurnResult(
        evaluation=AnswerEvaluation(
            correctness=8,
            depth=7,
            reasoning=8,
            clarity=8,
            strengths=["Clear architectural explanation"],
            weaknesses=[],
            misconception=None,
            should_follow_up=is_follow_up,
            follow_up_focus=None,
            recommended_difficulty="intermediate",
        ),
        question_text=f"How would you implement the objective for Day {day} ({curriculum_day.title})?",
        curriculum_day=day,
        objective=curriculum_day.objectives[0],
        purpose="application",
        difficulty="intermediate",
        is_follow_up=is_follow_up,
    )


def _build_fake_feedback() -> Feedback:
    return Feedback(
        summary="Sarah demonstrated strong conceptual clarity across curriculum areas.",
        strengths=["Solid knowledge of monitoring and vector embeddings", "Clear trade-off reasoning"],
        gaps=["Could deepen hands-on RAG chunking experience"],
        next=["Review Day 29 monitoring concepts", "Practice building production RAG pipelines"],
    )


def _make_fake_llm(
    turn_result: InterviewTurnResult | None = None,
) -> FakeLLMService:
    t_result = turn_result or _build_fake_turn_result(10, False)
    return FakeLLMService(
        responses={
            CandidateProfile: _build_fake_profile(),
            InterviewPlan: _build_fake_plan(),
            CurrentQuestion: _build_fake_first_q(),
            InterviewTurnResult: t_result,
            Feedback: _build_fake_feedback(),
        }
    )


class TestAdaptiveTurnFlow:
    def test_ai_answer_produces_next_question_and_updates_state(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-turn-1", candidate=sarah_candidate)
        llm = _make_fake_llm(_build_fake_turn_result(10, False))

        # Start AI interview
        start_interview(session, llm=llm)
        assert session.question_count == 1
        assert session.used_curriculum_days == [29]

        # Answer 1
        response = continue_interview(session, "We set metric alerts using Prometheus rules.", llm=llm)

        assert response.done is False
        assert "Day 10" in response.reply
        assert len(session.evaluations) == 1
        assert session.evaluations[0].correctness == 8
        assert session.question_count == 2
        assert session.current_question is not None
        assert session.current_question.curriculum_day == 10
        assert session.used_curriculum_days == [29, 10]

    def test_consecutive_follow_up_limit_enforced(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-follow-up-limit", candidate=sarah_candidate)
        llm = _make_fake_llm(_build_fake_turn_result(29, True))

        start_interview(session, llm=llm)

        # Turn 1: follow-up 1 allowed
        continue_interview(session, "Answer 1", llm=llm)
        assert session.consecutive_follow_ups == 1
        assert session.current_question is not None
        assert session.current_question.is_follow_up is True

        # Turn 2: follow-up 2 allowed
        continue_interview(session, "Answer 2", llm=llm)
        assert session.consecutive_follow_ups == 2
        assert session.current_question is not None
        assert session.current_question.is_follow_up is True

        # Turn 3: Gemini requests another follow-up, but Python OVERRIDES limit!
        continue_interview(session, "Answer 3", llm=llm)
        assert session.consecutive_follow_ups == 0
        assert session.current_question is not None
        assert session.current_question.is_follow_up is False

    def test_minimum_questions_and_coverage_enforced_before_completion(
        self, sarah_candidate: Candidate
    ) -> None:
        session = InterviewSession(session_id="test-min-questions", candidate=sarah_candidate)
        llm = _make_fake_llm(_build_fake_turn_result(10, False))

        start_interview(session, llm=llm)

        # Simulate 6 candidate answers (total question_count reaches 7)
        for i in range(6):
            resp = continue_interview(session, f"Answer {i + 1}", llm=llm)
            assert resp.done is False

        assert session.question_count == 7
        assert session.state.value == "active"

    def test_completion_and_final_feedback_returned(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-completion-ai", candidate=sarah_candidate)

        class DayRotatingLLM(FakeLLMService):
            def __init__(self) -> None:
                super().__init__(
                    responses={
                        CandidateProfile: _build_fake_profile(),
                        InterviewPlan: _build_fake_plan(),
                        CurrentQuestion: _build_fake_first_q(),
                        Feedback: _build_fake_feedback(),
                    }
                )
                self.days = [10, 12, 22, 16, 23, 28, 11]

            def generate_structured(self, prompt, schema, *, system_instruction=None):
                if schema is InterviewTurnResult:
                    day = self.days.pop(0) if self.days else 11
                    return _build_fake_turn_result(day, False)
                return super().generate_structured(prompt, schema, system_instruction=system_instruction)

        llm = DayRotatingLLM()
        start_interview(session, llm=llm)

        # Answer 8 times (answering questions 1 through 8, unique days >= 4)
        for i in range(8):
            resp = continue_interview(session, f"Detailed candidate answer {i + 1}", llm=llm)
            if i < 7:
                assert resp.done is False
            else:
                assert resp.done is True
                assert resp.reply == "Interview completed."
                assert resp.feedback is not None
                assert len(resp.feedback.strengths) >= 1
                assert len(resp.feedback.gaps) >= 1
                assert len(resp.feedback.next) >= 1

        assert session.state.value == "completed"

    def test_maximum_10_questions_hard_cap(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-max-cap", candidate=sarah_candidate)
        # LLM staying on same day to prevent meeting unique days until forced max cap
        llm = _make_fake_llm(_build_fake_turn_result(29, True))
        start_interview(session, llm=llm)

        # Answer 10 times (answering questions 1 through 10)
        for i in range(10):
            resp = continue_interview(session, f"Answer {i + 1}", llm=llm)
            if i < 9:
                assert resp.done is False
            else:
                # Reached 10 questions hard max
                assert resp.done is True
                assert resp.reply == "Interview completed."
                assert resp.feedback is not None

        assert session.state.value == "completed"

    def test_llm_failure_during_turn_uses_fallback(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-turn-fallback", candidate=sarah_candidate)
        # Empty FakeLLMService causes LLMError
        llm = FakeLLMService(responses={})

        start_interview(session, llm=llm)
        resp = continue_interview(session, "Answer with LLM failure", llm=llm)

        assert resp.done is False
        assert resp.reply
        assert len(session.evaluations) == 1
        assert session.question_count == 2

    def test_ai_disabled_mock_continue_remains_intact(
        self, monkeypatch: pytest.MonkeyPatch, client: TestClient, sample_candidate_raw: dict
    ) -> None:
        monkeypatch.setenv("AI_ENABLED", "false")
        get_settings.cache_clear()

        session_id = "test-mock-continue"
        start = client.post(
            "/api/interview",
            json={"sessionId": session_id, "candidate": sample_candidate_raw},
        )
        assert start.status_code == 200

        response = client.post(
            "/api/interview",
            json={"sessionId": session_id, "message": "Mock candidate response"},
        )
        assert response.status_code == 200
        body = response.json()
        assert body["done"] is False
        assert body["reply"]

    def test_end_to_end_adaptive_interview_api_flow(
        self, monkeypatch: pytest.MonkeyPatch, client: TestClient, sample_candidate_raw: dict
    ) -> None:
        monkeypatch.setenv("AI_ENABLED", "true")
        get_settings.cache_clear()

        session_id = "test-e2e-adaptive-api"

        start_res = client.post(
            "/api/interview",
            json={"sessionId": session_id, "candidate": sample_candidate_raw},
        )
        assert start_res.status_code == 200
        start_body = start_res.json()
        assert start_body["done"] is False
        assert start_body["reply"]

        for turn in range(8):
            answer_msg = f"This is candidate answer turn {turn + 1} explaining technical details."
            cont_res = client.post(
                "/api/interview",
                json={"sessionId": session_id, "message": answer_msg},
            )
            assert cont_res.status_code == 200
            cont_body = cont_res.json()

            if turn < 7:
                assert cont_body["done"] is False
                assert "reply" in cont_body
                assert "feedback" not in cont_body
            else:
                assert cont_body["done"] is True
                assert cont_body["reply"] == "Interview completed."
                assert "feedback" in cont_body
                feedback = cont_body["feedback"]
                assert "summary" in feedback
                assert isinstance(feedback["strengths"], list)
                assert isinstance(feedback["gaps"], list)
                assert isinstance(feedback["next"], list)

    def test_adaptive_turn_context_reduction(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-context-reduction", candidate=sarah_candidate)
        llm = _make_fake_llm(_build_fake_turn_result(10, False))

        start_interview(session, llm=llm)
        continue_interview(session, "Answer turn 1", llm=llm)

        # Inspect prompt passed to fake LLM during turn 1
        turn_calls = [call for call in llm.calls if call[0] is InterviewTurnResult]
        assert len(turn_calls) == 1
        prompt_text = turn_calls[0][1]

        # Verify that prompt includes Day 29 and Day 10 details, but NOT all 31 days (e.g. Day 31)
        assert "Day 29" in prompt_text
        assert "Day 10" in prompt_text
        assert "Day 31:" not in prompt_text

    def test_single_attempt_immediate_fallback_on_validation_failure(self, sarah_candidate: Candidate) -> None:
        session = InterviewSession(session_id="test-single-attempt-fallback", candidate=sarah_candidate)
        
        # Turn result with invalid curriculum day (999) to force validation failure
        invalid_turn_result = _build_fake_turn_result(10, False)
        invalid_turn_result.curriculum_day = 999

        llm = FakeLLMService(
            responses={
                CandidateProfile: _build_fake_profile(),
                InterviewPlan: _build_fake_plan(),
                CurrentQuestion: _build_fake_first_q(),
                InterviewTurnResult: invalid_turn_result,
                Feedback: _build_fake_feedback(),
            }
        )

        start_interview(session, llm=llm)
        response = continue_interview(session, "Answer turn 1", llm=llm)

        # Verify exact call count to InterviewTurnResult schema is 1 (no outer retry loop multiplier)
        turn_calls = [call for call in llm.calls if call[0] is InterviewTurnResult]
        assert len(turn_calls) == 1

        # Verify fallback response returned cleanly
        assert response.done is False
        assert response.reply
        assert len(session.evaluations) == 1


