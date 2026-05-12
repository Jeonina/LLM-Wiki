---
type: concept
title: µATAC-seq
aliases: [micro-ATAC-seq, nano-well scATAC]
tags: [scATAC-seq, throughput, ICELL8, Greenleaf-lab]
created: 2026-05-12
updated: 2026-05-12
---

# µATAC-seq

> A high-throughput single-cell ATAC-seq implementation on the Takara ICELL8 5,184-nanowell platform. Integrates Hoechst/PI fluorescence imaging for live-cell QC before reagent deposition. ~1,800 cells/chip at ~$0.81/cell library cost.

## Definition

Workflow: cells loaded under Poisson dilution → imaged for live single-cell wells → Tn5 transposition (40 nl per well) → EDTA quench → MgCl₂ neutralization → indexed PCR amplification → off-chip extraction by centrifugation.

## Why it matters

- ~20-fold throughput improvement over Fluidigm C1 at lower per-cell cost.
- Live-cell imaging compatibility enables multi-omic integration that combinatorial-indexing lacks.
- Per-cell fragment yield (~14k) higher than combinatorial-indexing methods.

## Examples

- 2,333 PBMCs from 3 donors → de novo clustering by hematopoietic cell type with PU.1, C/EBPα, RUNX1 motifs differential ([[10-Summaries/high-throughput-chromatin-accessibility-profiling-at-single-cell-resolution]]).

## Related

- [[30-Concepts/scatac-seq]] · [[30-Concepts/icell8-nanowell]] · [[30-Concepts/tn5-tagmentation]] · [[40-Topics/single-cell-atac-seq]] · [[20-Entities/sandy-klemm]] · [[20-Entities/william-greenleaf]]
