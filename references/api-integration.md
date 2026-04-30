# API Integration Reference — Layer 2: Image Providers

This file contains curl commands and parameter guidance for 6 image generation models across 3 platforms. In Phase 8, all selected providers receive the **same distilled prompt** from Layer 1 and are called in parallel. Naming convention: `[promptID]_[round]_[provider].png`.

API keys are stored in `config.local.json` (gitignored). This file references config keys, not raw tokens.

---

## Provider Overview

| # | Platform | Model | Config Key | Sync/Async | Supports 1K | Strength |
|---|----------|-------|-----------|-------------|-------------|----------|
| 1 | Baidu AI Studio | `ERNIE-Image-Turbo` | `baidu_ai_studio.api_key` | Sync | `1024x1024` | Fast Turbo inference, strong Chinese text |
| 2 | Alibaba Bailian | `wan2.7-image-pro` | `alibaba_bailian.api_key` | Hybrid | `"1K"` preset | 4K max resolution, thinking mode |
| 3 | Alibaba Bailian | `qwen-image-2.0` | `alibaba_bailian.api_key` | Sync | `1024*1024` | Best Chinese/English text rendering |
| 4 | Alibaba Bailian | `z-image-turbo` | `alibaba_bailian.api_key` | Sync | `1024*1024` | Fastest generation, portrait strength |
| 5 | API MART | `gemini-3-pro-image-preview` | `apimart.api_key` | Async | `"1K"` | Reasoning-driven, multi-reference editing |
| 6 | API MART | `gpt-image-2` | `apimart.api_key` | Async | `"1K"` | Near-perfect text, deep world knowledge |

---

## Naming Convention

All generated images follow: **`[promptID]_[round]_[provider].png`**

| Field | Description | Example |
|-------|-------------|--------|
| `promptID` | 3-digit zero-padded ID, auto-incremented from `state.json` | `001`, `002`, `003` |
| `round` | Round number for the same prompt, starts at `r1` | `r1`, `r2`, `r3` |
| `provider` | Short provider slug | `ernie`, `wan`, `qwen`, `zimage`, `gemini`, `gptimage2` |

**Examples:**
```
001_r1_ernie.png       ← Prompt #1, Round 1, ERNIE-Image-Turbo
001_r1_wan.png         ← Same prompt/round, wan2.7-image-pro
001_r1_qwen.png        ← Same prompt/round, qwen-image-2.0
001_r2_ernie.png       ← Prompt #1, Round 2 (regenerated)
002_r1_gemini.png      ← Prompt #2, Round 1, Gemini 3 Pro Image
```

**Round tracking:** `state.json` stores `current_prompt_id` and `current_round`. When the user regenerates the same prompt, increment round. When starting a new prompt, increment prompt ID and reset round to 1.

---

## Config File

Read API keys from `config.local.json` at the skill root (absolute path):

```
/Users/lemonade/.claude/skills/scientific-figure/config.local.json
```

Structure:
```json
{
  "baidu_ai_studio": { "api_key": "...", "base_url": "..." },
  "alibaba_bailian": { "api_key": "...", "base_url": "...", "task_url": "..." },
  "apimart": { "api_key": "...", "base_url": "..." }
}
```

**Never echo or display raw API keys in output.** Reference them as `$BAIDU_API_KEY`, `$BAILIAN_API_KEY`, `$APIMART_API_KEY` in curl commands shown to the user.

Read state from `state.json`:
```
/Users/lemonade/.claude/skills/scientific-figure/state.json
```

---

## Aspect Ratio & Resolution Mapping

All 6 models support 1K resolution. Map Phase 5 layout type to each model's native format:

| Layout Type | Target AR | ERNIE `size` | wan2.7 `size` | qwen-image `size` | z-image `size` | Gemini `size` | GPT-Image-2 `size` |
|------------|-----------|-------------|---------------|-------------------|----------------|--------------|-------------------|
| Pipeline | 16:9 | `1376x768` | `"1K"` | `1280*720` | `1280*720` | `"16:9"` | `"16:9"` |
| Central Hub | 1:1 | `1024x1024` | `"1K"` | `1024*1024` | `1024*1024` | `"1:1"` | `"1:1"` |
| Layered Stack | 9:16 | `768x1376` | `"1K"` | `720*1280` | `720*1280` | `"9:16"` | `"9:16"` |
| Biological Spatial | 9:16 | `768x1376` | `"1K"` | `720*1280` | `720*1280` | `"9:16"` | `"9:16"` |
| Branching Tree | 9:16 | `768x1376` | `"1K"` | `720*1280` | `720*1280` | `"9:16"` | `"9:16"` |
| Cyclic Loop | 1:1 | `1024x1024` | `"1K"` | `1024*1024` | `1024*1024` | `"1:1"` | `"1:1"` |

