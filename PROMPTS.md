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

## Prompt no : 8
**Ai Tool : Chatgpt**
**Author : Krishnakant Sharma**

### Prompt : 
one of my teammate has made this frontend take a look, there's no backend yet so no api routing or anything, apparently he didnt use any ui components or anything like whatever we have these files under pages, layouts, what should i improve

### Outcome : 
Yeah — I looked through all five screenshots, and honestly **your teammate has already produced a pretty solid visual base**. The dark enterprise aesthetic fits the problem very well. I **wouldn't throw this away or rebuild it with shadcn just for the sake of using shadcn**.

The bigger issue is that right now it looks like a **beautiful static prototype**, while the challenge is specifically about an **adaptive conversational interviewer**.

So I'd improve the **product behavior + information architecture first**, and only then polish the UI.

---

# My assessment

### Current frontend

| Area                   | Current      | What I'd do                   |
| ---------------------- | ------------ | ----------------------------- |
| Visual design          | 🟢 Good      | Keep                          |
| Dark theme             | 🟢 Good      | Keep                          |
| Typography             | 🟢 Good      | Minor tweaks                  |
| Candidate cards        | 🟢 Good      | Improve information hierarchy |
| Interview UI           | 🟡 Good base | Major functional changes      |
| Feedback UI            | 🟢 Good      | Connect to real output        |
| Responsiveness         | 🟡 Unknown   | Test properly                 |
| Component architecture | 🟡 Unknown   | Refactor reusable pieces      |
| API integration        | 🔴 None      | Add after backend contract    |
| Real interview state   | 🔴 None      | Important                     |
| Adaptive questioning   | 🔴 None      | **Most important**            |
| Conversation history   | 🔴 None      | **Must add**                  |

The problem statement explicitly requires a **multi-turn conversational interview, intelligent follow-ups, context maintenance, and structured feedback**. 

So that's where I'd spend your time.

---

# 1. DON'T rebuild the whole frontend

This is important.

You mentioned:

> "he didnt use any ui components or anything like whatever we have these files under pages, layouts"

That's **not inherently a problem**.

You don't need shadcn everywhere.

For a hackathon, this is perfectly valid:

```text
pages/
layouts/
components/
hooks/
services/
types/
```

And honestly, looking at the screenshots, the custom styling is already coherent.

I'd **keep his visual language** and introduce reusable components where they actually help.

---

# 2. The biggest problem: the Interview screen

This is the screenshot I'd change the most.

Currently:

```text
┌──────────────────────────────┬───────────────┐
│                              │ Progress      │
│ Question 1 / 8               │               │
│                              │ Topic         │
│ What problem does RAG solve? │ RAG           │
│                              │               │
│                              │ Difficulty    │
│                              │ Foundation     │
│                              │               │
│                              │ Personalization│
│                              │               │
│ Answer                       │               │
│ ┌──────────────────────────┐ │               │
│ │                          │ │               │
│ └──────────────────────────┘ │               │
└──────────────────────────────┴───────────────┘
```

Visually nice.

But this isn't really a **conversation** yet.

The requirement says:

> "Ask intelligent follow-up questions."

and

> "Maintain conversation context throughout the interview." 

You need the UI to communicate that.

---

# 3. Change the interview UI to a conversation

I'd make it:

```text
┌─────────────────────────────────────────────┐
│ AI INTERVIEWER                 Question 3/8 │
├─────────────────────────────────────────────┤
│                                             │
│  AI                                         │
│  ┌───────────────────────────────────────┐  │
│  │ Explain how RAG solves the problem   │  │
│  │ of outdated model knowledge.         │  │
│  └───────────────────────────────────────┘  │
│                                             │
│                    YOU                      │
│              ┌───────────────────────┐      │
│              │ It retrieves relevant │      │
│              │ context before...     │      │
│              └───────────────────────┘      │
│                                             │
│  AI                                         │
│  ┌───────────────────────────────────────┐  │
│  │ Interesting. How would you decide   │  │
│  │ whether to use vector search or SQL │  │
│  │ for that retrieval?                  │  │
│  └───────────────────────────────────────┘  │
│                                             │
├─────────────────────────────────────────────┤
│ Your answer                                 │
│ ┌─────────────────────────────────────────┐ │
│ │ Type your response...                   │ │
│ └─────────────────────────────────────────┘ │
│                              [Send →]       │
└─────────────────────────────────────────────┘
```

Now the judge can **see adaptation happening**.

That's much stronger.

---

# 4. Don't expose too much "AI reasoning" to the candidate

This part:

> `Difficulty: Foundation`

and:

> `Personalization: Based on completed curriculum days and focus areas.`

is useful for a **demo/debug panel**, but I wouldn't necessarily expose all of it to the candidate.

Imagine a real interview:

> Difficulty: Hard
> Reason for question: You struggled on Day 12

😂 Doesn't feel natural.

Instead, make the right panel something like:

```text
INTERVIEW PROGRESS

● ● ● ● ○ ○ ○ ○

Question 4 of 8

CURRENT FOCUS
Prompt Engineering

INTERVIEW STYLE
Adaptive

SESSION
~ 12 min
```

Then have a tiny:

**"Why this question?"**

button that opens an explanation.

That's a cool hackathon feature.

---

# 5. Add a "Follow-up" indicator

This is something I'd definitely add.

Suppose Q4 is generated because of Q3.

Show:

```text
┌─────────────────────────────┐
│ ↳ FOLLOW-UP                 │
│                             │
│ You mentioned vector        │
│ similarity. How would you   │
│ handle irrelevant results?  │
└─────────────────────────────┘
```

That visually proves:

**The AI listened to the previous answer.**

This directly addresses one of the key requirements. 

---

# 6. Candidate selection page is good — but improve the cards

The candidate screen is already quite good.

But right now:

```text
Sarah Johnson

Senior Data Engineer · 9 years experience

STRENGTH
Strong in Embeddings Explained

FOCUS AREA
Review Monitoring...
```

I'd add a tiny **learning profile**.

For example:

```text
Sarah Johnson
Senior Data Engineer

9 years · MS Computer Science

COHORT
██████████  30/31 missions

STRENGTH
Embeddings

FOCUS
Observability

┌─────────────────────────────┐
│ 28 active days    20 first try │
└─────────────────────────────┘

Prepare interview →
```

The data is actually available in the supplied candidate profiles, including mission completion, attempts, skipped topics, and learning signals. 

That makes the candidate selection screen feel **purpose-built around the challenge**.

---

# 7. Add candidate filtering

You have 20 candidates in the supplied dataset.

Showing them all in a giant grid will become annoying.

Add:

```text
Search candidates...

[All roles ▼]

[Completed ▼]

[Focus area ▼]
```

And perhaps:

```text
20 candidates
```

This makes the application feel much more like an actual enterprise tool.

---

# 8. Your Home page is slightly too empty

The hero:

> **Your learning journey. Your interview.**

is actually good.

But there's a lot of empty space.

I'd add a small visual explanation below it:

```text
YOUR JOURNEY
      ↓
CURRICULUM
      ↓
PERSONALIZED INTERVIEW
      ↓
ADAPTIVE FOLLOW-UPS
      ↓
ACTIONABLE FEEDBACK
```

Or three cards:

```text
01
Your journey

We analyze what you completed,
struggled with, and skipped.

02
Your interview

Questions adapt to your
answers in real time.

03
Your next step

Get specific recommendations
for what to learn next.
```

You already have the three cards at the bottom — I'd make them slightly more visual and connect them to the actual workflow.

---

# 9. Feedback page — good, but there's one important issue

This screen looks good.

But:

```text
76 /100 overall performance

Technical knowledge 84%
Reasoning 81%
Communication 78%
System design 75%
```

Where are those numbers coming from?

Currently they're obviously mock data.

That's fine **right now**.

But later, don't just have the LLM randomly generate numbers.

Create a structured evaluator.

For example:

```json
{
  "scores": {
    "technicalKnowledge": 84,
    "reasoning": 81,
    "communication": 78,
    "systemDesign": 75
  },
  "strengths": [...],
  "gaps": [...],
  "next": [...]
}
```

Then your frontend simply renders the response.

The official API contract requires:

```text
summary
strengths[]
gaps[]
next[]
```

for the final response. 

You can add the score fields internally without breaking that contract.

---

# 10. Add a curriculum map to Feedback

This could be one of your **best UI features**.

Instead of only:

```text
Recommended learning

Review vector databases

Practice RAG evaluation

Revisit deployment
```

show:

```text
CURRICULUM COVERAGE

Day 7   Embeddings          ████████░░
Day 10  Retrieval           █████████░
Day 12  Prompt Engineering  ██████░░░░
Day 22  Multi-Agent         ████████░░
Day 28  Deployment          █████░░░░░
```

Or:

```text
Your interview revealed:

✓ Strong
  Day 7 — Embeddings
  Day 22 — Multi-Agent

△ Needs work
  Day 12 — Prompt Engineering

○ Recommended
  Day 28 — Deployment
```

That would connect the **candidate → curriculum → interview → feedback** story beautifully.

---

# 11. Introduce actual reusable components

I wouldn't go through the entire project and convert everything into shadcn.

Instead, create these:

```text
components/

├── layout/
│   ├── Navbar.tsx
│   └── Container.tsx
│
├── candidate/
│   ├── CandidateCard.tsx
│   ├── CandidateGrid.tsx
│   └── CandidateStats.tsx
│
├── interview/
│   ├── InterviewHeader.tsx
│   ├── InterviewProgress.tsx
│   ├── MessageList.tsx
│   ├── MessageBubble.tsx
│   ├── AnswerInput.tsx
│   ├── FollowUpBadge.tsx
│   └── InterviewSidebar.tsx
│
├── feedback/
│   ├── ScoreCard.tsx
│   ├── SkillBreakdown.tsx
│   ├── StrengthList.tsx
│   ├── GapList.tsx
│   └── CurriculumRecommendations.tsx
│
└── ui/
    ├── Button.tsx
    ├── Card.tsx
    ├── Badge.tsx
    └── Progress.tsx
```

You don't **need** shadcn.

If your teammate already has custom `Card`, `Button`, etc. that look good, reuse them.

---

# 12. Your pages should become very thin

Ideally:

### `Home.tsx`

```tsx
<HomeHero />
<HowItWorks />
<CTA />
```

### `Candidates.tsx`

```tsx
<CandidateSearch />
<CandidateFilters />
<CandidateGrid />
```

### `Interview.tsx`

```tsx
<InterviewHeader />
<InterviewLayout>
    <MessageList />
    <AnswerInput />
    <InterviewSidebar />
</InterviewLayout>
```

### `Feedback.tsx`

```tsx
<FeedbackHeader />
<OverallScore />
<SkillBreakdown />
<Strengths />
<Gaps />
<CurriculumRecommendations />
```

This will make your frontend **much easier to connect to the backend**.

---

# 13. Don't create frontend API logic yet

Since your teammate hasn't built the backend, **don't start hardcoding fetch calls throughout the components.**

Instead create:

```text
services/
    interviewApi.ts
```

Eventually:

```typescript
startInterview()
sendAnswer()
getFeedback()
```

And your React components call those functions.

So later:

```text
AnswerInput
     ↓
sendAnswer()
     ↓
POST /api/interview
     ↓
FastAPI
```

The technical spec specifically says every turn goes through `/api/interview` with `sessionId` and the candidate's latest response. 

---

# 14. One architectural thing I would change NOW

Your teammate seems to have designed around a **fixed 8-question flow**.

That's okay as a minimum.

But don't structure the frontend like:

```typescript
const questions = [
   question1,
   question2,
   question3,
   ...
]
```

Instead:

```typescript
interface InterviewState {
  sessionId: string;
  questionNumber: number;
  totalQuestions: number;
  currentTopic: string;
  messages: Message[];
  isLoading: boolean;
  done: boolean;
}
```

Because later the backend will decide:

```text
Question 1
   ↓
Candidate answer
   ↓
Evaluator
   ↓
Follow-up?
   ├── YES → Follow-up
   └── NO  → New topic
```

The frontend shouldn't care **why** the next question was generated.

It just receives:

```json
{
  "reply": "That's a good start. How would you...",
  "done": false
}
```

and renders it.

---

# 15. The architecture I'd settle on

Since you're responsible for frontend + AI, I'd make your side:

```text
                    ┌──────────────┐
                    │   React UI   │
                    └──────┬───────┘
                           │
                    interviewApi.ts
                           │
                    POST /api/interview
                           │
                    ┌──────▼───────┐
                    │   FastAPI    │
                    └──────┬───────┘
                           │
                  ┌────────▼────────┐
                  │ Interview State │
                  └────────┬────────┘
                           │
                ┌──────────▼──────────┐
                │   AI Interviewer    │
                │                     │
                │ Candidate Context   │
                │ Curriculum Context  │
                │ Question Planning   │
                │ Answer Evaluation   │
                │ Adaptation           │
                │ Feedback             │
                └─────────────────────┘
```

And the frontend only cares about the state.

---

# What I'd do TODAY

Since you have a working frontend already, **don't start another AI-generated frontend.**

### Task 1 — 30 min

Open your teammate's project and reorganize/identify:

```text
pages
layouts
components
services
types
```

Don't rewrite everything.

### Task 2 — 1 hour

Refactor the interview page into:

```text
MessageList
MessageBubble
AnswerInput
InterviewProgress
InterviewSidebar
```

### Task 3 — 1 hour

Change the interview screen from:

**question → answer**

to:

**conversation → answer → follow-up → conversation**

using mock data.

### Task 4 — 30 min

Create:

```typescript
InterviewState
Message
Candidate
Feedback
```

types.

### Task 5

Then we start the **actual AI architecture**.

---

## And here's the important part

**I wouldn't use another AI agent to blindly improve this frontend.**

You've already got a good base. If you give Claude Code something like *"make this UI better"*, it'll probably rewrite half the project and you'll lose time.

Instead, when you're ready, give Claude Code **small, constrained tasks** like:

> "Refactor Interview.tsx into these five components without changing the visual design."

That's much safer.

And **I would handle the AI interviewer architecture with you**, because that's where the actual hackathon differentiation is: using the candidate's attempts/skips/signals + curriculum to decide **what to ask, when to follow up, how deeply to probe, and what feedback to produce**. The supplied curriculum explicitly contains learning objectives and tools per day, which gives us enough structure to build a genuinely curriculum-aware interviewer. 

If you send me the **current `src` folder (or zip the frontend)**, I can go through what your teammate actually wrote and tell you **exactly which files to keep, which to modify, which components to create, and what code should go in each** rather than guessing from the screenshots.

## Prompt no : 9
**Ai Tool : Chatgpt**
**Author : Krishnakant Sharma**

### Prompt : 
i want u to give me prompt for cursor, so that it can enhance the existing frontend and ui, and also use the components as and when needed, it has access to the project so i prefer cursor over claude

### Outcome : 
Absolutely. Since **Cursor has the whole repo context**, I’d use it rather than generating a new frontend. The key is to tell Cursor **not to rebuild what already works**, but to audit the existing UI, preserve the visual identity, and improve it systematically.

Paste this as your **first Cursor Agent prompt**:

