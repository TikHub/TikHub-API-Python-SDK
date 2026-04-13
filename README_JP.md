# TikHub API Python SDK

<p align="center">
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/stargazers"><img src="https://img.shields.io/github/stars/TikHub/TikHub-API-Python-SDK?style=social" alt="GitHub Stars"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/network/members"><img src="https://img.shields.io/github/forks/TikHub/TikHub-API-Python-SDK?style=social" alt="GitHub Forks"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/issues"><img src="https://img.shields.io/github/issues/TikHub/TikHub-API-Python-SDK" alt="GitHub Issues"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/pulls"><img src="https://img.shields.io/github/issues-pr/TikHub/TikHub-API-Python-SDK" alt="GitHub Pull Requests"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/blob/main/LICENSE"><img src="https://img.shields.io/github/license/TikHub/TikHub-API-Python-SDK" alt="License"></a>
</p>

<p align="center">
  <a href="README.md">English</a> | <a href="README_CN.md">中文</a> | <a href="README_FR.md">Fran&ccedil;ais</a> | <a href="README_ES.md">Espa&ntilde;ol</a> | 日本語
</p>

<p align="center">
  <img src="TikHub_Banner.jpg" alt="TikHub Banner">
</p>

[TikHub](https://tikhub.io) ソーシャルメディアデータ API の公式 Python SDK — TikTok、Douyin（抖音）、Instagram、YouTube、Twitter/X、Xiaohongshu（小紅書）、Bilibili、Weibo、Threads、LinkedIn、Reddit、Kuaishou（快手）、WeChat、Lemon8、Zhihu（知乎）など **16以上のソーシャルメディアプラットフォーム** にリアルタイムアクセスできる統一 REST API。

**AI トレーニング**、**インフルエンサー分析**、**トレンド監視**、**感情分析**、**市場調査**、**競合インテリジェンス** など、大規模な構造化ソーシャルメディアデータを必要とする開発者、データサイエンティスト、AI エンジニア向けに構築されています。

## TikHub を選ぶ理由

- **1000以上のエンドポイント** — 16プラットフォームを1つの API キーで利用可能
- **リアルタイムデータ** — 動画詳細、ユーザープロフィール、コメント、検索結果、ライブ配信、トレンドコンテンツ、EC分析
- **RESTful & OpenAPI ネイティブ** — すべてのエンドポイントが [OpenAPI 仕様](https://api.tikhub.io/openapi.json) に文書化され、[Swagger UI](https://api.tikhub.io) でテスト可能
- **MCP 統合** — [Model Context Protocol](https://tikhub.io) 経由で AI エージェント（Claude、LangChain、Coze、n8n）をソーシャルメディアデータに直接接続
- **データセット** — トレーニングと研究用の10億件以上の構造化済みレコード

## この SDK を選ぶ理由

- **100% エンドポイントカバレッジ** — OpenAPI 仕様 V5.3.2 の 1010 / 1010 エンドポイント、機械的に生成・検証
- **同期 + 非同期** — `TikHub` と `AsyncTikHub` クライアント、API は完全に同一
- **本番環境対応** — 指数バックオフによる自動リトライ、レート制限処理、構造化エラー階層
- **型安全** — `mypy --strict` 対応、`httpx` + `pydantic v2` で構築
- **ゼロコンフィグ** — フラットな kwargs、設定オブジェクト不要；環境変数1つで利用開始

> **バージョン:** `2.1.1` — Python 3.9+ が必要

## 対応プラットフォーム

| プラットフォーム | リソース | エンドポイント数 |
|---|---|---|
| TikTok | `tiktok_web`, `tiktok_app_v3`, `tiktok_creator`, `tiktok_analytics`, `tiktok_ads`, `tiktok_shop_web` | 200+ |
| Douyin（抖音） | `douyin_web`, `douyin_app_v3`, `douyin_search`, `douyin_billboard`, `douyin_creator`, `douyin_xingtu` | 400+ |
| Instagram | `instagram_v1`, `instagram_v2`, `instagram_v3` | 80+ |
| YouTube | `youtube_web`, `youtube_web_v2` | 50+ |
| Twitter / X | `twitter_web` | 13+ |
| Xiaohongshu（小紅書） | `xiaohongshu_web`, `xiaohongshu_app`（+ v2/v3 バリアント） | 80+ |
| Bilibili | `bilibili_web`, `bilibili_app` | 40+ |
| Weibo（微博） | `weibo_web`, `weibo_web_v2`, `weibo_app` | 30+ |
| Threads | `threads_web` | 10+ |
| LinkedIn | `linkedin_web` | 10+ |
| Reddit | `reddit_app` | 10+ |
| Kuaishou（快手） | `kuaishou_web`, `kuaishou_app` | 20+ |
| WeChat | `wechat_channels`, `wechat_media_platform_web` | 20+ |
| Lemon8 | `lemon8_app` | 10+ |
| Zhihu（知乎） | `zhihu_web` | 30+ |
| その他 | `toutiao_web`, `toutiao_app`, `xigua_app_v2`, `pipixia_app`, `sora2` | 30+ |

## インストール

```bash
pip install tikhub
```

Python 3.9+ が必要です。

### ソースからインストール

```bash
git clone https://github.com/TikHub/TikHub-API-Python-SDK.git
cd TikHub-API-Python-SDK
pip install -e ".[dev]"
pytest -q
```

## API キーの取得

1. [https://user.tikhub.io/login](https://user.tikhub.io/login) にアクセスしてサインアップ / ログインします。
2. ダッシュボードから API キーをコピーします。
3. 環境変数として設定するか、直接渡します：

```bash
export TIKHUB_API_KEY="YOUR_API_KEY"
```

## クイックスタート

```python
from tikhub import TikHub

client = TikHub(api_key="YOUR_API_KEY")

# OpenAPI 仕様と 1:1 対応 — リソース = タグ、メソッド = パスのベースネーム
video = client.douyin_web.fetch_one_video(aweme_id="7251234567890123456")
print(video.aweme_detail.desc)

client.close()
```

推奨のコンテキストマネージャーを使用：

```python
with TikHub(api_key="YOUR_API_KEY") as client:
    health = client.health_check.check()
    print(health.status)
```

## 非同期

```python
import asyncio
from tikhub import AsyncTikHub

async def main():
    async with AsyncTikHub(api_key="YOUR_API_KEY") as client:
        video = await client.douyin_web.fetch_one_video(aweme_id="...")
        print(video.aweme_detail.desc)

asyncio.run(main())
```

## 設定

コンストラクタは1つの必須引数といくつかのオプション kwargs を受け取ります：

```python
TikHub(
    api_key=None,        # str | None — デフォルトは $TIKHUB_API_KEY
    timeout=30,          # float | None — リクエストの合計タイムアウト（秒）
    base_url=None,       # str | None — プライベートミラー用のみ

    # 上級（まれ）：
    max_retries=3,
    proxy=None,
    user_agent=None,
    parse_response=True,
    http_client=None,    # 独自の httpx.Client を使用
)
```

## 命名規則

SDK は TikHub OpenAPI 仕様から機械的に生成されます。2つのルール：

1. **リソース属性** = OpenAPI タグを小文字化、ハイフンをアンダースコアに変換、`-API` を除去。
   `Douyin-Web-API` -> `client.douyin_web`。`TikTok-App-V3-API` -> `client.tiktok_app_v3`。
2. **メソッド名** = API パスの**最後のセグメントをそのまま使用**。
   `/api/v1/douyin/web/fetch_one_video` -> `client.douyin_web.fetch_one_video(...)`。

パラメータ名は OpenAPI 仕様と完全に一致します。

## CLI

```bash
export TIKHUB_API_KEY="YOUR_API_KEY"

tikhub health                                 # API 接続確認
tikhub fetch https://v.douyin.com/abc/        # ユニバーサル動画 URL パーサー
tikhub user info                              # プラン + クォータ
tikhub user usage                             # 本日のリクエスト数
```

すべてのコマンドは JSON を標準出力に表示します。

## ライセンス

MIT。
