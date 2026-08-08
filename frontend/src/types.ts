export type Difficulty = "Foundation" | "Intermediate" | "Advanced";

export type Candidate = {
  id: string;
  name: string;
  role: string;
  yearsExperience: number;
  education: string;
  completedDays: number[];
  completedCount: number;
  firstTryCount: number;
  commitDays: number;
  strength: string;
  focus: string;
};
export type InterviewTurn = { question: string; topic: string; difficulty: Difficulty; current: number; total: number; evaluatorNote?: string; completed: boolean; };
export type Feedback = { overall: number; summary: string; skills: { label: string; score: number }[]; strengths: string[]; improvements: string[]; recommendations: string[]; };