**Notes:**
- Gemini and GPT-Image-2 via API MART use `size` for aspect ratio (e.g. `"1:1"`, `"16:9"`) and a separate `resolution` field for output quality (`"1K"`/`"2K"`/`"4K"`).
- wan2.7-image-pro uses semantic presets (`"1K"`, `"2K"`, `"4K"`). A 1K preset produces the image at ~1024px on the shortest side; the model handles aspect ratio internally.
- ERNIE uses 7 fixed `WxH` strings. For aspect ratios not exactly matching, pick the closest supported size.
- qwen-image-2.0 and z-image-turbo use `W*H` pixel format (note: `*` not `x`). Total pixels must be within 512²–2048² range.
- For wan2.7-image-pro, passing `"size": "1K"` with `"parameters"` block works. For qwen-image-2.0 and z-image-turbo, pass exact pixel string.
- Gemini and GPT-Image-2 are **async** — they return a `task_id` that must be polled via `GET /v1/tasks/{task_id}`. The image URL is at `data.result.images[0].url[0]` in the completed task response.

---

## Provider 1: Baidu AI Studio — ERNIE-Image-Turbo

**Platform:** Baidu AI Studio  
**Config path:** `baidu_ai_studio.api_key`  
**Docs:** https://aistudio.baidu.com/llm/lmapi/v3/images/generations

**Endpoint:** `POST https://aistudio.baidu.com/llm/lmapi/v3/images/generations`

**Curl command:**
```bash
API_KEY=$(jq -r '.baidu_ai_studio.api_key' /Users/lemonade/.claude/skills/scientific-figure/config.local.json)

curl -s -X POST "https://aistudio.baidu.com/llm/lmapi/v3/images/generations" \
  -H "Authorization: bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Client-Platform: aistudio" \
  -d '{
    "model": "ERNIE-Image-Turbo",
    "prompt": "<DISTILLED_PROMPT>",
    "n": 1,
    "response_format": "url",
    "size": "<SIZE>",
    "seed": 42,
    "use_pe": true,
    "num_inference_steps": 8,
    "guidance_scale": 1.0
  }' > .claude/sf_ernie_response.json
```

**Supported sizes (7 fixed resolutions):**

| Name | Size | Aspect |
|------|------|--------|
| Square 1:1 | `1024x1024` | 1:1 |
| Portrait 2:3 | `848x1264` | 2:3 |
| Portrait 9:16 | `768x1376` | 9:16 |
| Portrait 3:4 | `896x1200` | 3:4 |
| Landscape 3:2 | `1264x848` | 3:2 |
| Landscape 16:9 | `1376x768` | 16:9 |
| Landscape 4:3 | `1200x896` | 4:3 |

Invalid sizes default to `1376x768`.

**Response format:**
```json
{
  "id": "xxx",
  "object": "image",
  "created": 1700000000,
  "data": [
    {
      "url": "https://...",
      "b64_json": null
    }
  ],
  "usage": { "prompt_tokens": 0, "total_tokens": 0 }
}
```

**Post-processing:** Extract `data[0].url` and download:
```bash
URL=$(jq -r '.data[0].url' .claude/sf_ernie_response.json)
curl -s -o "001_r1_ernie.png" "$URL"
```

**Cost:** ~$0.01–0.03/image (varies by resolution).

**Key characteristics:** Turbo variant uses DMD+RL distillation for ~8-step inference (6x faster than base). Good Chinese text rendering. 8B parameter Diffusion Transformer backbone.

---

## Provider 2: Alibaba Bailian — wan2.7-image-pro

**Platform:** Alibaba DashScope (阿里云百炼)  
**Config path:** `alibaba_bailian.api_key`  
**Docs:** https://www.alibabacloud.com/help/en/model-studio/wan-image-generation-and-editing-api-reference

