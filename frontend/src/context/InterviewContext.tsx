import { createContext, useContext, type ReactNode } from "react";
import { useInterview, type UseInterviewReturn } from "../hooks/useInterview";

const InterviewContext = createContext<UseInterviewReturn | null>(null);

export function InterviewProvider({ children }: { children: ReactNode }) {
  const value = useInterview();
  return <InterviewContext.Provider value={value}>{children}</InterviewContext.Provider>;
}

export function useInterviewContext(): UseInterviewReturn {
  const context = useContext(InterviewContext);
  if (!context) {
    throw new Error("useInterviewContext must be used within InterviewProvider");
  }
  return context;
}
