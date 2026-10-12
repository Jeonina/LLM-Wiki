---
type: concept
title: Latent Dirichlet Allocation
aliases: [LDA]
tags: [topic-modeling, Bayesian, machine-learning]
created: 2026-05-12
updated: 2026-10-12
---

# Latent Dirichlet Allocation (LDA)

> A generative probabilistic topic model originally developed for natural language processing (Blei, Ng, Jordan 2003). Treats documents as distributions over topics and topics as distributions over words. Adapted to single-cell epigenomics where "documents" are cells and "words" are accessible regions or chromatin features.

> [!abstract] 한눈에
> LDA는 문서를 topic의 분포로, topic을 단어의 분포로 보는 생성형 topic model이며, single-cell epigenomics에서는 세포를 문서로, accessible region을 단어로 바꿔 쓴다. cisTopic과 scChIX-seq가 이를 쓰고, embedded topic model은 deep encoder를 붙이면서도 해석 가능한 linear decoder를 유지한다 ([[10-Summaries/fan-2026-gfetm|GFETM]]).

## Definition

Two Dirichlet priors: α for topic-document distribution, β for word-topic distribution. Collapsed Gibbs sampling iteratively reassigns each word to a topic conditional on the rest, converging on stable topic and document distributions.

## Why it matters

- Naturally handles sparsity by aggregating signal into topics.
- Discovers regulatory programs without prior annotation.
- Used in [[30-Concepts/cistopic]] (cis-regulatory topics from scATAC) and [[30-Concepts/scchix-seq]] (chromatin-mark topics for deconvolution).
- Embedded topic models extend the LDA/cisTopic line to scATAC with deep encoders while keeping interpretable linear decoders; GFETM additionally embeds peak DNA with a genome foundation model ([[10-Summaries/fan-2026-gfetm|GFETM]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/cistopic|cisTopic]] — LDA with collapsed Gibbs sampling applied to scATAC-seq.
> - `concept` [[30-Concepts/scchix-seq|scChIX-seq]] — Two-mark sortChIC whose superimposed profiles are deconvolved with topics.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Chromatin accessibility measured one cell at a time.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/fan-2026-gfetm|Fan 2026]]
