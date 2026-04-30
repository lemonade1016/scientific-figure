# Narrative Composer

This module structures the scientific story the figure tells. It defines WHAT the figure communicates, providing the narrative skeleton that the Layout Engine (WHERE) and Style Library (HOW) build upon.

---

## Two Narrative Modes

The system auto-detects the appropriate mode from the user's input, then presents the recommendation for user confirmation.

### Mode A: Mechanism Diagram Engine

**Purpose:** Explain HOW something works — causal chains, process flows, structural relationships, dynamic mechanisms.

**Applicable figure types:**
- Biological pathway diagrams (signaling cascades, metabolic pathways)
- AI/ML architecture diagrams (neural networks, data pipelines)
- Algorithm flowcharts (step-by-step computation)
- Chemical reaction mechanisms (synthesis routes, catalytic cycles)
- Engineering system diagrams (device operation, energy flow)
- Clinical disease mechanisms (pathophysiology cascades)
- Physical process diagrams (phase transitions, quantum processes)
- Environmental cycle diagrams (biogeochemical cycles)

**Trigger keywords (auto-detection):**
`mechanism`, `pathway`, `process`, `how`, `workflow`, `pipeline`, `architecture`, `cascade`, `signaling`, `step`, `flow`, `transformation`, `conversion`, `reaction`, `synthesis`, `operation`, `circuit`, `cycle`, `feedback`, `interaction`, `chain`, `sequential`, `signal`

**Narrative Structure — The Causal Chain:**

```
┌─────────────────────────────────────────────────────┐
│  CONTEXT: Where does this happen?                    │
│  (cellular compartment, system boundary, environment) │
├─────────────────────────────────────────────────────┤
│                                                     │
│  INPUT ──→ PROCESS STEP 1 ──→ INTERMEDIATE STATE    │
│                │                                     │
│                ├──→ PROCESS STEP 2a ──→ ┐           │
│                │                         │           │
│                └──→ PROCESS STEP 2b ──→ FUSION       │
│                                          │           │
│                                    FINAL OUTPUT      │
│                                                     │
├─────────────────────────────────────────────────────┤
│  KEY INSIGHT: What is novel or surprising?           │
│  (highlighted visually as the figure's focal point)  │
└─────────────────────────────────────────────────────┘
```

**Narrative prompt block (Layer N in final assembly):**

```
NARRATIVE MODE: Mechanism Diagram

FIGURE STORY STRUCTURE:
This figure must tell a causal mechanism story with the following narrative arc:

1. CONTEXT & SETUP: Establish where the mechanism operates. Show the system boundary, cellular compartment, or environmental context. This sets the stage — the reader should immediately know the domain and scale.

2. INPUT / STARTING STATE: Clearly depict the initial state, input signal, precursor molecules, or starting conditions that trigger the mechanism.

3. TRANSFORMATION SEQUENCE: Show the step-by-step causal chain of transformations, interactions, or processing steps. Each step must flow logically into the next. Critical intermediate states should be visible. The causal direction must be unambiguous (left→right or top→bottom).

4. KEY INTERACTIONS: Highlight the most important molecular interactions, computational operations, or physical processes. These are where the mechanism's specificity and novelty reside. Use visual emphasis (scale, color saturation, line weight) to mark these.

5. OUTPUT / END STATE: Show the final product, activated state, prediction, or outcome. The contrast between INPUT and OUTPUT should be visually apparent.

6. NOVELTY MARKER: One element in this chain must be visually distinguished as the NOVEL contribution — this could be a new component, a newly discovered interaction, an unexpected intermediate, or an innovative processing step. This is what makes this figure publishable.

NARRATIVE PRINCIPLES:
- The causal chain must be traceable by a reader unfamiliar with the work
- Every arrow must represent a real mechanistic relationship (not just "is related to")
- If a step is hypothetical, mark it with dashed lines and a "?" annotation
- The story should have a clear "before → after" or "without → with" arc
- The mechanism's biological/chemical/physical plausibility must be visually respected
```

---

### Mode B: Graphical Abstract Engine

**Purpose:** Communicate the paper's CORE CONTRIBUTION in a single, self-contained visual — designed for journal homepages, social media, and rapid comprehension.

**Applicable scenarios:**
- Journal Graphical Abstract / TOC image (Nature, Cell, ACS, Elsevier)
- Press release figure
- Conference poster hero image
- Grant proposal summary figure
- Social media research dissemination

