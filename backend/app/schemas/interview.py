from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class CandidateMember(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    jobRole: str = Field(min_length=1)
    yearsExperience: int = Field(ge=0)
    education: str = Field(min_length=1)
    status: str | None = None


class CandidateMission(BaseModel):
    model_config = ConfigDict(extra="forbid")

    day: int = Field(ge=1)
    title: str | None = None
    passed: bool | None = None
    skipped: bool | None = None
    attempts: int | None = Field(default=None, ge=1)


class CandidateSignals(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commitDays: int = Field(ge=0)
    missionsCompleted: int = Field(ge=0)
    missionsFirstTry: int = Field(ge=0)


class Candidate(BaseModel):
    """Raw candidate object as sent by the frontend (single entry from candidates.json)."""

    model_config = ConfigDict(extra="forbid")

    member: CandidateMember
    missions: list[CandidateMission] = Field(min_length=1)
    signals: CandidateSignals


class InterviewStartRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sessionId: str = Field(min_length=1)
    candidate: Candidate


class InterviewContinueRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sessionId: str = Field(min_length=1)
    message: str = Field(min_length=1)


class InterviewRequest(BaseModel):
    """Accepts either a start payload (candidate) or a continuation payload (message)."""

    model_config = ConfigDict(extra="forbid")

    sessionId: str = Field(min_length=1)
    candidate: Candidate | None = None
    message: str | None = None

    @model_validator(mode="after")
    def validate_shape(self) -> InterviewRequest:
        has_candidate = self.candidate is not None
        has_message = self.message is not None

        if has_candidate and has_message:
            raise ValueError("Provide either candidate or message, not both.")
        if not has_candidate and not has_message:
            raise ValueError("Provide either candidate to start or message to continue.")
        if has_message and not self.message.strip():
            raise ValueError("Message cannot be empty.")

        return self

    def as_start(self) -> InterviewStartRequest:
        if self.candidate is None:
            raise ValueError("Not a start request.")
        return InterviewStartRequest(sessionId=self.sessionId, candidate=self.candidate)

    def as_continue(self) -> InterviewContinueRequest:
        if self.message is None:
            raise ValueError("Not a continuation request.")
        return InterviewContinueRequest(sessionId=self.sessionId, message=self.message.strip())


class Feedback(BaseModel):
    summary: str
    strengths: list[str]
    gaps: list[str]
    next: list[str]


class InterviewResponse(BaseModel):
    reply: str
    done: bool
    feedback: Feedback | None = None


class ConversationMessage(BaseModel):
    role: Literal["interviewer", "candidate"]
    content: str
