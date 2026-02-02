#!/usr/bin/env python3
import os
import json
import time
import argparse
import requests

BASE_URL = os.getenv("HODLAI_BASE_URL", "https://api.hodlai.fun/v1")
API_KEY = os.getenv("HODLAI_API_KEY")


def main():
    parser = argparse.ArgumentParser(description="Generate video via HodlAI (async).")
    parser.add_argument("--model", required=True, help="Video model name, e.g. sora-2")
    parser.add_argument("--prompt", required=True, help="Prompt text")
    parser.add_argument("--duration", type=int, default=10, help="Duration seconds (5-20)")
    parser.add_argument("--resolution", default="1080p", help="Resolution, e.g. 1080p")
    parser.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio, e.g. 16:9")
    parser.add_argument("--poll", action="store_true", help="Poll until completed")
    parser.add_argument("--interval", type=int, default=10, help="Poll interval seconds")
    args = parser.parse_args()

    if not API_KEY:
        raise SystemExit("Missing HODLAI_API_KEY env var")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    create_url = f"{BASE_URL}/video/generations"
    payload = {
        "model": args.model,
        "prompt": args.prompt,
        "duration": args.duration,
        "resolution": args.resolution,
        "aspect_ratio": args.aspect_ratio
    }

    r = requests.post(create_url, headers=headers, json=payload, timeout=60)
    r.raise_for_status()
    data = r.json()
    print(json.dumps(data, ensure_ascii=False, indent=2))

    task_id = data.get("id")
    if not args.poll or not task_id:
        return

    status_url = f"{BASE_URL}/video/generations/{task_id}"
    while True:
        s = requests.get(status_url, headers=headers, timeout=60)
        s.raise_for_status()
        out = s.json()
        print(json.dumps(out, ensure_ascii=False, indent=2))
        if out.get("status") in ("completed", "failed"):
            break
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
