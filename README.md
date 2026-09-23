# HodlAI 媒体生成脚本

本仓库提供面向 HodlAI OpenAI 兼容接口的图片和视频生成命令行脚本。API 密钥只从环境变量读取，不写入仓库。

## 快速索引

逐脚本参数和功能表见 [SCRIPT_CATALOG.md](SCRIPT_CATALOG.md)。

| 路径 | 作用 |
|---|---|
| `hodlai-media/scripts/hodlai_image.py` | 调用图片生成接口，提交模型、提示词、尺寸和数量，打印 JSON 结果。 |
| `hodlai-media/scripts/hodlai_video.py` | 创建异步视频任务；可选择按间隔轮询直到完成或失败。 |
| `hodlai-media/SKILL.md` | 媒体生成工作流和调用约定。 |
| `hodlai-media/references/hodlai_api.md` | HodlAI 接口字段、端点和参数参考。 |
| `hodlai-media.skill` | 可复用的技能描述入口。 |

## 配置

设置 `HODLAI_API_KEY`，可通过 `HODLAI_BASE_URL` 覆盖默认 API 地址。脚本使用 Python `requests`，视频脚本的 `--poll` 会持续查询异步任务状态。
