from __future__ import annotations

from app.schemas.interview import Candidate, CandidateMission


class CandidateValidationError(ValueError):
    """Raised when the raw candidate payload fails semantic validation."""


def validate_candidate(candidate: Candidate) -> Candidate:
    """Validate the raw candidate object and return it unchanged."""
    if not candidate.missions:
        raise CandidateValidationError("Candidate must include at least one mission.")

    seen_days: set[int] = set()
    for mission in candidate.missions:
        if mission.day in seen_days:
            raise CandidateValidationError(
                f"Duplicate mission day {mission.day} in candidate missions."
            )
        seen_days.add(mission.day)

        if mission.skipped and mission.passed:
            raise CandidateValidationError(
                f"Mission on day {mission.day} cannot be both skipped and passed."
            )

    return candidate


def get_candidate_name(candidate: Candidate) -> str:
    return candidate.member.name


def get_first_name(candidate: Candidate) -> str:
    return candidate.member.name.split()[0]


def get_skipped_missions(candidate: Candidate) -> list[CandidateMission]:
    return [mission for mission in candidate.missions if mission.skipped]


def get_difficult_missions(candidate: Candidate) -> list[CandidateMission]:
    return sorted(
        [
            mission
            for mission in candidate.missions
            if not mission.skipped and (mission.attempts or 0) > 1
        ],
        key=lambda mission: mission.attempts or 0,
        reverse=True,
    )


def get_first_try_missions(candidate: Candidate) -> list[CandidateMission]:
    return [
        mission
        for mission in candidate.missions
        if mission.passed and (mission.attempts or 0) == 1
    ]


def get_completed_days(candidate: Candidate) -> list[int]:
    return sorted(
        mission.day for mission in candidate.missions if mission.passed and not mission.skipped
    )


def get_mission_days(candidate: Candidate) -> list[int]:
    return sorted(mission.day for mission in candidate.missions)
