from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.interview.engine import continue_interview, plan_interview_days, start_interview
from app.schemas.interview import InterviewRequest, InterviewResponse
from app.services.candidate import CandidateValidationError, validate_candidate
from app.services.session import InterviewSession, SessionNotFoundError, session_store

router = APIRouter()


@router.post(
    "/interview",
    response_model=InterviewResponse,
    response_model_exclude_none=True,
)
def post_interview(request: InterviewRequest) -> InterviewResponse:
    if request.candidate is not None:
        return _handle_start(request)
    return _handle_continue(request)


def _handle_start(request: InterviewRequest) -> InterviewResponse:
    start_request = request.as_start()

    try:
        candidate = validate_candidate(start_request.candidate)
    except CandidateValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    if session_store.exists(start_request.sessionId):
        raise HTTPException(
            status_code=409,
            detail=f"Session already exists for sessionId '{start_request.sessionId}'.",
        )

    planned_days = plan_interview_days(candidate)
    session = InterviewSession(
        session_id=start_request.sessionId,
        candidate=candidate,
        planned_days=planned_days,
    )
    session_store.create(session)
    return start_interview(session)


def _handle_continue(request: InterviewRequest) -> InterviewResponse:
    continue_request = request.as_continue()

    try:
        session = session_store.get(continue_request.sessionId)
    except SessionNotFoundError as exc:
        raise HTTPException(status_code=404, detail="Unknown sessionId") from exc

    if session.state.value == "completed":
        raise HTTPException(status_code=400, detail="Interview is already completed.")

    return continue_interview(session, continue_request.message)
