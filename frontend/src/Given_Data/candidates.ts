import rawCandidates from "./candidates.json";
import curriculum from "./curriculum.json";
import type { CandidateViewModel, RawCandidate } from "../types";

type Mission = {
  day: number;
  title?: string;
  passed?: boolean;
  skipped?: boolean;
  attempts?: number;
};

const curriculumTitleByDay = new Map(
  curriculum.days.map((day) => [day.day, day.title]),
);

const titleFor = (mission: Mission) =>
  mission.title ?? curriculumTitleByDay.get(mission.day) ?? `Curriculum day ${mission.day}`;

function toViewModel(source: RawCandidate): CandidateViewModel {
  const completed = source.missions.filter((mission) => mission.passed);
  const skipped = source.missions.find((mission) => mission.skipped);
  const difficult = [...source.missions]
    .filter((mission) => !mission.skipped && (mission.attempts ?? 0) > 1)
    .sort((left, right) => (right.attempts ?? 0) - (left.attempts ?? 0))[0];
  const strongest = completed.find((mission) => mission.attempts === 1) ?? completed[0];

  return {
    id: source.member.id,
    name: source.member.name,
    role: source.member.jobRole,
    yearsExperience: source.member.yearsExperience,
    education: source.member.education,
    completedDays: completed.map((mission) => mission.day),
    completedCount: source.signals.missionsCompleted,
    firstTryCount: source.signals.missionsFirstTry,
    commitDays: source.signals.commitDays,
    strength: strongest ? `Strong in ${titleFor(strongest)}` : "Learning foundations",
    focus: skipped
      ? `Review ${titleFor(skipped)}`
      : difficult
        ? `Deepen ${titleFor(difficult)}`
        : "Explore advanced system trade-offs",
  };
}

export const rawCandidateList: RawCandidate[] = rawCandidates.candidates as RawCandidate[];

export const candidates: CandidateViewModel[] = rawCandidateList.map(toViewModel);

export function getRawCandidateById(id: string): RawCandidate | undefined {
  return rawCandidateList.find((candidate) => candidate.member.id === id);
}

export function getCandidateViewModelById(id: string): CandidateViewModel | undefined {
  return candidates.find((candidate) => candidate.id === id);
}

export function getCandidatePair(id: string): {
  viewModel: CandidateViewModel;
  raw: RawCandidate;
} | null {
  const raw = getRawCandidateById(id);
  const viewModel = getCandidateViewModelById(id);
  if (!raw || !viewModel) {
    return null;
  }
  return { viewModel, raw };
}
