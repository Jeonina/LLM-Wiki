---
type: topic
title: 3D genome
aliases: [chromatin conformation, Hi-C, nuclear architecture]
tags: [Hi-C, TAD, compartments, loops, single-cell, chromatin-structure]
created: 2026-05-12
updated: 2026-05-12
---

# 3D genome

> The 3D organization of chromatin within the nucleus — compartments (A/B), topologically associating domains (TADs), and chromatin loops — is a regulatory layer that shapes gene expression, replication timing, and cellular identity. Bulk Hi-C revealed the principles; single-cell methods (scHi-C, sciHi-C, Dip-C, scSPRITE, scNanoHi-C) revealed the heterogeneity, with TAD boundaries, compartments, and loops varying substantially between cells in ways that bulk data cannot resolve.

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

## Key entities

- [[20-Entities/hua-jun-wu]] — Wu lab; STARK + scNucleome
- [[20-Entities/fuying-dao]] — Dao lab; sc 3D genome review

## Sources, by sub-theme

### Review
- [[10-Summaries/navigating-the-3d-genome-at-single-cell-resolution-techniques-computation-and-mechanistic-landscapes]] — Hong/Dao 2025. Comprehensive review of sc3DG-seq technologies.

### Methods + benchmarking
- [[10-Summaries/harmonizing-single-cell-3d-genome-data-with-stark-and-scnucleome]] — Jiang/Wu 2026. STARK pipeline, EmptyCells, SSCE; benchmark of 15 sc3DG-seq methods; scNucleome public atlas.

### Clinical / cancer SVs (related to 3D regulation)
- [[10-Summaries/nanopore-sequencing-unveils-somatic-structural-variations-as-biomarkers-in-laryngeal-squamous-cell-carcinoma-genomes]] — Liu et al. 2025. Repeat expansions regulating *TP53BP2*/*FBXO28* via spatial proximity.

## Synthesized notes

None yet. The single-cell 3D-genome story is well-served by Hong 2025 and Jiang 2026 in tandem.

## Open questions

- Resolution: most sc3DG methods give ~1 Mb effective resolution per cell; bulk Hi-C achieves ~kb. Will ultra-deep single-cell or imaging-based methods (multiplexed FISH) close the gap?
- Causality: do TAD/loop changes drive gene-expression changes or follow them? Multi-omics methods (sn-m3C, HiRES) begin to address this.
- Single-cell SV-driven 3D rearrangements (Liu 2025) point to a new genome-instability axis.

## Related

- [[40-Topics/chromatin-architecture]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/long-read-sequencing]]
