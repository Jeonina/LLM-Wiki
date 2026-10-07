---
type: concept
title: "Differential Accessibility Analysis"
aliases: []
tags: []
created: 2026-10-07
updated: 2026-10-07
sources: ["[[10-Summaries/ashuach-2022-peakvi]]", "[[10-Summaries/zhao-2024-scada]]"]
---

# Differential Accessibility Analysis

> Differential accessibility (DA) analysis identifies chromatin regions whose accessibility differs between cell groups or conditions in scATAC-seq data ([[10-Summaries/zhao-2024-scada]]).

## Approaches

- Generative/posterior: PeakVI samples denoised accessibility from a VAE posterior and uses an absolute-difference effect size with a Bayesian FDR ([[10-Summaries/ashuach-2022-peakvi]]).
- Distributional: scaDA fits a zero-inflated negative binomial per peak and jointly tests mean, prevalence and dispersion, with empirical-Bayes dispersion shrinkage ([[10-Summaries/zhao-2024-scada]]).
- Standard tests: Wilcoxon (ArchR, scATAC-pro) and logistic regression (Signac) are the common defaults ([[10-Summaries/ashuach-2022-peakvi]], [[10-Summaries/zhao-2024-scada]]).

## Contested points

- In a replicate-vs-replicate null, Wilcoxon called 6,761 regions and a GLM 910 versus 0 for PeakVI ([[10-Summaries/ashuach-2022-peakvi]]); in scaDA's ZINB simulations, by contrast, scATAC-pro's Wilcoxon test was overly conservative rather than inflated ([[10-Summaries/zhao-2024-scada]]). The two benchmarks use different nulls and data, so calibration of Wilcoxon-based DA remains unsettled (synthesis).
- Real-data ground truth is usually indirect — bulk ATAC ([[10-Summaries/ashuach-2022-peakvi]]) or proximity to differentially expressed genes ([[10-Summaries/zhao-2024-scada]]).

## Related

- [[chromatin-accessibility]] · [[scatac-seq]] · [[pseudo-bulk]] · [[40-Topics/single-cell-atac-seq]]
