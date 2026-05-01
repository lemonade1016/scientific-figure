<img width="1672" height="941" alt="ChatGPT Image 2026年5月1日 04_00_58" src="https://github.com/user-attachments/assets/51064301-34e3-49e7-a8ac-0ee401b806bf" />

<p align="center">
  <img width="120" alt="ChatGPT Image 2026年5月1日 14_03_18" src="https://github.com/user-attachments/assets/756298f9-b50d-42fb-84c3-d903a3f94011" />
</p>

<h1 align="center">Scientific Figure Generator</h1>

<p align="center">
A two-layer Prompt Compiler for generating publication-quality scientific figures.
</p>

<p align="center">
  <img src="https://img.shields.io/github/v/release/yourname/scientific-figure">
  <img src="https://img.shields.io/github/downloads/yourname/scientific-figure/total">
  <img src="https://img.shields.io/badge/license-CC_BY_4.0-blue">
  <img src="https://img.shields.io/badge/platform-Claude_Code-black">
</p>

<p align="center">
  <a href="#why">Why</a> •
  <a href="#features">Features</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#roadmap">Roadmap</a>
</p>

<p align="center">
  <img width="1672" height="941" alt="ChatGPT Image 2026年5月1日 04_00_58" src="https://github.com/user-attachments/assets/51064301-34e3-49e7-a8ac-0ee401b806bf" />=
</p>
---

## Why This Exists

Researchers spend hours wrestling with AI image generators to produce scientific figures. The typical workflow looks like this:

| Your Pain Point | What Actually Happens | How We Solve It |
|---|---|---|
| **Blind prompting** | You type a description into a web UI, hit generate, and hope. No iteration, no guidance, no structure. | **5 interactive phases** that analyze your input, recommend discipline/style/layout, and let you confirm or override — expert guidance without removing your control. |
| **Token waste** | Your carefully written 800-token prompt gets diluted across the model's attention mechanism. Critical constraints buried in paragraph 3 are effectively ignored. | **Two-stage prompt distillation** compresses prompts by 40–60%, converting verbose academic rules into concrete visual vocabulary that image models actually respond to. |
| **Single-model gamble** | You pick one model (Midjourney? DALL·E? Gemini?), generate 4 variants, and settle. No way to know if another model would have nailed it. | **Parallel generation across 6 models** — same distilled prompt, all backends at once. Output filenames follow `[ID]_[round]_[provider].png` for systematic comparison. |
| **Layout guesswork** | You manually describe spatial arrangement ("put X on the left, Y on the right, Z in the middle...") with no guarantee the model understands it. | **Auto Layout Engine** with 6 layout types (Pipeline, Central Hub, Grid, Flow, Radial, Hierarchical), visual weight assignment, and reading-path optimization. |
| **Abstract rule failure** | You write "ensure consistency and readability" — the model doesn't know what that looks like. | **Visual primitive translation** — "consistent entity colors, grayscale-readable palette, ≥30% luminance gap" instead of abstract instructions. |
| **Domain ignorance** | Generic image models don't know biological signaling conventions, ML architecture diagram standards, or chemistry notation. | **8 discipline libraries** with domain-specific visual grammars: protein shapes, arrow semantics, CPK color conventions, layer representations, and more. |
| **No quality baseline** | You have to remember to include every quality requirement in every prompt. | **Built-in quality standards** — the Three-Second Rule, three-tier visual hierarchy, colorblind-safe palettes, and element count discipline are baked into every generation. |

---

## Highlights

<div align="center">

| 🧠 **Guided, Not Blind** | ⚡ **Distill, Don't Waste** | 🔀 **Compare, Don't Settle** |
|---|---|---|
| 5 interactive phases with expert recommendations. You make the decisions; we do the heavy lifting. | 40–60% token reduction. Convert "maintain visual consistency" into `1.5pt uniform strokes, flat 5-color palette, grid-aligned`. | One prompt → 6 models in parallel. Pick the best. Every. Single. Time. |

| 🎯 **Visual Primitives** | 📐 **Auto Layout** | 🧬 **Discipline-Native** |
|---|---|---|
| "Solid arrows=activation, T-bar=inhibition, dashed=indirect" — models understand this. | 6 layout types auto-detected from your description. No manual spatial wrangling. | From biomedical pathways to ML architectures — every field's visual conventions baked in. |

