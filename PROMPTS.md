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