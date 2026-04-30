# Style Prompt Library

Each style has a pre-built prompt block that captures the specific visual aesthetic, line quality, color treatment, lighting, texturing, and overall artistic direction. Select the block matching the user's Phase 2 choice and include it verbatim as Layer 3 of the final prompt.

---

## Style 1: Classic Vector — Clean Journal Style

```
STYLE: Classic Vector — Clean Journal Schematic

VISUAL INSTRUCTIONS:
- Render as a clean, flat vector illustration suitable for direct journal submission to Nature, Cell, or Science
- Use uniform-thickness outlines (1–2 pt stroke weight) for all structural elements — no variation in stroke weight between different components
- Apply flat, solid fill colors with zero gradients — use exactly 4–6 distinct colors total across the entire figure. Colors must be from a restrained, professional palette (no neon, no pastels, no overly saturated primaries)
- All shapes must be regular geometric primitives: rounded rectangles (corner radius 3–4pt), perfect circles, straight orthogonal lines (horizontal and vertical only, no diagonals unless representing a specific geometric relationship), equilateral triangles for directional markers
- Arrange all elements on a strict modular grid with equal spacing between components. Alignment must be mathematically precise — use consistent horizontal and vertical pitch
- Arrowheads must be sharp, uniform triangles with consistent size (6–8pt base width) — solid filled triangular arrowheads for activation/promotion, T-bar terminations (perpendicular line caps) for inhibition, open/unfilled arrowheads for translocation/transport
- Background: pure white (#FFFFFF) with no texture, no vignette, no gradient, no watermark
- Typography: clean sans-serif labels (Arial or Helvetica equivalent), 7–9 pt size at final figure dimensions, black (#000000) or dark grey (#333333), placed outside or adjacent to structural elements, never overlapping with lines or shapes
- Absolutely do NOT include: drop shadows, glows, textures, 3D extrusions, photographic elements, hand-drawn marks, gradients of any kind, multiple font families, decorative borders, emoji or icons
- The overall impression should be: "This could appear in the main figures section of Nature Methods — clean, precise, universally acceptable."
```

---

## Style 2: Hand-Drawn Sketch — Whiteboard Thinking Style

```
STYLE: Hand-Drawn Sketch — Research Notebook or Whiteboard Aesthetic

VISUAL INSTRUCTIONS:
- Render as an organic, hand-drawn sketch on a virtual whiteboard or researcher's notebook page
- All lines MUST appear hand-drawn: they should be slightly wobbly and imperfect with natural variation in trajectory — absolutely no perfectly straight lines, no geometrically perfect shapes, no machine-precision curves. Lines should have the slight irregularity of a human hand holding a pen
- Line weight must vary organically: thicker strokes (2–3 pt equivalent, like pressing harder with a marker) for primary structural elements and main flow arrows, thinner strokes (0.5–1 pt equivalent, like a lighter pen touch) for secondary details, annotations, and background context — as if drawn with varying pressure on a physical pen or marker
- Arrowheads must look hand-drawn: asymmetric, slightly irregular triangular shapes or simple V-stroke terminations — never perfect machine-rendered triangular arrowheads. Some arrowheads may have one side slightly longer or angled differently than the other
- Background: off-white or very light warm cream (#FAFAF5 to #F5F0E8) with subtle paper texture or extremely light grain — like high-quality sketch paper or a whiteboard surface
- Color palette: use muted, natural tones — pencil grey (#555555), ink black (#222222), soft slate blue (#6A8D9E), muted brick red (#C2786A), olive green (#7A9A6E), ochre yellow (#D4B872) — as if drawn with colored pencils or fine-tip markers on paper. Avoid saturated digital colors, neon tones, or glossy finishes
- Typography: labels and annotations should appear hand-lettered — informal sans-serif with slight natural irregularity in letter spacing and baseline alignment. Letters should vary subtly in size and angle. Text should feel like someone annotated a whiteboard, not like typeset labels
- Embrace slight imperfections: labels ever so slightly tilted (1–3° off horizontal), elements not perfectly aligned, some sketch marks or crossing lines that extend a tiny bit past their meeting points, occasional small decorative marks or dots at the end of important lines
- Do NOT make it look messy, sloppy, or unprofessional — it should feel like the polished whiteboard explanation from a particularly clear-thinking colleague who has explained this concept many times. The imperfections should feel intentional and charming, not careless
- Overall impression: "A brilliant researcher just drew this on their office whiteboard to explain their key idea — it's informal but perfectly clear."
```

