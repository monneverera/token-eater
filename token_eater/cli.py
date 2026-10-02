"""CLI entrypoint for Token Eater."""

from __future__ import annotations

from enum import Enum
from typing import Optional

import typer
from rich.console import Console

app = typer.Typer(
    name="token-eater",
    help="🦷 Stress-test & benchmark LLM token throughput, context limits, and rate profiles.",
    no_args_is_help=True,
)
console = Console()


class OutputFormat(str, Enum):
    terminal = "terminal"
    json = "json"
    csv = "csv"
    html = "html"


@app.command()
def bench(
    provider: str = typer.Option(..., help="Provider name (openai, anthropic, google, custom)"),
    model: str = typer.Option(..., help="Model identifier"),
    max_tokens: int = typer.Option(4096, help="Maximum tokens to test"),
    steps: int = typer.Option(10, help="Number of incremental payload steps"),
    output: OutputFormat = typer.Option(OutputFormat.terminal, "--format", help="Output format"),
    config: Optional[str] = typer.Option(None, help="Path to config TOML"),
) -> None:
    """Benchmark token throughput across payload sizes."""
    console.print(f"[bold green]🦷 Benchmarking[/] {provider}/{model}")
    console.print(f"   Max tokens: {max_tokens:,} | Steps: {steps} | Format: {output.value}")
    # TODO: wire up core.runner
    console.print("[yellow]⚠ Not yet implemented — scaffolding only.[/]")


@app.command()
def stress(
    provider: str = typer.Option(..., help="Provider name"),
    model: str = typer.Option(..., help="Model identifier"),
    fill_strategy: str = typer.Option("progressive", help="Context fill strategy (progressive, random, structured)"),
    output: OutputFormat = typer.Option(OutputFormat.terminal, "--format", help="Output format"),
) -> None:
    """Stress-test context window saturation."""
    console.print(f"[bold red]🦷 Stress testing[/] {provider}/{model}")
    console.print(f"   Strategy: {fill_strategy}")
    console.print("[yellow]⚠ Not yet implemented — scaffolding only.[/]")


@app.command()
def ratelimit(
    provider: str = typer.Option(..., help="Provider name"),
    model: str = typer.Option(..., help="Model identifier"),
    burst: int = typer.Option(20, help="Number of concurrent requests in burst"),
    cooldown: int = typer.Option(60, help="Cooldown period in seconds"),
    output: OutputFormat = typer.Option(OutputFormat.terminal, "--format", help="Output format"),
) -> None:
    """Profile API rate limits and recovery patterns."""
    console.print(f"[bold cyan]🦷 Rate limit profiling[/] {provider}/{model}")
    console.print(f"   Burst: {burst} | Cooldown: {cooldown}s")
    console.print("[yellow]⚠ Not yet implemented — scaffolding only.[/]")


@app.command()
def compare(
    providers: str = typer.Option(..., help="Comma-separated provider names"),
    models: str = typer.Option(..., help="Comma-separated model identifiers (matching providers)"),
    output: OutputFormat = typer.Option(OutputFormat.terminal, "--format", help="Output format"),
) -> None:
    """Compare providers side-by-side."""
    provider_list = [p.strip() for p in providers.split(",")]
    model_list = [m.strip() for m in models.split(",")]
    console.print("[bold magenta]🦷 Comparative benchmark[/]")
    for p, m in zip(provider_list, model_list):
        console.print(f"   • {p}/{m}")
    console.print("[yellow]⚠ Not yet implemented — scaffolding only.[/]")


if __name__ == "__main__":
    app()
