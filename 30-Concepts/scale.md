---
type: concept
title: SCALE (scATAC-seq analysis)
aliases: [SCALE, Single-Cell ATAC-seq analysis via Latent feature Extraction]
tags: [scATAC-seq, deep-learning, VAE, gaussian-mixture-model, imputation]
created: 2026-06-02
updated: 2026-10-07
---

# SCALE (scATAC-seq analysis via Latent feature Extraction)

> A deep generative method that models sparse scATAC-seq data by combining a **variational autoencoder (VAE)** with a **Gaussian Mixture Model (GMM)** prior over the latent space, supporting visualization, clustering, and denoising/imputation from interpretable latent features ([[10-Summaries/xiong-2019-scale]]).

## Definition

SCALE encodes each cell into a 10-dimensional latent variable on a GMM manifold (encoder 3200-1600-800-400; single-layer Bernoulli decoder), trained by maximizing the evidence lower bound = reconstruction term + KL divergence to the GMM ([[10-Summaries/xiong-2019-scale]]). The GMM prior gives a tighter posterior than a single-Gaussian VAE (e.g. scVI), which underfits sparse near-binary data ([[10-Summaries/xiong-2019-scale]]).

## Why it matters

- Demonstrated that scRNA-seq imputers (scVI) actively harm scATAC-seq analysis by making misclassified cells *less* similar to their true types — motivating ATAC-specific tooling ([[10-Summaries/xiong-2019-scale]]).
- The GMM yields disentangled latent dimensions that map onto biological cell types *and* can flag technical batch effects (plate-specific features), which can then be excluded from embedding ([[10-Summaries/xiong-2019-scale]]).

## How it compares

- Best overall clustering (ARI/NMI/F1) across six mixture datasets vs scABC, SC3, scVI, cisTopic (TF-IDF and Cicero compared only for visualization) ([[10-Summaries/xiong-2019-scale]]).
- A leading deep-learning entry in scATAC imputation; later benchmarked by scOpen, which reports higher AUPR and lower memory ([[10-Summaries/li-2021-scopen]]). See [[30-Concepts/scatac-imputation]].

## Examples

- Separated Epcam+ tumor from CD45+ immune cells in Pi-ATAC breast-tumor data from chromatin alone, comparable to the protein-indexed experimental method ([[10-Summaries/xiong-2019-scale]]).
- Imputation raised chromVAR significant motifs from 52 to 105 in forebrain data, recovering Mafb/Hoxd9 and MGE-pathway TFs ([[10-Summaries/xiong-2019-scale]]).

## Added 2026-10-07

PeakVI found SCALE especially sensitive to library-size effects and weaker than PeakVI at separating sorted cell types, though good at mixing batches ([[10-Summaries/ashuach-2022-peakvi]]); EpiAgent also benchmarks above SCALE on clustering metrics ([[10-Summaries/chen-2025-epiagent]]).

SCALE was used as a baseline in the scCASE benchmark, where it was outperformed on clustering metrics. As a GPU-based method it uses less CPU memory than CPU tools ([[10-Summaries/tang-2024-sccase]]).

On single-cell histone PTM datasets (<12,000 cells), SCALE was not competitive with LSI-based methods; it gained 21% from coverage-based cell filtering, and the authors conjecture that VAE methods could catch up at larger cell numbers ([[10-Summaries/raimundo-2023-schptm-benchmark]]).


## Related

- [[30-Concepts/scatac-imputation]] · [[30-Concepts/scopen]] · [[30-Concepts/cistopic]] · [[30-Concepts/scatac-seq]] · [[30-Concepts/chromvar]]
- [[40-Topics/single-cell-atac-seq]] · [[20-Entities/qiangfeng-cliff-zhang]]