---

## Style 3: Minimal Infographic — High-Impact Communication Style

```
STYLE: Minimal Infographic — High-Impact Editorial Communication

VISUAL INSTRUCTIONS:
- Render as a magazine-quality editorial infographic with extreme visual restraint and sophistication
- White space is the dominant visual element: at least 40% of the total canvas area must remain completely empty (no text, no lines, no fills, no elements of any kind). This breathing room is what gives the style its power
- Color palette: Use exactly 2–4 colors total for ALL elements. One dominant dark neutral for text and key structural lines (#1A1A1A or #2D3436), one accent color for the single most critical element in the figure (applied sparingly to draw the eye), and 1–2 extremely subtle supporting greys (#E8E8E8 for light fills, #CCCCCC for secondary lines) for everything else
- Replace text labels with simple, universally recognizable pictographic icons wherever humanly possible — each icon must be reducible to its geometric essence (a circle for a cell, a wavy line for a signal, a lock for a receptor, a key for a ligand). No more than 15 total icons in the entire figure
- Typography: One bold headline (18–24 pt equivalent, sans-serif, tight letter-spacing) that summarizes the core message in ≤8 words; all other labels in thin/light weight sans-serif (8–10 pt equivalent, generous letter-spacing of +20–40) positioned precisely
- Lines: Extraordinarily thin (0.5 pt, rarely 1 pt), elegant, and used with extreme parsimony — every single line in the figure must justify its existence. If removing a line doesn't reduce understanding, remove it
- Layout: Strict adherence to an underlying grid with generous margins (≥10% of canvas width on all four sides). Multi-element groups should be visibly aligned to grid intersections. Asymmetric balance is acceptable and often desirable
- Use subtle transparency fills (10–30% opacity) to define background structural zones rather than heavy outlines or borders — this creates spatial organization without adding visual weight
- Absolutely do NOT include: complex textures, multiple font families in the same figure, borders/frames around individual elements (use spatial grouping instead), heavy or large arrowheads (arrows should be simple lines with minimal terminations), saturated colors, decorative elements
- The overall impression should be: "I understood this in 3 seconds, I want to share it, and it looks like it belongs in the Communications section of a Nature journal."
```

---

## Style 4: Scientific Illustration — Textbook Realism Style

