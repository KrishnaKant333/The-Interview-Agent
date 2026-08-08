# AI Usage Log

# Format for adding new records 

## Prompt No.

**AI Tool:**

**Author:** 

### Prompt
---

### Outcome
---

## Prompt no : 1
**Ai Tool : Chatgpt**
**Author : Krishnakant Sharma**
### Prompt : 
hey there so we have this 48 hr online hackathon and this is one of the problem statements we have decided to make the solution of, i will be attaching the problem statement in text, and other provided info along with the problem in the next prompt, we are a group of 3, and so i want u to distribute the tasks to each of the member and provide me with the tech stack as well as the directory hierarchy and suggest me the ai agents/ IDEs which should be used to make this

### Outcome : 
Sounds good. Once you send the problem statement and the additional information, I'll treat this like we're planning a real hackathon project.

I'll provide:

### 1. Project Analysis
- Break down the problem statement
- Identify the core pain point
- Suggest the best solution (not just the obvious one)
- Recommend an MVP (48-hour realistic scope)
- List stretch goals if time permits

### 2. Team Task Distribution (3 Members)
I'll divide the work so everyone can work in parallel.

For example:

**Member 1 (Frontend + UI/UX)**
- Landing page
- Dashboard
- Responsive design
- Authentication UI
- State management

**Member 2 (Backend + Database)**
- API development
- Database schema
- Authentication
- Business logic
- Deployment

**Member 3 (AI + Integration + DevOps)**
- AI features
- Prompt engineering
- AI agent workflows
- External APIs
- Testing
- Final deployment
- Presentation/demo

I'll tailor these once I know the project.

---

### 3. Tech Stack Recommendation

Depending on the problem I'll recommend something like:

Frontend
- React + Vite
- TypeScript
- TailwindCSS
- shadcn/ui
- Framer Motion

Backend
- Node.js
- Express / Fastify
- Prisma
- PostgreSQL / MongoDB
- JWT / Clerk / Supabase Auth

AI
- OpenAI
- Gemini
- Claude
- LangChain (only if actually useful)
- MCP if applicable
- Vector DB if RAG is needed

Deployment
- Vercel
- Railway
- Render
- Neon
- Supabase

Version Control
- GitHub
- GitHub Projects
- GitHub Actions (if useful)

---

### 4. Complete Folder Structure

Something like:

```text
project/
│
├── client/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── layouts/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── context/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── lib/
│   │   └── App.tsx
│
├── server/
│   ├── src/
│   │   ├── routes/
│   │   ├── controllers/
│   │   ├── middleware/
│   │   ├── models/
│   │   ├── services/
│   │   ├── ai/
│   │   ├── utils/
│   │   └── app.ts
│
├── shared/
│
├── docs/
│
├── prompts/
│
├── scripts/
│
├── .env
├── docker-compose.yml
└── README.md
```

or a better architecture if the project requires microservices or AI pipelines.

---

### 5. AI Tools & IDEs

Since it's a **48-hour hackathon**, speed matters more than writing everything manually.

I'd recommend:

| Purpose | Tool |
|---------|------|
| Main IDE | VS Code |
| AI Coding | Claude Code (best for large codebases) |
| Backup AI | ChatGPT GPT-5.5 |
| Quick UI Generation | v0 |
| Component Library | shadcn/ui |
| Diagrams | Excalidraw |
| Database | Supabase |
| Deployment | Vercel + Railway |
| API Testing | Bruno or Postman |
| Design | Figma AI |
| Icons | Lucide |

---

### 6. AI Agent Workflow

I'll also design an efficient workflow, for example:

```
Member 1
↓

Claude Code
↓

Generate React pages

↓

ChatGPT

↓

Improve UX

↓

v0

↓

Generate premium UI
```

and similarly for backend and AI integration.

---

### 7. Git Workflow

I'll define:

- branch strategy
- merge strategy
- commit conventions
- who owns which branch
- conflict avoidance

---

### 8. Timeline (48 Hours)

Something like:

**Hour 0–3**
- Planning
- Architecture
- Git setup

**Hour 3–12**
- Core frontend
- Backend APIs
- Database

**Hour 12–24**
- AI integration
- Authentication
- Main features

**Hour 24–36**
- Polish
- Testing
- Fix bugs

**Hour 36–44**
- Deployment
- PPT
- Demo video

**Hour 44–48**
- Final testing
- README
- Submission

---

### 9. Extra Deliverables

If needed, I'll also help you create:
- High-quality README
- Architecture diagram
- System design diagram
- Database ER diagram
- API documentation
- Pitch deck
- 2-minute demo script
- Judge Q&A preparation
- Winning presentation strategy

Go ahead and send:
1. The complete problem statement.
2. Any constraints or judging criteria.
3. The hackathon theme.
4. Whether it's web, mobile, desktop, or open innovation.
5. Any mandatory technologies or APIs.

Once I have that, I'll give you a complete execution plan optimized for a 48-hour hackathon.

