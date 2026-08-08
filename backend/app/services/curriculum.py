from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class CurriculumModule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    n: int
    title: str
    days: list[int] = Field(min_length=1)


class CurriculumDay(BaseModel):
    model_config = ConfigDict(extra="forbid")

    day: int
    title: str
    type: str
    tools: list[str]
    objectives: list[str]


class Curriculum(BaseModel):
    model_config = ConfigDict(extra="forbid")

    cohort: str
    modules: list[CurriculumModule]
    days: list[CurriculumDay]


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "curriculum.json"


class CurriculumLoadError(RuntimeError):
    """Raised when curriculum.json cannot be loaded or validated."""


@lru_cache(maxsize=1)
def load_curriculum() -> Curriculum:
    try:
        raw: dict[str, Any] = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CurriculumLoadError(f"Curriculum file not found: {DATA_PATH}") from exc
    except json.JSONDecodeError as exc:
        raise CurriculumLoadError("Curriculum file contains invalid JSON.") from exc

    return Curriculum.model_validate(raw)


def get_day(day_number: int) -> CurriculumDay | None:
    for day in load_curriculum().days:
        if day.day == day_number:
            return day
    return None


def get_all_days() -> list[CurriculumDay]:
    return load_curriculum().days


def get_module_for_day(day_number: int) -> CurriculumModule | None:
    for module in load_curriculum().modules:
        start, end = module.days
        if start <= day_number <= end:
            return module
    return None


def title_for_day(day_number: int) -> str:
    day = get_day(day_number)
    return day.title if day else f"Curriculum day {day_number}"
