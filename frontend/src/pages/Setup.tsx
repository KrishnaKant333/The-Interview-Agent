import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { ErrorBanner } from "../components/common/ErrorBanner";
import { useInterviewContext } from "../context/InterviewContext";

export default function Setup() {
  const navigate = useNavigate();
  const { candidate, startInterview, isLoading, error, retry, messages } = useInterviewContext();

  useEffect(() => {
    if (!candidate) {
      navigate("/candidates", { replace: true });
    }
  }, [candidate, navigate]);

  useEffect(() => {
    if (messages.length > 0) {
      navigate("/interview", { replace: true });
    }
  }, [messages.length, navigate]);

  if (!candidate) {
    return null;
  }

  const handleBegin = async () => {
    const started = await startInterview();
    if (started) {
      navigate("/interview");
    }
  };

  return (
    <section className="container setup">
      <p className="eyebrow">INTERVIEW READY</p>
      <h2>Ready, {candidate.name.split(" ")[0]}?</h2>
      <p className="lead">We used this candidate’s progress to prepare a focused interview.</p>
      <div className="setup-card">
        <div>
          <small>CURRICULUM SIGNALS</small>
          <p>
            {candidate.completedCount} missions completed · {candidate.firstTryCount} first-try
            completions
          </p>
          <p>{candidate.commitDays} active commit days</p>
          <p>Focus area: {candidate.focus}</p>
        </div>
        <div>
          <small>INTERVIEW PLAN</small>
          <p>8 questions · 4+ curriculum days</p>
          <p>Adaptive follow-ups · final feedback</p>
        </div>
      </div>
      {error && <ErrorBanner message={error} onRetry={retry} />}
      <button type="button" className="primary" onClick={handleBegin} disabled={isLoading}>
        {isLoading ? "Preparing personalized interview…" : "Begin interview →"}
      </button>
    </section>
  );
}
