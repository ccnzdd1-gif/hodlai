# HodlAI API (OpenAI-compatible)

Base URL: `https://api.hodlai.fun/v1`

## Auth
- Use `Authorization: Bearer $HODLAI_API_KEY`

## Image
- POST `/v1/images/generations`
- Body: `{ "model": "...", "prompt": "...", "n": 1, "size": "1024x1024" }`

## Video (async)
- POST `/v1/video/generations`
- Body: `{ "model": "sora-2", "prompt": "...", "duration": 10, "resolution": "1080p", "aspect_ratio": "16:9" }`
- GET `/v1/video/generations/{id}` to poll status (`pending/processing/completed`)