## Prompt no : 2

**AI Tool : Chatgpt**

**Author : Krishnakant Sharma**

### Prompt : 
here, ive uploaded problem statement.txt, candidates and curriculum json files and technical specs markdown file, give me the plan

### Outcome :
After reading all four files, I actually think this is a **very winnable hackathon** if you don't over-engineer it.

The judges are **not asking for ChatGPT with a fancy UI**.

They're asking for an **AI interviewer** that:
- adapts to the learner
- asks intelligent follow-ups
- remembers previous answers
- generates feedback
- follows the supplied API contract.  

---

# What I think will stand out

Most teams will build:

Candidate
⬇
LLM
⬇
Questions

That's boring.

Instead build this:

```
Candidate Profile
        │
        ▼
Interview Planner Agent
        │
        ▼
Question Generator Agent
        │
        ▼
Interview Session
        │
        ▼
Answer Evaluator Agent
        │
        ▼
Difficulty Controller
        │
        ▼
Feedback Generator
```

This still uses one API endpoint, but internally behaves like an interviewer rather than a chatbot.

---

# MVP Features (must have)

From the problem statement:

✅ Personalized interview

✅ Minimum 8 questions

✅ 4+ curriculum days

✅ Follow-up questions

✅ Context memory

✅ Final feedback

✅ Required endpoint

That's enough for submission. 

---

# Stretch Features (what wins)

These are not required but judges will remember them.

### ⭐ Adaptive Difficulty

If candidate answers well

```
"What is RAG?"

↓

"Why does vector similarity outperform keyword search?"

↓

"What embedding model would you choose and why?"

↓

"When would you avoid RAG altogether?"
```

If candidate struggles

```
"What is RAG?"

↓

"What are embeddings?"

↓

"Why are embeddings needed?"

↓

"Can you explain with an example?"
```

---

### ⭐ Interview Scorecard

Live

```
Knowledge ████████░░

Communication ██████░░░░

Confidence ███████░░░

Reasoning ████████░░
```

---

### ⭐ Candidate Timeline

Instead of asking random questions

Generate interview from candidate history.

For example Candidate 1

```
Completed:
Day 7
Day 8
Day 10
Day 12
Day 16
Day 22
Day 23
Day 28

Skipped:
Day 29
```

Interview

```
Embeddings

↓

Vector DB

↓

Retrieval

↓

Prompt Engineering

↓

Backend

↓

Multi Agent

↓

MCP

↓

Deployment

↓

Skipped topic
```

Perfect personalization. 

---

# Architecture

```
React Frontend
        │
 REST API
        │
FastAPI Backend
        │
Interview Manager
        │
 ├── Candidate Analyzer
 ├── Curriculum Retriever
 ├── Question Planner
 ├── Follow-up Generator
 ├── Context Manager
 ├── Feedback Engine
 └── LLM
```

---

# Tech Stack

## Frontend

React

Vite

TypeScript

TailwindCSS

shadcn/ui

Framer Motion

React Query

---

## Backend

FastAPI

Pydantic

Python

Uvicorn

---

## AI

OpenAI GPT-4.1 / GPT-5 API (or Gemini if budget is a concern)

LangGraph (preferred over LangChain for stateful interview flow)

Instructor / PydanticAI for structured outputs (optional but useful)

---

## Database

SQLite

Why?

Need session state only.

No need for PostgreSQL.

---

## Deployment

Frontend

Vercel

Backend

Railway

or Render

---

## Monitoring

Logfire

or LangSmith

(optional)

---

# Recommended Directory

```
ai-interviewer/

frontend/
│
├── src/
│   ├── app/
│   ├── pages/
│   ├── components/
│   │      ├── interview/
│   │      ├── dashboard/
│   │      ├── feedback/
│   │      └── ui/
│   │
│   ├── hooks/
│   ├── services/
│   ├── utils/
│   ├── assets/
│   └── types/

backend/

├── app/
│
├── api/
│      interview.py
│
├── agents/
│      planner.py
│      interviewer.py
│      evaluator.py
│      feedback.py
│
├── services/
│      llm.py
│      curriculum.py
│      candidate.py
│      prompts.py
│
├── models/
│      session.py
│
├── schemas/
│
├── memory/
│
├── utils/
│
├── data/
│      candidates.json
│      curriculum.json
│
├── main.py
│
└── requirements.txt

shared/

README.md

docs/

architecture.png

API.md

Dockerfile

docker-compose.yml
```

---

# Team Division (3 Members)

## 👨‍💻 Member 1 (Frontend + UI)

Deliverables

- Landing page
- Candidate selection
- Chat UI
- Streaming messages
- Progress bar
- Interview completion page
- Feedback dashboard
- Responsive design

---

## 👨‍💻 Member 2 (Backend + API)

Deliverables

- FastAPI
- Session handling
- `/api/interview`
- Candidate parser
- Curriculum parser
- State machine
- API validation
- Deployment

