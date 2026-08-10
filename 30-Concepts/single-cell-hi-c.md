---
type: concept
title: Single-cell Hi-C
aliases: [scHi-C, sciHi-C, sc3DG-seq]
tags: [3D-genome, Hi-C, chromatin-contacts, single-cell]
created: 2026-05-12
updated: 2026-08-10
---

# Single-cell Hi-C

> A family of methods (scHi-C, sciHi-C, Dip-C, sn-m3C, snHi-C, HiRES, scSPRITE, scNanoHi-C, Droplet Hi-C, GAGE-seq) that profile genome-wide chromatin contacts at single-cell resolution.

## Definition

Most methods inherit the 3C/Hi-C ligation strategy (crosslink → restrict → ligate proximity-tagged fragments → sequence) and add per-cell partitioning (microfluidic, FACS plate-based, or combinatorial-indexing). scSPRITE replaces ligation with sonication-based spatial clustering; scNanoHi-C uses long reads to capture multi-way contacts.

## Why it matters

Reveals cell-to-cell variability in TADs, A/B compartments, and chromatin loops — variability that bulk Hi-C averages away. Critical for understanding lineage decisions, disease heterogeneity, and cell-cycle dynamics of 3D architecture.

## Examples

- See [[10-Summaries/hong-2025-sc3d-genome-review]] for the technology landscape.
- [[10-Summaries/jiang-2026-stark-scnucleome]] benchmarks 15 sc3DG-seq methods.

## Added 2026-08-10

Assay origin: [[10-Summaries/lieberman-aiden-2009-hic]], whose *n*²-resolution rule is the source of the sparsity constraint every single-cell variant negotiates with. High-throughput branch: [[10-Summaries/ramani-2017-scihi-c]] (combinatorial indexing, 10,696 cells at ~8,000–9,000 contacts each, in-silico cell-cycle sorting, translocations recoverable from contact structure).

The sparsity arithmetic: 5–10% linear genome coverage becomes **0.25–1% of possible contacts**, and coverage heterogeneity — not biology — is the leading factor driving clustering results ([[10-Summaries/zhou-2019-schicluster]]). Clustering degrades below 25,000 contacts per cell and collapses at 5,000 ([[10-Summaries/zhou-2019-schicluster]]), which is below what indexing-based protocols deliver. Imputation is therefore not optional: [[10-Summaries/zhou-2019-schicluster]] (convolution + random walk + top-20% selection) and [[10-Summaries/zhang-2022-higashi]] (hypergraph representation learning, sparse-native, borrowing across cells).


## Related

- [[40-Topics/3d-genome]] · [[30-Concepts/topologically-associating-domain]] · [[30-Concepts/chromatin-compartments]] · [[40-Topics/3d-genome]]
