---
type: concept
title: scOpen
aliases: [scOpen NMF, regularized NMF imputation]
tags: [scATAC-seq, imputation, NMF, denoising]
created: 2026-06-02
updated: 2026-06-02
---

# scOpen

> An unsupervised method that imputes and denoises sparse scATAC-seq matrices via **regularized non-negative matrix factorization** (NMF) on a TF-IDF-transformed binary open/closed matrix ([[10-Summaries/li-2021-scopen]]).

## Definition

scOpen binarizes the peak × cell count matrix, applies a term-frequency–inverse-document-frequency (TF-IDF) weighting, then factorizes it with a nuclear-norm-regularized NMF solved by cyclic coordinate descent, automatically choosing rank *k* by knee detection on the residual-sum-of-squares curve ([[10-Summaries/li-2021-scopen]]). It returns both a full imputed matrix and a low-dimensional reduced matrix (the factor **H**), with per-iteration time complexity O((m+n)k) ([[10-Summaries/li-2021-scopen]]).

## Why it matters

- scATAC-seq matrices are ~3–7% non-zero — far sparser than scRNA-seq — because each diploid peak has at most two capturable cut sites, most lost in library prep ([[10-Summaries/li-2021-scopen]]).
- Regularization is scOpen's distinguishing feature: it is the only benchmarked imputation method that regularizes to prevent overfitting, a known failure mode of single-cell imputation ([[10-Summaries/li-2021-scopen]]).
- Lowest memory footprint among scATAC imputers (≥2× less than cisTopic/MAGIC/SCALE) with tractable runtime on 10k-cell data ([[10-Summaries/li-2021-scopen]]).

## How it compares

- Outperforms 8 imputation methods (MAGIC, SAVER, scImpute, DCA, scBFA, cisTopic-impute, SCALE, imputePCA) on AUPR for recovering true open-chromatin regions, silhouette score, and clustering ARI ([[10-Summaries/li-2021-scopen]]).
- Beats dimension-reduction pipelines cisTopic, SnapATAC, and LSI/Cusanovich2018 on distance and clustering ([[10-Summaries/li-2021-scopen]]); see [[30-Concepts/scatac-imputation]] for the full landscape.

## Examples

- Improves downstream chromVAR, Cicero co-accessibility, and scABC clustering when used as input ([[10-Summaries/li-2021-scopen]]).
- Applied with HINT-ATAC footprinting to a 30k-cell mouse kidney fibrosis (UUO) time course, identifying Runx1 as the driver of fibroblast→myofibroblast differentiation ([[10-Summaries/li-2021-scopen]]).

## Related

- [[30-Concepts/scatac-imputation]] · [[30-Concepts/scale]] · [[30-Concepts/cistopic]] · [[30-Concepts/scatac-seq]] · [[30-Concepts/chromvar]]
- [[40-Topics/single-cell-atac-seq]] · [[20-Entities/ivan-costa]]
