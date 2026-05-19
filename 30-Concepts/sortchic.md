---
type: concept
title: sortChIC
aliases: [FACS-sorted ChIC]
tags: [histone-modifications, single-cell, MNase, FACS, van-Oudenaarden-lab]
created: 2026-05-12
updated: 2026-05-12
---

# sortChIC

> A single-cell histone-modification profiling method from the van Oudenaarden lab that combines pA-MNase + antibody binding with FACS sorting into 384-well plates. Designed for integration with cell-cycle reporters (FUCCI) and fluorescent labels.

## Definition

Workflow: bind antibody to histone mark in suspension → recruit pA-MNase → FACS sort single cells into plates (capturing fluorescence metadata) → MNase activation → adaptor ligation → IVT/PCR.

## Why it matters

- FACS compatibility enables integration with cell-cycle reporters (FUCCI), CellTrace dyes (intestinal anteroposterior axis labeling), and other fluorescent metadata that droplet platforms cannot capture.
- Substrate for [[30-Concepts/scchix-seq]] (two marks per cell) and [[30-Concepts/scepi2-seq]] (mark + 5mC per cell).

## Examples

- Mouse intestine epithelial vs immune lineage profiling with anteroposterior CellTrace labeling ([[10-Summaries/geisenberger-2025-scepi2-seq]]).

## Related

- [[30-Concepts/chic-seq]] · [[30-Concepts/scchic-seq]] · [[30-Concepts/scchix-seq]] · [[30-Concepts/scepi2-seq]] · [[40-Topics/histone-modifications]] · [[20-Entities/alexander-van-oudenaarden]]
