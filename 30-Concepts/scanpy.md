---
type: concept
title: scanpy
aliases: []
tags: [Python, single-cell, scRNA-seq, software, Theis-lab]
created: 2026-05-12
updated: 2026-10-12
---

# scanpy

> A Python package for scalable single-cell omics analysis (Wolf, Angerer, Theis 2018). Builds on the AnnData data structure. Provides clustering, manifold learning (UMAP, tSNE), trajectory inference (PAGA, diffusion pseudotime), and integration tools.

> [!abstract] 한눈에
> scanpy는 AnnData 구조 위에서 clustering, UMAP·tSNE, trajectory 추론, integration을 제공하는 single-cell 분석용 Python package다. episcanpy가 이를 scATAC-seq와 single-cell methylation으로 확장했다.

## Why it matters

The de facto Python framework for single-cell transcriptomics. [[30-Concepts/episcanpy]] extends it to scATAC-seq and single-cell methylation, inheriting the full ecosystem.

## Related

> [!cards]
> - `concept` [[30-Concepts/anndata|AnnData]] — Python data structure for cells × features matrices plus annotations.
> - `concept` [[30-Concepts/episcanpy|episcanpy]] — Brings scATAC-seq and single-cell methylation into scanpy / AnnData.
> - `entity` [[20-Entities/fabian-theis|Fabian Theis]] — Helmholtz Munich computational biologist.
