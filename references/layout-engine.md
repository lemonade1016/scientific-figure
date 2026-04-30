# Auto Layout Engine

This module automatically determines the optimal spatial arrangement for the scientific figure. It analyzes the user's content, classifies the figure type, assigns visual weights, selects the reading path, and generates layout instructions for the image generation prompt.

---

## Phase 1: Figure Type Classification

Analyze the user's content (after Phase 3 input collection) and classify into one of 6 layout types.

### Type 1: Pipeline Layout (Sequential Flow)

**Visual signature:**
```
[Input] ──→ [Step 1] ──→ [Step 2] ──→ [Step 3] ──→ [Output]
```

**Best for:** AI/ML workflows, chemical synthesis routes, signal transduction cascades, data processing pipelines, multi-step algorithms, manufacturing processes, linear mechanisms

**Detection keywords:** `step by step`, `first...then...finally`, `pipeline`, `workflow`, `sequential`, `chain`, `successive`, `stage`, `phase`, `feedforward`, `forward pass`, `propagation`, `synthesis route`, `signal cascade`, `processing pipeline`

**Detection pattern:** 3+ sequential steps with clear before/after relationships, linear dependency chain

**Layout rules:**
- Horizontal arrangement (left→right) for ≤5 steps; 2-row wrap for 6+ steps
- Elements equally spaced along the horizontal axis
- Arrow connectors between consecutive elements (→)
- Optional: phase grouping with background zones for multi-stage pipelines
- Novel/intermediate elements placed at 1/3 or 2/3 horizontal position (NOT at edges)
- Aspect ratio: 16:9 or wider (2.35:1 for long pipelines)

---

### Type 2: Central Hub Layout (Core Innovation Focus)

**Visual signature:**
```
         [Module A]
            ↑
[Module B] ← ★ CORE ★ → [Module C]
            ↓
         [Module D]
```

**Best for:** Novel framework papers, system architectures with a central controller, multi-modal fusion systems, hub-and-spoke biological signaling, centralized processing architectures

**Detection keywords:** `centered around`, `core`, `central`, `hub`, `our framework`, `proposed system`, `integrates`, `fuses`, `combines multiple`, `multi-modal`, `orchestrates`, `coordinates`, `main module`, `central processor`

**Detection pattern:** One dominant element described as coordinating/connecting multiple other elements, "our method" language

**Layout rules:**
- Core innovation at geometric center (largest element, highest visual weight)
- Supporting modules arranged radially around center (top, right, bottom, left)
- ≤6 radial modules (4 is ideal — one per cardinal direction)
- Bidirectional arrows or data flow lines connecting center ↔ each module
- Center element: 2–3× the visual area of each radial element
- Aspect ratio: 1:1 (square) or 4:3
- Reading order: center → top → right → bottom → left (clockwise from top)

---

### Type 3: Layered Stack Layout (Hierarchical Architecture)

**Visual signature:**
```
┌──────────────────────────┐
│     Input / Embedding     │
├──────────────────────────┤
│   Encoder / Processing    │
│   (may have sub-layers)   │
├──────────────────────────┤
│   Bottleneck / Fusion     │
├──────────────────────────┤
│   Decoder / Generation    │
├──────────────────────────┤
│    Output / Prediction    │
└──────────────────────────┘
```

**Best for:** Deep learning architectures (Transformer, CNN, RNN), encoder-decoder models, OSI network stacks, hierarchical processing systems, multi-scale models (if vertical scale hierarchy)

**Detection keywords:** `encoder`, `decoder`, `layer`, `stack`, `hierarchical`, `bottom-up`, `top-down`, `low-level`, `high-level`, `feature level`, `multi-scale`, `pyramid`, `embedding layer`, `hidden layer`, `output layer`, `transformer block`, `attention layer`, `feed-forward`, `convolutional layer`

**Detection pattern:** Named layers/modules stacked vertically or described with level/scale hierarchy

