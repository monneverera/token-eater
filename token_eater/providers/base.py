"""Abstract provider interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class ProviderResponse:
    """Standardized response from any LLM provider."""

    text: str
    input_tokens: int
    output_tokens: int
    latency_ms: float
    raw: dict[str, Any] | None = None


class BaseProvider(ABC):
    """Abstract base for LLM provider adapters."""

    def __init__(self, api_key: str, base_url: str | None = None) -> None:
        self.api_key = api_key
        self.base_url = base_url

    @abstractmethod
    async def complete(self, prompt: str, max_tokens: int = 256) -> ProviderResponse:
        """Send a completion request and return standardized response."""
        ...

    @abstractmethod
    def name(self) -> str:
        """Provider identifier string."""
        ...

    @property
    @abstractmethod
    def pricing(self) -> tuple[float, float]:
        """Return (input_price_per_mtok, output_price_per_mtok)."""
        ...
