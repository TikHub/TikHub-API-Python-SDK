# TikHub API Python SDK

<p align="center">
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/stargazers"><img src="https://img.shields.io/github/stars/TikHub/TikHub-API-Python-SDK?style=social" alt="GitHub Stars"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/network/members"><img src="https://img.shields.io/github/forks/TikHub/TikHub-API-Python-SDK?style=social" alt="GitHub Forks"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/issues"><img src="https://img.shields.io/github/issues/TikHub/TikHub-API-Python-SDK" alt="GitHub Issues"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/pulls"><img src="https://img.shields.io/github/issues-pr/TikHub/TikHub-API-Python-SDK" alt="GitHub Pull Requests"></a>
  <a href="https://github.com/TikHub/TikHub-API-Python-SDK/blob/main/LICENSE"><img src="https://img.shields.io/github/license/TikHub/TikHub-API-Python-SDK" alt="License"></a>
</p>

<p align="center">
  <a href="README.md">English</a> | 中文 | <a href="README_FR.md">Fran&ccedil;ais</a> | <a href="README_ES.md">Espa&ntilde;ol</a> | <a href="README_JP.md">日本語</a>
</p>

<p align="center">
  <img src="TikHub_Banner.jpg" alt="TikHub Banner">
</p>

[TikHub](https://tikhub.io) 社交媒体数据 API 的官方 Python SDK — 统一的 REST API，可实时访问 **16+ 社交媒体平台**，包括 TikTok、抖音、Instagram、YouTube、Twitter/X、小红书、B站、微博、Threads、LinkedIn、Reddit、快手、微信、Lemon8、知乎等。

专为开发者、数据科学家和 AI 工程师打造，适用于 **AI 训练**、**达人分析**、**趋势监控**、**舆情分析**、**市场调研** 和 **竞品情报** 等场景。

## 为什么选择 TikHub？

- **1000+ 接口**，覆盖 16 个平台，只需一个 API Key
- **实时数据** — 视频详情、用户资料、评论、搜索结果、直播、热门内容、电商分析
- **RESTful & OpenAPI 原生** — 所有接口均在 [OpenAPI 规范](https://api.tikhub.io/openapi.json) 中有文档，可通过 [Swagger UI](https://api.tikhub.io) 在线测试
- **MCP 集成** — 通过 [Model Context Protocol](https://tikhub.io) 将 AI Agent（Claude、LangChain、Coze、n8n）直接连接到社交媒体数据
- **数据集** — 10 亿+ 条预采集的结构化数据，可用于训练和研究

## 为什么选择这个 SDK？

- **100% 接口覆盖** — OpenAPI 规范 V5.3.2 的 1010 / 1010 个接口，机械化生成并验证
- **同步 + 异步** — `TikHub` 和 `AsyncTikHub` 客户端，API 完全一致
- **生产就绪** — 自动重试（指数退避）、速率限制处理、结构化异常体系（含完整调试上下文）
- **类型安全** — `mypy --strict` 通过，基于 `httpx` + `pydantic v2` 构建
- **零配置** — 扁平化参数，无需配置对象；设置一个环境变量即可使用

> **版本：** `2.1.1` — 需要 Python 3.9+

## 支持的平台

| 平台 | 资源 | 接口数 |
|---|---|---|
| TikTok | `tiktok_web`, `tiktok_app_v3`, `tiktok_creator`, `tiktok_analytics`, `tiktok_ads`, `tiktok_shop_web` | 200+ |
| 抖音 | `douyin_web`, `douyin_app_v3`, `douyin_search`, `douyin_billboard`, `douyin_creator`, `douyin_xingtu` | 400+ |
| Instagram | `instagram_v1`, `instagram_v2`, `instagram_v3` | 80+ |
| YouTube | `youtube_web`, `youtube_web_v2` | 50+ |
| Twitter / X | `twitter_web` | 13+ |
| 小红书 | `xiaohongshu_web`, `xiaohongshu_app`（+ v2/v3 变体） | 80+ |
| B站 | `bilibili_web`, `bilibili_app` | 40+ |
| 微博 | `weibo_web`, `weibo_web_v2`, `weibo_app` | 30+ |
| Threads | `threads_web` | 10+ |
| LinkedIn | `linkedin_web` | 10+ |
| Reddit | `reddit_app` | 10+ |
| 快手 | `kuaishou_web`, `kuaishou_app` | 20+ |
| 微信 | `wechat_channels`, `wechat_media_platform_web` | 20+ |
| Lemon8 | `lemon8_app` | 10+ |
| 知乎 | `zhihu_web` | 30+ |
| 其他 | `toutiao_web`, `toutiao_app`, `xigua_app_v2`, `pipixia_app`, `sora2` | 30+ |

## 安装

```bash
pip install tikhub
```

需要 Python 3.9+。

### 从源码安装

```bash
git clone https://github.com/TikHub/TikHub-API-Python-SDK.git
cd TikHub-API-Python-SDK
pip install -e ".[dev]"
pytest -q
```

## 获取 API Key

1. 前往 [https://user.tikhub.io/login](https://user.tikhub.io/login) 注册 / 登录。
2. 在控制台复制你的 API Key。
3. 设置为环境变量或直接传入：

```bash
export TIKHUB_API_KEY="YOUR_API_KEY"
```

## 快速开始

```python
from tikhub import TikHub

client = TikHub(api_key="YOUR_API_KEY")

# 与 OpenAPI 规范 1:1 对应 — 资源 = 标签, 方法 = 路径末段
video = client.douyin_web.fetch_one_video(aweme_id="7251234567890123456")
print(video.aweme_detail.desc)

client.close()
```

推荐使用上下文管理器：

```python
with TikHub(api_key="YOUR_API_KEY") as client:
    health = client.health_check.check()
    print(health.status)
```

## 异步用法

```python
import asyncio
from tikhub import AsyncTikHub

async def main():
    async with AsyncTikHub(api_key="YOUR_API_KEY") as client:
        video = await client.douyin_web.fetch_one_video(aweme_id="...")
        print(video.aweme_detail.desc)

asyncio.run(main())
```

## 配置

构造函数接受一个必需参数和少量可选参数：

```python
TikHub(
    api_key=None,        # str | None — 默认读取 $TIKHUB_API_KEY
    timeout=30,          # float | None — 总请求超时时间（秒）
    base_url=None,       # str | None — 仅在使用私有镜像时覆盖

    # 高级选项（较少使用）：
    max_retries=3,
    proxy=None,
    user_agent=None,
    parse_response=True,
    http_client=None,    # 传入自定义 httpx.Client
)
```

这就是全部的配置项。没有 `ClientConfig` 对象 — 所有选项都是扁平化的关键字参数。

## 命名规则

SDK 由 TikHub OpenAPI 规范机械化生成。两条规则：

1. **资源属性** = OpenAPI 标签，转小写，连字符转下划线，去掉 `-API` 后缀。
   `Douyin-Web-API` -> `client.douyin_web`。`TikTok-App-V3-API` -> `client.tiktok_app_v3`。
2. **方法名** = API 路径的**最后一段，保持原样**。
   `/api/v1/douyin/web/fetch_one_video` -> `client.douyin_web.fetch_one_video(...)`。

参数名与 OpenAPI 规范完全一致。如果你能读懂 TikHub API 文档，你就已经会用这个 SDK 了。

## 状态

**100% 接口覆盖**，基于 TikHub OpenAPI 规范 V5.3.2。

| | |
|---|---|
| 资源 | **52**（每个 OpenAPI 标签一个） |
| 接口 | **1010 / 1010** |
| 测试 | 110 个通过 |
| 类型检查 | mypy `--strict` 71 个源文件全部通过 |
| 代码检查 | ruff 通过 |

资源层由 `spec/openapi.json` **机械化生成**。当 TikHub 规范更新后，运行以下命令刷新：

```bash
python scripts/refresh_spec.py        # 拉取最新 openapi.json，打印差异
python scripts/generate_resources.py  # 重新生成所有 52 个资源文件 + 客户端
python scripts/generate_docs.py       # 重新生成 docs/reference.md
python scripts/verify_coverage.py     # 验证 100% 覆盖
pytest -q                             # 110 个测试
```

## CLI 命令行工具

SDK 内置了一个轻量命令行工具：

```bash
export TIKHUB_API_KEY="YOUR_API_KEY"

tikhub health                                 # 检查 API 连通性
tikhub fetch https://v.douyin.com/abc/        # 通用视频链接解析
tikhub user info                              # 账户套餐 + 配额
tikhub user usage                             # 今日请求量
```

所有命令输出 JSON 到标准输出 — 可通过管道传给 `jq` 或其他格式化工具。

## 文档

完整文档（mkdocs-material）：身份认证、异步、异常处理、分页、重试、日志、CLI、迁移指南、命名规则，以及所有 1010 个接口的自动生成参考文档。

```bash
pip install -e ".[docs]"
mkdocs serve            # http://127.0.0.1:8000
```

## 许可证

MIT。