**Layout rules:**
- Vertical stack, top→bottom data flow (input at top, output at bottom)
- Each layer is a horizontal rectangle spanning 70–80% of canvas width
- Layer height proportional to its importance (novel layers = taller)
- Skip connections shown as curved arrows on the right side, bypassing layers
- Sub-layers within a block shown as internal horizontal subdivisions
- Equal horizontal margins for all layers
- Aspect ratio: 9:16 (portrait) or 3:4

---

### Type 4: Biological Spatial Layout (Compartment-Based)

**Visual signature:**
```
┌──────────────────────────────┐
│    EXTRACELLULAR SPACE        │
│  [Ligand] [Antibody]         │
├──────────────────────────────┤
│    PLASMA MEMBRANE            │
│  [Receptor] [Channel]        │
├──────────────────────────────┤
│    CYTOPLASM                  │
│  [Signaling proteins]        │
│  [Second messengers]         │
├──────────────────────────────┤
│    NUCLEUS                    │
│  [Transcription factors]     │
│  [DNA]                       │
└──────────────────────────────┘
```

**Best for:** Cell biology mechanisms, signaling pathways, membrane transport, intracellular trafficking, tissue-level processes, drug delivery mechanisms, subcellular localization

**Detection keywords:** `extracellular`, `intracellular`, `membrane`, `cytoplasm`, `nucleus`, `mitochondria`, `ER`, `golgi`, `endosome`, `lysosome`, `plasma membrane`, `cell surface`, `cytosol`, `organelle`, `compartment`, `translocation`, `transport`, `uptake`, `secretion`, `endocytosis`, `exocytosis`, `nuclear translocation`

**Detection pattern:** Spatial compartment references (especially membrane, cytoplasm, nucleus triad)

**Layout rules:**
- Vertical stack of compartments with clear boundaries
- Extracellular space at TOP
- Plasma membrane as a distinct HORIZONTAL BAND (thin, ~5–8% of height)
- Cytoplasm as the largest central zone (~40–50% of height)
- Organelles (nucleus, mitochondria, ER) as distinct shapes within cytoplasm zone
- Nucleus at BOTTOM center (large oval, ~20–25% of area)
- Transmembrane proteins must span the membrane band
- Translocation arrows must cross compartment boundaries
- Aspect ratio: 3:4 or 2:3 (portrait)
- Compartment labels: subtle text at the edge of each zone

---

### Type 5: Branching Tree Layout (Decision/Classification)

**Visual signature:**
```
              [Root / Start]
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
    [Decision A]        [Decision B]
          │                   │
     ┌────┴────┐         ┌────┴────┐
     ↓         ↓         ↓         ↓
  [Outcome] [Outcome] [Outcome] [Outcome]
```

**Best for:** Clinical decision trees, diagnostic algorithms, classification systems, phylogenetic trees, fault tree analysis, treatment guidelines, differential diagnosis pathways

**Detection keywords:** `if...then`, `decision`, `branching`, `classification`, `diagnostic`, `differential`, `criteria`, `algorithm`, `decision tree`, `triage`, `stratification`, `subtype`, `either...or`, `depending on`, `conditional`

**Detection pattern:** Binary/multi-way branching logic, conditional pathways, "if X then Y else Z" structures

**Layout rules:**
- Root node at TOP center
- Branches split downward at decision nodes (diamond shape for decisions, rectangle for processes)
- Terminal nodes (outcomes) at BOTTOM
- Decision nodes: diamond ◆ (standard flowchart convention)
- Process nodes: rectangle
- Outcome nodes: rounded rectangle or oval
- Branch labels: short condition text on each branch line
- Tree should be balanced (equal visual weight on left and right halves)
- Aspect ratio: 2:3 or 3:4 (portrait)
- Edge-to-edge margins: 12% (trees need more breathing room)

---

### Type 6: Cyclic Loop Layout (Feedback & Cycles)

**Visual signature:**
```
        [Process A] ←── [Process D]
            │               ↑
            ↓               │
        [Process B] ──→ [Process C]
```

**Best for:** Metabolic cycles (TCA, Calvin), biogeochemical cycles (C, N, P, water), feedback regulation loops, circadian rhythms, limit cycles, virtuous/vicious cycles, iterative optimization loops, reinforcement learning loops

