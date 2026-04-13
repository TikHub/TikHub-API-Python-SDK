# TikHub API Python SDK

<p align="center">
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/stargazers"><img src="https://img.shields.io/github/stars/TikHub/TikHub-API-Python-SDK?style=social" alt="GitHub Stars"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/network/members"><img src="https://img.shields.io/github/forks/TikHub/TikHub-API-Python-SDK?style=social" alt="GitHub Forks"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/issues"><img src="https://img.shields.io/github/issues/TikHub/TikHub-API-Python-SDK" alt="GitHub Issues"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/pulls"><img src="https://img.shields.io/github/issues-pr/TikHub/TikHub-API-Python-SDK" alt="GitHub Pull Requests"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/blob/main/LICENSE"><img src="https://img.shields.io/github/license/TikHub/TikHub-API-Python-SDK" alt="License"></a>
</p>

<p align="center">
  <a href="README.md">English</a> | <a href="README_CN.md">中文</a> | Fran&ccedil;ais | <a href="README_ES.md">Espa&ntilde;ol</a> | <a href="README_JP.md">日本語</a>
</p>

<p align="center">
  <img src="TikHub_Banner.jpg" alt="TikHub Banner">
</p>

Le SDK Python officiel pour l'API de donn&eacute;es de m&eacute;dias sociaux [TikHub](https://tikhub.io) — une API REST unifi&eacute;e qui fournit un acc&egrave;s en temps r&eacute;el &agrave; **16+ plateformes de m&eacute;dias sociaux**, dont TikTok, Douyin, Instagram, YouTube, Twitter/X, Xiaohongshu (Red Note), Bilibili, Weibo, Threads, LinkedIn, Reddit, Kuaishou, WeChat, Lemon8, Zhihu, et plus encore.

Con&ccedil;u pour les d&eacute;veloppeurs, les data scientists et les ing&eacute;nieurs IA qui ont besoin de donn&eacute;es structur&eacute;es de m&eacute;dias sociaux &agrave; grande &eacute;chelle — pour l'**entra&icirc;nement IA**, l'**analyse d'influenceurs**, la **veille de tendances**, l'**analyse de sentiments**, les **&eacute;tudes de march&eacute;** et la **veille concurrentielle**.

## Pourquoi TikHub ?

