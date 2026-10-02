"""Throughput and latency metric calculators."""

from __future__ import annotations

import statistics
from dataclasses import dataclass


@dataclass
class LatencyStats:
    """Aggregated latency statistics."""

    mean_ms: float
    median_ms: float
    p95_ms: float
    p99_ms: float
    min_ms: float
    max_ms: float
    std_dev_ms: float

    @classmethod
    def from_samples(cls, samples_ms: list[float]) -> LatencyStats:
        if not samples_ms:
            return cls(0, 0, 0, 0, 0, 0, 0)
        sorted_s = sorted(samples_ms)
        n = len(sorted_s)
        return cls(
            mean_ms=statistics.mean(sorted_s),
            median_ms=statistics.median(sorted_s),
            p95_ms=sorted_s[int(n * 0.95)] if n > 1 else sorted_s[0],
            p99_ms=sorted_s[int(n * 0.99)] if n > 1 else sorted_s[0],
            min_ms=sorted_s[0],
            max_ms=sorted_s[-1],
            std_dev_ms=statistics.stdev(sorted_s) if n > 1 else 0.0,
        )


def tokens_per_second(token_count: int, latency_ms: float) -> float:
    """Calculate tokens per second from count and latency."""
    if latency_ms <= 0:
        return 0.0
    return token_count / (latency_ms / 1000.0)


def estimate_cost(
    input_tokens: int,
    output_tokens: int,
    input_price_per_mtok: float,
    output_price_per_mtok: float,
) -> float:
    """Estimate API call cost in USD."""
    input_cost = (input_tokens / 1_000_000) * input_price_per_mtok
    output_cost = (output_tokens / 1_000_000) * output_price_per_mtok
    return input_cost + output_cost
