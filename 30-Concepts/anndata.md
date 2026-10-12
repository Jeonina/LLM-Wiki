---
type: concept
title: AnnData
aliases: []
tags: [Python, data-structure, single-cell, scanpy]
created: 2026-05-12
updated: 2026-10-12
---

# AnnData

> A flexible Python data structure (built on NumPy/SciPy) for single-cell omics. Stores a (cells × features) count matrix together with per-cell metadata, per-feature metadata, dimensionality reductions, neighborhood graphs, and unstructured annotations.

> [!abstract] 한눈에
> AnnData는 세포×feature count matrix와 세포·feature별 metadata, 차원 축소 결과, 이웃 그래프를 한 객체에 담는 Python 자료구조다. scanpy, EpiScanpy, scvi-tools 같은 Python single-cell 도구들이 공통으로 쓰는 형식이다.

## Why it matters

- Lingua franca of the Python single-cell ecosystem.
- Used by scanpy, EpiScanpy, scvi-tools, CellRank, and many others.
- Enables multi-omics integration via paired AnnData objects.

## Related

> [!cards]
> - `concept` [[30-Concepts/scanpy|scanpy]] — Python single-cell analysis package built on AnnData.
> - `concept` [[30-Concepts/episcanpy|EpiScanpy]] — Brings scATAC-seq and single-cell methylation into the scanpy / AnnData ecosystem.
