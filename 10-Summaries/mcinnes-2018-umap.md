---
type: summary
title: "McInnes, Healy & Melville 2018 — UMAP: Uniform Manifold Approximation and Projection"
source: "[[00-Sources/papers/UMAP_ Uniform Manifold Approximation and Projection for Dimension Reduction]]"
source_kind: paper
author: "Leland McInnes, John Healy, James Melville"
published: 2018-02-09
ingested: 2026-08-10
doi: "10.48550/arXiv.1802.03426"
journal: "arXiv preprint (stat.ML) — never formally journal-published"
tags: [UMAP, dimensionality-reduction, visualization, manifold-learning, computational-tool, preprint]
entities: []
concepts: ["[[scanpy]]", "[[episcanpy]]"]
topics: ["[[single-cell-multiomics]]"]
---

**Citation:** McInnes, Healy & Melville (2018) — *UMAP: Uniform Manifold Approximation and Projection for dimension reduction* — arXiv:1802.03426. [DOI](https://doi.org/10.48550/arXiv.1802.03426)

# McInnes 2018 — UMAP

> A manifold-learning dimension-reduction method derived from Riemannian geometry and algebraic topology (fuzzy simplicial set approximation of the data manifold, then cross-entropy optimization of a low-dimensional analogue), competitive with t-SNE on visualization quality while preserving more global structure, running faster, and — unlike t-SNE — imposing no ceiling on embedding dimension.

> ⚠️ **Source caveat.** The bookmarked clipping is the arXiv abstract page. Claims below are from the abstract; the mathematical construction is not in the clipping.

## Key claims

- UMAP is built from a stated theoretical framework (Riemannian geometry + algebraic topology) rather than assembled heuristically — the authors' framing of what distinguishes it from t-SNE.
- Visualization quality is competitive with t-SNE; **global** structure preservation is argued to be better.
- Runtime is superior, and the algorithm scales to real-world data sizes.
- No computational restriction on output dimension, making it usable as a general-purpose reduction step feeding downstream ML, not only as a 2D picture.

## Methods / evidence

The abstract asserts these properties; the arXiv paper supplies the derivation and benchmarks. Notably this work was **never published in a peer-reviewed journal** — it is cited by essentially every single-cell paper in this wiki as a preprint. That is worth stating plainly in a methods chronology.

## Surprising or load-bearing bits

- UMAP is the default embedding in [[scanpy]], [[episcanpy]], Seurat, [[granja-2021-archr|ArchR]], [[zhang-2024-snapatac2|SnapATAC2]] and [[stuart-2021-natmethods|Signac]] — i.e. nearly every analysis path in this corpus terminates in a UMAP, which makes it a shared and rarely-examined dependency.
- The "preserves global structure" claim is the contested one: for single-cell epigenomics, inter-cluster distances on a UMAP are routinely over-read. The corpus's clustering discipline comes instead from [[traag-2019-leiden|Leiden]], which operates on the graph, not the embedding.
- Version history matters: v1 (2018) → v3 (2020). Tools pin different UMAP releases, so embeddings are not reproducible across pipeline versions.

## Concepts touched

- Underpins the visualization step in [[scatac-seq]], [[scbs-seq]] and [[single-cell-hi-c]] workflows alike — it is modality-agnostic, which is exactly why it needs a page-level caveat about over-interpretation.
- Pairs with [[traag-2019-leiden]]: UMAP for display, Leiden for the actual partition.

## Connections to other sources

- Consumed by [[granja-2021-archr]], [[zhang-2024-snapatac2]], [[stuart-2021-natmethods]], [[hao-2024-seurat-v5]], [[danese-2021-episcanpy]].
- [[heumos-2023-best-practices]] is the source that cautions against reading distances off UMAP embeddings.

## Open questions

- Does UMAP's distortion behave differently on sparse binary epigenomic matrices than on scRNA counts? No source in this corpus benchmarks that directly — a real gap given how much scATAC/scBS interpretation rests on it.

## Related

- [[traag-2019-leiden]] · [[heumos-2023-best-practices]] · [[scanpy]] · [[single-cell-multiomics]]
