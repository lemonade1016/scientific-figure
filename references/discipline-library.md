# Discipline Prompt Library

Each discipline has a pre-built prompt block that captures the specific visual conventions, common element types, color standards, and compositional norms of that field. Select the block matching the user's Phase 1 choice and include it verbatim as Layer 2 of the final prompt.

---

## Category 1: Biomedical & Molecular Life Sciences

```
CONTEXT: This is a biomedical mechanism diagram for a top-tier life science journal.

DOMAIN CONVENTIONS:
- Use standard biological visual grammar: plasma membrane as a phospholipid bilayer (hydrophilic heads + hydrophobic tails), receptors as Y-shaped transmembrane proteins, ligands as small circles or triangles, nucleus as a large double-membrane oval with nuclear pores, mitochondria as bean-shaped organelles with internal cristae, endoplasmic reticulum as a folded membrane network near the nucleus, Golgi apparatus as a stack of flattened cisternae
- Cellular compartments must be clearly delineated: extracellular space (top/outside), plasma membrane (thin boundary layer), cytoplasm (interior space), nucleus (central large organelle with envelope), mitochondria (scattered, bean-shaped), ER (perinuclear folded membranes)
- Signaling is directional and semantically consistent: solid arrows (→) for activation/promotion, T-bar terminations (⊣) for inhibition/blocking, dashed arrows for indirect or unknown mechanisms, circular arrows for feedback loops
- Post-translational modifications: phosphorylation shown as a small "P" circle transferring to a protein, causing a conformational change (shape shift of the protein); ubiquitination shown as "Ub" tags attaching to a protein
- Protein complexes: individual subunits assembling into a larger structure, indicated by a bracket or surrounding translucent box
- Color code biologically: warm colors (red, orange, coral) for active/phosphorylated/oncogenic/pro-inflammatory states; cool colors (blue, teal, purple) for inactive/tumor-suppressive/anti-inflammatory states; green for structural/cytoskeletal components; grey for basal/inactive/resting state
- Spatial scale cue: include relative size hierarchy (small molecule < protein < protein complex < organelle < cell)
- Label key proteins (gene names in italics where standard), phosphorylation sites, and cellular compartments minimally — use a legend for complex abbreviations
- Ensure directional flow reads left→right or top→bottom consistently throughout
- Standard pathway elements to use where relevant: NF-κB/IκB cascade, MAPK/ERK signaling, JAK/STAT pathway, GPCR/RTK receptor activation, caspase cascades, ubiquitin-proteasome system, endocytosis/exocytosis, transcription factor binding to DNA promoter regions
```

---

## Category 2: Chemistry, Materials & Nanoscience

```
CONTEXT: This is a chemistry or materials science mechanism diagram for a top-tier chemistry/materials journal.

DOMAIN CONVENTIONS:
- Chemical structures: Use standard bond-line notation for organic molecules, ball-and-stick or space-filling representations for 3D molecular structures, CPK coloring convention for atoms (carbon=grey/black, hydrogen=white, oxygen=red, nitrogen=blue, sulfur=yellow, phosphorus=orange, halogens=green, metals=grey/silver)
- Reaction schemes: Show reactants → intermediates → products with clear reaction arrows, annotate key conditions above/below arrows (Δ for heat, hν for light, catalyst names, solvent, temperature, pressure)
- Energy/coordinate diagrams: Reaction coordinate on x-axis, energy/free energy on y-axis, transition states as energy peaks (‡ symbol), intermediates as local energy minima, activation energies (ΔG‡) and reaction free energies (ΔG°) clearly labeled
- Material architectures: Show layered thin-film structures (substrate→interlayer→active layer→capping layer in cross-section), core-shell nanoparticles (concentric circles with labeled radii and compositions), porous frameworks (MOF/COF/zeolite with regular pore channels shown as structured void spaces), 2D material sheets (graphene, TMD, MXene as atomically thin layers)
- Synthesis workflows: Sequential step-by-step representation (Step 1 → Step 2 → Step 3), each step showing precursor materials→process→intermediate or product, with key parameters annotated (temperature, pressure, time, solvent, atmosphere)
- Color conventions: Distinct colors for different material phases or components, warm→cool gradient for energy scales (warm=high energy/unstable, cool=low energy/stable), consistent color coding across multi-panel figures
- Standard visualization types: Pourbaix diagrams (E vs pH), Tafel plots, Nyquist/Bode plots for impedance, XRD patterns as stick diagrams, TEM/SEM image annotations, band structure diagrams (E vs k), density of states plots, cyclic voltammograms
```

