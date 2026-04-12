"""``tikhub`` console script.

The CLI is intentionally minimal: it covers the small set of commands a
human might run from a terminal during ad-hoc data extraction or
debugging. Anything more complex belongs in a Python script that imports
the SDK directly.
"""

from __future__ import annotations

import json
import sys
from typing import Any, Callable

try:
    import typer
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "The CLI requires the 'cli' extra. Install with: pip install 'tikhub[cli]'"
    ) from exc

from tikhub import TikHub, TikHubError, __version__

app = typer.Typer(
    name="tikhub",
    help="TikHub - Python SDK CLI for the TikHub social-media data API.",
    add_completion=False,
)
user_app = typer.Typer(name="user", help="TikHub account introspection.")
app.add_typer(user_app, name="user")


def _print_json(value: Any) -> None:
    typer.echo(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True))


def _make_client() -> TikHub:
    try:
        return TikHub()
    except TikHubError as exc:
        typer.echo(f"error: {exc}", err=True)
        raise typer.Exit(code=2) from exc


def _run(callable_: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    try:
        return callable_(*args, **kwargs)
    except TikHubError as exc:
        typer.echo(f"error: {exc}", err=True)
        raise typer.Exit(code=1) from exc


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"tikhub {__version__}")
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def _root(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "--version",
        "-V",
        is_eager=True,
        callback=_version_callback,
        help="Print the SDK version and exit.",
    ),
) -> None:
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()


@app.command()
def health() -> None:
    """Verify the TikHub API is reachable and your key is valid."""
    with _make_client() as client:
        result = _run(client.health_check.check)
    _print_json(result)


@app.command()
def fetch(
    url: str = typer.Argument(..., help="Share URL of any supported video platform."),
) -> None:
    """Universal video URL parser via /api/v1/hybrid/video_data."""
    with _make_client() as client:
        result = _run(client.hybrid_parsing.video_data, url=url)
    _print_json(result)


@user_app.command("info")
def user_info() -> None:
    """Show TikHub account info (plan, quota, etc.)."""
    with _make_client() as client:
        result = _run(client.tikhub_user.get_user_info)
    _print_json(result)


@user_app.command("usage")
def user_usage() -> None:
    """Show today's API usage."""
    with _make_client() as client:
        result = _run(client.tikhub_user.get_user_daily_usage)
    _print_json(result)


def main() -> None:  # pragma: no cover - thin wrapper
    """Entry point referenced by ``[project.scripts]`` in ``pyproject.toml``."""
    try:
        app()
    except KeyboardInterrupt:
        typer.echo("aborted", err=True)
        sys.exit(130)
