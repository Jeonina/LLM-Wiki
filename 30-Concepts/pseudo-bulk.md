---
type: concept
title: Pseudo-bulk
aliases: [aggregation, in-silico bulk]
tags: [single-cell, aggregation, cluster, analysis]
created: 2026-05-12
updated: 2026-10-12
---

# Pseudo-bulk

> A common analysis pattern where reads from many single cells of the same identified type (cluster) are aggregated into a "pseudo-bulk" profile, enabling robust peak calling, motif analysis, differential testing, or comparison to true bulk data ([[10-Summaries/gur-2025-scatac-vs-bulk|Gur & Hughes 2025]]).

> [!abstract] 한눈에
> Pseudo-bulk는 같은 cluster로 묶인 세포들의 read를 합쳐 bulk 수준의 profile을 만드는 방법이며, scATAC에서는 수백 개 세포를 합치면 bulk ATAC과 같은 신호를 얻는다 ([[10-Summaries/gur-2025-scatac-vs-bulk|Gur & Hughes 2025]]). 다만 합치는 것이 늘 최선은 아니어서, 세포 하나하나를 단위로 다루면 더 많은 loop를 찾거나 연속적인 상태를 보존할 수 있다 ([[10-Summaries/li-2022-snaphic2|SnapHiC2]]; [[10-Summaries/lal-2026-decima|Decima]]).

## Definition

Pseudo-bulk aggregates reads from cells of one identified type into a single profile ([[10-Summaries/gur-2025-scatac-vs-bulk|Gur & Hughes 2025]]). It is conceptually closer to "bulk RNA-seq of a sorted cell type" than to "bulk RNA-seq of unfractionated tissue" (synthesis). The benefit over original bulk: cell-type composition is *known* (from the single-cell clustering), so apparent expression changes can be attributed to per-cell transcription rather than to composition shifts — addressing one of the central limitations of bulk RNA-seq for heterogeneous samples (synthesis; see [[30-Concepts/scrna-seq]] § Bulk RNA-seq vs scRNA-seq).

## Why it matters

- Single cells are sparse; aggregating ~hundreds of cells gives a profile of similar quality to bulk sequencing for that cell type ([[10-Summaries/gur-2025-scatac-vs-bulk|Gur & Hughes 2025]]).
- Pseudo-bulking is used in essentially every single-cell ATAC, RNA, and chromatin pipeline (synthesis).
- Pseudo-bulk is the bridge between cell-resolved data and bulk-style differential-expression frameworks (synthesis).

## Uses

| Use | Assay | What pooling buys | Source |
|---|---|---|---|
| Bulk-equivalent profiles plus heterogeneity | scATAC-seq | Pseudo-bulked scATAC matches bulk and adds within-population heterogeneity detection | ([[10-Summaries/gur-2025-scatac-vs-bulk\|Gur & Hughes 2025]]) |
| Composite methylomes | scWGBS | An early pseudo-bulk construction for DNA methylation: pooling dozens of one-cell or four-cell methylomes gives near-complete CpG coverage plus an inherent estimate of cell-to-cell variation | ([[10-Summaries/farlik-2015-scwgbs\|Farlik 2015]]) |
| Recovering off-target reads | sciMET-cap | About 70% of reads fall off target; aggregated per cluster, they yield near-complete methylomes | ([[10-Summaries/acharya-2024-scimet-cap\|sciMET-cap]]) |
| Peak calling, correlation and chromatin states | scCUT&Tag | Because scCUT&Tag is so sparse, peak calling and global correlation analyses (e.g. against ENCODE ChIP-seq) run on pseudobulk profiles, and ChromHMM states are learned from multi-mark pseudobulk tracks | ([[10-Summaries/wu-2026-sccut-tag-review\|Wu 2026]]) |
| Single-cell peak calling with a control | DeChIC-seq | Pseudo-bulk merges plus a simulated pseudo-IgG | ([[10-Summaries/shi-2026-dechic-seq\|DeChIC-seq]]) |
| Matched normal from the same sample | SPLONGGET | Reads from non-tumour cells across time points form a normal pseudobulk for tumour–normal ASCAT, Severus and ClairS-TO calling against tumour pseudobulks | ([[10-Summaries/pancikova-2025-splongget\|SPLONGGET]]) |
| Priors for imputation | scATAC-seq (scCASER) | References built by aggregating a paired dataset from the same tissue by cell type, or the target dataset by its own Louvain clusters (a "self-reference") | ([[10-Summaries/tang-2024-sccase\|scCASE]]) |
| Training targets for sequence models | scATAC-seq | ChromBPNet trained on GM12878 pseudobulk scATAC | ([[10-Summaries/pampari-2024-chrombpnet\|ChromBPNet]]) |
| Training targets for sequence models | scATAC-seq | Borzoi's training targets include pseudobulk scATAC tracks from CATlas | ([[10-Summaries/linder-2025-borzoi\|Borzoi]]) |
| Training targets for sequence models | sc/snRNA-seq | Decima trains on pseudobulked sc/snRNA-seq instead of single cells, which lets it scale to more than 22 million cells across 201 cell types and 82 diseases | ([[10-Summaries/lal-2026-decima\|Decima]]) |

