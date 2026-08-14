---
type: concept
title: Imputation
aliases: [data smoothing, missing-value imputation, contact map imputation]
tags: [sparsity, single-cell, smoothing, scHi-C, denoising]
created: 2026-08-10
updated: 2026-08-10
---

# Imputation

> Filling in values that a sparse assay did not observe, so that per-cell structure becomes analysable. Necessary in single-cell Hi-C in particular, because sparsity compounds in two dimensions — 5–10% linear genome coverage becomes **0.25–1% of possible contacts** ([[zhou-2019-schicluster]]).

## Approaches

**Convolution plus random walk.** Replace each matrix element by a weighted average of its neighbourhood (sharing information along the linear genome), then apply random walk with restart (sharing among network neighbours), then keep only the **top 20% of imputed interactions** to strip coverage bias ([[zhou-2019-schicluster]]). All three steps are required; every one- and two-step combination underperforms ([[zhou-2019-schicluster]]). The approach requires dense matrices in memory, limiting resolution ([[zhang-2022-higashi]]).

**Hypergraph representation learning.** Model the whole dataset as one hypergraph — cells and genomic bins as nodes, each non-zero contact as a hyperedge — so imputation becomes hyperedge prediction and can **borrow from a cell's neighbours in embedding space** ([[zhang-2022-higashi]]). Sparse-native, and 30–43% better median similarity than random-walk imputation at the lowest coverage against imaging-derived ground truth ([[zhang-2022-higashi]]).

## What imputation buys

- Cell-type clustering that raw contact matrices cannot support ([[zhou-2019-schicluster]]).
- Per-cell A/B compartment scores and TAD-like domain boundaries, including boundaries that are **present/absent** across cells and boundaries that **slide** along the genome ([[zhang-2022-higashi]]).
- Cell-type-specific structure that is obscured in pooled maps — a boundary near *THBS2* visible per cell and invisible in the population contact map ([[zhang-2022-higashi]]).

## The standing concern

Smoothing that makes cells clusterable necessarily reduces apparent cell-to-cell variability, and the trade is not quantified in either framework ([[zhou-2019-schicluster]], [[zhang-2022-higashi]]). Borrowing across neighbours risks circularity — cells are imputed toward their neighbours, so measured variability is partly a function of the imputation ([[zhang-2022-higashi]]). Validation against orthogonal imaging data is what keeps the claims credible ([[zhang-2022-higashi]]).

Practical floor: clustering performance degrades below **25,000 contacts** per cell and collapses at 5,000 ([[zhou-2019-schicluster]]) — which is below what combinatorial-indexing scHi-C delivers ([[ramani-2017-scihi-c]]).

## Related

- [[single-cell-hi-c]] · [[scatac-imputation]] · [[dimensionality-reduction]] · [[computational-methods]]

## Added 2026-08-13

Random walk with restart, introduced for scHi-C clustering by [[10-Summaries/zhou-2019-schicluster|scHiCluster]], is reused for a different downstream task in [[10-Summaries/yu-2021-snaphic|SnapHiC]]: per-cell RWR (restart probability 0.05) on a binary 10-kb contact graph, followed by distance-stratified *z*-score normalisation, as the front end of loop calling ([[10-Summaries/yu-2021-snaphic]]).

[[10-Summaries/xiong-2024-scghost|scGHOST]] instead consumes [[10-Summaries/zhang-2022-higashi|Higashi]]-imputed maps and layers graph embedding on top — inheriting whatever Higashi gets wrong ([[10-Summaries/xiong-2024-scghost]]). (synthesis)

A sharper claim about imputation appears outside 3D genomics: ISON's *inferred* spatial chromatin accessibility recovers *cis*-eQTL and Hi-C-supported regulatory links **better than the directly measured** spatial ATAC, because the measurement is so dropout-ridden ([[10-Summaries/debnath-2026-ison]]). The caveat is circularity — the strong correlation numbers use MAGIC-imputed data as ground truth ([[10-Summaries/debnath-2026-ison]]). (synthesis)