Basically everything required by the technical spec. 

---

## 👨‍💻 Member 3 (AI Engineer)

Deliverables

- Prompt engineering
- Interview planner
- Follow-up generation
- Answer evaluation
- Feedback generation
- Difficulty adaptation
- Testing prompts

This member owns all LLM behaviour.

---

# Git Branches

```
main

develop

frontend

backend

ai-agent
```

Everyone works independently.

Merge into develop.

Final merge

develop

↓

main

---

# AI Tools I'd Use

## Cursor

For editing

★★★★★

---

## Claude Code

For backend

★★★★★

---

## ChatGPT

For

Prompt engineering

Architecture

Debugging

Planning

★★★★★

---

## v0

Generate UI in minutes

★★★★★

---

## Excalidraw

Architecture diagram

★★★★★

---

## GitHub Copilot

Autocomplete

★★★★☆

---

# 48-Hour Timeline

## Hours 0–3
- Read spec and define architecture
- Set up repo, FastAPI, React, Git branches

## Hours 3–10
- Frontend skeleton
- Backend endpoint
- Load candidate and curriculum JSON
- Session management

## Hours 10–18
- Implement interview planner and question generator
- Build adaptive follow-up logic
- Basic chat interface

## Hours 18–28
- Feedback engine
- UI polish
- Candidate timeline
- Progress indicators

## Hours 28–36
- Integrate LLM
- Test multiple candidate profiles
- Fix edge cases

## Hours 36–44
- Deploy frontend and backend
- Prepare README, architecture diagram, and API docs
- Record demo video

## Hours 44–48
- Full testing
- Polish prompts
- Practice presentation and submit

# One suggestion that I think could make your project memorable

The provided candidate data isn't just a list of completed modules—it includes **attempt counts, skipped topics, commit days, and learning signals**. Use those to shape the interview. For example, if a candidate took five attempts on Prompt Engineering or skipped Docker, spend more time probing those areas, while asking deeper questions on topics they mastered quickly. That demonstrates you're using the supplied data intelligently rather than simply reading it. 

If you execute this well, you'll have a polished AI interviewer that clearly satisfies the requirements while showcasing thoughtful personalization based on the curriculum structure and candidate progress.

## Prompt no : 3
**Ai Tool : Chatgpt**
**Author : Krishnakant Sharma**

### Prompt : 
i along with one other member will be looking over the frontend and AI part, tell me where to start with setting up react vite env and how to generate the frontend
### Outcome : 
Perfect. Since you're handling the **Frontend + AI**, I'd actually recommend you **don't start coding immediately**. Spend the first 1–2 hours getting the project structure right—your teammate can begin the backend while you build the UI skeleton.

---

# Phase 1: Create the React Project (15–20 min)

### 1. Install Node.js
Verify your installation:

```bash
node -v
npm -v
```

If both commands return versions, you're ready.

---

### 2. Create a Vite + React + TypeScript project

```bash
npm create vite@latest frontend -- --template react-ts
```

Go into the project:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run it:

```bash
npm run dev
```

You should see something like:

```
http://localhost:5173
```

Open it in your browser.

---

# Phase 2: Install Everything You'll Need

Run:

```bash
npm install react-router-dom
```

```bash
npm install @tanstack/react-query
```

```bash
npm install axios
```

```bash
npm install framer-motion
```

```bash
npm install lucide-react
```

```bash
npm install clsx
```

```bash
npm install react-hook-form
```

```bash
npm install zod
```

```bash
npm install @hookform/resolvers
```

---

# Phase 3: Install Tailwind CSS

The exact Tailwind setup differs between major versions, so use the **official installation guide for Vite** rather than older tutorials.

After installing Tailwind, verify it works by adding:

```tsx
<h1 className="text-5xl font-bold">
Hello
</h1>
```

If it appears styled, you're ready.

---

# Phase 4: Install shadcn/ui

Initialize it:

```bash
npx shadcn@latest init
```

Recommended options:

```
TypeScript → Yes

Tailwind → Yes

App Directory → No

Alias → @/*
```

Then install the components you'll use:

```bash
npx shadcn@latest add button
```

```bash
npx shadcn@latest add card
```

```bash
npx shadcn@latest add badge
```

```bash
npx shadcn@latest add input
```

```bash
npx shadcn@latest add textarea
```

```bash
npx shadcn@latest add progress
```

```bash
npx shadcn@latest add dialog
```

```bash
npx shadcn@latest add avatar
```

```bash
npx shadcn@latest add separator
```

---

# Phase 5: Clean the Boilerplate

Delete:

```
App.css

index.css (replace with Tailwind)

assets/react.svg
```

Replace `App.tsx` with:

```tsx
function App() {
  return (
    <div>
      Hello Interview Agent
    </div>
  );
}

export default App;
```

---

# Phase 6: Create the Folder Structure

Inside `src`:

