---
type: concept
title: "Latent semantic indexing (TF-IDF + SVD)"
aliases: []
tags: []
created: 2026-10-07
updated: 2026-10-07
sources: ["[[10-Summaries/luo-2024-scatac-benchmark]]", "[[10-Summaries/raimundo-2023-schptm-benchmark]]", "[[10-Summaries/wu-2026-sccut-tag-review]]"]
---

# Latent semantic indexing (TF-IDF + SVD)

> Latent semantic indexing (LSI) is the two-step embedding of TF-IDF normalization followed by SVD/PCA, borrowed from information retrieval and now the default dimensionality reduction for sparse single-cell chromatin data ([[10-Summaries/wu-2026-sccut-tag-review]]).

## In practice

- Implemented in Signac and ArchR (iterative LSI); the first component is usually dropped because it correlates with sequencing depth, and dimensions 2–30 are kept ([[10-Summaries/wu-2026-sccut-tag-review]]).
- Variants differ in post-processing: ChromSCape_LSI weights components by eigenvalue, while Signac whitens and uses 50 dimensions by default, which the benchmark links to Signac's weaker results on the low-coverage PBMC data ([[10-Summaries/raimundo-2023-schptm-benchmark]]).
- TF-IDF can also be paired with NMF (scOpen-style TFIDF-NMF) ([[10-Summaries/raimundo-2023-schptm-benchmark]]).

## Evidence

- For single-cell histone PTM data, the three best embeddings all use TF-IDF, and the gap between NMF and TFIDF-NMF isolates the effect of the transform ([[10-Summaries/raimundo-2023-schptm-benchmark]]).
- For scATAC-seq, an independent benchmark found SnapATAC/SnapATAC2 and feature aggregation outperform LSI-based methods ([[10-Summaries/luo-2024-scatac-benchmark]]), so the advantage is modality-dependent (synthesis).

## Related

- [[dimensionality-reduction]] · [[snapatac]] · [[cistopic]] · [[scopen]] · [[cut-and-tag]] · [[scatac-seq]]
