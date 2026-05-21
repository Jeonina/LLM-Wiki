---
type: concept
title: G&T-seq
aliases: [Genome and Transcriptome sequencing, G and T-seq]
tags: [multi-omics, scDNA-scRNA, physical-separation, method]
created: 2026-05-11
updated: 2026-05-11
---

# G&T-seq

> Plate-based single-cell multi-omic method that physically separates polyA RNA (on oligo-dT beads) from genomic DNA (in supernatant) before independent library preparation. Developed by [[20-Entities/thierry-voet|Voet lab]] at KU Leuven; provides the cleanest separation of DNA and RNA modalities at single-cell scale, compatible with any choice of WGA chemistry.

## Definition

In G&T-seq ([[10-Summaries/vandereyken-2023-scmultiomics-review]]):

1. Single cell lysed in a multiwell plate.
2. Oligo-dT magnetic beads capture polyA RNA.
3. Supernatant — containing genomic and mitochondrial DNA — is removed for [[scwga]] (MDA, PCR, or DA-PCR).
4. Captured RNA on beads undergoes reverse transcription + Smart-seq2-style amplification.
5. Both fractions are sequenced independently and merged computationally by well/cell.

Sibling methods using similar physical-separation principles: scONE-seq, scDNA + scRNA, single-cell transcriptogenomics (with targeted exome).

## Why it matters

- **Modality independence**: each fraction can be processed by the best-of-class single-modality protocol — G&T-seq doesn't force a compromise on either RNA or DNA quality.
- **Compatible with long-read sequencing** of the RNA fraction for isoform detection.
- **Foundational scDNA + scRNA method** — provided the proof that paired genome + transcriptome at single-cell scale is achievable.

## Variants and refinements

- **SIDR-seq, DNTR-seq** — nuclear-cytosolic partitioning variants ([[10-Summaries/vandereyken-2023-scmultiomics-review]]).
- **DNTR-seq** — uses direct Tn5 tagmentation of nuclear DNA instead of WGA, sidestepping WGA artifacts at the cost of lower coverage breadth.
- **DR-seq** — pre-amplification then split.

## Contested points

- Plate-based throughput limits — hundreds of cells per day even with robotic automation.
- Beadwash losses reduce per-cell DNA yield vs nuclear-cytosolic partitioning methods.

## Examples

- Studies of clonal architecture in cancer using paired DNA+RNA from G&T-seq.

## Related

- [[scdna-seq]]
- [[single-cell-multiomics]]
- [[mda]]
- [[40-Topics/single-cell-multiomics]]
