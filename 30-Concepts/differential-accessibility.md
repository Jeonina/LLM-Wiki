---
type: concept
title: "Differential Accessibility Analysis"
aliases: []
tags: []
created: 2026-10-07
updated: 2026-10-12
sources: ["[[10-Summaries/ashuach-2022-peakvi]]", "[[10-Summaries/zhao-2024-scada]]"]
---

# Differential Accessibility Analysis

> Differential accessibility (DA) analysis identifies chromatin regions whose accessibility differs between cell groups or conditions in scATAC-seq data ([[10-Summaries/zhao-2024-scada|scaDA]]).

> [!abstract] 한눈에
> Differential accessibility 분석은 scATAC-seq에서 세포 집단이나 조건에 따라 accessibility가 다른 영역을 찾는 일이다 ([[10-Summaries/zhao-2024-scada|scaDA]]). 흔히 쓰는 Wilcoxon 검정의 calibration은 benchmark마다 결론이 달라 아직 정리되지 않았다 ([[10-Summaries/ashuach-2022-peakvi|PeakVI]]; [[10-Summaries/zhao-2024-scada|scaDA]]).

## Approaches

- Generative/posterior: PeakVI samples denoised accessibility from a VAE posterior and uses an absolute-difference effect size with a Bayesian FDR ([[10-Summaries/ashuach-2022-peakvi|PeakVI]]).
- Distributional: scaDA fits a zero-inflated negative binomial per peak and jointly tests mean, prevalence and dispersion, with empirical-Bayes dispersion shrinkage ([[10-Summaries/zhao-2024-scada|scaDA]]).
- Standard tests: Wilcoxon (ArchR, scATAC-pro) and logistic regression (Signac) are the common defaults ([[10-Summaries/ashuach-2022-peakvi|PeakVI]]; [[10-Summaries/zhao-2024-scada|scaDA]]).

## Contested points

- In a replicate-vs-replicate null, Wilcoxon called 6,761 regions and a GLM 910 versus 0 for PeakVI ([[10-Summaries/ashuach-2022-peakvi|PeakVI]]); in scaDA's ZINB simulations, by contrast, scATAC-pro's Wilcoxon test was overly conservative rather than inflated ([[10-Summaries/zhao-2024-scada|scaDA]]). The two benchmarks use different nulls and data, so calibration of Wilcoxon-based DA remains unsettled (synthesis).
- Real-data ground truth is usually indirect — bulk ATAC ([[10-Summaries/ashuach-2022-peakvi|PeakVI]]) or proximity to differentially expressed genes ([[10-Summaries/zhao-2024-scada|scaDA]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — Whether a region of DNA is open or closed to regulatory machinery.
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Genome-wide chromatin accessibility in single cells, read out by Tn5.
> - `concept` [[30-Concepts/pseudo-bulk|Pseudo-bulk]] — Aggregating reads from cells of one cluster into a bulk-like profile.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — scATAC-seq methods, analysis and applications.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/ashuach-2022-peakvi|Ashuach 2022]]
> - [[10-Summaries/zhao-2024-scada|Zhao 2024]]
