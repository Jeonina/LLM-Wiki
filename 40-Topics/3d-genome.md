---
type: topic
title: 3D genome
aliases: [chromatin conformation, Hi-C, nuclear architecture, 3D chromatin organization]
tags: [Hi-C, TAD, compartments, loops, single-cell, chromatin-structure, chromatin]
created: 2026-05-12
updated: 2026-06-29
---

# 3D genome

> The three-dimensional organization of DNA within the nucleus — chromosome territories, A/B compartments (active vs inactive) ([[10-Summaries/van-steensel-2017-lads-review]]), topologically associating domains (TADs) ([[10-Summaries/nagano-2013-nature]]), chromatin loops (e.g. enhancer–promoter, CTCF-anchored) ([[10-Summaries/ahn-2021-llps-cancer-looping]]), and **spatial positioning relative to the nuclear lamina** ([[10-Summaries/van-steensel-2017-lads-review]]) — is a regulatory layer that shapes gene expression, replication timing, and cellular identity. Bulk Hi-C revealed the principles ([[10-Summaries/nagano-2013-nature]]); single-cell methods (scHi-C, sciHi-C, Dip-C, scSPRITE, scNanoHi-C, scDamID) revealed the heterogeneity ([[10-Summaries/hong-2025-sc3d-genome-review]]), with TAD boundaries, compartments, loops, and lamina contacts varying substantially between cells in ways that bulk data cannot resolve ([[10-Summaries/tan-2018-science]]; [[10-Summaries/mali-2025-conformational-heterogeneity]]).

## Hierarchical organization

The 3D genome is organized hierarchically across scales: chromosomes → compartments (~5–10 Mb) → TADs (~100 kb–1 Mb) → loops (kb-scale) ([[10-Summaries/hong-2025-sc3d-genome-review]]; [[10-Summaries/nagano-2013-nature]]). It is mapped via 3C-family proximity-ligation methods — 3C, 4C, 5C, ChIA-PET, Hi-C, Capture Hi-C, Micro-C ([[10-Summaries/hong-2025-sc3d-genome-review]]). Single-cell variants — scHi-C, sciHi-C, Dip-C, scSPRITE, scNanoHi-C — extend these to per-cell 3D measurement ([[10-Summaries/hong-2025-sc3d-genome-review]]; [[10-Summaries/tan-2018-science]]), revealing substantial cell-to-cell variability in compartments and TAD boundaries that bulk Hi-C smears together ([[10-Summaries/nagano-2013-nature]]; [[10-Summaries/mali-2025-conformational-heterogeneity]]).

## Why it matters

- **Regulatory layer**: enhancer–promoter loops drive gene expression, while TAD boundaries constrain which regulatory interactions occur ([[10-Summaries/hong-2025-sc3d-genome-review]]).
- **Compartment switching** tracks cell-state changes during development and in cancer ([[10-Summaries/hong-2025-sc3d-genome-review]]).
- **LADs ≈ Compartment B** at megabase scale — lamina-associated domains coincide with the inactive B compartment ([[10-Summaries/van-steensel-2017-lads-review]]).
- **LLPS-driven loops** can rewire 3D contacts independently of CTCF ([[10-Summaries/ahn-2021-llps-cancer-looping]]).
- **Lamin depletion** raises conformational heterogeneity genome-wide → predicted increase in transcriptional noise ([[10-Summaries/mali-2025-conformational-heterogeneity]]).

## Core concepts

- [[30-Concepts/single-cell-hi-c]] — the assay class
- [[30-Concepts/topologically-associating-domain]] — TADs
- [[30-Concepts/chromatin-compartments]] — A/B compartments
- [[30-Concepts/sc-sprite]] — sonication-based multi-way contact capture
- [[30-Concepts/dip-c]] — diploid Hi-C
- [[30-Concepts/stark]] — unified sc3DG-seq analysis pipeline
- [[30-Concepts/sscce]] — single-cell structural quality metric
- [[30-Concepts/empty-cells-algorithm]] — filtering sc3DG-seq barcodes
- [[30-Concepts/nuclear-lamina]] — peripheral organizing surface
- [[30-Concepts/lamina-associated-domains]] — LADs; the cLAD/fLAD distinction (compartment B substrate)
- [[30-Concepts/damid]] — protein–DNA contact mapping; the lamina assay class
- [[30-Concepts/scdamt-seq]] — joint genome–protein + transcriptome readout
- [[30-Concepts/conformational-heterogeneity]] — across-cell 3D variability metric
- [[30-Concepts/chromatin-phase-separation]] — LLPS condensates as a 3D-organization mechanism
- [[30-Concepts/chromatin-mechanical-properties]] — viscoelastic / rigidity sub-axis