---

## Category 3: Artificial Intelligence & Computer Science

```
CONTEXT: This is an AI/ML architecture or mechanism diagram for a top-tier machine learning conference or journal (NeurIPS, ICML, ICLR, JMLR, CVPR).

DOMAIN CONVENTIONS:
- Neural network layers: Represent as labeled rectangular blocks with rounded corners (radius ~4pt). Use consistent color coding: encoder blocks in blue tones, decoder blocks in green tones, attention mechanisms in orange/yellow, feed-forward networks (FFN/MLP) in purple, normalization layers in grey, embedding layers with subtle gradient fill
- Data tensors: Show as 3D isometric boxes or annotated parallelograms with shape annotations [batch_size, sequence_length, hidden_dim]. Data flow arrows should be thick (2–3pt) and directional between tensors and operations
- Attention mechanisms: Show Query (Q), Key (K), Value (V) as parallel input arrows entering the attention operation. Depict the scaled dot-product step (QK^T/√d_k), softmax normalization, and weighted value aggregation. Multi-head attention shown as h parallel copies feeding into a concatenation operation then linear projection
- Architecture hierarchy: Show main model overview at high level → detailed sub-module insets zooming into key components (e.g., zoom-in circle on the attention block) → component-level details for critical innovations
- Flow conventions: Data flow = solid thick arrows (left→right or bottom→top), gradient flow = dashed thin red arrows (right→left or top→bottom during backpropagation), skip/residual connections = curved thin arrows bypassing blocks, gating signals = thin lines entering gating mechanisms with ⊗ or ⊙ symbols
- Standard elements: Transformer block (Multi-Head Attention + Add&Norm + FFN + Add&Norm), Mixture of Experts (Router + Expert FFNs + weighted combination), LoRA adapters (small rectangles A and B injecting into frozen weight matrix W), positional encoding (sine/cosine wave icon or learned position indices), token embedding (discrete token→continuous vector), KV-cache (memory bank icon storing past keys and values), RAG (Retriever→Document store→Generator pipeline), diffusion model (noise addition forward process + denoising reverse process)
- Color conventions: Blue=encoding/representation, Green=decoding/generation, Orange=attention/interaction, Purple=FFN/transformation, Grey=normalization/utility, Red=loss/gradient/error, Yellow=embedding/input, Cyan=output/prediction
- Typography: Monospace font for code/variable/tensor names; sans-serif for module labels
```

---

## Category 4: Engineering & Applied Physics

```
CONTEXT: This is an engineering or applied physics mechanism diagram for a top-tier engineering or applied physics journal.

DOMAIN CONVENTIONS:
- Device schematics: Cross-sectional views (substrate at bottom, active layers stacked above, contacts/electrodes on sides or top surface), isometric or perspective views for 3D device architectures, plan-view (top-down) for lithographic patterns and circuit layouts
- System diagrams: Block diagram notation — functional blocks (rectangles) connected by signal/power/fluid flow lines (arrows), input→process→output flow direction, feedback loops shown as curved return paths from output back to controller/comparator
- Energy systems: Energy flow diagrams (input source→conversion step→transmission→storage→end use, with loss streams branching off), electronic band diagrams (energy E vs position x, showing conduction band minimum, valence band maximum, Fermi level, band bending at interfaces, built-in potentials), efficiency cascade or Sankey diagrams
- Mechanical systems: Engineering drawing conventions (visible edges = solid lines, hidden edges = dashed lines, centerlines/axes = dash-dot lines, dimension lines with arrowheads and measurements), force vectors as labeled arrows with magnitude, stress-strain curves with key points (yield, ultimate, fracture), free body diagrams with all forces and moments
- Electrical/Electronic: IEEE/ANSI standard symbols for components (resistors, capacitors, inductors, transistors, diodes, op-amps), signal flow left→right, power rails at top (+Vcc) and bottom (GND), ground symbols at reference nodes
- Optical/Photonic: Ray tracing with refractive/reflective paths (solid lines with arrows), wavefront visualization (dashed lines perpendicular to rays), optical element symbols (lenses, mirrors, beam splitters, waveguides), wavelength indicated by color
- Color conventions: Metallic=grey/silver, semiconductor=blue/grey, insulator=brown/tan, thermal=red/orange gradient (hot→cold), electrical=red (+), black (−), optical=rainbow for broadband or specific monochromatic colors for discrete wavelengths
- Standard labeling: Physical quantities in italics (T, P, V, I, E, B, σ, ε), units in roman type, key dimensions annotated with measurement lines and values
```