**Endpoint:** `POST https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation`

**Curl command (async — need to poll):**
```bash
API_KEY=$(jq -r '.alibaba_bailian.api_key' /Users/lemonade/.claude/skills/scientific-figure/config.local.json)

# Step 1: Submit generation task
TASK_RESPONSE=$(curl -s -X POST "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "wan2.7-image-pro",
    "input": {
      "messages": [
        {
          "role": "user",
          "content": [
            {"text": "<DISTILLED_PROMPT>"}
          ]
        }
      ]
    },
    "parameters": {
      "size": "1K",
      "n": 1,
      "watermark": false,
      "thinking_mode": true
    }
  }')

TASK_ID=$(echo "$TASK_RESPONSE" | jq -r '.output.task_id')

# Step 2: Poll for completion (max 120s)
TASK_URL=$(jq -r '.alibaba_bailian.task_url' /Users/lemonade/.claude/skills/scientific-figure/config.local.json)
STATUS="PENDING"
while [ "$STATUS" = "PENDING" ] || [ "$STATUS" = "RUNNING" ]; do
  sleep 3
  POLL_RESPONSE=$(curl -s "https://dashscope.aliyuncs.com/api/v1/tasks/${TASK_ID}" \
    -H "Authorization: Bearer $API_KEY")
  STATUS=$(echo "$POLL_RESPONSE" | jq -r '.output.task_status')
done

# Step 3: Download when SUCCEEDED
if [ "$STATUS" = "SUCCEEDED" ]; then
  IMAGE_URL=$(echo "$POLL_RESPONSE" | jq -r '.output.results[0].url')
  curl -s -o "001_r1_wan.png" "$IMAGE_URL"
fi
```

**Parameters:**

| Parameter | Options | Guidance |
|-----------|---------|----------|
| `size` | `"1K"`, `"2K"`, `"4K"` | Use `"1K"` per user requirement |
| `n` | 1–4 (1–12 sequential) | Use `1` for cost efficiency |
| `thinking_mode` | `true`/`false` | Enables reasoning-driven generation for complex prompts |
| `watermark` | `true`/`false` | Set `false` for publication figures |
| `enable_sequential` | `true`/`false` | Image-set mode, leave default |

**Response (initial task creation):**
```json
{
  "output": {
    "task_id": "xxx",
    "task_status": "PENDING"
  },
  "request_id": "xxx"
}
```

**Cost:** ~$0.02–0.06/image at 1K.

**Key characteristics:** Highest ceiling of the 3 Bailian models (4K max). Thinking mode adds reasoning for complex spatial instructions. **Hybrid sync/async:** may return a direct image URL (sync `choices` response) or a `task_id` (async) depending on generation speed. Always check the response format — if `output.choices` is present with an image URL, download directly without polling. 500 free images for new users.

---

## Provider 3: Alibaba Bailian — qwen-image-2.0

**Platform:** Alibaba DashScope (阿里云百炼)  
**Config path:** `alibaba_bailian.api_key`  
**Docs:** https://www.alibabacloud.com/help/en/model-studio/qwen-image-api

**Endpoint:** `POST https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation`

**Curl command (sync):**
```bash
API_KEY=$(jq -r '.alibaba_bailian.api_key' /Users/lemonade/.claude/skills/scientific-figure/config.local.json)

curl -s -X POST "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-image-2.0",
    "input": {
      "messages": [
        {
          "role": "user",
          "content": [
            {"text": "<DISTILLED_PROMPT>"}
          ]
        }
      ]
    },
    "parameters": {
      "size": "1024*1024",
      "n": 1,
      "prompt_extend": true,
      "negative_prompt": "blurry, low quality, distorted, watermark, text artifacts, jpeg artifacts, deformed, ugly",
      "watermark": false,
      "seed": null
    }
  }' > .claude/sf_qwen_response.json
```

**Parameters:**

| Parameter | Options | Guidance |
|-----------|---------|----------|
| `size` | `W*H` pixel string | Use `1024*1024` for 1K square, `1280*720` for 16:9, `720*1280` for 9:16. Total pixels: 512²–2048² |
| `n` | 1–6 | Use `1` for cost efficiency |
| `prompt_extend` | `true`/`false` | Smart prompt rewriting — set `false` to preserve exact distilled prompt |
| `negative_prompt` | free text | Always include quality negatives |
| `seed` | int or `null` | Set for reproducibility |
| `watermark` | `true`/`false` | Set `false` for publication |

