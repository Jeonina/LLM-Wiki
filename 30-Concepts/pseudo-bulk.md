---
type: concept
title: Pseudo-bulk
aliases: [aggregation, in-silico bulk]
tags: [single-cell, aggregation, cluster, analysis]
created: 2026-05-12
updated: 2026-05-14
---

# Pseudo-bulk

> A common analysis pattern where reads from many single cells of the same identified type (cluster) are aggregated into a "pseudo-bulk" profile, enabling robust peak calling, motif analysis, differential testing, or comparison to true bulk data.

## Why it matters

Single cells are sparse; aggregating ~hundreds of cells gives a profile of similar quality to bulk sequencing for that cell type. Pseudo-bulking is used in essentially every single-cell ATAC, RNA, and chromatin pipeline.

## Why pseudo-bulk ≠ original bulk

Pseudo-bulk is conceptually closer to "bulk RNA-seq of a sorted cell type" than to "bulk RNA-seq of unfractionated tissue." The benefit over original bulk: cell-type composition is *known* (from the single-cell clustering), so apparent expression changes can be attributed to per-cell transcription rather than to composition shifts — addressing one of the central limitations of bulk RNA-seq for heterogeneous samples (see [[30-Concepts/scrna-seq]] § Bulk RNA-seq vs scRNA-seq).

## Examples

- [[10-Summaries/gur-2025-scatac-vs-bulk]] (Gur/Hughes 2025) — pseudo-bulked scATAC matches bulk and adds within-population heterogeneity detection.

## Related

- [[30-Concepts/scatac-seq]] · [[30-Concepts/snapatac]] · [[40-Topics/single-cell-atac-seq]]
- [[30-Concepts/scrna-seq]] — pseudo-bulk is the bridge between cell-resolved data and bulk-style differential-expression frameworks