## When not to pool

- OneCell CUT&Tag is explicitly designed to avoid pseudobulk or metacell aggregation; its ~26,000 median unique fragments per cell let single-cell coverage tracks be read at 1-Mb resolution, whereas droplet methods at ~5,000 reads/cell required pseudobulk of clustered cells ([[10-Summaries/schwager-2026-onecell-cut-tag|OneCell CUT&Tag]]).
- Pooling cells is not always the power-maximising choice for loop calling ([[10-Summaries/li-2022-snaphic2|SnapHiC2]]).
- Single-cell profiles predicted by scooby correlated with observed profiles better than the cell's own pseudobulk did ([[10-Summaries/hingerl-2025-scooby|scooby]]).

## Evidence and examples

- scATAC-seq with pseudo-bulk aggregation gives the same chromatin signal as bulk ATAC-seq and adds within-population heterogeneity detection ([[10-Summaries/gur-2025-scatac-vs-bulk|Gur & Hughes 2025]]).
- sciMET-cap cluster aggregates reached a median 96.0% of 1,500-bp windows with ≥10 CpG coverage across 14 PBMC clusters ([[10-Summaries/acharya-2024-scimet-cap|sciMET-cap]]). The abstract says genome-wide DMR calling works for clusters as small as 115 cells ([[10-Summaries/acharya-2024-scimet-cap|sciMET-cap]]).
- Pooled HiCCUPS on 742 mESCs found 6 chr3 loops at 5 kb, while SnapHiC2, treating each cell as a unit, found 294 ([[10-Summaries/li-2022-snaphic2|SnapHiC2]]).
- In scCASE, both the paired-dataset reference and the self-reference improve enhancement over using no reference ([[10-Summaries/tang-2024-sccase|scCASE]]).
- ChromBPNet trained on GM12878 pseudobulk scATAC from 11,000 down to ~100 cells imputed profiles and motifs with the same depth trends as bulk subsampling, though rare-motif recall and variant classification drop below ~25 M reads ([[10-Summaries/pampari-2024-chrombpnet|ChromBPNet]]).
- scooby's predicted single-cell profiles beat the cell's own pseudobulk (RNA 0.15 vs 0.09, ATAC 0.11 vs 0.08) but remained far below the 100-nearest-neighbour average used as the upper bound ([[10-Summaries/hingerl-2025-scooby|scooby]]).
- Borzoi ablations showed that adding DNase/ATAC data to RNA-seq improved test accuracy, eQTL concordance and enhancer–gene linking ([[10-Summaries/linder-2025-borzoi|Borzoi]]).
- SPLONGGET's authors argue that a normal pseudobulk avoids extra sampling or sorting when no germline control is taken, for example in tumour biopsies ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).

## Contested points

- Pooling trades resolution for depth (synthesis): Decima's pseudobulk training collapses continuous states and donors ([[10-Summaries/lal-2026-decima|Decima]]), and per-cell loop calling found far more loops than pooled calling ([[10-Summaries/li-2022-snaphic2|SnapHiC2]]).
- A dedicated method for matching cells across marks or modalities is still lacking in scCUT&Tag, beyond pseudobulk or metacell aggregation ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Genome-wide chromatin accessibility in individual cells, read out by Tn5 insertion.
> - `concept` [[30-Concepts/snapatac|SnapATAC]] — Peak-free scATAC-seq pipeline built on 5-kb bins and Jaccard similarity between cells.
> - `concept` [[30-Concepts/scrna-seq|scRNA-seq]] — Per-cell expression profiling; pseudo-bulk bridges it to bulk-style differential-expression frameworks.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Chromatin accessibility in single cells and the sparsity that drives aggregation.

## All sources on this page

> [!info]- 13 summaries cited here
> - [[10-Summaries/acharya-2024-scimet-cap|Acharya 2024]]
> - [[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]
> - [[10-Summaries/gur-2025-scatac-vs-bulk|Gur & Hughes 2025]]
> - [[10-Summaries/hingerl-2025-scooby|scooby 2025]]
> - [[10-Summaries/lal-2026-decima|Decima 2026]]
> - [[10-Summaries/li-2022-snaphic2|Li 2022]]
> - [[10-Summaries/linder-2025-borzoi|Borzoi 2025]]
> - [[10-Summaries/pampari-2024-chrombpnet|ChromBPNet 2024]]
> - [[10-Summaries/pancikova-2025-splongget|Pančíková 2025 (bioRxiv preprint)]]
> - [[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]
> - [[10-Summaries/shi-2026-dechic-seq|Shi 2026]]
> - [[10-Summaries/tang-2024-sccase|Tang 2024]]
> - [[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]
