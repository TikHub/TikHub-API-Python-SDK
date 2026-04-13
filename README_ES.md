# TikHub API Python SDK

<p align="center">
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/stargazers"><img src="https://img.shields.io/github/stars/TikHub/TikHub-API-Python-SDK?style=social" alt="GitHub Stars"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/network/members"><img src="https://img.shields.io/github/forks/TikHub/TikHub-API-Python-SDK?style=social" alt="GitHub Forks"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/issues"><img src="https://img.shields.io/github/issues/TikHub/TikHub-API-Python-SDK" alt="GitHub Issues"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/pulls"><img src="https://img.shields.io/github/issues-pr/TikHub/TikHub-API-Python-SDK" alt="GitHub Pull Requests"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/blob/main/LICENSE"><img src="https://img.shields.io/github/license/TikHub/TikHub-API-Python-SDK" alt="License"></a>
</p>

<p align="center">
  <a href="README.md">English</a> | <a href="README_CN.md">中文</a> | <a href="README_FR.md">Fran&ccedil;ais</a> | Espa&ntilde;ol | <a href="README_JP.md">日本語</a>
</p>

<p align="center">
  <img src="TikHub_Banner.jpg" alt="TikHub Banner">
</p>

El SDK oficial de Python para la API de datos de redes sociales de [TikHub](https://tikhub.io) — una API REST unificada que proporciona acceso en tiempo real a **m&aacute;s de 16 plataformas de redes sociales**, incluyendo TikTok, Douyin, Instagram, YouTube, Twitter/X, Xiaohongshu (Red Note), Bilibili, Weibo, Threads, LinkedIn, Reddit, Kuaishou, WeChat, Lemon8, Zhihu, y m&aacute;s.

Dise&ntilde;ado para desarrolladores, cient&iacute;ficos de datos e ingenieros de IA que necesitan datos estructurados de redes sociales a escala — para **entrenamiento de IA**, **an&aacute;lisis de influencers**, **monitoreo de tendencias**, **an&aacute;lisis de sentimientos**, **investigaci&oacute;n de mercado** e **inteligencia competitiva**.

## &iquest;Por qu&eacute; TikHub?

- **M&aacute;s de 1000 endpoints** en 16 plataformas con una sola clave API
- **Datos en tiempo real** — detalles de v&iacute;deos, perfiles de usuarios, comentarios, resultados de b&uacute;squeda, transmisiones en vivo, contenido en tendencia y an&aacute;lisis de e-commerce
- **RESTful y nativo de OpenAPI** — cada endpoint est&aacute; documentado en la [especificaci&oacute;n OpenAPI](https://api.tikhub.io/openapi.json) y se puede probar v&iacute;a [Swagger UI](https://api.tikhub.io)
- **Integraci&oacute;n MCP** — conecta agentes de IA (Claude, LangChain, Coze, n8n) directamente a los datos sociales v&iacute;a [Model Context Protocol](https://tikhub.io)
- **Datasets disponibles** — m&aacute;s de 1000 millones de registros estructurados pre-recolectados para entrenamiento e investigaci&oacute;n

## &iquest;Por qu&eacute; este SDK?

- **Cobertura del 100%** — 1010 / 1010 endpoints de la especificaci&oacute;n OpenAPI V5.3.2, generados y verificados mec&aacute;nicamente
- **Sync + async** — clientes `TikHub` y `AsyncTikHub` con APIs id&eacute;nticas
- **Listo para producci&oacute;n** — reintentos autom&aacute;ticos con backoff exponencial, manejo de l&iacute;mites de tasa, jerarqu&iacute;a de errores estructurada
- **Type-safe** — compatible con `mypy --strict`, construido sobre `httpx` + `pydantic v2`
- **Cero configuraci&oacute;n** — kwargs simples, sin objetos de configuraci&oacute;n; establece una variable de entorno y listo

> **Versi&oacute;n:** `2.1.1` — Requiere Python 3.9+

## Plataformas soportadas

| Plataforma | Recurso | Endpoints |
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
| Otros | `toutiao_web`, `toutiao_app`, `xigua_app_v2`, `pipixia_app`, `sora2` | 30+ |

## Instalaci&oacute;n

```bash
pip install tikhub
```

Requiere Python 3.9+.

### Desde el c&oacute;digo fuente

```bash
git clone https://github.com/TikHub/TikHub-API-Python-SDK.git
cd TikHub-API-Python-SDK
pip install -e ".[dev]"
pytest -q
```

## Obtener tu clave API

1. Ve a [https://user.tikhub.io/login](https://user.tikhub.io/login) y reg&iacute;strate / inicia sesi&oacute;n.
2. Copia tu clave API desde el panel de control.
3. Establ&eacute;cela como variable de entorno o p&aacute;sala directamente:

```bash
export TIKHUB_API_KEY="YOUR_API_KEY"
```

## Inicio r&aacute;pido

```python
from tikhub import TikHub

client = TikHub(api_key="YOUR_API_KEY")

# 1:1 con la especificaci&oacute;n OpenAPI — recurso = tag, m&eacute;todo = basename de la ruta
video = client.douyin_web.fetch_one_video(aweme_id="7251234567890123456")
print(video.aweme_detail.desc)

client.close()
```

O con el gestor de contexto recomendado:

```python
with TikHub(api_key="YOUR_API_KEY") as client:
    health = client.health_check.check()
    print(health.status)
```

## As&iacute;ncrono

```python
import asyncio
from tikhub import AsyncTikHub

async def main():
    async with AsyncTikHub(api_key="YOUR_API_KEY") as client:
        video = await client.douyin_web.fetch_one_video(aweme_id="...")
        print(video.aweme_detail.desc)

asyncio.run(main())
```

## Configuraci&oacute;n

El constructor acepta un argumento obligatorio y algunos kwargs opcionales:

```python
TikHub(
    api_key=None,        # str | None — por defecto $TIKHUB_API_KEY
    timeout=30,          # float | None — timeout total de la solicitud en segundos
    base_url=None,       # str | None — solo sobrescribir para un espejo privado

    # Avanzado (raro):
    max_retries=3,
    proxy=None,
    user_agent=None,
    parse_response=True,
    http_client=None,    # trae tu propio httpx.Client
)
```

## Reglas de nomenclatura

El SDK se genera mec&aacute;nicamente a partir de la especificaci&oacute;n OpenAPI de TikHub. Dos reglas:

1. **Atributo de recurso** = tag OpenAPI, en min&uacute;sculas, guiones -> underscores, `-API` eliminado.
   `Douyin-Web-API` -> `client.douyin_web`. `TikTok-App-V3-API` -> `client.tiktok_app_v3`.
2. **Nombre del m&eacute;todo** = el **&uacute;ltimo segmento de la ruta API, tal cual**.
   `/api/v1/douyin/web/fetch_one_video` -> `client.douyin_web.fetch_one_video(...)`.

Los nombres de par&aacute;metros coinciden exactamente con la especificaci&oacute;n OpenAPI.

## CLI

```bash
export TIKHUB_API_KEY="YOUR_API_KEY"

tikhub health                                 # verificar conectividad de la API
tikhub fetch https://v.douyin.com/abc/        # analizador universal de URLs de v&iacute;deo
tikhub user info                              # plan + cuota
tikhub user usage                             # conteo de solicitudes de hoy
```

Todos los comandos imprimen JSON en stdout.

## Licencia

MIT.
