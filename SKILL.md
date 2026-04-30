---
name: scientific-figure
description: >-
  Two-layer Prompt Compiler for scientific figures. Layer 1 (Decision
  Engine, Phases 0-7) analyzes user input to produce a distilled prompt,
  layout, style, and aspect ratio. Layer 2 (Image Providers, Phase 8)
  sends the same distilled prompt to user-selected models in parallel:
  ERNIE-Image-Turbo (Baidu), wan2.7-image-pro / qwen-image-2.0 /
  z-image-turbo (Alibaba Bailian), gemini-3-pro-image-preview /
  GPT-Image-2 (API MART). Outputs use [promptID]_[round]_[provider].png
  naming for cross-model comparison. Use when the user asks to 'draw a
  mechanism diagram', 'generate a scientific figure', 'create a
  schematic', 'make a graphical abstract', or provides a paper
  description / model architecture for visualization.
license: CC-BY-4.0
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, WebFetch, AskUserQuestion]
---

# Scientific Figure Generator v2

## Reference files

When this skill mentions `references/xxx.md`, read the file using its absolute path:

- `references/discipline-library.md` → `/Users/lemonade/.claude/skills/scientific-figure/references/discipline-library.md`
- `references/style-library.md` → `/Users/lemonade/.claude/skills/scientific-figure/references/style-library.md`
- `references/quality-standards.md` → `/Users/lemonade/.claude/skills/scientific-figure/references/quality-standards.md`
- `references/api-integration.md` → `/Users/lemonade/.claude/skills/scientific-figure/references/api-integration.md`
- `references/narrative-composer.md` → `/Users/lemonade/.claude/skills/scientific-figure/references/narrative-composer.md`
- `references/layout-engine.md` → `/Users/lemonade/.claude/skills/scientific-figure/references/layout-engine.md`
- `references/prompt-distillation.md` → `/Users/lemonade/.claude/skills/scientific-figure/references/prompt-distillation.md`

**Config & state files (local, gitignored):**
- `config.local.json` → `/Users/lemonade/.claude/skills/scientific-figure/config.local.json` — API keys for all providers
- `state.json` → `/Users/lemonade/.claude/skills/scientific-figure/state.json` — prompt ID counter and round tracking

Always read the relevant reference file(s) when a phase references them.

---

## Architecture Overview

This skill is a **Prompt Compiler** split into two independent layers:

- **Layer 1 — Decision Engine (Phases 0–7):** Takes raw user input and produces a distilled prompt, layout, style, and aspect ratio. This layer is model-agnostic — it compiles user intent into an optimized image-generation prompt without coupling to any specific provider.
- **Layer 2 — Image Providers (Phase 8):** Takes the distilled prompt from Layer 1 and sends it to user-selected models in parallel. This enables cross-model comparison: same prompt, different backends, scientific evaluation of which model renders the concept best.

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

### v2 Improvements over v1

| v1 Problem | v2 Solution | Module |
|------------|-------------|--------|
| Prompt too long, model attention diluted | Two-stage: full prompt → distilled prompt | `prompt-distillation.md` |
| Blind selection (user picks without guidance) | Auto-analysis + expert recommendations | Phase 0–4 (this file) |
| No narrative structure | Mechanism vs Graphical Abstract engine | `narrative-composer.md` |
| No spatial intelligence | Auto Layout Engine (6 types + visual weights) | `layout-engine.md` |
| Single-model output, no comparison | Layer 2: parallel multi-provider generation | `api-integration.md` |

### The 8-Phase Workflow

Phases 0–7 (Layer 1) and Phase 8 (Layer 2):

```
USER INPUT
    │
    ▼
Phase 0: INTAKE ─── Collect raw description/code first
    │
    ▼
Phase 1: AUTO-ANALYSIS ─── Detect discipline, narrative mode, layout type, style fit
    │
    ▼
Phase 2: GUIDED DISCIPLINE ─── Recommendation + alternatives → User confirms
    │
    ▼
Phase 3: NARRATIVE MODE ─── Mechanism vs Graphical Abstract → User confirms
    │
    ▼
Phase 4: GUIDED STYLE ─── Recommendation (discipline-aware) + alternatives → User confirms
    │
    ▼
Phase 5: AUTO LAYOUT ─── Layout type, visual weights, reading path, spacing
    │
    ▼
Phase 6: PROMPT CONSTRUCTION ─── 7-layer full prompt assembly
    │
    ▼
Phase 7: PROMPT DISTILLATION ─── Compress 60% for image model optimization
    │
    ▼
Phase 8: MULTI-PROVIDER GENERATION ─── User selects N providers, parallel generation, comparison
```