```
src/

assets/

components/
    ui/
    chat/
    interview/
    feedback/
    common/

pages/
    Home.tsx
    Interview.tsx
    Feedback.tsx

layouts/

hooks/

services/
    api.ts
    interview.ts

types/

utils/

context/

constants/

App.tsx

main.tsx
```

---

# Phase 7: Set Up Routing

Create three pages:

```
Home

Interview

Feedback
```

Routes:

```
/

↓

Select Candidate

↓

/interview

↓

Chat Screen

↓

/feedback
```

---

# What the UI Should Look Like

### Home

```
-----------------------------------------

Interview Agent

Select Candidate

Sarah Johnson

Alex Turner

Emily Chen

[Start Interview]

-----------------------------------------
```

---

### Interview Screen

```
+--------------------------------------+

Candidate

Progress

Question 3 / 8

--------------------------------------

AI

Can you explain embeddings?

--------------------------------------

You

Embeddings convert text...

--------------------------------------

Input Box

[Send]

--------------------------------------
```

---

### Feedback Screen

```
Interview Complete

Overall

8.6/10

Strengths

✔ Good understanding

✔ Strong RAG concepts

✔ Good reasoning

Needs Improvement

• MCP

• Deployment

Recommended Topics

Day 23

Day 28

Download Report
```

---

# What to Ask AI to Generate

Don't ask it to generate the whole app in one prompt. Break it down.

### Prompt 1

> Create a modern landing page for an AI Interview Agent using React, TypeScript, TailwindCSS, and shadcn/ui. Include a hero section, candidate selector, and a prominent "Start Interview" button. Use a clean enterprise design with dark mode.

---

### Prompt 2

> Create a ChatGPT-style interview interface with an interviewer panel, candidate responses, progress indicator (Question X of 8), streaming message bubbles, input field, and responsive layout.

---

### Prompt 3

> Create a feedback dashboard showing interview summary, strengths, weaknesses, recommended curriculum days, score cards, and progress bars.

---

# AI Tools I'd Use

- **v0** for quickly generating polished React + Tailwind UI.
- **Claude Code** for implementing and refactoring components.
- **ChatGPT** (me) for architecture, debugging, prompts, and integration.

---

## My recommendation for your workflow

Since you only have **48 hours**, I'd split your work like this:

- **First 2–3 hours:** Set up Vite, Tailwind, shadcn/ui, routing, and folder structure.
- **Next 3–4 hours:** Generate the three main screens (Home, Interview, Feedback) using AI, then clean up and connect them.
- **Only after the backend API is ready:** Wire the frontend to `/api/interview` and focus on polish, animations, and responsiveness.

This approach gets a professional-looking frontend in place early, while leaving plenty of time for AI integration and debugging before submission.

## Prompt no : 4
**Ai Tool : Chatgpt**
**Author : Krishnakant Sharma**

### Prompt : 
ive installed and set up the required files, tell me where to proceed next and what to create/ which ai agent to use to start with

### Outcome :
Yep. Since the **Vite + React environment, Tailwind/shadcn, routing, and folders are already set up**, don't touch the backend yet.

Your next goal should be:

> **Get a complete clickable frontend prototype working with mock data before connecting the AI/API.**

That gives you something demonstrable even if the backend/LLM integration breaks later.

## Step 1 — Build the frontend in this order

I recommend this exact sequence:

```text
1. App shell / layout
       ↓
2. Candidate selection
       ↓
3. Interview screen
       ↓
4. Feedback screen
       ↓
5. Mock interview flow
       ↓
6. API integration
       ↓
7. AI-driven behavior
       ↓
8. Polish
```

Don't start with the AI agent.

The AI needs a UI and API contract to plug into.

---

# Step 2 — Start with the App Shell

Create:

```text
src/
├── components/
│   ├── common/
│   │   ├── Navbar.tsx
│   │   └── PageContainer.tsx
│   │
│   └── ui/
│
├── layouts/
│   └── MainLayout.tsx
│
├── pages/
│   ├── Home.tsx
│   ├── Interview.tsx
│   └── Feedback.tsx
```

For now, make `MainLayout` extremely simple.

You want:

```text
┌──────────────────────────────────────────┐
│  AI Interviewer                 ● Online │
├──────────────────────────────────────────┤
│                                          │
│              PAGE CONTENT                │
│                                          │
└──────────────────────────────────────────┘
```

Don't spend an hour making a navbar.

---

# Step 3 — Use an AI coding agent for the first screen

### Use **Claude Code** for implementation.

I'd use the agents like this:

| Task                    | Agent                     |
| ----------------------- | ------------------------- |
| Architecture            | **ChatGPT**               |
| Generate initial UI     | **v0**                    |
| Implement/refactor code | **Claude Code**           |
| Debug                   | **Claude Code + ChatGPT** |
| AI prompts/behavior     | **ChatGPT**               |
| Final UI polish         | **v0 + Claude Code**      |

