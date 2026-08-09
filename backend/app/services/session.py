from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Literal

from app.ai.schemas import (
    AnswerEvaluation,
    CandidateProfile,
    CurrentQuestion,
    InterviewPlan,
)
from app.schemas.interview import Candidate, ConversationMessage


class SessionState(str, Enum):
    ACTIVE = "active"
    COMPLETED = "completed"


class SessionNotFoundError(LookupError):
    """Raised when no session exists for the given sessionId."""


class SessionAlreadyExistsError(ValueError):
    """Raised when attempting to start a session that already exists."""


class SessionCompletedError(ValueError):
    """Raised when continuing an interview that is already completed."""


@dataclass
class InterviewSession:
    session_id: str
    candidate: Candidate
    conversation: list[ConversationMessage] = field(default_factory=list)
    question_count: int = 0
    planned_days: list[int] = field(default_factory=list)
    state: SessionState = SessionState.ACTIVE
    candidate_profile: CandidateProfile | None = None
    interview_plan: InterviewPlan | None = None
    current_question: CurrentQuestion | None = None
    evaluations: list[AnswerEvaluation] = field(default_factory=list)
    used_curriculum_days: list[int] = field(default_factory=list)
    plan_cursor: int = 0
    consecutive_follow_ups: int = 0

    def append_message(self, role: Literal["interviewer", "candidate"], content: str) -> None:
        self.conversation.append(ConversationMessage(role=role, content=content))


class SessionStore:
    def __init__(self) -> None:
        self._sessions: dict[str, InterviewSession] = {}

    def create(self, session: InterviewSession) -> InterviewSession:
        if session.session_id in self._sessions:
            raise SessionAlreadyExistsError(
                f"Session already exists for sessionId '{session.session_id}'."
            )
        self._sessions[session.session_id] = session
        return session

    def get(self, session_id: str) -> InterviewSession:
        session = self._sessions.get(session_id)
        if session is None:
            raise SessionNotFoundError(f"Unknown sessionId '{session_id}'.")
        return session

    def exists(self, session_id: str) -> bool:
        return session_id in self._sessions

    def clear(self) -> None:
        """Remove all sessions — intended for tests only."""
        self._sessions.clear()


session_store = SessionStore()
