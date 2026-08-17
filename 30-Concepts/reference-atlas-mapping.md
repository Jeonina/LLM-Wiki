---
type: concept
title: Reference atlas mapping
aliases: [reference mapping, label transfer, query mapping, cross-modality prediction, atlas mapping]
tags: [integration, atlas, label-transfer, annotation, Human-Cell-Atlas]
created: 2026-08-14
updated: 2026-08-14
---

# Reference atlas mapping

> Placing new ("query") cells into an existing annotated reference embedding, and transferring annotations — or even **unmeasured modalities** — from the reference to the query.

## Why it is a distinct operation from integration

Integration builds a shared space from datasets treated symmetrically. Reference mapping is asymmetric: the reference is **frozen** and the query is placed into it ([[10-Summaries/kang-2021-symphony]]). The distinction is not cosmetic. Re-integrating reference and query de novo is intractable at atlas scale, requires shipping raw reference data, and — most importantly — **corrupts an embedding that was painstakingly constructed and annotated** ([[10-Summaries/kang-2021-symphony]]). A moving reference also means two labs mapping the same query get different answers. (synthesis)

The operation is explicitly analogous to read alignment: an expensive, rare reference-building step, then a cheap, constant-time mapping step ([[10-Summaries/kang-2021-symphony]]).

## Three strategies

| Strategy | Mechanism | Example |
|---|---|---|
| Compressed frozen embedding | Store an integrated reference in portable form; localise query cells within it in seconds | [[10-Summaries/kang-2021-symphony]] (built on [[10-Summaries/korsunsky-2019-harmony]]) |
| Anchor-based | Find corresponding cells across reference and query, then transfer | [[10-Summaries/butler-2018-seurat-cca]] → [[10-Summaries/hao-2021-seurat-wnn]] → [[10-Summaries/hao-2024-seurat-v5]] |
| Learned classifier over cell graphs | Train a graph convolutional network to transfer labels, capturing higher-order cell relations | [[10-Summaries/song-2021-scgcn]] |

Embedding-first (Symphony) and classifier-first (scGCN) are the two poles: the first makes annotation a downstream, revisable step; the second bakes the annotation into the model. (synthesis)

## Predicting a modality you never measured

The most consequential extension: if the reference measured something the query did not, mapping can supply it. Four instances in this corpus, attacking it from different directions:

- **RNA → surface protein** by reference mapping ([[10-Summaries/kang-2021-symphony]]) or by deep learning with uncertainty ([[10-Summaries/lakkis-2022-scipenn]]).
- **RNA → spatial position** by alignment ([[10-Summaries/biancalani-2021-tangram]]) or deconvolution ([[10-Summaries/kleshchevnikov-2022-cell2location]]).
- **RNA → spatial chromatin accessibility**, either propagated through a paired assay ([[10-Summaries/biancalani-2021-tangram]] on SHARE-seq data) or learned from a joint embedding ([[10-Summaries/debnath-2026-ison]]).

The shared premise is that a reference substitutes for an experiment. The shared risk is that the prediction reproduces the reference's structure rather than the query's biology — and only [[10-Summaries/lakkis-2022-scipenn|sciPENN]] returns an uncertainty estimate, so in every other case an imputed value is indistinguishable from a measured one in the output matrix. (synthesis)

## The shared structural limitation

Every reference-based method inherits the same failure: **a state absent from the reference has nowhere correct to go**. Landmark-projection approaches place novel cell types arbitrarily ([[10-Summaries/haghverdi-2018-mnn]]); frozen embeddings cannot represent them ([[10-Summaries/kang-2021-symphony]]); deconvolution silently redistributes them among known types ([[10-Summaries/kleshchevnikov-2022-cell2location]]); label transfer assigns a wrong label with full confidence ([[10-Summaries/song-2021-scgcn]]). (synthesis)

A second, quieter risk: transferred annotations inherit every bias and error of the source annotation, propagating silently at scale — a risk none of these papers quantifies. (synthesis)

## Related

- [[multimodal-integration-methods]] · [[batch-effect]] · [[cell-type-annotation]] · [[spatial-multiomics]] · [[imputation]] · [[40-Topics/computational-methods]]
