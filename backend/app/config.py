from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache


from pathlib import Path

def _load_env_file() -> None:
    paths = [
        Path(__file__).resolve().parent.parent / ".env",
        Path(".env").resolve(),
    ]
    for p in paths:
        if p.exists():
            try:
                from dotenv import load_dotenv
                load_dotenv(p, override=False)
            except ImportError:
                pass
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    k = k.strip()
                    if k not in os.environ:
                        os.environ[k] = v.strip()
            break

_load_env_file()


def _env_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    gemini_api_key: str
    ai_model: str
    ai_enabled: bool


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings(
        gemini_api_key=os.getenv("GEMINI_API_KEY", "").strip(),
        ai_model=os.getenv("AI_MODEL", "gemini-3.5-flash").strip(),
        ai_enabled=_env_bool("AI_ENABLED", default=False),
    )