**Trigger keywords (auto-detection):**
`graphical abstract`, `TOC`, `table of contents`, `cover`, `summary`, `highlight`, `graphic abstract`, `visual abstract`, `one figure`, `single image`, `overview`, `our contribution`, `significance`, `impact`, `key finding`, `main result`, `takeaway`

**Narrative Structure — The Impact Arc:**

```
┌──────────────────────────────────────────────────────┐
│                                                      │
│   PROBLEM ────→ INNOVATION ────→ RESULT             │
│   (left)        (center,        (right)              │
│   small/dark)   LARGEST/BRIGHT) large/bright)        │
│                                                      │
│                 ↓                                    │
│            SIGNIFICANCE                              │
│         (bottom, broad impact statement)             │
│                                                      │
└──────────────────────────────────────────────────────┘
```

**Narrative prompt block (Layer N in final assembly):**

```
NARRATIVE MODE: Graphical Abstract

FIGURE STORY STRUCTURE:
This figure is a graphical abstract — a self-contained visual summary of a research paper's core contribution. It must communicate the paper's essence to a browsing reader in under 5 seconds.

LAYOUT: Left→Center→Right flow with bottom significance band.

LEFT ZONE (25% width) — THE PROBLEM / KNOWLEDGE GAP:
- What problem does this paper address? What was unknown or unsolved?
- Render in darker, more muted tones — this represents the "before" state
- Keep to 1–2 visual elements maximum
- May include: diseased state, failed previous approach, question mark, knowledge gap symbol

CENTER ZONE (40% width) — THE INNOVATION / METHOD:
- What is the NEW approach, method, or discovery?
- This is the visual DOMINANT — largest scale, brightest colors, highest contrast
- Render in the most visually striking treatment the chosen style allows
- Include: the key novel component, mechanism, or methodology
- This zone should capture ~70% of initial viewer attention

RIGHT ZONE (25% width) — THE RESULT / OUTCOME:
- What did the innovation achieve? What is the "after" state?
- Render in bright, positive, resolved tones — this represents success
- Keep to 1–2 visual elements
- May include: healthy state, performance improvement, solved structure

BOTTOM BAND (10% height, full width) — THE SIGNIFICANCE:
- One line: the broader impact statement
- "Enables X for Y applications"
- Rendered as subtle text or a simple icon+text combination
- This band is visually subordinate but narratively essential

CRITICAL RULES FOR GRAPHICAL ABSTRACTS:
- Maximum 5 total visual elements (3 is ideal)
- Exactly ONE main color accent (the innovation)
- At least 40% white/empty space
- No figure panels (a, b, c...) — this is a SINGLE unified image
- Must work at 200px thumbnail size — test: can you still read the story?
- Text must be minimal (≤10 words total, ideally ≤5)
- The reading path must be unambiguous: Problem → Innovation → Result → Significance
- The viewer should understand the paper's contribution without reading the title
```

---

## Auto-Detection Logic

When the user provides their input, scan for keywords to determine the narrative mode:

```
if (any trigger from Mode B list) AND (user mentions "graphical abstract", "TOC", "cover", "summary figure"):
    → Mode B: Graphical Abstract Engine (confidence: HIGH)
elif (any trigger from Mode A list) AND (user describes a process/mechanism):
    → Mode A: Mechanism Diagram Engine (confidence: HIGH)
elif (user provides model architecture code):
    → Mode A: Mechanism Diagram Engine (confidence: HIGH)
elif (user describes problem→method→result structure):
    → Mode B: Graphical Abstract Engine (confidence: MEDIUM)
else:
    → Default to Mode A: Mechanism Diagram Engine (most common request)
```

Present the detection result to the user:

> "**Narrative Mode detected: [Mode A / Mode B]**  
> [One-line justification based on detected keywords]  
> Is this correct, or would you prefer the other mode?"

---

## Combined Mode (Advanced)

For users who want a figure that serves both purposes (mechanism detail + graphical abstract impact), use the **Hybrid Narrative**:

```
UPPER 70%: Mode A — Detailed mechanism with causal chain
LOWER 30%: Mode B — Condensed Problem→Innovation→Result→Significance band
```

This creates a figure that works as both an in-text mechanism diagram and a graphical abstract. Only offer this mode when the user explicitly requests a dual-purpose figure.