```text
You are working on an existing React + TypeScript + Vite frontend for a hackathon project called "KY² Interview Agent".

IMPORTANT:
This is an EXISTING frontend created by another team member. Do NOT rebuild the application from scratch and do NOT replace the current design with a generic template.

Your job is to AUDIT, ENHANCE, and REFACTOR the existing frontend while preserving its current visual identity.

PROJECT CONTEXT
----------------
The product is an AI Technical Interview Agent for a 31-day AI engineering cohort.

The system will eventually:
- Analyze a candidate's curriculum progress
- Personalize the interview based on completed, failed, skipped, and repeatedly-attempted topics
- Conduct a multi-turn technical interview
- Ask adaptive follow-up questions based on previous answers
- Maintain conversation context
- Complete at least 8 questions across at least 4 curriculum days
- Produce structured feedback at the end

The frontend currently has:
- A landing/home page
- Candidate selection/profile cards
- Interview page
- Feedback page
- Existing layouts/pages and custom styling

There is currently NO backend/API integration. Do not implement the backend in this task.

CORE OBJECTIVE
--------------
Make the existing frontend look and feel like a polished, premium enterprise AI interviewing product suitable for a hackathon final demo.

The current visual direction is already good:
- dark-first interface
- navy/black background
- subtle blue/lavender accents
- minimal enterprise aesthetic
- clean typography
- restrained use of borders/cards

PRESERVE THIS VISUAL LANGUAGE.

Do NOT turn it into:
- a generic SaaS template
- a colorful dashboard
- a generic ChatGPT clone
- an over-animated landing page
- a glassmorphism-heavy design
- a gradient-heavy AI website

FIRST: INSPECT THE PROJECT
---------------------------
Before changing anything:

1. Inspect the entire src/ directory.
2. Inspect package.json.
3. Inspect the existing routing.
4. Inspect existing pages.
5. Inspect existing layouts.
6. Inspect existing components.
7. Inspect existing CSS/Tailwind configuration.
8. Identify which components/styles are reusable.
9. Identify duplicated UI code.
10. Identify anything that should be moved from pages into reusable components.

Do NOT modify files until you understand the current architecture.

After inspection, give yourself a short internal implementation plan and then execute it.

DO NOT:
- delete working pages
- replace the project with a new template
- change the framework
- introduce unnecessary dependencies
- install a new UI library if an equivalent existing component already exists
- rewrite package.json unnecessarily
- modify backend files
- create fake API endpoints
- hardcode the final backend architecture

COMPONENT ARCHITECTURE
----------------------
Improve the existing component structure where useful.

Use reusable components for repeated UI patterns.

A reasonable structure is:

src/
├── components/
│   ├── common/
│   ├── candidate/
│   ├── interview/
│   ├── feedback/
│   └── ui/
├── layouts/
├── pages/
├── services/
├── hooks/
├── types/
├── utils/
└── constants/

Do NOT blindly create every folder above if the existing project already has a good equivalent.

Pages should become relatively thin composition layers.

For example:

Home page:
- Hero
- HowItWorks
- CTA

Candidate page:
- Search/filter controls
- CandidateGrid
- CandidateCard

Interview page:
- InterviewHeader
- Conversation
- MessageBubble
- AnswerInput
- InterviewProgress
- InterviewSidebar

Feedback page:
- FeedbackHeader
- OverallScore
- SkillBreakdown
- Strengths
- Gaps
- CurriculumRecommendations

Use existing custom components where they already look good.

Use shadcn/ui components where they genuinely improve consistency or accessibility:
- Button
- Card
- Badge
- Progress
- Input
- Textarea
- Tooltip
- Dialog
- Separator
etc.

Do NOT convert every element into shadcn just because shadcn is installed.

HOME PAGE
---------
Improve the existing landing page without changing its core concept.

Keep the existing messaging around:

"Your learning journey.
Your interview."

Strengthen the visual hierarchy and make the product flow immediately understandable.

Add/improve a concise visual explanation:

1. Learning journey
2. Personalized interview
3. Adaptive follow-ups
4. Actionable feedback

The page should immediately communicate:
"This interviewer understands what I learned and adapts to how I answer."

Avoid excessive empty space while keeping the premium minimalist aesthetic.

Add subtle motion only where it improves the experience.

CANDIDATE SELECTION
-------------------
Improve the candidate selection interface.

Candidate cards should clearly prioritize:

- Candidate name
- Job role
- Experience
- Education
- Cohort progress
- Strength
- Focus area
- Relevant learning signals

Use the candidate data already present in the project/mock data.

Do not expose every raw mission on the card.

Add:
- candidate search
- useful filtering if the existing architecture supports it
- clear selected/hover states
- responsive grid
- consistent card heights
- clear "Prepare interview" CTA

Consider displaying a compact learning progress indicator such as:

"27 missions completed"
"15 first-try completions"
"25 active commit days"

where that data exists.

INTERVIEW PAGE — HIGHEST PRIORITY
---------------------------------
This page needs the biggest UX improvement.

The interview should visually feel like a REAL CONVERSATIONAL TECHNICAL INTERVIEW rather than:

question → textbox → next question

Convert the experience into a conversation timeline.

Example:

AI INTERVIEWER

AI:
"Explain how RAG helps address outdated model knowledge."

Candidate:
"It retrieves relevant information..."

AI:
"Good. You mentioned retrieval. How would you decide between vector search and structured database lookup?"

This conversation structure must be represented visually.

Create reusable components such as:

- MessageList
- MessageBubble
- InterviewHeader
- InterviewProgress
- AnswerInput
- FollowUpIndicator
- InterviewSidebar

Messages should visually distinguish:
- interviewer
- candidate

Add:
- question number
- total questions
- progress indicator
- current topic
- interview state
- loading/typing state
- disabled state while submitting
- textarea auto-resize if appropriate
- Enter/Shift+Enter behavior if appropriate

The interface should support future API-driven messages without requiring a redesign.

IMPORTANT:
Do NOT hardcode the interview to a static array of 8 questions.

The backend will eventually determine the next question.

The frontend should instead be designed around an interview state such as:

sessionId
questionNumber
totalQuestions
messages
currentTopic
isLoading
done

FOLLOW-UP VISUALIZATION
-----------------------
Make adaptive follow-ups visually understandable.

When a question is a follow-up, optionally show a subtle indicator such as:

↳ FOLLOW-UP

or

"Based on your previous answer"

This should be subtle and professional.

Do NOT expose hidden chain-of-thought or internal model reasoning.

Do NOT display things like:
"AI confidence: 72%"
"Reasoning tokens"
"Model thought process"

The user should only see useful interview information.

INTERVIEW SIDEBAR
-----------------
The existing sidebar can be improved.

Show:

INTERVIEW PROGRESS
Question 3 / 8

CURRENT FOCUS
Retrieval & RAG

INTERVIEW MODE
Adaptive

SESSION
Technical Interview

Avoid exposing unnecessary internal AI reasoning.

If useful, add a small tooltip or "Why this question?" interaction that explains the high-level personalization reason without revealing chain-of-thought.

FEEDBACK PAGE
-------------
Keep the existing strong feedback visual design, but make the information hierarchy clearer.

The final feedback should support:

- overall score
- summary
- strengths
- gaps
- next/recommended learning
- skill breakdown
- curriculum/topic references

The backend will eventually return at minimum:

{
  "summary": "string",
  "strengths": [],
  "gaps": [],
  "next": []
}

Design the frontend so these values can later be plugged in directly.

Do not depend on mock values being permanently hardcoded.

Improve the feedback page with a clear narrative:

1. Overall performance
2. What the candidate did well
3. Where they struggled
4. What to learn next

Add curriculum context where useful, e.g.:

Strong:
Day 7 — Embeddings

Needs work:
Day 12 — Prompt Engineering

Recommended:
Day 28 — Deployment

Do not make the page excessively dense.

RESPONSIVENESS
--------------
Test all important pages at:
- desktop
- tablet
- mobile

Fix:
- overflow
- text wrapping
- cards becoming too narrow
- sidebar behavior
- textarea sizing
- navigation
- buttons
- spacing

The interview screen must remain usable on smaller screens.

ACCESSIBILITY
-------------
Improve:
- keyboard navigation
- focus states
- button labels
- textarea labels
- semantic HTML
- sufficient contrast
- disabled/loading states

Do not sacrifice the existing visual style.

ANIMATION
---------
Use subtle animation only.

Good:
- page transitions
- message appearance
- progress changes
- hover states
- button feedback
- loading/typing indicator

Avoid:
- excessive floating animations
- huge entrance animations
- distracting effects
- animation on every element

Use the existing animation library if already installed.

TYPE SAFETY
-----------
Use TypeScript properly.

Create/reuse interfaces for:

Candidate
Mission
LearningSignals
InterviewMessage
InterviewState
Feedback
SkillScore

Do not use `any` unless absolutely unavoidable.

MOCK DATA
---------
Because there is currently no backend, keep the existing mock data necessary to demonstrate the frontend.

However, separate mock data from UI components.

For example:

src/
├── data/
│   ├── candidates.ts
│   └── mockInterview.ts

or use the project's existing equivalent.

The eventual API should be able to replace the mock service without rewriting components.

SERVICE LAYER
-------------
If one does not already exist, create a small abstraction such as:

src/services/interviewApi.ts

For now it can expose the expected interface without making real backend requests.

For example conceptually:

startInterview()
sendAnswer()
getFeedback()

Do NOT create fake backend routes.

Do NOT hardcode localhost API calls throughout components.

The goal is to make future integration clean.

IMPORTANT API CONTRACT
-----------------------
The backend will eventually expose:

POST /api/interview

The request will use a sessionId.

Initial request contains:
- sessionId
- candidate

Subsequent requests contain:
- sessionId
- message

Final response contains:
- reply
- done
- feedback

Design the frontend so this contract can be integrated later.

CODE QUALITY
------------
After implementation:

1. Remove duplicated styles/components where appropriate.
2. Remove unused imports.
3. Remove dead code.
4. Fix TypeScript errors.
5. Fix React warnings.
6. Ensure routing still works.
7. Ensure `npm run build` succeeds.
8. Ensure there are no console errors.
9. Do not leave broken imports.
10. Do not change unrelated configuration.

VERY IMPORTANT WORKFLOW
-----------------------
Work incrementally.

First inspect.

Then improve in this order:

1. Shared layout/components
2. Candidate selection
3. Interview experience
4. Feedback experience
5. Responsive behavior
6. Accessibility
7. Animation/polish
8. Cleanup/type safety

After each major stage, verify the app still runs.

Do not perform a giant destructive rewrite.

At the end, report:
- files created
- files modified
- major UX improvements
- dependencies added (if any)
- remaining TODOs for backend integration
- whether `npm run build` succeeds

The result should feel like a polished hackathon-winning AI interview product, while clearly remaining the same existing project rather than a completely different template.
```

### One important thing before you hit Enter

Because Cursor has the repo, **let it inspect first**. If it starts immediately changing 30 files without showing you what it found, stop it.

I'd actually do this in **two Cursor prompts** rather than one giant execution.

First, give it:

```text
Before making ANY changes, inspect the entire existing frontend.

Analyze:
- src structure
- pages
- layouts
- components
- routing
- styling
- package.json
- existing mock data
- existing candidate/interview/feedback implementation

Do not modify anything yet.

Tell me:
1. What is already good and should be preserved?
2. What should be refactored?
3. What components are missing?
4. What is currently preventing clean API integration?
5. What exact files you propose creating/modifying?
6. Any unnecessary dependencies or duplicated code?

Wait for my approval before editing.
```

**That's the one I'd start with.**

Then, once Cursor gives you its audit, paste the big enhancement prompt. This is safer because we don't know your teammate's actual implementation from the screenshots alone.

And yes — **Cursor is a better choice for this particular stage** because it can inspect the existing codebase and make targeted changes rather than generating a disconnected UI from scratch.

## Prompt no : 10
**Ai Tool : Cursor**
**Author : Krishnakant Sharma**

### Prompt : 
Before making ANY changes, inspect the entire existing frontend.

Analyze:
- src structure
- pages
- layouts
- components
- routing
- styling
- package.json
- existing mock data
- existing candidate/interview/feedback implementation

Do not modify anything yet.

Tell me:
1. What is already good and should be preserved?
2. What should be refactored?
3. What components are missing?
4. What is currently preventing clean API integration?
5. What exact files you propose creating/modifying?
6. Any unnecessary dependencies or duplicated code?

Wait for my approval before editing.

### Outcome : 
Here is a read-only audit of the current frontend. **Nothing was modified.**

---

## Current State Overview

The app is **functional as a mock prototype**, but it is **not wired to the real API contract** and sits alongside an **unfinished scaffold** (empty pages, unused shadcn/Tailwind stack).

### Active architecture (what actually runs)

```
main.tsx → App.tsx (monolithic state machine)
              ├── interviewGateway.ts (mock)
              ├── types.ts
              └── Given_Data/candidates.ts → candidates.json + curriculum.json
```

`main.tsx` renders only `App.tsx`. There is **no React Router**, **no layouts**, and **no page components** in use.

Flow is driven by local state in `App.tsx`:

| `page` value   | Screen        |
|----------------|---------------|
| `landing`      | Hero / CTA    |
| `candidates`   | Pick candidate|
| `setup`        | Pre-interview |
| `interview`    | Q&A loop      |
| `results`      | Feedback      |

Build succeeds (`tsc -b && vite build`, ~231 KB JS, ~4.5 KB CSS).

---

## 1. What is already good and should be preserved

**UX and visual design (`index.css` + `App.tsx`)**
- Cohesive dark theme (Manrope + DM Mono, radial gradient, responsive breakpoints).
- Complete end-to-end flow: landing → candidate select → setup → interview → results.
- Interview sidebar (progress dots, topic, difficulty) is well thought out.
- Results screen with skill bars, strengths, improvements, recommendations is polished.

**Domain modeling (`types.ts`)**
- Clear `Candidate`, `InterviewTurn`, and `Feedback` types.
- Good foundation for UI state, even if API shapes differ.

**Candidate data pipeline (`Given_Data/candidates.ts`)**
- Smart transformation from raw hackathon JSON into UI-friendly `Candidate` objects.
- Derives `strength` / `focus` from missions, attempts, and skipped days.
- Joins with `curriculum.json` for titles — this is real personalization logic worth keeping.

**Gateway abstraction (`interviewGateway.ts`)**
- `InterviewGateway` interface (`start`, `submit`, `feedback`) is the right seam for swapping mock → real API.
- Mock implementation gives a working demo without a backend.

**Tooling**
- Vite + React 19 + TypeScript, path alias `@/*`, oxlint — sensible baseline.
- `vite.config.ts` is minimal and correct.

---

## 2. What should be refactored

**`App.tsx` — monolith (~32 lines of dense JSX)**
- All 5 screens, nav, and inline helpers (`Feature`, `Info`) live in one file.
- Uses string-literal page state instead of routes.
- Hard to test, extend, or share state cleanly.

**Dual styling systems (conflict)**
- **Active:** plain CSS classes in `index.css` (`.hero`, `.candidate`, `.interview-shell`, etc.).
- **Inactive:** Tailwind + shadcn in `components/ui/*`, but Tailwind is never imported in CSS (`index.css` has no `@import "tailwindcss"`), and shadcn tokens (`bg-card`, `text-muted-foreground`) would not work without theme setup.
- `components.json` points to missing `src/App.css`.

**Empty scaffold files (misleading structure)**
These exist but are **0 bytes** and unused:
- `pages/Home.tsx`, `pages/Interview.tsx`, `pages/Feedback.tsx`
- `layouts/MainLayout.tsx`
- `components/common/Navbar.tsx`, `PageContainer.tsx`
- `services/api.ts`, `services/interview.ts`

**Type / API mismatch**
Frontend types do not align with `technical-spec.md`:

| Concern | Frontend (`types.ts` / mock) | API spec |
|--------|------------------------------|----------|
| Turn shape | `question`, `topic`, `difficulty`, `current`, `total`, `evaluatorNote` | `{ reply, done }` |
| Feedback | `overall`, `skills[]`, `strengths`, `improvements`, `recommendations` | `{ summary, strengths, gaps, next }` |
| Session | None | `sessionId` on every request |
| Start payload | `Candidate` (UI shape) | Full raw `candidate.json` object |
| End signal | `completed: true` on turn, then separate `feedback()` call | `done: true` + inline `feedback` on same response |

**Mock gateway gaps**
- `start(candidate)` accepts `Candidate` but **ignores it** — same 8 hardcoded RAG questions for everyone.
- No conversation history; only an index counter.
- `feedback()` is decoupled from the last turn instead of arriving with `done: true`.

**Duplicate data locations**
- Authoritative copies used by code: `src/Given_Data/*`
- Extra copies at `frontend/Given_Data/*` (git shows root `Given_Data/` deleted, frontend copies untracked)
- Risk of drift and confusion about source of truth.

---

## 3. What components are missing

**Feature / domain components (extracted from `App.tsx`)**
- `LandingHero` / feature grid
- `CandidateGrid` + `CandidateCard`
- `InterviewSetup` (curriculum signals + plan)
- `InterviewSession` (question, answer form, sidebar)
- `FeedbackResults` (scores, strengths, recommendations)
- `InterviewProgress` (dots / step indicator)
- `SkillBreakdown` (bar chart rows)

**Infrastructure components**
- `LoadingState` / `SubmittingOverlay`
- `ErrorBanner` / `ErrorBoundary`
- `EmptyState` (no candidates, failed load)

**API / session layer**
- `ApiInterviewGateway` implementing `InterviewGateway` (or replacing it)
- Session ID generator + persistence (in-memory or `sessionStorage`)
- Request/response mappers (API ↔ UI types)
- Optional: React Query hooks (`useStartInterview`, `useSubmitAnswer`)

**Routing shell (if adopting the scaffold)**
- Router setup in `main.tsx` or `App.tsx`
- `MainLayout` with shared header/nav
- Route guards (e.g. redirect if no candidate selected)

**Config**
- `.env` / `VITE_API_BASE_URL`
- Vite dev proxy to backend (`/api/interview`)

---

## 4. What is preventing clean API integration

1. **No HTTP client** — `services/api.ts` and `services/interview.ts` are empty; axios is installed but unused.

2. **No `sessionId` lifecycle** — spec requires the same ID on every `POST /api/interview`; nothing generates or stores it.

3. **Schema mismatch** — UI expects structured turns (`topic`, `difficulty`, question N of M); API returns free-text `reply` + `done`. You need either:
   - parsing/heuristics on `reply`, or
   - backend metadata extensions, or
   - UI adaptation to conversational `reply` strings.

4. **Feedback shape mismatch** — UI shows numeric `overall` and `skills[]`; API provides `summary`, `strengths`, `gaps`, `next`. Mapping layer required.

5. **Wrong candidate payload** — API expects the **raw** candidate object from JSON; UI sends the **transformed** `Candidate` type (missing `member`, `missions`, `signals`).

6. **Two-step feedback flow vs one-shot API** — mock calls `submit()` then `feedback()` separately; API embeds feedback in the final `{ done: true, feedback }` response.

7. **Gateway interface may need revision** — `submit` → `feedback` split doesn’t match a single conversational endpoint; consider `postMessage(sessionId, payload)` instead.

8. **No error/loading/retry handling** for network failures.

9. **No dev proxy** — frontend will hit CORS issues calling backend directly without Vite proxy config.

---

## 5. Proposed files to create/modify (awaiting your approval)

### Modify

| File | Purpose |
|------|---------|
| `src/App.tsx` | Slim router + providers; delegate to pages |
| `src/main.tsx` | Add `BrowserRouter`, optional `QueryClientProvider` |
| `src/types.ts` | Add API types + UI view-model types; keep mappers separate |
| `src/interviewGateway.ts` | Add `ApiInterviewGateway`; keep mock for dev fallback |
| `src/index.css` | Either keep as-is OR migrate to Tailwind — pick one stack |
| `vite.config.ts` | Add `/api` proxy to backend |
| `index.html` | Update title from `"frontend"` to product name |
| `package.json` | Remove unused deps OR commit to using them |

### Create

| File | Purpose |
|------|---------|
| `src/services/api.ts` | Axios/fetch client, base URL, error normalization |
| `src/services/interview.ts` | `POST /api/interview` with session management |
| `src/lib/session.ts` | Generate/persist `sessionId` |
| `src/lib/mappers.ts` | API response → UI models (turn metadata, feedback) |
| `src/hooks/useInterview.ts` | Interview state machine hook |
| `src/pages/Landing.tsx` | Extract landing from App |
| `src/pages/Candidates.tsx` | Candidate selection |
| `src/pages/Setup.tsx` | Pre-interview |
| `src/pages/Interview.tsx` | Live interview (replace empty file) |
| `src/pages/Feedback.tsx` | Results (replace empty file) |
| `src/layouts/MainLayout.tsx` | Shared header/nav |
| `src/components/interview/*` | Extracted UI pieces |
| `.env.example` | `VITE_API_BASE_URL=http://localhost:XXXX` |

### Delete or consolidate (recommended)

| Path | Reason |
|------|--------|
| `frontend/Given_Data/*` | Duplicate of `src/Given_Data/*` |
| Empty stub files | Either implement or remove to avoid confusion |
| Root `package.json` | Only contains `react-router-dom`; redundant with frontend |

### Optional (only if choosing shadcn/Tailwind path)

| File | Purpose |
|------|---------|
| `src/App.css` or update `index.css` | `@import "tailwindcss"` + CSS variables |
| Refactor pages to use `components/ui/*` | Align with installed design system |

---

## 6. Unnecessary dependencies and duplicated code

### Likely unused dependencies (installed, not imported in active app)

| Package | Status |
|---------|--------|
| `@tanstack/react-query` | Unused |
| `axios` | Unused (empty services) |
| `react-router-dom` | Unused (also duplicated in root `package.json`) |
| `react-hook-form` | Unused |
| `@hookform/resolvers` | Unused |
| `zod` | Unused |
| `framer-motion` | Unused |
| `@fontsource-variable/geist` | Unused |
| `shadcn` (CLI package) | Dev/scaffold only; not runtime |
| `@tailwindcss/vite`, `tailwindcss`, `tw-animate-css` | Configured but CSS never loaded |
| `@base-ui/react`, `class-variance-authority`, `lucide-react` | Only used by unused shadcn components |

**Bundle proof:** production build transforms only **20 modules** — shadcn stack is tree-shaken out entirely.

### Duplicated / dead code

- **`App.tsx` UI vs empty `pages/*`** — same screens planned twice; only App implements them.
- **`Given_Data` in two places** — `src/Given_Data/` (used) vs `frontend/Given_Data/` (orphan).
- **Two nav patterns** — inline `<header className="nav">` in App vs empty `Navbar.tsx`.
- **Mock questions** — hardcoded RAG set unrelated to selected candidate’s curriculum days.
- **`Feature` / `Info` helpers** — inline in App; would become shared components on refactor.

---

## Recommended direction (for your decision)

Two viable paths:

**A. Minimal API hookup (smallest diff)**  
Keep current CSS/UI, implement `ApiInterviewGateway` + mappers, add session + proxy. Refactor `App.tsx` into files later.

**B. Full scaffold completion (cleaner long-term)**  
Wire React Router + pages, pick **one** styling system (I'd lean **keep custom CSS** since it's already polished, and remove unused Tailwind/shadcn unless you want that design system), implement services layer, map API types explicitly.