---

## Category 5: Clinical Medicine & Healthcare

```
CONTEXT: This is a clinical medicine mechanism or healthcare diagram for a top-tier medical journal (NEJM, Lancet, JAMA, BMJ).

DOMAIN CONVENTIONS:
- Anatomical context: Show relevant organ or tissue in muted, semi-transparent background tones — the mechanism overlay must be the visual foreground. Use standard anatomical views as appropriate: coronal (frontal), sagittal (lateral), axial (transverse/cross-section), or anterior/posterior surface views
- Disease mechanisms: Show healthy→diseased progression with clear visual contrast — healthy state in calm blue/green tones with intact structures; diseased state in red/orange tones with disrupted structures, inflammatory infiltrates, fibrotic remodeling, or neoplastic transformation
- Drug Mechanism of Action (MoA): Show drug entering the system (oral→gastrointestinal absorption→bloodstream, or intravenous→direct circulation), reaching target tissue, binding to molecular target (lock-and-key or induced-fit binding representation), downstream signaling cascade, and final therapeutic outcome. Include key PK/PD parameters where relevant
- Clinical pathways: Decision-tree format — diamond nodes for decision points, rectangles for actions/interventions, ovals for outcomes/endpoints. Patient flow moves left→right with branches at decision nodes. Include probability/percentage annotations on branches where evidence-based
- Diagnostic algorithms: Sequential Test→Result→Interpretation→Next Action chain, with sensitivity/specificity or positive/negative predictive value annotations at key branch points
- Color conventions: Arterial=red, venous=blue, lymphatic=green, neural=yellow, healthy tissue=pink/peach, lesion/tumor=dark red/grey, inflammation=orange/red gradient, fibrosis=collagen-grey, necrosis=dark brown/black, edema=pale blue
- Key elements: Organ cross-sections with tissue layers clearly labeled, blood vessel trees with arterial→capillary→venous hierarchy, lymph node architecture (cortex, paracortex, medulla, germinal centers), tumor microenvironment (tumor cells + immune infiltrate + stromal cells + blood vessels), epithelial tissue layers (epithelium, basement membrane, lamina propria, submucosa, muscularis, serosa)
- Typography: Drug names in International Nonproprietary Name (INN) format, gene/protein names following HGNC guidelines, biomarkers in italics where standard, clinical endpoints clearly boxed and highlighted
- Ethical note: Maintain balanced visual representation of therapeutic benefits and adverse effects; avoid exaggerated claims through disproportionate visual emphasis
```

---

## Category 6: Environmental, Earth & Climate Sciences

