---
type: concept
title: Pseudo-bulk
aliases: [aggregation, in-silico bulk]
tags: [single-cell, aggregation, cluster, analysis]
created: 2026-05-12
updated: 2026-10-08
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

Cell-type labels can build a matched normal from the same sample. SPLONGGET pools reads from non-tumour cells across time points into a normal pseudobulk and runs tumour–normal ASCAT, Severus and ClairS-TO calling against tumour pseudobulks ([[10-Summaries/pancikova-2025-splongget]]). The authors argue this avoids extra sampling or sorting when no germline control is taken, for example in tumour biopsies ([[10-Summaries/pancikova-2025-splongget]]).

## Added 2026-10-08 — sequence models & foundation models

- ChromBPNet trained on GM12878 pseudobulk scATAC from 11,000 down to ~100 cells imputed profiles and motifs with the same depth trends as bulk subsampling, though rare-motif recall and variant classification drop below ~25 M reads ([[10-Summaries/pampari-2024-chrombpnet]])
- Single-cell profiles predicted by scooby correlated with observed profiles better than the cell's own pseudobulk did (RNA 0.15 vs 0.09, ATAC 0.11 vs 0.08), but remained far below the 100-nearest-neighbour average used as the upper bound ([[10-Summaries/hingerl-2025-scooby]]).
- Borzoi's training targets include pseudobulk scATAC tracks from CATlas, and ablations showed that adding DNase/ATAC data to RNA-seq improved test accuracy, eQTL concordance and enhancer–gene linking ([[10-Summaries/linder-2025-borzoi]])
- Decima trains on pseudobulked sc/snRNA-seq instead of single cells, which lets it scale to more than 22 million cells across 201 cell types and 82 diseases at the cost of collapsing continuous states and donors ([[10-Summaries/lal-2026-decima]]).

## Related

- [[30-Concepts/scatac-seq]] · [[30-Concepts/snapatac]] · [[40-Topics/single-cell-atac-seq]]
- [[30-Concepts/scrna-seq]] — pseudo-bulk is the bridge between cell-resolved data and bulk-style differential-expression frameworks
