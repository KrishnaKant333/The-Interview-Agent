import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AnswerForm } from "../components/interview/AnswerForm";
import { InterviewSidebar } from "../components/interview/InterviewSidebar";
import { ErrorBanner } from "../components/common/ErrorBanner";
import { useInterviewContext } from "../context/InterviewContext";

export default function Interview() {
  const navigate = useNavigate();
  const {
    candidate,
    currentReply,
    questionNumber,
    totalQuestions,
    isLoading,
    error,
    done,
    messages,
    sendMessage,
    retry,
  } = useInterviewContext();
  const [answer, setAnswer] = useState("");

  useEffect(() => {
    if (!candidate) {
      navigate("/candidates", { replace: true });
      return;
    }
    if (messages.length === 0 && !isLoading) {
      navigate("/setup", { replace: true });
    }
  }, [candidate, messages.length, isLoading, navigate]);

  useEffect(() => {
    if (done) {
      navigate("/feedback", { replace: true });
    }
  }, [done, navigate]);

  if (!candidate || messages.length === 0) {
    return null;
  }

  const handleSubmit = async () => {
    const trimmed = answer.trim();
    if (!trimmed || isLoading) return;
    setAnswer("");
    await sendMessage(trimmed);
  };

  return (
    <section className="interview-shell">
      <div className="interview-main">
        <div className="progress-label">
          <span>AI INTERVIEWER</span>
          <span>
            Question {questionNumber} / {totalQuestions}
          </span>
        </div>
        {error && <ErrorBanner message={error} onRetry={retry} />}
        <div className="question">
          <div>
            <h2>{currentReply}</h2>
          </div>
        </div>
        <AnswerForm
          value={answer}
          onChange={setAnswer}
          onSubmit={handleSubmit}
          isLoading={isLoading}
          disabled={done}
        />
      </div>
      <InterviewSidebar questionNumber={questionNumber} totalQuestions={totalQuestions} />
    </section>
  );
}