- **1000+ endpoints** sur 16 plateformes avec une seule cl&eacute; API
- **Donn&eacute;es en temps r&eacute;el** — d&eacute;tails vid&eacute;o, profils utilisateurs, commentaires, r&eacute;sultats de recherche, livestreams, contenu tendance et analyses e-commerce
- **RESTful & natif OpenAPI** — chaque endpoint est document&eacute; dans la [sp&eacute;cification OpenAPI](https://api.tikhub.io/openapi.json) et testable via [Swagger UI](https://api.tikhub.io)
- **Int&eacute;gration MCP** — connectez les agents IA (Claude, LangChain, Coze, n8n) directement aux donn&eacute;es sociales via [Model Context Protocol](https://tikhub.io)
- **Datasets disponibles** — 1 milliard+ d'enregistrements structur&eacute;s pr&eacute;-collect&eacute;s pour l'entra&icirc;nement et la recherche

## Pourquoi ce SDK ?

- **Couverture &agrave; 100%** — 1010 / 1010 endpoints de la sp&eacute;cification OpenAPI V5.3.2, g&eacute;n&eacute;r&eacute;s et v&eacute;rifi&eacute;s m&eacute;caniquement
- **Sync + async** — clients `TikHub` et `AsyncTikHub` avec des APIs identiques
- **Pr&ecirc;t pour la production** — nouvelles tentatives automatiques avec backoff exponentiel, gestion des limites de taux, hi&eacute;rarchie d'erreurs structur&eacute;e
- **Type-safe** — compatible `mypy --strict`, construit sur `httpx` + `pydantic v2`
- **Z&eacute;ro configuration** — kwargs simples, pas d'objets de config ; d&eacute;finissez une variable d'environnement et c'est parti

> **Version :** `2.1.1` — Requiert Python 3.9+

## Plateformes support&eacute;es

| Plateforme | Ressource | Endpoints |
|---|---|---|
| TikTok | `tiktok_web`, `tiktok_app_v3`, `tiktok_creator`, `tiktok_analytics`, `tiktok_ads`, `tiktok_shop_web` | 200+ |
| Douyin | `douyin_web`, `douyin_app_v3`, `douyin_search`, `douyin_billboard`, `douyin_creator`, `douyin_xingtu` | 400+ |
| Instagram | `instagram_v1`, `instagram_v2`, `instagram_v3` | 80+ |
| YouTube | `youtube_web`, `youtube_web_v2` | 50+ |
| Twitter / X | `twitter_web` | 13+ |
| Xiaohongshu (Red Note) | `xiaohongshu_web`, `xiaohongshu_app` (+ variantes v2/v3) | 80+ |
| Bilibili | `bilibili_web`, `bilibili_app` | 40+ |
| Weibo | `weibo_web`, `weibo_web_v2`, `weibo_app` | 30+ |
| Threads | `threads_web` | 10+ |
| LinkedIn | `linkedin_web` | 10+ |
| Reddit | `reddit_app` | 10+ |
| Kuaishou | `kuaishou_web`, `kuaishou_app` | 20+ |
| WeChat | `wechat_channels`, `wechat_media_platform_web` | 20+ |
| Lemon8 | `lemon8_app` | 10+ |
| Zhihu | `zhihu_web` | 30+ |
| Autres | `toutiao_web`, `toutiao_app`, `xigua_app_v2`, `pipixia_app`, `sora2` | 30+ |

## Installation

```bash
pip install tikhub
```

Requiert Python 3.9+.

### Depuis les sources

```bash
git clone https://github.com/TikHub/TikHub-API-Python-SDK.git
cd TikHub-API-Python-SDK
pip install -e ".[dev]"
pytest -q
```

## Obtenir votre cl&eacute; API

1. Rendez-vous sur [https://user.tikhub.io/login](https://user.tikhub.io/login) et inscrivez-vous / connectez-vous.
2. Copiez votre cl&eacute; API depuis le tableau de bord.
3. D&eacute;finissez-la comme variable d'environnement ou passez-la directement :

```bash
export TIKHUB_API_KEY="YOUR_API_KEY"
```

## D&eacute;marrage rapide

```python
from tikhub import TikHub

client = TikHub(api_key="YOUR_API_KEY")

# 1:1 avec la sp&eacute;cification OpenAPI — ressource = tag, m&eacute;thode = basename du chemin
video = client.douyin_web.fetch_one_video(aweme_id="7251234567890123456")
print(video.aweme_detail.desc)

client.close()
```

Ou avec le gestionnaire de contexte recommand&eacute; :

```python
with TikHub(api_key="YOUR_API_KEY") as client:
    health = client.health_check.check()
    print(health.status)
```

## Asynchrone

```python
import asyncio
from tikhub import AsyncTikHub

async def main():
    async with AsyncTikHub(api_key="YOUR_API_KEY") as client:
        video = await client.douyin_web.fetch_one_video(aweme_id="...")
        print(video.aweme_detail.desc)

asyncio.run(main())
```

## Configuration

Le constructeur accepte un argument obligatoire et quelques kwargs optionnels :

```python
TikHub(
    api_key=None,        # str | None — par d&eacute;faut $TIKHUB_API_KEY
    timeout=30,          # float | None — timeout total de la requ&ecirc;te en secondes
    base_url=None,       # str | None — &agrave; ne remplacer que pour un miroir priv&eacute;

    # Avanc&eacute; (rare) :
    max_retries=3,
    proxy=None,
    user_agent=None,
    parse_response=True,
    http_client=None,    # apportez votre propre httpx.Client
)
```

## R&egrave;gles de nommage

Le SDK est g&eacute;n&eacute;r&eacute; m&eacute;caniquement depuis la sp&eacute;cification OpenAPI de TikHub. Deux r&egrave;gles :

1. **Attribut de ressource** = tag OpenAPI, en minuscules, tirets -> underscores, `-API` supprim&eacute;.
   `Douyin-Web-API` -> `client.douyin_web`. `TikTok-App-V3-API` -> `client.tiktok_app_v3`.
2. **Nom de m&eacute;thode** = le **dernier segment du chemin API, tel quel**.
   `/api/v1/douyin/web/fetch_one_video` -> `client.douyin_web.fetch_one_video(...)`.

Les noms de param&egrave;tres correspondent exactement &agrave; la sp&eacute;cification OpenAPI.

## CLI

```bash
export TIKHUB_API_KEY="YOUR_API_KEY"

tikhub health                                 # v&eacute;rifier la connectivit&eacute; API
tikhub fetch https://v.douyin.com/abc/        # analyseur universel d'URL vid&eacute;o
tikhub user info                              # forfait + quota
tikhub user usage                             # nombre de requ&ecirc;tes du jour
```

Toutes les commandes affichent du JSON sur stdout.

## Licence

MIT.
