---
type: concept
title: scEpi²-seq
aliases: [single-cell Epi² sequencing]
tags: [single-cell, multi-omics, histone-modifications, methylation, TAPS, sortChIC]
created: 2026-05-12
updated: 2026-05-12
---

# scEpi²-seq

> A single-cell multi-omics method that profiles a histone modification **and** DNA methylation **and** nucleosome positioning from the same cell. Combines sortChIC (pA-MNase + FACS) with TAPS conversion (bisulfite-free 5mC → uracil).

## Definition

Workflow: FACS-sort cells → bind to antibody-recruited pA-MNase → MNase digestion → adaptor ligation with cell-barcoded UMIs → pool → TAPS chemistry (without destroying barcoded adaptors, unlike bisulfite) → IVT/RT/PCR → Illumina sequencing. Read-start distances reconstruct nucleosome positioning.

## Why it matters

- Bisulfite can't be combined with histone-modification adaptor-ligation workflows because it fragments DNA. TAPS preserves them.
- Joint per-cell readout of histone + methylation reveals mechanisms of methylation maintenance: nucleosome occupancy blocks DNMT1 (12% methylation drop at nucleosome midpoint vs 4% at linker DNA through S-phase).
- DMRs within H3K27me3 domains distinguish epithelial from immune cell lineages — methylation is an **additive** regulatory layer over PRC2-marked facultative heterochromatin.

## Examples

- K562, RPE-1 hTERT FUCCI cells, mouse small intestine ([[10-Summaries/single-cell-multi-omic-detection-of-dna-methylation-and-histone-modifications-reconstructs-the-dynamics-of-epigenomic-maintenance]]).

## Related

- [[30-Concepts/sortchic]] · [[30-Concepts/taps]] · [[30-Concepts/histone-modifications]] · [[30-Concepts/dna-methylation]] · [[30-Concepts/replication-timing]] · [[40-Topics/single-cell-multiomics]]
