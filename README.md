# 🦷 Token Eater

**A stress-testing & benchmarking toolkit for LLM token throughput, context window limits, and API rate analysis.**

> *How many tokens can your model chew before it chokes?*

---

## Overview

Token Eater is a developer-focused CLI tool designed to push Large Language Models to their limits. It systematically benchmarks:

- **Token throughput** — tokens/sec across varying payload sizes
- **Context window saturation** — graceful degradation as context fills up
- **Rate limit profiling** — burst capacity & recovery patterns
- **Cost estimation** — dollar-per-token analysis across providers

## Installation

```bash
pip install token-eater
```

Or from source:

```bash
git clone https://github.com/monneverera/token-eater.git
cd token-eater
pip install -e ".[dev]"
```

## Quick Start

```bash
# Benchmark OpenAI GPT-4o throughput
token-eater bench --provider openai --model gpt-4o --max-tokens 128000

# Stress-test context window
token-eater stress --provider anthropic --model claude-sonnet-4-20250514 --fill-strategy progressive

# Profile rate limits
token-eater ratelimit --provider openai --model gpt-4o-mini --burst 50 --cooldown 60

# Compare providers side-by-side
token-eater compare --providers openai,anthropic,google --models gpt-4o,claude-sonnet-4-20250514,gemini-2.0-flash
```

## Configuration

Create a `token-eater.toml` in your project root or `~/.config/token-eater/config.toml`:

```toml
[providers.openai]
api_key_env = "OPENAI_API_KEY"
base_url = "https://api.openai.com/v1"

[providers.anthropic]
api_key_env = "ANTHROPIC_API_KEY"
base_url = "https://api.anthropic.com"

[providers.google]
api_key_env = "GOOGLE_API_KEY"

[providers.custom]
api_key_env = "CUSTOM_API_KEY"
base_url = "http://localhost:11434/v1"  # e.g. Ollama
```

## Output

Token Eater generates structured reports in multiple formats:

| Format   | Flag             | Description                    |
|----------|------------------|--------------------------------|
| Terminal | *(default)*      | Rich tables & progress bars    |
| JSON     | `--format json`  | Machine-readable results       |
| CSV      | `--format csv`   | Spreadsheet-friendly           |
| HTML     | `--format html`  | Interactive charts (Plotly)     |

## Architecture

```
token_eater/
├── __init__.py
├── cli.py              # Typer CLI entrypoint
├── core/
│   ├── runner.py       # Benchmark orchestrator
│   ├── payloads.py     # Token payload generators
│   └── metrics.py      # Throughput & latency calculators
├── providers/
│   ├── base.py         # Abstract provider interface
│   ├── openai.py       # OpenAI adapter
│   ├── anthropic.py    # Anthropic adapter
│   └── google.py       # Google Gemini adapter
├── reporters/
│   ├── terminal.py     # Rich console output
│   ├── json_report.py  # JSON export
│   ├── csv_report.py   # CSV export
│   └── html_report.py  # Plotly HTML charts
└── utils/
    ├── config.py       # TOML config loader
    ├── tokenizer.py    # Token counting (tiktoken/sentencepiece)
    └── rate_limiter.py # Adaptive rate limiting
```

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Lint & format
ruff check . && ruff format .

# Type check
mypy token_eater/
```

## Authors

- **Remon** — [@monneverera](https://github.com/monneverera)
- **Orion** — AI Chief of Staff, Lumen Lab

## License

MIT — see [LICENSE](LICENSE) for details.

---

*Built with quiet intensity at [Lumen Lab](https://github.com/monneverera).*