**Recommended resolutions for 1K-equivalent:**

| Aspect Ratio | Size String |
|-------------|------------|
| 1:1 | `1024*1024` |
| 16:9 | `1280*720` |
| 9:16 | `720*1280` |

**Response (sync):**
```json
{
  "output": {
    "choices": [
      {
        "message": {
          "content": [
            {"image": "https://dashscope.aliyuncs.com/..."}
          ]
        }
      }
    ]
  },
  "usage": { "image_count": 1 }
}
```

**Post-processing:**
```bash
IMAGE_URL=$(jq -r '.output.choices[0].message.content[0].image' .claude/sf_qwen_response.json)
curl -s -o "001_r1_qwen.png" "$IMAGE_URL"
```

**Cost:** ~$0.02–0.06/image. 500 free images for new users.

**Key characteristics:** Best Chinese/English bilingual text rendering among all providers. `prompt_extend: false` recommended to preserve the distilled prompt exactly for cross-model comparison.

---

## Provider 4: Alibaba Bailian — z-image-turbo

**Platform:** Alibaba DashScope (阿里云百炼)  
**Config path:** `alibaba_bailian.api_key`  
**Docs:** https://www.alibabacloud.com/help/en/model-studio/z-image-api-reference

**Endpoint:** `POST https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation`

**Curl command (sync, fastest):**
```bash
API_KEY=$(jq -r '.alibaba_bailian.api_key' /Users/lemonade/.claude/skills/scientific-figure/config.local.json)

curl -s -X POST "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "z-image-turbo",
    "input": {
      "messages": [
        {
          "role": "user",
          "content": [
            {"text": "<DISTILLED_PROMPT>"}
          ]
        }
      ]
    },
    "parameters": {
      "size": "1024*1024",
      "prompt_extend": false
    }
  }' > .claude/sf_zimage_response.json
```

**Parameters:**

| Parameter | Options | Guidance |
|-----------|---------|----------|
| `size` | `W*H` pixel string | `1024*1024` for 1K square, `1280*720` for 16:9, `720*1280` for 9:16 |
| `prompt_extend` | `true`/`false` | Set `false` to preserve exact prompt for fair comparison |
| `n` | fixed 1 | Not configurable |

**Recommended resolutions:**

| Aspect Ratio | 1024² Series | 1280² Series |
|-------------|-------------|-------------|
| 1:1 | `1024*1024` | `1280*1280` |
| 16:9 | `1280*720` | — |
| 9:16 | `720*1280` | — |

**Response:** Same format as qwen-image-2.0 (see above).

**Post-processing:**
```bash
IMAGE_URL=$(jq -r '.output.choices[0].message.content[0].image' .claude/sf_zimage_response.json)
curl -s -o "001_r1_zimage.png" "$IMAGE_URL"
```

**Cost:** ~$0.01–0.03/image (most affordable of the 6).

**Key characteristics:** Fastest generation speed among all 6 providers. Strongest portrait/face realism. Fixed single-image output. No image editing support. Best for rapid iteration rounds.

---

## Provider 5: API MART — gemini-3-pro-image-preview (Nano Banana Pro)

**Platform:** API MART (OpenAI-compatible proxy to Google Gemini)  
**Config path:** `apimart.api_key`  
**Docs:** https://docs.apimart.ai/cn/api-reference/images/gemini-3-pro/generation

**⚠️ Async:** Returns `task_id` on submit; must poll `GET /v1/tasks/{task_id}` for results.

**Endpoint:** `POST https://api.apimart.ai/v1/images/generations`

**Step 1 — Submit generation task:**
```bash
API_KEY=$(jq -r '.apimart.api_key' /Users/lemonade/.claude/skills/scientific-figure/config.local.json)

TASK_RESPONSE=$(curl -s -X POST "https://api.apimart.ai/v1/images/generations" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "prompt": "<DISTILLED_PROMPT>",
    "size": "<ASPECT_RATIO>",
    "n": 1,
    "resolution": "1K"
  }')

TASK_ID=$(echo "$TASK_RESPONSE" | jq -r '.data[0].task_id')
```

