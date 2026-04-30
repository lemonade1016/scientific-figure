#!/usr/bin/env python3
"""
Scientific Figure — Parallel Image Generator (stdlib only, zero dependencies).

Replaces the fragile inline Bash orchestration. Accepts a distilled prompt via file,
reads API keys from config.local.json, fires all selected providers concurrently,
polls async ones, downloads images, and outputs a minimal JSON summary.

Usage:
  python generate_images.py \\
    --prompt-file .claude/distilled_prompt.txt \\
    --providers ernie,qwen,gemini \\
    --output-prefix 001_r1 \\
    --aspect-ratio 1:1
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error
import ssl
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Optional

SKILL_DIR = Path(__file__).resolve().parent
CONFIG_PATH = SKILL_DIR / "config.local.json"

# ── Size mapping: layout AR → per-provider format ──────────────────────
SIZE_MAP = {
    "1:1": {
        "ernie": "1024x1024", "wan": "1K", "qwen": "1024*1024",
        "zimage": "1024*1024", "gemini": "1:1", "gptimage2": "1:1",
    },
    "16:9": {
        "ernie": "1376x768", "wan": "1K", "qwen": "1280*720",
        "zimage": "1280*720", "gemini": "16:9", "gptimage2": "16:9",
    },
    "9:16": {
        "ernie": "768x1376", "wan": "1K", "qwen": "720*1280",
        "zimage": "720*1280", "gemini": "9:16", "gptimage2": "9:16",
    },
}

POLL_INTERVAL = 5   # seconds between async polls
MAX_POLL_TIME = 120  # seconds total timeout for async providers
SSL_CONTEXT = ssl.create_default_context()


# ── Helpers ─────────────────────────────────────────────────────────────
def _req(url: str, headers: dict, body: Optional[dict] = None,
         method: str = "POST") -> dict:
    """Send an HTTP request, return parsed JSON. Raises on non-2xx."""
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
    # Ensure User-Agent is set — some APIs block the default Python-urllib UA
    headers.setdefault("User-Agent", "scientific-figure/2.0")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30, context=SSL_CONTEXT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        # Try to include the response body in the error
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code} from {url}: {err_body[:500]}")


def _download(url: str, dest: str) -> None:
    """Download a file from *url* to *dest*."""
    req = urllib.request.Request(url, headers={"User-Agent": "scientific-figure/2.0"})
    with urllib.request.urlopen(req, timeout=60, context=SSL_CONTEXT) as resp:
        Path(dest).write_bytes(resp.read())


# ── Provider definitions ────────────────────────────────────────────────
@dataclass
class Provider:
    slug: str
    platform: str
    model: str
    is_async: bool

    def build_payload(self, prompt: str, size: str, ar: str) -> dict:
        """Return the JSON body for the creation request."""
        raise NotImplementedError

    def build_headers(self, api_key: str) -> dict:
        """Return HTTP headers."""
        raise NotImplementedError

    @property
    def endpoint(self) -> str:
        raise NotImplementedError

    def extract_image_url(self, resp: dict) -> Optional[str]:
        """Extract the final download URL from a completed response."""
        raise NotImplementedError

    def extract_task_id(self, resp: dict) -> Optional[str]:
        """For async providers: extract task_id from submission response."""
        return None

    def poll_url(self, task_id: str) -> str:
        """For async providers: the polling endpoint."""
        raise NotImplementedError

    def poll_headers(self, api_key: str) -> dict:
        """Headers for the polling request."""
        return self.build_headers(api_key)

    def is_terminal_status(self, status: str) -> bool:
        """Check whether a polling status is terminal."""
        raise NotImplementedError

    def is_success_status(self, status: str) -> bool:
        raise NotImplementedError

    def extract_image_url_from_poll(self, resp: dict) -> Optional[str]:
        """Extract image URL from the polling response."""
        return self.extract_image_url(resp)


# ── ERNIE-Image-Turbo (Baidu, sync) ────────────────────────────────────
class ErnieProvider(Provider):
    def __init__(self):
        super().__init__("ernie", "baidu", "ERNIE-Image-Turbo", is_async=False)

    @property
    def endpoint(self):
        return "https://aistudio.baidu.com/llm/lmapi/v3/images/generations"

    def build_headers(self, api_key):
        return {
            "Authorization": f"bearer {api_key}",
            "Content-Type": "application/json",
            "X-Client-Platform": "aistudio",
        }

    def build_payload(self, prompt, size, ar):
        return {
            "model": "ERNIE-Image-Turbo",
            "prompt": prompt,
            "n": 1,
            "response_format": "url",
            "size": size,
            "seed": 42,
            "use_pe": True,
            "num_inference_steps": 8,
            "guidance_scale": 1.0,
        }

    def extract_image_url(self, resp):
        try:
            return resp["data"][0]["url"]
        except (KeyError, IndexError):
            return None


# ── wan2.7-image-pro (Bailian, hybrid sync/async) ─────────────────────
class WanProvider(Provider):
    def __init__(self):
        super().__init__("wan", "bailian", "wan2.7-image-pro", is_async=True)

    @property
    def endpoint(self):
        return "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation"

    def build_headers(self, api_key):
        return {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def build_payload(self, prompt, size, ar):
        return {
            "model": "wan2.7-image-pro",
            "input": {"messages": [{"role": "user", "content": [{"text": prompt}]}]},
            "parameters": {"size": size, "n": 1, "watermark": False, "thinking_mode": True},
        }

    def _extract_image_from_choices(self, resp):
        """Extract image URL from a sync-style response (choices array)."""
        try:
            return resp["output"]["choices"][0]["message"]["content"][0]["image"]
        except (KeyError, IndexError):
            return None

    def extract_task_id(self, resp):
        # Try async path first
        try:
            return resp["output"]["task_id"]
        except KeyError:
            pass
        # Sync response — no task_id needed, image is already in response
        if self._extract_image_from_choices(resp):
            return "__sync__"
        return None

    def extract_image_url(self, resp):
        # Direct sync image
        url = self._extract_image_from_choices(resp)
        if url:
            return url
        # Async path
        try:
            return resp["output"]["results"][0]["url"]
        except (KeyError, IndexError):
            return None

    def poll_url(self, task_id):
        return f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}"

    def is_terminal_status(self, status):
        return status not in ("PENDING", "RUNNING")

    def is_success_status(self, status):
        return status == "SUCCEEDED"

    def extract_image_url_from_poll(self, resp):
        try:
            return resp["output"]["results"][0]["url"]
        except (KeyError, IndexError):
            return None


# ── qwen-image-2.0 (Bailian, sync) ─────────────────────────────────────
class QwenProvider(Provider):
    def __init__(self):
        super().__init__("qwen", "bailian", "qwen-image-2.0", is_async=False)

    @property
    def endpoint(self):
        return "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation"

    def build_headers(self, api_key):
        return {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def build_payload(self, prompt, size, ar):
        return {
            "model": "qwen-image-2.0",
            "input": {"messages": [{"role": "user", "content": [{"text": prompt}]}]},
            "parameters": {
                "size": size, "n": 1, "prompt_extend": False,
                "watermark": False,
                "negative_prompt": "blurry, low quality, distorted, watermark, text artifacts, jpeg artifacts, deformed, ugly",
            },
        }

    def extract_image_url(self, resp):
        try:
            return resp["output"]["choices"][0]["message"]["content"][0]["image"]
        except (KeyError, IndexError):
            return None


# ── z-image-turbo (Bailian, sync) ──────────────────────────────────────
class ZImageProvider(Provider):
    def __init__(self):
        super().__init__("zimage", "bailian", "z-image-turbo", is_async=False)

    @property
    def endpoint(self):
        return "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation"

    def build_headers(self, api_key):
        return {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def build_payload(self, prompt, size, ar):
        return {
            "model": "z-image-turbo",
            "input": {"messages": [{"role": "user", "content": [{"text": prompt}]}]},
            "parameters": {"size": size, "prompt_extend": False},
        }

    def extract_image_url(self, resp):
        try:
            return resp["output"]["choices"][0]["message"]["content"][0]["image"]
        except (KeyError, IndexError):
            return None


# ── gemini-3-pro-image-preview (API MART, async) ──────────────────────
class GeminiProvider(Provider):
    def __init__(self):
        super().__init__("gemini", "apimart", "gemini-3-pro-image-preview", is_async=True)

    @property
    def endpoint(self):
        return "https://api.apimart.ai/v1/images/generations"

    def build_headers(self, api_key):
        return {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def build_payload(self, prompt, size, ar):
        return {
            "model": "gemini-3-pro-image-preview",
            "prompt": prompt,
            "size": ar,  # aspect ratio like "1:1"
            "n": 1,
            "resolution": "1K",
            "official_fallback": True,
        }

    def extract_task_id(self, resp):
        try:
            return resp["data"][0]["task_id"]
        except (KeyError, IndexError):
            return None

    def extract_image_url(self, resp):
        try:
            return resp["data"]["result"]["images"][0]["url"][0]
        except (KeyError, IndexError):
            return None

    def poll_url(self, task_id):
        return f"https://api.apimart.ai/v1/tasks/{task_id}"

    def is_terminal_status(self, status):
        return status not in ("submitted", "processing", "pending")

    def is_success_status(self, status):
        return status == "completed"

    def extract_image_url_from_poll(self, resp):
        try:
            return resp["data"]["result"]["images"][0]["url"][0]
        except (KeyError, IndexError):
            return None


# ── GPT-Image-2 (API MART, async) ──────────────────────────────────────
class GptImage2Provider(Provider):
    def __init__(self):
        super().__init__("gptimage2", "apimart", "gpt-image-2", is_async=True)

    @property
    def endpoint(self):
        return "https://api.apimart.ai/v1/images/generations"

    def build_headers(self, api_key):
        return {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def build_payload(self, prompt, size, ar):
        return {
            "model": "gpt-image-2",
            "prompt": prompt,
            "n": 1,
            "size": ar,
            "resolution": "1k",
            "official_fallback": True,
        }

    def extract_task_id(self, resp):
        try:
            return resp["data"][0]["task_id"]
        except (KeyError, IndexError):
            return None

    def extract_image_url(self, resp):
        try:
            return resp["data"]["result"]["images"][0]["url"][0]
        except (KeyError, IndexError):
            return None

    def poll_url(self, task_id):
        return f"https://api.apimart.ai/v1/tasks/{task_id}"

    def is_terminal_status(self, status):
        return status not in ("submitted", "processing", "pending")

    def is_success_status(self, status):
        return status == "completed"

    def extract_image_url_from_poll(self, resp):
        try:
            return resp["data"]["result"]["images"][0]["url"][0]
        except (KeyError, IndexError):
            return None


# ── Provider registry ───────────────────────────────────────────────────
PROVIDERS: dict[str, Provider] = {
    "ernie": ErnieProvider(),
    "wan": WanProvider(),
    "qwen": QwenProvider(),
    "zimage": ZImageProvider(),
    "gemini": GeminiProvider(),
    "gptimage2": GptImage2Provider(),
}

PLATFORM_KEYS = {
    "baidu": "baidu_ai_studio",
    "bailian": "alibaba_bailian",
    "apimart": "apimart",
}


# ── Core logic ──────────────────────────────────────────────────────────
def load_config() -> dict:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Config not found: {CONFIG_PATH}")
    with open(CONFIG_PATH) as f:
        return json.load(f)


def get_api_key(config: dict, platform: str) -> str:
    key_path = PLATFORM_KEYS[platform]
    return config[key_path]["api_key"]


def submit_sync(prov: Provider, prompt: str, size: str, ar: str,
                api_key: str, output_prefix: str, workdir: str) -> dict:
    """Submit to a sync provider, download the image. Returns result dict."""
    payload = prov.build_payload(prompt, size, ar)
    headers = prov.build_headers(api_key)
    resp = _req(prov.endpoint, headers, payload)
    img_url = prov.extract_image_url(resp)
    if not img_url:
        return {"provider": prov.slug, "status": "failed",
                "error": f"Could not extract image URL from response: {json.dumps(resp)[:300]}"}

    filename = f"{output_prefix}_{prov.slug}.png"
    dest = os.path.join(workdir, filename)
    _download(img_url, dest)
    return {"provider": prov.slug, "status": "success", "output": filename,
            "path": dest}


def submit_and_poll(prov: Provider, prompt: str, size: str, ar: str,
                    api_key: str, output_prefix: str, workdir: str) -> dict:
    """Submit to an async provider, poll, download. Returns result dict."""
    # Submit
    payload = prov.build_payload(prompt, size, ar)
    headers = prov.build_headers(api_key)
    resp = _req(prov.endpoint, headers, payload)
    task_id = prov.extract_task_id(resp)
    if not task_id:
        return {"provider": prov.slug, "status": "failed",
                "error": f"Could not extract task_id from: {json.dumps(resp)[:300]}"}

    # Handle sync-in-disguise: wan2.7 may return the image directly
    if task_id == "__sync__":
        img_url = prov.extract_image_url(resp)
        if not img_url:
            return {"provider": prov.slug, "status": "failed",
                    "error": "Sync response but no image URL found"}
        filename = f"{output_prefix}_{prov.slug}.png"
        dest = os.path.join(workdir, filename)
        _download(img_url, dest)
        return {"provider": prov.slug, "status": "success",
                "output": filename, "path": dest}

    # Poll
    poll_hdrs = prov.poll_headers(api_key)
    deadline = time.time() + MAX_POLL_TIME
    last_resp = None
    while time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        try:
            last_resp = _req(prov.poll_url(task_id), poll_hdrs, method="GET")
        except RuntimeError as e:
            # Transient poll error — keep trying
            if time.time() < deadline:
                continue
            return {"provider": prov.slug, "status": "failed",
                    "error": f"Polling error: {e}"}
        status = None
        # Try Bailian-style status path
        try:
            status = last_resp["output"]["task_status"]
        except KeyError:
            pass
        # Try API MART-style status path
        if status is None:
            try:
                status = last_resp["data"]["status"]
            except KeyError:
                pass
        if status is None:
            continue
        if prov.is_terminal_status(status):
            if prov.is_success_status(status):
                img_url = prov.extract_image_url_from_poll(last_resp)
                if not img_url:
                    return {"provider": prov.slug, "status": "failed",
                            "error": "Terminal status but no image URL"}
                filename = f"{output_prefix}_{prov.slug}.png"
                dest = os.path.join(workdir, filename)
                _download(img_url, dest)
                return {"provider": prov.slug, "status": "success",
                        "output": filename, "path": dest}
            else:
                return {"provider": prov.slug, "status": "failed",
                        "error": f"Task ended with status: {status}"}

    return {"provider": prov.slug, "status": "timeout",
            "error": f"Polling timed out after {MAX_POLL_TIME}s"}


def generate(providers: list[str], prompt: str, output_prefix: str,
             aspect_ratio: str, workdir: str = ".") -> dict:
    """Main entry: fire all providers in parallel, return summary dict."""
    config = load_config()
    ar = aspect_ratio
    if ar not in SIZE_MAP:
        raise ValueError(f"Unsupported aspect ratio: {ar}. Use: {list(SIZE_MAP.keys())}")

    size_lookup = SIZE_MAP[ar]
    results = {}

    with ThreadPoolExecutor(max_workers=len(providers)) as pool:
        futures = {}
        for slug in providers:
            prov = PROVIDERS[slug]
            api_key = get_api_key(config, prov.platform)
            size = size_lookup[slug]
            if prov.is_async:
                fut = pool.submit(submit_and_poll, prov, prompt, size, ar,
                                  api_key, output_prefix, workdir)
            else:
                fut = pool.submit(submit_sync, prov, prompt, size, ar,
                                  api_key, output_prefix, workdir)
            futures[fut] = slug

        for fut in as_completed(futures):
            slug = futures[fut]
            try:
                results[slug] = fut.result()
            except Exception as e:
                results[slug] = {"provider": slug, "status": "failed",
                                 "error": str(e)}

    # Build summary
    success = [r for r in results.values() if r["status"] == "success"]
    failed = [r for r in results.values() if r["status"] != "success"]

    return {
        "prompt_id": output_prefix,
        "aspect_ratio": ar,
        "total": len(providers),
        "success": len(success),
        "failed": len(failed),
        "providers": {slug: results[slug] for slug in providers},
    }


# ── CLI ─────────────────────────────────────────────────────────────────
def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Scientific Figure — Parallel Image Generator")
    parser.add_argument("--prompt-file", required=True,
                        help="Path to file containing the distilled prompt")
    parser.add_argument("--providers", required=True,
                        help="Comma-separated provider slugs: ernie,wan,qwen,zimage,gemini,gptimage2")
    parser.add_argument("--output-prefix", required=True,
                        help="Output prefix, e.g. 003_r1")
    parser.add_argument("--aspect-ratio", default="1:1",
                        help="Aspect ratio: 1:1, 16:9, or 9:16")
    parser.add_argument("--workdir", default=".",
                        help="Working directory for output images (default: .)")
    args = parser.parse_args()

    # Read prompt
    prompt_path = Path(args.prompt_file)
    if not prompt_path.exists():
        print(json.dumps({"error": f"Prompt file not found: {args.prompt_file}"}))
        sys.exit(1)
    prompt = prompt_path.read_text(encoding="utf-8").strip()
    if not prompt:
        print(json.dumps({"error": "Prompt file is empty"}))
        sys.exit(1)

    # Parse providers
    slugs = [s.strip() for s in args.providers.split(",")]
    for s in slugs:
        if s not in PROVIDERS:
            print(json.dumps({"error": f"Unknown provider: {s}. Choose from: {list(PROVIDERS.keys())}"}))
            sys.exit(1)

    # Generate
    summary = generate(slugs, prompt, args.output_prefix,
                       args.aspect_ratio, args.workdir)

    # Minimal JSON summary to stdout — everything else is silent
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
