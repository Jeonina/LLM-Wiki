---
type: concept
title: Multimodal integration methods
aliases: [multi-omics integration, multimodal integration, cross-modality integration]
tags: [computational, integration, multiomics, machine-learning]
created: 2026-05-19
updated: 2026-05-19
---

# Multimodal integration methods

> Computational methods for combining multiple single-cell omics modalities — paired (measured on the same cells) or unpaired (separate cell populations) — into a unified low-dimensional representation. Three families: matrix factorization, manifold alignment, and deep generative models ([[10-Summaries/wang-2023-multimodal-review]]).

## Method families

- **Matrix factorization** — MOFA / MOFA+ ([[10-Summaries/argelaguet-2020-mofa-plus]]), LIGER. Extract latent factors per modality; struggle at high dimensionality.
- **Manifold alignment / anchoring** — CCA, MNN, WNN (all in Seurat per [[10-Summaries/stuart-2021-natmethods]]), Tangram, Cell2location.
- **Deep generative models** — totalVI, sciPENN, scMVP, MultiVI ([[10-Summaries/ashuach-2023-multivi]]), Cobolt ([[10-Summaries/gong-2021-cobolt]]), scJoint, GLUE ([[10-Summaries/cao-2022-glue]]), Symphony.

## Paired vs unpaired

- **Paired**: cells measured by both modalities; problem is *alignment* of within-cell features.
- **Unpaired**: separate cell populations, possibly different protocols; problem is *finding common cells* across datasets ([[10-Summaries/wang-2023-multimodal-review]]).

## Related

- [[40-Topics/single-cell-multiomics]] · [[30-Concepts/joint-single-cell-multi-omics]]
