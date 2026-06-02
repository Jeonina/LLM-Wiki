---
type: concept
title: scATAC-seq imputation and denoising
aliases: [scATAC imputation, chromatin accessibility imputation, dropout recovery scATAC]
tags: [scATAC-seq, imputation, denoising, dropout, benchmarking]
created: 2026-06-02
updated: 2026-06-02
---

# scATAC-seq imputation and denoising

> Computational recovery of missing open-chromatin signal in scATAC-seq, whose count matrices are extremely sparse (~3–7% non-zero) because each diploid peak has at most two capturable Tn5 cut sites, most lost during library preparation ([[10-Summaries/li-2021-scopen]]).

## Definition

Imputation/denoising methods estimate the true accessibility status of each region in each cell from the observed sparse matrix, mitigating dropout before downstream clustering, visualization, motif analysis, and *cis*-regulatory prediction ([[10-Summaries/li-2021-scopen]]). Assuming only ~25% of accessible DNA is sequenced, ~56% of accessible sites get zero cut sites under a binomial model — the dropout problem these methods address ([[10-Summaries/li-2021-scopen]]).

## Why it matters

- Sparsity is worse than scRNA-seq and confounds distance metrics, making clustering and co-accessibility unreliable on raw matrices ([[10-Summaries/xiong-2019-scale]]).
- Imputation strongly improves correlation-based *cis*-regulatory prediction (Cicero) because dropouts at two regions are independent — the same logic as MAGIC for scRNA-seq gene–gene interactions ([[10-Summaries/li-2021-scopen]]).
- Despite this, imputation was historically "widely ignored" in standard pipelines like Signac and ArchR ([[10-Summaries/li-2021-scopen]]).

## Variants and refinements

- **scOpen** — regularized NMF on TF-IDF binary matrix; lowest memory, highest AUPR in its benchmark ([[10-Summaries/li-2021-scopen]]). See [[30-Concepts/scopen]].
- **SCALE** — VAE + Gaussian Mixture Model; deep-learning, interpretable latent features, GPU-bound ([[10-Summaries/xiong-2019-scale]]). See [[30-Concepts/scale]].
- **cisTopic-impute** — multiply topic-cell × region-topic LDA distributions for a predictive matrix; runtime scales poorly with reads ([[10-Summaries/bravo-2019-cistopic]]). See [[30-Concepts/cistopic]].
- **Repurposed scRNA-seq imputers** — MAGIC, SAVER, scImpute, DCA, scBFA; generally underfit scATAC sparsity and can introduce false signals ([[10-Summaries/xiong-2019-scale]], [[10-Summaries/li-2021-scopen]]).

## Contested points

- Whether imputation helps or misleads: imputation can induce false signals, and the field lacks a definitive rule for when recovery is trustworthy vs hallucinated ([[10-Summaries/li-2021-scopen]]).
- scOpen reports beating SCALE; SCALE's strengths are interpretability and batch-effect detection rather than raw AUPR ([[10-Summaries/li-2021-scopen]], [[10-Summaries/xiong-2019-scale]]).

## Related

- [[30-Concepts/scopen]] · [[30-Concepts/scale]] · [[30-Concepts/cistopic]] · [[30-Concepts/snapatac]] · [[30-Concepts/scatac-seq]] · [[30-Concepts/chromatin-accessibility]] · [[30-Concepts/allele-dropout]]
- [[40-Topics/single-cell-atac-seq]]
