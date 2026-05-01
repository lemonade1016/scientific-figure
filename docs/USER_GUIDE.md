# Scientific Figure Generator — Complete User Guide

---

## Table of Contents

1. [Overview](#1-overview)
2. [Core Architecture: Two-Layer Prompt Compiler](#2-core-architecture-two-layer-prompt-compiler)
3. [Eight-Phase Workflow in Detail](#3-eight-phase-workflow-in-detail)
4. [Supported Disciplines](#4-supported-disciplines)
5. [Seven Visual Styles](#5-seven-visual-styles)
6. [Two Narrative Modes](#6-two-narrative-modes)
7. [Six Auto-Layout Types](#7-six-auto-layout-types)
8. [Multi-Model Image Generation (Layer 2)](#8-multi-model-image-generation-layer-2)
9. [File Naming Convention](#9-file-naming-convention)
10. [API Configuration Guide](#10-api-configuration-guide)
11. [Cross-Model Comparison & Evaluation](#11-cross-model-comparison--evaluation)
12. [Iteration & Optimization](#12-iteration--optimization)
13. [Quality Assurance System](#13-quality-assurance-system)
14. [Quick Start Examples](#14-quick-start-examples)
15. [FAQ & Troubleshooting](#15-faq--troubleshooting)

---

## 1. Overview

**Scientific Figure Generator v2** is an AI-powered scientific figure generation system that runs as a Claude Code Skill. It accepts natural language descriptions of scientific mechanisms, model architectures, or research concepts, processes them through 8 phases of intelligent analysis and compilation, and finally invokes multiple commercial image generation models in parallel to produce outputs—enabling a "same prompt, multi-model comparison" scientific visualization workflow.

### Core Capabilities

- **Intelligent Understanding**: Automatically detects discipline, narrative mode, and layout type—no need for users to manually select all parameters
- **Expert-Level Prompt Compilation**: 7-layer prompt architecture covering role assignment, discipline conventions, style aesthetics, spatial layout, narrative structure, quality standards, and user content
- **Prompt Distillation**: Compresses 800–1500 word full prompts by 40–60%, preserving all critical constraints while adapting to image generation models' attention mechanisms
- **6-Model Parallel Generation**: Sends the same distilled prompt simultaneously to ERNIE-Image-Turbo, wan2.7-image-pro, qwen-image-2.0, z-image-turbo, Gemini-3-Pro-Image, and GPT-Image-2
- **Cross-Model Comparison**: Scientifically evaluates different models across five dimensions: spatial accuracy, style fidelity, scientific accuracy, text quality, and overall impact

### Use Cases

- Paper figures (mechanism diagrams, model architecture diagrams, flow schematics)
- Graphical Abstract / TOC images
- Conference poster main figures
- Journal cover proposals
- Grant application summary figures
- Academic social media graphics

---

## 2. Core Architecture: Two-Layer Prompt Compiler

The entire Skill is divided into two independent layers:

```
                    ┌─────────────────────────────────┐
                    │  LAYER 1: Decision Engine       │
                    │  Phase 0-7, model-agnostic      │
                    │                                  │
User Input ────────▶│ Phase 0: Requirement Collection  │
                    │ Phase 1: Auto-Analysis           │
                    │ Phase 2: Discipline Selection    │──▶ Output:
                    │ Phase 3: Narrative Mode          │      · Distilled Prompt
                    │ Phase 4: Style Selection         │      · Layout Type
                    │ Phase 5: Auto-Layout             │      · Style
                    │ Phase 6: Prompt Construction     │      · Aspect Ratio
                    │ Phase 7: Prompt Distillation     │
                    └──────────────┬──────────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────────┐
                    │  LAYER 2: Image Providers       │
                    │  Phase 8, multi-model parallel   │
                    │                                  │
    Distilled Prompt ───▶│  User selects N models          │
                    │  ├─ ERNIE-Image-Turbo (Baidu)    │──▶ Output:
                    │  ├─ wan2.7-image-pro (Alibaba)   │      [ID]_[round]_[provider].png
                    │  ├─ qwen-image-2.0 (Alibaba)     │      for cross-model comparison
                    │  ├─ z-image-turbo (Alibaba)      │
                    │  ├─ gemini-3-pro-image (API MART)│
                    │  └─ GPT-Image-2 (API MART)       │
                    └─────────────────────────────────┘
```

### Layer 1: Decision Engine (Phase 0–7)

**Model-agnostic**—responsible only for compiling user intent into an optimal image generation prompt, decoupled from any specific model. Includes intelligent detection, expert recommendations, auto-layout, prompt construction, and distillation.

### Layer 2: Image Generation (Phase 8)

**Multi-model parallel**—sends the same distilled prompt from Layer 1 to multiple user-selected commercial models, enabling scientifically controlled cross-model comparisons.

### v2 Improvements Over v1

| v1 Issue | v2 Solution | Module |
|---------|------------|--------|
| Prompts too long, diluted model attention | Two-stage: Full Prompt → Distilled Prompt | `prompt-distillation.md` |
| Blind user selection (no guidance) | Auto-analysis + expert recommendations | Phase 0–4 |
| No narrative structure | Mechanism Diagram vs Graphical Abstract dual engine | `narrative-composer.md` |
| No spatial intelligence | 6 layout types + visual weight system | `layout-engine.md` |
| Single-model output, no comparison | Layer 2 multi-model parallel generation | `api-integration.md` |

---

## 3. Eight-Phase Workflow in Detail

```
USER INPUT
    │
    ▼
Phase 0: Requirement Collection ─── Gather raw description/code
    │
    ▼
Phase 1: Auto-Analysis ─── Detect discipline, narrative mode, layout type, style match
    │
    ▼
Phase 2: Discipline Selection ─── Recommend + alternatives → user confirmation
    │
    ▼
Phase 3: Narrative Mode ─── Mechanism Diagram vs Graphical Abstract → user confirmation
    │
    ▼
Phase 4: Style Selection ─── Discipline-aware recommendation + alternatives → user confirmation
    │
    ▼
Phase 5: Auto-Layout ─── Layout type, visual weights, reading path, spacing
    │
    ▼
Phase 6: Prompt Construction ─── 7-layer full prompt assembly
    │
    ▼
Phase 7: Prompt Distillation ─── Compress 40–60%, optimize model attention
    │
    ▼
Phase 8: Multi-Model Generation ─── User selects N models, parallel generation, cross comparison
```

**User Interaction Phases**: Phase 0, 2, 3, 4, 8 (5 interactions total)
**Automated Phases**: Phase 1, 5, 6, 7 (fully automatic)

**Prompt Cache Directory**: Full prompts and distilled prompts from Phase 6 and Phase 7 are silently written to `.claude/prompt_cache/` rather than displayed directly in the conversation (to avoid consuming tokens). Users can open files in this directory at any time to view or copy prompts for use in other tools.

---

### Phase 0: Requirement Collection (User Interaction)

**Goal**: Collect the user's raw requirements in full before asking any choice questions.

The system asks the user:

> "Please describe your requirements in as much detail as possible:
> - What mechanism, architecture, or concept do you want to visualize?
> - What are the key components and their relationships?
> - What is the core message or innovation?
> - What is the figure for? (Journal submission, preprint, Graphical Abstract, conference presentation, cover, etc.)
> - If you have a target journal or conference, please specify."

Users can provide:
- Natural language mechanism descriptions
- Model architecture code (Python/PyTorch/TensorFlow)
- Structured step outlines
- Target journal/conference information
- Reference style descriptions

**Code Auto-Translation**: If the user provides code, the system automatically parses module names, data flows, special connections, and innovative components, converting them into natural language descriptions.

---

### Phase 1: Auto-Analysis (Automated)

The system performs four-dimensional analysis on the Phase 0 input:

**1A. Discipline Detection**: Scans input for domain keywords, counts matches, and selects the discipline with the highest match score.

**1B. Narrative Mode Detection**:
- Graphical Abstract triggers: `graphical abstract`, `TOC`, `cover`, `summary`, `highlight`
- Mechanism Diagram triggers: `mechanism`, `pathway`, `process`, `pipeline`, `architecture`

**1C. Layout Type Pre-Detection**: Scans for keywords matching 6 layout types and pre-computes the best match.

**1D. Journal/Conference Extraction**: Identifies target journal names (Nature, Cell, Science, NeurIPS, ICML, etc.) or types (preprint, conference, journal, cover, etc.).

The system outputs an analysis summary:

> **Auto-Analysis Results:**
> - **Detected Discipline:** Biomedicine & Molecular Life Sciences (Confidence: HIGH)
> - **Detected Narrative Mode:** Mechanism Diagram
> - **Detected Layout Type:** Pipeline Layout
> - **Target Journal:** Nature Biotechnology

---

### Phase 2: Discipline Selection (User Interaction)

Based on Phase 1 analysis, the system **recommends** (rather than lists) a discipline field, using `AskUserQuestion` interaction.

**Recommendation Logic**:
- If a clear target journal has a known mapping to a discipline → boost that discipline's weight
- If detection confidence is HIGH → recommend directly
- If confidence is MEDIUM or LOW → recommend top 2, let user choose
- Always preserve user override option

Recommended options are marked with `⭐ Recommended (reason)`.
<img width="821" height="484" alt="phase2-discipline-selection" src="https://github.com/user-attachments/assets/bf926b4b-eb9e-4dd3-a83d-a33e12b7b0ea" />

---

### Phase 3: Narrative Mode Selection (User Interaction)

The system presents the detected narrative mode for confirmation.

**Option 1: Mechanism Diagram**
- Causal chain: Input → Process → Interaction → Output
- Explains "how it works"
- Best for: pathway diagrams, architecture diagrams, algorithm flowcharts, process schematics

**Option 2: Graphical Abstract**
- Impact arc: Problem → Innovation → Result → Significance
- Conveys "what was done and why it matters"
- Best for: journal TOC figures, press release graphics, covers, social media summaries

Users can also select **Hybrid Mode** (top 70% detailed mechanism, bottom 30% Graphical Abstract summary bar).
<img width="821" alt="phase3-narrative-mode" src="https://github.com/user-attachments/assets/9deb7535-d954-4fb2-b267-aef0aaf720b1" />

---

### Phase 4: Style Selection (User Interaction)

The system computes the optimal style recommendation based on a three-dimensional matrix of "discipline + narrative mode + target journal".

**Style Decision Matrix**:

| Scenario | Recommended Style | Reason |
|----------|------------------|--------|
| Traditional journal + any discipline | Classic Vector or Hybrid | Editor acceptance priority |
| Preprint + any discipline | Hand-Drawn Sketch or Minimal Infographic | Social media virality |
| Graphical Abstract + any | Minimal Infographic or Hybrid | Thumbnail readability |
| Mechanism Diagram + AI/CS | Hand-Drawn Sketch | Domain trend |
| Mechanism Diagram + Biomedicine | Scientific Illustration or Classic Vector | Biological accuracy requirements |
| Mechanism Diagram + Chemistry/Materials | Classic Vector or 3D Render | Molecular visualization needs |
| Conference poster | Futuristic Tech or Minimal Infographic | Long-distance visual impact |
| Journal cover | 3D Render or Scientific Illustration | Maximum visual impact |
| Interdisciplinary | Hybrid | Multi-layer information hierarchy |

The system presents 7 styles via `AskUserQuestion`, marking the recommended style with `⭐ Recommended` and alternatives with `🔄 Alternative`.
<img width="821" alt="phase4-style-selection" src="https://github.com/user-attachments/assets/5f20574a-d501-4e9e-87dd-0586761ce1ea" />

---

### Phase 5: Auto-Layout Analysis (Automated)

The system automatically executes 4 sub-steps without user intervention.

**5A. Figure Type Classification**: Classifies the figure into one of 6 layout types (see Section 7).

**5B. Visual Weight Calculation**: Extracts all named components and scores them (1–10) based on the following signals:

| Signal | Score |
|--------|-------|
| Tagged "novel", "our", "proposed", "innovative" | 10 |
| Tagged "first", "breakthrough", "首次" | 10 |
| Main research subject (target protein, model name, candidate drug) | 9 |
| Tagged "critical", "essential", "key" | 8 |
| Tagged "important" | 7 |
| Standard system component | 5 |
| Auxiliary element | 3 |
| Environmental context | 3 |
| Optional add-on element | 2 |

**5C. Reading Path Assignment**: Determines visual flow based on layout type.

**5D. Layout Prompt Assembly**: Generates layout instructions as Layer 4 of Phase 6.

The system briefly outputs the layout analysis results.

---

### Phase 6: Full Prompt Construction (Automated)

The system assembles the prompt according to a **7-layer architecture**:

```
LAYER 1: Role & Identity ── 20-year-experience scientific illustrator persona
LAYER 2: Discipline-Specific Conventions ── loaded from discipline-library
LAYER 3: Style Aesthetic Instructions ── loaded from style-library
LAYER 4: Auto-Layout Spatial Instructions ── Phase 5 output
LAYER 5: Narrative Structure ── loaded from narrative-composer
LAYER 6: Top-Tier Quality Standards ── loaded from quality-standards
LAYER 7: User-Specific Content ── components, relationships, core message
```

Full prompts (~800–1500 words) are lengthy, so by default they are **silently written to cache files** rather than displayed in the conversation, to save token overhead. File path:

```
.claude/prompt_cache/full_prompt_[promptID].txt
```

The system will notify when writing is complete; users can open the file at any time to review content and adjust any layer before continuing.

---

### Phase 7: Prompt Distillation (Automated)

**Why distillation is needed**: Image generation models' cross-attention mechanisms dilute key constraints under long prompts (>500 tokens). Distillation converts abstract rules into concrete visual vocabulary that models respond to more effectively.

**Distillation Process**:

1. **Phase 1 Transformation** (Rules → Visual Descriptors):
   - Remove meta-instructions and preambles
   - Convert abstract rules to concrete visual descriptors
   - Cluster multi-constraint rules into keyword groups
   - Convert structural rules to spatial descriptors

2. **Phase 2 Priority Reordering**:
   - Style identifier + layout type → **Highest priority** (first 15%)
   - Key visual constraints + core elements → **High priority** (next 20%)
   - Discipline conventions + secondary elements → **Medium priority** (next 30%)
   - Quality standards (compressed) + details → **Low priority** (next 25%)
   - Negative constraints → **Lowest priority** (last 10%)

3. **Verify 6 Key Constraints Are Preserved**:
   - Color accessibility (red-green colorblind safe)
   - Arrow semantics (type consistency)
   - Visual hierarchy (3 clear levels)
   - Reading path (clear flow direction)
   - Scientific accuracy markers (hypothetical = dashed line)
   - Style identifier (not corrupted by compression)

Distilled prompts are also **silently written to cache files**:

```
.claude/prompt_cache/distilled_prompt_[promptID].txt
```

The system will report the distilled word count and compression rate, and ask the user which version to use. Users can open the corresponding file to view contents.

**Default**: Use distilled prompt (250–400 words, recommended). Full prompt is available for manual review. Both file sets are retained simultaneously for easy subsequent iteration and comparison.

---

### Phase 8: Multi-Model Parallel Generation (User Interaction)

**This is Layer 2: Image Generation Layer**. See Section 8 for details.

---

## 4. Supported Disciplines

The system supports 8 major disciplines, each with dedicated prompt templates covering the field's visual grammar, common element types, color standards, and composition conventions.

### 1. Biomedicine & Molecular Life Sciences
- Standard biological visual grammar: phospholipid bilayer membrane, Y-shaped receptors, ligand small molecules, double-membrane nucleus, mitochondrial cristae, etc.
- Clear cellular compartment delineation: extracellular, plasma membrane, cytoplasm, nucleus, mitochondria, ER, Golgi
- Signal direction semantics: solid arrow (activation), T-bar termination (inhibition), dashed line (indirect/unknown), circular arrow (feedback)
- Post-translational modifications: phosphorylation (P-circle transfer), ubiquitination (Ub tag)
- Biological color scheme: warm colors (active/oncogenic/pro-inflammatory), cool colors (inhibitory/tumor-suppressive/anti-inflammatory), green (structural), gray (baseline)

### 2. Chemistry, Materials & Nanoscience
- Chemical structures: standard bond-line notation, ball-and-stick models, CPK atomic coloring
- Reaction schemes: reactant → intermediate → product, reaction condition annotations
- Energy/coordinate diagrams: reaction coordinate vs free energy, transition state (‡), activation energy (ΔG‡)
- Materials architecture: thin-film cross-sections, core-shell nanoparticles, porous frameworks, 2D material sheets
- Synthesis workflows: stepwise representation with key parameter annotations

### 3. Artificial Intelligence & Computer Science
- Neural network layers: color coding (blue=encoder, green=decoder, orange=attention, purple=FFN, gray=normalization)
- Data tensors: 3D isometric boxes + shape annotations `[B, L, D]`
- Attention mechanisms: Q/K/V parallel inputs, scaled dot-product, multi-head concatenation
- Standard elements: Transformer Block, MoE, LoRA, positional encoding, KV-Cache, RAG, diffusion models
- Flow conventions: data flow=thick solid line, gradient flow=red dashed line, residual connection=thin curved line

### 4. Engineering & Applied Physics
- Device schematics: cross-sections, isometric views, top views
- System block diagrams: functional blocks + signal/power/fluid connections
- Energy diagrams: Sankey diagrams, band diagrams, efficiency cascades
- Mechanical diagrams: engineering drawing standards, force analysis, stress-strain curves
- Electronic diagrams: IEEE/ANSI standard symbols
- Optical diagrams: ray tracing, wavefront visualization

### 5. Clinical Medicine & Healthcare
- Anatomical context: organ/tissue semi-transparent backgrounds
- Disease mechanisms: healthy→disease progression comparison (cool→warm color transition)
- Mechanism of Action (MoA): absorption→distribution→target binding→signal cascade→efficacy
- Clinical pathways: decision tree format, diamond=decision point, rectangle=action, ellipse=outcome
- Diagnostic algorithms: test→result→interpretation→next step
- Color scheme: arterial=red, venous=blue, lymphatic=green, neural=yellow

### 6. Environmental, Earth & Climate Science
- Cycle diagrams: reservoirs (boxes) + fluxes (arrows, width ∝ rate)
- Ecosystems: trophic level vertical stacking
- Climate systems: five-sphere interactions, radiative forcing
- Geological cross-sections: stratigraphic columns, structural features (faults, folds, unconformities)
- Biogeochemistry: element reservoirs + transformation arrows
- Color scheme: atmosphere=light blue, ocean=dark blue, land/vegetation=green, anthropogenic impact=warm colors

### 7. Physics & Mathematics
- Feynman diagrams: fermion=solid line, photon=wavy line, gluon=coil, W/Z=dashed line, Higgs=dotted line
- Phase diagrams: first-order transition=solid line, second-order=dashed line, crossover=gradient
- Spacetime diagrams (Penrose diagrams): conformal infinity boundaries, light cones, worldlines
- Quantum mechanics: potential well+bound state wavefunctions, quantum tunneling, Bloch sphere, energy level diagrams
- Condensed matter: Brillouin zones, Fermi surfaces, band structures, density of states
- Mathematical structures: commutative diagrams, manifold embeddings

### 8. Interdisciplinary & Emerging Fields
- Multi-scale integration: molecule→cell→tissue→organ→organism→population
- Cross-domain mapping: computational domain + biological/physical domain + interface/bridge domain
- Data-to-mechanism integration: experimental data thumbnails + mechanism schematic elements
- Digital twins: physical system ↔ digital representation bidirectional information flow
- Workflow integration: computational pipeline ∥ experimental pipeline, cross-feedback
- Color scheme: each parent discipline assigned a different color family

---

## 5. Seven Visual Styles

Each style has a complete visual instruction block including line quality, color treatment, lighting, texture, and overall artistic direction.

### Style 1: Classic Vector (Clean Journal Style)
- Flat vector illustration, suitable for direct submission to Nature/Cell/Science
- Uniform outline weight (1–2pt), 4–6 solid colors, zero gradients
- Regular geometric shapes, strict modular grid alignment
- Sharp triangular solid arrows, pure white background `#FFFFFF`
- No shadows, no glows, no textures, no 3D effects
- Overall impression: "Nature Methods main-figure quality—clean, precise, universal"

### Style 2: Hand-Drawn Sketch (Whiteboard Thinking Style)
- Organic hand-drawn feel, simulating whiteboard or lab notebook
- Slightly trembling, imperfect lines with natural stroke variation (0.5–3pt)
- Asymmetric hand-drawn arrows, off-white paper texture background `#FAFAF5`
- Soft natural tones: pencil gray, ink black, slate blue, brick red, olive green
- Labels like handwritten text, slightly irregular
- Overall impression: "The smart colleague's key idea sketched on a whiteboard—informal yet crystal clear"

### Style 3: Minimal Infographic (High-Impact Communication Style)
- Magazine-quality editorial infographic, extreme visual restraint
- At least 40% white space, only 2–4 colors
- Icon-based instead of text labels, ≤15 icons
- Ultra-thin lines (0.5pt), extreme minimalism
- 8–10% margin on all four sides, asymmetric balance
- Overall impression: "Readable in 3 seconds, Nature Communications-level quality"

### Style 4: Scientific Illustration (Textbook Realism Style)
- Professional-grade scientific illustration, suitable for Nature Reviews / Cell / textbooks
- Semi-realistic rendering of biological structures, accurate morphology
- Soft naturalistic gradient shadows, upper-left 45° light source
- 8–12 colors + tonal variations, surface texture details
- Three-point lighting (key+fill+ambient occlusion), no hard shadows
- Overall impression: "Nature Reviews Molecular Cell Biology Figure 1"

### Style 5: Futuristic Tech (Frontier Innovation Style)
- Dark tech aesthetic background `#0A0A1A`, subtle grid texture
- Neon glowing lines: cyan `#00E5FF`, electric blue `#4488FF`, magenta `#FF44AA`
- Glassmorphism nodes, 2–4px glow effects, data particle streams
- Monospace or tech sans-serif fonts
- ⚠️ Note: Mainly for presentations/posters/preprints; may be considered too informal for traditional journal submission
- Overall impression: "NeurIPS main stage or CES keynote level"

### Style 6: Hybrid (Multi-Layer Visual Hierarchy, Top 2025–2026 Trend)
- **Three-layer visual system**:
  - Layer 1 (60% visual weight): Clean Vector structural framework—module boxes, main arrows, compartment boundaries (soft blue-gray)
  - Layer 2 (25% visual weight): Hand-Drawn emphasis—2–3 key innovation points (warm orange, deep blue, bold strokes)
  - Layer 3 (15% visual weight): Scientific Illustration context—cells/molecules/tissues (soft and delicate)
- Readers can read at three levels: 3-second skim → 30-second study → 3-minute deep dive
- Warm gray background `#F8F7F4`
- Overall impression: "The new standard for contemporary top-tier journals—extreme information hierarchy clarity"

### Style 7: 3D Render (Photorealistic Depth Style)
- Professional-grade 3D scientific visualization, Blender/Cinema 4D/Maya quality
- **Three-point lighting**: key 60% (upper-left 5500K) + fill 30% (lower-right) + rim 40% (rear-upper 6500K)
- **Physically accurate materials**: glass IOR 1.5, metal roughness 0.1–0.6, biological tissue subsurface scattering
- Perspective camera (50–85mm focal length), subtle depth of field
- Procedural surface textures, tiny realistic surface imperfections
- Overall impression: "Advanced Materials or Cell journal cover level"

---

## 6. Two Narrative Modes

### Mode A: Mechanism Diagram Engine

**Purpose**: Explain "how it works"—causal chains, process flows, structural relationships, dynamic mechanisms.

**Narrative Structure—Causal Chain**:

```
┌──────────────────────────────────────┐
│  Context: Where does it happen?      │
│  (Compartment/System boundary)       │
├──────────────────────────────────────┤
│  Input ──→ Step1 ──→ Intermediate    │
│              ├──→ Step2a ──→ ┐       │
│              └──→ Step2b ──→ Merge ──→ Final Output
├──────────────────────────────────────┤
│  Key Insight: Innovation/Unexpected  │
│  finding (visual focal point)        │
└──────────────────────────────────────┘
```

**6 Narrative Beats**: Context → Input/Starting State → Transformation Sequence → Key Interaction → Output/Final State → Innovation Marker

### Mode B: Graphical Abstract Engine

**Purpose**: Convey the paper's core contribution in a single self-contained visual—for journal homepages, social media, and rapid comprehension.

**Narrative Structure—Impact Arc**:

```
┌────────────────────────────────────────────┐
│  Problem ────→   Innovation    ←──── Result │
│  (Left, 25%)  (Center, 40%,   (Right, 25%) │
│   Dark/Small)  Largest/Brightest) Bright/Large)
│                 ↓                            │
│          Significance (Bottom 10%,          │
│          broad impact statement)             │
└────────────────────────────────────────────┘
```

**Key Rules**:
- Maximum 5 visual elements (ideal: 3)
- Exactly 1 primary color accent (innovation area)
- At least 40% white/blank space
- No a/b/c panels—single unified image
- Must remain readable at 200px thumbnail size
- Text ≤ 10 words (ideal ≤ 5 words)
- Clear reading path: Problem → Innovation → Result → Significance

---

## 7. Six Auto-Layout Types

The system automatically detects the optimal layout type from user input without manual selection.

### Type 1: Pipeline Layout
```
[Input] ──→ [Step1] ──→ [Step2] ──→ [Step3] ──→ [Output]
```
- **Best for**: AI/ML workflows, chemical synthesis routes, signal transduction cascades, data processing pipelines
- **Detection keywords**: `step by step`, `pipeline`, `workflow`, `sequential`
- **Aspect ratio**: 16:9 (≤5 steps) or wider (6+ steps)
- **Reading path**: Z-pattern (upper-left→upper-right→lower-left→lower-right)

### Type 2: Central Hub Layout
```
         [ModuleA]
            ↑
[ModuleB] ← ★ Core ★ → [ModuleC]
            ↓
         [ModuleD]
```
- **Best for**: New framework papers, multimodal fusion systems, centralized processing architectures
- **Detection keywords**: `core`, `central`, `hub`, `our framework`, `integrates`
- **Aspect ratio**: 1:1 (square)
- **Reading path**: Center→Top→Right→Bottom→Left (clockwise)

### Type 3: Layered Stack Layout
```
┌──────────────────────┐
│   Input / Embedding  │
├──────────────────────┤
│   Encoder / Processing│
├──────────────────────┤
│   Bottleneck / Fusion│
├──────────────────────┤
│   Decoder / Generation│
├──────────────────────┤
│   Output / Prediction│
└──────────────────────┘
```
- **Best for**: Transformer/CNN/RNN architectures, encoder-decoder models
- **Detection keywords**: `encoder`, `decoder`, `layer`, `stack`, `hierarchical`
- **Aspect ratio**: 9:16 (portrait)
- **Reading path**: Top-to-bottom

### Type 4: Biological Spatial Layout
```
┌──────────────────────┐
│   Extracellular Space│
├──────────────────────┤
│   Plasma Membrane    │
├──────────────────────┤
│   Cytoplasm          │
│   [Signaling Protein]│
├──────────────────────┤
│   Nucleus            │
│   [Transcription     │
│    Factor] [DNA]     │
└──────────────────────┘
```
- **Best for**: signaling pathways, membrane transport, intracellular trafficking, drug delivery
- **Detection keywords**: `membrane`, `cytoplasm`, `nucleus`, `compartment`
- **Aspect ratio**: 3:4 or 2:3 (portrait)

### Type 5: Branching Tree Layout
```
              [Root/Start]
                  │
          ┌───────┴───────┐
          ↓               ↓
     [DecisionA]      [DecisionB]
          │               │
     ┌────┴────┐     ┌────┴────┐
     ↓         ↓     ↓         ↓
  [Outcome] [Outcome] [Outcome] [Outcome]
```
- **Best for**: clinical decision trees, diagnostic algorithms, classification systems, treatment guidelines
- **Detection keywords**: `if...then`, `decision`, `branching`, `classification`
- **Aspect ratio**: 2:3 or 3:4 (portrait)

### Type 6: Cyclic Loop Layout
```
        [ProcessA] ←── [ProcessD]
            │           ↑
            ↓           │
        [ProcessB] ──→ [ProcessC]
```
- **Best for**: metabolic cycles (TCA, Calvin), biogeochemical cycles, feedback regulation
- **Detection keywords**: `cycle`, `loop`, `feedback`, `regeneration`
- **Aspect ratio**: 1:1 (square)
- **Reading path**: Clockwise (entering from 12 o'clock position)

---

## 8. Multi-Model Image Generation (Layer 2)

### 8.1 Six Available Models

| # | Model | Platform | API Type | Strengths | Cost per Image |
|---|-------|----------|----------|-----------|----------------|
| 1 | ERNIE-Image-Turbo | Baidu AI Studio | Sync | Fast turbo inference, strong Chinese text | $0.01–0.03 |
| 2 | wan2.7-image-pro | Alibaba Bailian | Async | Up to 4K, thinking mode reasoning enhancement | $0.02–0.06 |
| 3 | qwen-image-2.0 | Alibaba Bailian | Sync | Best bilingual text rendering | $0.02–0.06 |
| 4 | z-image-turbo | Alibaba Bailian | Sync | Fastest generation speed | $0.01–0.03 |
| 5 | gemini-3-pro-image-preview | API MART | Async | Reasoning-driven, multi-reference image editing | $0.03–0.08 |
| 6 | GPT-Image-2 | API MART | Async | Near-perfect text rendering, rich world knowledge | $0.04–0.12 |

### 8.2 Resolution

All 6 models support **1K resolution**, with some supporting higher resolutions (switchable by modifying parameters in `generate_images.py`). Different models use different size formats:

| Model | size (ratio) | resolution |
|-------|-------------|------------|
| ERNIE-Image-Turbo | `1024x1024` / `1376x768` / `768x1376` | — (determined by size) |
| wan2.7-image-pro | `"1K"` / `"2K"` / `"4K"` | — (determined by size) |
| qwen-image-2.0 | `1024*1024` / `1280*720` / `720*1280` | — (determined by size) |
| z-image-turbo | `1024*1024` / `1280*720` / `720*1280` | — (determined by size) |
| gemini-3-pro-image | `"1:1"` / `"16:9"` / `"9:16"` etc. | `"1K"` / `"2K"` / `"4K"` |
| GPT-Image-2 | `"1:1"` / `"16:9"` / `"9:16"` etc. | `"1k"` / `"2k"` / `"4k"` |

> **⚠️ Note:** Gemini and GPT-Image-2 use `size` for aspect ratios (e.g., `"1:1"`) and control resolution via a separate `resolution` field. Gemini uses uppercase K (`"1K"`), GPT-Image-2 uses lowercase k (`"1k"`). This is completely different from the ERNIE/wan/qwen/z-image format.

### 8.3 Parallel Generation

Parallel generation is orchestrated by `generate_images.py` (stdlib-only Python script, zero external dependencies). Uses `concurrent.futures.ThreadPoolExecutor` for true concurrent I/O; each model runs independently, and a single failure does not affect others.

**Key Rules**:
- All models receive the **same distilled prompt**
- qwen/z-image models set `prompt_extend: false` to preserve exact prompts for fair comparison
- wan2.7-image-pro, gemini-3-pro-image-preview, and GPT-Image-2 are asynchronous—require task submission followed by polling (5-second interval), total timeout 120 seconds
- Synchronous models (ERNIE/qwen/z-image) return results in a single request; async models return a `task_id`, and the final image is obtained via polling
- Results are output as concise JSON summaries; raw API responses or prompt text are not written to conversation context

> **Manual invocation**: If you need to call the generation script outside the Skill flow:
> ```bash
> python3 /Users/lemonade/.claude/skills/scientific-figure/generate_images.py \
>   --prompt-file .claude/prompt_cache/distilled_prompt_001.txt \
>   --providers ernie,qwen,gemini \
>   --output-prefix 001_r1 \
>   --aspect-ratio 1:1
> ```
<img width="821" alt="phase8-parallel-generation" src="https://github.com/user-attachments/assets/1862b2e7-f4c6-4e0c-9053-256b2503c67d" />

---

## 9. File Naming Convention

All generated images follow a unified naming rule:

```
[promptID]_[round]_[provider].png
```

| Field | Source | Format | Example |
|-------|--------|--------|---------|
| `promptID` | Auto-incremented from `state.json` | 3-digit zero-padded | `001`, `002` |
| `round` | `state.json` current_round | `r` + number | `r1`, `r2` |
| `provider` | Model short name | lowercase | `ernie`, `qwen`, `gptimage2` |

### Model Short Name Reference

| Model | Short Name | Filename Example |
|-------|------------|------------------|
| ERNIE-Image-Turbo | `ernie` | `001_r1_ernie.png` |
| wan2.7-image-pro | `wan` | `001_r1_wan.png` |
| qwen-image-2.0 | `qwen` | `001_r1_qwen.png` |
| z-image-turbo | `zimage` | `001_r1_zimage.png` |
| gemini-3-pro-image-preview | `gemini` | `001_r1_gemini.png` |
| GPT-Image-2 | `gptimage2` | `001_r1_gptimage2.png` |

### Round Management

`state.json` tracks `current_prompt_id` and `current_round`:
- **New Prompt**: Increment `next_prompt_id`, set as `current_prompt_id`, reset `current_round` to 1
- **Regenerate Same Prompt**: Increment `current_round`

---

## 10. API Configuration Guide

### 10.1 Configuration File Location

```
/Users/lemonade/.claude/skills/scientific-figure/config.local.json
```

This file is excluded by `.gitignore` and will not be committed to version control.

### 10.2 Configuration File Structure

```json
{
  "baidu_ai_studio": {
    "api_key": "Your Baidu AI Studio API Key",
    "base_url": "https://aistudio.baidu.com/llm/lmapi/v3/images/generations"
  },
  "alibaba_bailian": {
    "api_key": "Your Alibaba Bailian API Key",
    "base_url": "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation",
    "task_url": "https://dashscope.aliyuncs.com/api/v1/tasks"
  },
  "apimart": {
    "api_key": "Your API MART API Key",
    "base_url": "https://api.apimart.ai/v1/images/generations"
  }
}
```

### 10.3 Platform-to-Model Mapping

| Platform | Config Key | Available Models |
|----------|-----------|------------------|
| Baidu AI Studio | `baidu_ai_studio.api_key` | `ernie-image-turbo` |
| Alibaba Bailian | `alibaba_bailian.api_key` | `wan2.7-image-pro`, `qwen-image-2.0`, `z-image-turbo` |
| API MART | `apimart.api_key` | `gemini-3-pro-image-preview`, `gpt-image-2` |

### 10.4 Obtaining API Keys

- **Baidu AI Studio**: https://console.bce.baidu.com/iam/#/iam/apikey/list
- **Alibaba Bailian**: https://bailian.console.aliyun.com/
- **API MART**: https://apimart.ai/

If the configuration file is missing or all keys are empty, the system prompts:
> "No API Key found in `config.local.json`. Please add your key to the configuration file."

### 10.5 Platform Availability Scan

At the start of Phase 8, the system automatically scans `config.local.json` and only displays models from configured platforms. Unconfigured platforms are shown as `⚠️ Not configured (please add key in config.local.json)`.

---

## 11. Cross-Model Comparison & Evaluation

After all models receive the same distilled prompt, the system prompts evaluation across 5 dimensions:

| Dimension | Evaluation Content | Typical Best Performers |
|-----------|-------------------|------------------------|
| **Spatial Accuracy** | Which model best followed layout instructions? | GPT-Image-2, wan2.7 (thinking mode) |
| **Style Fidelity** | Which model best captured the target style aesthetic? | qwen-image-2.0 (precise prompt preservation) |
| **Scientific Accuracy** | Which model avoided hallucinated structures/connections? | GPT-Image-2, gemini-3-pro |
| **Text Quality** | Which model produced the cleanest labels? | qwen-image-2.0, GPT-Image-2 |
| **Overall Impact** | Which image most effectively conveyed the core message? | Subjective—compare all |

### Post-Generation Processing Recommendations

1. **Select Best Output**: Different models may excel in different dimensions
2. **Text Labels**: Add precise labels in Illustrator/Inkscape/PPT—AI text is unreliable across all models
3. **Scientific Validation**: Verify all details against known domain facts
4. **Color Consistency**: Match the paper's global color scheme
5. **Arrow Semantics**: Verify consistency of all arrow types
6. **3-Second Test**: Show to a colleague unfamiliar with the work
7. **Journal Compliance**: Adjust resolution, color space, and fonts to target journal requirements
8. **Cross-Model Insights**: Track which model performs best for your discipline/style combination

---

## 12. Iteration & Optimization

After generation, the system provides the following iteration options:

- **Refine Prompt**: Adjust specific wording or details, then re-run all (or selected) models
- **Adjust Style Intensity**: "More hand-drawn" / "Less glow"
- **Fix Layout**: Move specific elements, add/remove connections
- **Switch Style/Discipline**: Try different approaches
- **Regenerate Same Prompt**: Same prompt, same model, different random seed (increment round)
- **Cross-Model Iteration**: Keep the best model output, adjust prompt only for underperforming models and regenerate

---

## 13. Quality Assurance System

The system embeds top-tier journal quality standards (30 non-negotiable rules) as Layer 6 of the prompt in every generation request.

### A. Clarity & Instant Readability
- **3-Second Rule**: Core mechanism must be identifiable within 3 seconds
- **Single Flow Direction**: Uniform left→right or top→bottom, never mixed
- **Element Economy**: Every element must justify its existence
- **3–7 Key Structural Elements** (logically groupable)

### B. Three-Level Visual Hierarchy
- Level 1 (Dominant): Core pathway—largest, most saturated, thickest lines
- Level 2 (Secondary): Supporting details—medium
- Level 3 (Tertiary): Contextual elements—smallest, faintest
- Reader attention sequence: Level 1 (<1s) → Level 2 (2–5s) → Level 3 (10s+)

### C. Color Standards
- Maximum 6 distinct hues (excluding black/white/gray neutrals)
- Red-green colorblind safe (deuteranopia + protanopia): no pure red-green contrast, ensure >30% brightness difference, fully distinguishable in grayscale
- Semantic colors: warm=active/upregulated, cool=inhibitory/downregulated, neutral=structural/baseline
- Color coding consistency: same entity must have the same color wherever it appears

### D. Arrow & Connection Semantics
- Solid arrow (→) = direct activation/promotion/conversion
- T-bar termination (⊣) = direct inhibition/blockage
- Dashed arrow (⇢) = indirect/hypothetical/unknown mechanism
- Open arrow (⟶) = translocation/transport
- Thin connecting line (─) = physical binding/complex formation
- Arrows must not cross (use "bridge" when necessary)

### E. Typography & Labeling
- Sans-serif font throughout (Arial/Helvetica equivalent)
- Labels 7–9pt (at final publication size)
- Labels must not overlap any structural line/shape
- All text horizontal (sole exception: y-axis labels on plots)

### F. Composition & Layout
- Minimum 8% margin on all four sides
- All elements grid-aligned
- Multi-panel label positions consistent

### G. Narrative Structure
- Three-act story arc: Context → Mechanism → Result
- Innovation emphasis: novel contribution must be a Level 1 element

### H. Scientific Accuracy & Integrity
- Spatial plausibility: proteins cannot be larger than cells
- Uncertainty disclosure: hypothetical steps must be marked with dashed lines + light color + "?" or "[hypothetical]"
- No fabrication: do not create molecular structures or mechanism details not supported by user input
- Scale awareness: known scale information must be reasonably respected

### I. Technical Production Standards
- Equivalent 300 dpi (full-page ~2100px wide)
- RGB color space
- Thumbnail readability (still distinguishable at 400px wide)
- No AI artifacts: no garbled text, no anatomically impossible structures, no Escher-style spatial paradoxes, no blurry edges, no inconsistent multi-light-source shadows

---

## 14. Quick Start Examples

### Example Conversation

**User**:
> "I need a Graphical Abstract for a paper I'm submitting to Nature Biotechnology. The paper is about an AI model with a hybrid graph neural network + Transformer architecture for predicting protein-drug binding affinity."

**System Flow**:

1. **Phase 0**: Requirement collection complete
2. **Phase 1**: Auto-analysis
   - Discipline: Interdisciplinary (AI + biology keywords detected)
   - Narrative mode: Graphical Abstract (explicitly mentioned by user)
   - Target journal: Nature Biotechnology
3. **Phase 2**: Discipline recommendation → ⭐ Interdisciplinary & Emerging Fields (AI+Biomed keywords detected)
4. **Phase 3**: Narrative mode confirmation → ⭐ Graphical Abstract
5. **Phase 4**: Style recommendation → ⭐ Hybrid (best choice for interdisciplinary GA in Nature Biotechnology)
6. **Phase 5**: Layout → Central Hub (core = GNN+Transformer fusion model)
7. **Phase 6**: Assemble 7-layer full prompt (~1200 words)
8. **Phase 7**: Distill prompt (~350 words, ~70% compression)
9. **Phase 8**: User selects 3 models (ERNIE + qwen-image-2.0 + GPT-Image-2) → parallel generation → outputs:
   - `001_r1_ernie.png`
   - `001_r1_qwen.png`
   - `001_r1_gptimage2.png`
   → side-by-side comparison → user selects best output

### How to Trigger This Skill

In Claude Code, simply describe your needs in natural language—the Skill will activate automatically:

> "I need a mechanism diagram showing our proposed Dual-Stream Transformer architecture. It includes two parallel encoder streams (image stream and text stream), fused through a cross-modal attention module, and finally outputting multimodal representations through a joint decoder. Target conference is CVPR."

Trigger keywords include: `mechanism diagram`, `scientific figure`, `Graphical Abstract`, `model architecture diagram`, `draw a mechanism diagram`, `generate a scientific figure`, etc. No prefix command is needed—just describe directly.

---

## 15. FAQ & Troubleshooting

### API Issues

| Error | Possible Cause | Solution |
|-------|---------------|----------|
| `401 Unauthorized` | Invalid or expired API Key | Verify Key in `config.local.json` |
| `429 Too Many Requests` | Rate limit exceeded | Wait 30 seconds and retry that model |
| `400 Bad Request` | Prompt too long or invalid size format | Check size format (varies by model); truncate prompt if >4000 characters |
| ERNIE invalid size | Unsupported size string | ERNIE only accepts 7 fixed sizes; remap to nearest size |
| API MART `400` parameter error | `size` passed `"1K"` instead of ratio | Gemini/GPT-Image-2 `size` must be a ratio like `"1:1"`; use `resolution` field for resolution |
| Bailian `PENDING` stuck | Async task incomplete | Poll up to 120 seconds; if still PENDING, report timeout |
| API MART task stuck at `submitted` | Async task incomplete | Poll at 5-second intervals, max 120 seconds; if still stuck, report timeout |
| API MART task does not exist | Task expired | Resubmit generation task |
| API MART `402` | Insufficient account balance | Recharge at https://apimart.ai/keys |
| API MART `content_filter` | Safety filter triggered | Remove medical gore, explicit anatomy, drug abuse, etc. |
| Bailian `task_id` is null | Sync model used async workflow | wan2.7 is async; qwen/z-image are sync—use correct mode |
| wan2.7 polling timeout | Model high load | Offer retry; consider sync alternatives (qwen/z-image) |

### Common Questions

**Q: What if the distilled prompt loses key information?**
A: Phase 7 writes both full and distilled prompts to `.claude/prompt_cache/`. If you feel the distilled version omits important content, you can choose to use the full prompt for generation. However, in the vast majority of cases, the distilled version performs better (because model attention is more focused).

**Q: Can I use my own API Key?**
A: Yes. Simply edit the `config.local.json` file and enter your API Key from Baidu AI Studio, Alibaba Bailian, or API MART. Unconfigured platform models will be automatically hidden.

**Q: Can I get the prompt without using any API?**
A: Yes. Even without configuring any API Key, Phases 0–7 run completely and produce a distilled prompt. You can copy the distilled prompt to any image generation tool (Midjourney, DALL-E, Stable Diffusion, etc.).

**Q: Can generated images be submitted directly?**
A: Recommended as a starting point. AI-generated text labels are unreliable and usually require post-processing in Illustrator/Inkscape/PPT—adding precise labels, adjusting colors to match journal requirements, and verifying scientific accuracy.

**Q: How do I get the best results?**
A: (1) Provide as detailed a description as possible (components, relationships, innovations); (2) Select 3–4 models for cross-model comparison; (3) Always use the distilled prompt; (4) Post-edit the best output; (5) Track which model performs best for your discipline/style combination.

**Q: How do I view generated prompts?**
A: Full and distilled prompts are saved in `.claude/prompt_cache/`, named `full_prompt_[ID].txt` and `distilled_prompt_[ID].txt`. You can open them directly, or copy them to Midjourney, DALL-E, and other image generation tools.

**Q: Can I skip image generation and only get the prompt?**
A: Yes. Even without configuring any API Key, Phases 0–7 run completely, and the final distilled prompt is written to `.claude/prompt_cache/`. Simply select "No generation" in Phase 8.

**Q: Can I retry a single model after failure without rerunning all?**
A: Yes. During parallel generation, each model runs independently; a single model failure does not affect others. The system marks the failed model and error reason in the results, and provides a retry option without rerunning all models.

**Q: What does it cost?**
A: Single-image costs range from $0.01 to $0.12 across the 6 models. Generating 1K images with 3–4 models in parallel typically costs $0.05–$0.30 total. Alibaba Bailian and Baidu offer hundreds of free credits for new users.

---

## Appendix: Skill File Structure

```
~/.claude/skills/scientific-figure/
├── SKILL.md                          # Main skill file (workflow definition)
├── config.local.json                  # API Key configuration (gitignored)
├── state.json                         # Prompt ID and round tracking
└── references/                        # Reference libraries
    ├── discipline-library.md          # 8-discipline prompt templates
    ├── style-library.md               # 7-style prompt templates
    ├── quality-standards.md           # 30 quality standards
    ├── api-integration.md             # 6-model API call guide
    ├── narrative-composer.md          # 2 narrative mode definitions
    ├── layout-engine.md               # 6 layout types + visual weight system
    └── prompt-distillation.md         # Prompt distillation methodology
```

---

> **Version**: v2.0
> **License**: CC-BY-4.0
> **Updated**: 2026-05-01
