import rawCandidates from "./candidates.json";
import curriculum from "./curriculum.json";
import type { Candidate } from "../types";

type Mission = { day: number; title?: string; passed?: boolean; skipped?: boolean; attempts?: number };
type SourceCandidate = {
  member: { id: string; name: string; jobRole: string; yearsExperience: number; education: string };
  missions: Mission[];
  signals: { commitDays: number; missionsCompleted: number; missionsFirstTry: number };
};

const curriculumTitleByDay = new Map(
  curriculum.days.map((day) => [day.day, day.title]),
);

const titleFor = (mission: Mission) => mission.title ?? curriculumTitleByDay.get(mission.day) ?? `Curriculum day ${mission.day}`;

function toCandidate(source: SourceCandidate): Candidate {
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
    focus: skipped ? `Review ${titleFor(skipped)}` : difficult ? `Deepen ${titleFor(difficult)}` : "Explore advanced system trade-offs",
  };
}

export const candidates: Candidate[] = (rawCandidates.candidates as SourceCandidate[]).map(toCandidate);
