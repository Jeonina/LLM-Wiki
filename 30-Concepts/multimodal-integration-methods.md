---
type: concept
title: Multimodal integration methods
aliases: [multi-omics integration, multimodal integration, cross-modality integration]
tags: [computational, integration, multiomics, machine-learning]
created: 2026-05-19
updated: 2026-08-10
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

## The anchor taxonomy

- **The anchor determines the assumptions.** *Horizontal* integration anchors on features (batch correction); *vertical* on cells (matched multimodal); *diagonal* when no anchor exists in high-dimensional space; *mosaic* when different modalities are measured on different cells from the same sample, leaving entire matrices missing ([[10-Summaries/argelaguet-2021-integration-principles]]).
- **Named failure modes**: overcorrection (merging non-matching subpopulations when no shared biological axis exists); latent-space integration distorting the high-dimensional observations so marker detection becomes problematic; and biological variability that tracks batch being inseparable from it ([[10-Summaries/argelaguet-2021-integration-principles]]).
- **Sequence context is a systematic confounder** in epigenomic association: GC content raises apparent accessibility and lowers apparent methylation, so nulls should be built from features with matched sequence context, as chromVAR does ([[10-Summaries/argelaguet-2021-integration-principles]]).
- **Feature-count imbalance** lets the modality with more features dominate a joint latent space — the problem WNN reweighting exists to solve ([[10-Summaries/argelaguet-2021-integration-principles]]).
- **Diagonal integration usually rests on the gene-activity assumption**, which is known to fail in early development where gene-body methylation and accessibility do not predict expression ([[10-Summaries/argelaguet-2021-integration-principles]]).
- **Bridge integration removes that assumption** by treating each cell of a multiomic dataset as a dictionary atom, learning the cross-modality relationship instead of assuming it; ~50 bridge cells per cell type suffice, and prediction confidence drops sharply (0.907 → 0.514) when a cell type is missing from the bridge ([[10-Summaries/hao-2024-seurat-v5]]).

## Related

- [[40-Topics/single-cell-multiomics]] · [[30-Concepts/joint-single-cell-multi-omics]]
- [[10-Summaries/argelaguet-2021-integration-principles]] · [[10-Summaries/hao-2024-seurat-v5]] · [[10-Summaries/lake-2018-brain-snrna-scths]]
