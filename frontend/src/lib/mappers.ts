import type { DemoFeedbackPresentation, InterviewFeedback } from "../types";

/** Derives demo-only skill scores for visual presentation — not from the API. */
export function buildDemoPresentation(feedback: InterviewFeedback): DemoFeedbackPresentation {
  const base = Math.min(92, 68 + feedback.strengths.length * 4 - feedback.gaps.length * 2);

  return {
    overall: base,
    skills: [
      { label: "Technical knowledge", score: Math.min(95, base + 4) },
      { label: "Reasoning", score: Math.min(95, base + 1) },
      { label: "Communication", score: Math.min(95, base - 3) },
      { label: "System design", score: Math.min(95, base - 6) },
    ],
  };
}
