# Scientific Figure Generator

A **two-layer Prompt Compiler** for generating scientific figures using multiple AI image generation models. This is a [Claude Code](https://claude.ai/code) skill that compiles natural language descriptions of scientific concepts into optimized image-generation prompts, then dispatches them to multiple providers in parallel for cross-model comparison.

## Architecture

```
                    +-----------------------------------+
                    |  LAYER 1: DECISION ENGINE          |
                    |  (Phases 0-7, model-agnostic)      |
                    |                                    |
USER INPUT --------->| Phase 0: Intake                  |
                    | Phase 1: Auto-Analysis            |
                    | Phase 2: Discipline Selection     |----> Output:
                    | Phase 3: Narrative Mode           |      - distilled prompt
                    | Phase 4: Style Selection          |      - layout type
                    | Phase 5: Auto Layout              |      - style
                    | Phase 6: Prompt Construction      |      - aspect ratio
                    | Phase 7: Prompt Distillation      |
                    +---------------++------------------+
                                    ||
                                    vv
                    +-----------------------------------+
                    |  LAYER 2: IMAGE PROVIDERS          |
                    |  (Phase 8, multi-model parallel)   |
                    |                                    |
    distilled ------>|  User selects N providers         |
    prompt          |  +- ERNIE-Image-Turbo (Baidu)     |
                    |  +- wan2.7-image-pro (Bailian)    |----> Output:
                    |  +- qwen-image-2.0 (Bailian)      |      [ID]_[round]_[prov].png
                    |  +- z-image-turbo (Bailian)       |      for cross-model comparison
                    |  +- gemini-3-pro-image (API MART) |
                    |  +- GPT-Image-2 (API MART)        |
                    +-----------------------------------+
```

**Layer 1** is model-agnostic — it compiles user intent into an optimized prompt without coupling to any specific provider. **Layer 2** takes that distilled prompt and sends it to user-selected models in parallel, enabling scientific evaluation of which model renders the concept best.

## Supported Image Providers

| Provider | Model | API Gateway |
|---|---|---|
| Baidu AI Studio | ERNIE-Image-Turbo | Baidu |
| Alibaba Bailian | wan2.7-image-pro | DashScope |
| Alibaba Bailian | qwen-image-2.0 | DashScope |
| Alibaba Bailian | z-image-turbo | DashScope |
| API MART | gemini-3-pro-image-preview | api.apimart.ai |
| API MART | GPT-Image-2 | api.apimart.ai |

## File Structure

```
scientific-figure/
  SKILL.md                          # Main skill definition & workflow (Phases 0-8)
  generate_images.py                # Parallel image generator (stdlib only)
  references/
    discipline-library.md           # Scientific discipline taxonomy & style mappings
    style-library.md                # Visual style catalog with examples
    quality-standards.md            # Figure quality criteria & audit checklist
    api-integration.md              # API endpoint specifications for each provider
    narrative-composer.md           # Narrative mode templates (abstract, method, etc.)
    layout-engine.md                # Layout type taxonomy & composition rules
    prompt-distillation.md          # Prompt optimization & compression strategies
  config.local.json                 # API keys (gitignored, user-provided)
  state.json                        # Prompt ID counter & round tracking (gitignored)
```

## Quick Start

1. Copy this directory into your Claude Code skills folder:

   ```
   ~/.claude/skills/scientific-figure/
   ```

2. Configure your API keys in `config.local.json`:

   ```json
   {
     "baidu_ai_studio": {
       "api_key": "<your-baidu-api-key>",
       "base_url": "https://aistudio.baidu.com/llm/lmapi/v3/images/generations"
     },
     "alibaba_bailian": {
       "api_key": "<your-bailian-api-key>",
       "base_url": "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation",
       "task_url": "https://dashscope.aliyuncs.com/api/v1/tasks"
     },
     "apimart": {
       "api_key": "<your-apimart-api-key>",
       "base_url": "https://api.apimart.ai/v1/images/generations"
     }
   }
   ```

3. Invoke the skill in Claude Code by describing your figure:

   ```
   /scientific-figure
   Draw a mechanism diagram of a Transformer attention layer with
   multi-head attention, layer norm, and residual connections.
   ```

4. The skill will guide you through discipline selection, style choices, and layout before generating images from your chosen providers.

## Usage via Python Script

You can also call `generate_images.py` directly:

```bash
python generate_images.py \
  --prompt-file .claude/distilled_prompt.txt \
  --providers ernie,qwen,gemini \
  --output-prefix 001_r1 \
  --aspect-ratio 1:1
```

The script has zero dependencies beyond the Python standard library.

## Features

- **Discipline-aware design** — tailors figure style to your field (computer science, biology, chemistry, physics, etc.)
- **7 narrative modes** — abstract, method-overview, architecture, workflow, comparison, taxonomy, and timeline
- **Auto layout engine** — selects optimal layout based on content structure (grid, flow, radial, hierarchical, etc.)
- **Cross-model comparison** — same prompt, multiple backends; evaluate which model renders your concept best
- **Structured output naming** — `[promptID]_[round]_[provider].png` for systematic comparison

## License

This project is licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). See [LICENSE](LICENSE) for the full text.

## Author

**Li Mengde**

- Email: [le875251489@gmail.com](mailto:le875251489@gmail.com)
- GitHub: [@Lemonade](https://github.com/Lemonade)
