import { useCallback, useState } from "react";
import { getCandidatePair } from "../Given_Data/candidates";
import { interviewGateway } from "../interviewGateway";
import { buildDemoPresentation } from "../lib/mappers";
import {
  clearSessionId,
  getSessionId,
  startFreshSession,
} from "../lib/session";
import { getApiErrorMessage } from "../services/api";
import type {
  CandidateViewModel,
  ChatMessage,
  DemoFeedbackPresentation,
  InterviewFeedback,
  RawCandidate,
} from "../types";
import { DEFAULT_TOTAL_QUESTIONS } from "../types";

const CANDIDATE_KEY = "interview:candidateId";
const MESSAGES_KEY = "interview:messages";
const QUESTION_KEY = "interview:questionNumber";
const DONE_KEY = "interview:done";
const FEEDBACK_KEY = "interview:feedback";
const DEMO_KEY = "interview:demoPresentation";

function readStoredMessages(): ChatMessage[] {
  try {
    const raw = sessionStorage.getItem(MESSAGES_KEY);
    return raw ? (JSON.parse(raw) as ChatMessage[]) : [];
  } catch {
    return [];
  }
}

function readStoredFeedback(): InterviewFeedback | null {
  try {
    const raw = sessionStorage.getItem(FEEDBACK_KEY);
    return raw ? (JSON.parse(raw) as InterviewFeedback) : null;
  } catch {
    return null;
  }
}

function readStoredDemo(): DemoFeedbackPresentation | null {
  try {
    const raw = sessionStorage.getItem(DEMO_KEY);
    return raw ? (JSON.parse(raw) as DemoFeedbackPresentation) : null;
  } catch {
    return null;
  }
}

