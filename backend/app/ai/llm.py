from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Any, TypeVar

from pydantic import BaseModel, ValidationError

from app.config import Settings, get_settings

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class LLMError(Exception):
    """Raised when the LLM service fails or returns invalid structured output."""


class LLMService(ABC):
    @abstractmethod
    def generate_structured(
        self,
        prompt: str,
        schema: type[T],
        *,
        system_instruction: str | None = None,
    ) -> T:
        """Generate and validate structured output against a Pydantic schema."""


def _clean_schema_for_gemini(data: Any) -> Any:
    """Recursively remove keys unsupported by Gemini REST API schema validation."""
    if isinstance(data, dict):
        cleaned = {}
        for key, value in data.items():
            if key in ("additionalProperties", "additional_properties"):
                continue
            cleaned[key] = _clean_schema_for_gemini(value)
        return cleaned
    elif isinstance(data, list):
        return [_clean_schema_for_gemini(item) for item in data]
    return data


class GeminiLLMService(LLMService):
    def __init__(self, settings: Settings | None = None) -> None:
        self._settings = settings or get_settings()
        if not self._settings.gemini_api_key:
            raise LLMError("GEMINI_API_KEY is not configured.")

    def generate_structured(
        self,
        prompt: str,
        schema: type[T],
        *,
        system_instruction: str | None = None,
    ) -> T:
        try:
            from google import genai
            from google.genai import types
        except ImportError as exc:
            raise LLMError("google-genai package is not installed.") from exc

        client = genai.Client(api_key=self._settings.gemini_api_key)
        cleaned_schema = _clean_schema_for_gemini(schema.model_json_schema())

        config_kwargs: dict = {
            "response_mime_type": "application/json",
            "response_schema": cleaned_schema,
            "temperature": 0.4,
            "max_output_tokens": 1024,
        }
        if hasattr(types, "ThinkingConfig"):
            config_kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=512)
        if system_instruction:
            config_kwargs["system_instruction"] = system_instruction

        try:
            response = client.models.generate_content(
                model=self._settings.ai_model,
                contents=prompt,
                config=types.GenerateContentConfig(**config_kwargs),
            )
        except Exception as exc:
            logger.exception("Gemini API call failed")
            raise LLMError("Gemini API call failed.") from exc

        finish_reason = None
        if getattr(response, "candidates", None) and len(response.candidates) > 0:
            finish_reason = getattr(response.candidates[0], "finish_reason", None)

        usage = getattr(response, "usage_metadata", None)
        prompt_tokens = getattr(usage, "prompt_token_count", None) if usage else None
        output_tokens = getattr(usage, "candidates_token_count", None) if usage else None
        thoughts_tokens = getattr(usage, "thoughts_token_count", None) if usage else None
        total_tokens = getattr(usage, "total_token_count", None) if usage else None

        logger.info(
            "Gemini structured response diagnostic: model=%s, finish_reason=%s, "
            "prompt_tokens=%s, output_tokens=%s, thoughts_tokens=%s, total_tokens=%s",
            self._settings.ai_model,
            finish_reason,
            prompt_tokens,
            output_tokens,
            thoughts_tokens,
            total_tokens,
        )

        parsed = getattr(response, "parsed", None)
        if parsed is not None:
            if isinstance(parsed, schema):
                return parsed
            try:
                return schema.model_validate(parsed)
            except ValidationError as exc:
                logger.warning("Parsed response validation failed: %s", exc)

        text = getattr(response, "text", None)
        if text:
            try:
                return schema.model_validate_json(text)
            except ValidationError as exc:
                raise LLMError("Gemini structured output failed validation.") from exc

        raise LLMError("Gemini returned no valid structured output.")


class FakeLLMService(LLMService):
    """Deterministic LLM stub for tests — maps schema types to canned responses."""

    def __init__(
        self,
        responses: dict[type[BaseModel], BaseModel] | None = None,
        *,
        on_call: list[tuple[type[BaseModel], str]] | None = None,
    ) -> None:
        self._responses = responses or {}
        self._on_call: list[tuple[type[BaseModel], str]] = on_call if on_call is not None else []

    @property
    def calls(self) -> list[tuple[type[BaseModel], str]]:
        return list(self._on_call)

    def generate_structured(
        self,
        prompt: str,
        schema: type[T],
        *,
        system_instruction: str | None = None,
    ) -> T:
        self._on_call.append((schema, prompt))
        response = self._responses.get(schema)
        if response is None:
            raise LLMError(f"No fake response registered for schema {schema.__name__}.")
        if not isinstance(response, schema):
            return schema.model_validate(response.model_dump())
        return response


def get_llm_service(settings: Settings | None = None) -> LLMService:
    settings = settings or get_settings()
    if settings.ai_enabled and settings.gemini_api_key:
        return GeminiLLMService(settings)
    raise LLMError("AI is not enabled or GEMINI_API_KEY is missing.")


def generate_with_retry(
    llm: LLMService,
    prompt: str,
    schema: type[T],
    *,
    system_instruction: str | None = None,
    retries: int = 1,
) -> T:
    last_error: Exception | None = None
    attempts = retries + 1
    for _ in range(attempts):
        try:
            return llm.generate_structured(
                prompt,
                schema,
                system_instruction=system_instruction,
            )
        except (LLMError, ValidationError) as exc:
            last_error = exc
            logger.warning("Structured generation attempt failed: %s", exc)
    raise LLMError("Structured generation failed after retries.") from last_error
