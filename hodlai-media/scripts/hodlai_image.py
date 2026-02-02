#!/usr/bin/env python3
import os
import json
import argparse
import requests

BASE_URL = os.getenv("HODLAI_BASE_URL", "https://api.hodlai.fun/v1")
API_KEY = os.getenv("HODLAI_API_KEY")


def main():
    parser = argparse.ArgumentParser(description="Generate image via HodlAI (OpenAI-compatible).")
    parser.add_argument("--model", required=True, help="Image model name")
    parser.add_argument("--prompt", required=True, help="Prompt text")
    parser.add_argument("--size", default="1024x1024", help="Image size, e.g. 1024x1024")
    parser.add_argument("--n", type=int, default=1, help="Number of images")
    args = parser.parse_args()

    if not API_KEY:
        raise SystemExit("Missing HODLAI_API_KEY env var")

    url = f"{BASE_URL}/images/generations"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": args.model,
        "prompt": args.prompt,
        "n": args.n,
        "size": args.size
    }

    r = requests.post(url, headers=headers, json=payload, timeout=60)
    r.raise_for_status()
    print(json.dumps(r.json(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
