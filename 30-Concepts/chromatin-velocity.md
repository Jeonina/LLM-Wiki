---
type: concept
title: Chromatin velocity
aliases: [multi-modal velocity in chromatin]
tags: [single-cell, dynamics, differentiation, histone-modifications]
created: 2026-05-12
updated: 2026-10-07
---

# Chromatin velocity

> Coordinated dynamics of chromatin marks within a single cell over a differentiation trajectory — conceptually analogous to RNA velocity but for the chromatin layer.

## Definition

By measuring two or more histone modifications per cell ([[30-Concepts/scchix-seq]]) or chromatin + transcription jointly, one can infer how chromatin states shift during cellular state transitions and predict future states from current ones.

## Why it matters

Provides a chromatin-layer prediction of cell fate. Extends the RNA-velocity framework (La Manno et al. 2018) to epigenetic measurements.

## Examples

- Macrophage in vitro differentiation: scChIX-seq reveals coordinated H3K4me1 + H3K36me3 dynamics that predict differentiation trajectory ([[10-Summaries/yeung-2023-scchix-seq]]).

## Added 2026-10-07

nano-CUT&Tag passed ATAC and H3K27ac gene-by-cell matrices to scVelo as the "unspliced" and "spliced" layers and recovered the OPC-to-mature-oligodendrocyte direction, while the anti-correlated H3K27ac/H3K27me3 pair failed ([[10-Summaries/bartosovic-2022-nano-cut-tag]]).

## Related

- [[30-Concepts/scchix-seq]] · [[40-Topics/histone-modifications]]
