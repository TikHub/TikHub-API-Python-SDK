"""Tests for the optional ``tikhub`` CLI.

The CLI is a thin typer wrapper around the SDK. These tests use typer's
``CliRunner`` plus ``httpx.MockTransport`` to verify each command emits
the right outgoing request and renders the response as JSON without
hitting the network.
"""

from __future__ import annotations

import json

import httpx
import pytest

typer = pytest.importorskip("typer")
from typer.testing import CliRunner  # noqa: E402

from tikhub.cli.main import app  # noqa: E402

runner = CliRunner()


def _set_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TIKHUB_API_KEY", "sk-test")


def _patch_client(monkeypatch: pytest.MonkeyPatch, handler):
    """Replace the TikHub constructor used by the CLI with one that wires
    a mock httpx transport in front of every request.
    """
    import tikhub.cli.main as cli_main

    real_ctor = cli_main.TikHub

    def factory():
        return real_ctor(transport=httpx.MockTransport(handler))

    monkeypatch.setattr(cli_main, "TikHub", factory)


# ---------------------------------------------------------------------------
# Top-level
# ---------------------------------------------------------------------------


def test_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert result.stdout.startswith("tikhub ")


def test_no_args_prints_help():
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    assert "Usage:" in result.stdout
    assert "health" in result.stdout
    assert "fetch" in result.stdout
    assert "user" in result.stdout


# ---------------------------------------------------------------------------
# health
# ---------------------------------------------------------------------------


def test_health_success(monkeypatch: pytest.MonkeyPatch):
    _set_key(monkeypatch)
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"code": 200, "data": {"status": "ok"}})

    _patch_client(monkeypatch, handler)
    result = runner.invoke(app, ["health"])
    assert result.exit_code == 0
    assert len(captured) == 1
    assert captured[0].method == "GET"
    assert captured[0].url.path == "/api/v1/health/check"
    body = json.loads(result.stdout)
    assert body == {"code": 200, "data": {"status": "ok"}}


# ---------------------------------------------------------------------------
# fetch
# ---------------------------------------------------------------------------


def test_fetch_passes_url_param(monkeypatch: pytest.MonkeyPatch):
    _set_key(monkeypatch)
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"platform": "douyin", "ok": True})

    _patch_client(monkeypatch, handler)
    result = runner.invoke(app, ["fetch", "https://v.douyin.com/abc/"])
    assert result.exit_code == 0
    assert len(captured) == 1
    assert captured[0].url.path == "/api/v1/hybrid/video_data"
    assert captured[0].url.params["url"] == "https://v.douyin.com/abc/"


# ---------------------------------------------------------------------------
# user info / usage
# ---------------------------------------------------------------------------


def test_user_info(monkeypatch: pytest.MonkeyPatch):
    _set_key(monkeypatch)
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"plan": "pro", "quota": 100000})

    _patch_client(monkeypatch, handler)
    result = runner.invoke(app, ["user", "info"])
    assert result.exit_code == 0
    assert captured[0].url.path == "/api/v1/tikhub/user/get_user_info"
    body = json.loads(result.stdout)
    assert body["plan"] == "pro"


def test_user_usage(monkeypatch: pytest.MonkeyPatch):
    _set_key(monkeypatch)
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"used": 42})

    _patch_client(monkeypatch, handler)
    result = runner.invoke(app, ["user", "usage"])
    assert result.exit_code == 0
    assert captured[0].url.path == "/api/v1/tikhub/user/get_user_daily_usage"
    body = json.loads(result.stdout)
    assert body["used"] == 42


# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------


def test_health_no_api_key():
    """Without $TIKHUB_API_KEY the CLI exits cleanly with an error message."""
    result = runner.invoke(app, ["health"])
    assert result.exit_code == 2
    # Confirm it's the SDK config error, not a typer crash.
    assert "API key" in result.stderr or "API key" in result.stdout


def test_health_upstream_error(monkeypatch: pytest.MonkeyPatch):
    _set_key(monkeypatch)

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(500, json={"error": "internal"})

    # Patch the factory and disable retries so the test runs fast.
    import tikhub.cli.main as cli_main

    real_ctor = cli_main.TikHub
    monkeypatch.setattr(
        cli_main,
        "TikHub",
        lambda: real_ctor(
            transport=httpx.MockTransport(handler),
            max_retries=0,
        ),
    )
    result = runner.invoke(app, ["health"])
    assert result.exit_code == 1
    assert "500" in (result.stderr + result.stdout)
