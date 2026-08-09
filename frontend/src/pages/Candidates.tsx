import { useNavigate } from "react-router-dom";
import { getCandidatePair } from "../Given_Data/candidates";
import { CandidateGrid } from "../components/candidate/CandidateGrid";
import { useInterviewContext } from "../context/InterviewContext";
import type { CandidateViewModel } from "../types";

export default function Candidates() {
  const navigate = useNavigate();
  const { selectCandidate } = useInterviewContext();

  const handleSelect = (candidate: CandidateViewModel) => {
    const pair = getCandidatePair(candidate.id);
    if (!pair) return;
    selectCandidate(pair.viewModel, pair.raw);
    navigate("/setup");
  };

  return (
    <section className="container">
      <p className="eyebrow">STEP 1 OF 2</p>
      <h2>Choose a candidate</h2>
      <p className="muted">Use the supplied learner data to shape the interview.</p>
      <CandidateGrid onSelect={handleSelect} />
    </section>
  );
}
