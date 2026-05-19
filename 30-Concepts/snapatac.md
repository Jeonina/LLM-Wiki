---
type: concept
title: SnapATAC
aliases: [snapATAC2]
tags: [scATAC-seq, peak-free, Ren-lab, scalable, software]
created: 2026-05-12
updated: 2026-05-12
---

# SnapATAC

> Single Nucleus Analysis Pipeline for ATAC-seq. A peak-free scATAC-seq pipeline from the Ren lab that bins the genome into 5-kb windows, computes pairwise Jaccard similarities between cells, and uses the ensemble Nyström method for scalable low-rank embedding to 1M cells.

## Definition

Workflow: SnapTools for preprocessing → snap file format → 5-kb binary bin vector per cell → Jaccard similarity matrix → regression-normalized for depth → eigenvector decomposition → optional Harmony batch correction → clustering. Includes peak calling, enhancer-target gene linking via scRNA integration, trajectory inference, and dataset integration with scATAC atlases.

## Why it matters

- Discovers rare cell types (<0.1% of population) that peak-anchored methods miss, because bin-level signal works even for cells too rare to define peaks.
- Off-peak reads contribute clustering signal (correlate with euchromatin / compartment A).
- Scales to 1M cells via ensemble Nyström approximation.

## Examples

- Mouse secondary motor cortex (MOp): 55,592 cells → 31 cell populations → ~370k cREs, including rare interneurons Sst+, Vip+ ([[10-Summaries/fang-2021-snapatac]]).

## Related

- [[30-Concepts/scatac-seq]] · [[30-Concepts/jaccard-similarity]] · [[30-Concepts/nystrom-method]] · [[30-Concepts/cistopic]] · [[40-Topics/single-cell-atac-seq]] · [[20-Entities/bing-ren]]
