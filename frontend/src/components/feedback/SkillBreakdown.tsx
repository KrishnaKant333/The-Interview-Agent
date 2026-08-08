import type { DemoFeedbackPresentation } from "../../types";

const scoreWidth = (value: number) => ({ width: `${value}%` });

type SkillBreakdownProps = {
  presentation: DemoFeedbackPresentation;
};

export function SkillBreakdown({ presentation }: SkillBreakdownProps) {
  return (
    <div className="panel">
      <h3>Skill breakdown</h3>
      <p className="demo-note">Demo visualization — not returned by the API.</p>
      {presentation.skills.map((skill) => (
        <div className="skill" key={skill.label}>
          <span>{skill.label}</span>
          <b>{skill.score}%</b>
          <div className="bar">
            <i style={scoreWidth(skill.score)} />
          </div>
        </div>
      ))}
    </div>
  );
}