```
STYLE: Scientific Illustration — Professional Textbook and Review Article Quality

VISUAL INSTRUCTIONS:
- Render as a professional-grade scientific illustration suitable for a Nature Reviews, Cell, or major textbook figure
- Biological and chemical structures must appear semi-realistic with accurate morphology: organelles should have recognizable internal structures (mitochondria with visible cristae and double membrane, Golgi with stacked cisternae and vesicles budding off, ER with ribosomes dotting the rough ER surface), proteins should have discernible domain architecture (distinct globular domains connected by linker regions), tissues must show proper histological layering and cell-type organization
- Apply soft, naturalistic shading throughout using gradient fills or subtle airbrush-style rendering. Establish a consistent light source from the upper-left at ~45° angle, creating gentle shadows at the lower-right of three-dimensional forms. Shadow intensity should be subtle (15–25% darker than base color) — enough to create depth without being dramatic
- Color palette: Use a rich but disciplined palette of 8–12 colors with tonal variations (light, medium, and dark shades of each key structural color) to create depth and distinguish related but distinct elements. Colors should feel natural and biologically/chemically plausible — avoid artificial-looking saturated primaries
- Surface textures are important: plasma membranes with subtle lipid bilayer striation texture, nuclear envelopes dotted with nuclear pore complexes, extracellular matrix with fine fibrous texture, protein surfaces with subtle bump mapping suggesting atomic-level surface roughness, mineral/crystalline surfaces with subtle facet reflections
- Lighting setup: Soft key light from upper-left (60% intensity, warm white ~5500K), subtle fill light from lower-right (20% intensity, neutral), ambient occlusion creating slightly deeper tones in crevices and contact points between elements. Absolutely no harsh shadows, no dramatic spotlighting, no theatrical rim lighting — this should feel like a well-lit laboratory or classroom, not a movie set
- Depth treatment: Foreground elements (the mechanism being explained) in sharp focus with full detail. Background anatomical or cellular context elements may be slightly softened (not blurred, but rendered with slightly less contrast and detail) to create depth hierarchy
- Border treatment: Elements may extend to the canvas edges without hard frames — a soft vignette at the very edges (5–10% darkening) is acceptable for cover/hero images but not for inline figures
- Absolutely do NOT include: cartoon-like outlines (avoid uniform black strokes around biological objects — use subtle tonal edges instead), neon or highly saturated colors, unrealistic proportions or spatial relationships, comic-style shading or cell-shading
- The overall impression should be: "This could be Figure 1 in a Nature Reviews Molecular Cell Biology article — authoritative, beautiful, and scientifically credible."
```

---

## Style 5: Futuristic Tech — Cutting-Edge Innovation Style

```
STYLE: Futuristic Tech — Cutting-Edge Digital Innovation Aesthetic

VISUAL INSTRUCTIONS:
- Render as a futuristic technology visualization with a dark, digital, innovation-forward aesthetic
- Background: deep near-black (#0A0A1A to #0D1117) with a subtle blue or purple undertone (NOT pure black). May include an extremely faint tech-grid pattern at 5–10% opacity — square or hexagonal grid in slightly lighter blue (#1A1A3A) — to suggest a digital/technological substrate. The grid should be barely visible, providing texture without distraction
- Primary visual elements: Rendered as glowing neon lines and luminous geometric forms. Core color palette: cyan (#00E5FF), electric blue (#4488FF), magenta (#FF44AA), and deep purple (#8844FF). All illuminated elements should have a bloom/glow effect extending 2–4 pixels around each element — this glow is essential to the aesthetic
- Connection lines: Thin (1 pt) glowing paths between elements — may use dashed or pulsing visual rhythms to suggest data transmission. Data flow can be shown as small bright particles (~2–3 px) traveling along connection lines, like packets moving through a network
- Nodes and modules: Dark glass-like or frosted-glass rectangles (#1A1A2E at 60–80% opacity) with bright colored edge highlights (1–2 px glow on the border) and subtle internal illumination. Transparent or holographic overlay panels where multiple layers of information overlap — these should have a slight blue/cyan tint (#88CCFF at 10–15% opacity)
- Data and computation representation: Abstract flowing particle streams (small luminous dots moving in parallel), subtle digital matrix-like effects (very faint, only as background texture), glowing data points connected in network topologies, volumetric light beams through semi-transparent overlays
- Typography: Monospace or tech-style sans-serif in bright white (#FFFFFF) or cyan (#00E5FF). Labels may have a subtle outer glow effect (1–2 px in a complementary color) for readability against the dark background. Use a single monospace or tech font family consistently
- Lighting effects (use sparingly and tastefully): Small lens flares at 1–2 key focal points (subtle, not JJ Abrams style), volumetric light rays passing through semi-transparent elements, very subtle fog or particulate mist near the base plane of the composition
- Absolutely do NOT include: cartoon elements, paper or natural textures, hand-drawn lines, traditional journal formatting conventions, white backgrounds, serif fonts, earthy or natural color palettes
- IMPORTANT CAVEAT: This style is primarily for presentations, posters, preprints, and tech blogs. It may be perceived as "not serious enough" for traditional journal manuscript submission. Use with awareness of the venue
- The overall impression should be: "This is the future of technology — it belongs on the main stage at NeurIPS, CES, or a major tech company keynote."
```

