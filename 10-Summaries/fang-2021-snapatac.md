---
type: summary
title: "Fang 2021 — SnapATAC: comprehensive analysis of single-cell ATAC-seq data"
aliases: ["Fang 2021 SnapATAC", "SnapATAC"]
tags: [SnapATAC, scATAC-seq, Nystrom-method, genome-bin, Jaccard, Ren-lab, Ecker-lab, UCSD-Salk]
created: 2026-05-13
updated: 2026-05-13
sources: ["Comprehensive analysis of single cell ATAC-seq data with SnapATAC.md"]
---

Fang, Preissl, Li et al. (Ren, Ecker, Behrens labs; UCSD + Salk) developed **SnapATAC**, an scATAC-seq pipeline that does NOT require pre-defined peaks. Splits the genome into 5-kb bins, computes Jaccard similarity matrix between cells, applies regression-based depth normalization, then performs eigenvector decomposition. Uses **Nyström method** for scalability — analyzes up to a million cells. Applied to 55,592 mouse secondary motor cortex nuclei, identified ~370,000 cis-regulatory elements across 31 distinct cell populations.

## Why this matters

The most scalable scATAC analysis tool of its generation. Precedes SnapATAC2 (Zhang 2024 Rust rewrite). Important for atlas-scale brain mapping. Anchors §4 (scATAC analysis).

## Related

- [[10-Summaries/zhang-2024-snapatac2]]
- [[10-Summaries/cusanovich-2015-sciatac]]
- [[10-Summaries/schep-2017-chromvar]]
- [[10-Summaries/bravo-2019-cistopic]]
