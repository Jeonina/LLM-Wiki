---
type: concept
title: G&T-seq
aliases: [Genome and Transcriptome sequencing, G and T-seq, GnT-seq, G&T-seq]
tags: [multi-omics, scDNA-scRNA, physical-separation, joint-assay, foundational, method]
created: 2026-05-11
updated: 2026-06-29
---

# G&T-seq (Genome and Transcriptome sequencing)

> Plate-based single-cell joint DNA + RNA method that **physically separates** poly(A) mRNA (on oligo-dT magnetic beads) from genomic DNA (in the supernatant) before independent library preparation. Introduced by Macaulay et al. 2015 ([[10-Summaries/macaulay-2015-gt-seq]]); developed in the [[20-Entities/thierry-voet|Voet lab]] at KU Leuven. Provides the cleanest separation of DNA and RNA modalities at single-cell scale, compatible with any choice of WGA chemistry, and is the methodological root of [[scnmt-seq]] (which inherits the separation chemistry).

## Definition

Macaulay et al. 2015 ([[10-Summaries/macaulay-2015-gt-seq]]). In G&T-seq:

1. Single cell lysed in a multiwell plate.
2. Biotinylated oligo-dT magnetic beads capture poly(A) mRNA.
3. Supernatant — containing genomic and mitochondrial DNA — is moved to a fresh well for [[scwga]] (MDA preferred for SNV / deep coverage; PicoPlex/PCR preferred for CNV; or DA-PCR).
4. On-bead mRNA undergoes Smart-seq2 reverse transcription → full-length cDNA → Nextera XT.
5. Both fractions are sequenced independently and merged computationally by well/cell.

The separation-before-amplification design gives three advantages over the one-pot [[30-Concepts/dr-seq|DR-seq]] alternative: no coding-region masking needed, any WGA chemistry can be used, and full-length Smart-seq2 RNA (not 3′-biased).

## Why it matters

- **First true single-cell joint DNA + RNA assay** — provided the proof that paired genome + transcriptome at single-cell scale is achievable.
- **Modality independence**: each fraction can be processed by the best-of-class single-modality protocol — G&T-seq doesn't force a compromise on either RNA or DNA quality.
- **Compatible with long-read sequencing** of the RNA fraction for isoform detection.
- Demonstrated detection of a **trisomy-11 subclone in HCC38-BL lymphoblastoid cells** (10% frequency, confirmed by FISH) — first joint single-cell aneuploidy + dosage measurement.
- **Reversine-treated mouse 8-cell embryos**: reciprocal aneuploidies between sister blastomeres, with concordant chromosome-wide expression dosage in the *same* cells → expression dosing established within one division.
- MTAP–PCDH7 fusion captured at DNA and RNA level in the same HCC38 cells, with PacBio long-read confirmation.

## Variants and refinements

- **G&T-seq** ([[10-Summaries/macaulay-2015-gt-seq]]; protocol [[10-Summaries/macaulay-2016-gt-seq-protocol]]) — original DNA + RNA.
- **[[scnmt-seq]]** ([[10-Summaries/clark-2018-scnmt-seq]]) — inherits the separation chemistry; adds GpC methylation labeling for accessibility + endogenous CpG methylation.
- **SIDR-seq, DNTR-seq** — nuclear-cytosolic partitioning variants ([[10-Summaries/vandereyken-2023-scmultiomics-review]]). DNTR-seq uses direct Tn5 tagmentation of nuclear DNA instead of WGA, sidestepping WGA artifacts at the cost of lower coverage breadth.
- **DR-seq** — pre-amplification then split ([[30-Concepts/dr-seq]]).

## Contested points

- Plate-based throughput limits — 172 cells in the original benchmark; hundreds per day even with robotic automation, far below later combinatorial-indexing methods.
- Beadwash losses reduce per-cell DNA yield vs nuclear-cytosolic partitioning methods; some RNA is lost to the gDNA supernatant during separation.

## Examples

- Studies of clonal architecture in cancer using paired DNA+RNA from G&T-seq.

## Related

- [[30-Concepts/scdna-seq]]
- [[30-Concepts/single-cell-multiomics]]
- [[mda]]
- [[malbac]]
- [[dr-seq]]
- [[scwga]]
- [[scnmt-seq]]
- [[20-Entities/thierry-voet]]
- [[40-Topics/single-cell-multiomics]]
- [[40-Topics/whole-genome-amplification]]
