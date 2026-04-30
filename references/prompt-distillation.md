# Prompt Distillation Engine

This module compresses the fully assembled, multi-layer prompt into image-model-optimized language. The goal: preserve ALL semantic constraints while reducing token count by 40–60%, converting verbose academic rules into the concrete visual vocabulary that text-to-image models respond to most reliably.

---

## Why Distillation Matters

Image generation models (DALL·E, Stable Diffusion, Midjourney, Flux) have specific prompt-sensitivity characteristics:

1. **Attention dilution:** Long prompts (>500 tokens) cause the model to lose focus on critical constraints. The model's cross-attention mechanism spreads thin across too many tokens.
2. **Concrete > Abstract:** Models respond better to "crisp 1.5pt outlines, flat colors" than to "maintain visual consistency and clarity across all structural elements."
3. **Visual vocabulary:** Models are trained on alt-text and caption datasets. They understand visual-descriptive language better than prescriptive rule language.
4. **Position bias:** Critical constraints placed early in the prompt receive more attention weight than those placed late.

---

## Two-Phase Distillation Process

### Phase 1: Rule → Visual Descriptor Translation

Convert each abstract quality rule into a concrete visual descriptor. Use the following transformation patterns:

#### Pattern A: Meta-instruction Removal

| Before (Verbose Rule) | After (Visual Descriptor) |
|-----------------------|--------------------------|
| "You must ensure that all elements are clearly visible and readable." | (DELETE — implied by quality) |
| "It is important to maintain consistency." | (DELETE — redundant with actual descriptors) |
| "Make sure the reader can understand..." | (DELETE — output quality, not input instruction) |
| "The figure should be designed to..." | (DELETE — preamble) |

#### Pattern B: Abstraction → Concrete Visual

| Abstract Rule | Concrete Visual Descriptor |
|---------------|---------------------------|
| "Maintain consistent color semantics across repeated biological entities while preserving grayscale distinguishability." | `consistent entity colors, grayscale-readable palette, ≥30% luminance gap` |
| "Ensure all arrow types are semantically consistent and unambiguous." | `solid arrows=activation, T-bar=inhibition, dashed=indirect, open=transport` |
| "The main mechanism must be visually dominant and identifiable within 3 seconds." | `dominant central mechanism, high contrast, largest element, 3-sec readability` |
| "Maximum 6 distinct colors. Colorblind-safe. No red-green-only contrasts." | `≤6 colors, deuteranopia-safe palette, no pure red-green pairing` |
| "Sans-serif font, 7–9pt, labels outside elements." | `Helvetica-style labels, 8pt, placed adjacent, no overlap` |

#### Pattern C: Multi-Constraint → Keyword Cluster

| Multiple Constraints | Compressed Cluster |
|---------------------|-------------------|
| "Use uniform-thickness outlines (1–2 pt). Flat solid colors with zero gradients. Exactly 4–6 distinct colors. Regular geometric shapes. Modular grid layout." | `clean vector: uniform 1.5pt strokes, flat 5-color palette, geometric, grid-aligned, zero gradients` |
| "Organic wobbly lines. Varied line weight (0.5–3pt). Asymmetric hand-drawn arrowheads. Off-white paper background. Muted pencil/ink colors." | `hand-drawn: organic wobbly strokes, variable weight 0.5-3pt, irregular arrowheads, cream paper bg, muted pencil tones` |

#### Pattern D: Structural → Spatial

| Structural Rule | Spatial Descriptor |
|-----------------|-------------------|
| "Elements arranged on a modular grid with equal spacing." | `grid-aligned, equal pitch, mathematically precise spacing` |
| "Three-tier visual hierarchy with distinct scale and saturation per level." | `3-level depth: large/saturated→medium/muted→small/pale` |
| "Generous margins with at least 8% empty space on all sides." | `≥8% margin, breathing room, framed composition` |

---

### Phase 2: Priority-Ordered Reassembly

After translating all rules to visual descriptors, reassemble the prompt in priority order. Image models weight early tokens more heavily.

#### Priority Ordering Rules

1. **HIGHEST PRIORITY (first 15% of prompt):** Style identity + Layout type
   - "Clean flat vector scientific schematic" or "Hand-drawn organic whiteboard sketch"
   - "Horizontal pipeline layout" or "Central hub composition"

2. **HIGH PRIORITY (next 20%):** Key visual constraints + Core elements
   - Color palette rules, line quality, critical spatial relationships
   - The 2–3 most important components and their positions

3. **MEDIUM PRIORITY (next 30%):** Detailed conventions + Secondary elements
   - Discipline-specific visual grammar
   - Supporting components and their relationships

4. **LOWER PRIORITY (next 25%):** Quality standards (compressed) + Fine details
   - Accessibility rules, typography, technical specs
   - Annotations, labels, fine spatial adjustments

5. **LOWEST PRIORITY (final 10%):** Negative constraints
   - What NOT to include
   - Style guardrails

---

## Distillation Templates

### Style Distillation (Layer 3 compressed)

