# Interview Agent Backend

FastAPI backend for the AI-powered adaptive technical interviewer. This MVP uses a deterministic mock interview engine (no LLM calls) to prove the end-to-end flow with the React frontend.

## Prerequisites

- Python 3.11+
- pip

## Setup

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
```

## Run the API

From the `backend` directory:

```bash
uvicorn app.main:app --reload
```

The API listens on `http://localhost:8000`.

- Swagger UI: http://localhost:8000/docs
- OpenAPI JSON: http://localhost:8000/openapi.json

## Manual verification

### Start an interview

```bash
curl -X POST http://localhost:8000/api/interview ^
  -H "Content-Type: application/json" ^
  -d "{\"sessionId\":\"manual-1\",\"candidate\":{\"member\":{\"id\":\"CAND-001\",\"name\":\"Sarah Johnson\",\"jobRole\":\"Senior Data Engineer\",\"yearsExperience\":9,\"education\":\"MS Computer Science\",\"status\":\"COMPLETED\"},\"missions\":[{\"day\":7,\"title\":\"Embeddings Explained\",\"passed\":true,\"attempts\":1}],\"signals\":{\"commitDays\":28,\"missionsCompleted\":30,\"missionsFirstTry\":20}}}"
```

On macOS/Linux, replace `^` with `\` for line continuation.

### Continue the interview

```bash
curl -X POST http://localhost:8000/api/interview ^
  -H "Content-Type: application/json" ^
  -d "{\"sessionId\":\"manual-1\",\"message\":\"Embeddings represent text as dense vectors for semantic search.\"}"
```

Repeat the continue request until `done` is `true` and `feedback` is returned (8 questions total).

## Run tests

```bash
cd backend
pytest -v
```

## API contract

### `POST /api/interview`

**Start**

```json
{
  "sessionId": "abc-123",
  "candidate": { "...raw candidate object..." }
}
```

**Continue**

```json
{
  "sessionId": "abc-123",
  "message": "Candidate answer"
}
```

**Response (in progress)**

```json
{
  "reply": "...",
  "done": false
}
```

**Response (complete)**

```json
{
  "reply": "Interview completed.",
  "done": true,
  "feedback": {
    "summary": "...",
    "strengths": [],
    "gaps": [],
    "next": []
  }
}
```

## Frontend integration

Set the frontend to live API mode:

```bash
# in frontend/
# Point directly at the FastAPI server (Vite proxy target is not configured for port 8000)
VITE_USE_MOCK=false VITE_API_BASE_URL=http://localhost:8000 npm run dev
```

The Vite dev server (`http://localhost:5173`) is allowed via CORS.

## Project layout

```
backend/
├── app/
│   ├── main.py              # FastAPI app + CORS
│   ├── api/interview.py     # POST /api/interview route
│   ├── schemas/interview.py # Pydantic request/response models
│   ├── services/            # candidate, curriculum, session
│   ├── interview/engine.py  # Deterministic mock interviewer
│   └── data/                # candidates.json, curriculum.json
├── tests/test_interview.py
├── requirements.txt
└── README.md
```

## Data schemas

The API accepts a **single raw candidate object** (not the `candidates.json` wrapper):

- `member`: `{ id, name, jobRole, yearsExperience, education, status? }`
- `missions`: `[{ day, title?, passed?, skipped?, attempts? }]`
- `signals`: `{ commitDays, missionsCompleted, missionsFirstTry }`

Curriculum (`curriculum.json`):

- `cohort`: string
- `modules`: `[{ n, title, days }]`
- `days`: `[{ day, title, type, tools[], objectives[] }]`

## Notes

- Session state is stored in memory and is lost on server restart.
- No authentication, database, or LLM integration in this MVP.
- The mock engine asks 8 deterministic questions covering at least 4 curriculum days, tailored using each candidate's mission history (skipped areas, retry counts, first-try passes).
