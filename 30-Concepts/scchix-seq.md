---
type: concept
title: scChIX-seq
aliases: [single-cell ChIC and unmixing]
tags: [histone-modifications, single-cell, multi-modal, deconvolution, LDA]
created: 2026-05-12
updated: 2026-10-12
---

# scChIX-seq

> Multiplexes two histone-mark antibodies in the same cell during sortChIC, then computationally **deconvolves the superimposed cut-site profiles** using single-incubated reference datasets and LDA topic modeling ([[10-Summaries/yeung-2023-scchix-seq|Yeung 2023]]).

> [!abstract] 한눈에
> scChIX-seq는 sortChIC에서 두 histone mark antibody를 한 세포에 함께 쓰고, 단일 antibody reference와 LDA topic model로 겹친 신호를 mark별로 풀어내는 방법이다 ([[10-Summaries/yeung-2023-scchix-seq|Yeung 2023]]). 덕분에 한 세포 안에서 mark 사이의 배타성·공존·전환과 chromatin velocity를 볼 수 있다 ([[10-Summaries/yeung-2023-scchix-seq|Yeung 2023]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 히스톤 변형](../60-Explainers/histone-modifications.html)
<!-- /explainer-links -->

## Definition

Three datasets per experiment: single-incubated dataset A (mark 1 only), single-incubated dataset B (mark 2 only), double-incubated dataset C (both marks). LDA learns topic models on A and B; for each cell in C, select the most-likely (topic-A, topic-B) pair and probabilistically assign each fragment to mark 1 or mark 2.

## Why it matters

- Per-cell relationships between marks (mutually exclusive, co-occurring, transitions) are visible from a single cell. Bulk averages obscure cell-type-specific transitions.
- Enables "chromatin velocity" — coordinated mark dynamics through differentiation trajectories.

## Examples

- H3K27me3 + H3K9me3 in mouse BM (B cells, granulocytes, NK cells): FDR 10/3/1% respectively, recovers mutual exclusivity ([[10-Summaries/yeung-2023-scchix-seq|Yeung 2023]]).
- H3K4me1 + H3K27me3 in BM: resolves pro-B → B-cell transition via *IgK* chromatin opening ([[10-Summaries/yeung-2023-scchix-seq|Yeung 2023]]).
- Macrophage differentiation: H3K4me1 + H3K36me3 chromatin velocity ([[10-Summaries/yeung-2023-scchix-seq|Yeung 2023]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/sortchic|sortChIC]] — pA-MNase plus FACS sorting into 384-well plates; the platform scChIX-seq builds on.
> - `concept` [[30-Concepts/latent-dirichlet-allocation|Latent Dirichlet allocation]] — Generative topic model adapted to single-cell epigenomics.
> - `concept` [[30-Concepts/chromatin-velocity|Chromatin velocity]] — Coordinated chromatin-mark dynamics along a differentiation trajectory.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone-tail marks that demarcate chromatin states.
> - `entity` [[20-Entities/alexander-van-oudenaarden|Alexander van Oudenaarden]] — Hubrecht Institute; developer of sortChIC and scChIX-seq.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/yeung-2023-scchix-seq|Yeung 2023]]
