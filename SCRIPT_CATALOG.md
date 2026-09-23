# HodlAI 脚本目录

| 脚本 | 功能 | 关键输入 |
|---|---|---|
| `hodlai-media/scripts/hodlai_image.py` | 创建图片生成任务并打印接口返回结果。 | `--model`、`--prompt`、`--size`、`--n`、`HODLAI_API_KEY` |
| `hodlai-media/scripts/hodlai_video.py` | 创建视频生成任务；使用 `--poll` 时轮询任务直到 `completed` 或 `failed`。 | `--model`、`--prompt`、`--duration`、`--resolution`、`--aspect_ratio` |

两个脚本都使用 HTTPS API，不保存生成结果或密钥；运行前应确认模型名、时长和分辨率符合服务端限制。
