---
type: concept
title: sciCUT&Tag
aliases: [single-cell combinatorial indexing CUT&Tag]
tags: [CUT&Tag, single-cell, combinatorial-indexing, Henikoff-lab, ICELL8]
created: 2026-05-12
updated: 2026-05-12
---

# sciCUT&Tag

> A combinatorial-indexing variant of CUT&Tag that combines barcoded pA-Tn5 tagmentation (96 wells, first index) with ICELL8 5,184-nanowell PCR (second index) to profile ~40,000 cells per chip at ~$0.11/cell.

## Definition

Workflow: lightly cross-link nuclei → bind to WGA-magnetic beads → bulk primary + secondary antibody → array in 96-well plate with differentially barcoded pA-Tn5 → tagmentation → pool → dispense on ICELL8 at 12–24 cells/nanowell → PCR with second barcode → sequencing. SNP-based collision removal optional via multi-donor mixing.

## Why it matters

- ~8× cost reduction vs droplet-based scCUT&Tag.
- ~2× the unique reads/cell of original scCUT&Tag (2,116 vs 1,110 median reads for H3K27me3 in PBMCs).
- Underlying platform for **MulTI-Tag** (multi-target identification by tagmentation) — multi-epitope per cell.

## Examples

- Mixed-donor PBMC H3K4me1-2-3 and H3K27me3 profiling, with SNP-based collision QC ([[10-Summaries/janssens-2023-scicut-tag]]).

## Related

- [[30-Concepts/cut-and-tag]] · [[30-Concepts/combinatorial-indexing]] · [[30-Concepts/multi-tag]] · [[30-Concepts/icell8-nanowell]] · [[40-Topics/histone-modifications]] · [[20-Entities/steven-henikoff]]