Since you're already inside the project, **Claude Code is the one I'd start with now.**

---

# Step 4 — Give Claude Code this prompt

Don't tell it to build the entire application.

Give it one controlled task:

```text
You are working on an existing React + TypeScript + Vite project.

The project is an AI Technical Interview Agent for a 31-day AI engineering cohort.

The frontend will eventually have three primary screens:

1. Candidate Selection
2. Technical Interview
3. Interview Feedback

For now, ONLY implement the application shell and Candidate Selection screen.

Requirements:

- React + TypeScript
- TailwindCSS
- shadcn/ui components already installed
- React Router
- Lucide icons
- Do not install unnecessary dependencies
- Do not modify the backend
- Do not create fake API calls yet
- Keep components reusable
- Follow the existing src folder structure

Candidate selection should display:
- Candidate name
- Job role
- Years of experience
- Education
- Cohort completion status
- A "Start Interview" button

Use mock candidate data for now.

Make the UI feel like a premium enterprise AI interview platform rather than a generic chatbot.

Design:
- modern
- minimal
- professional
- responsive
- excellent typography
- subtle animations
- dark-first interface
- accessible contrast
- avoid excessive gradients

When a candidate is selected, navigate to /interview/:candidateId.

Do not implement the interview logic yet.

Before modifying files, inspect the existing project structure and reuse existing components where possible.
```

**Let Claude inspect the project first.**

That's important.

Don't let it blindly overwrite your setup.

---

# Step 5 — Your Candidate Card

The candidate data is actually important here.

The supplied candidate profiles contain things like:

```text
name
jobRole
yearsExperience
education
status
missions
signals
```

For example, Sarah's profile contains her completed missions and learning signals such as `commitDays`, `missionsCompleted`, and `missionsFirstTry`. 

But **don't display all of that on the card**.

Show:

```text
Sarah Johnson
Senior Data Engineer

9 years experience
MS Computer Science

31-Day AI Cohort
✓ Completed

[Start Interview]
```

Then we'll use the deeper information **inside the AI engine**, not clutter the UI.

---

# Step 6 — Then build the Interview screen

After the candidate screen works, give Claude Code this:

```text
Now implement the /interview/:candidateId screen.

Do not connect to the backend or LLM yet.

Create a realistic technical interview interface using mock interview data.

The interface should contain:

- Candidate information
- Interview progress
- Current question number
- AI interviewer message
- Candidate response area
- Send button
- Conversation history
- Typing/loading state
- End interview control

The interview must visually feel like a real technical interview, NOT a generic ChatGPT clone.

Use reusable components:

InterviewHeader
InterviewProgress
MessageList
MessageBubble
AnswerInput
InterviewControls

Create a small mock interview service so that clicking Send produces predetermined interviewer responses.

Keep the architecture ready for replacing the mock service with POST /api/interview later.

Do not modify unrelated files.
```

---

# Step 7 — Build the Feedback screen

Then:

```text
Implement /feedback/:sessionId using mock data.

Create:

- Interview completed header
- Overall assessment
- Summary
- Strengths
- Knowledge gaps
- Recommended next topics
- Curriculum day references
- Topic-level scores
- Restart interview button

The backend will eventually return:

{
  "summary": "...",
  "strengths": [],
  "gaps": [],
  "next": []
}

Design the components so this exact response can later be rendered without restructuring the page.

Use reusable components and shadcn/ui.

Do not connect to the API yet.
```

The final API specifically requires `summary`, `strengths`, `gaps`, and `next`, so building the feedback UI around that structure now will save you trouble later. 

---

# Step 8 — THEN we bring in the AI

This is where your role becomes particularly important.

Don't make one giant "AI Agent."

I'd structure the AI side conceptually as:

```text
             Candidate
                 │
                 ▼
       ┌──────────────────┐
       │ Candidate Analyzer│
       └────────┬─────────┘
                │
                ▼
       ┌──────────────────┐
       │ Interview Planner│
       └────────┬─────────┘
                │
                ▼
       ┌──────────────────┐
       │    Interviewer   │
       └────────┬─────────┘
                │
          Candidate Answer
                │
                ▼
       ┌──────────────────┐
       │ Answer Evaluator │
       └────────┬─────────┘
                │
                ▼
       ┌──────────────────┐
       │ Difficulty/Topic │
       │    Controller    │
       └────────┬─────────┘
                │
                ▼
           Next Question
```

But **don't implement all five agents as separate LLM calls**.

That will waste your 48 hours and API credits.

Instead, use **one stateful interview agent/workflow** with these logical stages.

---

# The most important AI logic

Your agent should first look at:

### Candidate

```text
jobRole
experience
education
completed missions
failed missions
skipped topics
attempt counts
learning signals
```

### Curriculum

The curriculum is organized into 8 modules, including Embeddings & Vector Search, LLM Core/Prompting, Chatbot Application Build, Agentic AI & MCP, and Evaluation/Security/Deployment. 

