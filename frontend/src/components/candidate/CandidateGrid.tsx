import { candidates } from "../../Given_Data/candidates";
import type { CandidateViewModel } from "../../types";
import { CandidateCard } from "./CandidateCard";

type CandidateGridProps = {
  onSelect: (candidate: CandidateViewModel) => void;
};

export function CandidateGrid({ onSelect }: CandidateGridProps) {
  return (
    <div className="candidate-grid">
      {candidates.map((candidate) => (
        <CandidateCard key={candidate.id} candidate={candidate} onSelect={onSelect} />
      ))}
    </div>
  );
}
