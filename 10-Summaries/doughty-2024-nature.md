---
type: summary
title: "Doughty 2024 — Single-molecule states link transcription factor binding to gene expression"
aliases: ["Doughty 2024", "SMF TF binding"]
tags: [single-molecule-footprinting, SMF, transcription-factor, enhancer, Greenleaf-lab, Bintu-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Benjamin_2024_Nature.pdf"]
---

Doughty, Hinks, Schaepe and colleagues (Greenleaf / Bintu labs) applied single-molecule footprinting (SMF) — methyltransferase-based chromatin stenciling read by long-read sequencing — to engineered enhancer-promoter constructs in K562 cells. The constructs contain variable numbers of TetO binding sites for either a synthetic TF (rTetR-VP48) or an endogenous TF involved in the type-I interferon response. SMF reads, per fiber, the configuration of TF binding + nucleosome positioning + accessibility on the same molecule, then correlates with steady-state and dynamic gene expression measured by mCherry/citrine reporters.

Three findings. (1) TF binding events on nucleosome-free DNA are independent of each other (statistically uncorrelated), but activation domains recruit chromatin remodelers (BAF) that destabilize nucleosomes, driving observed TF binding cooperativity. (2) Average TF occupancy linearly determines promoter activity, allowing decomposition of TF strength into separable binding and activation terms. (3) Thermodynamic and kinetic models built from SMF data quantitatively predict both enhancer binding microstates and gene expression dynamics.

## Why this matters

Concrete demonstration that single-molecule footprinting answers questions about TF-binding cooperativity, nucleosome eviction, and activation-domain function that bulk and single-cell antibody-based methods cannot. Bridges §3.2 (single-molecule footprinting / scDAF-seq family) and §3.4 (TF occupancy) by showing what the locus-state framework's "transcription factor layer" looks like when measured directly per molecule. Anchors the methodological case that fiber-resolution measurements provide mechanism, not just resolution.

## Related

- [[30-Concepts/single-molecule-footprinting]]
- [[30-Concepts/transcription-factor-occupancy]]
- [[10-Summaries/andrewb-2020-science]]
- [[10-Summaries/elliott-2025-naturebiotechnology]]
