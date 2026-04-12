# CLI

The `tikhub` package ships an optional command-line wrapper for ad-hoc data extraction. Install it with the `cli` extra:

```bash
pip install "tikhub[cli]"
```

This adds [`typer`](https://typer.tiangolo.com) as a dependency and registers a `tikhub` console script.

## Authenticate

Set `TIKHUB_API_KEY` in your environment so you don't have to pass it on every call:

```bash
export TIKHUB_API_KEY="YOUR_API_KEY"
```

## Commands

### `tikhub health`

Verifies your API key and the TikHub API is reachable.

```bash
tikhub health
```

### `tikhub fetch <url>`

Universal video URL parser — pass a Douyin / TikTok / Bilibili / Xiaohongshu / etc. share URL and the SDK uses the `hybrid_parsing` endpoint to figure out the platform and pull the data.

```bash
tikhub fetch https://v.douyin.com/abc/
tikhub fetch https://www.tiktok.com/@user/video/7251234567890
```

### `tikhub user info`

Show your TikHub account info — quota, plan, etc.

```bash
tikhub user info
```

### `tikhub user usage`

Show your daily request usage.

```bash
tikhub user usage
```

## Output

Every command prints JSON to stdout. Pipe it to `jq`, `python -m json.tool`, or your favourite formatter:

```bash
tikhub health | jq .
tikhub fetch https://v.douyin.com/abc/ | jq '.aweme_detail.desc'
```

## Help

```bash
tikhub --help
tikhub user --help
tikhub fetch --help
```

## Why so few commands?

The CLI deliberately stays small. The Python SDK is the primary interface — the CLI is for `curl`-style ad-hoc fetches. If you need to script a complex pipeline, write a Python script importing `tikhub` directly.
