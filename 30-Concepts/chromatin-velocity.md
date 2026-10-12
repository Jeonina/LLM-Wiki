---
type: concept
title: Chromatin velocity
aliases: [multi-modal velocity in chromatin]
tags: [single-cell, dynamics, differentiation, histone-modifications]
created: 2026-05-12
updated: 2026-10-12
---

# Chromatin velocity

> Coordinated dynamics of chromatin marks within a single cell over a differentiation trajectory — conceptually analogous to RNA velocity but for the chromatin layer ([[10-Summaries/yeung-2023-scchix-seq|scChIX-seq]]).

> [!abstract] 한눈에
> Chromatin velocity는 RNA velocity의 발상을 염색질에 옮긴 것으로, 한 세포에서 둘 이상의 histone mark나 chromatin과 전사를 함께 재서 분화 중 세포 상태가 어느 방향으로 움직이는지 추정한다 ([[10-Summaries/yeung-2023-scchix-seq|scChIX-seq]]). nano-CUT&Tag에서는 ATAC와 H3K27ac 쌍으로 방향을 복원했지만 서로 반대로 움직이는 H3K27ac/H3K27me3 쌍에서는 실패했다 ([[10-Summaries/bartosovic-2022-nano-cut-tag|Bartosovic 2022]]).

## Definition

By measuring two or more histone modifications per cell ([[30-Concepts/scchix-seq]]) or chromatin and transcription jointly, one can infer how chromatin states shift during cellular state transitions and predict future states from current ones ([[10-Summaries/yeung-2023-scchix-seq|scChIX-seq]]).

## Why it matters

Provides a chromatin-layer prediction of cell fate. Extends the RNA-velocity framework (La Manno et al. 2018) to epigenetic measurements ([[10-Summaries/yeung-2023-scchix-seq|scChIX-seq]]).

## Examples

- Macrophage in vitro differentiation: scChIX-seq reveals coordinated H3K4me1 + H3K36me3 dynamics that predict differentiation trajectory ([[10-Summaries/yeung-2023-scchix-seq|scChIX-seq]]).
- nano-CUT&Tag passed ATAC and H3K27ac gene-by-cell matrices to scVelo as the "unspliced" and "spliced" layers and recovered the OPC-to-mature-oligodendrocyte direction, while the anti-correlated H3K27ac/H3K27me3 pair failed ([[10-Summaries/bartosovic-2022-nano-cut-tag|Bartosovic 2022]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/scchix-seq|scChIX-seq]] — Two histone marks per cell by computational deconvolution.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Single-cell profiling of histone marks.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/bartosovic-2022-nano-cut-tag|Bartosovic 2022]]
> - [[10-Summaries/yeung-2023-scchix-seq|Yeung 2023]]
