/** Raw candidate object as defined in candidates.json — sent to the API as-is. */
export type RawCandidate = {
  member: {
    id: string;
    name: string;
    jobRole: string;
    yearsExperience: number;
    education: string;
    status?: string;
  };
  missions: Array<{
    day: number;
    title?: string;
    passed?: boolean;
    skipped?: boolean;
    attempts?: number;
  }>;
  signals: {
    commitDays: number;
    missionsCompleted: number;
    missionsFirstTry: number;
  };
};

/** UI-facing candidate derived from raw data — never sent to the API. */
export type CandidateViewModel = {
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

export type InterviewFeedback = {
  summary: string;
  strengths: string[];
  gaps: string[];
  next: string[];
};

export type InterviewResponse = {
  reply: string;
  done: boolean;
  feedback?: InterviewFeedback;
};

export type InterviewStartRequest = {
  sessionId: string;
  candidate: RawCandidate;
};

export type InterviewMessageRequest = {
  sessionId: string;
  message: string;
};

export type InterviewRequest = InterviewStartRequest | InterviewMessageRequest;

export type ChatMessage = {
  role: "interviewer" | "candidate";
  content: string;
};

/** Demo-only presentation data — not part of the official API contract. */
export type DemoFeedbackPresentation = {
  overall: number;
  skills: { label: string; score: number }[];
};

export const DEFAULT_TOTAL_QUESTIONS = 8;
