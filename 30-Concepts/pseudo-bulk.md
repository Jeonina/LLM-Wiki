---
type: concept
title: Pseudo-bulk
aliases: [aggregation, in-silico bulk]
tags: [single-cell, aggregation, cluster, analysis]
created: 2026-05-12
updated: 2026-05-12
---

# Pseudo-bulk

> A common analysis pattern where reads from many single cells of the same identified type (cluster) are aggregated into a "pseudo-bulk" profile, enabling robust peak calling, motif analysis, differential testing, or comparison to true bulk data.

## Why it matters

Single cells are sparse; aggregating ~hundreds of cells gives a profile of similar quality to bulk sequencing for that cell type. Pseudo-bulking is used in essentially every single-cell ATAC, RNA, and chromatin pipeline.

## Examples

- [[10-Summaries/scatac-seq-generates-more-accurate-and-complete-regulatory-maps-than-bulk-atac-seq]] (Gur/Hughes 2025) — pseudo-bulked scATAC matches bulk and adds within-population heterogeneity detection.

## Related

- [[30-Concepts/scatac-seq]] · [[30-Concepts/snapatac]] · [[40-Topics/single-cell-atac-seq]]