```
CONTEXT: This is an environmental, earth, or climate science mechanism diagram for a top-tier geoscience or environmental science journal.

DOMAIN CONVENTIONS:
- Cycle diagrams: Circular or semi-circular layout showing reservoirs (rectangular or oval boxes) connected by fluxes (arrows with width proportional to transfer rate). Reservoir box size should be proportional to pool magnitude where data supports this. Use clockwise flow direction for standard cycles
- Ecosystem representations: Trophic levels stacked vertically (primary producers at base → primary consumers → secondary consumers → apex predators → decomposers cycling back). Species interaction networks shown as nodes connected by edges labeled with interaction type (+, −, or ±)
- Climate system: Earth system components shown as interacting boxes (atmosphere, ocean, land surface, cryosphere, biosphere) connected by coupling fluxes. Radiative forcing: incoming shortwave solar radiation (yellow arrows from top), outgoing longwave terrestrial radiation (red arrows upward), greenhouse gas trapping shown as partial reflection of outgoing radiation
- Geological sections: Vertical stratigraphic columns (youngest strata at top, oldest at base), cross-sectional profiles through crust and upper mantle (depth on y-axis, horizontal distance on x-axis), structural features using standard geological symbols (faults with relative motion arrows, fold axes, unconformities as wavy lines), plate tectonic diagrams (subduction zones with slab dip, mid-ocean ridges with spreading arrows, transform faults)
- Biogeochemistry: Element reservoirs (atmosphere, biomass, soil, ocean, sediment) connected by transformation arrows labeled with process names. Oxidation states indicated by color gradient where relevant. Microbial mediation of transformations shown with microbe icons at key transformation steps
- Color conventions: Atmosphere=pale blue/white gradient, Ocean=deep blue gradient (light at surface, dark at depth), Land/Vegetation=green, Bare soil/rock=brown/tan, Ice/Snow=white/pale cyan, Anthropogenic impacts=red/orange/warm tones, Biosphere=green
- Standard elements: Global carbon cycle (Atmosphere CO₂ ↔ Land C₃/C₄ plants and soil C ↔ Ocean dissolved inorganic and organic C, with GPP, respiration, air-sea exchange, sedimentation fluxes), nitrogen cycle (N₂ fixation→NH₄⁺→NO₂⁻→NO₃⁻→denitrification→N₂), hydrological cycle (evaporation, transpiration, precipitation, surface runoff, infiltration, groundwater flow), climate feedback loops (positive=self-reinforcing shown with + signs, negative=damping shown with − signs)
- Scale annotations: Temporal scale arrows (hours→days→seasons→years→decades→centuries→millennia→geological time), spatial scale bars (μm→mm→m→km→global/planetary scale)
```

---

## Category 7: Physics & Mathematics

```
CONTEXT: This is a physics or mathematics mechanism/concept diagram for a top-tier physics or mathematics journal (Physical Review, JHEP, Annals of Mathematics).

DOMAIN CONVENTIONS:
- Feynman diagrams: Fermions (electrons, quarks, neutrinos) as straight solid lines with arrows indicating particle/antiparticle direction, photons as wavy/curly lines, gluons as curly loops, W±/Z bosons as dashed lines, Higgs boson as dotted lines. Time axis clearly indicated (convention: vertical up or horizontal right). Vertices where lines meet represent interaction points
- Phase diagrams: State variable axes (P vs T, composition, external magnetic field H, etc.). First-order phase transitions = solid boundary lines, second-order/critical transitions = dashed lines, crossover regions = dotted lines or gradient. Critical point marked with filled circle; triple point with filled triangle. Label each phase region clearly
- Spacetime diagrams (Penrose/Carter/Penrose-Carter): Conformal infinity boundaries marked as I+ (future null infinity), I− (past null infinity), i⁰ (spatial infinity), i⁺ (future timelike infinity), i⁻ (past timelike infinity). Light cones = 45° lines. Worldlines: timelike (within light cone, <45°), lightlike/null (on light cone, =45°), spacelike (outside light cone, >45°). Event horizons = 45° boundaries. Black hole singularity = zigzag or jagged line at top
- Quantum mechanics: Potential wells (harmonic oscillator, infinite/finite square well, double well) with bound state wavefunctions overlaid (n=1 ground state at bottom, n=2, 3... excited states above, node count = n−1). Quantum tunneling = wavefunction amplitude decaying exponentially through classically forbidden barrier region. Bloch sphere for qubit representation (computational basis |0⟩ at north pole, |1⟩ at south pole, superposition states on surface, mixed states interior). Energy level diagrams (increasing energy upward, allowed transitions as vertical arrows with wavelength color coding)
- Condensed matter: Brillouin zones (truncated polyhedra in reciprocal space), Fermi surfaces (closed curves in 2D, closed surfaces in 3D within Brillouin zone), band structure (E vs k along high-symmetry path Γ→X→M→Γ→R→X in Brillouin zone), density of states (g(E) vs E with van Hove singularities)
- Mathematical structures: Commutative diagrams (categories/objects as labeled nodes, morphisms/functors as labeled arrows, diagram commutes when all paths between two objects are equal). Manifold embeddings (coordinate charts, transition maps). Group actions (orbits as point sets, fundamental domains as shaded regions)
- Color conventions: Monochromatic base (black/dark grey lines) with purposeful color accents for key features. Spectral coloring (red→orange→yellow→green→blue→violet) for continuous field values or energy scales. Distinct, clearly differentiated colors for different particle species or quantum states. Maintain ≥30% luminance difference between adjacent colored regions
- Key principles: Symmetries must be visually emphasized (mirror planes, rotation axes, translation vectors). Conserved quantities should be explicitly marked. Broken symmetries shown with asymmetric final state compared to symmetric initial state
```

