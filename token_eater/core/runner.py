"""Benchmark orchestrator — runs test sequences and collects metrics."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class BenchmarkResult:
    """Single benchmark measurement."""

    provider: str
    model: str
    input_tokens: int
    output_tokens: int
    latency_ms: float
    tokens_per_second: float
    cost_usd: float | None = None
    error: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class BenchmarkSuite:
    """Collection of benchmark results for a run."""

    results: list[BenchmarkResult] = field(default_factory=list)

    @property
    def avg_throughput(self) -> float:
        successful = [r for r in self.results if r.error is None]
        if not successful:
            return 0.0
        return sum(r.tokens_per_second for r in successful) / len(successful)

    @property
    def total_cost(self) -> float:
        return sum(r.cost_usd for r in self.results if r.cost_usd is not None)

    @property
    def error_rate(self) -> float:
        if not self.results:
            return 0.0
        errors = sum(1 for r in self.results if r.error is not None)
        return errors / len(self.results)