export function useInterview() {
  const [sessionId, setSessionIdState] = useState<string | null>(() => getSessionId());
  const [candidate, setCandidate] = useState<CandidateViewModel | null>(() => {
    const id = sessionStorage.getItem(CANDIDATE_KEY);
    if (!id) return null;
    return getCandidatePair(id)?.viewModel ?? null;
  });
  const [rawCandidate, setRawCandidate] = useState<RawCandidate | null>(() => {
    const id = sessionStorage.getItem(CANDIDATE_KEY);
    if (!id) return null;
    return getCandidatePair(id)?.raw ?? null;
  });
  const [messages, setMessages] = useState<ChatMessage[]>(() => readStoredMessages());
  const [questionNumber, setQuestionNumber] = useState(() => {
    const stored = sessionStorage.getItem(QUESTION_KEY);
    return stored ? Number(stored) : 0;
  });
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [done, setDone] = useState(() => sessionStorage.getItem(DONE_KEY) === "true");
  const [feedback, setFeedback] = useState<InterviewFeedback | null>(() => readStoredFeedback());
  const [demoPresentation, setDemoPresentation] = useState<DemoFeedbackPresentation | null>(
    () => readStoredDemo(),
  );

  const totalQuestions = DEFAULT_TOTAL_QUESTIONS;

  const persistMessages = useCallback((next: ChatMessage[]) => {
    setMessages(next);
    sessionStorage.setItem(MESSAGES_KEY, JSON.stringify(next));
  }, []);

  const selectCandidate = useCallback(
    (viewModel: CandidateViewModel, raw: RawCandidate) => {
      setCandidate(viewModel);
      setRawCandidate(raw);
      sessionStorage.setItem(CANDIDATE_KEY, viewModel.id);
      setError(null);
    },
    [],
  );

  const clearInterviewState = useCallback(() => {
    setMessages([]);
    setQuestionNumber(0);
    setDone(false);
    setFeedback(null);
    setDemoPresentation(null);
    setError(null);
    setCandidate(null);
    setRawCandidate(null);
    clearSessionId();
    sessionStorage.removeItem(CANDIDATE_KEY);
    sessionStorage.removeItem(MESSAGES_KEY);
    sessionStorage.removeItem(QUESTION_KEY);
    sessionStorage.removeItem(DONE_KEY);
    sessionStorage.removeItem(FEEDBACK_KEY);
    sessionStorage.removeItem(DEMO_KEY);
    setSessionIdState(null);
  }, []);

  const resetInterview = useCallback(() => {
    clearInterviewState();
  }, [clearInterviewState]);

  const startInterview = useCallback(async (): Promise<boolean> => {
    if (!rawCandidate || isLoading) return false;

    setIsLoading(true);
    setError(null);

    try {
      const id = startFreshSession();
      setSessionIdState(id);

      const response = await interviewGateway.startInterview(id, rawCandidate);

      if (!response.reply.trim()) {
        throw new Error("Empty response from the interview service.");
      }

      const nextMessages: ChatMessage[] = [{ role: "interviewer", content: response.reply }];
      persistMessages(nextMessages);
      setQuestionNumber(1);
      sessionStorage.setItem(QUESTION_KEY, "1");
      setDone(false);
      sessionStorage.setItem(DONE_KEY, "false");
      setFeedback(null);
      setDemoPresentation(null);
      sessionStorage.removeItem(FEEDBACK_KEY);
      sessionStorage.removeItem(DEMO_KEY);
      return true;
    } catch (err) {
      setError(getApiErrorMessage(err));
      return false;
    } finally {
      setIsLoading(false);
    }
  }, [rawCandidate, isLoading, persistMessages]);

  const sendMessage = useCallback(
    async (message: string) => {
      const trimmed = message.trim();
      if (!trimmed || !sessionId || isLoading || done) return;

      setIsLoading(true);
      setError(null);

      const withCandidate: ChatMessage[] = [
        ...messages,
        { role: "candidate", content: trimmed },
      ];
      persistMessages(withCandidate);

      try {
        const response = await interviewGateway.sendMessage(sessionId, trimmed);

        if (!response.reply.trim() && !response.done) {
          throw new Error("Empty response from the interview service.");
        }

        const withReply: ChatMessage[] = response.reply.trim()
          ? [...withCandidate, { role: "interviewer", content: response.reply }]
          : withCandidate;
        persistMessages(withReply);

        if (response.done) {
          if (!response.feedback) {
            throw new Error("Interview finished without feedback.");
          }
          setDone(true);
          sessionStorage.setItem(DONE_KEY, "true");
          setFeedback(response.feedback);
          sessionStorage.setItem(FEEDBACK_KEY, JSON.stringify(response.feedback));
          const demo = buildDemoPresentation(response.feedback);
          setDemoPresentation(demo);
          sessionStorage.setItem(DEMO_KEY, JSON.stringify(demo));
          setQuestionNumber(totalQuestions);
          sessionStorage.setItem(QUESTION_KEY, String(totalQuestions));
        } else {
          const nextQuestion = Math.min(questionNumber + 1, totalQuestions);
          setQuestionNumber(nextQuestion);
          sessionStorage.setItem(QUESTION_KEY, String(nextQuestion));
        }
      } catch (err) {
        setMessages(messages);
        sessionStorage.setItem(MESSAGES_KEY, JSON.stringify(messages));
        setError(getApiErrorMessage(err));
      } finally {
        setIsLoading(false);
      }
    },
    [sessionId, isLoading, done, messages, persistMessages, questionNumber, totalQuestions],
  );

  const retry = useCallback(() => {
    setError(null);
  }, []);

  const currentReply =
    messages.filter((message) => message.role === "interviewer").at(-1)?.content ?? "";

  return {
    sessionId,
    candidate,
    rawCandidate,
    messages,
    currentReply,
    questionNumber: questionNumber || (messages.length > 0 ? 1 : 0),
    totalQuestions,
    isLoading,
    error,
    done,
    feedback,
    demoPresentation,
    selectCandidate,
    startInterview,
    sendMessage,
    resetInterview,
    retry,
  };
}

export type UseInterviewReturn = ReturnType<typeof useInterview>;
