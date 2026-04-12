"""Constructor and configuration tests for ``TikHub`` / ``AsyncTikHub``."""

from __future__ import annotations

import pytest

from tikhub import AsyncTikHub, TikHub, TikHubConfigError


def test_explicit_api_key():
    client = TikHub(api_key="sk-test")
    assert client._api_key == "sk-test"
    assert client._base_url == "https://api.tikhub.io"
    client.close()


def test_api_key_from_env(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("TIKHUB_API_KEY", "sk-from-env")
    client = TikHub()
    assert client._api_key == "sk-from-env"
    client.close()


def test_missing_api_key_raises():
    with pytest.raises(TikHubConfigError, match="No API key provided"):
        TikHub()


def test_explicit_overrides_env(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("TIKHUB_API_KEY", "sk-env")
    client = TikHub(api_key="sk-explicit")
    assert client._api_key == "sk-explicit"
    client.close()


def test_base_url_default():
    client = TikHub(api_key="sk-test")
    assert client._base_url == "https://api.tikhub.io"
    client.close()


def test_base_url_override_strips_trailing_slash():
    client = TikHub(api_key="sk-test", base_url="https://mirror.example.com/")
    assert client._base_url == "https://mirror.example.com"
    client.close()


def test_context_manager_closes_client():
    with TikHub(api_key="sk-test") as client:
        assert not client._client.is_closed
    assert client._client.is_closed


def test_repr_does_not_leak_key():
    client = TikHub(api_key="sk-secret-do-not-leak")
    rendered = repr(client)
    assert "sk-secret-do-not-leak" not in rendered
    assert "https://api.tikhub.io" in rendered
    client.close()


async def test_async_repr_does_not_leak_key():
    client = AsyncTikHub(api_key="sk-secret-do-not-leak")
    rendered = repr(client)
    assert "sk-secret-do-not-leak" not in rendered
    await client.aclose()


async def test_async_context_manager_closes_client():
    async with AsyncTikHub(api_key="sk-test") as client:
        assert not client._client.is_closed
    assert client._client.is_closed
