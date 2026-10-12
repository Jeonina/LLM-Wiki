---
type: concept
title: Reference atlas mapping
aliases: [reference mapping, label transfer, query mapping, cross-modality prediction, atlas mapping]
tags: [integration, atlas, label-transfer, annotation, Human-Cell-Atlas]
created: 2026-08-14
updated: 2026-10-12
---

# Reference atlas mapping

> Placing new ("query") cells into an existing annotated reference embedding, and transferring annotations — or even **unmeasured modalities** — from the reference to the query ([[10-Summaries/kang-2021-symphony|Symphony]]).

> [!abstract] 한눈에
> Reference atlas mapping은 이미 annotation된 reference를 고정해 두고 새 query 세포를 그 안에 놓아 label이나 측정하지 않은 modality를 옮겨 오는 작업이다 ([[10-Summaries/kang-2021-symphony|Symphony]]). reference에 없는 세포 상태는 올바르게 놓일 자리가 없다는 한계를 모든 방법이 공유한다 ([[10-Summaries/haghverdi-2018-mnn|MNN]]; [[10-Summaries/song-2021-scgcn|scGCN]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [분석 도구 교재](../60-Explainers/computational-methods.html)
<!-- /explainer-links -->

## Definition

Integration builds a shared space from datasets treated symmetrically. Reference mapping is asymmetric: the reference is **frozen** and the query is placed into it ([[10-Summaries/kang-2021-symphony|Symphony]]). The operation is explicitly analogous to read alignment: an expensive, rare reference-building step, then a cheap, constant-time mapping step ([[10-Summaries/kang-2021-symphony|Symphony]]).

## Why it matters

The distinction from integration is not cosmetic. Re-integrating reference and query de novo is intractable at atlas scale, requires shipping raw reference data, and — most importantly — **corrupts an embedding that was painstakingly constructed and annotated** ([[10-Summaries/kang-2021-symphony|Symphony]]). A moving reference also means two labs mapping the same query get different answers (synthesis).

## Three strategies

| Strategy | Mechanism | Example |
|---|---|---|
| Compressed frozen embedding | Store an integrated reference in portable form; localise query cells within it in seconds | [[10-Summaries/kang-2021-symphony\|Symphony]] (built on [[10-Summaries/korsunsky-2019-harmony\|Harmony]]) |
| Anchor-based | Find corresponding cells across reference and query, then transfer | [[10-Summaries/butler-2018-seurat-cca\|Butler 2018]] → [[10-Summaries/hao-2021-seurat-wnn\|Hao 2021]] → [[10-Summaries/hao-2024-seurat-v5\|Hao 2024]] |
| Learned classifier over cell graphs | Train a graph convolutional network to transfer labels, capturing higher-order cell relations | [[10-Summaries/song-2021-scgcn\|scGCN]] |

Embedding-first (Symphony) and classifier-first (scGCN) are the two poles: the first makes annotation a downstream, revisable step; the second bakes the annotation into the model (synthesis).

## Predicting a modality you never measured

The most consequential extension: if the reference measured something the query did not, mapping can supply it. Four instances in this corpus, attacking it from different directions:

| Prediction | Route | Source |
|---|---|---|
| RNA → surface protein | Reference mapping | ([[10-Summaries/kang-2021-symphony\|Symphony]]) |
| RNA → surface protein | Deep learning with uncertainty | ([[10-Summaries/lakkis-2022-scipenn\|sciPENN]]) |
| RNA → spatial position | Alignment | ([[10-Summaries/biancalani-2021-tangram\|Tangram]]) |
| RNA → spatial position | Deconvolution | ([[10-Summaries/kleshchevnikov-2022-cell2location\|cell2location]]) |
| RNA → spatial chromatin accessibility | Propagated through a paired assay (Tangram on SHARE-seq data) | ([[10-Summaries/biancalani-2021-tangram\|Tangram]]) |
| RNA → spatial chromatin accessibility | Learned from a joint embedding | ([[10-Summaries/debnath-2026-ison\|ISON]]) |

The shared premise is that a reference substitutes for an experiment (synthesis).

## Evidence and examples

- Symphony localises query cells within a compressed reference in seconds ([[10-Summaries/kang-2021-symphony|Symphony]]).
- Only sciPENN is reported to return a well-calibrated uncertainty estimate; Seurat 4 provides none, and totalVI's prediction intervals are badly under-covered ([[10-Summaries/lakkis-2022-scipenn|sciPENN]]).

## Contested points

- **A state absent from the reference has nowhere correct to go.** Every reference-based method inherits this failure (synthesis): landmark-projection approaches place novel cell types arbitrarily ([[10-Summaries/haghverdi-2018-mnn|MNN]]); frozen embeddings cannot represent them ([[10-Summaries/kang-2021-symphony|Symphony]]); deconvolution silently redistributes them among known types ([[10-Summaries/kleshchevnikov-2022-cell2location|cell2location]]); label transfer assigns a wrong label with full confidence ([[10-Summaries/song-2021-scgcn|scGCN]]).
- **Predictions may reproduce the reference rather than the query.** The shared risk of modality prediction is that the output reproduces the reference's structure rather than the query's biology; without calibrated uncertainty ([[10-Summaries/lakkis-2022-scipenn|sciPENN]]), an imputed value is easily mistaken for a measured one in the output matrix (synthesis).
- **Annotation errors propagate.** Transferred annotations inherit every bias and error of the source annotation, propagating silently at scale — a risk none of these papers quantifies (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/multimodal-integration-methods|Multimodal integration methods]] — Combining several single-cell modalities into one representation.
> - `concept` [[30-Concepts/batch-effect|Batch effect]] — Systematic variation from when, where or how data were generated.
> - `concept` [[30-Concepts/cell-type-annotation|Cell-type annotation]] — Assigning biological identity to clusters.
> - `concept` [[30-Concepts/spatial-multiomics|Spatial multiomics]] — Single-cell multi-omics that preserve spatial position in tissue.
> - `concept` [[30-Concepts/imputation|Imputation]] — Filling in values a sparse assay did not observe.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — The tool layer: aligners, formats, callers, imputers and integrators.

## All sources on this page

> [!info]- 11 summaries cited here
> - [[10-Summaries/biancalani-2021-tangram|Biancalani 2021]]
> - [[10-Summaries/butler-2018-seurat-cca|Butler 2018]]
> - [[10-Summaries/debnath-2026-ison|Debnath 2026]]
> - [[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]
> - [[10-Summaries/hao-2021-seurat-wnn|Hao 2021]]
> - [[10-Summaries/hao-2024-seurat-v5|Hao 2024]]
> - [[10-Summaries/kang-2021-symphony|Kang 2021]]
> - [[10-Summaries/kleshchevnikov-2022-cell2location|Kleshchevnikov 2022]]
> - [[10-Summaries/korsunsky-2019-harmony|Korsunsky 2019]]
> - [[10-Summaries/lakkis-2022-scipenn|Lakkis 2022]]
> - [[10-Summaries/song-2021-scgcn|Song 2021]]