---

## Style 6: Hybrid — Multi-Layered Visual Hierarchy Style

```
STYLE: Hybrid — Multi-Layered Visual Hierarchy (Current Top-Tier Trend, 2025–2026)

VISUAL INSTRUCTIONS:
- This composition uses THREE distinct visual layers to create optimal information hierarchy. Each layer has a specific role, visual weight, and rendering treatment. The layers must be visually distinguishable at first glance — the reader should subconsciously register the hierarchy before consciously processing any content

LAYER 1 — STRUCTURAL FRAMEWORK (60% of total visual weight):
- The overall architecture and layout of the mechanism: modular boxes defining the main components or steps, primary flow arrows showing the main direction of the mechanism, and compartment or phase boundaries organizing the space
- Rendered in clean, restrained vector style: muted professional colors (slate blue, warm grey, pale blue-grey), clean 1.5–2 pt outlines, regular geometric shapes, precise alignment
- This layer answers the reader's question: "What is the overall structure of this mechanism?"
- This layer should be the most spatially extensive — it provides the skeleton that Layers 2 and 3 attach to

LAYER 2 — EMPHASIZED KEY ELEMENTS (25% of total visual weight):
- The 2–3 most important components, interactions, or discoveries in the mechanism — the elements the authors most want to communicate
- Rendered with hand-drawn sketch treatment: slightly organic outlines, thicker and more varied lines (2–3 pt), more saturated accent colors (warm orange, deep crimson, rich cobalt, emerald), slightly larger scale than Layer 1 equivalents
- These elements must visually "pop" from the Layer 1 framework — the reader's eye must be drawn here first, within 1 second of viewing
- This layer answers the reader's question: "What should I pay attention to? What is new or important here?"
- Strategic placement at key nodes in the Layer 1 framework — typically at decision points, transformation steps, or the central novel interaction

LAYER 3 — CONTEXTUAL DETAILS (15% of total visual weight):
- Supporting biological objects (cells, organelles, tissues), molecular structures, experimental data thumbnails, or environmental context that grounds the mechanism in scientific reality
- Rendered with scientific illustration or minimal infographic treatment: softer rendering, thinner lines (0.5–1 pt), lighter or more muted colors, smaller scale, less contrast
- These elements are visually and hierarchically subordinate to Layers 1 and 2 — they provide context without competing for attention
- This layer answers the reader's question: "What is the biological, chemical, or physical context?"
- Cluster these elements around Layer 2 elements to provide supporting context, not scattered randomly

COMPOSITION RULES ACROSS LAYERS:
- The three layers must be visually distinct — if you squint at the figure, the Layer 2 elements should be the only things you clearly see
- No more than 5 total Layer 2 emphasized elements — if everything is emphasized, nothing is
- Layer 3 elements should form natural clusters around Layer 2 nodes, not float independently
- Background: very light warm grey (#F8F7F4) or a subtle radial gradient from white at the center to very light grey (#EEECEA) at the edges — this is more sophisticated than pure white and helps the layers separate visually
- Typography: sans-serif across all layers, but with deliberate hierarchy: Layer 2 labels may be 1–2 pt larger and bolder than Layer 1 labels; Layer 3 labels are 1 pt smaller and lighter weight
- The overall impression should be: "I can read this figure at three levels — the 3-second skim tells me the main point, the 30-second study gives me the mechanism, and the 3-minute deep dive gives me the full scientific context."
```

---

## Style 7: 3D Render — Photorealistic Depth Style

