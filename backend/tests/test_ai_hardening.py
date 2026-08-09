from __future__ import annotations

import json
from pathlib import Path

import pytest
from pydantic import BaseModel, ValidationError

from app.ai.interviewer import (
    analyze_candidate,
    build_candidate_facts,
    validate_candidate_profile,
)
from app.ai.llm import FakeLLMService
from app.ai.schemas import (
    AnswerEvaluation,
    CandidateProfile,
    CurrentQuestion,
    FocusArea,
    InterviewTurnResult,
)
from app.interview.constants import (
    MAX_CONSECUTIVE_FOLLOW_UPS,
    MAX_QUESTIONS,
    MIN_QUESTIONS,
    MIN_UNIQUE_DAYS,
)
from app.schemas.interview import Candidate
from app.services.curriculum import get_day, title_for_day

CANDIDATES_PATH = Path(__file__).resolve().parent.parent / "app" / "data" / "candidates.json"


@pytest.fixture
def sarah_candidate() -> Candidate:
    data = json.loads(CANDIDATES_PATH.read_text(encoding="utf-8"))
    return Candidate.model_validate(data["candidates"][0])


class TestCentralizedConstants:
    def test_interview_constants_values(self) -> None:
        assert MIN_QUESTIONS == 8
        assert MIN_UNIQUE_DAYS == 4
        assert MAX_QUESTIONS == 10
        assert MAX_CONSECUTIVE_FOLLOW_UPS == 2


class TestFocusArea:
    def test_focus_area_model(self) -> None:
        area = FocusArea(day=29, title="Monitoring, Logging & Observability", reason="skipped")
        assert area.day == 29
        assert area.reason == "skipped"

    def test_focus_area_rejects_invalid_reason(self) -> None:
        with pytest.raises(ValidationError):
            FocusArea.model_validate(
                {"day": 29, "title": "Monitoring", "reason": "invented"}
            )


class TestCandidateProfileFocusAreas:
    def test_fallback_profile_uses_structured_focus_areas(self, sarah_candidate: Candidate) -> None:
        profile = analyze_candidate(sarah_candidate, llm=None)

        assert profile.recommended_focus_areas
        assert all(isinstance(area, FocusArea) for area in profile.recommended_focus_areas)
        assert profile.recommended_focus_areas[0].day == 29
        assert profile.recommended_focus_areas[0].reason == "skipped"

    def test_fallback_focus_area_titles_match_curriculum(self, sarah_candidate: Candidate) -> None:
        profile = analyze_candidate(sarah_candidate, llm=None)

        for area in profile.recommended_focus_areas:
            curriculum_day = get_day(area.day)
            assert curriculum_day is not None
            assert area.title == curriculum_day.title


