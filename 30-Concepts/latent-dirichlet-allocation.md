---
type: concept
title: Latent Dirichlet Allocation
aliases: [LDA]
tags: [topic-modeling, Bayesian, machine-learning]
created: 2026-05-12
updated: 2026-05-12
---

# Latent Dirichlet Allocation (LDA)

> A generative probabilistic topic model originally developed for natural language processing (Blei, Ng, Jordan 2003). Treats documents as distributions over topics and topics as distributions over words. Adapted to single-cell epigenomics where "documents" are cells and "words" are accessible regions or chromatin features.

## Definition

Two Dirichlet priors: α for topic-document distribution, β for word-topic distribution. Collapsed Gibbs sampling iteratively reassigns each word to a topic conditional on the rest, converging on stable topic and document distributions.

## Why it matters

- Naturally handles sparsity by aggregating signal into topics.
- Discovers regulatory programs without prior annotation.
- Used in [[30-Concepts/cistopic]] (cis-regulatory topics from scATAC) and [[30-Concepts/scchix-seq]] (chromatin-mark topics for deconvolution).

## Related

- [[30-Concepts/cistopic]] · [[30-Concepts/scchix-seq]] · [[40-Topics/single-cell-atac-seq]]
