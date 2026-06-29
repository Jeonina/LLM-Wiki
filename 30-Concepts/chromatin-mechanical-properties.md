---
type: concept
title: Chromatin mechanical properties
aliases: [chromatin viscoelasticity, chromatin mechanics, chromatin rigidity, chromatin elasticity, chromatin fluidity]
tags: [biophysics, viscoelastic, mechanics, locus-state, polymer]
created: 2026-05-15
updated: 2026-05-15
---

# Chromatin mechanical properties

> The **mechanical / viscoelastic / biophysical state** of chromatin — rigidity, elasticity, fluid-like vs gel-like behavior, condensation, and the mesh through which nuclear proteins diffuse. This is the **mechanical sub-axis of DNA locus state**: a locus's mechanical context (stiff heterochromatin floor vs soft euchromatin droplet vs nuclear-body-confined condensate) is a regulatory variable distinct from sequence and chromatin marks.

## Why it's a real axis

- The same DNA sequence with the same histone marks can behave differently if the surrounding chromatin is more or less viscoelastic — transcription factor residence times, condensate stability, and loop formation kinetics all depend on local mechanics.
- Lamin depletion increases chromatin **conformational heterogeneity** at nearly all genomic separations ([[10-Summaries/mali-2025-conformational-heterogeneity]]) — predicted to elevate transcriptional noise because the mechanical anchor is gone.
- Active transcription **locally stabilizes nucleosomes** while preserving free-protein mobility ([[10-Summaries/daugird-2024-viscoelastic-chromatin]]) — transcription is a mechanical event, not just chemical.

## Measurement methods

| Method | What it measures | Single-cell? |
|---|---|---|
| **Lattice light-sheet single-molecule imaging** | Nucleosome diffusion, viscoelastic moduli of interchromatin space | Live single cells |
| **Optical / magnetic tweezers** | Chromatin fiber elastic modulus, force-extension | Bulk fibers |
| **Polymer modeling from Hi-C** | Predicted viscoelastic regimes from contact data | Per-cell with scHi-C |
| **Microrheology (tracer particles)** | Mesh size, viscosity gradients | Single cells, indirect |
| **FRAP / single-molecule tracking** | Protein residence times in chromatin domains | Live cells |

## Concepts under this umbrella

- **Viscoelasticity** — combined viscous (energy-dissipating) + elastic (energy-storing) behavior; chromatin is viscoelastic across multiple timescales.
- **Rigidity** — heterochromatin tends stiffer than euchromatin; lamin-tethered chromatin is the rigid backbone.
- **Condensation** — local density modulated by H1, nucleosome spacing, acetylation status.
- **Fluid-like behavior / phase separation** — see [[30-Concepts/chromatin-phase-separation]].
- **Entropic confinement** — chromatin mesh constrains condensate coalescence ([[10-Summaries/qi-zhang-2021-nucleoli-coalescence]]).

## Locus-state framing

Three sub-axes of structural-physical state:

1. **3D contact state** — Hi-C-based interaction maps.
2. **Spatial positioning state** — lamina / NAD / speckle contact via DamID & friends.
3. **Mechanical / viscoelastic state** — what *this concept* covers.

Single-cell coverage is strongest for axis 1, growing for axis 2, sparse for axis 3.

## Related

- [[30-Concepts/chromatin-phase-separation]] · [[30-Concepts/nuclear-lamina]] · [[30-Concepts/conformational-heterogeneity]] · [[30-Concepts/topologically-associating-domain]] · [[40-Topics/3d-genome]]
- Sources: [[10-Summaries/daugird-2024-viscoelastic-chromatin]] · [[10-Summaries/qi-zhang-2021-nucleoli-coalescence]] · [[10-Summaries/gibson-2019-chromatin-llps]] · [[10-Summaries/mali-2025-conformational-heterogeneity]]