---

Tell me which path you prefer (A minimal, B full refactor, or a hybrid), and whether to **keep the current visual design** or **migrate to shadcn/Tailwind**. I’ll wait for your approval before editing anything.

## Prompt no : 11
**Ai Tool : Chatgpt**
**Author : Krishnakant Sharma**

### Prompt : 
Pasted markdown.md
File
this is what cursor gave : 
tell me what to do next think twice

### Outcome : 
Yes. I read Cursor's audit carefully, and **this changes my recommendation slightly**.

Your teammate's frontend is actually better structured conceptually than we thought from the screenshots, because it already has a useful `InterviewGateway` abstraction and the candidate transformation logic. The problem is that the project has **two competing architectures**: the working `App.tsx` prototype and the unused `pages/layouts/shadcn` scaffold. 

### My verdict: choose **Hybrid**, not A or B.

**Do not migrate to Tailwind/shadcn. Do not rewrite the UI.**

But also **don't just slap the API onto the current monolithic App.tsx**.

You have 48 hours. We want:

```text
KEEP current visual design
        +
clean up architecture
        +
align exactly with API contract
        +
prepare frontend for real AI
```

The current custom CSS is already polished and working, while Tailwind/shadcn is effectively unused. Cursor specifically confirmed that the current production build doesn't even use the shadcn stack.  

---

# What you should do next

## Phase 1 — DO THIS NOW

Tell Cursor to perform a **controlled hybrid refactor**.

Do **not** tell it to enhance the UI again yet.

We need to fix the foundation first.

Paste this into Cursor:

```text
Proceed with a HYBRID refactor.

IMPORTANT: Do NOT migrate the project to Tailwind/shadcn.
Keep the existing custom CSS and visual design exactly as the primary design system.

Do NOT rebuild the UI from scratch.

The goal is to cleanly separate the existing working prototype into reusable pages/components and prepare it for the real backend API.

EXECUTE THE FOLLOWING:

1. PRESERVE CURRENT VISUAL DESIGN

Keep:
- existing dark theme
- typography
- colors
- spacing system
- cards
- buttons
- interview layout
- candidate cards
- feedback design
- existing responsive behavior

Do not redesign the application during this task.

2. REMOVE ARCHITECTURAL DUPLICATION

The current active application is App.tsx, while pages/, layouts/, and some components are empty unused scaffolding.

Refactor the working UI into the existing intended structure.

Create/use:

src/pages/
  Landing.tsx
  Candidates.tsx
  Setup.tsx
  Interview.tsx
  Feedback.tsx

src/layouts/
  MainLayout.tsx

src/components/
  common/
  candidate/
  interview/
  feedback/

Do not create unnecessary abstractions.

3. APP.TSX

Make App.tsx a thin application/router layer.

Use React Router because react-router-dom is already installed.

Routes:

/
 /candidates
 /setup
 /interview
 /feedback

Preserve the current user flow.

Do not introduce authentication or route guards requiring a backend.

4. CANDIDATE DATA

KEEP src/Given_Data as the authoritative source.

Do NOT use the duplicate frontend/Given_Data copy.

Delete/consolidate the duplicate only after verifying it is not referenced.

IMPORTANT:

The UI Candidate type is a view model.

The API requires the RAW candidate object from candidates.json.

Therefore preserve both concepts:

RawCandidate
CandidateViewModel

Do NOT change the raw candidate data structure just to fit the UI.

5. INTERVIEW GATEWAY

KEEP the existing InterviewGateway abstraction.

Refactor it so that it represents the real API contract.

The gateway should conceptually support:

startInterview(sessionId, rawCandidate)

sendMessage(sessionId, message)

Do NOT keep a separate feedback() API call.

The real API returns feedback together with the final response.

Keep the mock implementation so the frontend remains runnable before the backend exists.

6. API TYPES

Create explicit API types.

For example:

InterviewStartRequest
InterviewMessageRequest
InterviewResponse
InterviewFeedback

The API response is:

{
  reply: string,
  done: boolean,
  feedback?: {
    summary: string,
    strengths: string[],
    gaps: string[],
    next: string[]
  }
}

Do not force the API response into the current UI's InterviewTurn shape.

Use a mapper/view-model layer instead.

7. SESSION MANAGEMENT

Create:

src/lib/session.ts

It should:
- generate a UUID sessionId
- persist it in sessionStorage
- allow starting a fresh interview
- allow retrieving the active session

Do not use localStorage.

Do not create persistent user accounts.

8. API SERVICE

Create:

src/services/api.ts

and:

src/services/interview.ts

Use axios if it is already installed.

Do not scatter axios/fetch calls throughout React components.

The only backend endpoint needed is:

POST /api/interview

Do not create additional frontend assumptions.

9. FRONTEND INTERVIEW STATE

Create:

src/hooks/useInterview.ts

The hook should manage:

sessionId
candidate
messages
questionNumber
totalQuestions
isLoading
error
done
feedback

The UI should NOT know how the AI decides the next question.

It simply receives the next interviewer reply from the gateway.

10. IMPORTANT API CONTRACT DETAIL

The API specification only guarantees:

reply
done
feedback on completion

Therefore DO NOT fabricate backend-only metadata such as:
- actual AI difficulty
- actual topic selected by the AI
- AI confidence
- hidden reasoning
- evaluator score

The existing UI can display generic interview progress.

If topic/difficulty metadata is later intentionally added to the backend contract, we can integrate it separately.

For now, do not pretend the frontend knows something the API does not return.

11. MOCK MODE

Keep the current mock gateway.

Update it so that it behaves like the real API:

start:
returns:
{
  reply: "...",
  done: false
}

subsequent messages:
returns:
{
  reply: "...",
  done: false
}

final:
returns:
{
  reply: "Interview completed.",
  done: true,
  feedback: {
    summary: "...",
    strengths: [...],
    gaps: [...],
    next: [...]
  }
}

The mock should maintain conversation history instead of only incrementing an index.

12. FEEDBACK

Update the frontend feedback model to consume:

summary
strengths
gaps
next

The existing visual score/skill breakdown can remain temporarily as mock/demo-only presentation data, but clearly separate it from the actual API feedback fields.

Do NOT require the backend to return fields that the official API contract does not specify.

13. ERROR / LOADING STATES

Add reusable:
- LoadingState
- ErrorBanner
- Retry button

The interview should handle:
- network failure
- empty response
- duplicate submit
- backend error

Disable the submit button while a request is active.

14. VITE PROXY

Do NOT hardcode a backend port unless one is already defined in the project.

Prepare vite.config.ts for:

/api → backend

but use a clearly marked placeholder if the backend port is not known yet.

Also create:

.env.example

with:

VITE_API_BASE_URL=

Do not create a fake backend.

15. DEPENDENCIES

Do NOT add new dependencies unless genuinely necessary.

Keep the existing custom CSS.

Do not activate Tailwind/shadcn merely because the packages exist.

Do not remove existing dependencies in this task unless they are definitely causing a problem.

We can clean unused dependencies after the architecture is stable.

16. VALIDATION

After completing the refactor:

- npm run build
- verify all routes work
- verify mock interview still works end-to-end
- verify candidate selection works
- verify feedback works
- verify refresh does not produce broken imports
- verify there are no TypeScript errors
- verify no console errors

DO NOT redesign anything.

At the end provide:
1. files created
2. files modified
3. files deleted
4. API contract alignment changes
5. remaining backend integration TODOs
6. build result
```

---

# Why this is the right move

Cursor identified a **very important problem**:

Your current mock does this:

```text
start()
   ↓
8 hardcoded RAG questions
   ↓
submit()
   ↓
feedback()
```

It doesn't actually use the candidate to determine the questions. 

That is exactly what we **don't** want to accidentally preserve.

The real architecture needs to become:

```text
Candidate
   ↓
POST /api/interview
   ↓
AI Interviewer
   ↓
reply
   ↓
Candidate answer
   ↓
POST /api/interview
   ↓
AI evaluates context
   ↓
next reply
   ↓
...
   ↓
done:true + feedback
```

The technical specification explicitly requires the same `sessionId` throughout the conversation. 

---

# One thing Cursor got VERY right

This:

> **Don't force the API response into the current UI's InterviewTurn shape.**

Absolutely.

Your current frontend expects:

```typescript
{
  question,
  topic,
  difficulty,
  current,
  total
}
```

But the actual backend gives:

```json
{
  "reply": "...",
  "done": false
}
```

and eventually:

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

That's straight from the technical specification.  

So don't make the frontend pretend the backend sends things it doesn't.

---

# ⚠️ And don't do this yet

Cursor suggested potentially adding React Query.

**Don't.**

You have:

```text
1 endpoint
1 conversation
1 session
```

You don't need React Query right now.

A simple:

```text
useInterview()
      ↓
interviewGateway
      ↓
axios
```

is completely sufficient.

Every extra abstraction is another place to debug during a 48-hour hackathon.

---

# What happens after Cursor finishes this

Then your project should look roughly like:

```text
src/
│
├── components/
│   ├── candidate/
│   │   ├── CandidateCard.tsx
│   │   └── CandidateGrid.tsx
│   │
│   ├── interview/
│   │   ├── InterviewHeader.tsx
│   │   ├── MessageList.tsx
│   │   ├── MessageBubble.tsx
│   │   ├── AnswerInput.tsx
│   │   └── InterviewProgress.tsx
│   │
│   ├── feedback/
│   │   ├── SkillBreakdown.tsx
│   │   ├── Strengths.tsx
│   │   └── Recommendations.tsx
│   │
│   └── common/
│       ├── LoadingState.tsx
│       └── ErrorBanner.tsx
│
├── pages/
│   ├── Landing.tsx
│   ├── Candidates.tsx
│   ├── Setup.tsx
│   ├── Interview.tsx
│   └── Feedback.tsx
│
├── layouts/
│   └── MainLayout.tsx
│
├── hooks/
│   └── useInterview.ts
│
├── services/
│   ├── api.ts
│   └── interview.ts
│
├── lib/
│   ├── session.ts
│   └── mappers.ts
│
├── Given_Data/
│
├── types.ts
├── App.tsx
└── main.tsx
```

**But don't obsess over matching this exact tree.** Cursor should adapt it to the actual code.

---

# Then comes YOUR actual job: the AI

This is where I would **not** ask Cursor to start inventing things yet.

Once this refactor is done, your three-person split becomes:

### Teammate 1 — Backend

```text
FastAPI
POST /api/interview
session management
LLM connection
```

### You — AI

```text
Candidate analysis
       ↓
Interview planning
       ↓
Question generation
       ↓
Answer evaluation
       ↓
Adaptive follow-up
       ↓
Feedback generation
```

### You + frontend teammate

```text
API
 ↓
useInterview()
 ↓
Conversation UI
 ↓
Feedback UI
```

And the candidate data gives us **excellent signals** to work with: completed missions, skipped topics, failed attempts, number of attempts, commit days, etc. 

---

# One more important decision: don't implement "five AI agents"

I want to correct something from my earlier recommendation.

For a **48-hour hackathon**, I would **not** build:

```text
Candidate Agent
Question Agent
Evaluator Agent
Difficulty Agent
Feedback Agent
```

as five separate LLM agents.

That's unnecessary complexity.

Instead:

```text
              Interview Agent
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
   Candidate    Interview    Evaluation
    Context       State       Logic
        │           │           │
        └───────────┼───────────┘
                    ↓
                   LLM
```

One stateful interviewer with structured stages.

If you use LangGraph, those stages can be nodes. If not, ordinary Python state management is enough.

---

## So your immediate next action is very clear:

**Run the hybrid refactor prompt above in Cursor.**

Don't let it redesign anything.

Once Cursor finishes, **paste its change summary/output here**. Then we'll do the next step: designing the **actual interview-agent state machine + prompt + candidate-personalization algorithm** before anyone starts wiring random LLM calls.

That part is where we can make this considerably stronger than a basic "LLM asks 8 questions" submission.


## Prompt no : 12
**Ai Tool : Cursor**
**Author : Krishnakant Sharma**

### Prompt : 
Proceed with a HYBRID refactor.

IMPORTANT: Do NOT migrate the project to Tailwind/shadcn.
Keep the existing custom CSS and visual design exactly as the primary design system.

Do NOT rebuild the UI from scratch.

The goal is to cleanly separate the existing working prototype into reusable pages/components and prepare it for the real backend API.

EXECUTE THE FOLLOWING:

1. PRESERVE CURRENT VISUAL DESIGN

Keep:
- existing dark theme
- typography
- colors
- spacing system
- cards
- buttons
- interview layout
- candidate cards
- feedback design
- existing responsive behavior

Do not redesign the application during this task.

2. REMOVE ARCHITECTURAL DUPLICATION

The current active application is App.tsx, while pages/, layouts/, and some components are empty unused scaffolding.

Refactor the working UI into the existing intended structure.

Create/use:

src/pages/
  Landing.tsx
  Candidates.tsx
  Setup.tsx
  Interview.tsx
  Feedback.tsx

src/layouts/
  MainLayout.tsx

src/components/
  common/
  candidate/
  interview/
  feedback/

Do not create unnecessary abstractions.

3. APP.TSX

Make App.tsx a thin application/router layer.

Use React Router because react-router-dom is already installed.

Routes:

/
 /candidates
 /setup
 /interview
 /feedback

Preserve the current user flow.

Do not introduce authentication or route guards requiring a backend.

4. CANDIDATE DATA

KEEP src/Given_Data as the authoritative source.

Do NOT use the duplicate frontend/Given_Data copy.

Delete/consolidate the duplicate only after verifying it is not referenced.

IMPORTANT:

The UI Candidate type is a view model.

The API requires the RAW candidate object from candidates.json.

Therefore preserve both concepts:

RawCandidate
CandidateViewModel

Do NOT change the raw candidate data structure just to fit the UI.

5. INTERVIEW GATEWAY

KEEP the existing InterviewGateway abstraction.

Refactor it so that it represents the real API contract.

The gateway should conceptually support:

startInterview(sessionId, rawCandidate)

sendMessage(sessionId, message)

Do NOT keep a separate feedback() API call.

The real API returns feedback together with the final response.

Keep the mock implementation so the frontend remains runnable before the backend exists.

6. API TYPES

Create explicit API types.

For example:

InterviewStartRequest
InterviewMessageRequest
InterviewResponse
InterviewFeedback

The API response is:

{
  reply: string,
  done: boolean,
  feedback?: {
    summary: string,
    strengths: string[],
    gaps: string[],
    next: string[]
  }
}

Do not force the API response into the current UI's InterviewTurn shape.

Use a mapper/view-model layer instead.

7. SESSION MANAGEMENT

Create:

src/lib/session.ts

It should:
- generate a UUID sessionId
- persist it in sessionStorage
- allow starting a fresh interview
- allow retrieving the active session

Do not use localStorage.

Do not create persistent user accounts.

8. API SERVICE

Create:

src/services/api.ts

and:

src/services/interview.ts

Use axios if it is already installed.

Do not scatter axios/fetch calls throughout React components.

The only backend endpoint needed is:

POST /api/interview

Do not create additional frontend assumptions.

9. FRONTEND INTERVIEW STATE

Create:

src/hooks/useInterview.ts

The hook should manage:

sessionId
candidate
messages
questionNumber
totalQuestions
isLoading
error
done
feedback

The UI should NOT know how the AI decides the next question.

It simply receives the next interviewer reply from the gateway.

10. IMPORTANT API CONTRACT DETAIL

The API specification only guarantees:

reply
done
feedback on completion

Therefore DO NOT fabricate backend-only metadata such as:
- actual AI difficulty
- actual topic selected by the AI
- AI confidence
- hidden reasoning
- evaluator score

The existing UI can display generic interview progress.

If topic/difficulty metadata is later intentionally added to the backend contract, we can integrate it separately.

For now, do not pretend the frontend knows something the API does not return.

11. MOCK MODE

Keep the current mock gateway.

Update it so that it behaves like the real API:

start:
returns:
{
  reply: "...",
  done: false
}

subsequent messages:
returns:
{
  reply: "...",
  done: false
}

final:
returns:
{
  reply: "Interview completed.",
  done: true,
  feedback: {
    summary: "...",
    strengths: [...],
    gaps: [...],
    next: [...]
  }
}

The mock should maintain conversation history instead of only incrementing an index.

12. FEEDBACK

Update the frontend feedback model to consume:

summary
strengths
gaps
next

The existing visual score/skill breakdown can remain temporarily as mock/demo-only presentation data, but clearly separate it from the actual API feedback fields.

Do NOT require the backend to return fields that the official API contract does not specify.

13. ERROR / LOADING STATES

Add reusable:
- LoadingState
- ErrorBanner
- Retry button

The interview should handle:
- network failure
- empty response
- duplicate submit
- backend error

Disable the submit button while a request is active.

14. VITE PROXY

Do NOT hardcode a backend port unless one is already defined in the project.

Prepare vite.config.ts for:

/api → backend

but use a clearly marked placeholder if the backend port is not known yet.

Also create:

.env.example

with:

VITE_API_BASE_URL=

Do not create a fake backend.

15. DEPENDENCIES

Do NOT add new dependencies unless genuinely necessary.

Keep the existing custom CSS.

Do not activate Tailwind/shadcn merely because the packages exist.

Do not remove existing dependencies in this task unless they are definitely causing a problem.

We can clean unused dependencies after the architecture is stable.

16. VALIDATION

After completing the refactor:

- npm run build
- verify all routes work
- verify mock interview still works end-to-end
- verify candidate selection works
- verify feedback works
- verify refresh does not produce broken imports
- verify there are no TypeScript errors
- verify no console errors

DO NOT redesign anything.

At the end provide:
1. files created
2. files modified
3. files deleted
4. API contract alignment changes
5. remaining backend integration TODOs
6. build result

### Outcome : 
Hybrid refactor is complete. The existing visual design is preserved; the monolithic `App.tsx` is now split into routed pages with a clean API-ready layer underneath.

---

## 1. Files created

| File | Purpose |
|------|---------|
| `src/context/InterviewContext.tsx` | Shared interview state across routes |
| `src/hooks/useInterview.ts` | Session, messages, loading, error, feedback state |
| `src/lib/session.ts` | UUID + `sessionStorage` session management |
| `src/lib/mappers.ts` | Demo-only skill score presentation |
| `src/pages/Landing.tsx` | Hero / start CTA |
| `src/pages/Candidates.tsx` | Candidate selection |
| `src/pages/Setup.tsx` | Pre-interview setup |
| `src/pages/Interview.tsx` | Live Q&A |
| `src/pages/Feedback.tsx` | Results screen |
| `src/layouts/MainLayout.tsx` | Shared nav shell |
| `src/components/common/Feature.tsx` | Feature grid item |
| `src/components/common/LoadingState.tsx` | Reusable loading indicator |
| `src/components/common/ErrorBanner.tsx` | Error + retry |
| `src/components/candidate/CandidateCard.tsx` | Candidate card |
| `src/components/candidate/CandidateGrid.tsx` | Candidate grid |
| `src/components/interview/AnswerForm.tsx` | Answer textarea + submit |
| `src/components/interview/InterviewProgress.tsx` | Progress dots |
| `src/components/interview/InterviewSidebar.tsx` | Sidebar (generic progress only) |
| `src/components/feedback/SkillBreakdown.tsx` | Demo skill bars |
| `src/components/feedback/FeedbackResults.tsx` | Feedback layout |
| `.env.example` | `VITE_API_BASE_URL`, `VITE_USE_MOCK` |