```
STYLE: 3D Photorealistic Render — Cinematic Scientific Visualization

VISUAL INSTRUCTIONS:
- Render as a photorealistic 3D scientific visualization at the quality level of professional Blender, Cinema 4D, or Maya work by an experienced scientific 3D artist

LIGHTING SETUP (Critical — this defines the quality):
- Professional three-point studio lighting:
  - Key light: 60% intensity, positioned upper-left at ~45° elevation and ~30° azimuth, warm white color temperature ~5500K, moderately soft shadows
  - Fill light: 30% intensity, positioned lower-right, very soft, neutral white ~5000K — reduces shadow darkness without eliminating shadows entirely
  - Rim/Back light: 40% intensity, positioned upper-back-right, cool white ~6500K — creates a subtle bright edge that separates the subject from the background and defines its 3D volume
- Additional: Subtle ambient occlusion (AO) to darken crevices and contact points where surfaces meet — this greatly enhances depth perception
- Global illumination or indirect lighting: subtle light bounce from nearby surfaces, creating natural fill in shadowed areas

MATERIAL PROPERTIES (Physically accurate):
- Glass/transparent materials: ~1.5 index of refraction (IOR), subtle reflections on surface (Fresnel effect — more reflective at glancing angles), slight tint if colored glass
- Metallic surfaces: appropriate roughness values (0.1–0.3 for polished, 0.4–0.6 for brushed/matte metal), subtle anisotropic highlights for machined or brushed surfaces, environment-appropriate reflectivity
- Biological tissues: subsurface scattering (SSS) for skin, organ surfaces, and translucent biological materials — light penetrates slightly and scatters internally before exiting, creating a soft, living appearance rather than hard plastic look
- Liquids/gels: correct refractive properties, subtle caustics where light focuses through curved liquid surfaces, appropriate viscosity suggested by surface tension curvature
- Plastics/polymers: moderate roughness (0.2–0.4), subtle specular highlights, no metallic reflections

CAMERA & COMPOSITION:
- Perspective view (NOT orthographic — this is a photorealistic render, not a technical schematic) with moderate focal length (50–85 mm equivalent — similar to human vision or a portrait lens)
- Subtle depth of field: the mechanism plane in sharp focus; elements significantly in front of or behind this plane softly defocused. This guides attention and enhances the 3D feel
- Camera positioned at a slight elevation (~15–30°) to show both top and side surfaces of 3D objects, providing clear spatial information

SURFACE QUALITY & DETAIL:
- High-resolution procedural textures where appropriate (not photographic image textures that might conflict stylistically)
- Subtle surface imperfections for photorealism: microscopic roughness variation, gentle micro-scratches on metallic surfaces (barely visible), organic surface variation on biological structures (pores, slight bumps, natural asymmetry)
- These imperfections should be SUBTLE — they add realism without being consciously noticeable

COLOR PALETTE:
- Rich, saturated colors rendered with physically-based shading — colors should look like real materials under real lighting, not flat digital fills
- The interplay of light and material creates natural color variation (brighter on illuminated faces, darker in shadow, color bleeding from nearby colored objects)
- Overall color scheme should remain scientific and professional — this is a journal figure, not a video game

ENVIRONMENT & BACKGROUND:
- Subtle gradient background: studio light grey transitioning to slightly darker edges, OR a contextual scientific environment (laboratory bench surface, biological fluid milieu, clean room setting) if relevant to the mechanism — but never distracting
- Background elements should be significantly darker, lighter, or defocused compared to the subject

COMPOSITION:
- Elements arranged in a 3D scene with realistic spatial relationships, depth, and scale hierarchy
- Objects closer to camera are larger; objects further away are smaller — use this for natural visual hierarchy
- The main mechanism elements should occupy the foreground-to-midground

Absolutely do NOT include: flat/unlit materials (cartoon shaders), 2D vector overlays that break the 3D illusion, excessive post-processing filters (heavy vignetting, extreme color grading), visible polygon edges or low-resolution geometry, unrealistic material assignments, dramatic or theatrical lighting that obscures scientific content

The overall impression should be: "This could be the cover image of Advanced Materials, Nature, or a Cell journal — visually stunning but scientifically rigorous, where the 3D rendering enhances understanding rather than distracting from it."
```