## Key entities

- [[20-Entities/hua-jun-wu]] — Wu lab; STARK + scNucleome
- [[20-Entities/fuying-dao]] — Dao lab; sc 3D genome review
- [[20-Entities/jop-kind]] — Kind lab; scDamID + scDam&T-seq
- [[20-Entities/alexey-onufriev]] — Onufriev lab; polymer models + C.H. metric

## Sources, by sub-theme

### Review
- [[10-Summaries/hong-2025-sc3d-genome-review]] — Hong/Dao 2025. Comprehensive review of sc3DG-seq technologies.
- [[10-Summaries/van-steensel-2017-lads-review]] — van Steensel & Belmont 2017. Canonical LADs review; three-compartment competition (NL/nucleoli/pericentric).

### Foundational Hi-C
- [[10-Summaries/nagano-2013-nature]] — Nagano et al. 2013. First single-cell Hi-C; cell-to-cell variability in TADs.
- [[10-Summaries/tan-2018-science]] — Tan et al. 2018. Dip-C; haplotype-resolved single-cell 3D structures.

### Clinical / cancer SVs (related to 3D regulation)
- [[10-Summaries/liu-2025-nanopore-lscc-svs]] — Liu et al. 2025. Repeat expansions regulating *TP53BP2*/*FBXO28* via spatial proximity.

### Nuclear lamina / spatial positioning (DamID lineage)

- [[10-Summaries/de-luca-2021-scdamid-protocol]] — de Luca & Kind 2021. Canonical bench protocol for scDamID; Dam-LMNB1 ↔ lamina contacts in single mammalian cells.
- [[10-Summaries/rooijers-2019-scdamt-seq]] — Rooijers/Kind/Dey 2019. **scDam&T-seq**: joint protein–DNA contacts + transcriptome in same cell via T7-IVT linear amplification. Reveals that the lamina↔transcription coupling is concentrated in **fLADs (H3K27me3-rich)**, not in constitutive cLADs.

### Conformational heterogeneity (single-cell 3D metrics)

- [[10-Summaries/mali-2025-conformational-heterogeneity]] — Mali/Onufriev 2025. Defines **C.H. = stdev_cells(⟨R_s⟩)** as a metric for cell-to-cell 3D variability. Bulk-Hi-C-trained vs scHi-C-trained *Drosophila* models diverge at 1–10 Mb; lamin depletion raises C.H. genome-wide → prediction of increased transcriptional noise.

### Phase separation × 3D architecture

- [[10-Summaries/ahn-2021-llps-cancer-looping]] — Ahn/Wang 2021. LLPS-competent IDR fusions induce **CTCF-independent chromatin loops** at oncogenic targets. New 3D-rearrangement class beyond SV/CN-driven loops.
- [[10-Summaries/qi-zhang-2021-nucleoli-coalescence]] — Qi/Zhang 2021. Polymer simulation: viscoelastic chromatin arrests nucleolus coalescence, stabilizing multi-droplet nuclear bodies.

## Synthesized notes

None yet. The single-cell 3D-genome story spans three measurement modalities — proximity ligation (scHi-C family, Hong 2025 + Jiang 2026), protein-tethered methylation (DamID lineage, Kind/Rooijers/de Luca), and polymer modeling (Onufriev). The three should be read together.

## Open questions

- Resolution: most sc3DG methods give ~1 Mb effective resolution per cell; bulk Hi-C achieves ~kb. Will ultra-deep single-cell or imaging-based methods (multiplexed FISH) close the gap?
- Causality: do TAD/loop changes drive gene-expression changes or follow them? Multi-omics methods (sn-m3C, HiRES, scDam&T-seq) begin to address this.
- Single-cell SV-driven 3D rearrangements (Liu 2025) point to a new genome-instability axis.
- Why does the lamina↔transcription coupling restrict to fLADs (H3K27me3) and not cLADs (H3K9me3) ([[10-Summaries/rooijers-2019-scdamt-seq]])? The differential heterochromatin "floor" vs "regulatable" interpretation needs perturbation testing.
- Are bulk-Hi-C and scHi-C trained 3D models genuinely orthogonal in what they capture ([[10-Summaries/mali-2025-conformational-heterogeneity]])? The C.H. divergence at 1–10 Mb suggests yes.

## Related

- [[40-Topics/chromatin-architecture]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/long-read-sequencing]]
- [[50-Notes/regulatory-layers-overview]] — 3D genome as one of the four molecular regulatory layers

## Linked summaries (lint pass 2026-05-21)

- [[10-Summaries/bersaglieri-2019-cells]] — Bersaglieri & Santoro 2019 — Genome organization in and around the nucleolus.
