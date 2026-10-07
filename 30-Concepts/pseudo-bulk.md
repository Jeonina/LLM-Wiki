---
type: concept
title: Pseudo-bulk
aliases: [aggregation, in-silico bulk]
tags: [single-cell, aggregation, cluster, analysis]
created: 2026-05-12
updated: 2026-10-07
---

# Pseudo-bulk

> A common analysis pattern where reads from many single cells of the same identified type (cluster) are aggregated into a "pseudo-bulk" profile, enabling robust peak calling, motif analysis, differential testing, or comparison to true bulk data.

## Why it matters

Single cells are sparse; aggregating ~hundreds of cells gives a profile of similar quality to bulk sequencing for that cell type. Pseudo-bulking is used in essentially every single-cell ATAC, RNA, and chromatin pipeline.

## Why pseudo-bulk ≠ original bulk

Pseudo-bulk is conceptually closer to "bulk RNA-seq of a sorted cell type" than to "bulk RNA-seq of unfractionated tissue." The benefit over original bulk: cell-type composition is *known* (from the single-cell clustering), so apparent expression changes can be attributed to per-cell transcription rather than to composition shifts — addressing one of the central limitations of bulk RNA-seq for heterogeneous samples (see [[30-Concepts/scrna-seq]] § Bulk RNA-seq vs scRNA-seq).

## Examples

- [[10-Summaries/gur-2025-scatac-vs-bulk]] (Gur/Hughes 2025) — pseudo-bulked scATAC matches bulk and adds within-population heterogeneity detection.

## Added 2026-10-07

'Composite methylomes' are an early pseudo-bulk construction for DNA methylation. Pooling dozens of one-cell or four-cell methylomes gives near-complete CpG coverage plus an inherent estimate of cell-to-cell variation ([[10-Summaries/farlik-2015-scwgbs]]).

OneCell CUT&Tag is explicitly designed to avoid pseudobulk or metacell aggregation. Its ~26,000 median unique fragments per cell let single-cell coverage tracks be read at 1-Mb resolution, whereas droplet methods at ~5,000 reads/cell required pseudobulk of clustered cells ([[10-Summaries/schwager-2026-onecell-cut-tag]]).

Pooling cells is not always the power-maximising choice: pooled HiCCUPS on 742 mESCs found 6 chr3 loops at 5 kb, while SnapHiC2, treating each cell as a unit, found 294 ([[10-Summaries/li-2022-snaphic2]]). DeChIC-seq instead uses pseudo-bulk merges plus a simulated pseudo-IgG for single-cell peak calling ([[10-Summaries/shi-2026-dechic-seq]]).

Pseudo-bulk profiles can serve as priors for imputation. scCASER builds references by aggregating a paired dataset from the same tissue by cell type, or by aggregating the target dataset by its own Louvain clusters (a "self-reference"), and both improve enhancement over using no reference ([[10-Summaries/tang-2024-sccase]]).

In sciMET-cap, about 70% of reads fall off target. Aggregated per cluster, they yield near-complete methylomes: a median 96.0% of 1,500-bp windows reached ≥10 CpG coverage across 14 PBMC clusters ([[10-Summaries/acharya-2024-scimet-cap]]). The abstract says genome-wide DMR calling works for clusters as small as 115 cells ([[10-Summaries/acharya-2024-scimet-cap]]).

Because scCUT&Tag is so sparse, peak calling and global correlation analyses (e.g. against ENCODE ChIP-seq) are run on pseudobulk profiles, and ChromHMM chromatin states are learned from multi-mark pseudobulk tracks; a dedicated method for matching cells across marks or modalities is still lacking, beyond pseudobulk or metacell aggregation ([[10-Summaries/wu-2026-sccut-tag-review]]).


## Related

- [[30-Concepts/scatac-seq]] · [[30-Concepts/snapatac]] · [[40-Topics/single-cell-atac-seq]]
- [[30-Concepts/scrna-seq]] — pseudo-bulk is the bridge between cell-resolved data and bulk-style differential-expression frameworks
