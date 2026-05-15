---
type: topic
title: 3D genome
aliases: [chromatin conformation, Hi-C, nuclear architecture]
tags: [Hi-C, TAD, compartments, loops, single-cell, chromatin-structure]
created: 2026-05-12
updated: 2026-05-15
---

# 3D genome

> The 3D organization of chromatin within the nucleus — compartments (A/B), topologically associating domains (TADs), chromatin loops, and **spatial positioning relative to the nuclear lamina** — is a regulatory layer that shapes gene expression, replication timing, and cellular identity. Bulk Hi-C revealed the principles; single-cell methods (scHi-C, sciHi-C, Dip-C, scSPRITE, scNanoHi-C, scDamID) revealed the heterogeneity, with TAD boundaries, compartments, loops, and lamina contacts varying substantially between cells in ways that bulk data cannot resolve.

## Core concepts

- [[30-Concepts/3d-genome]] — the overall framework
- [[30-Concepts/single-cell-hi-c]] — the assay class
- [[30-Concepts/topologically-associating-domain]] — TADs
- [[30-Concepts/chromatin-compartments]] — A/B compartments
- [[30-Concepts/sc-sprite]] — sonication-based multi-way contact capture
- [[30-Concepts/dip-c]] — diploid Hi-C
- [[30-Concepts/stark]] — unified sc3DG-seq analysis pipeline
- [[30-Concepts/sscce]] — single-cell structural quality metric
- [[30-Concepts/empty-cells-algorithm]] — filtering sc3DG-seq barcodes
- [[30-Concepts/nuclear-lamina]] — peripheral organizing surface
- [[30-Concepts/lamina-associated-domains]] — LADs; the cLAD/fLAD distinction
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
- [[10-Summaries/navigating-the-3d-genome-at-single-cell-resolution-techniques-computation-and-mechanistic-landscapes]] — Hong/Dao 2025. Comprehensive review of sc3DG-seq technologies.

### Methods + benchmarking
- [[10-Summaries/harmonizing-single-cell-3d-genome-data-with-stark-and-scnucleome]] — Jiang/Wu 2026. STARK pipeline, EmptyCells, SSCE; benchmark of 15 sc3DG-seq methods; scNucleome public atlas.

### Clinical / cancer SVs (related to 3D regulation)
- [[10-Summaries/nanopore-sequencing-unveils-somatic-structural-variations-as-biomarkers-in-laryngeal-squamous-cell-carcinoma-genomes]] — Liu et al. 2025. Repeat expansions regulating *TP53BP2*/*FBXO28* via spatial proximity.

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
