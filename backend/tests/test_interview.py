from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.interview.engine import MIN_QUESTIONS
from app.main import app
from app.services.session import session_store

CANDIDATES_PATH = Path(__file__).resolve().parent.parent / "app" / "data" / "candidates.json"


@pytest.fixture(autouse=True)
def clear_sessions() -> None:
    session_store.clear()
    yield
    session_store.clear()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def sample_candidate() -> dict:
    data = json.loads(CANDIDATES_PATH.read_text(encoding="utf-8"))
    return data["candidates"][0]


def test_start_interview(client: TestClient, sample_candidate: dict) -> None:
    response = client.post(
        "/api/interview",
        json={"sessionId": "test-start-1", "candidate": sample_candidate},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["reply"]
    assert body["done"] is False
    assert "feedback" not in body


def test_continue_interview(client: TestClient, sample_candidate: dict) -> None:
    session_id = "test-continue-1"
    start = client.post(
        "/api/interview",
        json={"sessionId": session_id, "candidate": sample_candidate},
    )
    assert start.status_code == 200

    response = client.post(
        "/api/interview",
        json={"sessionId": session_id, "message": "Embeddings map text into vector space."},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["reply"]
    assert body["done"] is False


def test_session_persistence(client: TestClient, sample_candidate: dict) -> None:
    session_id = "test-persistence-1"
    client.post(
        "/api/interview",
        json={"sessionId": session_id, "candidate": sample_candidate},
    )

    for index in range(3):
        response = client.post(
            "/api/interview",
            json={"sessionId": session_id, "message": f"Answer number {index + 1} with enough detail."},
        )
        assert response.status_code == 200
        assert response.json()["done"] is False

    session = session_store.get(session_id)
    candidate_messages = [message for message in session.conversation if message.role == "candidate"]
    assert len(candidate_messages) == 3
    assert session.question_count == 4
    assert session.state.value == "active"


def test_unknown_session(client: TestClient) -> None:
    response = client.post(
        "/api/interview",
        json={"sessionId": "does-not-exist", "message": "hello"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Unknown sessionId"


def test_interview_completion(client: TestClient, sample_candidate: dict) -> None:
    session_id = "test-completion-1"
    client.post(
        "/api/interview",
        json={"sessionId": session_id, "candidate": sample_candidate},
    )

    for index in range(MIN_QUESTIONS - 1):
        response = client.post(
            "/api/interview",
            json={"sessionId": session_id, "message": f"Detailed answer {index + 1}."},
        )
        assert response.status_code == 200
        assert response.json()["done"] is False

    final = client.post(
        "/api/interview",
        json={"sessionId": session_id, "message": "Final detailed answer."},
    )

    assert final.status_code == 200
    body = final.json()
    assert body["done"] is True
    assert body["reply"] == "Interview completed."
    assert "feedback" in body
    assert body["feedback"]["summary"]
    assert isinstance(body["feedback"]["strengths"], list)
    assert isinstance(body["feedback"]["gaps"], list)
    assert isinstance(body["feedback"]["next"], list)


def test_missing_message_on_continuation(client: TestClient, sample_candidate: dict) -> None:
    session_id = "test-missing-message"
    client.post(
        "/api/interview",
        json={"sessionId": session_id, "candidate": sample_candidate},
    )

    response = client.post(
        "/api/interview",
        json={"sessionId": session_id},
    )

    assert response.status_code == 422


def test_invalid_candidate(client: TestClient) -> None:
    response = client.post(
        "/api/interview",
        json={
            "sessionId": "test-invalid-candidate",
            "candidate": {"member": {"id": "X"}, "missions": [], "signals": {}},
        },
    )

    assert response.status_code == 422


def test_completed_session_rejects_continuation(
    client: TestClient, sample_candidate: dict
) -> None:
    session_id = "test-completed-session"
    client.post(
        "/api/interview",
        json={"sessionId": session_id, "candidate": sample_candidate},
    )

    for index in range(MIN_QUESTIONS):
        client.post(
            "/api/interview",
            json={"sessionId": session_id, "message": f"Answer {index + 1}."},
        )

    response = client.post(
        "/api/interview",
        json={"sessionId": session_id, "message": "Another answer."},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Interview is already completed."
