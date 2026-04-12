"""Modern Python SDK for the TikHub social-media data API.

Quick start::

    from tikhub import TikHub

    with TikHub(api_key="YOUR_API_KEY") as client:
        video = client.douyin_web.fetch_one_video(aweme_id="...")

"""

from __future__ import annotations

from tikhub._errors import (
    TikHubAuthError,
    TikHubBadRequestError,
    TikHubConfigError,
    TikHubConnectionError,
    TikHubError,
    TikHubFeatureRemovedError,
    TikHubHTTPError,
    TikHubNotFoundError,
    TikHubPermissionError,
    TikHubProxyError,
    TikHubRateLimitError,
    TikHubServerError,
    TikHubTimeoutError,
    TikHubUpstreamError,
    TikHubValidationError,
)
from tikhub._pagination import (
    CursorPaginator,
    OffsetPaginator,
    Page,
    PagePaginator,
)
from tikhub._version import __version__
from tikhub.async_client import AsyncTikHub
from tikhub.client import TikHub

__all__ = [
    "AsyncTikHub",
    # Pagination
    "CursorPaginator",
    "OffsetPaginator",
    "Page",
    "PagePaginator",
    # Clients
    "TikHub",
    "TikHubAuthError",
    "TikHubBadRequestError",
    "TikHubConfigError",
    "TikHubConnectionError",
    # Errors
    "TikHubError",
    "TikHubFeatureRemovedError",
    "TikHubHTTPError",
    "TikHubNotFoundError",
    "TikHubPermissionError",
    "TikHubProxyError",
    "TikHubRateLimitError",
    "TikHubServerError",
    "TikHubTimeoutError",
    "TikHubUpstreamError",
    "TikHubValidationError",
    # Metadata
    "__version__",
]