---

## 2. Files modified

| File | Change |
|------|--------|
| `src/App.tsx` | Thin router: `/`, `/candidates`, `/setup`, `/interview`, `/feedback` |
| `src/types.ts` | `RawCandidate`, `CandidateViewModel`, API request/response types |
| `src/Given_Data/candidates.ts` | Exports raw + view model; lookup helpers |
| `src/interviewGateway.ts` | `startInterview` / `sendMessage`; mock + API implementations |
| `src/services/api.ts` | Axios client + error normalization |
| `src/services/interview.ts` | `POST /api/interview` |
| `src/index.css` | Error banner, loading spinner, demo note styles (no redesign) |
| `vite.config.ts` | `/api` proxy placeholder → `http://localhost:3000` |
| `index.html` | Title → "KY² Interview Agent" |

---

## 3. Files deleted

| File | Reason |
|------|--------|
| `src/pages/Home.tsx` | Empty stub; replaced by `Landing.tsx` |
| `src/components/common/Navbar.tsx` | Empty stub; nav lives in `MainLayout` |
| `src/components/common/PageContainer.tsx` | Empty stub; pages use existing `.container` classes |

`frontend/Given_Data/` was already absent — no duplicate to remove. Authoritative data remains in `src/Given_Data/`.

---

## 4. API contract alignment changes

| Before | After |
|--------|-------|
| `start(candidate)` → `InterviewTurn` | `startInterview(sessionId, rawCandidate)` → `InterviewResponse` |
| `submit(answer)` → `InterviewTurn` | `sendMessage(sessionId, message)` → `InterviewResponse` |
| Separate `feedback()` call | Feedback included when `done: true` |
| UI `Candidate` sent to gateway | Raw `RawCandidate` sent to API; `CandidateViewModel` for UI only |
| Fabricated topic/difficulty/evaluator notes | Removed — sidebar shows generic progress only |
| Feedback: `improvements`, `recommendations` | Mapped from API `gaps`, `next` |
| Skill scores from mock feedback | Demo-only via `buildDemoPresentation()` — labeled as not from API |

**Mock mode** (`VITE_USE_MOCK=true`, default): behaves like the real API contract with conversation history.

**Live mode** (`VITE_USE_MOCK=false`): uses `ApiInterviewGateway` → axios → `POST /api/interview`.

---

## 5. Remaining backend integration TODOs

1. Set backend port in `vite.config.ts` proxy target (currently `http://localhost:3000` placeholder).
2. Copy `.env.example` → `.env` and set `VITE_API_BASE_URL` for production.
3. Set `VITE_USE_MOCK=false` when the backend is ready.
4. Verify backend accepts raw `candidate.json` objects (not the view model).
5. Confirm backend returns `feedback` on the final `{ done: true }` response.
6. Test error paths: network failure, empty `reply`, missing `feedback` on completion.
7. Optional later: if backend adds metadata (topic, difficulty), integrate via mappers — not assumed today.

---

## 6. Build result

```
✓ tsc -b && vite build — SUCCESS
✓ 103 modules transformed
✓ 0 TypeScript errors
✓ 0 linter errors
dist/assets/index-nbqCwH7t.css    5.25 kB
dist/assets/index-CxKEBsJt.js   324.10 kB
```

---

## Architecture summary

```
App (Router)
 └── InterviewProvider (useInterview)
      └── MainLayout
           ├── Landing → Candidates → Setup → Interview → Feedback
           └── interviewGateway
                ├── MockInterviewGateway (default)
                └── ApiInterviewGateway (VITE_USE_MOCK=false)
                     └── services/interview.ts → POST /api/interview
```

Run locally with:

```bash
cd frontend
npm run dev
```

Mock interview works end-to-end without a backend. When you're ready to connect the real API, update the proxy target and flip `VITE_USE_MOCK=false`.

## Prompt no : 13
**Ai Tool : Chatgpt**
**Author : Krishnakant Sharma**

### Prompt : 
Hybrid refactor is complete. The existing visual design is preserved; the monolithic `App.tsx` is now split into routed pages with a clean API-ready layer underneath.

---

## 1. Files created

| File                                             | Purpose                                           |
| ------------------------------------------------ | ------------------------------------------------- |
| `src/context/InterviewContext.tsx`               | Shared interview state across routes              |
| `src/hooks/useInterview.ts`                      | Session, messages, loading, error, feedback state |
| `src/lib/session.ts`                             | UUID + `sessionStorage` session management        |
| `src/lib/mappers.ts`                             | Demo-only skill score presentation                |
| `src/pages/Landing.tsx`                          | Hero / start CTA                                  |
| `src/pages/Candidates.tsx`                       | Candidate selection                               |
| `src/pages/Setup.tsx`                            | Pre-interview setup                               |
| `src/pages/Interview.tsx`                        | Live Q&A                                          |
| `src/pages/Feedback.tsx`                         | Results screen                                    |
| `src/layouts/MainLayout.tsx`                     | Shared nav shell                                  |
| `src/components/common/Feature.tsx`              | Feature grid item                                 |
| `src/components/common/LoadingState.tsx`         | Reusable loading indicator                        |
| `src/components/common/ErrorBanner.tsx`          | Error + retry                                     |
| `src/components/candidate/CandidateCard.tsx`     | Candidate card                                    |
| `src/components/candidate/CandidateGrid.tsx`     | Candidate grid                                    |
| `src/components/interview/AnswerForm.tsx`        | Answer textarea + submit                          |
| `src/components/interview/InterviewProgress.tsx` | Progress dots                                     |
| `src/components/interview/InterviewSidebar.tsx`  | Sidebar (generic progress only)                   |
| `src/components/feedback/SkillBreakdown.tsx`     | Demo skill bars                                   |
| `src/components/feedback/FeedbackResults.tsx`    | Feedback layout                                   |
| `.env.example`                                   | `VITE_API_BASE_URL`, `VITE_USE_MOCK`              |

---

## 2. Files modified

| File                           | Change                                                               |
| ------------------------------ | -------------------------------------------------------------------- |
| `src/App.tsx`                  | Thin router: `/`, `/candidates`, `/setup`, `/interview`, `/feedback` |
| `src/types.ts`                 | `RawCandidate`, `CandidateViewModel`, API request/response types     |
| `src/Given_Data/candidates.ts` | Exports raw + view model; lookup helpers                             |
| `src/interviewGateway.ts`      | `startInterview` / `sendMessage`; mock + API implementations         |
| `src/services/api.ts`          | Axios client + error normalization                                   |
| `src/services/interview.ts`    | `POST /api/interview`                                                |
| `src/index.css`                | Error banner, loading spinner, demo note styles (no redesign)        |
| `vite.config.ts`               | `/api` proxy placeholder → `http://localhost:3000`                   |
| `index.html`                   | Title → "KY² Interview Agent"                                        |

---

## 3. Files deleted

| File                                      | Reason                                              |
| ----------------------------------------- | --------------------------------------------------- |
| `src/pages/Home.tsx`                      | Empty stub; replaced by `Landing.tsx`               |
| `src/components/common/Navbar.tsx`        | Empty stub; nav lives in `MainLayout`               |
| `src/components/common/PageContainer.tsx` | Empty stub; pages use existing `.container` classes |

`frontend/Given_Data/` was already absent — no duplicate to remove. Authoritative data remains in `src/Given_Data/`.

---

## 4. API contract alignment changes

| Before                                      | After                                                             |
| ------------------------------------------- | ----------------------------------------------------------------- |
| `start(candidate)` → `InterviewTurn`        | `startInterview(sessionId, rawCandidate)` → `InterviewResponse`   |
| `submit(answer)` → `InterviewTurn`          | `sendMessage(sessionId, message)` → `InterviewResponse`           |
| Separate `feedback()` call                  | Feedback included when `done: true`                               |
| UI `Candidate` sent to gateway              | Raw `RawCandidate` sent to API; `CandidateViewModel` for UI only  |
| Fabricated topic/difficulty/evaluator notes | Removed — sidebar shows generic progress only                     |
| Feedback: `improvements`, `recommendations` | Mapped from API `gaps`, `next`                                    |
| Skill scores from mock feedback             | Demo-only via `buildDemoPresentation()` — labeled as not from API |

**Mock mode** (`VITE_USE_MOCK=true`, default): behaves like the real API contract with conversation history.

**Live mode** (`VITE_USE_MOCK=false`): uses `ApiInterviewGateway` → axios → `POST /api/interview`.

---

## 5. Remaining backend integration TODOs

1. Set backend port in `vite.config.ts` proxy target (currently `http://localhost:3000` placeholder).
2. Copy `.env.example` → `.env` and set `VITE_API_BASE_URL` for production.
3. Set `VITE_USE_MOCK=false` when the backend is ready.
4. Verify backend accepts raw `candidate.json` objects (not the view model).
5. Confirm backend returns `feedback` on the final `{ done: true }` response.
6. Test error paths: network failure, empty `reply`, missing `feedback` on completion.
7. Optional later: if backend adds metadata (topic, difficulty), integrate via mappers — not assumed today.

---

## 6. Build result

```
✓ tsc -b && vite build — SUCCESS
✓ 103 modules transformed
✓ 0 TypeScript errors
✓ 0 linter errors
dist/assets/index-nbqCwH7t.css    5.25 kB
dist/assets/index-CxKEBsJt.js   324.10 kB
```

---

## Architecture summary

```
App (Router)
 └── InterviewProvider (useInterview)
      └── MainLayout
           ├── Landing → Candidates → Setup → Interview → Feedback
           └── interviewGateway
                ├── MockInterviewGateway (default)
                └── ApiInterviewGateway (VITE_USE_MOCK=false)
                     └── services/interview.ts → POST /api/interview
```

Run locally with:

```bash
cd frontend
npm run dev
```

Mock interview works end-to-end without a backend. When you're ready to connect the real API, update the proxy target and flip `VITE_USE_MOCK=false`.



it has made it so that visually there's no distinct change, but the architecture has changed significantly, now tell me what to do next should we start with the backend then?

### Outcome : 
Yes — **now is the right time to start the backend**, but with one important distinction:

> **Don't start by building the AI. Start by building the API contract + session/state layer.**
>
> In parallel, you and your teammate can design the AI interview logic.

The frontend refactor is in a good place now. The fact that the visual appearance barely changed is actually **exactly what we wanted**: we changed the architecture without risking the working demo. Cursor reports the build is clean and the frontend now has a gateway, session management, mappers, and API-ready state. 

---

# The order I'd follow now

```text
                    CURRENT STATE
                         │
                         ▼
              ┌────────────────────┐
              │  FRONTEND READY    │
              │  Mock API working  │
              └─────────┬──────────┘
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
      BACKEND MEMBER          YOU + AI MEMBER
             │                     │
             ▼                     ▼
       API + Session          Interview Logic
       State + LLM            Prompts + Evaluation
             │                     │
             └──────────┬──────────┘
                        ▼
                  INTEGRATION
                        │
                        ▼
                  REAL INTERVIEW
                        │
                        ▼
                 POLISH + DEMO
```

This is much better than having all three of you sit around waiting for one person to finish.

---

# Phase 1 — Backend skeleton first

Your backend member should build **only this first**:

```text
POST /api/interview
```

The specification is very explicit: there is one endpoint, no authentication is required, and `sessionId` must maintain state across requests. 

### First request

```json
{
  "sessionId": "abc-123",
  "candidate": { ...raw candidate... }
}
```

Backend should temporarily return:

```json
{
  "reply": "Welcome. Let's begin your interview.",
  "done": false
}
```

Exactly like the specification. 

### Second request

```json
{
  "sessionId": "abc-123",
  "message": "My answer..."
}
```

Return:

```json
{
  "reply": "Good. Can you explain why...",
  "done": false
}
```

Again, exactly matching the contract. 

### Final request

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

That's the contract you need to lock down. 

---

# Give your backend teammate this prompt

Assuming you're using **FastAPI + Python**, I'd send them this:

```text
Build the backend for our hackathon AI Interview Agent.

IMPORTANT:
Do NOT implement the LLM/AI logic yet.
First build and test the API contract and interview session infrastructure.

TECH STACK
----------
Python
FastAPI
Pydantic
Uvicorn

Keep dependencies minimal.

API CONTRACT
------------

Expose exactly:

POST /api/interview

No authentication.

The endpoint must maintain interview state using sessionId.

INITIAL REQUEST:

{
  "sessionId": "abc-123",
  "candidate": { ...raw candidate.json object... }
}

Response:

{
  "reply": "Welcome. Let's begin your interview.",
  "done": false
}

SUBSEQUENT REQUEST:

{
  "sessionId": "abc-123",
  "message": "Candidate's latest answer"
}

Response:

{
  "reply": "...",
  "done": false
}

FINAL RESPONSE:

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

SESSION MANAGEMENT
------------------
Create an in-memory session store initially.

Each session should contain at minimum:

sessionId
candidate
conversation history
question count
interview state

Use sessionId to retrieve the same session on every request.

Do NOT use a database yet.

We can add persistence later only if necessary.

CANDIDATE
---------
The candidate object received from the frontend must be the RAW candidate.json structure.

Do not require the frontend CandidateViewModel.

Load/validate the supplied candidate schema.

CURRICULUM
----------
Load the supplied curriculum.json.

Create a clean service for accessing curriculum information.

Do not implement sophisticated retrieval yet.

MOCK INTERVIEW ENGINE
---------------------
Before adding an LLM, implement a deterministic mock interview engine.

It should:

1. Start an interview.
2. Ask a question.
3. Accept an answer.
4. Store the answer in conversation history.
5. Return another question.
6. Continue for at least 8 questions.
7. Finish with done=true and feedback.

Make sure the question sequence spans at least 4 curriculum days.

Do NOT make the mock questions identical for every candidate if simple candidate-specific selection can be implemented from the supplied data.

ARCHITECTURE
------------

backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── interview.py
│   ├── schemas/
│   │   └── interview.py
│   ├── services/
│   │   ├── session.py
│   │   ├── candidate.py
│   │   └── curriculum.py
│   ├── interview/
│   │   └── engine.py
│   └── data/
│       ├── candidates.json
│       └── curriculum.json
│
├── requirements.txt
└── .env.example

Keep business logic out of the FastAPI route.

CORS
----
Allow the Vite frontend during development.

For example localhost:5173.

ERROR HANDLING
--------------
Return sensible HTTP errors for:

- missing sessionId
- unknown sessionId
- invalid candidate
- missing message
- malformed request

Do not expose internal stack traces.

TESTING
-------
Create basic tests for:

1. Start interview
2. Continue interview
3. Same sessionId maintains history
4. Unknown sessionId
5. Interview completion
6. Final feedback structure

Also verify:

POST /api/interview

works with curl/Postman.

IMPORTANT:
Do not implement OpenAI/Gemini/Claude calls yet.

The immediate goal is to prove:

React
  ↓
POST /api/interview
  ↓
FastAPI
  ↓
Session state
  ↓
Mock interviewer
  ↓
JSON response
  ↓
React
```

---

# Meanwhile, YOU should start the AI design

This is the important part.

**Don't wait for the backend to finish.**

You can design the AI engine independently because we already know exactly what the backend has to eventually produce.

I would structure the AI as **one Interview Agent with several logical stages**, not five separate agents.

```text
                 INTERVIEW AGENT
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
 Candidate         Interview       Evaluation
 Analyzer            Planner         Logic
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                Question Generator
                       │
                       ▼
                  Candidate Answer
                       │
                       ▼
                  Answer Evaluator
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        Follow-up             New Topic
             │                   │
             └─────────┬─────────┘
                       ▼
                  Next Question
```

---

# And this is where your candidate data becomes powerful

The candidate JSON isn't just there to display a name.

It has learning signals, missions, attempts, skipped topics, etc. Cursor already identified that the existing frontend derives strength/focus from this data. 

The curriculum gives you the other half: modules, days, topics, objectives, and tools. 

So your AI pipeline should be:

```text
RAW CANDIDATE
      +
CURRICULUM
      ↓
Candidate Profile
      ↓
Strengths
Weak Areas
Skipped Areas
High-attempt Areas
      ↓
Interview Plan
      ↓
8+ Questions
across 4+ days
      ↓
Adaptive Interview
      ↓
Evaluation
      ↓
Feedback
```

That's your differentiator.

---

# Don't start with LangGraph yet

I'd actually hold off on it.

First make the logic work conceptually:

```python
session = {
    "candidate": ...,
    "plan": ...,
    "messages": [...],
    "current_question": 3,
    "evaluations": [...]
}
```

Then:

```text
answer
 ↓
evaluate(answer)
 ↓
should_follow_up?
 ↓
yes → generate_follow_up()
no  → generate_next_question()
```

Once that's working, **then** decide whether LangGraph genuinely makes the implementation cleaner.

For 48 hours, simple Python state management may be enough.

---

# Your AI work should start with the Interview Plan

Before asking the LLM to generate questions, make it produce a structured plan.

Something like:

```json
{
  "totalQuestions": 8,
  "curriculumDays": [7, 10, 12, 22],
  "questions": [
    {
      "day": 7,
      "topic": "Embeddings",
      "purpose": "core understanding",
      "difficulty": "foundation"
    },
    {
      "day": 10,
      "topic": "Retrieval",
      "purpose": "application",
      "difficulty": "intermediate"
    }
  ]
}
```

Then the actual interviewer operates from that plan.

This prevents the LLM from going:

> "Hmm... RAG sounds cool, let me ask 8 random RAG questions."

😂

---

# Your 8-question structure

I'd use:

```text
Q1  → Core concept
Q2  → Core concept + application
Q3  → Deeper reasoning
Q4  → Scenario/application
Q5  → Adaptive follow-up
Q6  → Different curriculum topic
Q7  → Weak-area probe
Q8  → Challenging synthesis question
```

And **Q5/Q7 aren't necessarily fixed follow-ups**.

The AI decides.

---

# Example of what makes your agent impressive

Candidate profile:

```text
Strong:
Embeddings

Weak:
Prompt Engineering

High attempts:
Prompt Engineering

Skipped:
Deployment
```

AI decides:

```text
Q1 → Embeddings fundamentals
Q2 → Embeddings application
Q3 → RAG architecture
Q4 → Prompt Engineering fundamentals
```

Candidate gives a weak answer.

Then:

```text
Evaluator
    ↓
Weak understanding
    ↓
Follow-up
```

AI:

> "Let's approach that from another angle. Suppose you need an LLM to consistently return JSON. What techniques would you use?"

Candidate answers well.

AI:

```text
confidence ↑
difficulty ↑
```

Next:

> "How would you evaluate whether your structured-output prompting actually improves reliability?"

**That is an adaptive interview.**

Not:

```text
Question 1
Question 2
Question 3
...
```

---

# One important frontend change after backend starts

Your frontend currently has generic progress because we correctly removed fabricated topic/difficulty metadata. Cursor explicitly noted that those fields are no longer assumed from the API. 

That's good.

**Don't add topic/difficulty back just to make the sidebar prettier.**

If the backend later decides to return optional metadata such as:

```json
{
  "reply": "...",
  "done": false,
  "meta": {
    "topic": "Prompt Engineering",
    "isFollowUp": true
  }
}
```

then we can enhance the UI.

But first make the official contract work.

---

# Your next 6–8 hours

I'd divide it like this:

### Backend teammate

**Hour 1–2**

```text
FastAPI
Pydantic
/api/interview
CORS
```

**Hour 2–4**

```text
session store
candidate loading
curriculum loading
mock interview
```

**Hour 4–5**

```text
tests
frontend connection
```

---

### You + AI teammate

**Hour 1**

Study the exact candidate/curriculum structures.

**Hour 2**

Define:

```text
Candidate Analyzer
Interview Planner
Answer Evaluator
Feedback Generator
```

**Hour 3**

Write structured JSON schemas.

**Hour 4**

Create prompts.

**Hour 5**

Connect LLM to the backend's mock engine.

---

# Then the first integration test

You want to reach this as quickly as possible:

```text
Browser
   │
   │ Start
   ▼
POST /api/interview
   │
   ▼
FastAPI
   │
   ▼
Session created
   │
   ▼
"Welcome..."
```

Then:

```text
Browser
   │
   │ Candidate answer
   ▼
POST /api/interview
   │
   ▼
Same session
   │
   ▼
AI
   │
   ▼
Adaptive next question
```

Then finally:

```text
POST /api/interview
       ↓
done: true
       +
feedback
       ↓
React Feedback page
```

That's the **first real milestone**.

---

## So yes: **start the backend now.**

But don't stop your AI work waiting for it.

Your three tracks should now be:

```text
             ┌──────────────┐
             │  FRONTEND    │
             │   READY      │
             └──────┬───────┘
                    │
              API CONTRACT
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   BACKEND MEMBER           YOU + AI
   FastAPI                  Interview logic
   Session state            Candidate analysis
   Mock engine              Question planning
   API tests                Evaluation
        │                       │
        └───────────┬───────────┘
                    ▼
               INTEGRATION
                    ▼
              REAL AI DEMO
```

**The next thing I would personally do with you is design the AI engine before writing any LLM prompt.** We should take the actual `candidates.json` + `curriculum.json` structure and define exactly how the agent selects the 4+ curriculum days, identifies weak areas, decides when a follow-up is warranted, evaluates an answer, and produces the final `summary/strengths/gaps/next`. That is the part that can turn this from a polished chatbot into a genuinely strong hackathon solution.

## Prompt No.14

**AI Tool: Chatgpt**

**Author: Yash Palkar** 

### Prompt
so frontend has been done for now , and we are starting with backend now so give me a prompt for cursor based on this 

Build the backend for our hackathon AI Interview Agent.

IMPORTANT:
Do NOT implement the LLM/AI logic yet.
First build and test the API contract and interview session infrastructure.

## TECH STACK

Python
FastAPI
Pydantic
Uvicorn

Keep dependencies minimal.

## API CONTRACT

Expose exactly:

POST /api/interview

No authentication.

The endpoint must maintain interview state using sessionId.

INITIAL REQUEST:

{
"sessionId": "abc-123",
"candidate": { ...raw candidate.json object... }
}

Response:

{
"reply": "Welcome. Let's begin your interview.",
"done": false
}

SUBSEQUENT REQUEST:

{
"sessionId": "abc-123",
"message": "Candidate's latest answer"
}

Response:

{
"reply": "...",
"done": false
}

FINAL RESPONSE:

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

## SESSION MANAGEMENT

Create an in-memory session store initially.

Each session should contain at minimum:

sessionId
candidate
conversation history
question count
interview state

Use sessionId to retrieve the same session on every request.

Do NOT use a database yet.

We can add persistence later only if necessary.

## CANDIDATE

The candidate object received from the frontend must be the RAW candidate.json structure.

Do not require the frontend CandidateViewModel.

Load/validate the supplied candidate schema.

## CURRICULUM

Load the supplied curriculum.json.

Create a clean service for accessing curriculum information.

Do not implement sophisticated retrieval yet.

## MOCK INTERVIEW ENGINE

Before adding an LLM, implement a deterministic mock interview engine.

It should:

1. Start an interview.
2. Ask a question.
3. Accept an answer.
4. Store the answer in conversation history.
5. Return another question.
6. Continue for at least 8 questions.
7. Finish with done=true and feedback.

Make sure the question sequence spans at least 4 curriculum days.

Do NOT make the mock questions identical for every candidate if simple candidate-specific selection can be implemented from the supplied data.

## ARCHITECTURE

backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── interview\.py
│   ├── schemas/
│   │   └── interview\.py
│   ├── services/
│   │   ├── session.py
│   │   ├── candidate.py
│   │   └── curriculum.py
│   ├── interview/
│   │   └── engine.py
│   └── data/
│       ├── candidates.json
│       └── curriculum.json
│
├── requirements.txt
└── .env.example

Keep business logic out of the FastAPI route.

## CORS

Allow the Vite frontend during development.

For example localhost:5173.

## ERROR HANDLING

Return sensible HTTP errors for:

- missing sessionId
- unknown sessionId
- invalid candidate
- missing message
- malformed request

Do not expose internal stack traces.

## TESTING

Create basic tests for:

1. Start interview
2. Continue interview
3. Same sessionId maintains history
4. Unknown sessionId
5. Interview completion
6. Final feedback structure

Also verify:

POST /api/interview

works with curl/Postman.

IMPORTANT:
Do not implement OpenAI/Gemini/Claude calls yet.

The immediate goal is to prove:

React
↓
POST /api/interview
↓
FastAPI
↓
Session state
↓
Mock interviewer
↓
JSON response
↓
React

### Outcome
Yes. Your prompt is already good, but for Cursor I would make it **more explicit about implementation boundaries, validation, tests, and not touching the frontend**. That reduces the chance that the agent over-engineers the backend.

Also, because this is the first backend pass, I strongly recommend asking Cursor to **inspect the supplied `candidates.json`, `curriculum.json`, and technical specification before writing schemas**. That prevents it from inventing fields.

## Paste this into Cursor Agent

```text
You are the backend engineer for our 48-hour hackathon project.

We are building an AI-powered adaptive technical interviewer.

IMPORTANT:
The frontend is already implemented.

Your job is to build ONLY the backend.

DO NOT modify the frontend.
DO NOT implement any real LLM/AI calls yet.
DO NOT add authentication.
DO NOT add a database.
DO NOT add unnecessary dependencies.

The immediate goal is to prove this flow end-to-end:

React frontend
    ↓
POST /api/interview
    ↓
FastAPI
    ↓
Session state
    ↓
Deterministic mock interviewer
    ↓
JSON response
    ↓
React frontend


==================================================
PHASE 0 — INSPECT THE PROVIDED FILES
==================================================

Before writing code:

1. Inspect the supplied:
   - candidates.json
   - curriculum.json
   - technical specification / project requirements

2. Determine their ACTUAL schemas and field names.

3. Do NOT invent candidate fields.
4. Do NOT transform the candidate into the frontend CandidateViewModel.
5. The API must accept the RAW candidate.json object supplied by the frontend.

6. Determine the actual curriculum structure from curriculum.json.

If any required structure is ambiguous, document the assumption instead of silently inventing fields.

==================================================
TECH STACK
==================================================

Use:

- Python
- FastAPI
- Pydantic
- Uvicorn
- pytest
- httpx if required for FastAPI TestClient

Keep dependencies minimal.

Use Python type hints throughout.

Do not introduce:
- LangChain
- LangGraph
- OpenAI SDK
- Gemini SDK
- Anthropic SDK
- vector databases
- PostgreSQL
- Redis
- SQLAlchemy
- Docker unless absolutely necessary

We will add AI integration later.

==================================================
PROJECT STRUCTURE
==================================================

Create:

backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── interview.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── interview.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── session.py
│   │   ├── candidate.py
│   │   └── curriculum.py
│   │
│   ├── interview/
│   │   ├── __init__.py
│   │   └── engine.py
│   │
│   └── data/
│       ├── candidates.json
│       └── curriculum.json
│
├── tests/
│   ├── __init__.py
│   └── test_interview.py
│
├── requirements.txt
├── .env.example
└── README.md


==================================================
API CONTRACT
==================================================

Expose exactly:

POST /api/interview

No authentication.

The endpoint must maintain interview state using sessionId.

------------------------------------------
INITIAL REQUEST
------------------------------------------

Request:

{
  "sessionId": "abc-123",
  "candidate": {
    "...raw candidate.json object..."
  }
}

Response:

{
  "reply": "Welcome. Let's begin your interview.",
  "done": false
}


------------------------------------------
SUBSEQUENT REQUEST
------------------------------------------

Request:

{
  "sessionId": "abc-123",
  "message": "Candidate's latest answer"
}

Response:

{
  "reply": "...",
  "done": false
}


------------------------------------------
FINAL RESPONSE
------------------------------------------

Response:

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


IMPORTANT:

Keep the public API contract exactly as specified.

Do not add unnecessary response fields.

Do not change:
- sessionId
- candidate
- message
- reply
- done
- feedback
- summary
- strengths
- gaps
- next


==================================================
REQUEST VALIDATION
==================================================

The endpoint accepts two valid request shapes.

START:

{
  "sessionId": "...",
  "candidate": {...}
}

CONTINUE:

{
  "sessionId": "...",
  "message": "..."
}

A request should not need both candidate and message.

Validate the request using Pydantic.

Handle sensible errors for:

1. Missing sessionId
2. Empty sessionId
3. Invalid candidate
4. Missing message on continuation
5. Empty message
6. Unknown sessionId
7. Malformed JSON

Return appropriate HTTP status codes and clean JSON error responses.

Do not expose Python stack traces to the client.


==================================================
SESSION MANAGEMENT
==================================================

Implement an in-memory session store.

DO NOT use a database.

Each session must contain at minimum:

- sessionId
- candidate
- conversation history
- question count
- interview state

A reasonable internal representation is:

InterviewSession
    ├── session_id
    ├── candidate
    ├── conversation
    ├── question_count
    └── state

Possible states:

- active
- completed

Use sessionId to retrieve the same session for every request.

The session store should be isolated inside:

services/session.py

Do not put session logic directly inside the FastAPI route.


==================================================
CANDIDATE SERVICE
==================================================

Create:

services/candidate.py

Responsibilities:

- validate the raw candidate object
- expose useful candidate information to the interview engine
- keep the raw candidate available in session state

IMPORTANT:

The frontend sends the RAW candidate.json structure.

Do NOT require the frontend's CandidateViewModel.

Do NOT make the frontend transform the candidate.

If candidate.json contains nested structures, preserve them.

Use the actual candidate schema found in the supplied file.


==================================================
CURRICULUM SERVICE
==================================================

Create:

services/curriculum.py

Responsibilities:

- load curriculum.json
- validate/load it safely
- expose curriculum information to the interview engine
- provide access to curriculum days/topics/modules

Do not implement vector search, embeddings, RAG, or sophisticated retrieval.

For now, simple deterministic access is enough.


==================================================
MOCK INTERVIEW ENGINE
==================================================

Create:

interview/engine.py

This is a deterministic replacement for the future AI interviewer.

DO NOT call any LLM.

The engine must:

1. Start an interview.
2. Generate the first question.
3. Accept candidate answers.
4. Store every answer in conversation history.
5. Generate the next question.
6. Continue for AT LEAST 8 questions.
7. Cover AT LEAST 4 curriculum days.
8. Finish with done=true.
9. Return final feedback.

The interview must be deterministic so that tests are reliable.

Do not make every candidate receive exactly the same interview if
simple candidate-specific selection can be derived from the supplied
candidate data.

For example, if the supplied candidate structure provides useful
learning signals such as completed days, attempts, skipped areas,
or similar information, use those signals for simple deterministic
question selection.

Do NOT build sophisticated AI reasoning yet.

The goal is only to create a realistic mock engine whose interface
can later be replaced by an LLM-based implementation.


==================================================
CONVERSATION HISTORY
==================================================

Store conversation history inside the session.

Represent messages clearly, for example:

{
  "role": "interviewer",
  "content": "..."
}

{
  "role": "candidate",
  "content": "..."
}

The engine must receive the previous conversation when deciding
which mock question comes next.

The history must remain associated with the sessionId.


==================================================
INTERVIEW FLOW
==================================================

Implement this behavior:

START:

POST /api/interview

{
  "sessionId": "abc-123",
  "candidate": {...}
}

↓

Create session

↓

Generate question 1

↓

Return:

{
  "reply": "...",
  "done": false
}


CONTINUE:

POST /api/interview

{
  "sessionId": "abc-123",
  "message": "candidate answer"
}

↓

Retrieve session

↓

Store candidate answer

↓

Increment question count

↓

Generate next question

↓

Return:

{
  "reply": "...",
  "done": false
}


AFTER AT LEAST 8 QUESTIONS:

↓

Generate final feedback

↓

Mark session completed

↓

Return:

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


==================================================
FEEDBACK
==================================================

For now feedback is deterministic/mock.

It should be structurally valid and based at least loosely on the
candidate/interview data.

Required fields:

feedback.summary
feedback.strengths
feedback.gaps
feedback.next

Use arrays for strengths, gaps, and next.

Do not call an LLM.

Later we will replace this implementation with an AI evaluator.


==================================================
FASTAPI ROUTE
==================================================

Create:

api/interview.py

The route should be thin.

It should roughly perform:

request validation
    ↓
session lookup/create
    ↓
candidate/curriculum services
    ↓
interview engine
    ↓
response

DO NOT put business logic into the route.

The route should delegate to services/engine.


==================================================
MAIN APPLICATION
==================================================

Create:

app/main.py

Configure:

FastAPI application

POST /api/interview

CORS

Development frontend origin:

http://localhost:5173

Allow the Vite frontend to communicate with the API.

Do not use wildcard CORS unless necessary.


==================================================
ERROR HANDLING
==================================================

Return clean API errors.

Examples:

Unknown session:

HTTP 404

{
  "detail": "Unknown sessionId"
}

Invalid request:

HTTP 422

FastAPI/Pydantic validation is acceptable.

Completed session:

Return a sensible error if another answer is submitted after
the interview is already completed.


==================================================
TESTING
==================================================

Create tests using pytest and FastAPI's test client.

At minimum test:

1. Start interview

POST /api/interview

with:

sessionId + candidate

Expected:
- HTTP 200
- reply exists
- done == false


2. Continue interview

Send the same sessionId with message.

Expected:
- HTTP 200
- reply exists
- done == false


3. Session persistence

Send multiple requests using the same sessionId.

Verify:
- conversation history grows
- question count increases
- state remains active until completion


4. Unknown sessionId

Send:

{
  "sessionId": "does-not-exist",
  "message": "hello"
}

Expected:
- HTTP 404


5. Interview completion

Continue a session until the minimum question count is reached.

Verify:
- done == true
- feedback exists
- feedback.summary exists
- feedback.strengths is a list
- feedback.gaps is a list
- feedback.next is a list


6. Missing message

Send a continuation request without message.

Expected:
- validation error


7. Invalid candidate

Send malformed candidate data.

Expected:
- validation error


==================================================
MANUAL API VERIFICATION
==================================================

After implementation, verify the API manually.

Run:

uvicorn app.main:app --reload

Then test:

POST http://localhost:8000/api/interview

using curl or the FastAPI Swagger UI.

Also verify:

http://localhost:8000/docs

The endpoint must appear there.

Document the exact commands in README.md.


==================================================
ENVIRONMENT
==================================================

Create:

.env.example

For now there should be NO LLM API key.

If environment variables are needed, document them.

Do not hardcode secrets.


==================================================
CODE QUALITY
==================================================

Follow these rules:

- Python type hints
- small focused functions
- clear naming
- no unnecessary abstractions
- no duplicated business logic
- no global mutable state except the intentional in-memory session store
- keep route handlers thin
- separate schemas, services, session management and interview engine
- clear comments only where useful

Do not over-engineer.

This is a 48-hour hackathon MVP.


==================================================
IMPORTANT DEVELOPMENT RULE
==================================================

Implement this in stages.

STAGE 1:
Inspect files and report the discovered candidate/curriculum schemas.

STAGE 2:
Create project structure and dependencies.

STAGE 3:
Implement Pydantic schemas.

STAGE 4:
Implement curriculum and candidate services.

STAGE 5:
Implement in-memory session manager.

STAGE 6:
Implement deterministic mock interview engine.

STAGE 7:
Implement POST /api/interview.

STAGE 8:
Implement tests.

STAGE 9:
Run tests and fix failures.

STAGE 10:
Run the API and manually verify the endpoint.

Do NOT jump directly to writing the entire application.

After each stage, briefly report:
- files changed
- what was implemented
- tests/status
- anything that remains

MOST IMPORTANT:
DO NOT IMPLEMENT OPENAI, GEMINI, CLAUDE, LANGCHAIN, OR ANY OTHER LLM INTEGRATION.

We will add the real AI interviewer only after the API contract,
session management, mock engine, and tests are working correctly.
```

## Why I changed your original prompt

There are three important improvements.

### 1. Tell Cursor to inspect the JSON first

This is critical because you explicitly said:

> raw candidate.json object

So don't let Cursor invent:

```python
class Candidate(BaseModel):
    name: str
    role: str
    experience: int
```

unless those fields actually exist.

You want:

```text
actual candidates.json
       ↓
Pydantic validation
       ↓
session
```

---

### 2. Make the route thin

You don't want:

```text
interview.py
 ├── session logic
 ├── candidate logic
 ├── curriculum logic
 ├── question generation
 ├── feedback
 └── validation
```

You want:

```text
POST /api/interview
       │
       ▼
SessionService
       │
       ▼
CandidateService
       │
       ▼
CurriculumService
       │
       ▼
InterviewEngine
```

That will make replacing the mock engine with the real AI engine much easier.

---

### 3. Build the mock engine as if it were the real AI engine

This is the most important architectural decision.

Today:

```text
InterviewEngine
      ↓
Mock questions
```

Later:

```text
InterviewEngine
      ↓
AI Interview Agent
      ↓
LLM
```

Your API shouldn't need to change.

Your frontend shouldn't need to change.

Only the implementation behind the engine changes.

---

# What you should expect Cursor to produce

At the end of this phase, you should have:

```text
React
   │
   │ POST /api/interview
   ▼
FastAPI
   │
   ▼
Session Store
   │
   ▼
Mock Interview Engine
   │
   ├── Q1
   ├── Q2
   ├── Q3
   ├── Q4
   ├── Q5
   ├── Q6
   ├── Q7
   └── Q8
   │
   ▼
Feedback
   │
   ▼
JSON
   │
   ▼
React
```

**Do not start the LLM work until this entire flow passes the tests.**

Then the next phase can be:

```text
MockInterviewEngine
        ↓
AIInterviewEngine
        ↓
Candidate context
        +
Curriculum context
        +
Conversation history
        ↓
LLM
        ↓
Structured question/evaluation
```

That separation will make the second phase considerably easier.

## Prompt No.15

**AI Tool: Cursor**

**Author: Yash Palkar** 

### Prompt
You are the backend engineer for our 48-hour hackathon project.

We are building an AI-powered adaptive technical interviewer.

IMPORTANT:
The frontend is already implemented.

Your job is to build ONLY the backend.