Then create an interview plan.

For example:

```json
{
  "questions": [
    {
      "day": 7,
      "topic": "Embeddings",
      "difficulty": "medium"
    },
    {
      "day": 10,
      "topic": "Retrieval",
      "difficulty": "hard"
    },
    {
      "day": 12,
      "topic": "Prompt Engineering",
      "difficulty": "medium"
    }
  ]
}
```

Then the interview actually begins.

---

# Very important: exploit the candidate data

This is where you can differentiate yourselves.

Suppose:

```text
Day 7 → passed, 1 attempt
Day 8 → passed, 1 attempt
Day 10 → passed, 4 attempts
Day 12 → passed, 5 attempts
Day 22 → passed, 2 attempts
```

The interviewer shouldn't treat all topics equally.

It should think:

```text
Strong:
Day 7
Day 8

Potential weakness:
Day 10
Day 12

Probe:
Day 12
```

Then ask progressively deeper questions.

The supplied candidate data explicitly provides attempt counts and skipped/failed missions, making this personalization possible. 

---

# Your 8-question interview

I'd implement this structure:

```text
Q1 — Warm-up
       ↓
Q2 — Core concept
       ↓
Q3 — Deeper concept
       ↓
Q4 — Application
       ↓
Q5 — Follow-up based on answer
       ↓
Q6 — Architecture/scenario
       ↓
Q7 — Weak-area probe
       ↓
Q8 — Final challenging question
       ↓
Feedback
```

This guarantees the minimum **8 questions across at least 4 curriculum days** required by the challenge. 

---

# How the adaptive part should work

Imagine:

**Interviewer:**

> Explain how embeddings are used in a RAG system.

Candidate:

> They convert text into vectors so we can search similar information.

Don't immediately jump to another topic.

Agent:

> Good. You mentioned similarity search. What would happen if two chunks contain similar words but have different semantic meanings?

Now the candidate answers.

The agent evaluates that answer.

If strong:

```text
difficulty += 1
```

If weak:

```text
difficulty -= 1
```

And the next question changes accordingly.

**That's your actual "AI interviewer."**

---

# Where I'd put this code

Eventually:

```text
backend/
│
├── agents/
│   ├── interview_agent.py
│   ├── planner.py
│   ├── evaluator.py
│   └── feedback.py
│
├── services/
│   ├── curriculum.py
│   ├── candidates.py
│   └── llm.py
│
└── schemas/
    ├── interview.py
    └── feedback.py
```

Your frontend shouldn't know anything about how the AI reasons.

It only knows:

```text
POST /api/interview
```

The technical specification requires exactly that endpoint and uses `sessionId` to maintain the interview state. 

---

# So, RIGHT NOW

Don't touch LangGraph or prompts yet.

Do this:

### 🟢 You

**1. Run Claude Code**

↓

**2. Give it the Candidate Selection prompt above**

↓

**3. Test `/`**

↓

**4. Build Interview screen**

↓

**5. Build Feedback screen**

↓

**6. Make the complete mock flow work**

```text
Home
 ↓
Select Sarah
 ↓
Interview
 ↓
8 mock questions
 ↓
Feedback
```

### 🟡 Meanwhile your other member

Should start building:

```text
FastAPI
 ↓
POST /api/interview
 ↓
sessionId handling
 ↓
candidate parsing
 ↓
curriculum parsing
```

### 🔴 Then we connect them

```text
React
  │
  │ POST /api/interview
  ▼
FastAPI
  │
  ▼
Interview Agent
  │
  ▼
LLM
```

**That's the point where I'd help you build the actual AI interviewer prompts/state machine.**

And one thing I'd strongly recommend: **don't let Claude Code decide your entire architecture.** Let it write the components, but keep the interview state, API contract, and adaptive logic under your control. That's the part the judges are actually evaluating.


## Prompt No. 5

**AI Tool: Codex**

**Author: Yash Palkar** 

