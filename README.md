# The Interview Agent

An AI-powered adaptive technical interview platform built with React,
FastAPI, and Google Gemini. It analyzes candidate history, creates a
curriculum-grounded interview plan, evaluates answers, adapts subsequent
questions, and generates final feedback.

## Features

-   Candidate-aware interview planning
-   Curriculum-grounded questions
-   Real-time answer evaluation
-   Adaptive follow-up and difficulty changes
-   Evaluation of correctness, depth, reasoning, and clarity
-   Minimum 8 questions and 4 curriculum days
-   Maximum 10 questions and 2 consecutive follow-ups
-   AI-generated final feedback
-   Rule-based fallbacks when Gemini is unavailable
-   Mock mode for development and testing

## Tech Stack

### Frontend

-   React
-   TypeScript
-   Vite
-   React Router
-   Custom CSS/UI
-   Axios/API service layer

### Backend

-   Python
-   FastAPI
-   Pydantic
-   Uvicorn
-   In-memory session store

### AI

-   Google Gemini API
-   `google-genai`
-   Structured Pydantic outputs
-   Candidate analysis
-   Interview planning
-   Adaptive interview turns
-   Final feedback generation

### Data

-   JSON candidate dataset
-   31-day curriculum across 8 modules

## Architecture

``` text
Candidate Selection
        |
        v
Candidate Analysis
        |
        v
Interview Planning
        |
        v
First Question
        |
        v
+--------------------------+
|      Interview Loop      |
|                          |
| Candidate Answer         |
|        |                 |
|        v                 |
| AI Evaluation            |
|        |                 |
|        v                 |
| Adaptive Next Question   |
+------------+-------------+
             |
             v
     Final AI Feedback
```

The application enforces interview constraints in the backend:

-   Minimum questions: 8
-   Minimum unique curriculum days: 4
-   Maximum questions: 10
-   Maximum consecutive follow-ups: 2

## Project Structure

``` text
The Interview Agent/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── context/
│   │   ├── hooks/
│   │   ├── layouts/
│   │   ├── lib/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── Given_Data/
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── .env.example
│   ├── package.json
│   └── vite.config.ts
│
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   │   ├── prompts/
│   │   │   ├── interviewer.py
│   │   │   ├── llm.py
│   │   │   └── schemas.py
│   │   ├── api/
│   │   ├── data/
│   │   ├── interview/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── config.py
│   │   └── main.py
│   ├── tests/
│   ├── .env.example
│   └── requirements.txt
│
└── README.md
```

## API

The main endpoint is:

``` text
POST /api/interview
```

### Start an interview

``` json
{
  "sessionId": "unique-session-id",
  "candidate": {
    "...": "raw candidate object"
  }
}
```

### Submit an answer

``` json
{
  "sessionId": "unique-session-id",
  "message": "Candidate answer"
}
```

### Response

``` json
{
  "reply": "Next interviewer response/question",
  "done": false
}
```

When the interview finishes, the response includes final feedback:

``` json
{
  "reply": "...",
  "done": true,
  "feedback": {
    "summary": "...",
    "strengths": [],
    "gaps": [],
    "next": []
  }
}
```

## Local Development

### Backend

``` powershell
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Create `backend/.env`:

``` env
GEMINI_API_KEY=your_gemini_api_key
AI_MODEL=gemini-3.5-flash
AI_ENABLED=true
```

Run the backend:

``` powershell
uvicorn app.main:app --reload
```

Backend:

``` text
http://localhost:8000
```

API documentation:

``` text
http://localhost:8000/docs
```

### Frontend

In another terminal:

``` powershell
cd frontend
npm install
npm run dev
```

Configure the frontend environment:

``` env
VITE_API_BASE_URL=http://localhost:8000
VITE_USE_MOCK=false
```

## Mock Mode

The backend can run without live Gemini calls:

``` env
AI_ENABLED=false
```

This uses the deterministic interview engine and is useful for
development, testing, and demos when AI access is unavailable.

## Testing

From the `backend` directory:

``` powershell
pytest
```

The completed implementation was verified with the project's automated
test suite.

## Environment Variables

### Backend

``` env
GEMINI_API_KEY=
AI_MODEL=gemini-3.5-flash
AI_ENABLED=true
```

### Frontend

``` env
VITE_API_BASE_URL=
VITE_USE_MOCK=false
```

Never expose `GEMINI_API_KEY` in frontend code.

## Limitations

-   Interview sessions are stored in memory and are lost if the backend
    restarts.
-   Multiple backend instances would require shared session storage.
-   AI behavior depends on the configured Gemini API quota and
    availability.
-   Rule-based fallbacks provide continuity when the AI service is
    unavailable.

## Team

Built as a 3-member hackathon project.
