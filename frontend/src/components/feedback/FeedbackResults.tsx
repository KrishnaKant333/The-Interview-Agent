import type { DemoFeedbackPresentation, InterviewFeedback } from "../../types";
import { SkillBreakdown } from "./SkillBreakdown";

type FeedbackResultsProps = {
  candidateName: string;
  feedback: InterviewFeedback;
  demoPresentation: DemoFeedbackPresentation | null;
  onRestart: () => void;
};

export function FeedbackResults({
  candidateName,
  feedback,
  demoPresentation,
  onRestart,
}: FeedbackResultsProps) {
  return (
    <section className="container results">
      <p className="eyebrow">INTERVIEW COMPLETE</p>
      <h2>Great work, {candidateName.split(" ")[0]}.</h2>
      <p className="lead">{feedback.summary}</p>

      {demoPresentation && (
        <div className="overall">
          <b>{demoPresentation.overall}</b>
          <span>/ 100 overall performance (demo)</span>
        </div>
      )}

      <div className="result-grid">
        {demoPresentation && <SkillBreakdown presentation={demoPresentation} />}
        <div className="panel">
          <h3>Strengths</h3>
          {feedback.strengths.map((item) => (
            <p className="positive" key={item}>
              ✓ {item}
            </p>
          ))}
          <h3>Improve next</h3>
          {feedback.gaps.map((item) => (
            <p className="improve" key={item}>
              → {item}
            </p>
          ))}
        </div>
      </div>

      <div className="panel recommendations">
        <small>RECOMMENDED LEARNING</small>
        {feedback.next.map((item) => (
          <p key={item}>{item}</p>
        ))}
      </div>

      <button type="button" className="primary" onClick={onRestart}>
        Start another interview →
      </button>
    </section>
  );
}