### Prompt
Continuing from [Hackathon Task Distribution](chatgpt-conversation://6a7621a3-25e0-83ee-a802-e95a73bc09c6): Help the user execute a 48-hour AI-first hackathon build for the AI interviewer project. They own the frontend. Provide a practical AI-assisted development workflow, frontend architecture/folder structure, prompts for coding agents, division of work across 3 members, and a sequence for building with mock data then integrating the backend. Base requirements on the uploaded project context where available; do not invent unsupported API details.

### Outcome
Build a focused, demo-ready AI interviewer: personalized from candidate progress and curriculum, at least 8 questions across 4+ curriculum days, adaptive follow-ups, conversational memory, and final feedback. Those are the requirements visible in the supplied project context; treat the technical-spec endpoint and payload as the source of truth during integration.

## 48-hour build sequence

| Time | Frontend — you | Member 2 | Member 3 |
|---|---|---|---|
| 0–3h | Set up UI shell, routes, mock-data layer | Set up server, load supplied JSON, expose spec-required endpoint | Extract personalization rules from candidate + curriculum data |
| 3–10h | Landing, candidate picker, setup screen | Session/state foundation, validate endpoint contract | Design structured prompt/output for plan, question, evaluation |
| 10–18h | Interview room: question, answer, progress, thinking state | Connect question lifecycle and session memory | Implement adaptive follow-up and scoring |
| 18–28h | Results dashboard and recommendation UI | Return final feedback through contract | Generate feedback, strengths, gaps, next curriculum recommendations |
| 28–36h | Replace mocks with real adapter; responsive/error states | Deploy backend and fix integration | Test 3 candidate journeys; tune prompts |
| 36–44h | UI polish and end-to-end demo path | API robustness, CORS/config | Demo script, evaluation examples |
| 44–48h | No new features—test and present | Final integration support | Final demo rehearsal |

## Ownership

**You — Frontend + demo experience**

- Candidate selection based on the supplied `candidates.json`
- Personalization/setup screen showing relevant learning signals
- Interview room with answer input, question count, topic, adaptive-difficulty display, and “evaluating” state
- Final feedback dashboard
- Mock data first, then one API adapter for integration
- Responsive layout, loading/error/empty states, deployment of frontend

**Member 2 — Backend + contract**

- Implement exactly the required API endpoint/schema from `technical specs.md`
- Parse candidates and curriculum data
- Session ID and interview-state management
- Connect AI-engine outputs to the endpoint
- Validate requests/responses and deploy backend
- Publish an `API.md` containing real example requests/responses early

**Member 3 — AI behavior + quality**

- Map completed, skipped, difficult, and mastered curriculum areas into an interview plan
- Generate 8+ questions spanning 4+ curriculum days
- Evaluate answers and determine next difficulty/follow-up
- Maintain concise session memory
- Produce final structured feedback: score dimensions, strengths, improvements, recommended next learning
- Test consistent outputs for several candidate profiles

## Frontend architecture

```text
ai-interviewer/
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── routes.tsx
│   │   │   └── AppProviders.tsx
│   │   ├── pages/
│   │   │   ├── LandingPage.tsx
│   │   │   ├── CandidatesPage.tsx
│   │   │   ├── InterviewSetupPage.tsx
│   │   │   ├── InterviewPage.tsx
│   │   │   └── ResultsPage.tsx
│   │   ├── components/
│   │   │   ├── ui/
│   │   │   ├── candidate/
│   │   │   │   ├── CandidateCard.tsx
│   │   │   │   └── LearningSummary.tsx
│   │   │   ├── interview/
│   │   │   │   ├── InterviewHeader.tsx
│   │   │   │   ├── QuestionCard.tsx
│   │   │   │   ├── AnswerInput.tsx
│   │   │   │   ├── ThinkingIndicator.tsx
│   │   │   │   ├── ProgressTracker.tsx
│   │   │   │   └── InterviewSidebar.tsx
│   │   │   └── feedback/
│   │   │       ├── ScoreOverview.tsx
│   │   │       ├── SkillBreakdown.tsx
│   │   │       ├── StrengthsList.tsx
│   │   │       └── LearningRecommendations.tsx
│   │   ├── features/interview/
│   │   │   ├── useInterview.ts
│   │   │   ├── interview.types.ts
│   │   │   └── interview.mapper.ts
│   │   ├── services/
│   │   │   ├── interviewApi.ts
│   │   │   └── interviewGateway.ts
│   │   ├── mocks/
│   │   │   ├── candidates.ts
│   │   │   └── interviewResponses.ts
│   │   ├── lib/
│   │   └── styles/
│   └── .env.example
├── backend/
├── shared/
│   └── api-contract.md
├── docs/
│   ├── demo-script.md
│   └── architecture.md
└── README.md
```

Use React + TypeScript + Vite + Tailwind. Add a component library only if it speeds you up. Avoid auth, databases in the frontend, complex global state, and elaborate animations.

## Mock-first integration approach

Do not let the UI depend directly on backend shapes.

1. Create frontend display types based on what the UI needs: current question, progress, topic, difficulty, completion status, feedback.
2. Put all fake interview scenarios in `mocks/interviewResponses.ts`.
3. Make `interviewGateway.ts` the only import used by pages/hooks.
4. Start in mock mode.
5. When Member 2 shares the real contract, update only:
   - `interviewApi.ts`
   - `interview.mapper.ts`
   - environment configuration  
   
Do not hardcode a guessed endpoint, action name, or payload. The prior conversation proposed examples, but your uploaded technical spec must override them.

## Definition of a convincing frontend demo

Your best flow is:

```text
Choose candidate
→ “Analyzing learning journey”
→ show relevant completed / skipped / difficult areas
→ personalized interview begins
→ answer submitted
→ “Evaluating answer…”
→ follow-up visibly becomes deeper or simpler
→ final feedback connects weaknesses to curriculum recommendations
```

The key is showing that the product used the provided learner data—not merely displaying a chat interface.

## Prompts for coding agents

Use one task per prompt. Have the agent inspect existing files before editing, and always ask it to run the project checks afterward.

**Frontend foundation**

```text
You are working on a React + TypeScript + Vite frontend for an AI interviewer hackathon project.

Inspect the existing project first. Implement only the application shell: routes for Landing, Candidates, Setup, Interview, and Results; a shared layout; and a clean dark, accessible visual system. Do not add backend calls or invent API details. Keep components small and use mock data only where required. Run the type check/build and report changed files.
```

**Interview room**

```text
Implement the Interview page only. It must show the current AI question, a large answer textarea, submit/loading state, interview progress, current topic, and a difficulty indicator. Obtain all data through an existing interview gateway abstraction; if it does not exist, create a mock-compatible interface without assuming backend endpoints or payload fields. Keep the page responsive and accessible. Run checks afterward.
```

**Mock scenario**

```text
Create realistic mock interview scenarios for the existing frontend types: one strong candidate path, one struggling candidate path, and one final-feedback result. Demonstrate personalization, at least 8 questions, an adaptive follow-up, memory of a previous answer, and curriculum-linked recommendations. Do not alter the technical API contract.
```

**Integration**

```text
Read shared/api-contract.md and the current frontend interview types. Replace the mock implementation behind the interview gateway with a real HTTP adapter that follows the documented contract exactly. Keep UI components unchanged as far as possible. Map API responses into frontend display types, handle loading and errors, and document required environment variables in .env.example.
```

**AI-engine task**

```text
Using only the provided candidates and curriculum data plus the documented API contract, design structured AI outputs for: interview plan, next question, answer evaluation, adaptive difficulty decision, and final feedback. Ensure the flow covers at least 8 questions across 4+ curriculum days, includes follow-ups and session memory, and returns machine-readable fields that the backend can validate. Include three test cases.
```

## Collaboration rules that prevent hackathon pain

- Agree on the API contract by hour 3; publish it in `shared/api-contract.md`.
- You work from mocks until the API passes one known test case.
- Each member owns separate folders; avoid simultaneous edits to shared files.
- Merge small, working commits frequently.
- Test one “hero candidate” path end to end before adding polish.
- Reserve the last six hours for a reliable demo, deployment, README, and presentation—not new features.


## Prompt No. 6

**AI Tool: Codex**

**Author: Yash Palkar** 

### Prompt
so give me the code for this project and tell give me instruction step by step

### Outcome
I created the runnable frontend MVP here:

[Open the project folder](</C:\Users\Yash Palkar\Documents\Codex\2026-08-08\referenced-chatgpt-conversation-this-is-an\outputs\ai-interviewer-frontend>)

It includes landing, candidate selection, personalized setup, adaptive mock interview, loading state, progress tracker, and final feedback dashboard.

## Run it

1. Install Node.js 20+ if needed.
2. Open a terminal in the project folder.
3. Run:

```bash
npm install
npm run dev
```

4. Open the local URL shown in the terminal.

## What to do next

1. Replace the three mock candidates in `src/App.tsx` with data mapped from your supplied `candidates.json`.
2. Ask your backend teammate for the exact endpoint request/response from `technical specs.md`.
3. Update only `src/interviewGateway.ts`:
   - Replace `MockInterviewGateway`
   - Keep the `InterviewGateway` interface
   - Map real responses into `InterviewTurn` and `Feedback`
4. Test this demo journey:
   - Select a candidate
   - Begin interview
   - Submit 8 answers
   - Confirm final feedback appears
5. Polish only after the full flow works on mobile and desktop.

The important integration file is [interviewGateway.ts](</C:\Users\Yash Palkar\Documents\Codex\2026-08-08\referenced-chatgpt-conversation-this-is-an\outputs\ai-interviewer-frontend\src\interviewGateway.ts>). This prevents backend changes from forcing a UI rewrite.


## Prompt No. 7

**AI Tool: Codex**

**Author: Yash Palkar** 

### Prompt
replace the dummy data from these files

### Outcome
Done—the dummy profiles are now replaced by all 20 real candidates from your supplied JSON files.

The UI now uses real:

- Name, role, experience, and education
- Completed missions and active commit days
- First-try completions
- Focus areas derived from skipped or high-attempt missions
- Curriculum titles to describe candidate strengths and review areas

I also verified the project builds successfully.

Key updated files:

- [App.tsx](</C:\Users\Yash Palkar\Documents\Codex\2026-08-08\referenced-chatgpt-conversation-this-is-an\outputs\ai-interviewer-frontend\src\App.tsx>)
- [candidate data mapper](</C:\Users\Yash Palkar\Documents\Codex\2026-08-08\referenced-chatgpt-conversation-this-is-an\outputs\ai-interviewer-frontend\src\data\candidates.ts>)

Restart or refresh your development server, then open **Choose a candidate** to see the real profiles.