**Detection keywords:** `cycle`, `loop`, `feedback`, `circular`, `regeneration`, `recycling`, `iterative`, `recurrent`, `closed loop`, `positive feedback`, `negative feedback`, `oscillation`, `rhythm`, `turnover`, `back to`, `returns to`, `cyclic`

**Detection pattern:** Process descriptions where the output feeds back to an earlier step, closed loops, circular dependencies

**Layout rules:**
- Circular or elliptical arrangement of process nodes
- Clockwise flow direction (standard convention for cycles)
- Each node placed at equal angular intervals
- Primary input INTO the cycle at TOP or LEFT
- Primary output/waste OUT of the cycle at BOTTOM or RIGHT
- Feedback connectors: curved arrows along the outside of the circle
- Positive feedback marked with ⊕ (reinforcing), negative with ⊖ (damping)
- Aspect ratio: 1:1 (square)
- Central area of the cycle may contain: cycle name, key enzyme/rate-limiting step, or the overall outcome

---

## Phase 2: Visual Weight Computation

Assign an importance score (1–10) to each component extracted from the user's input. This determines relative size, color saturation, and spatial prominence.

### Scoring Rules

| Signal | Score | Rationale |
|--------|-------|-----------|
| Explicitly labeled as "novel", "our", "proposed", "new", "key", "core", "innovation" | 10 | The paper's contribution — must dominate visually |
| Described with superlatives or uniqueness claims ("first", "only", "breakthrough") | 10 | |  
| Named as the main research object (the protein of interest, the model name, the drug candidate) | 9 | Central subject |
| Described as "critical", "essential", "rate-limiting", "bottleneck" | 8 | Key constraint or control point |
| Described as "important", "significant", "major" | 7 | Important but not central |
| Standard components of the described system (common pathways, typical layers, known intermediates) | 5 | Necessary context |
| Supporting/auxiliary elements (buffers, solvents, standard conditions, helper functions) | 3 | Background context |
| Environmental context (cellular compartment, system boundary, experimental setup) | 3 | Scene-setting |
| Optional/additional elements mentioned with "also", "additionally", "furthermore" | 2 | Peripheral |

### Weight-to-Visual Translation

Translate importance scores into visual properties:

| Score | Relative Size | Color Saturation | Line Weight | Position |
|-------|--------------|-----------------|-------------|----------|
| 10 | 100% (reference) | 100% (full saturation) | 2.5–3 pt | Center or focal point |
| 8–9 | 80% | 85% | 2 pt | Adjacent to center |
| 6–7 | 65% | 70% | 1.5 pt | Mid-periphery |
| 4–5 | 50% | 55% | 1 pt | Periphery |
| 1–3 | 35% | 35% | 0.5 pt | Edge or background |

### Spatial Hierarchy

The highest-scoring component (score 10) must be:
- Placed at the layout's natural focal point (center for Central Hub, 1/3 position for Pipeline, center of the largest compartment for Biological Spatial)
- 2–3× the visual area of score-5 components
- The most color-saturated element in the composition
- The termination point of the primary reading path

---

## Phase 3: Reading Path Generation

Define the explicit visual path the viewer's eye should follow. This must be translated into spatial arrangement instructions for the image model.

### Path Types

**Z-Path (Pipeline, some Layered Stacks):**
```
Top-Left ──────────→ Top-Right
                        │
                        ↓
Bottom-Left ←───── Bottom-Right
```
- Default for Western-reader scientific figures
- Implemented via: left→right flow of primary elements, top-row then bottom-row
- Use when the mechanism has a clear sequential flow AND fits in 2 rows

**F-Path (Branching Trees, Decision diagrams):**
```
Top-Left ──→ Top-Right
    │
    ↓
Mid-Left ──→ Mid-Right
    │
    ↓
Bottom-Left
```
- Default for tree diagrams and text-heavy infographics
- Implemented via: vertical reading interrupted by horizontal scans

