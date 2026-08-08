import type { CandidateViewModel } from "../../types";

type CandidateCardProps = {
  candidate: CandidateViewModel;
  onSelect: (candidate: CandidateViewModel) => void;
};

export function CandidateCard({ candidate, onSelect }: CandidateCardProps) {
  return (
    <button type="button" className="candidate" onClick={() => onSelect(candidate)}>
      <div className="avatar">{candidate.name[0]}</div>
      <h3>{candidate.name}</h3>
      <p>
        {candidate.role} · {candidate.yearsExperience} years experience
      </p>
      <hr />
      <small>STRENGTH</small>
      <strong>{candidate.strength}</strong>
      <small>FOCUS AREA</small>
      <strong>{candidate.focus}</strong>
      <span>Prepare interview →</span>
    </button>
  );
}
