import { Outlet, useNavigate } from "react-router-dom";
import { useInterviewContext } from "../context/InterviewContext";

export default function MainLayout() {
  const navigate = useNavigate();
  const { resetInterview } = useInterviewContext();

  const handleRestart = () => {
    resetInterview();
    navigate("/");
  };

  return (
    <main>
      <header className="nav">
        <button type="button" className="brand" onClick={handleRestart}>
          <span>KY² Interview Agent</span>
        </button>
        <span className="nav-note">Adaptive technical interviews</span>
      </header>
      <Outlet />
    </main>
  );
}
