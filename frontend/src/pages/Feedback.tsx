import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { FeedbackResults } from "../components/feedback/FeedbackResults";
import { useInterviewContext } from "../context/InterviewContext";

export default function Feedback() {
  const navigate = useNavigate();
  const { candidate, feedback, demoPresentation, resetInterview } = useInterviewContext();

  useEffect(() => {
    if (!candidate) {
      navigate("/candidates", { replace: true });
      return;
    }
    if (!feedback) {
      navigate("/interview", { replace: true });
    }
  }, [candidate, feedback, navigate]);

  if (!candidate || !feedback) {
    return null;
  }

  const handleRestart = () => {
    resetInterview();
    navigate("/");
  };

  return (
    <FeedbackResults
      candidateName={candidate.name}
      feedback={feedback}
      demoPresentation={demoPresentation}
      onRestart={handleRestart}
    />
  );
}
