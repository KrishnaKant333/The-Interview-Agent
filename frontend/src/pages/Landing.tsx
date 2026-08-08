import { useNavigate } from "react-router-dom";
import { Feature } from "../components/common/Feature";

export default function Landing() {
  const navigate = useNavigate();

  return (
    <section className="hero">
      <p className="eyebrow">PERSONALIZED AI INTERVIEWER</p>
      <h1>
        Your learning journey.
        <br />
        <em>Your interview.</em>
      </h1>
      <p className="lead">
        A technical interview that adapts to what you have learned, where you struggled, and how
        you answer.
      </p>
      <button type="button" className="primary" onClick={() => navigate("/candidates")}>
        Start interview <b>→</b>
      </button>
      <div className="feature-grid">
        <Feature title="Personalized" text="Built around curriculum progress" />
        <Feature title="Adaptive" text="Follow-ups shift with each answer" />
        <Feature title="Actionable" text="Feedback points to what to learn next" />
      </div>
    </section>
  );
}
