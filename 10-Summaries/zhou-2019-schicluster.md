---
type: summary
title: "Zhou et al. 2019 — Robust single-cell Hi-C clustering by convolution- and random-walk-based imputation (scHiCluster)"
source: "[[00-Sources/papers/Robust single-cell Hi-C clustering by convolution- and random-walk–based imputation]]"
source_kind: paper
author: "Jingtian Zhou, Jianzhu Ma, Yusi Chen, Chuankai Cheng, Bokan Bao, Jian Peng, Terrence J. Sejnowski, Jesse R. Dixon, Joseph R. Ecker"
published: 2019-05-20
ingested: 2026-08-10
doi: "10.1073/pnas.1901423116"
journal: "PNAS"
tags: [scHiCluster, imputation, random-walk, convolution, clustering, TAD-like-structures, coverage-bias]
entities: ["[[joseph-ecker]]", "[[jesse-dixon]]"]
concepts: ["[[single-cell-hi-c]]", "[[imputation]]", "[[topologically-associating-domain]]", "[[dimensionality-reduction]]", "[[batch-effect]]"]
topics: ["[[3d-genome]]", "[[computational-methods]]"]
---

**Citation:** Zhou et al. (2019) — *Robust single-cell Hi-C clustering by convolution- and random-walk-based imputation* — *PNAS* 116, 14011–14018. [DOI](https://doi.org/10.1073/pnas.1901423116)

# Zhou 2019 — scHiCluster

> Three steps to make sparse single-cell contact matrices clusterable: **linear convolution** (each element replaced by a weighted average of its neighbourhood, sharing information along the linear genome), **random walk with restart** (sharing information among network neighbours), and **keeping only the top 20% of imputed interactions** to strip out coverage bias. Then project into a shared low-dimensional space and cluster.

## Key claims

- **The three challenges, named explicitly.** (1) Intrinsic variability — imaging shows large heterogeneity in locus positioning even within one cell type, and how that compares to between-type variation is unknown. (2) **Sparsity**: single-cell DNA assays cover 5–10% of the linear genome, but because Hi-C data is a 2D matrix, that translates to **0.25–1% of all possible contacts**. (3) **Coverage heterogeneity**, which the authors find is "the leading factor to drive clustering results" and is not cleanly removable by dropping PC1, since PC1 also carries biology.
- The **top-20% selection** is the coverage-bias fix, and the ablation shows all three steps are required — PCA, convolution-only, random-walk-only, and every two-step combination all underperform the full pipeline.
- **Simulation design matters here**: naively downsampling bulk Hi-C produces cells that are *less* sparse and more evenly distributed than real ones, giving optimistically good clustering. The authors control sparsity and add noise to the contact–distance curve so simulated cells are indistinguishable from real ones on the first two PCs.
- On simulated data from seven human (Rao) and three mouse (Bonev) cell types, scHiCluster consistently beats PCA by adjusted Rand index. Performance **degrades below 25,000 contacts and collapses at 5,000**, where coverage bias can no longer be removed. **1 Mb resolution outperformed 200 kb** — lower resolution, lower sparsity, is sufficient for cell typing.
- On real data ([[ramani-2017-scihi-c|Ramani]], median 10.0 k contacts; Flyamer, median 97.3 k) scHiCluster beats PCA, HiCRep+MDS, the eigenvector method and the decay-profile method on both visualization and ARI. The higher-coverage [[tan-2018-science|Tan]] dataset (median 513 k) was excluded because simple PCA already separates it.
- **Speed**: ~30–60 seconds versus **8 hours (Flyamer) and 4.5 days (Ramani)** for HiCRep, which is designed for pairwise comparison and therefore repeats work across a cohort.
- **The PCs are interpretable.** PC1 weights lie uniformly parallel to the diagonal — it captures the contact–distance curve, i.e. cell cycle. PC2 weights are region-specific — it captures compartment strength. This explains why oocytes/zygotes separate on PC1 while cancer cell lines separate on PC2.
- **TAD-like structures (TLSs)**, not TADs. Merging imputed matrices within a cluster reveals square diagonal patterns; the authors deliberately avoid calling them TADs because single-cell TAD existence is unsettled and sparsity limits identification. A TLS at chr9:133.6–134.2 Mb appears in 9/10 K562 cells but 2/10 GM12878 cells, matches bulk Hi-C, and coincides with higher K562 expression and H3K4me1.

## Methods / evidence

Two simulation frameworks (with the explicit correction for over-optimistic bulk downsampling), three real datasets spanning two orders of magnitude in coverage, four baseline methods, a full ablation over all one- and two-step combinations, parameter-sensitivity analysis, runtime benchmarking, per-chromosome analysis, and a cell-cycle recovery check on the Nagano 1,992-cell dataset.

Baselines were given their best possible configuration (all combinations of clustering method and PC count) while scHiCluster used a fixed K-means on 10 PCs — a deliberately unfavourable comparison for the authors' own method.

## Surprising or load-bearing bits

- **The 5–10% linear coverage → 0.25–1% contact coverage conversion is the single most useful number here.** Sparsity squares when you move from one dimension to two. It explains why single-cell Hi-C is qualitatively harder than scATAC or scWGS, and it is the quantitative form of [[lieberman-aiden-2009-hic|Hi-C's]] *n*²-resolution rule applied per cell.
- **Coverage is the leading source of variation, ahead of biology**, and it is not separable by simply removing PC1. Any single-cell Hi-C clustering that has not explicitly addressed coverage bias may be clustering library depth.
- **Per-chromosome results split by task**: nearly every chromosome alone separates oocytes from zygotes (a global structural difference), but only one chromosome separates the human cancer cell lines. Global conformational states are cheap to detect; cell-type distinctions need the whole genome or careful feature selection.
- **"TAD-like structures" is honest naming that later work partly abandoned.** [[zhang-2022-higashi|Higashi]] says "TAD-like domain boundaries" and reports insulation scores; the caution is warranted given that [[kerpedjiev-2018-higlass|seven TAD callers disagree on bulk data]].
- The **25,000-contact floor** is a concrete design constraint for experiments: sciHi-C's ~8,000–10,000 contacts per cell sits *below* it, which is why sciHi-C data needs either the strongest imputation available or aggregation.
- Random-walk imputation requires **dense matrices in memory**, the limitation [[zhang-2022-higashi|Higashi]] later targets directly with its sparse hypergraph formulation.

## Entities mentioned

- [[joseph-ecker]] — senior author; also the sn-m3C-seq and single-cell methylome programs.
- [[jesse-dixon]] — co-author; first author of [[dixon-2012-tads]].

## Concepts touched

- [[imputation]] — convolution plus random walk with restart as the first widely used scHi-C imputation scheme.
- [[single-cell-hi-c]] — the sparsity arithmetic and the coverage-bias problem.

## Connections to other sources

- Input datasets: [[ramani-2017-scihi-c]], [[nagano-2013-nature]], [[tan-2018-science]].
- Superseded on both embedding and imputation by [[zhang-2022-higashi]], which uses it as the primary baseline.
- Features being recovered: [[dixon-2012-tads]] (domains), [[lieberman-aiden-2009-hic]] (compartments).
- Storage and pipeline context: [[abdennur-2020-cooler]], [[servant-2015-hicpro]].

## Open questions

- **Whether TLSs are real per-cell structures or imputation artefacts is left open by the authors themselves** — they are validated against bulk and against expression, but not against an independent per-cell measurement.
- How within-cell-type conformational fluctuation compares to between-cell-type variation is stated as unknown in the introduction and is not resolved.
- Smoothing that makes cells clusterable necessarily reduces apparent cell-to-cell variability; the trade-off is not quantified here.

## Related

- [[zhang-2022-higashi]] · [[imputation]] · [[single-cell-hi-c]] · [[3d-genome]]