**Classic Vector:**
```
clean flat vector scientific diagram, uniform 1.5pt crisp strokes, 5-color restrained palette, geometric rounded rectangles, strict grid layout, pure white background, sharp triangular arrowheads, no gradients no shadows no textures
```

**Hand-Drawn Sketch:**
```
organic hand-drawn whiteboard sketch, wobbly pen strokes variable 0.5-3pt weight, irregular asymmetrical arrowheads, cream paper texture background #FAFAF5, muted pencil-ink palette (grey teal brick olive), varied lettering, intentional slight imperfections, approachable notebook aesthetic
```

**Minimal Infographic:**
```
editorial infographic, 40% whitespace minimum, 3-color palette (charcoal + one accent + light grey), geometric icon-based representation, thin 0.5pt elegant lines, bold headline + light label typography, strict grid generous margins, apple-design refinement
```

**Scientific Illustration:**
```
professional textbook scientific illustration, semi-realistic biological rendering, soft naturalistic shading upper-left 5500K key light, accurate anatomical proportions, 10-color tonal palette, detailed surface textures (membrane lipid bilayer, nuclear pores, ECM fibrous), subtle depth of field, Nature Reviews quality
```

**Futuristic Tech:**
```
dark tech visualization #0A0A1A background with subtle grid, neon cyan #00E5FF blue #4488FF magenta #FF44AA purple #8844FF glowing lines 2-4px bloom, glass-morphism nodes 60% opacity with bright edge highlights, data particle streams, volumetric light rays, conference-keynote aesthetic
```

**Hybrid:**
```
three-layer visual hierarchy: Layer1 clean-vector structural framework muted blues greys, Layer2 hand-drawn emphasis on 2-3 key innovations warm orange deep blue thicker strokes, Layer3 scientific-illustration contextual cells molecules tissues softer thinner lighter, warm-grey #F8F7F4 background, multi-depth reading experience
```

**3D Render:**
```
photorealistic 3D scientific render, three-point studio lighting (key 60% upper-left 5500K, fill 30% lower-right, rim 40% upper-back 6500K), physically-accurate materials (glass IOR1.5, metallic roughness0.2, biological subsurface scattering), 50-85mm perspective camera with subtle depth-of-field, procedural surface textures, Blender-quality output
```

### Quality Standards Distillation (Layer 4 compressed)

```
PUBLICATION QUALITY: 3-level visual hierarchy (dominant primary→medium secondary→subtle tertiary), single consistent left-to-right flow direction, ≤6 deuteranopia-safe colors with ≥30% luminance gap, semantically consistent arrows (solid→=activate, T-bar⊣=inhibit, dashed⇢=indirect, open⟶=transport, curved↻=feedback), sans-serif 7-9pt labels adjacent to elements, ≥8% margins all sides, grid-aligned composition, 3-second readability at thumbnail size, grayscale-distinguishable, no AI artifacts no gibberish text no impossible geometries no inconsistent lighting
```

---

## Complete Distilled Prompt Format

After distilling each layer, assemble the final prompt in this EXACT order:

```
[STYLE IDENTITY + LAYOUT TYPE] (first ~15%)

[DISCIPLINE CONTEXT — compressed to 2–3 sentences] (~10%)

[LAYOUT ARRANGEMENT — element positions, sizes, reading path] (~15%)

[NARRATIVE ARC — the story structure] (~10%)

[KEY COMPONENTS — the user's specific content, structured spatially] (~25%)

[VISUAL CONSTRAINTS — compressed style rules, color, line quality] (~15%)

[QUALITY STANDARDS — compressed to essential keywords] (~5%)

[NEGATIVE CONSTRAINTS — what to avoid] (~5%)
```

**Target total length:** 250–400 words (down from 800–1500 words in the full layered prompt).

---

## Distillation Execution

When the skill reaches the distillation phase:

1. **Read the full assembled prompt** (output of Phase 4/5 in the main workflow)
2. **Apply Phase 1 transformations:** Convert each sentence using the patterns above
3. **Apply Phase 2 priority ordering:** Reorder into the priority template
4. **Verify constraint preservation:** Check that all critical constraints survived:
   - ✅ Color accessibility (deuteranopia-safe)
   - ✅ Arrow semantics (consistent types)
   - ✅ Visual hierarchy (3 levels)
   - ✅ Reading path (unambiguous flow)
   - ✅ Scientific accuracy markers (hypothetical = dashed)
   - ✅ Style identity (not degraded by compression)
5. **Output the distilled prompt** alongside the full prompt

---

## User Presentation

Present both versions to the user:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 FULL PROMPT (for review & understanding)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Complete 5-layer prompt, ~800-1500 words]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ DISTILLED PROMPT (for image generation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Compressed prompt, ~250-400 words]

The distilled prompt is 60% shorter while preserving all critical constraints.
This is what will be sent to the image generation API for optimal results.

Proceed with the distilled prompt? (y/n)
Or would you prefer to use the full prompt?
```