**Step 2 — Poll for completion (max 120s):**
```bash
STATUS="submitted"
while [ "$STATUS" = "submitted" ] || [ "$STATUS" = "processing" ]; do
  sleep 5
  POLL_RESPONSE=$(curl -s "https://api.apimart.ai/v1/tasks/${TASK_ID}" \
    -H "Authorization: Bearer $API_KEY")
  STATUS=$(echo "$POLL_RESPONSE" | jq -r '.data.status')
done
```

**Step 3 — Download when completed:**
```bash
if [ "$STATUS" = "completed" ]; then
  IMAGE_URL=$(echo "$POLL_RESPONSE" | jq -r '.data.result.images[0].url[0]')
  curl -s -o "001_r1_gemini.png" "$IMAGE_URL"
fi
```

**Parameters:**

| Parameter | Options | Guidance |
|-----------|---------|----------|
| `model` | `gemini-3-pro-image-preview` | Required |
| `prompt` | string | The distilled prompt |
| `size` | `"1:1"`, `"16:9"`, `"9:16"`, `"2:3"`, `"3:2"`, `"3:4"`, `"4:3"`, `"4:5"`, `"5:4"`, `"21:9"` | Aspect ratio (not resolution!) |
| `n` | 1–4 | Use `1` for cost efficiency |
| `resolution` | `"1K"`, `"2K"`, `"4K"` | Output resolution (separate from `size`) |
| `official_fallback` | `true`/`false` | Use `true` to enable official channel fallback |
| `image_urls` | array of URLs/base64 | Optional reference images (max 14) |

**Response (task creation):**
```json
{
  "code": 200,
  "data": [
    {
      "status": "submitted",
      "task_id": "task_01K8SGYNNNVBQTXNR4MM964S7K"
    }
  ]
}
```

**Response (polling, when completed):**
```json
{
  "code": 200,
  "data": {
    "id": "task_xxx",
    "status": "completed",
    "progress": 100,
    "result": {
      "images": [
        {
          "url": ["https://upload.apimart.ai/f/image/xxx.png"],
          "expires_at": 1776835126
        }
      ]
    }
  }
}
```

**Post-processing:** Extract `data.result.images[0].url[0]` and download. Image URLs expire 24h after completion.

**Cost:** ~$0.03–0.08/image at 1K (via API MART proxy pricing).

**Key characteristics:** Reasoning-driven generation (Google Gemini backbone). Strong multi-image reference editing. SynthID + C2PA watermarking. Good for complex scenes requiring compositional reasoning. Supports up to 14 reference images for editing/consistency tasks. Async only — requires polling. Set `User-Agent` header (not default Python-urllib) to avoid 403 blocks.

---

## Provider 6: API MART — GPT-Image-2

**Platform:** API MART (OpenAI-compatible proxy to OpenAI GPT-Image-2)  
**Config path:** `apimart.api_key`  
**Docs:** https://docs.apimart.ai/cn/api-reference/images/

**⚠️ Async:** Returns `task_id` on submit; must poll `GET /v1/tasks/{task_id}` for results.

**Endpoint:** `POST https://api.apimart.ai/v1/images/generations`

**Step 1 — Submit generation task:**
```bash
API_KEY=$(jq -r '.apimart.api_key' /Users/lemonade/.claude/skills/scientific-figure/config.local.json)

TASK_RESPONSE=$(curl -s -X POST "https://api.apimart.ai/v1/images/generations" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2",
    "prompt": "<DISTILLED_PROMPT>",
    "n": 1,
    "size": "<ASPECT_RATIO>",
    "resolution": "1k"
  }')

TASK_ID=$(echo "$TASK_RESPONSE" | jq -r '.data[0].task_id')
```

**Step 2 — Poll for completion (max 120s):**
```bash
STATUS="submitted"
while [ "$STATUS" = "submitted" ] || [ "$STATUS" = "processing" ]; do
  sleep 5
  POLL_RESPONSE=$(curl -s "https://api.apimart.ai/v1/tasks/${TASK_ID}" \
    -H "Authorization: Bearer $API_KEY")
  STATUS=$(echo "$POLL_RESPONSE" | jq -r '.data.status')
done
```