**User-facing phases:** 0, 2, 3, 4, 8 (5 interactions)
**System-internal phases:** 1, 5, 6, 7 (automatic)

---

## Phase 0: Intake First

**CRITICAL: Collect the user's raw input BEFORE asking any selection questions.** This enables intelligent recommendations in later phases rather than forcing blind choices.

Ask the user:

> "Please describe what you need. Include as much detail as possible:
> - What is the mechanism, architecture, or concept you want to visualize?
> - What are the key components and their relationships?
> - What is the main message or novel contribution?
> - Where will this figure be used? (journal submission, preprint, graphical abstract, conference presentation, cover art, etc.)
> - If you have a target journal or venue in mind, please mention it.
> 
> You can also paste model architecture code, a structured description, or reference an existing figure."

The user's response may include:
- Natural language mechanism description
- Model architecture code (Python/PyTorch/TensorFlow)
- Structured step-by-step outline
- Target venue information (journal name, preprint server, conference)
- Reference to an existing figure style

### Code-to-Description Translation

If the user provides code, parse it immediately to extract:
1. Module/class names and types (encoder, decoder, attention, FFN, normalization, embedding, etc.)
2. Data flow — input shapes → transformations → output shapes
3. Special connections (skip connections, gating, multi-path routing)
4. Novel/custom components (the paper's contribution)
5. Training vs. inference paths (if distinguishable)

Translate into a natural language description preserving all architectural details. Use standard CS/ML terminology.

---

## Phase 1: Auto-Analysis

Analyze the Phase 0 intake to generate recommendations. Read `references/narrative-composer.md` and `references/layout-engine.md` for detection keywords.

### 1A: Discipline Detection

Scan the user's input for domain-specific keywords. Count matches per discipline.

| Discipline | High-confidence keywords |
|------------|------------------------|
| Biomedical & Molecular Life Sciences | `protein`, `pathway`, `signaling`, `cell`, `receptor`, `gene`, `kinase`, `phosphorylat`, `transcription`, `membrane`, `cytoplasm`, `nucleus`, `ligand`, `immune`, `antibody`, `apoptosis`, `autophagy` |
| Chemistry, Materials & Nanoscience | `synthesis`, `catalyst`, `nanoparticle`, `polymer`, `crystal`, `MOF`, `reaction`, `electrode`, `electrolyte`, `monomer`, `ligand`, `coordination`, `oxidation`, `reduction`, `band gap`, `doping` |
| Artificial Intelligence & Computer Science | `transformer`, `attention`, `neural`, `embedding`, `training`, `inference`, `gradient`, `loss`, `encoder`, `decoder`, `token`, `layer`, `GPU`, `dataset`, `fine-tun`, `LLM`, `agent`, `RL`, `CNN`, `RNN` |
| Engineering & Applied Physics | `device`, `circuit`, `mechanical`, `optical`, `sensor`, `actuator`, `voltage`, `current`, `waveguide`, `resonator`, `transistor`, `diode`, `MEMS`, `thermal`, `fluidic` |
| Clinical Medicine & Healthcare | `patient`, `clinical`, `disease`, `treatment`, `drug`, `surgery`, `diagnosis`, `tumor`, `cancer`, `therapy`, `prognosis`, `biomarker`, `trial`, `dose`, `adverse` |
| Environmental, Earth & Climate Sciences | `climate`, `ecosystem`, `carbon`, `nitrogen`, `geological`, `ocean`, `atmosphere`, `sediment`, `weathering`, `biodiversity`, `emission`, `runoff`, `groundwater`, `tectonic` |
| Physics & Mathematics | `quantum`, `particle`, `wavefunction`, `Hamiltonian`, `Lagrangian`, `spacetime`, `fermion`, `boson`, `manifold`, `topology`, `gauge`, `spin`, `scattering`, `symmetry`, `Feynman` |
| Interdisciplinary & Emerging Fields | Mixed keywords from ≥2 categories above, OR `AI+Science`, `bioinformatic`, `digital twin`, `multi-scale`, `synthetic biology`, `computational biology`, `quantum computing`, `neural engineering` |

Select the discipline with the highest keyword match count. If tied, prefer the one with the most high-confidence matches. If unclear, default to Interdisciplinary.

### 1B: Narrative Mode Detection

Read `references/narrative-composer.md` for the auto-detection logic. Scan for:
- **Graphical Abstract triggers:** `graphical abstract`, `TOC`, `cover`, `summary`, `highlight`, `one figure`
- **Mechanism triggers:** `mechanism`, `pathway`, `process`, `how`, `pipeline`, `architecture`, `workflow`

### 1C: Layout Type Pre-Detection

Read `references/layout-engine.md` Phase 1. Scan for the 6 layout type keywords and compute the best match. Store for Phase 5.

### 1D: Venue Extraction

Scan for venue mentions: journal names (`Nature`, `Cell`, `Science`, `NeurIPS`, `ICML`, `JACS`, `NEJM`, etc.), venue types (`preprint`, `conference`, `journal`, `cover`, `poster`), or explicit statements about the figure's destination.

### Output the Analysis Summary

Present the analysis to the user before proceeding:

> **Auto-Analysis Results:**
> - **Detected discipline:** [Discipline Name] (confidence: [HIGH/MEDIUM/LOW])
> - **Detected narrative mode:** [Mechanism Diagram / Graphical Abstract]
> - **Detected layout type:** [Layout Name]
> - **Target venue:** [Journal/venue name or "Not specified"]
>
> Proceeding to recommendations...

---

## Phase 2: Guided Discipline Selection

Based on the Phase 1 analysis, present a **recommendation** (not just a list) using `AskUserQuestion`.

### Recommendation Logic

- If venue is explicitly mentioned and maps to a known discipline convention → boost that discipline
- If the detected discipline has HIGH confidence → recommend it
- If confidence is MEDIUM or LOW → recommend the top 2 matches, ask user to choose
- Always include the option for the user to override

### Discipline Options Presentation

**Question:** "Confirm the scientific discipline for your figure."

Format each option as: **Discipline Name** — one-line description + "⭐ Recommended for [reason]" on the top match.

Present all 8 categories but mark the recommended one:

1. **Biomedical & Molecular Life Sciences** — Cell biology, molecular biology, genetics, immunology, neuroscience, biochemistry
2. **Chemistry, Materials & Nanoscience** — Chemistry, materials science, nanotechnology, catalysis, polymer science
3. **Artificial Intelligence & Computer Science** — ML, deep learning, NLP, CV, LLMs, AI agents, algorithms
4. **Engineering & Applied Physics** — Mechanical, electrical, civil, chemical, optics, photonics, energy, robotics
5. **Clinical Medicine & Healthcare** — Clinical research, anatomy, pathology, pharmacology, surgery, diagnostics
6. **Environmental, Earth & Climate Sciences** — Ecology, climate science, geology, oceanography, atmospheric science
7. **Physics & Mathematics** — Theoretical physics, quantum mechanics, particle physics, astrophysics, mathematics
8. **Interdisciplinary & Emerging Fields** — Bioinformatics, AI+Science, synthetic biology, digital health, quantum computing

The recommended option(s) should include the label: `⭐ Recommended ([reason in ≤8 words])`

Always end with: "You have the final decision — the recommendation is based on automated keyword analysis and may not capture your full context."

---

## Phase 3: Narrative Mode Selection

Read `references/narrative-composer.md` for the full narrative structures.

Present the detected narrative mode for confirmation using `AskUserQuestion`.

**Question:** "What type of figure story do you want to tell?"

**Options:**

1. **Mechanism Diagram** — Causal chain: Input → Process → Interaction → Output. Explains HOW something works. Best for: pathway diagrams, architecture figures, algorithm flowcharts, process schematics. ⭐ [Recommended if detected]

2. **Graphical Abstract** — Impact arc: Problem → Innovation → Result → Significance. Communicates WHAT was achieved and WHY it matters. Best for: journal TOC images, press-release figures, cover art, social media summaries. ⭐ [Recommended if detected]

Use `AskUserQuestion` with `multiSelect: false`. After selection, read the corresponding narrative prompt block from `references/narrative-composer.md` — this will become Layer N in Phase 6.

If the user has a dual-purpose need (both detailed mechanism AND graphical abstract), offer the Combined Mode described in `references/narrative-composer.md`.

---

## Phase 4: Guided Style Selection

### Style Recommendation Matrix

Based on the confirmed discipline + narrative mode + venue, compute the optimal style recommendation.

**Decision matrix:**

| Scenario | Recommended Style | Reasoning |
|----------|------------------|-----------|
| Venue = traditional journal (Nature/Cell/Science/etc.) + any discipline | **Classic Vector** or **Hybrid** | Editorial acceptance priority |
| Venue = preprint (arXiv/bioRxiv) + any discipline | **Hand-Drawn Sketch** or **Minimal Infographic** | Social media engagement, modern feel |
| Narrative = Graphical Abstract + any discipline | **Minimal Infographic** or **Hybrid** | Communication clarity, thumbnail readability |
| Narrative = Mechanism + AI/CS discipline | **Hand-Drawn Sketch** | Domain trend — AI researchers strongly prefer this |
| Narrative = Mechanism + Biomedical discipline | **Scientific Illustration** or **Classic Vector** | Biological accuracy expected |
| Narrative = Mechanism + Chemistry/Materials discipline | **Classic Vector** or **3D Render** | Clean schematics or molecular visualization |
| Venue = conference presentation/poster | **Futuristic Tech** or **Minimal Infographic** | Visual impact from distance |
| Venue = journal cover art | **3D Render** or **Scientific Illustration** | Maximum visual impact, photorealistic quality |
| Multi-domain interdisciplinary | **Hybrid** | Multi-layered hierarchy needed |
| User wants "modern/trendy/current" | **Hybrid** | Current strongest trend in top journals |

Adjust the recommendation based on any explicit user preference clues in the Phase 0 intake.

### Style Options Presentation

Read `references/style-library.md` for the full style descriptions.

Present using `AskUserQuestion`.

**Question:** "Select the visual style for your figure."

Format with the recommended style marked `⭐ Recommended ([specific reason])` and one style marked `🔄 Alternative ([specific reason])`. The remaining 5 styles are presented without markers.

**Style list:**

1. **Classic Vector — Clean Journal Style** — Crisp outlines, flat colors, geometric precision, modular grid. Gold standard for journal submissions.
2. **Hand-Drawn Sketch — Whiteboard Thinking Style** — Organic wobbly lines, paper texture, varied strokes. Popular in AI/ML, engaging for preprints.
3. **Minimal Infographic — High-Impact Communication Style** — 40%+ whitespace, 2-4 colors, icon-based. Best for graphical abstracts and social media.
4. **Scientific Illustration — Textbook Realism Style** — Semi-realistic biological rendering, soft shading, accurate proportions. Authoritative for biomedical journals.
5. **Futuristic Tech — Cutting-Edge Innovation Style** — Glowing neon, dark background, digital particles. Best for presentations and posters. (Caution: may feel informal for journal submission.)
6. **Hybrid — Multi-Layered Visual Hierarchy Style** — Vector framework + hand-drawn emphasis + illustration context. Current top-tier trend. Best for complex interdisciplinary stories.
7. **3D Render — Photorealistic Depth Style** — Ray-traced lighting, physical materials, cinematic composition. Best for covers and high-impact visuals.

Always end with: "⭐ = system recommendation based on your task. You have the final decision."

---

## Phase 5: Auto Layout Analysis

Read `references/layout-engine.md` for the full layout engine specification.

Execute the layout engine's 4 phases automatically (no user interaction needed):

### 5A: Figure Type Classification

Use the detection keywords and patterns from `references/layout-engine.md` Phase 1 to classify the figure into one of 6 layout types:
1. Pipeline (Sequential Flow)
2. Central Hub (Core Innovation Focus)
3. Layered Stack (Hierarchical Architecture)
4. Biological Spatial (Compartment-Based)
5. Branching Tree (Decision/Classification)
6. Cyclic Loop (Feedback & Cycles)

### 5B: Visual Weight Computation

Extract all named components from the user's input. Score each using the rules in `references/layout-engine.md` Phase 2.

Identify the **highest-weight component** (score 9–10) — this is the figure's visual anchor.

### 5C: Reading Path Assignment

Based on the detected layout type, assign the reading path as specified in `references/layout-engine.md` Phase 3.

### 5D: Layout Prompt Assembly

Assemble the layout instructions using the template in `references/layout-engine.md` Phase 5. This becomes Layer L in Phase 6.

### Output

Briefly inform the user of the layout analysis results:

> **Auto Layout:**
> - Layout type: [Name] — [one-line justification]
> - Visual anchor: [Component name] (weight: [score]/10)
> - Reading path: [Path type]
> - Aspect ratio: [ratio]

---

## Phase 6: Full Prompt Construction

Read `references/quality-standards.md` before constructing the prompt.
Read `references/discipline-library.md` to load the confirmed discipline prompt.
Read `references/style-library.md` to load the confirmed style prompt.
Read `references/narrative-composer.md` to load the confirmed narrative prompt.

### 7-Layer Assembly Architecture

```
LAYER 1: Role & Persona Framing
LAYER 2: Discipline-Specific Conventions
LAYER 3: Style-Specific Aesthetic Instructions
LAYER 4: Auto-Layout Spatial Instructions  ← NEW
LAYER 5: Narrative Structure               ← NEW
LAYER 6: Top-Tier Quality Standards
LAYER 7: User's Specific Content
```

### Layer Assembly

**Layer 1 — Role:**
> "You are an expert scientific illustrator with 20 years of experience creating publication-quality mechanism diagrams for [CONFIRMED DISCIPLINE]. You are preparing a figure for [VENUE or 'a top-tier journal']. Your illustrations have won multiple scientific visualization awards. You combine deep domain knowledge with exceptional visual design skills. Scientific accuracy and clarity are paramount — aesthetics serve understanding, never the reverse."

**Layer 2 — Discipline:** Load the confirmed discipline's prompt block from `references/discipline-library.md`. Include verbatim.

**Layer 3 — Style:** Load the confirmed style's prompt block from `references/style-library.md`. Include verbatim.

**Layer 4 — Layout:** Use the layout prompt block assembled in Phase 5D. Include verbatim.

**Layer 5 — Narrative:** Load the confirmed narrative mode's prompt block from `references/narrative-composer.md`. Include verbatim.

**Layer 6 — Quality:** Load the full quality standards prompt from `references/quality-standards.md`. Include verbatim.

**Layer 7 — User Content:**
> "USER'S SPECIFIC CONTENT: The figure must depict the following specific mechanism:
> [USER'S RAW DESCRIPTION OR PARSED CODE DESCRIPTION]
> 
> KEY COMPONENTS:
> - [Component 1] (visual weight: [score]/10) — [role in mechanism]
> - [Component 2] (visual weight: [score]/10) — [role in mechanism]
> - [...]
> 
> RELATIONSHIPS: [extracted causal/logical relationships between components]
> MAIN MESSAGE: [extracted or inferred core insight — the one thing the viewer must understand]"

### Write the Full Prompt (Silent)

**CRITICAL: Do NOT print the full prompt to stdout.** It is ~1,000–1,400 words — dumping it into the conversation context wastes thousands of tokens. Instead, write it silently to a cache file.

Write the complete assembled prompt to:
```
.claude/prompt_cache/full_prompt_[promptID].txt
```

Use `Write` to save the file silently (no path echo). Then tell the user:

> "Full prompt assembled ([N] words, 7 layers). Written to `.claude/prompt_cache/full_prompt_[ID].txt`. Would you like to review or adjust any layer before I distill and generate? (You can open the file to inspect.)"

---

## Phase 7: Prompt Distillation

Read `references/prompt-distillation.md` for the full distillation methodology.

### Distillation Process

1. Apply **Phase 1 transformations** (Rule → Visual Descriptor) from the distillation reference:
   - Remove meta-instructions and preambles
   - Convert abstract rules to concrete visual descriptors
   - Cluster multi-constraint rules into keyword groups
   - Translate structural rules to spatial descriptors

2. Apply **Phase 2 priority ordering**:
   - Style identity + Layout type → FIRST (first 15% of prompt)
   - Key visual constraints + Core elements → HIGH (next 20%)
   - Discipline conventions + Secondary elements → MEDIUM (next 30%)
   - Quality standards (compressed) + Fine details → LOWER (next 25%)
   - Negative constraints → LAST (final 10%)

3. **Verify constraint preservation** — check that all 6 critical constraints survived:
   - ✅ Color accessibility (deuteranopia-safe)
   - ✅ Arrow semantics (consistent types, not ambiguous)
   - ✅ Visual hierarchy (3 distinct levels)
   - ✅ Reading path (unambiguous flow)
   - ✅ Scientific accuracy markers (hypothetical = dashed)
   - ✅ Style identity preserved (not degraded by compression)

### Write Both Versions (Silent)

**CRITICAL: Do NOT print prompts to stdout.** Both the full prompt and the distilled prompt must be written to disk silently — never dumped into the conversation context. Each prompt is hundreds of words; printing them wastes thousands of input tokens.

Write both files silently using `Write`:

1. Full prompt → `.claude/prompt_cache/full_prompt_[promptID].txt` (already written in Phase 6)
2. Distilled prompt → `.claude/prompt_cache/distilled_prompt_[promptID].txt`

After writing, tell the user:

> "Distilled prompt ready ([M] words, ~[X]% compression). Full prompt ([N] words) and distilled prompt both saved to `.claude/prompt_cache/`. Use the ⚡ distilled prompt for generation? (Recommended — better model attention.) Or would you prefer the full 📝 prompt?"

**Default:** Use the distilled prompt. The full prompt is for human review; the distilled prompt is for the image model.

---

## Phase 8: Multi-Provider Image Generation (Layer 2)

Read `references/api-integration.md` for endpoint details and curl commands for all 6 providers.

This phase is **Layer 2: Image Providers** — it takes the distilled prompt from Layer 1 (Phases 0–7) and sends it to user-selected models in parallel. All providers receive the **same distilled prompt**, enabling scientific cross-model comparison.

### File Naming Convention

All generated images follow a unified naming scheme:

```
[promptID]_[round]_[provider].png
```

| Field | Source | Format | Example |
|-------|--------|--------|--------|
| `promptID` | Auto-incremented from `state.json` | 3-digit zero-padded | `001`, `002` |
| `round` | `state.json` current_round | `r` + number | `r1`, `r2` |
| `provider` | Short slug per model | lowercase | `ernie`, `wan`, `qwen`, `zimage`, `gemini`, `gptimage2` |

**Provider slugs:**

| Model | Slug | Filename Example |
|-------|------|-----------------|
| ERNIE-Image-Turbo | `ernie` | `001_r1_ernie.png` |
| wan2.7-image-pro | `wan` | `001_r1_wan.png` |
| qwen-image-2.0 | `qwen` | `001_r1_qwen.png` |
| z-image-turbo | `zimage` | `001_r1_zimage.png` |
| gemini-3-pro-image-preview | `gemini` | `001_r1_gemini.png` |
| GPT-Image-2 | `gptimage2` | `001_r1_gptimage2.png` |

**Round tracking:** Read `state.json` at the start of Phase 8. If this is a new prompt (different from `current_prompt_id`), increment `next_prompt_id`, set `current_prompt_id` to the new ID, and reset `current_round` to 1. If regenerating the same prompt, increment `current_round`. Write back to `state.json` after.

### 8A: Provider Availability Scan

Read API keys from `config.local.json` (absolute path: `/Users/lemonade/.claude/skills/scientific-figure/config.local.json`). Check which platform keys are non-empty:

| Platform | Config Key | Models Available |
|----------|-----------|-----------------|
| Baidu AI Studio | `baidu_ai_studio.api_key` | `ernie-image-turbo` |
| Alibaba Bailian | `alibaba_bailian.api_key` | `wan2.7-image-pro`, `qwen-image-2.0`, `z-image-turbo` |
| API MART | `apimart.api_key` | `gemini-3-pro-image-preview`, `gpt-image-2` |

If config file is missing or all keys are empty:
> "No API keys found in `config.local.json`. Add your keys to:
> `/Users/lemonade/.claude/skills/scientific-figure/config.local.json`
>
> See the config structure in `references/api-integration.md`. The distilled prompt is shown above — you can copy it to any image generation tool."

### 8B: Provider Selection

Present all available models using `AskUserQuestion` with `multiSelect: true`.

**Question:** "Select image generation models to use. Choose one or more — selecting multiple enables cross-model comparison of the same distilled prompt."

**Options (dynamically generated from available platforms):**

| # | Model | Platform | Strength | Cost Est. |
|---|-------|----------|----------|-----------|
| 1 | ERNIE-Image-Turbo | Baidu AI Studio | Fast Turbo, strong Chinese text | $0.01–0.03 |
| 2 | wan2.7-image-pro | Alibaba Bailian | 4K max, thinking mode | $0.02–0.06 |
| 3 | qwen-image-2.0 | Alibaba Bailian | Best bilingual text rendering | $0.02–0.06 |
| 4 | z-image-turbo | Alibaba Bailian | Fastest generation, portraits | $0.01–0.03 |
| 5 | gemini-3-pro-image-preview | API MART | Reasoning-driven, multi-ref | $0.03–0.08 |
| 6 | GPT-Image-2 | API MART | Near-perfect text, world knowledge | $0.04–0.12 |

For each option, show the description. Only show models whose parent platform key is configured. If a platform key is missing, show all its models as `⚠️ Not configured (add key to config.local.json → [platform_key])`.

**Suggestion:** For a meaningful cross-model comparison, select 3–4 models spanning different platforms.

### 8C: Resolution — All Models at 1K

All 6 models support 1K resolution. The exact format varies per model:

| Model | 1K Square (1:1) | 1K Wide (16:9) | 1K Tall (9:16) |
|-------|----------------|----------------|---------------|
| ERNIE-Image-Turbo | `1024x1024` | `1376x768` | `768x1376` |
| wan2.7-image-pro | `"1K"` | `"1K"` | `"1K"` |
| qwen-image-2.0 | `1024*1024` | `1280*720` | `720*1280` |
| z-image-turbo | `1024*1024` | `1280*720` | `720*1280` |
| gemini-3-pro-image-preview | size=`"1:1"`, resolution=`"1K"` | size=`"16:9"`, resolution=`"1K"` | size=`"9:16"`, resolution=`"1K"` |
| GPT-Image-2 | size=`"1:1"`, resolution=`"1k"` | size=`"16:9"`, resolution=`"1k"` | size=`"9:16"`, resolution=`"1k"` |

Map from the Phase 5 layout type to the correct size per model. See `references/api-integration.md` for the full mapping table.

### 8D: Cost Disclosure

Sum the cost across all selected models before generating:

> "**Generation Plan** — Prompt #`[ID]`, Round `r[N]`:
> | # | Model | Platform | Size | Est. Cost |
> |---|-------|----------|------|-----------|
> | 1 | ernie-image-turbo | Baidu | 1024x1024 | $0.02 |
> | 2 | qwen-image-2.0 | Bailian | 1024*1024 | $0.04 |
> | 3 | gpt-image-2 | API MART | 1K | $0.08 |
> | **Total** | | | | **$0.14** |
>
> Output files: `001_r1_ernie.png`, `001_r1_qwen.png`, `001_r1_gptimage2.png`
>
> Proceed with parallel generation?"

### 8E: Parallel Generation (Python Orchestrator)

**All generation is handled by `generate_images.py`** — a stdlib-only Python script with zero external dependencies. It replaces the previous fragile inline Bash orchestration with proper `concurrent.futures` parallelism, error isolation, and structured retry logic.

**Why Python instead of Bash:**
- True concurrent I/O via `ThreadPoolExecutor` — no `sleep 30` guessing
- Proper error isolation — one provider failing doesn't corrupt shared shell state
- Normalized size/aspect-ratio mapping per provider
- Returns a minimal JSON summary instead of dumping raw API responses into context

**Invocation:**

```bash
python3 /Users/lemonade/.claude/skills/scientific-figure/generate_images.py \
  --prompt-file .claude/prompt_cache/distilled_prompt_[ID].txt \
  --providers [comma-separated-slugs] \
  --output-prefix [ID]_r[N] \
  --aspect-ratio [1:1|16:9|9:16] \
  --workdir .
```

**Arguments:**
| Flag | Value | Example |
|------|-------|---------|
| `--prompt-file` | Path to the distilled prompt file (written in Phase 7) | `.claude/prompt_cache/distilled_prompt_003.txt` |
| `--providers` | Comma-separated provider slugs | `ernie,qwen,gemini` |
| `--output-prefix` | `[promptID]_[round]` per naming convention | `003_r1` |
| `--aspect-ratio` | `1:1`, `16:9`, or `9:16` (from Phase 5 layout) | `1:1` |
| `--workdir` | Output directory for `.png` files | `.` (current working directory) |

**Provider slugs for `--providers`:**
`ernie`, `wan`, `qwen`, `zimage`, `gemini`, `gptimage2`

**What the script does internally:**
1. Reads API keys from `config.local.json`
2. Reads the distilled prompt from `--prompt-file`
3. Maps `--aspect-ratio` to each provider's native size format (see 8C table)
4. Fires all selected providers concurrently using `ThreadPoolExecutor`
5. Sync providers (ernie, qwen, zimage) → submit + download in one step
6. Async providers (wan, gemini, gptimage2) → submit, poll every 5s (120s timeout), download
7. Saves images as `[output-prefix]_[slug].png` in `--workdir`
8. Prints a **minimal JSON summary** to stdout — no raw API responses dumped

**Context discipline:** The Python script's stdout is the only thing that enters the LLM context. The script does NOT echo prompts, API keys, or raw JSON responses. The summary format:

```json
{
  "prompt_id": "003_r1",
  "aspect_ratio": "1:1",
  "total": 3,
  "success": 3,
  "failed": 0,
  "providers": {
    "ernie": {"status": "success", "output": "003_r1_ernie.png", "path": "/abs/path/003_r1_ernie.png"},
    "qwen":  {"status": "success", "output": "003_r1_qwen.png", "path": "/abs/path/003_r1_qwen.png"},
    "gemini":{"status": "success", "output": "003_r1_gemini.png", "path": "/abs/path/003_r1_gemini.png"}
  }
}
```

**Error handling:** Failures are isolated per provider. If one provider times out or errors, the others still complete. The JSON summary includes `"status": "failed"` or `"status": "timeout"` with an `"error"` field for each failed provider. Offer retry for failed providers only.

### 8F: Results Presentation

After all images are generated, present results with the unified naming:

> "**Generation Results** — Prompt #`[ID]`, Round `r[N]`, same distilled prompt across [N] models:
>
> | # | Model | Platform | Status | Output |
> |---|-------|----------|--------|--------|
> | 1 | ERNIE-Image-Turbo | Baidu | ✅ | `001_r1_ernie.png` |
> | 2 | qwen-image-2.0 | Bailian | ✅ | `001_r1_qwen.png` |
> | 3 | GPT-Image-2 | API MART | ✅ | `001_r1_gptimage2.png` |
>
> **Cross-model comparison dimensions:**
> 1. **Spatial accuracy:** Which model best followed the layout instructions?
> 2. **Style fidelity:** Which model best captured the [selected style] aesthetic?
> 3. **Scientific accuracy:** Which model avoided hallucinated structures/connections?
> 4. **Text quality:** Which model produced the cleanest labels?
> 5. **Overall impact:** Which figure communicates the core message most effectively?"

If any provider failed, show the error and offer retry for that specific provider.

### 8G: Post-Generation Instructions

After reviewing images:
1. **Select the best output** — different models may excel at different dimensions
2. **Text labels:** Add precise labels in Illustrator/Inkscape/PowerPoint — AI text is unreliable across all providers
3. **Scientific verification:** Verify all details against known domain facts
4. **Color consistency:** Match paper-wide palette
5. **Arrow semantics:** Verify all arrow types are consistent
6. **3-second test:** Show to a colleague unfamiliar with the work
7. **Journal compliance:** Adjust resolution, color space, and font per target journal
8. **Cross-model insight:** Track which model performs best for your discipline/style combination — this feeds into future provider selection

---

## Iteration Support

After generation, offer:
- **Refine prompt:** Adjust specific wording or details, then re-run all (or selected) providers
- **Change style intensity:** "More hand-drawn" / "Less glow"
- **Fix layout:** Move specific elements, add/remove connections
- **Switch style/discipline:** Try a different approach
- **Regenerate:** Same prompt, same providers, different random seed
- **Cross-model iterate:** Keep the best provider's output, regenerate only the underperforming ones after prompt tweaks

---

## Quick Start Example

**User:** "I need a graphical abstract for my paper going to Nature Biotechnology. It's about a new AI model that predicts protein-drug binding affinity using a hybrid graph neural network + transformer architecture."

**Skill flow:**
1. **Phase 0:** Intake collected
2. **Phase 1:** Auto-analysis → Interdisciplinary (AI + Biology keywords), Graphical Abstract (explicit mention), target venue = Nature Biotechnology
3. **Phase 2:** Discipline recommendation: ⭐ Interdisciplinary (AI+Biomed keywords detected)
4. **Phase 3:** Narrative mode: ⭐ Graphical Abstract (explicitly requested)
5. **Phase 4:** Style recommendation: ⭐ Hybrid (best for Nature Biotechnology interdisciplinary GA); Alternative: Minimal Infographic
6. **Phase 5:** Layout: Central Hub (core = novel GNN+Transformer fusion model)
7. **Phase 6:** Full prompt assembled (7 layers)
8. **Phase 7:** Distilled prompt generated (~60% compression)
9. **Phase 8:** User selects 3 models (ERNIE-Image-Turbo + qwen-image-2.0 + GPT-Image-2) → parallel generation → outputs `001_r1_ernie.png`, `001_r1_qwen.png`, `001_r1_gptimage2.png` → side-by-side comparison → user picks the best output