</div>

---

## Architecture

```
                    ┌─────────────────────────────────┐
                    │  LAYER 1: DECISION ENGINE        │
                    │  (Phases 0–7, model-agnostic)    │
                    │                                  │
USER INPUT ────────▶│ Phase 0: Intake                  │
                    │ Phase 1: Auto-Analysis           │
                    │ Phase 2: Discipline Selection    │──▶ Output:
                    │ Phase 3: Narrative Mode          │      • distilled prompt
                    │ Phase 4: Style Selection         │      • layout type
                    │ Phase 5: Auto Layout             │      • style
                    │ Phase 6: Prompt Construction     │      • aspect ratio
                    │ Phase 7: Prompt Distillation     │
                    └──────────────┬──────────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────────┐
                    │  LAYER 2: IMAGE PROVIDERS        │
                    │  (Phase 8, multi-model parallel) │
                    │                                  │
    distilled ─────▶│  User selects N providers        │
    prompt          │  ┌─ ERNIE-Image-Turbo (Baidu)    │
                    │  ├─ wan2.7-image-pro (Bailian)   │──▶ Output:
                    │  ├─ qwen-image-2.0 (Bailian)     │      [ID]_[round]_[prov].png
                    │  ├─ z-image-turbo (Bailian)      │      for cross-model comparison
                    │  ├─ gemini-3-pro-image (API MART)│
                    │  └─ GPT-Image-2 (API MART)       │
                    └─────────────────────────────────┘
```

**Layer 1** is model-agnostic — it compiles user intent into an optimized prompt without coupling to any specific provider. **Layer 2** takes that distilled prompt and sends it to user-selected models in parallel, enabling scientific evaluation of which model renders the concept best.

### The 8-Phase Workflow

| Phase | Name | Type | What Happens |
|---|---|---|---|
| 0 | Intake | 👤 User | Describe your figure — natural language, code, or structured outline |
| 1 | Auto-Analysis | ⚙️ Auto | Detect discipline, narrative mode, layout type, and style fit |
| 2 | Guided Discipline | 👤 User | Confirm or override the recommended scientific field |
| 3 | Narrative Mode | 👤 User | Choose mechanism diagram or graphical abstract mode |
| 4 | Guided Style | 👤 User | Select visual style from discipline-aware recommendations |
| 5 | Auto Layout | ⚙️ Auto | Determine optimal layout type, visual weights, and reading path |
| 6 | Prompt Construction | ⚙️ Auto | Assemble 7-layer full prompt with all constraints |
| 7 | Prompt Distillation | ⚙️ Auto | Compress 40–60% — convert abstract rules to visual vocabulary |
| 8 | Multi-Provider Generation | 👤 User | Select providers, generate in parallel, compare results |

## Features

### Discipline Libraries (8 fields)

Each discipline comes with domain-specific visual conventions, standard element vocabularies, and color standards:

- **Biomedical & Molecular Life Sciences** — signaling cascades, protein complexes, cellular compartments
- **Chemistry, Materials & Nanoscience** — synthesis routes, crystal structures, energy diagrams
- **AI & Computer Science** — neural architectures, data pipelines, attention mechanisms
- **Engineering & Applied Physics** — device schematics, circuit diagrams, MEMS structures
- **Clinical Medicine & Healthcare** — disease mechanisms, treatment workflows, trial designs
- **Environmental, Earth & Climate Sciences** — biogeochemical cycles, ecosystem models, climate feedbacks
- **Physics & Mathematics** — quantum processes, spacetime diagrams, manifold visualizations
- **General Science** — fallback for interdisciplinary or emerging fields

### Visual Styles (5 modes)

- **Classic Vector** — clean, flat, journal-ready (Nature/Cell/Science grade)
- **Hand-Drawn Sketch** — whiteboard/research-notebook aesthetic
- **Minimal Infographic** — high-impact editorial communication
- **Photorealistic 3D Render** — for cover art and press releases
- **Retro Scientific Illustration** — vintage textbook etching style

### Narrative Modes

- **Mechanism Diagram** — explain HOW something works (causal chains, process flows)
- **Graphical Abstract** — convey the key finding in a single compelling composition
- Plus 5 sub-modes: architecture, workflow, comparison, taxonomy, and timeline

