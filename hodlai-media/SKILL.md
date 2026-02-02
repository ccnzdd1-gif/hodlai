---
name: hodlai-media
description: Use when configuring or using HodlAI (hodlai.fun) OpenAI-compatible APIs to generate images or videos, including setup of base URL, API key, and calling image/video endpoints.
---

# HodlAI Media

## Overview
使用 HodlAI 的 OpenAI 兼容接口，快速配置图像生成与视频生成能力。

## Quick Start
1) 设置环境变量：
```bash
export HODLAI_API_KEY="<your_key>"
export HODLAI_BASE_URL="https://api.hodlai.fun/v1"
```

2) 图像生成：
```bash
python3 scripts/hodlai_image.py --model <image_model> --prompt "A cat in space" --size 1024x1024
```

3) 视频生成（异步 + 轮询）：
```bash
python3 scripts/hodlai_video.py --model sora-2 --prompt "A cat walking on Mars" --duration 10 --resolution 1080p --aspect_ratio 16:9 --poll
```

## Notes
- 详细接口说明见 `references/hodlai_api.md`。
- 若需要在现有服务中集成，请复用相同 Base URL 与 Authorization 头。
