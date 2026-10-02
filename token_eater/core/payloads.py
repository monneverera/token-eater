"""Token payload generators for benchmarking."""

from __future__ import annotations

import random
import string


def generate_random_text(target_tokens: int, chars_per_token: float = 4.0) -> str:
    """Generate random text approximating the target token count."""
    target_chars = int(target_tokens * chars_per_token)
    words = []
    current_chars = 0
    while current_chars < target_chars:
        word_len = random.randint(1, 12)
        word = "".join(random.choices(string.ascii_lowercase, k=word_len))
        words.append(word)
        current_chars += word_len + 1  # +1 for space
    return " ".join(words)


def generate_progressive_payloads(
    max_tokens: int,
    steps: int = 10,
) -> list[str]:
    """Generate payloads of increasing size up to max_tokens."""
    step_size = max(1, max_tokens // steps)
    return [
        generate_random_text(step_size * (i + 1))
        for i in range(steps)
    ]


def generate_structured_payload(target_tokens: int) -> str:
    """Generate semi-structured text (JSON-like) for realistic benchmarking."""
    entries = []
    tokens_per_entry = 20  # rough estimate
    num_entries = max(1, target_tokens // tokens_per_entry)
    for i in range(num_entries):
        entry = (
            f'{{"id": {i}, '
            f'"name": "item_{i}", '
            f'"value": {random.uniform(0, 1000):.2f}, '
            f'"active": {random.choice(["true", "false"])}}}'
        )
        entries.append(entry)
    return "[" + ",\n".join(entries) + "]"
