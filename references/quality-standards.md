# Top-Tier Quality Standards

This is the universal quality standards prompt. It is ALWAYS appended as Layer 4 of the final image generation prompt, regardless of the discipline or style selected.

---

## Full Quality Standards Prompt

Include the following block verbatim as Layer 4:

```
QUALITY STANDARDS — TOP-TIER PUBLICATION REQUIREMENTS:

These quality standards are non-negotiable. Every element of the generated figure must satisfy them.

═══════════════════════════════════════════
SECTION A: CLARITY & IMMEDIATE READABILITY
═══════════════════════════════════════════

1. THREE-SECOND RULE: The main mechanism must be visually dominant and immediately identifiable within 3 seconds of first viewing. A reader glancing at this figure should instantly know (a) what the topic is, (b) what the main flow or process is, and (c) what the single most important finding or component is.

2. SINGLE FLOW DIRECTION: Establish one consistent visual flow direction — either left→right OR top→bottom — and maintain it throughout the entire figure. Never mix flow directions (e.g., some arrows going left→right while others go top→bottom) as this destroys readability. The only exception is feedback/return loops, which may curve back against the main flow direction.

3. EVERY ELEMENT MUST EARN ITS PLACE: Remove any purely decorative element that does not contribute to scientific understanding. If removing something doesn't reduce comprehension, remove it. Visual economy is a virtue.

4. ELEMENT COUNT DISCIPLINE: Use exactly 3–7 key structural elements as the primary visual components. If the mechanism has more than 7 steps or components, group them into 3–7 logical clusters with clear visual grouping (surrounding boxes, background zones, or brackets).

═══════════════════════════════════════════
SECTION B: VISUAL HIERARCHY (THREE LEVELS)
═══════════════════════════════════════════

5. THREE-TIER VISUAL HIERARCHY:
   - PRIMARY (Level 1): The core mechanism pathway — largest scale, most saturated colors, thickest lines, highest contrast against background. These elements must dominate the visual field.
   - SECONDARY (Level 2): Supporting details and annotations — medium scale, moderately muted colors, medium line weight. These provide necessary detail without competing with Level 1.
   - TERTIARY (Level 3): Contextual elements, background structures, fine annotations — smallest scale, lightest/most muted colors, thinnest lines. These add depth and context without demanding attention.

6. The reader's eye must follow this natural attention sequence: Level 1 (immediate, <1 sec) → Level 2 (secondary scan, 2–5 sec) → Level 3 (detailed study, 10+ sec). You can verify this by squinting at the figure — only Level 1 elements should remain clearly visible.

═══════════════════════════════════════════
SECTION C: COLOR STANDARDS
═══════════════════════════════════════════

7. COLOR COUNT: Maximum 6 distinct hues in total across the entire figure (excluding white, grey, and black which are neutrals). More than 6 colors creates cognitive overload and visual chaos.

8. ACCESSIBILITY (COLOR VISION DEFICIENCY): Every pair of adjacent or interacting colors must be distinguishable by readers with deuteranopia (red-green color blindness, affecting ~6% of males) and protanopia (~2% of males). Specifically:
   - NEVER rely solely on red vs. green to convey a distinction
   - If red and green must both be used, ensure at least 30% luminance difference between them, AND add a secondary encoding (shape difference, texture, label)
   - Prefer red vs. blue, orange vs. purple, or yellow vs. dark blue for critical distinctions
   - Test: the figure must remain fully interpretable when converted to grayscale

9. CONSISTENT COLOR CODING: Any entity (protein, module, component, cell type, material phase, particle species) that appears in multiple locations or panels within the figure MUST have exactly the same color in every instance. Color is an information channel — inconsistency corrupts that channel.

10. SEMANTIC COLOR CONVENTIONS:
    - Warm colors (red, orange, amber, warm yellow) = active, stimulated, upregulated, diseased, high-energy, unstable
    - Cool colors (blue, teal, indigo, purple) = inactive, inhibited, downregulated, healthy/basal, low-energy, stable
    - Neutral colors (grey, white, black, beige) = structural, background, reference, baseline state
    - Green = context-dependent: may indicate "go/active" (traffic light convention) OR "natural/healthy/control" (biological convention) — use with explicit context

═══════════════════════════════════════════
SECTION D: ARROW & CONNECTION SEMANTICS
═══════════════════════════════════════════

11. ARROW TYPES MUST BE SEMANTICALLY CONSISTENT. Use the following conventions and NEVER deviate from them within a single figure:
    - → Solid arrow with filled triangular head = DIRECT activation, promotion, transformation, or conversion
    - ⊣ Solid line with perpendicular T-bar termination = DIRECT inhibition, blocking, suppression, or negative regulation
    - ⇢ Dashed or dotted arrow = INDIRECT mechanism, hypothetical pathway, unknown mechanism, or speculative connection
    - ↻ Curved arrow returning to an earlier point = FEEDBACK loop (positive feedback = marked with ⊕, negative = marked with ⊖, or use color: red=positive, blue=negative)
    - ⟶ Arrow with open/unfilled head = TRANSLOCATION, transport, movement from one compartment to another
    - ─ Thin connector line without arrowhead = PHYSICAL ASSOCIATION, binding, complex formation (not directional)

12. ARROW CLARITY: Arrows must not cross each other unless absolutely unavoidable. If arrows must cross, use a small "bridge" (one arrow arcs over the other) to avoid visual ambiguity. Arrows should have clear start and end points — the reader should never wonder "where does this arrow start or end?"

═══════════════════════════════════════════
SECTION E: TYPOGRAPHY & LABELING
═══════════════════════════════════════════

13. FONT: Sans-serif throughout (Arial, Helvetica, or closest visual equivalent). No serif fonts, no decorative fonts, no handwriting fonts (unless the entire figure is Hand-Drawn Sketch style, in which case use hand-lettered style consistently).

14. FONT SIZE: All labels 7–9 pt equivalent at the figure's final publication size. Nothing smaller than 6 pt. Key terms or main titles may be 10–12 pt.

15. LABEL PLACEMENT: Labels must be outside or adjacent to the elements they identify — never overlapping with structural lines, shapes, or other labels. Use leader lines (thin lines from label to element) if necessary.

16. TEXT ORIENTATION: All text must be horizontal (left-to-right reading direction). Rotated or vertical text is forbidden. The single exception is y-axis labels on graphs, which may be rotated 90° counterclockwise.

17. ABBREVIATIONS: Use full names for the first occurrence of any term; use a compact legend box for complex multi-element abbreviations rather than cluttering the figure with dozens of labels.

═══════════════════════════════════════════
SECTION F: COMPOSITION & LAYOUT
═══════════════════════════════════════════

18. MARGINS: Maintain generous margins — at least 8% of the total canvas dimension on all four sides must be empty space. This is not wasted space; it frames the content and improves readability.

19. ALIGNMENT: All elements must be aligned to an underlying grid. Nothing should be placed arbitrarily — every element's position should relate systematically to other elements. Consistent spacing between parallel elements.

20. MULTI-PANEL LAYOUT (if applicable): Panels must be of consistent size, aligned in a regular grid. Panel labels (a, b, c, d...) must be in the same position for every panel (convention: upper-left corner of each panel, bold, 10–12 pt). The reading order must be obvious: left→right then top→bottom (Z-pattern) or top→bottom then left→right.

═══════════════════════════════════════════
SECTION G: NARRATIVE STRUCTURE
═══════════════════════════════════════════

21. THREE-PART STORY ARC: Every mechanism diagram should have a discernible narrative:
    - CONTEXT/SETUP: Where does the mechanism operate? What is the starting state?
    - MECHANISM/ACTION: What happens? What are the key steps, interactions, transformations?
    - OUTCOME/RESULT: What is the consequence? What changes from the starting state?

22. INNOVATION EMPHASIS: The novel contribution — the new mechanism, the unexpected interaction, the key insight — must be visually prominent. It should be a Level 1 element. If the reader cannot identify what is new about this mechanism, the figure has failed its primary purpose.

═══════════════════════════════════════════
SECTION H: SCIENTIFIC ACCURACY & INTEGRITY
═══════════════════════════════════════════

23. SPATIAL PLAUSIBILITY: All relative positions, sizes, and spatial relationships must be scientifically plausible. A protein cannot be larger than the cell that contains it. A molecule cannot pass through a membrane without a transporter or channel (unless it is explicitly lipophilic). Organelles must be in their correct cellular locations.

24. UNCERTAINTY DISCLOSURE: If any step or interaction in the mechanism is hypothetical, speculative, or not yet experimentally validated, it MUST be visually distinguished:
    - Use dashed lines instead of solid lines
    - Use lighter, more muted colors
    - Add a small "?" annotation or "[hypothetical]" label
    - Never present speculation with the same visual confidence as established fact

25. DO NOT INVENT: Do not create molecular structures, binding interactions, post-translational modifications, or mechanistic details that are not supported by the user's input. If the user's description is vague about a step, render it with appropriate uncertainty markers. It is better to be vague and honest than specific and wrong.

26. PROPORTIONALITY: Where scale information is known, respect it. If a mitochondrion (typically ~0.5–1 μm wide and ~2–8 μm long) is shown next to a protein complex (typically ~5–20 nm), the size ratio should be approximately correct (~50–100× difference), not literal but not absurd.

═══════════════════════════════════════════
SECTION I: TECHNICAL PRODUCTION STANDARDS
═══════════════════════════════════════════

27. RESOLUTION: Generate at the equivalent of 300 dpi at final print size. For a full-page figure (~175 mm wide), this means approximately 2100 pixels across minimum.

28. COLOR SPACE: Render in RGB color space (standard for digital submission). Do not simulate CMYK — the conversion happens at the publisher.

29. SCALEABILITY: The figure must remain clear and legible at BOTH full-page width AND thumbnail/smartphone size (approximately 400 px wide). Test mentally: at thumbnail size, the Level 1 mechanism should still be discernible, even if Level 2 and 3 details are lost.

30. NO AI ARTIFACTS: The generated image must not contain:
    - Gibberish pseudo-text (AI-generated nonsense letterforms)
    - Anatomically impossible structures (cells with two nuclei, inside-out organelles)
    - Escher-like impossible geometries (arrows that feed into themselves, M.C. Escher-style spatial paradoxes)
    - Blurry or smeared edges on elements that should be sharp
    - Inconsistent lighting that betrays multiple light sources or impossible shadows
```
