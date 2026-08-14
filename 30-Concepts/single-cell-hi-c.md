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

## Added 2026-08-13

Three 2021–2026 methods extend scHi-C beyond clustering to per-feature calling, and share a common statistical move — **treat cells as replicates rather than as reads**.

- **Loops**: [[10-Summaries/yu-2021-snaphic|SnapHiC]] imputes each cell separately (random walk with restart), then paired *t*-tests across cells at each bin pair. Pseudobulk approaches need >500–1,000 cells; SnapHiC calls 1,050–1,420 loops from 75 ([[10-Summaries/yu-2021-snaphic]]).
- **Subcompartments**: [[10-Summaries/xiong-2024-scghost|scGHOST]] embeds loci as graph nodes via constrained random walks over Higashi-imputed maps. Subcompartments resisted single-cell analysis for a coverage-arithmetic reason — bulk annotation needs ≥50M *trans* reads, and scHi-C has almost none even at pseudobulk ([[10-Summaries/xiong-2024-scghost]]).
- **Multi-way interactions**: [[10-Summaries/park-2026-mintsc|MINTsC]] reads scHi-C as a multilayer network where a multi-way contact is a clique — a question bulk Hi-C cannot express at all ([[10-Summaries/park-2026-mintsc]]).

**Systematic biases in imputed scHi-C are negligible**: normalisation against fragment size, GC content, or mappability is unnecessary, unlike bulk Hi-C — sparsity apparently swamps the systematic biases ([[10-Summaries/yu-2021-snaphic]]).

**A shared unresolved dependency**: all three assume a homogeneous cell group and report features per *cell type*, not per cell. The single-cell formulation buys statistical power but does not yet deliver per-cell feature variability ([[10-Summaries/yu-2021-snaphic]]; [[10-Summaries/park-2026-mintsc]]). (synthesis)

Cell-type labels in the brain applications come from methylation, independently of contacts ([[10-Summaries/luo-2017-snmc-seq]]; [[10-Summaries/lee-2019-natmethods]]).