---

## Category 8: Interdisciplinary & Emerging Fields

```
CONTEXT: This is an interdisciplinary mechanism diagram spanning multiple scientific domains, for a top-tier interdisciplinary journal (Nature, Science, PNAS, Nature Computational Science).

DOMAIN CONVENTIONS:
- Multi-scale integration: Show the mechanism operating across multiple spatial or temporal scales (molecular→cellular→tissue→organ→organism→population, or quantum→atomistic→mesoscale→continuum→system). Use clear scale transition markers (zoom-in circles with magnification indicators, scale-axis annotations, or nested frames with size labels)
- Cross-domain mapping: When combining distinct domains (e.g., AI model + biological system), use clearly separated visual "zones" with soft but distinct boundaries. One zone for computational/algorithmic components (may use cleaner, more geometric rendering), another zone for biological/physical components (may use more organic, scientific illustration rendering), and an explicit interface/bridge zone showing the interaction between domains (data flow, model→experiment coupling, prediction→validation cycle)
- Data-to-mechanism integration: Experimental data representations (heatmaps, scatter plots, spectra, microscopy thumbnails) integrated seamlessly with mechanistic schematic elements. Use connecting lines or shared color coding to link observed data patterns to their mechanistic interpretations. Distinguish between data-driven conclusions (solid connections) and hypothesized mechanisms (dashed connections)
- Digital twin / Virtual-physical coupling: Physical system represented on one side (photographic or realistic rendering), digital/virtual representation on the other (schematic or wireframe), with bidirectional information flow arrows: physical→digital (sensing, measurement, data acquisition) and digital→physical (prediction, control, actuation)
- Workflow integration: Computational pipeline (data→preprocessing→feature extraction→model training→inference→analysis→interpretation) shown in parallel with experimental pipeline (sample preparation→assay→data acquisition→processing→analysis→conclusion), with explicit crossover points and feedback from computational results informing next experimental iteration
- Color conventions: Assign distinct color families to each parent discipline represented (e.g., blue for computational components, green for biological components, orange for chemical components). Within each domain, use internally consistent color sub-palettes. At domain interfaces, use a neutral bridging color (white, light grey gradient, or a unique interface color) to signal cross-domain information transfer. Maintain the same color assignment for a given domain throughout the entire figure
- Key principles: Cross-domain information transfer must be visually explicit (what information passes from domain A to domain B?). Uncertainty increases at domain boundaries — acknowledge this with softer rendering at interfaces. Maintain consistent visual grammar within each domain even as overall figure style varies across domains. The reader should instantly know which domain any element belongs to by its visual treatment
- Typography: Domain-specific naming conventions preserved within each zone. Gene/protein names in italics (biological), model/algorithm names in bold (computational), chemical formulas with proper subscripts/superscripts, mathematical variables in LaTeX-style italics
```