### Auto Layout Engine (6 types)

| Layout Type | Best For | Visual Pattern |
|---|---|---|
| Pipeline | Workflows, cascades, sequential processes | Left→right linear flow |
| Central Hub | Framework papers, multi-modal systems | Core surrounded by modules |
| Grid | Comparisons, multi-condition experiments | Matrix arrangement |
| Flow | Cycles, feedback loops, state machines | Directed graph |
| Radial | Hierarchies, phylogenetic trees | Concentric or branching |
| Hierarchical | Taxonomies, organizational structures | Top-down tree |

### Prompt Distillation

The distillation engine compresses the full assembled prompt before sending it to image models. Key transformations:

- **Meta-instruction removal** — delete "you must ensure that..." and "it is important to..."
- **Abstraction → visual vocabulary** — "maintain color semantics" → `consistent entity colors, ≥30% luminance gap`
- **Multi-constraint clustering** — merge related rules into compact visual descriptors
- **Position optimization** — critical constraints placed early where model attention is strongest
- **Structural → spatial** — "grid layout, equal spacing" → `3×2 grid, uniform 24pt gap, left-aligned`

Result: same semantic content, 40–60% fewer tokens, significantly better model adherence.

### Quality Standards (built into every generation)

- **Three-Second Rule** — core mechanism identifiable on first glance
- **Three-Tier Visual Hierarchy** — primary → secondary → tertiary attention sequence
- **Colorblind-Safe** — deuteranopia- and protanopia-compatible palettes
- **Element Count Discipline** — 3–7 structural elements, grouped if needed
- **Single Flow Direction** — consistent left→right or top→bottom

## Supported Image Providers

| Provider | Model | API Gateway |
|---|---|---|
| Baidu AI Studio | ERNIE-Image-Turbo | Baidu |
| Alibaba Bailian | wan2.7-image-pro | DashScope |
| Alibaba Bailian | qwen-image-2.0 | DashScope |
| Alibaba Bailian | z-image-turbo | DashScope |
| API MART | gemini-3-pro-image-preview | api.apimart.ai |
| API MART | GPT-Image-2 | api.apimart.ai |

## Quick Start

### 1. Install

Copy this directory into your Claude Code skills folder:

```
~/.claude/skills/scientific-figure/
```

### 2. Configure API Keys

Edit `config.local.json` (gitignored):

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

You only need to configure the providers you intend to use.

### 3. Generate

Invoke the skill in Claude Code:

```
/scientific-figure
Draw a mechanism diagram of a Transformer attention layer with
multi-head attention, layer norm, and residual connections.
```

The skill will analyze your input, recommend discipline/style/layout, and after confirmation, generate images from your chosen providers in parallel.

### 4. Compare & Iterate

Output files follow `[promptID]_[round]_[provider].png` naming. Compare results across models, refine your description in a new round, and converge on the best figure.

### Standalone Script Usage

You can also call `generate_images.py` directly (zero dependencies beyond Python stdlib):

```bash
python generate_images.py \
  --prompt-file .claude/distilled_prompt.txt \
  --providers ernie,qwen,gemini \
  --output-prefix 001_r1 \
  --aspect-ratio 1:1
```

## File Structure

```
scientific-figure/
  SKILL.md                          # Main skill definition & workflow (Phases 0–8)
  generate_images.py                # Parallel image generator (stdlib only)
  references/
    discipline-library.md           # Scientific discipline taxonomy & style mappings
    style-library.md                # Visual style catalog with examples
    quality-standards.md            # Figure quality criteria & audit checklist
    api-integration.md              # API endpoint specifications for each provider
    narrative-composer.md           # Narrative mode templates
    layout-engine.md                # Layout type taxonomy & composition rules
    prompt-distillation.md          # Prompt optimization & compression strategies
  config.local.json                 # API keys (gitignored, user-provided)
  state.json                        # Prompt ID counter & round tracking (gitignored)
```

## License

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) — see [LICENSE](LICENSE).

## Author

**Li Mengde**

- Email: [le875251489@gmail.com](mailto:le875251489@gmail.com)
- GitHub: [@lemonade1016](https://github.com/lemonade1016)