**Center-Out (Central Hub):**
```
Center → Top → Right → Bottom → Left
```
- For hub-and-spoke layouts
- Core innovation viewed first, then supporting modules clockwise

**Top-Down (Layered Stack, Biological Spatial):**
```
Top → Bottom (straight vertical scan)
```
- For hierarchical, compartmental, and vertical stack layouts
- Data/concept flows from top to bottom

**Clockwise (Cyclic Loop):**
```
12 o'clock → 3 → 6 → 9 → back to 12
```
- For cycle diagrams
- Entry point at top (12 o'clock position)

### Reading Path Implementation in Prompt

Translate the chosen path into explicit spatial language:

```
READING PATH: [Path Type]
- The viewer's eye must enter at [START POSITION]
- Flow [DIRECTION] through the primary elements
- The key innovation at [POSITION] must receive focus second (after initial orientation)
- Exit at [END POSITION] where the outcome/conclusion resides
- No element may pull attention against this flow direction
```

---

## Phase 4: Whitespace & Margin Optimization

### Spacing Rules

| Rule | Value | Rationale |
|------|-------|-----------|
| Inter-element gap | ≥ 20% of average element width | Prevents visual crowding; allows each element to "breathe" |
| Edge margin (all sides) | ≥ 8% of canvas dimension | Frames the content; prevents edge-clipping in publication |
| Center zone reservation | Center 30% of canvas reserved for highest-weight element | Creates natural focal point |
| Group spacing | Gap between logical groups ≥ 1.5× inter-element gap | Distinguishes functional modules |
| Arrow clearance | Arrows must not pass within 10px of unrelated elements | Prevents visual tangling |

### Margin Calculation

```
canvas_width = W, canvas_height = H
margin_x = max(0.08 * W, 60px)
margin_y = max(0.08 * H, 40px)
usable_width = W - 2 * margin_x
usable_height = H - 2 * margin_y
```

All primary elements must be placed within the usable area. Background elements may extend into margins.

---

## Phase 5: Layout Prompt Assembly

After completing Phases 1–4, assemble the layout instructions into a prompt block for Layer L (Layout) of the final prompt:

```
LAYOUT TYPE: [Detected Type Name]

SPATIAL ARRANGEMENT:
- [Specific arrangement description from the layout type rules]
- [Element placement: which component goes where, based on visual weight scores]
- [Size hierarchy: the [highest-weight element] is the largest element, at visual center]
- [Connector routing: how arrows/connections flow between elements]

READING PATH: [Path Type]
- Eye enters at [position], flows [direction] to [position], exits at [position]
- The path must feel natural and unforced

SPACING:
- Element spacing: [X]% of element width minimum
- Margins: [X]% on all sides
- Center zone reserved for: [highest-weight element name]

DIMENSIONAL GUIDANCE:
- Recommended aspect ratio: [ratio]
- Total distinct elements: [count]
- Maximum nesting depth: [depth if hierarchical]
```

---

## Quick Detection Reference

When processing user input, scan for these patterns and count matches. The layout type with the most keyword matches wins. In case of a tie, prefer: Pipeline > Central Hub > Layered Stack > Biological Spatial > Branching Tree > Cyclic Loop.

| Layout Type | Keyword Density Check |
|-------------|----------------------|
| Pipeline | `step`, `then`, `pipeline`, `sequential`, `workflow`, `chain`, `propagat`, `stage`, `phase` |
| Central Hub | `core`, `central`, `hub`, `our`, `proposed`, `framework`, `integrat`, `fus`, `coordinat` |
| Layered Stack | `layer`, `stack`, `encoder`, `decoder`, `hierarch`, `level`, `block`, `embed` |
| Biological Spatial | `membrane`, `cytoplasm`, `nucleus`, `extracellular`, `compartment`, `organelle`, `translocat`, `transport` |
| Branching Tree | `if`, `decision`, `branch`, `classif`, `diagnos`, `criterion`, `either`, `depend` |
| Cyclic Loop | `cycle`, `loop`, `feedback`, `circular`, `regenerat`, `recycl`, `rhythm`, `iterat`, `oscillat` |