DO NOT modify the frontend.
DO NOT implement any real LLM/AI calls yet.
DO NOT add authentication.
DO NOT add a database.
DO NOT add unnecessary dependencies.

The immediate goal is to prove this flow end-to-end:

React frontend
    ↓
POST /api/interview
    ↓
FastAPI
    ↓
Session state
    ↓
Deterministic mock interviewer
    ↓
JSON response
    ↓
React frontend


==================================================
PHASE 0 — INSPECT THE PROVIDED FILES
==================================================

Before writing code:

1. Inspect the supplied:
   - candidates.json
   - curriculum.json
   - technical specification / project requirements

2. Determine their ACTUAL schemas and field names.

3. Do NOT invent candidate fields.
4. Do NOT transform the candidate into the frontend CandidateViewModel.
5. The API must accept the RAW candidate.json object supplied by the frontend.

6. Determine the actual curriculum structure from curriculum.json.

If any required structure is ambiguous, document the assumption instead of silently inventing fields.

==================================================
TECH STACK
==================================================

Use:

- Python
- FastAPI
- Pydantic
- Uvicorn
- pytest
- httpx if required for FastAPI TestClient

Keep dependencies minimal.

Use Python type hints throughout.

Do not introduce:
- LangChain
- LangGraph
- OpenAI SDK
- Gemini SDK
- Anthropic SDK
- vector databases
- PostgreSQL
- Redis
- SQLAlchemy
- Docker unless absolutely necessary

We will add AI integration later.

==================================================
PROJECT STRUCTURE
==================================================

Create:

backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── interview.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── interview.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── session.py
│   │   ├── candidate.py
│   │   └── curriculum.py
│   │
│   ├── interview/
│   │   ├── __init__.py
│   │   └── engine.py
│   │
│   └── data/
│       ├── candidates.json
│       └── curriculum.json
│
├── tests/
│   ├── __init__.py
│   └── test_interview.py
│
├── requirements.txt
├── .env.example
└── README.md


==================================================
API CONTRACT
==================================================

Expose exactly:

POST /api/interview

No authentication.

The endpoint must maintain interview state using sessionId.

------------------------------------------
INITIAL REQUEST
------------------------------------------

Request:

{
  "sessionId": "abc-123",
  "candidate": {
    "...raw candidate.json object..."
  }
}

Response:

{
  "reply": "Welcome. Let's begin your interview.",
  "done": false
}


------------------------------------------
SUBSEQUENT REQUEST
------------------------------------------

Request:

{
  "sessionId": "abc-123",
  "message": "Candidate's latest answer"
}

Response:

{
  "reply": "...",
  "done": false
}


------------------------------------------
FINAL RESPONSE
------------------------------------------

Response:

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


IMPORTANT:

Keep the public API contract exactly as specified.

Do not add unnecessary response fields.

Do not change:
- sessionId
- candidate
- message
- reply
- done
- feedback
- summary
- strengths
- gaps
- next


==================================================
REQUEST VALIDATION
==================================================

The endpoint accepts two valid request shapes.

START:

{
  "sessionId": "...",
  "candidate": {...}
}

CONTINUE:

{
  "sessionId": "...",
  "message": "..."
}

A request should not need both candidate and message.

Validate the request using Pydantic.

Handle sensible errors for:

1. Missing sessionId
2. Empty sessionId
3. Invalid candidate
4. Missing message on continuation
5. Empty message
6. Unknown sessionId
7. Malformed JSON

Return appropriate HTTP status codes and clean JSON error responses.

Do not expose Python stack traces to the client.


==================================================
SESSION MANAGEMENT
==================================================

Implement an in-memory session store.

DO NOT use a database.

Each session must contain at minimum:

- sessionId
- candidate
- conversation history
- question count
- interview state

A reasonable internal representation is:

InterviewSession
    ├── session_id
    ├── candidate
    ├── conversation
    ├── question_count
    └── state

Possible states:

- active
- completed

Use sessionId to retrieve the same session for every request.

The session store should be isolated inside:

services/session.py

Do not put session logic directly inside the FastAPI route.


==================================================
CANDIDATE SERVICE
==================================================

Create:

services/candidate.py

Responsibilities:

- validate the raw candidate object
- expose useful candidate information to the interview engine
- keep the raw candidate available in session state

IMPORTANT:

The frontend sends the RAW candidate.json structure.

Do NOT require the frontend's CandidateViewModel.

Do NOT make the frontend transform the candidate.

If candidate.json contains nested structures, preserve them.

Use the actual candidate schema found in the supplied file.


==================================================
CURRICULUM SERVICE
==================================================

Create:

services/curriculum.py

Responsibilities:

- load curriculum.json
- validate/load it safely
- expose curriculum information to the interview engine
- provide access to curriculum days/topics/modules

Do not implement vector search, embeddings, RAG, or sophisticated retrieval.

For now, simple deterministic access is enough.


==================================================
MOCK INTERVIEW ENGINE
==================================================

Create:

interview/engine.py

This is a deterministic replacement for the future AI interviewer.

DO NOT call any LLM.

The engine must:

1. Start an interview.
2. Generate the first question.
3. Accept candidate answers.
4. Store every answer in conversation history.
5. Generate the next question.
6. Continue for AT LEAST 8 questions.
7. Cover AT LEAST 4 curriculum days.
8. Finish with done=true.
9. Return final feedback.

The interview must be deterministic so that tests are reliable.

Do not make every candidate receive exactly the same interview if
simple candidate-specific selection can be derived from the supplied
candidate data.

For example, if the supplied candidate structure provides useful
learning signals such as completed days, attempts, skipped areas,
or similar information, use those signals for simple deterministic
question selection.

Do NOT build sophisticated AI reasoning yet.

The goal is only to create a realistic mock engine whose interface
can later be replaced by an LLM-based implementation.


==================================================
CONVERSATION HISTORY
==================================================

Store conversation history inside the session.

Represent messages clearly, for example:

{
  "role": "interviewer",
  "content": "..."
}

{
  "role": "candidate",
  "content": "..."
}

The engine must receive the previous conversation when deciding
which mock question comes next.

The history must remain associated with the sessionId.


==================================================
INTERVIEW FLOW
==================================================

Implement this behavior:

START:

POST /api/interview

{
  "sessionId": "abc-123",
  "candidate": {...}
}

↓

Create session

↓

Generate question 1

↓

Return:

{
  "reply": "...",
  "done": false
}


CONTINUE:

POST /api/interview

{
  "sessionId": "abc-123",
  "message": "candidate answer"
}

↓

Retrieve session

↓

Store candidate answer

↓

Increment question count

↓

Generate next question

↓

Return:

{
  "reply": "...",
  "done": false
}


AFTER AT LEAST 8 QUESTIONS:

↓

Generate final feedback

↓

Mark session completed

↓

Return:

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


==================================================
FEEDBACK
==================================================

For now feedback is deterministic/mock.

It should be structurally valid and based at least loosely on the
candidate/interview data.

Required fields:

feedback.summary
feedback.strengths
feedback.gaps
feedback.next

Use arrays for strengths, gaps, and next.

Do not call an LLM.

Later we will replace this implementation with an AI evaluator.


==================================================
FASTAPI ROUTE
==================================================

Create:

api/interview.py

The route should be thin.

It should roughly perform:

request validation
    ↓
session lookup/create
    ↓
candidate/curriculum services
    ↓
interview engine
    ↓
response

DO NOT put business logic into the route.

The route should delegate to services/engine.


==================================================
MAIN APPLICATION
==================================================

Create:

app/main.py

Configure:

FastAPI application

POST /api/interview

CORS

Development frontend origin:

http://localhost:5173

Allow the Vite frontend to communicate with the API.

Do not use wildcard CORS unless necessary.


==================================================
ERROR HANDLING
==================================================

Return clean API errors.

Examples:

Unknown session:

HTTP 404

{
  "detail": "Unknown sessionId"
}

Invalid request:

HTTP 422

FastAPI/Pydantic validation is acceptable.

Completed session:

Return a sensible error if another answer is submitted after
the interview is already completed.


==================================================
TESTING
==================================================

Create tests using pytest and FastAPI's test client.

At minimum test:

1. Start interview

POST /api/interview

with:

sessionId + candidate

Expected:
- HTTP 200
- reply exists
- done == false


2. Continue interview

Send the same sessionId with message.

Expected:
- HTTP 200
- reply exists
- done == false


3. Session persistence

Send multiple requests using the same sessionId.

Verify:
- conversation history grows
- question count increases
- state remains active until completion


4. Unknown sessionId

Send:

{
  "sessionId": "does-not-exist",
  "message": "hello"
}

Expected:
- HTTP 404


5. Interview completion

Continue a session until the minimum question count is reached.

Verify:
- done == true
- feedback exists
- feedback.summary exists
- feedback.strengths is a list
- feedback.gaps is a list
- feedback.next is a list


6. Missing message

Send a continuation request without message.

Expected:
- validation error


7. Invalid candidate

Send malformed candidate data.

Expected:
- validation error


==================================================
MANUAL API VERIFICATION
==================================================

After implementation, verify the API manually.

Run:

uvicorn app.main:app --reload

Then test:

POST http://localhost:8000/api/interview

using curl or the FastAPI Swagger UI.

Also verify:

http://localhost:8000/docs

The endpoint must appear there.

Document the exact commands in README.md.


==================================================
ENVIRONMENT
==================================================

Create:

.env.example

For now there should be NO LLM API key.

If environment variables are needed, document them.

Do not hardcode secrets.


==================================================
CODE QUALITY
==================================================

Follow these rules:

- Python type hints
- small focused functions
- clear naming
- no unnecessary abstractions
- no duplicated business logic
- no global mutable state except the intentional in-memory session store
- keep route handlers thin
- separate schemas, services, session management and interview engine
- clear comments only where useful

Do not over-engineer.

This is a 48-hour hackathon MVP.


==================================================
IMPORTANT DEVELOPMENT RULE
==================================================

Implement this in stages.

STAGE 1:
Inspect files and report the discovered candidate/curriculum schemas.

STAGE 2:
Create project structure and dependencies.

STAGE 3:
Implement Pydantic schemas.

STAGE 4:
Implement curriculum and candidate services.

STAGE 5:
Implement in-memory session manager.

STAGE 6:
Implement deterministic mock interview engine.

STAGE 7:
Implement POST /api/interview.

STAGE 8:
Implement tests.

STAGE 9:
Run tests and fix failures.

STAGE 10:
Run the API and manually verify the endpoint.

Do NOT jump directly to writing the entire application.

After each stage, briefly report:
- files changed
- what was implemented
- tests/status
- anything that remains

MOST IMPORTANT:
DO NOT IMPLEMENT OPENAI, GEMINI, CLAUDE, LANGCHAIN, OR ANY OTHER LLM INTEGRATION.

We will add the real AI interviewer only after the API contract,
session management, mock engine, and tests are working correctly.

### Outcome
## Stage 1 — Discovered Schemas

### Candidate (single object sent to API — **not** the `candidates.json` wrapper)

The file `candidates.json` wraps entries in `{ "candidates": [...] }`, but the frontend sends **one raw entry** via `postInterview({ sessionId, candidate: rawCandidate })`.

| Field | Type | Notes |
|-------|------|-------|
| `member.id` | string | e.g. `"CAND-001"` |
| `member.name` | string | |
| `member.jobRole` | string | |
| `member.yearsExperience` | number | |
| `member.education` | string | |
| `member.status` | string? | e.g. `"COMPLETED"` |
| `missions[]` | array | `{ day, title?, passed?, skipped?, attempts? }` |
| `signals.commitDays` | number | |
| `signals.missionsCompleted` | number | |
| `signals.missionsFirstTry` | number | |

**Assumption:** A mission may be `passed`, `skipped`, or neither; `skipped` and `passed` are mutually exclusive.

### Curriculum (`curriculum.json`)

| Field | Type |
|-------|------|
| `cohort` | string |
| `modules[]` | `{ n, title, days: [start, end] }` |
| `days[]` | `{ day, title, type, tools[], objectives[] }` |

---

## Stages 2–10 — Implementation Complete

### Files created

```
backend/
├── app/
│   ├── main.py
│   ├── api/interview.py
│   ├── schemas/interview.py
│   ├── services/{session,candidate,curriculum}.py
│   ├── interview/engine.py
│   └── data/{candidates,curriculum}.json
├── tests/test_interview.py
├── requirements.txt
├── .env.example
└── README.md
```

### What was implemented

| Component | Behavior |
|-----------|----------|
| **Pydantic schemas** | Validates START (`sessionId` + `candidate`) vs CONTINUE (`sessionId` + `message`); rejects both/neither |
| **Candidate service** | Validates raw candidate; exposes skipped/difficult/first-try missions |
| **Curriculum service** | Loads and validates `curriculum.json`; day/module lookup |
| **Session store** | In-memory `InterviewSession` with conversation, question count, planned days, state |
| **Mock engine** | 8 deterministic questions, ≥4 curriculum days, candidate-tailored day selection (skipped → retries → strengths) |
| **API route** | Thin `POST /api/interview` delegating to services/engine |
| **CORS** | Allows `http://localhost:5173` |
| **Errors** | 404 unknown session, 409 duplicate start, 400 completed session, 422 validation |

### Tests & manual verification

- **8/8 pytest tests passing**
- **Manual API verified** — start + continue work on `http://127.0.0.1:8000`
- **Swagger UI** — `http://localhost:8000/docs`

### Run it

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest -v
```

### Connect frontend (no frontend changes made)

The Vite proxy still targets port 3000, so use:

```bash
VITE_USE_MOCK=false VITE_API_BASE_URL=http://localhost:8000 npm run dev
```

---

## Interview flow

1. **START** → welcome + question 1 (`done: false`)
2. **CONTINUE** × 7 → next questions (`done: false`)
3. **CONTINUE** (8th answer) → `"Interview completed."` + `feedback` (`done: true`)

Question selection prioritizes skipped missions, high-attempt areas, and first-try strengths — rotated deterministically by `member.id`.

No LLM, auth, or database was added. The mock engine interface in `interview/engine.py` is ready to swap for a real AI interviewer later.

## Prompt No.16

**AI Tool: Chatgpt**

**Author: Yash Palkar** 

### Prompt
## Stage 1 — Discovered Schemas

### Candidate (single object sent to API — **not** the `candidates.json` wrapper)

The file `candidates.json` wraps entries in `{ "candidates": [...] }`, but the frontend sends **one raw entry** via `postInterview({ sessionId, candidate: rawCandidate })`.

| Field                       | Type    | Notes                                           |
| --------------------------- | ------- | ----------------------------------------------- |
| `member.id`                 | string  | e.g. `"CAND-001"`                               |
| `member.name`               | string  |                                                 |
| `member.jobRole`            | string  |                                                 |
| `member.yearsExperience`    | number  |                                                 |
| `member.education`          | string  |                                                 |
| `member.status`             | string? | e.g. `"COMPLETED"`                              |
| `missions[]`                | array   | `{ day, title?, passed?, skipped?, attempts? }` |
| `signals.commitDays`        | number  |                                                 |
| `signals.missionsCompleted` | number  |                                                 |
| `signals.missionsFirstTry`  | number  |                                                 |

**Assumption:** A mission may be `passed`, `skipped`, or neither; `skipped` and `passed` are mutually exclusive.

### Curriculum (`curriculum.json`)

| Field       | Type                                          |
| ----------- | --------------------------------------------- |
| `cohort`    | string                                        |
| `modules[]` | `{ n, title, days: [start, end] }`            |
| `days[]`    | `{ day, title, type, tools[], objectives[] }` |

---

## Stages 2–10 — Implementation Complete

### Files created

```
backend/
├── app/
│   ├── main.py
│   ├── api/interview.py
│   ├── schemas/interview.py
│   ├── services/{session,candidate,curriculum}.py
│   ├── interview/engine.py
│   └── data/{candidates,curriculum}.json
├── tests/test_interview.py
├── requirements.txt
├── .env.example
└── README.md
```

### What was implemented

| Component              | Behavior                                                                                                        |
| ---------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Pydantic schemas**   | Validates START (`sessionId` + `candidate`) vs CONTINUE (`sessionId` + `message`); rejects both/neither         |
| **Candidate service**  | Validates raw candidate; exposes skipped/difficult/first-try missions                                           |
| **Curriculum service** | Loads and validates `curriculum.json`; day/module lookup                                                        |
| **Session store**      | In-memory `InterviewSession` with conversation, question count, planned days, state                             |
| **Mock engine**        | 8 deterministic questions, ≥4 curriculum days, candidate-tailored day selection (skipped → retries → strengths) |
| **API route**          | Thin `POST /api/interview` delegating to services/engine                                                        |
| **CORS**               | Allows `http://localhost:5173`                                                                                  |
| **Errors**             | 404 unknown session, 409 duplicate start, 400 completed session, 422 validation                                 |

### Tests & manual verification

- **8/8 pytest tests passing**
- **Manual API verified** — start + continue work on `http://127.0.0.1:8000`
- **Swagger UI** — `http://localhost:8000/docs`

### Run it

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest -v
```

### Connect frontend (no frontend changes made)

The Vite proxy still targets port 3000, so use:

```bash
VITE_USE_MOCK=false VITE_API_BASE_URL=http://localhost:8000 npm run dev
```

---

## Interview flow

1. **START** → welcome + question 1 (`done: false`)
2. **CONTINUE** × 7 → next questions (`done: false`)
3. **CONTINUE** (8th answer) → `"Interview completed."` + `feedback` (`done: true`)

Question selection prioritizes skipped missions, high-attempt areas, and first-try strengths — rotated deterministically by `member.id`.

No LLM, auth, or database was added. The mock engine interface in `interview/engine.py` is ready to swap for a real AI interviewer later.



cursor created this , so what to do next

### Outcome
This is actually a **very good checkpoint**. Don't ask Cursor to add the LLM yet.

You now have a working backend skeleton whose job is:

```text
Frontend
   ↓
POST /api/interview
   ↓
FastAPI
   ↓
Session Store
   ↓
Mock Interview Engine
   ↓
JSON
   ↓
Frontend
```

## What you should do next

### Step 1 — Don't change code yet. Run the backend yourself

From the backend folder:

```bash
cd backend

python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Then:

```bash
pip install -r requirements.txt
```

Run:

```bash
uvicorn app.main:app --reload
```

You should see something like:

```text
Uvicorn running on http://127.0.0.1:8000
```

Then open:

```text
http://localhost:8000/docs
```

You should see:

```text
POST /api/interview
```

---

# Step 2 — Test the API through Swagger

Don't connect the frontend yet.

First prove the backend works independently.

Click:

```text
POST /api/interview
→ Try it out
```

For the first request, use an **actual raw candidate object from your `candidates.json`**, because Cursor discovered that the frontend sends one candidate entry rather than the entire `{ "candidates": [...] }` wrapper.

Your request should conceptually be:

```json
{
  "sessionId": "test-001",
  "candidate": {
    "...actual candidate object..."
  }
}
```

You should get:

```json
{
  "reply": "...",
  "done": false
}
```

Save the `sessionId`.

---

# Step 3 — Test the session

Now send:

```json
{
  "sessionId": "test-001",
  "message": "This is my answer to the question."
}
```

You should get another question:

```json
{
  "reply": "...",
  "done": false
}
```

Do this repeatedly.

Your target is:

```text
START
  ↓
Q1
  ↓
Answer
  ↓
Q2
  ↓
Answer
  ↓
Q3
  ↓
...
  ↓
Q8
  ↓
Final feedback
```

Eventually:

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

---

# Step 4 — Run the automated tests

In another terminal:

```bash
cd backend
.venv\Scripts\activate
pytest -v
```

You already have **8/8 passing**, so this is mainly making sure the environment on your machine reproduces Cursor's result.

Don't move forward if tests fail.

---

# Step 5 — Now connect your existing frontend

This is the exciting part.

Your existing frontend already has the abstraction:

```text
InterviewGateway
```

and apparently already has the ability to switch between mock and API mode.

Cursor reported:

```bash
VITE_USE_MOCK=false
VITE_API_BASE_URL=http://localhost:8000
```

So run the frontend with:

```bash
VITE_USE_MOCK=false VITE_API_BASE_URL=http://localhost:8000 npm run dev
```

On Windows PowerShell, use:

```powershell
$env:VITE_USE_MOCK="false"
$env:VITE_API_BASE_URL="http://localhost:8000"
npm run dev
```

Then:

```text
Browser
   ↓
Frontend
   ↓
POST localhost:8000/api/interview
   ↓
FastAPI
```

---

# Step 6 — Test the complete flow

Now go through your actual UI.

You want to verify:

### Candidate selection

```text
Candidates page
      ↓
Select candidate
```

### Start

```text
Start interview
      ↓
POST /api/interview
      ↓
Backend creates session
      ↓
Question appears
```

### Answer

```text
Type answer
      ↓
Submit
      ↓
POST /api/interview
      ↓
Backend finds session
      ↓
Stores answer
      ↓
Generates next question
      ↓
Frontend displays it
```

### Completion

```text
8 questions
      ↓
Backend returns done=true
      ↓
Frontend navigates/displays Results
      ↓
Feedback displayed
```

---

# ⚠️ There is one thing I want you to check carefully

Your backend report says:

> `candidate service validates raw candidate`

and:

> `Pydantic schemas validate START`

That's good, **but don't assume the schema is correct just because the tests pass**.

The tests may only prove that the implementation is internally consistent.

You should verify that the actual candidate JSON being sent by your frontend is accepted.

Specifically test an actual object containing:

```text
member
  ├── id
  ├── name
  ├── jobRole
  ├── yearsExperience
  ├── education
  └── status

missions[]

signals
  ├── commitDays
  ├── missionsCompleted
  └── missionsFirstTry
```

because this is the actual structure Cursor discovered.

---

# Step 7 — Check the browser Network tab

This is one of the most useful things you can do.

Open Chrome/Edge DevTools:

```text
F12
→ Network
→ Fetch/XHR
```

Start the interview.

You should see:

```text
POST
/api/interview
```

Click it and inspect:

### Request

```json
{
  "sessionId": "...",
  "candidate": {...}
}
```

Then inspect the response:

```json
{
  "reply": "...",
  "done": false
}
```

Then submit an answer.

You should see another:

```text
POST /api/interview
```

with:

```json
{
  "sessionId": "...",
  "message": "..."
}
```

This proves your frontend and backend are genuinely communicating.

---

# Step 8 — Fix integration issues, not architecture

If the frontend breaks, **don't immediately ask Cursor to rewrite everything**.

Give Cursor the actual error.

For example:

```text
The backend is running on localhost:8000 and the frontend is
running on localhost:5173.

The frontend is making:

POST /api/interview

The backend returns HTTP 422.

Here is the actual request payload:

[PASTE NETWORK REQUEST]

Here is the response:

[PASTE RESPONSE]

Inspect the existing frontend InterviewGateway and backend
Pydantic schema.

Find the contract mismatch.

Do NOT rewrite the architecture.
Make the smallest change necessary while preserving the
specified API contract.
```

That's the kind of AI-assisted development you want.

---

# Step 9 — Commit this checkpoint

Once this works:

```bash
git add backend
git commit -m "feat: add interview backend session infrastructure"
```

Then you have a stable checkpoint.

Your Git history becomes something like:

```text
frontend complete
       ↓
backend API contract
       ↓
mock interview engine
       ↓
frontend-backend integration
       ↓
AI interviewer       ← NEXT MAJOR PHASE
       ↓
final polish
```

---

# And THEN we build the actual AI

This is where I would **not** let Cursor randomly "add AI".

Your current architecture gives us a very nice seam:

```text
                    CURRENT
                       │
                       ▼
              Mock Interview Engine
                       │
                       │
                    replace
                       │
                       ▼
                    FUTURE
                       │
                       ▼
              AI Interview Engine
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     Candidate     Curriculum    Conversation
      Context        Context       History
          │            │            │
          └────────────┼────────────┘
                       ▼
                  AI Interviewer
                       │
              ┌────────┴────────┐
              ▼                 ▼
          Question          Evaluation
              │                 │
              └────────┬────────┘
                       ▼
                  Next Question
```

The AI should eventually be responsible for the **adaptive reasoning**, while FastAPI remains responsible for the **API, session, validation, and orchestration**.

---

# Your next 3 tasks, in exact order

Don't get distracted by anything else right now.

### 🔴 Task 1 — Backend standalone

```text
pytest -v
        ↓
8/8 pass
        ↓
Swagger
        ↓
START → CONTINUE → ... → DONE
```

### 🟠 Task 2 — Frontend ↔ Backend

```text
Vite :5173
     ↓
FastAPI :8000
     ↓
POST /api/interview
     ↓
Mock engine
```

Verify the complete interview through the actual UI.

### 🟢 Task 3 — Only after that

We replace:

```text
MockInterviewEngine
```

with:

```text
AIInterviewEngine
```

**Don't start Task 3 until Task 1 + Task 2 are working.**

That's the safest way to spend your hackathon time because if the AI integration gets messy, you'll still have a completely functional end-to-end product to demo.

## Prompt No.17

**AI Tool: Chatgpt**

**Author: Yash Palkar** 

### Prompt
the automated tests show this result : 

\======================================================= test session starts =======================================================
platform win32 -- Python 3.14.2, pytest-8.4.2, pluggy-1.6.0 -- D:\Hackathon\AB talks\The-Interview-Agent\backend.venv\Scripts\python.exe
cachedir: .pytest\_cache
rootdir: D:\Hackathon\AB talks\The-Interview-Agent\backend
plugins: anyio-4.14.2
collected 8 items

tests/test\_interview\.py::test\_start\_interview PASSED                                                                         [ 12%]
tests/test\_interview\.py::test\_continue\_interview PASSED                                                                      [ 25%]
tests/test\_interview\.py::test\_session\_persistence PASSED                                                                     [ 37%]
tests/test\_interview\.py::test\_unknown\_session PASSED                                                                         [ 50%]
tests/test\_interview\.py::test\_interview\_completion PASSED                                                                    [ 62%]
tests/test\_interview\.py::test\_missing\_message\_on\_continuation PASSED                                                         [ 75%]
tests/test\_interview\.py::test\_invalid\_candidate PASSED                                                                       [ 87%]
tests/test\_interview\.py::test\_completed\_session\_rejects\_continuation PASSED                                                  [100%]

\======================================================== warnings summary =========================================================
.venv\Lib\site-packages\fastapi\testclient.py:1
D:\Hackathon\AB talks\The-Interview-Agent\backend.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
from starlette.testclient import TestClient as TestClient  # noqa

