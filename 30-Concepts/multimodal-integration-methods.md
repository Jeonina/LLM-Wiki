---
type: concept
title: Multimodal integration methods
aliases: [multi-omics integration, multimodal integration, cross-modality integration]
tags: [computational, integration, multiomics, machine-learning]
created: 2026-05-19
updated: 2026-05-27
---

# Multimodal integration methods

> Computational methods for combining multiple single-cell omics modalities — paired (measured on the same cells) or unpaired (separate cell populations) — into a unified low-dimensional representation. Three method families ([[10-Summaries/wang-2023-multimodal-review]]): matrix factorization, manifold alignment, and deep generative models. Three integration *topologies* per the Argelaguet taxonomy ([[10-Summaries/bi-2024-multiomics-review]]): horizontal (same modality, different cells, anchored on genomic features), vertical (different modalities, same cell, anchored on the cell), and diagonal (different modalities, different cells, no anchor).

## Method families

- **Matrix factorization** — MOFA / MOFA+ ([[10-Summaries/argelaguet-2020-mofa-plus]]), LIGER. Extract latent factors per modality; struggle at high dimensionality.
- **Manifold alignment / anchoring** — CCA, MNN, WNN (all in Seurat per [[10-Summaries/stuart-2021-natmethods]]), Tangram, Cell2location.
- **Deep generative models** — totalVI, sciPENN, scMVP, MultiVI ([[10-Summaries/ashuach-2023-multivi]]), Cobolt ([[10-Summaries/gong-2021-cobolt]]), scJoint, GLUE ([[10-Summaries/cao-2022-glue]]), Symphony.

## Paired vs unpaired (= vertical vs horizontal/diagonal)

- **Paired / vertical**: cells measured by both modalities; problem is *alignment* of within-cell features ([[10-Summaries/bi-2024-multiomics-review]]).
- **Unpaired / horizontal**: same modality across cell populations, anchored on shared genomic features ([[10-Summaries/bi-2024-multiomics-review]]; [[10-Summaries/wang-2023-multimodal-review]]).
- **Unpaired / diagonal**: different modalities and different cells, no anchor — the hardest case because batch correction risks erasing biology ([[10-Summaries/bi-2024-multiomics-review]]).

## Related

- [[40-Topics/single-cell-multiomics]] · [[30-Concepts/joint-single-cell-multi-omics]]