**Step 3 — Download when completed:**
```bash
if [ "$STATUS" = "completed" ]; then
  IMAGE_URL=$(echo "$POLL_RESPONSE" | jq -r '.data.result.images[0].url[0]')
  curl -s -o "001_r1_gptimage2.png" "$IMAGE_URL"
fi
```

**Parameters:**

| Parameter | Options | Guidance |
|-----------|---------|----------|
| `model` | `gpt-image-2` | Required |
| `prompt` | string | The distilled prompt |
| `size` | `"1:1"`, `"16:9"`, `"9:16"`, `"3:2"`, `"2:3"`, `"4:3"`, `"3:4"`, `"5:4"`, `"4:5"`, `"21:9"`, `"9:21"`, `"2:1"`, `"1:2"`, `"auto"` | Aspect ratio (not resolution!) |
| `n` | 1 | Single image |
| `resolution` | `"1k"`, `"2k"`, `"4k"` | Output resolution (lowercase k). 4K only for 16:9/9:16/2:1/1:2/21:9/9:21 |
| `official_fallback` | `true`/`false` | Use `true` to enable official channel fallback |
| `image_urls` | array of URLs/base64 | Optional reference images (max 16) |

**Response (task creation):**
```json
{
  "code": 200,
  "data": [
    {
      "status": "submitted",
      "task_id": "task_01KPQ7J7DWB7QZ3WCEK3YVPBRA"
    }
  ]
}
```

**Response (polling, when completed):**
```json
{
  "code": 200,
  "data": {
    "id": "task_xxx",
    "status": "completed",
    "progress": 100,
    "result": {
      "images": [
        {
          "url": ["https://upload.apimart.ai/f/image/xxx.png"],
          "expires_at": 1776835126
        }
      ]
    }
  }
}
```

**Post-processing:** Extract `data.result.images[0].url[0]` and download. Image URLs expire 24h after completion.

**Cost:** ~$0.04–0.12/image at 1K (via API MART proxy pricing, varies by resolution).

**Key characteristics:** Near-perfect text rendering (natively integrated into GPT-4o autoregressive architecture). Deep world knowledge for accurate scientific depictions. Best for figures with precise label requirements. Supports transparent backgrounds in PNG format. Async only — requires polling. Set `User-Agent` header (not default Python-urllib) to avoid 403 blocks.

---

## Parallel Execution — `generate_images.py`

**Phase 8E uses `generate_images.py`** (stdlib only, zero dependencies) instead of inline Bash. The script is at:

```
/Users/lemonade/.claude/skills/scientific-figure/generate_images.py
```

### Why Python instead of Bash

| Bash (v1) | Python (v2) |
|-----------|-------------|
| Inline JSON string interpolation breaks on special characters | Proper `json.dumps()` serialization |
| `sleep 30` / `sleep 15` hardcoded waits | `ThreadPoolExecutor` with 5s adaptive polling |
| One error pollutes shared shell state | Isolated per-provider exception handling |
| Raw API JSON dumped to stdout → context bloat | Minimal JSON summary only |
| Temp files in `/tmp/` — permission issues on macOS | Prompt read from `.claude/prompt_cache/`, outputs to working directory |

### Invocation

```bash
python3 /Users/lemonade/.claude/skills/scientific-figure/generate_images.py \
  --prompt-file .claude/prompt_cache/distilled_prompt_[ID].txt \
  --providers ernie,qwen,gemini \
  --output-prefix [ID]_r[N] \
  --aspect-ratio 1:1 \
  --workdir .
```

### Provider class design (6 classes, normalized schemas)

Each provider is a Python class inheriting from `Provider`:

| Class | Slug | Platform | Sync/Async | Size format |
|-------|------|----------|------------|-------------|
| `ErnieProvider` | `ernie` | baidu | Sync | `1024x1024` (WxH) |
| `WanProvider` | `wan` | bailian | Hybrid | `"1K"` (preset) |
| `QwenProvider` | `qwen` | bailian | Sync | `1024*1024` (W*H) |
| `ZImageProvider` | `zimage` | bailian | Sync | `1024*1024` (W*H) |
| `GeminiProvider` | `gemini` | apimart | Async | `"1:1"` (AR) + `"1K"` (res) |
| `GptImage2Provider` | `gptimage2` | apimart | Async | `"1:1"` (AR) + `"1k"` (res) |

