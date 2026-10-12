---
type: concept
title: scOpen
aliases: [scOpen NMF, regularized NMF imputation]
tags: [scATAC-seq, imputation, NMF, denoising]
created: 2026-06-02
updated: 2026-10-12
---

# scOpen

> An unsupervised method that imputes and denoises sparse scATAC-seq matrices via **regularized non-negative matrix factorization** (NMF) on a TF-IDF-transformed binary open/closed matrix ([[10-Summaries/li-2021-scopen|scOpen]]).

> [!abstract] 한눈에
> scOpen은 binary화하고 TF-IDF를 적용한 scATAC-seq 행렬을 정규화된 NMF로 분해해 희소한 값을 채우고 잡음을 줄이는 방법이다 ([[10-Summaries/li-2021-scopen|scOpen]]). 이후 나온 scCASE가 clustering 지표에서 scOpen을 앞선다고 보고했다 ([[10-Summaries/tang-2024-sccase|scCASE]]).

## Definition

scOpen binarizes the peak × cell count matrix, applies a term-frequency–inverse-document-frequency (TF-IDF) weighting, then factorizes it with a nuclear-norm-regularized NMF solved by cyclic coordinate descent, automatically choosing rank *k* by knee detection on the residual-sum-of-squares curve ([[10-Summaries/li-2021-scopen|scOpen]]). It returns both a full imputed matrix and a low-dimensional reduced matrix (the factor **H**), with per-iteration time complexity O((m+n)k) ([[10-Summaries/li-2021-scopen|scOpen]]).

## Why it matters

- scATAC-seq matrices are ~3–7% non-zero — far sparser than scRNA-seq — because each diploid peak has at most two capturable cut sites, most lost in library prep ([[10-Summaries/li-2021-scopen|scOpen]]).
- Regularization is scOpen's distinguishing feature: it is the only benchmarked imputation method that regularizes to prevent overfitting, a known failure mode of single-cell imputation ([[10-Summaries/li-2021-scopen|scOpen]]).

## How it compares

| Compared with | Result | Source |
|---|---|---|
| 8 imputation methods (MAGIC, SAVER, scImpute, DCA, scBFA, cisTopic-impute, SCALE, imputePCA) | Outperforms them on AUPR for recovering true open-chromatin regions, silhouette score, and clustering ARI | ([[10-Summaries/li-2021-scopen\|scOpen]]) |
| Dimension-reduction pipelines (cisTopic, SnapATAC, LSI/Cusanovich2018) | Beats them on distance and clustering | ([[10-Summaries/li-2021-scopen\|scOpen]]) |
| scATAC imputers (cisTopic, MAGIC, SCALE) on memory | Lowest memory footprint (≥2× less), with tractable runtime on 10k-cell data | ([[10-Summaries/li-2021-scopen\|scOpen]]) |
| [[10-Summaries/tang-2024-sccase\|scCASE]], a later NMF-based competitor | Adopts scOpen's evaluation protocol (silhouette on 1 − Pearson distances, PCA + Louvain clustering) and reports beating scOpen on clustering metrics across eight datasets | ([[10-Summaries/tang-2024-sccase\|scCASE]]) |

See [[30-Concepts/scatac-imputation]] for the full landscape.

## Evidence and examples

- Improves downstream chromVAR, Cicero co-accessibility, and scABC clustering when used as input ([[10-Summaries/li-2021-scopen|scOpen]]).
- Applied with HINT-ATAC footprinting to a 30k-cell mouse kidney fibrosis (UUO) time course, identifying Runx1 as the driver of fibroblast→myofibroblast differentiation ([[10-Summaries/li-2021-scopen|scOpen]]).
- Going from 20k to 100k cells, scOpen's peak memory rose 8.62× compared with 7.67× for scCASE ([[10-Summaries/tang-2024-sccase|scCASE]]).

## Contested points

- scOpen reports beating other imputers on clustering ([[10-Summaries/li-2021-scopen|scOpen]]), while scCASE, using scOpen's own evaluation protocol, reports beating scOpen ([[10-Summaries/tang-2024-sccase|scCASE]]); each comparison is run by the newer method's authors (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/scatac-imputation|scATAC imputation]] — Methods that fill in or denoise sparse accessibility matrices.
> - `concept` [[30-Concepts/scale|SCALE]] — Deep generative scATAC-seq model used as an imputation comparator.
> - `concept` [[30-Concepts/cistopic|cisTopic]] — Topic modelling of scATAC-seq, a dimension-reduction comparator.
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Single-cell chromatin accessibility by Tn5 tagmentation.
> - `concept` [[30-Concepts/chromvar|chromVAR]] — TF motif accessibility deviations; a downstream tool scOpen improves.
> - `entity` [[20-Entities/ivan-costa|Ivan Costa]] — Corresponding author of scOpen.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Assays and analysis of single-cell chromatin accessibility.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/li-2021-scopen|Li 2021]]
> - [[10-Summaries/tang-2024-sccase|Tang 2024]]