class TestCandidateProfileGrounding:
    def test_valid_profile_passes_validation(self, sarah_candidate: Candidate) -> None:
        facts = build_candidate_facts(sarah_candidate)
        profile = analyze_candidate(sarah_candidate, llm=None)
        validate_candidate_profile(profile, facts)

    def test_rejects_invalid_curriculum_day(self, sarah_candidate: Candidate) -> None:
        facts = build_candidate_facts(sarah_candidate)
        profile = analyze_candidate(sarah_candidate, llm=None)
        invalid = profile.model_copy(
            update={
                "recommended_focus_areas": [
                    FocusArea(day=999, title="Fake Day", reason="other"),
                ]
            }
        )

        with pytest.raises(ValueError, match="invalid curriculum day"):
            validate_candidate_profile(invalid, facts)

    def test_rejects_unsubstantiated_skipped_reason(self, sarah_candidate: Candidate) -> None:
        facts = build_candidate_facts(sarah_candidate)
        profile = analyze_candidate(sarah_candidate, llm=None)
        day_12 = get_day(12)
        assert day_12 is not None
        invalid = profile.model_copy(
            update={
                "recommended_focus_areas": [
                    FocusArea(day=12, title=day_12.title, reason="skipped"),
                ]
            }
        )

        with pytest.raises(ValueError, match="skipped"):
            validate_candidate_profile(invalid, facts)

    def test_rejects_invented_mission_day(self, sarah_candidate: Candidate) -> None:
        facts = build_candidate_facts(sarah_candidate)
        profile = analyze_candidate(sarah_candidate, llm=None)
        day_1 = get_day(1)
        assert day_1 is not None
        invalid = profile.model_copy(
            update={
                "recommended_focus_areas": [
                    FocusArea(day=1, title=day_1.title, reason="other"),
                ]
            }
        )

        with pytest.raises(ValueError, match="not supported by candidate mission data"):
            validate_candidate_profile(invalid, facts)

    def test_invalid_llm_profile_retries_then_succeeds(self, sarah_candidate: Candidate) -> None:
        day_1 = get_day(1)
        assert day_1 is not None
        invalid_profile = CandidateProfile(
            role="Senior Data Engineer",
            experience_level="senior",
            strengths=["Test strength"],
            recommended_focus_areas=[
                FocusArea(day=1, title=day_1.title, reason="other"),
            ],
        )
        valid_profile = CandidateProfile(
            role="Senior Data Engineer",
            experience_level="senior",
            strengths=["First-try on Embeddings Explained"],
            recommended_focus_areas=[
                FocusArea(
                    day=29,
                    title=title_for_day(29),
                    reason="skipped",
                ),
            ],
        )

        class SequentialFakeLLM(FakeLLMService):
            def __init__(self) -> None:
                super().__init__()
                self._profiles = [invalid_profile, valid_profile]

            def generate_structured(
                self,
                prompt: str,
                schema: type[BaseModel],
                *,
                system_instruction: str | None = None,
            ):
                self._on_call.append((schema, prompt))
                if schema is CandidateProfile:
                    return self._profiles.pop(0)
                return super().generate_structured(
                    prompt, schema, system_instruction=system_instruction
                )

        llm = SequentialFakeLLM()
        profile = analyze_candidate(sarah_candidate, llm=llm)

        assert profile.recommended_focus_areas[0].day == 29
        assert len(llm.calls) == 2

    def test_invalid_llm_profile_falls_back_after_retry(self, sarah_candidate: Candidate) -> None:
        day_1 = get_day(1)
        assert day_1 is not None
        invalid_profile = CandidateProfile(
            role="Senior Data Engineer",
            experience_level="senior",
            strengths=["Test strength"],
            recommended_focus_areas=[
                FocusArea(day=1, title=day_1.title, reason="other"),
            ],
        )
        llm = FakeLLMService(responses={CandidateProfile: invalid_profile})
        profile = analyze_candidate(sarah_candidate, llm=llm)

        assert profile.recommended_focus_areas[0].day == 29
        assert profile.recommended_focus_areas[0].reason == "skipped"
        assert len(llm.calls) == 2


class TestCurrentQuestion:
    def test_current_question_model(self) -> None:
        question = CurrentQuestion(
            text="How would you debug irrelevant RAG chunks?",
            curriculum_day=11,
            objective="Build a minimal RAG pipeline",
            purpose="scenario",
            difficulty="intermediate",
            is_follow_up=False,
            source="planned",
        )

        assert question.source == "planned"
        assert question.is_follow_up is False


class TestInterviewTurnResult:
    def test_interview_turn_result_model(self) -> None:
        evaluation = AnswerEvaluation(
            correctness=7,
            depth=6,
            reasoning=7,
            clarity=8,
            should_follow_up=True,
            follow_up_focus="chunking strategy",
            recommended_difficulty="intermediate",
        )
        result = InterviewTurnResult(
            evaluation=evaluation,
            question_text="Can you elaborate on your chunking approach?",
            curriculum_day=11,
            objective="Build a minimal RAG pipeline",
            purpose="reasoning",
            difficulty="intermediate",
            is_follow_up=True,
        )

        assert result.is_follow_up is True
        assert result.evaluation.should_follow_up is True
