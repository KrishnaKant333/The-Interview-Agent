from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

Difficulty = Literal["foundation", "intermediate", "advanced"]
ExperienceLevel = Literal["junior", "mid", "senior", "lead"]
QuestionPurpose = Literal[
    "concept",
    "explanation",
    "application",
    "reasoning",
    "trade-off",
    "scenario",
    "diagnostic",
]

MIN_PLAN_QUESTIONS = 8
MIN_PLAN_CURRICULUM_DAYS = 4


class CandidateProfile(BaseModel):
    """Internal analysis of a candidate grounded in supplied mission and signal data."""

    model_config = ConfigDict(extra="forbid")

    role: str
    experience_level: ExperienceLevel
    strengths: list[str] = Field(min_length=1)
    potential_weaknesses: list[str] = Field(default_factory=list)
    high_effort_topics: list[str] = Field(default_factory=list)
    skipped_topics: list[str] = Field(default_factory=list)
    completed_topics: list[str] = Field(default_factory=list)
    recommended_focus_areas: list[str] = Field(min_length=1)


class PlannedQuestion(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question_number: int = Field(ge=1)
    curriculum_day: int = Field(ge=1)
    topic: str = Field(min_length=1)
    objective: str = Field(min_length=1)
    purpose: QuestionPurpose
    difficulty: Difficulty


class InterviewPlan(BaseModel):
    model_config = ConfigDict(extra="forbid")

    total_questions: int = Field(ge=MIN_PLAN_QUESTIONS, le=12)
    curriculum_days: list[int] = Field(min_length=MIN_PLAN_CURRICULUM_DAYS)
    questions: list[PlannedQuestion] = Field(min_length=MIN_PLAN_QUESTIONS)

    @field_validator("questions")
    @classmethod
    def questions_match_total(cls, questions: list[PlannedQuestion], info) -> list[PlannedQuestion]:
        total = info.data.get("total_questions")
        if total is not None and len(questions) != total:
            raise ValueError("questions length must equal total_questions")
        return questions

    @field_validator("curriculum_days")
    @classmethod
    def unique_curriculum_days(cls, days: list[int]) -> list[int]:
        if len(set(days)) < MIN_PLAN_CURRICULUM_DAYS:
            raise ValueError(
                f"curriculum_days must include at least {MIN_PLAN_CURRICULUM_DAYS} distinct days"
            )
        return days


class AnswerEvaluation(BaseModel):
    """Structured evaluation of a candidate answer (Phase 2+)."""

    model_config = ConfigDict(extra="forbid")

    correctness: int = Field(ge=0, le=10)
    depth: int = Field(ge=0, le=10)
    reasoning: int = Field(ge=0, le=10)
    clarity: int = Field(ge=0, le=10)
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    misconception: str | None = None
    should_follow_up: bool
    follow_up_focus: str | None = None
    recommended_difficulty: Difficulty
