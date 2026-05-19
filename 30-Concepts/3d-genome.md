---
type: concept
title: 3D genome
aliases: [3D chromatin organization, nuclear architecture]
tags: [chromatin, Hi-C, TAD, compartments, loops]
created: 2026-05-12
updated: 2026-05-19
---

# 3D genome

> The three-dimensional organization of DNA within the nucleus, comprising **chromosome territories**, **A/B compartments** (active vs inactive) ([[10-Summaries/van-steensel-2017-lads-review]]), **topologically associating domains (TADs)** ([[10-Summaries/nagano-2013-nature]]), and **chromatin loops** (e.g., enhancer-promoter, CTCF-anchored) ([[10-Summaries/ahn-2021-llps-cancer-looping]]).

## Definition

Mapped via 3C-family methods (3C, 4C, 5C, ChIA-PET, Hi-C, Capture Hi-C, Micro-C) ([[10-Summaries/hong-2025-sc3d-genome-review]]). The hierarchical organization spans scales: chromosomes → compartments (~5–10 Mb) → TADs (~100 kb–1 Mb) → loops (kb-scale) ([[10-Summaries/hong-2025-sc3d-genome-review]]; [[10-Summaries/nagano-2013-nature]]).

Single-cell variants — scHi-C, sciHi-C, Dip-C, scSPRITE, scNanoHi-C — extend to per-cell 3D measurement ([[10-Summaries/hong-2025-sc3d-genome-review]]; [[10-Summaries/tan-2018-science]]). They reveal substantial cell-to-cell variability in compartments and TAD boundaries that bulk Hi-C smears together ([[10-Summaries/nagano-2013-nature]]; [[10-Summaries/mali-2025-conformational-heterogeneity]]).

## Why it matters

- **Regulatory layer**: enhancer-promoter loops drive gene expression; TAD boundaries constrain which regulatory interactions occur ([[10-Summaries/hong-2025-sc3d-genome-review]]).
- **Compartment switching** tracks cell state changes during development and in cancer ([[10-Summaries/hong-2025-sc3d-genome-review]]).
- **LADs ≈ Compartment B** at megabase scale ([[10-Summaries/van-steensel-2017-lads-review]]).
- **LLPS-driven loops** can rewire 3D contacts independently of CTCF ([[10-Summaries/ahn-2021-llps-cancer-looping]]).
- **Lamin depletion** raises conformational heterogeneity genome-wide → predicted increase in transcriptional noise ([[10-Summaries/mali-2025-conformational-heterogeneity]]).

## Related

- [[30-Concepts/single-cell-hi-c]] · [[30-Concepts/topologically-associating-domain]] · [[30-Concepts/chromatin-compartments]]
- [[30-Concepts/dip-c]] · [[30-Concepts/sc-sprite]] · [[30-Concepts/stark]]
- [[30-Concepts/lamina-associated-domains]] (compartment B substrate)
- [[40-Topics/3d-genome]] · [[40-Topics/chromatin-architecture]]
- [[50-Notes/regulatory-layers-overview]] — 3D genome as one of the four molecular regulatory layers