Each class encapsulates: `build_payload()`, `build_headers()`, `extract_image_url()`, `extract_task_id()`, `poll_url()`, `is_terminal_status()`, `is_success_status()`.

### Output format (minimal JSON)

```json
{
  "prompt_id": "003_r1",
  "aspect_ratio": "1:1",
  "total": 3,
  "success": 3,
  "failed": 0,
  "providers": {
    "ernie":  {"provider": "ernie",  "status": "success", "output": "003_r1_ernie.png", "path": "/abs/path/003_r1_ernie.png"},
    "qwen":   {"provider": "qwen",   "status": "success", "output": "003_r1_qwen.png", "path": "/abs/path/003_r1_qwen.png"},
    "gemini": {"provider": "gemini", "status": "success", "output": "003_r1_gemini.png", "path": "/abs/path/003_r1_gemini.png"}
  }
}
```

Failed providers appear with `"status": "failed"` or `"status": "timeout"` and an `"error"` field.

### Individual provider curl examples (for manual debugging only)

The curl commands below are retained for reference and manual debugging. **Production generation uses `generate_images.py`.** When testing individual endpoints manually, write temp responses to `.claude/` not `/tmp/`:

---

## Cross-Model Comparison Dimensions

After all images are generated, evaluate across these 5 dimensions:

| Dimension | What to Check | Best Provider (Typical) |
|-----------|--------------|------------------------|
| **Spatial accuracy** | Did the layout instructions survive? | GPT-Image-2, wan2.7 (thinking mode) |
| **Style fidelity** | Does the output match the selected style? | qwen-image-2.0 (exact prompt preservation) |
| **Scientific accuracy** | Are structures/connections plausible? | GPT-Image-2, gemini-3-pro |
| **Text quality** | Clean labels, minimal garbled text? | qwen-image-2.0, GPT-Image-2 |
| **Overall impact** | Which communicates the message best? | Subjective — compare all |

---

## Provider Availability Check

In Phase 8A, read `config.local.json` and check which API keys are non-empty. Present available providers for user selection.

If the config file is missing or all keys are empty:
> "No API keys found in `config.local.json`. Please add your keys to:
> `/Users/lemonade/.claude/skills/scientific-figure/config.local.json`
>
> See the `config.local.json` structure in this reference file."

---

## Common Error Handling

| Error | Likely Cause | Action |
|-------|-------------|--------|
| `401 Unauthorized` | Invalid/expired API key | Verify key in `config.local.json` |
| `429 Too Many Requests` | Rate limit exceeded | Wait 30s, retry that provider once |
| `400 Bad Request` | Prompt too long or invalid size | Check size format (each model different); truncate prompt if >4000 chars |
| ERNIE invalid size | Unsupported resolution string | ERNIE only accepts 7 fixed sizes; remap to closest match. Also check that `X-Client-Platform: aistudio` header is set. |
| Bailian `PENDING` stuck | Async task not completing | Poll up to 120s; if still PENDING, report as timeout |
| API MART `400` on size | `"1K"` passed to `size` instead of aspect ratio | Gemini/GPT-Image-2: `size` must be aspect ratio like `"1:1"`; use `resolution` for quality |
| API MART `content_filter` | Safety filter triggered | Remove medical gore, explicit anatomy, drug references |
| API MART task stuck at `submitted` | Async task not completing | Poll up to 120s (5s intervals); if still stuck, report as timeout |
| API MART `task not found` | Task expired from database | Task retention is limited; re-submit the generation |
| API MART `payment_required` (402) | Account balance empty | Top up at https://apimart.ai/keys |
| wan2.7 returned sync (choices) | Fast generation returned image directly | Handle both sync (`output.choices`) and async (`output.task_id`) response formats |
| API MART `403` (code 1010) | Blocked User-Agent or missing `official_fallback` | Set `User-Agent: scientific-figure/2.0` header; add `"official_fallback": true` to payload |
| Bailian `task_id` null | Sync model used async workflow | wan2.7-image-pro is async; qwen/z-image are sync — use correct mode |
| wan2.7 poll timeout | Model under high load | Offer retry; consider using sync alternatives (qwen/z-image) |
