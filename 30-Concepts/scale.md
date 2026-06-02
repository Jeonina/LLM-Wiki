---
type: concept
title: SCALE (scATAC-seq analysis)
aliases: [SCALE, Single-Cell ATAC-seq analysis via Latent feature Extraction]
tags: [scATAC-seq, deep-learning, VAE, gaussian-mixture-model, imputation]
created: 2026-06-02
updated: 2026-06-02
---

# SCALE (scATAC-seq analysis via Latent feature Extraction)

> A deep generative method that models sparse scATAC-seq data by combining a **variational autoencoder (VAE)** with a **Gaussian Mixture Model (GMM)** prior over the latent space, supporting visualization, clustering, and denoising/imputation from interpretable latent features ([[10-Summaries/xiong-2019-scale]]).

## Definition

SCALE encodes each cell into a 10-dimensional latent variable on a GMM manifold (encoder 3200-1600-800-400; single-layer Bernoulli decoder), trained by maximizing the evidence lower bound = reconstruction term + KL divergence to the GMM ([[10-Summaries/xiong-2019-scale]]). The GMM prior gives a tighter posterior than a single-Gaussian VAE (e.g. scVI), which underfits sparse near-binary data ([[10-Summaries/xiong-2019-scale]]).

## Why it matters

- Demonstrated that scRNA-seq imputers (MAGIC, scVI) actively harm scATAC-seq analysis by making misclassified cells *less* similar to their true types — motivating ATAC-specific tooling ([[10-Summaries/xiong-2019-scale]]).
- The GMM yields disentangled latent dimensions that map onto biological cell types *and* can flag technical batch effects (plate-specific features), which can then be excluded from embedding ([[10-Summaries/xiong-2019-scale]]).

## How it compares

- Best overall clustering (ARI/NMI/F1) across six mixture datasets vs scABC, SC3, scVI, cisTopic, TF-IDF, Cicero ([[10-Summaries/xiong-2019-scale]]).
- A leading deep-learning entry in scATAC imputation; later benchmarked by scOpen, which reports higher AUPR and lower memory ([[10-Summaries/li-2021-scopen]]). See [[30-Concepts/scatac-imputation]].

## Examples

- Separated Epcam+ tumor from CD45+ immune cells in Pi-ATAC breast-tumor data from chromatin alone, comparable to the protein-indexed experimental method ([[10-Summaries/xiong-2019-scale]]).
- Imputation raised chromVAR significant motifs from 52 to 105 in forebrain data, recovering Mafb/Hoxd9 and MGE-pathway TFs ([[10-Summaries/xiong-2019-scale]]).

## Related

- [[30-Concepts/scatac-imputation]] · [[30-Concepts/scopen]] · [[30-Concepts/cistopic]] · [[30-Concepts/scatac-seq]] · [[30-Concepts/chromvar]]
- [[40-Topics/single-cell-atac-seq]] · [[20-Entities/qiangfeng-cliff-zhang]]
