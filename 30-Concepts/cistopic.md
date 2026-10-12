---
type: concept
title: cisTopic
aliases: [LDA-based scATAC clustering]
tags: [scATAC-seq, topic-modeling, LDA, Aerts-lab, software]
created: 2026-05-12
updated: 2026-10-12
---

# cisTopic

> An R/Bioconductor package by the Aerts lab that applies Latent Dirichlet Allocation (LDA) with collapsed Gibbs sampling to scATAC-seq, co-optimizing the clustering of cells and the clustering of regulatory regions into "cis-regulatory topics" ([[10-Summaries/bravo-2019-cistopic|cisTopic]]).

> [!abstract] 한눈에
> cisTopic은 scATAC-seq의 cell × region 행렬에 LDA를 적용해 세포와 조절 영역을 한꺼번에 topic으로 묶고, 같은 TF가 분화 단계마다 다른 조절 프로그램을 쓰는 모습까지 분리해 낸다 ([[10-Summaries/bravo-2019-cistopic|cisTopic]]). scATAC 벤치마크에서는 상위권이었지만 batch를 보정하지 못하고, histone PTM 데이터에서는 TF-IDF 계열 방법보다 뒤처졌다 ([[10-Summaries/ashuach-2022-peakvi|PeakVI]]; [[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]).

## Definition

cisTopic, from [[20-Entities/stein-aerts]]'s lab, takes a binary cell × region accessibility matrix as input ([[10-Summaries/bravo-2019-cistopic|cisTopic]]). [[30-Concepts/latent-dirichlet-allocation]] derives two distributions: region-topic (which regions belong to which topic) and topic-cell (how each cell's accessibility maps to topics) ([[10-Summaries/bravo-2019-cistopic|cisTopic]]). Topics can be interpreted as combinatorial regulatory programs ([[10-Summaries/bravo-2019-cistopic|cisTopic]]).

## Why it matters

- It resolves temporal heterogeneity that [[30-Concepts/chromvar]] averages away — for example GATA-mediated regulation at HSC, intermediate and MEP stages, each a distinct topic ([[10-Summaries/bravo-2019-cistopic|cisTopic]]).
- It handles the sparsity of [[30-Concepts/scatac-seq]] naturally via topic aggregation ([[10-Summaries/bravo-2019-cistopic|cisTopic]]).
- Topic regions enrich for TF motifs that correspond to cell-type master regulators ([[10-Summaries/bravo-2019-cistopic|cisTopic]]).
- Its multiplied topic-cell × region-topic distributions also serve as an imputation ("cisTopic-impute"), a baseline later benchmarked against [[30-Concepts/scopen]] and [[30-Concepts/scale]] ([[10-Summaries/li-2021-scopen|scOpen]]; [[10-Summaries/xiong-2019-scale|SCALE]]); see [[30-Concepts/scatac-imputation]].

## Benchmarks and extensions

| Context | How cisTopic fared or was extended | Source |
|---|---|---|
| PeakVI benchmark (10x PBMC multiome, sorted haematopoietic cells) | Nearly as good as PeakVI at matching RNA-defined clusters and separating sorted cell types, but did not correct batch effects | ([[10-Summaries/ashuach-2022-peakvi\|PeakVI]]) |
| EpiAgent comparison | EpiAgent reports outperforming cisTopic on NMI and ARI after fine-tuning | ([[10-Summaries/chen-2025-epiagent\|EpiAgent]]) |
| Single-cell histone PTM benchmark | Ranked behind the TF-IDF methods (ChromSCape_LSI, TFIDF-NMF, Signac) and behind [[30-Concepts/snapatac]] and PeakVI | ([[10-Summaries/raimundo-2023-schptm-benchmark\|Raimundo 2023]]) |
| CoBATCH Pol II and H3K36me3 profiles | Applied with 15 topics beyond accessibility data | ([[10-Summaries/wang-2019-cobatch\|CoBATCH]]) |
| GFETM | Classes cisTopic with PCA, Cicero, SCALE and PeakVI as sequence-free; extends the topic model to an embedded topic model (a VAE with a linear, interpretable decoder) whose peak embeddings come from a genome foundation model | ([[10-Summaries/fan-2026-gfetm\|GFETM]]) |

## Evidence and examples

- cisTopic was applied to haematopoietic differentiation, brain cell types (cortical excitatory layers, glia) and SOX10-knockdown dynamics in melanoma ([[10-Summaries/bravo-2019-cistopic|cisTopic]]).
- On CoBATCH profiles of E16.5 cardiac Cdh5-traced cells, it resolved macrophage-like, mesenchymal, arterial and venous endothelial clusters ([[10-Summaries/wang-2019-cobatch|CoBATCH]]).

## Contested points

- **Accessibility benchmarks do not transfer to histone data.** cisTopic ranked behind TF-IDF methods on single-cell histone PTM data despite being among the best tools in an earlier scATAC-seq benchmark ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]).
- **No sequence information.** GFETM argues that sequence-free methods such as cisTopic ignore the DNA under each peak ([[10-Summaries/fan-2026-gfetm|GFETM]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/latent-dirichlet-allocation|Latent Dirichlet allocation]] — The topic model cisTopic applies.
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Single-cell chromatin accessibility by Tn5 transposition.
> - `concept` [[30-Concepts/chromvar|chromVAR]] — Motif-level accessibility deviations; complementary to topics.
> - `concept` [[30-Concepts/snapatac|SnapATAC]] — Bin-based scATAC clustering compared in benchmarks.
> - `concept` [[30-Concepts/scatac-imputation|scATAC imputation]] — Where cisTopic-impute serves as a baseline.
> - `concept` [[30-Concepts/scopen|scOpen]] — Regularized-NMF imputation benchmarked against cisTopic.
> - `concept` [[30-Concepts/scale|SCALE]] — VAE plus Gaussian mixture for scATAC.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Methods and analysis for single-cell chromatin accessibility.

## All sources on this page

> [!info]- 8 summaries cited here
> - [[10-Summaries/ashuach-2022-peakvi|Ashuach 2022]]
> - [[10-Summaries/bravo-2019-cistopic|Bravo González-Blas 2019]]
> - [[10-Summaries/chen-2025-epiagent|Chen 2025]]
> - [[10-Summaries/fan-2026-gfetm|Fan 2026]]
> - [[10-Summaries/li-2021-scopen|Li 2021]]
> - [[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]
> - [[10-Summaries/wang-2019-cobatch|Wang 2019]]
> - [[10-Summaries/xiong-2019-scale|Xiong 2019]]
