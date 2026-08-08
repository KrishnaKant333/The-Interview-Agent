import type { InterviewResponse, RawCandidate } from "./types";
import { postInterview } from "./services/interview";

export interface InterviewGateway {
  startInterview(sessionId: string, rawCandidate: RawCandidate): Promise<InterviewResponse>;
  sendMessage(sessionId: string, message: string): Promise<InterviewResponse>;
}

const wait = (milliseconds: number) =>
  new Promise((resolve) => setTimeout(resolve, milliseconds));

class MockInterviewGateway implements InterviewGateway {
  private history: string[] = [];
  private questionIndex = 0;
  private strongAnswers = 0;

  private readonly questions = [
    "In your own words, what problem does Retrieval-Augmented Generation solve?",
    "You mentioned retrieval. Why are embeddings useful for retrieving relevant context?",
    "How would you decide whether to use vector search, keyword search, or a hybrid approach?",
    "Walk me through the main components you would include in a RAG pipeline.",
    "What can cause a RAG answer to be inaccurate even if the source documents are correct?",
    "How would you write a prompt that asks the model to cite only supplied context?",
    "What would you monitor after deploying this system?",
    "Which part of this design would you improve first, and what trade-off would that introduce?",
  ];

  async startInterview(_sessionId: string, rawCandidate: RawCandidate): Promise<InterviewResponse> {
    this.history = [];
    this.questionIndex = 0;
    this.strongAnswers = 0;
    await wait(700);

    const welcome = `Welcome, ${rawCandidate.member.name.split(" ")[0]}. Let's begin your personalized technical interview.`;
    this.history.push(`Interviewer: ${welcome}`);
    this.history.push(`Interviewer: ${this.questions[0]}`);

    return { reply: `${welcome}\n\n${this.questions[0]}`, done: false };
  }

  async sendMessage(_sessionId: string, message: string): Promise<InterviewResponse> {
    const trimmed = message.trim();
    if (!trimmed) {
      throw new Error("Answer cannot be empty.");
    }

    this.history.push(`Candidate: ${trimmed}`);
    if (trimmed.split(/\s+/).length > 18) {
      this.strongAnswers++;
    }

    this.questionIndex++;
    await wait(900);

    if (this.questionIndex >= this.questions.length) {
      const closing = "Interview completed.";
      this.history.push(`Interviewer: ${closing}`);

      return {
        reply: closing,
        done: true,
        feedback: {
          summary:
            "You showed a clear grasp of retrieval concepts and connected them to practical product decisions.",
          strengths: [
            "Explains RAG concepts clearly",
            "Connects technical choices to user outcomes",
            "Recognizes retrieval trade-offs",
          ],
          gaps: [
            "Use a concrete example earlier in your answer",
            "Be more explicit about evaluation metrics",
          ],
          next: [
            "Review the curriculum day covering vector databases",
            "Practice RAG evaluation and grounded-answer testing",
            "Revisit deployment and monitoring concepts",
          ],
        },
      };
    }

    const followUp = this.questions[this.questionIndex];
    this.history.push(`Interviewer: ${followUp}`);

    return { reply: followUp, done: false };
  }
}

class ApiInterviewGateway implements InterviewGateway {
  startInterview(sessionId: string, rawCandidate: RawCandidate): Promise<InterviewResponse> {
    return postInterview({ sessionId, candidate: rawCandidate });
  }

  sendMessage(sessionId: string, message: string): Promise<InterviewResponse> {
    return postInterview({ sessionId, message });
  }
}

function createGateway(): InterviewGateway {
  const mockEnv = import.meta.env.VITE_USE_MOCK;
  const useMock = mockEnv !== "false";
  const gatewayName = useMock ? "MockInterviewGateway" : "ApiInterviewGateway";

  // TEMP DEBUG — remove after verifying live API mode
  console.log("[interviewGateway] VITE_USE_MOCK:", mockEnv);
  console.log("[interviewGateway] selected gateway:", gatewayName);

  if (useMock) {
    return new MockInterviewGateway();
  }
  return new ApiInterviewGateway();
}

export const interviewGateway: InterviewGateway = createGateway();