\-- Docs: [https://docs.pytest.org/en/stable/how-to/capture-warnings.html](https://docs.pytest.org/en/stable/how-to/capture-warnings.html)
\================================================== 8 passed, 1 warning in 0.63s ===================================================




as for the testing on swagger, i think im supposed to enter the member field of the json under the candidate after the session id but it shows 

| 422 |   |
| --- | - |

Error: Unprocessable Content

what am i doing wrong? 

### Outcome
You're actually in a **good state**: `8 passed` means the backend's automated tests are working. The `httpx` message is only a warning, not a test failure.

The Swagger `422` is a separate issue. Most likely, the JSON you're entering doesn't match the **Pydantic request schema that Cursor generated**.

### First: understand what `422` means

FastAPI returns:

```text
422 Unprocessable Content
```

when the JSON is valid JSON, but it **doesn't match the API's expected structure/types**.

Your endpoint has two possible request shapes:

**Start:**

```json
{
  "sessionId": "test-001",
  "candidate": {
    "...raw candidate object..."
  }
}
```

**Continue:**

```json
{
  "sessionId": "test-001",
  "message": "My answer..."
}
```

For the first request, yes, you put the **whole raw candidate object** under `candidate`.

But here's the important part:

> Don't put just the `"member"` object under `"candidate"`.

The candidate appears to have this structure:

```json
{
  "member": {
    "id": "CAND-001",
    "name": "...",
    "jobRole": "...",
    "yearsExperience": 2,
    "education": "...",
    "status": "COMPLETED"
  },
  "missions": [
    ...
  ],
  "signals": {
    "commitDays": 10,
    "missionsCompleted": 8,
    "missionsFirstTry": 6
  }
}
```

So your request should look like:

```json
{
  "sessionId": "test-001",
  "candidate": {
    "member": {
      "id": "CAND-001",
      "name": "Actual Candidate Name",
      "jobRole": "Software Engineer",
      "yearsExperience": 2,
      "education": "Computer Science",
      "status": "COMPLETED"
    },
    "missions": [
      {
        "day": 1,
        "title": "Some mission",
        "passed": true,
        "skipped": false,
        "attempts": 1
      }
    ],
    "signals": {
      "commitDays": 5,
      "missionsCompleted": 3,
      "missionsFirstTry": 2
    }
  }
}
```

**But don't use my example values if your actual `candidates.json` has different values/structure.** Use one complete candidate entry from your actual JSON.

---

## The easiest way to diagnose your exact 422

In Swagger, after the `422`, look at the response body.

It should give something like:

```json
{
  "detail": [
    {
      "loc": ["body", "candidate", "member"],
      "msg": "Field required"
    }
  ]
}
```

That `loc` tells us exactly what is wrong.

### Do this:

1. Go to:

```text
http://localhost:8000/docs
```

2. Open:

```text
POST /api/interview
```

3. Click **Try it out**.

4. Enter your request.

5. Click **Execute**.

6. Copy the **Response body under the 422**.

Send me that response body.

---

## Even better: use an actual candidate from your JSON

Since your backend has:

```text
backend/app/data/candidates.json
```

open that file.

You'll probably see something like:

```json
{
  "candidates": [
    {
      "member": {...},
      "missions": [...],
      "signals": {...}
    }
  ]
}
```

Take the **entire first object inside `candidates`**, not the wrapper:

```text
❌ Don't send:

{
  "candidates": [...]
}

❌ Don't send:

{
  "member": {...}
}

✅ Send:

{
  "member": {...},
  "missions": [...],
  "signals": {...}
}
```

Then wrap that under `"candidate"`:

```json
{
  "sessionId": "swagger-test-001",
  "candidate": {
    "member": {
      "...": "..."
    },
    "missions": [],
    "signals": {
      "...": "..."
    }
  }
}
```

---

## Your test result itself is excellent

This:

```text
8 passed, 1 warning
```

means:

```text
START                    ✅
CONTINUE                 ✅
SESSION PERSISTENCE      ✅
UNKNOWN SESSION          ✅
COMPLETION               ✅
MISSING MESSAGE          ✅
INVALID CANDIDATE        ✅
COMPLETED SESSION        ✅
```

The warning:

```text
StarletteDeprecationWarning:
Using `httpx` with `starlette.testclient` is deprecated
```

is **not causing your 422**.

Don't start changing dependencies just because of that warning. Your tests are passing.

---

### One thing I want from you

Send me **the exact 422 Response body from Swagger** (the JSON under the response), and if possible the JSON you're currently entering.

I'll tell you exactly which field is causing it and what to paste into Swagger.


## Prompt No.18

**AI Tool: Chatgpt**

**Author: Yash Palkar** 

### Prompt
got the interview completed as well, now tell me how to connect the frontend and backend together

### Outcome
Absolutely. Since **both sides are independently working now**, you're at the best point to integrate them. Don't rewrite either side. We just need to connect the existing `InterviewGateway` in your frontend to `POST /api/interview`.

Your target is:

```text
┌──────────────────┐
│   React + Vite   │
│   localhost:5173 │
└────────┬─────────┘
         │
         │ POST /api/interview
         ▼
┌──────────────────┐
│     FastAPI      │
│   localhost:8000 │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Mock Interview   │
│     Engine       │
└──────────────────┘
```

## 1. Keep both servers running

### Terminal 1 — Backend

From `backend/`:

```bash
.venv\Scripts\activate
uvicorn app.main:app --reload
```

You should have:

```text
http://localhost:8000
```

Verify:

```text
http://localhost:8000/docs
```

works.

---

### Terminal 2 — Frontend

From your frontend root:

```bash
npm install
npm run dev
```

You should have something like:

```text
http://localhost:5173
```

---

# 2. Check your frontend's `interviewGateway.ts`

This is the key file.

Your frontend already has the abstraction:

```text
src/
└── interviewGateway.ts
```

You want it to have **two implementations** conceptually:

```text
InterviewGateway
       │
       ├── MockInterviewGateway
       │
       └── HttpInterviewGateway
```

The current mock implementation can remain.

We just need the HTTP implementation.

---

# 3. Ask Cursor to inspect before changing anything

Since Cursor already knows your frontend codebase, give it this prompt:

```text
We now have a working FastAPI backend and need to connect the existing
frontend to it.

IMPORTANT:
Do NOT rewrite the frontend architecture.
Do NOT modify the UI.
Do NOT remove MockInterviewGateway.
Do NOT change the backend API.

First inspect:
- src/interviewGateway.ts
- src/App.tsx
- src/data/candidates.ts
- package.json
- existing Vite configuration
- existing environment configuration

The backend is running at:

http://localhost:8000

API:

POST /api/interview

START request:

{
  "sessionId": "abc-123",
  "candidate": <RAW candidate.json object>
}

START response:

{
  "reply": "...",
  "done": false
}

CONTINUE request:

{
  "sessionId": "abc-123",
  "message": "candidate answer"
}

CONTINUE response:

{
  "reply": "...",
  "done": false
}

FINAL response:

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

The frontend should use the HTTP backend when:

VITE_USE_MOCK=false

and continue using the existing mock gateway when:

VITE_USE_MOCK=true

Implement the smallest possible change.

Requirements:

1. Preserve the existing InterviewGateway interface if possible.
2. Add an HTTP implementation of InterviewGateway.
3. Use fetch() rather than adding Axios.
4. Generate/store a sessionId when an interview starts.
5. Send the RAW candidate JSON object expected by the backend.
6. Send the candidate only on the initial request.
7. Send only sessionId + message on subsequent requests.
8. Convert the backend response into the existing frontend InterviewTurn/Feedback types.
9. Preserve loading/error handling.
10. Do not modify visual/UI components unless absolutely necessary.
11. Do not expose or add any API keys.
12. Do not modify the FastAPI backend.

Environment variables:

VITE_USE_MOCK=false
VITE_API_BASE_URL=http://localhost:8000

After implementing:
- run npm run build
- fix any TypeScript errors
- explain exactly which files were changed.
```

That should be your next Cursor task.

---

# 4. Important: the candidate object

This is probably the **most likely integration issue**.

Your backend expects:

```json
{
  "sessionId": "...",
  "candidate": {
    "member": {...},
    "missions": [...],
    "signals": {...}
  }
}
```

It does **NOT** want the frontend's transformed `CandidateViewModel`.

Your frontend currently has a transformation layer:

```text
candidates.json
       ↓
candidates.ts
       ↓
CandidateViewModel
       ↓
UI
```

That's great for displaying candidates.

But when starting the interview, you need:

```text
Selected candidate
       ↓
RAW candidate JSON
       ↓
POST /api/interview
```

So tell Cursor specifically:

> **Do not send the display/view model to the backend. Send the original raw candidate object.**

This is very important.

---

# 5. Session ID

The frontend needs to create a session ID when the interview starts.

For example:

```ts
const sessionId = crypto.randomUUID();
```

Then:

```json
{
  "sessionId": "generated-id",
  "candidate": {...}
}
```

Every subsequent answer uses that **same** ID:

```json
{
  "sessionId": "same-id",
  "message": "candidate answer"
}
```

So:

```text
START
sessionId = ABC
        ↓
Q1

ANSWER
sessionId = ABC
        ↓
Q2

ANSWER
sessionId = ABC
        ↓
Q3
```

Never generate a new ID for each answer.

---

# 6. Your HTTP implementation should conceptually look like this

You don't necessarily need to manually write this if Cursor implements it, but understand what it's doing.

### Start

```ts
const response = await fetch(
  `${API_BASE_URL}/api/interview`,
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      sessionId,
      candidate: rawCandidate,
    }),
  }
);
```

Then:

```ts
const data = await response.json();
```

---

### Submit answer

```ts
const response = await fetch(
  `${API_BASE_URL}/api/interview`,
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      sessionId,
      message: answer,
    }),
  }
);
```

That's literally the bridge between your two systems.

---

# 7. Environment configuration

I'd create:

```text
frontend/
├── .env
├── .env.example
└── ...
```

Development `.env`:

```env
VITE_USE_MOCK=false
VITE_API_BASE_URL=http://localhost:8000
```

And `.env.example`:

```env
VITE_USE_MOCK=true
VITE_API_BASE_URL=http://localhost:8000
```

Don't put secrets there.

There shouldn't be any AI API key in the frontend.

---

# 8. CORS is already handled

Your backend already allows:

```text
http://localhost:5173
```

So:

```text
localhost:5173
      │
      │ browser request
      ▼
localhost:8000
```

should be permitted.

If your Vite server happens to start on `5174` or another port, you'll get a CORS issue.

If that happens, either:

* start Vite on `5173`, or
* update backend CORS to include the actual development origin.

For now, keep it at `5173`.

---

# 9. Now test the real integration

Once Cursor finishes, start both servers.

### Backend

```bash
uvicorn app.main:app --reload
```

### Frontend

```bash
npm run dev
```

Then open:

```text
http://localhost:5173
```

Go through:

```text
Landing
   ↓
Candidates
   ↓
Select candidate
   ↓
Setup
   ↓
Start Interview
```

When you start the interview, open:

```text
F12
→ Network
```

You should see:

```text
POST http://localhost:8000/api/interview
```

with:

```json
{
  "sessionId": "...",
  "candidate": {
    "member": {},
    "missions": [],
    "signals": {}
  }
}
```

And response:

```json
{
  "reply": "...",
  "done": false
}
```

---

# 10. Then submit an answer

Type something into your interview answer box.

Click submit.

Network should show:

```text
POST http://localhost:8000/api/interview
```

Request:

```json
{
  "sessionId": "THE-SAME-ID",
  "message": "My answer..."
}
```

Response:

```json
{
  "reply": "Next question...",
  "done": false
}
```

The critical thing is:

```text
START sessionId
       ↓
      ABC
       ↓
Answer 1 → ABC
       ↓
Answer 2 → ABC
       ↓
Answer 3 → ABC
```

If the ID changes, the backend will treat it as a new/unknown session.

---

# 11. Finally test completion

Continue until the eighth question.

You should eventually see:

```json
{
  "reply": "Interview completed.",
  "done": true,
  "feedback": {
    "summary": "...",
    "strengths": [...],
    "gaps": [...],
    "next": [...]
  }
}
```

Your frontend should then show the Results screen.

So your complete product is now:

```text
                 YOUR HACKATHON PRODUCT

┌──────────────────────────────────────────┐
│              React Frontend              │
│                                          │
│ Landing → Candidates → Setup             │
│                         ↓                │
│                     Interview             │
│                         ↓                │
│                     Results               │
└─────────────────────┬────────────────────┘
                      │
                      │ HTTP
                      ▼
┌──────────────────────────────────────────┐
│              FastAPI Backend             │
│                                          │
│ POST /api/interview                      │
│          ↓                               │
│ Session Manager                          │
│          ↓                               │
│ Candidate + Curriculum Services          │
│          ↓                               │
│ Mock Interview Engine                    │
└──────────────────────────────────────────┘
```

### And don't add the real LLM yet.

First get **this exact flow working from the browser**.

Once you can select a candidate → start → answer → get 8 questions → see feedback **without opening Swagger**, your frontend/backend integration is complete.

Then you're ready for the most important next phase: replacing the deterministic mock engine with the actual **AI interviewer**, while keeping this API contract unchanged.


## Prompt No.19

**AI Tool: Cursor**

**Author: Yash Palkar** 

### Prompt
We now have a working FastAPI backend and need to connect the existing
frontend to it.

IMPORTANT:
Do NOT rewrite the frontend architecture.
Do NOT modify the UI.
Do NOT remove MockInterviewGateway.
Do NOT change the backend API.

First inspect:
- src/interviewGateway.ts
- src/App.tsx
- src/data/candidates.ts
- package.json
- existing Vite configuration
- existing environment configuration

The backend is running at:

http://localhost:8000

API:

POST /api/interview

START request:

{
  "sessionId": "abc-123",
  "candidate": <RAW candidate.json object>
}

START response:

{
  "reply": "...",
  "done": false
}

CONTINUE request:

{
  "sessionId": "abc-123",
  "message": "candidate answer"
}

CONTINUE response:

{
  "reply": "...",
  "done": false
}

FINAL response:

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

The frontend should use the HTTP backend when:

VITE_USE_MOCK=false

and continue using the existing mock gateway when:

VITE_USE_MOCK=true

Implement the smallest possible change.

Requirements:

1. Preserve the existing InterviewGateway interface if possible.
2. Add an HTTP implementation of InterviewGateway.
3. Use fetch() rather than adding Axios.
4. Generate/store a sessionId when an interview starts.
5. Send the RAW candidate JSON object expected by the backend.
6. Send the candidate only on the initial request.
7. Send only sessionId + message on subsequent requests.
8. Convert the backend response into the existing frontend InterviewTurn/Feedback types.
9. Preserve loading/error handling.
10. Do not modify visual/UI components unless absolutely necessary.
11. Do not expose or add any API keys.
12. Do not modify the FastAPI backend.

Environment variables:

VITE_USE_MOCK=false
VITE_API_BASE_URL=http://localhost:8000

After implementing:
- run npm run build
- fix any TypeScript errors
- explain exactly which files were changed.

### Outcome
The frontend was already wired for live mode — `ApiInterviewGateway`, `useInterview`, session handling, and raw candidate payloads were in place. The only functional gap was that `postInterview` used Axios instead of `fetch()`.

## What changed

| File | Change |
|------|--------|
| `frontend/src/services/interview.ts` | Replaced Axios with `fetch()` — POSTs to `{VITE_API_BASE_URL}/api/interview`, sends start (`sessionId` + raw `candidate`) or continue (`sessionId` + `message`), validates and returns `InterviewResponse` |
| `frontend/src/services/api.ts` | Removed Axios client; kept `getApiErrorMessage()` for thrown `Error` messages from fetch |
| `frontend/vite.config.ts` | Updated dev proxy target from port 3000 → **8000** |
| `frontend/.env.example` | Documented live-mode defaults |

**Unchanged:** `interviewGateway.ts` (both gateways), `useInterview.ts`, UI components, types, backend.

## How it works

- `VITE_USE_MOCK=true` → `MockInterviewGateway` (unchanged)
- `VITE_USE_MOCK=false` → `ApiInterviewGateway` → `fetch()` → `http://localhost:8000/api/interview`

`useInterview` already generates a UUID via `startFreshSession()`, sends the raw candidate on start only, and maps `InterviewResponse` (including `feedback`) into existing state.

## Run live mode

```bash
# frontend/
cp .env.example .env
npm run dev
```

Ensure the backend is running:

```bash
cd backend && uvicorn app.main:app --reload
```

`npm run build` completed successfully with no TypeScript errors.

## Prompt No.20

**AI Tool: Chatgpt**

**Author: Yash Palkar** 

### Prompt
The frontend was already wired for live mode — `ApiInterviewGateway`, `useInterview`, session handling, and raw candidate payloads were in place. The only functional gap was that `postInterview` used Axios instead of `fetch()`.

## What changed

| File                                 | Change                                                                                                                                                                                                     |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `frontend/src/services/interview.ts` | Replaced Axios with `fetch()` — POSTs to `{VITE_API_BASE_URL}/api/interview`, sends start (`sessionId` + raw `candidate`) or continue (`sessionId` + `message`), validates and returns `InterviewResponse` |
| `frontend/src/services/api.ts`       | Removed Axios client; kept `getApiErrorMessage()` for thrown `Error` messages from fetch                                                                                                                   |
| `frontend/vite.config.ts`            | Updated dev proxy target from port 3000 → **8000**                                                                                                                                                         |
| `frontend/.env.example`              | Documented live-mode defaults                                                                                                                                                                              |

**Unchanged:** `interviewGateway.ts` (both gateways), `useInterview.ts`, UI components, types, backend.

## How it works

- `VITE_USE_MOCK=true` → `MockInterviewGateway` (unchanged)
- `VITE_USE_MOCK=false` → `ApiInterviewGateway` → `fetch()` → `http://localhost:8000/api/interview`

`useInterview` already generates a UUID via `startFreshSession()`, sends the raw candidate on start only, and maps `InterviewResponse` (including `feedback`) into existing state.

## Run live mode

```bash
# frontend/
cp .env.example .env
npm run dev
```

Ensure the backend is running:

```bash
cd backend && uvicorn app.main:app --reload
```

`npm run build` completed successfully with no TypeScript errors.

this is what cursor finished with, but i still couldnt see the POST req in the network tab what to do now

### Outcome
Yep — don't change the backend yet. Since Cursor says the frontend is already wired, the next job is to find **why the code path that calls `postInterview()` isn't being reached**.

The key clue is:

> You don't see **any** POST request in Network.

That usually means the problem is **before `fetch()`**, rather than CORS/backend.

## 1. First check that you're actually running the updated frontend

Stop the frontend server completely with `Ctrl+C`.

Then from the **frontend directory** run:

```bash
npm run dev
```

Look at the terminal. You should see something like:

```text
Local: http://localhost:5173/
```

Open **that exact URL**.

Don't open an old tab/bookmark.

Then do:

```text
Ctrl + Shift + R
```

to hard-refresh the page.

---

# 2. Check the `.env` file

This is VERY important.

Cursor says:

```text
VITE_USE_MOCK=false
```

But it only says `.env.example` was updated.

You need an actual:

```text
frontend/.env
```

containing:

```env
VITE_USE_MOCK=false
VITE_API_BASE_URL=http://localhost:8000
```

### Not this:

```text
.env.example
```

### This:

```text
.env
```

Vite only loads the actual environment file.

After creating/changing `.env`, **restart Vite**:

```bash
Ctrl+C
npm run dev
```

Vite reads environment variables when it starts.

---

# 3. Check whether live mode is actually active

This is the fastest diagnostic.

Ask Cursor to temporarily add a console log at the point where the gateway is selected.

Give Cursor:

```text
The frontend build succeeds, but when I start an interview I don't see
POST /api/interview in the browser Network tab.

Do not modify the architecture.

Inspect the existing:
- interviewGateway.ts
- services/interview.ts
- useInterview.ts
- environment configuration

First determine whether VITE_USE_MOCK=false is actually causing
ApiInterviewGateway to be selected.

Add temporary console logging only for debugging that shows:

1. VITE_USE_MOCK value
2. selected gateway (MockInterviewGateway or ApiInterviewGateway)
3. when postInterview() is called
4. the API URL being used

Do not change the behavior otherwise.

After identifying the issue, explain the cause before making a permanent fix.
```

Then reload the app and look at:

```text
F12
→ Console
```

You should see something conceptually like:

```text
VITE_USE_MOCK = false
Selected gateway = ApiInterviewGateway
```

If instead you see:

```text
VITE_USE_MOCK = true
Selected gateway = MockInterviewGateway
```

we've found the problem.

---

# 4. Make sure you're actually starting the interview

This sounds obvious, but Network only shows the request **after the function executes**.

Go through:

```text
Candidate
   ↓
Select candidate
   ↓
Start Interview
```

Then immediately check:

```text
F12
→ Network
→ Fetch/XHR
```

Don't filter for only `POST` initially.

Clear the Network tab first:

```text
🗑 Clear
```

Then click the actual **Start Interview** button.

You should see something like:

```text
interview
POST
200
```

---

# 5. Check the Console for JavaScript errors

Before clicking Start Interview, open:

```text
F12
→ Console
```

Look for red errors.

Especially things like:

```text
Uncaught TypeError
```

or:

```text
Failed to fetch
```

or:

```text
Cannot read properties of undefined
```

If there is a frontend exception **before `fetch()`**, Network will show nothing.

---

# 6. Check the backend terminal

Keep this running:

```bash
uvicorn app.main:app --reload
```

When the frontend successfully calls the backend, the backend terminal should show something like:

```text
127.0.0.1:xxxxx - "POST /api/interview HTTP/1.1" 200 OK
```

So we have a very simple diagnostic:

| What you see                                     | Meaning                              |
| ------------------------------------------------ | ------------------------------------ |
| Nothing in Network + nothing in backend terminal | `postInterview()` isn't being called |
| Network request but backend sees nothing         | Browser/network/proxy issue          |
| Backend sees `POST` + 4xx                        | Request payload/API contract issue   |
| Backend sees `POST` + 200                        | Integration works                    |
| Network shows `OPTIONS` but not POST             | CORS/preflight issue                 |

**Based on what you're describing, I suspect the first case.**

---

# 7. One more important thing: Vite proxy vs API URL

Cursor changed:

```text
vite.config.ts
```

from port `3000` → `8000`.

That's okay, but there are two possible approaches.

### Direct API

Frontend:

```text
localhost:5173
       │
       │ fetch()
       ▼
localhost:8000/api/interview
```

### Vite proxy

Frontend:

```text
localhost:5173
       │
       │ /api/interview
       ▼
Vite proxy
       │
       ▼
localhost:8000
```

Cursor says your code is using:

```text
VITE_API_BASE_URL=http://localhost:8000
```

so you're probably doing the **first approach**.

That's perfectly fine for development.

---

# 8. Let's do one extremely useful test

Open your browser console and run:

```javascript
fetch("http://localhost:8000/api/interview", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    sessionId: crypto.randomUUID(),
    candidate: {}
  })
})
```

You'll probably get a `422`, because `{}` isn't a valid candidate.

**That's okay.**

The important thing is whether the browser makes the request.

Go to:

```text
F12 → Network
```

and you should see:

```text
POST /api/interview
```

If you see that, your browser can reach the backend.

Then we know the problem is definitely somewhere in the frontend's interview flow.

---

# 9. Better: use a REAL candidate for this test

Take one complete candidate object from:

```text
backend/app/data/candidates.json
```

and run:

```javascript
fetch("http://localhost:8000/api/interview", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    sessionId: crypto.randomUUID(),
    candidate: YOUR_REAL_CANDIDATE_OBJECT
  })
})
.then(r => r.json())
.then(console.log)
```

You should get:

```json
{
  "reply": "...",
  "done": false
}
```

If that works, your:

```text
Browser
   ↓
localhost:8000
   ↓
FastAPI
```

connection is definitely good.

---

# 10. I would NOT ask Cursor to make more changes yet

Right now we want to locate the problem rather than let Cursor start modifying things randomly.

Do these **three things in order**:

### A.

Check:

```text
frontend/.env
```

It should contain:

```env
VITE_USE_MOCK=false
VITE_API_BASE_URL=http://localhost:8000
```

Restart Vite afterward.

### B.

Open DevTools → Console and check whether the app is actually selecting:

```text
ApiInterviewGateway
```

### C.

If it still doesn't work, give Cursor the debugging prompt above and get it to log:

```text
VITE_USE_MOCK
selected gateway
postInterview called
API URL
```

---

## Send me these 3 things after that

You don't need to send the whole project.

Just send:

1. **Your `frontend/.env` contents** (only these two variables; no secrets)
2. **What the browser Console says when you click Start Interview**
3. **The relevant code from `interviewGateway.ts`**

Then I can tell you exactly where the request is getting stuck instead of guessing.



## Prompt No. 21

**AI Tool: Cursor**

**Author: Yash Palkar** 

### Prompt
The frontend build succeeds, but when I start an interview I don't see
POST /api/interview in the browser Network tab.

Do not modify the architecture.

Inspect the existing:
- interviewGateway.ts
- services/interview.ts
- useInterview.ts
- environment configuration

First determine whether VITE_USE_MOCK=false is actually causing
ApiInterviewGateway to be selected.

Add temporary console logging only for debugging that shows:

1. VITE_USE_MOCK value
2. selected gateway (MockInterviewGateway or ApiInterviewGateway)
3. when postInterview() is called
4. the API URL being used

Do not change the behavior otherwise.

After identifying the issue, explain the cause before making a permanent fix.

### Outcome
## Diagnosis

**`VITE_USE_MOCK=false` was not taking effect** because there was no `frontend/.env` file — only `frontend/.env.example`.

Vite loads `.env`, `.env.local`, etc., but **not** `.env.example`. So at runtime:

```ts
import.meta.env.VITE_USE_MOCK  // undefined
undefined !== "false"          // true  → mock mode
```

That means `createGateway()` always picked **`MockInterviewGateway`**, which never calls `postInterview()` — so nothing showed up in the Network tab.

`useInterview.ts` is fine: it calls `interviewGateway.startInterview()` correctly. The gateway selection happened once at module load, before any interview started.

---

## What the debug logs will show

**Before fix** (no


## Prompt No. 22

**AI Tool: Chatgpt**

**Author: Yash Palkar** 

### Prompt
cursor made the frontend/.env and now we can see the POST req in the network tab, so the frontend backend has been linked right ? or are there any other steps also, what to do next

### Outcome

Yes — **if you can see `POST /api/interview` in the browser Network tab when you start/continue the interview, the frontend is now actually calling the backend.** 🎉

But there's one more distinction:

> **Seeing the POST means the connection is established. Seeing the correct response and completing the interview through the UI means the integration is working end-to-end.**

So don't start the AI/LLM work quite yet. Do this checklist first.

## 1. Verify the POST response

In DevTools:

```text
Network
  ↓
POST /api/interview
  ↓
Response
```

For the first request, you want:

```json
{
  "reply": "...",
  "done": false
}
```

and ideally HTTP:

```text
200 OK
```

If you see `200`, excellent.

---

## 2. Verify the request payload

Click the POST → **Payload**.

For the first request it should look like:

```json
{
  "sessionId": "some-uuid",
  "candidate": {
    "member": {...},
    "missions": [...],
    "signals": {...}
  }
}
```

The important things are:

* `sessionId` exists
* `candidate` is the **raw candidate structure**
* `candidate` contains the expected `member`, `missions`, `signals`
* you're not accidentally sending the frontend `CandidateViewModel`

---

## 3. Verify continuation requests

This is even more important.

Submit an answer.

You should see another:

```text
POST /api/interview
```

But this time the payload should be:

```json
{
  "sessionId": "THE-SAME-UUID",
  "message": "your answer..."
}
```

Notice:

```text
START:
sessionId + candidate

CONTINUE:
sessionId + message
```

And **the session ID must remain identical**.

For example:

```text
START       → abc-123
Answer 1    → abc-123
Answer 2    → abc-123
Answer 3    → abc-123
...
Answer 8    → abc-123
```

---

## 4. Complete the entire interview from the UI

This is the real integration test.

Don't use Swagger now.

Do:

```text
Select candidate
      ↓
Start interview
      ↓
Question 1
      ↓
Submit answer
      ↓
Question 2
      ↓
...
      ↓
Question 8
      ↓
Interview completed
      ↓
Results page
```

At the end, check that the frontend actually displays the backend feedback:

```json
{
  "feedback": {
    "summary": "...",
    "strengths": [],
    "gaps": [],
    "next": []
  }
}
```

If the Results page shows that correctly, **frontend ↔ backend integration is done.**

---

# 5. Check the backend terminal too

While doing the interview, your FastAPI terminal should show requests similar to:

```text
POST /api/interview 200 OK
POST /api/interview 200 OK
POST /api/interview 200 OK
...
```

You should see roughly one POST per interview interaction.

That confirms the requests are reaching FastAPI.

---

# 6. Test the error cases from the actual frontend

You don't need to deliberately break the UI, but check that errors don't crash the app.

For example, if the backend becomes unavailable:

```text
Frontend
   ↓
Backend unavailable
   ↓
Frontend displays a sensible error
```

You don't want:

```text
Uncaught TypeError...
blank screen
```

Your existing `getApiErrorMessage()` should help here.

---

# 7. One important thing before the AI phase

Right now your architecture is:

```text
React
  ↓
ApiInterviewGateway
  ↓
POST /api/interview
  ↓
FastAPI
  ↓
Session Manager
  ↓
Mock Interview Engine
  ↓
Response
```

That is **exactly what you want at this stage**.

The next change should NOT be:

```text
Frontend → LLM
```

Instead:

```text
React
  ↓
ApiInterviewGateway
  ↓
FastAPI
  ↓
Session Manager
  ↓
AI Interview Engine
  ↓
LLM
```

Your frontend shouldn't need to know whether the interviewer is mock or AI.

That's a good architecture for the hackathon.

---

# So your current status

I'd consider you here:

```text
                    STATUS

Frontend UI                  ✅
Frontend gateway             ✅
Environment configuration    ✅
FastAPI                      ✅
API contract                 ✅
Session management           ✅
Mock interview               ✅
Automated tests              ✅ 8/8
Swagger testing              ✅
Frontend → Backend request   ✅
```

Now you need to confirm:

```text
Full UI interview            ⬅️ DO THIS NOW
        ↓
Final feedback displayed     ⬅️ DO THIS NOW
        ↓
AI interviewer               ⬅️ THEN START
```

### My recommendation

**Do one complete interview from the actual frontend right now.** Don't change any code.

If you can:

1. select a candidate,
2. start the interview,
3. answer all 8 questions,
4. see the next questions arrive,
5. reach `done: true`,
6. see the feedback on the Results page,

then **freeze this version and make a Git commit**:

```bash
git add .
git commit -m "feat: connect frontend to interview backend"
```

That gives you a safe working checkpoint.

**After that, your next task is the real AI interviewer.** That's where we should carefully design the prompt/context/structured output and replace the mock engine without breaking the API you've just finished integrating.

