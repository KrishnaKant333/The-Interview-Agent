import type { Candidate, Feedback, InterviewTurn } from "./types";

export interface InterviewGateway {
  start(candidate: Candidate): Promise<InterviewTurn>;
  submit(answer: string): Promise<InterviewTurn>;
  feedback(): Promise<Feedback>;
}

const wait = (milliseconds: number) => new Promise((resolve) => setTimeout(resolve, milliseconds));

class MockInterviewGateway implements InterviewGateway {
  private index = 0;
  private strongAnswer = false;
  private readonly questions = [
    ["In your own words, what problem does Retrieval-Augmented Generation solve?", "RAG", "Foundation"],
    ["You mentioned retrieval. Why are embeddings useful for retrieving relevant context?", "Embeddings", "Intermediate"],
    ["How would you decide whether to use vector search, keyword search, or a hybrid approach?", "Retrieval", "Advanced"],
    ["Walk me through the main components you would include in a RAG pipeline.", "System design", "Intermediate"],
    ["What can cause a RAG answer to be inaccurate even if the source documents are correct?", "Evaluation", "Advanced"],
    ["How would you write a prompt that asks the model to cite only supplied context?", "Prompt engineering", "Intermediate"],
    ["What would you monitor after deploying this system?", "Deployment", "Intermediate"],
    ["Which part of this design would you improve first, and what trade-off would that introduce?", "Reasoning", "Advanced"],
  ] as const;

  async start(): Promise<InterviewTurn> { this.index = 0; await wait(700); return this.turn(); }
  async submit(answer: string): Promise<InterviewTurn> { this.strongAnswer = answer.trim().split(/\s+/).length > 18; this.index++; await wait(900); return this.turn(); }
  async feedback(): Promise<Feedback> { await wait(650); return { overall: this.strongAnswer ? 84 : 76, summary: "You showed a clear grasp of retrieval concepts and connected them to practical product decisions.", skills: [{ label: "Technical knowledge", score: 84 }, { label: "Reasoning", score: 81 }, { label: "Communication", score: 78 }, { label: "System design", score: 75 }], strengths: ["Explains RAG concepts clearly", "Connects technical choices to user outcomes", "Recognizes retrieval trade-offs"], improvements: ["Use a concrete example earlier in your answer", "Be more explicit about evaluation metrics"], recommendations: ["Review the curriculum day covering vector databases", "Practice RAG evaluation and grounded-answer testing", "Revisit deployment and monitoring concepts"] }; }
  private turn(): InterviewTurn { const done = this.index >= this.questions.length; if (done) return { question: "Interview complete", topic: "", difficulty: "Intermediate", current: 8, total: 8, completed: true }; const [question, topic, difficulty] = this.questions[this.index]; return { question, topic, difficulty, current: this.index + 1, total: 8, evaluatorNote: this.index > 0 ? this.strongAnswer ? "Good reasoning. Let’s go one level deeper." : "Good start. Let’s make this more concrete." : undefined, completed: false }; }
}

export const interviewGateway: InterviewGateway = new MockInterviewGateway();