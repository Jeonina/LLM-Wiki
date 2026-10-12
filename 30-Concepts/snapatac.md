---
type: concept
title: SnapATAC
aliases: [snapATAC2]
tags: [scATAC-seq, peak-free, Ren-lab, scalable, software]
created: 2026-05-12
updated: 2026-10-12
---

# SnapATAC

> Single Nucleus Analysis Pipeline for ATAC-seq: a peak-free scATAC-seq pipeline from the Ren lab that bins the genome into 5-kb windows, computes pairwise Jaccard similarities between cells, and uses the ensemble Nyström method for scalable low-rank embedding to 1M cells ([[10-Summaries/fang-2021-snapatac|Fang 2021]]).

> [!abstract] 한눈에
> SnapATAC은 peak를 부르지 않고 5-kb bin 단위로 세포 간 Jaccard 유사도를 계산해 scATAC-seq 세포를 군집화하는 pipeline이고, Nyström 근사로 100만 세포까지 확장된다. peak 밖의 read도 세포 유형 신호를 담고 있어서 0.1% 미만의 희귀 세포 유형까지 찾아낸다 ([[10-Summaries/fang-2021-snapatac|Fang 2021]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [scATAC-seq 희소성 시뮬레이터](../60-Explainers/single-cell-atac-seq.html)
<!-- /explainer-links -->

## Definition

[[bing-ren|Ren-lab]] pipeline that represents each cell as a binary vector over 5-kb genomic bins and clusters cells from their pairwise [[jaccard-similarity|Jaccard similarity]], with no peak-calling step before clustering ([[10-Summaries/fang-2021-snapatac|Fang 2021]]).

## Why it matters

- Discovers rare cell types (<0.1% of population) that peak-anchored methods miss, because bin-level signal works even for cells too rare to define peaks ([[10-Summaries/fang-2021-snapatac|Fang 2021]]).
- Off-peak reads contribute clustering signal (they correlate with euchromatin / compartment A) ([[10-Summaries/fang-2021-snapatac|Fang 2021]]).
- Scales to 1M cells via ensemble [[nystrom-method|Nyström]] approximation ([[10-Summaries/fang-2021-snapatac|Fang 2021]]).

## Workflow

- SnapTools for preprocessing → snap file format → 5-kb binary bin vector per cell ([[10-Summaries/fang-2021-snapatac|Fang 2021]]).
- Jaccard similarity matrix → regression-normalized for depth → eigenvector decomposition ([[10-Summaries/fang-2021-snapatac|Fang 2021]]).
- Optional Harmony batch correction → clustering ([[10-Summaries/fang-2021-snapatac|Fang 2021]]).
- Also includes peak calling, enhancer-target gene linking via scRNA integration, trajectory inference, and dataset integration with scATAC atlases ([[10-Summaries/fang-2021-snapatac|Fang 2021]]).

## Evidence and examples

- Mouse secondary motor cortex (MOs): 9,529 nuclei → 31 cell populations → ~370k cREs, including rare interneurons Sst+, Vip+ ([[10-Summaries/fang-2021-snapatac|Fang 2021]]).
- On single-cell histone PTM data, SnapATAC (Jaccard similarity + kernel PCA) ranked fourth to fifth, behind the TF-IDF methods but ahead of [[cistopic|cisTopic]] and SCALE ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]).

## Contested points

- The 5-kb bin choice is empirical; cell types distinguished by sub-1-kb accessibility may need finer bins ([[10-Summaries/fang-2021-snapatac|Fang 2021]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Genome-wide accessibility in individual cells.
> - `concept` [[30-Concepts/jaccard-similarity|Jaccard similarity]] — Set-similarity metric SnapATAC uses between cells.
> - `concept` [[30-Concepts/nystrom-method|Nyström method]] — Low-rank approximation from a sampled subset of landmark cells.
> - `concept` [[30-Concepts/cistopic|cisTopic]] — LDA topic modelling for scATAC-seq, a head-to-head comparator.
> - `entity` [[20-Entities/bing-ren|Bing Ren]] — UC San Diego; SnapATAC developer.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Accessibility profiling in individual cells and its analysis tools.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/fang-2021-snapatac|Fang 2021]]
> - [[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]
