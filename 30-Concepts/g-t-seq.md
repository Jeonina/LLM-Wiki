---
type: concept
title: G&T-seq
aliases: [G&T-seq, genome and transcriptome sequencing, GnT-seq]
tags: [joint-assay, single-cell-multiomics, scDNA, scRNA-seq, foundational, method]
created: 2026-05-12
updated: 2026-05-12
---

# G&T-seq (Genome and Transcriptome sequencing)

> Single-cell joint DNA + RNA assay that **physically separates** poly(A) mRNA from genomic DNA using a biotinylated oligo-dT primer before independent amplification. Predecessor and methodological root of [[scnmt-seq]] (which inherits the separation chemistry).

## Definition

Macaulay et al. 2015 ([[10-Summaries/macaulay-2015-gt-seq]]). Cell is lysed → biotinylated oligo-dT magnetic beads capture mRNA → supernatant (gDNA) is moved to a fresh well. mRNA arm: on-bead Smart-seq2 reverse transcription → full-length cDNA → Nextera XT. DNA arm: any WGA chemistry (MDA preferred for SNV / deep coverage; PicoPlex preferred for CNV) → Nextera XT.

## Why it matters

- **First true single-cell joint DNA + RNA assay**.
- The separation-before-amplification design gives three advantages over the one-pot [[30-Concepts/dr-seq|DR-seq]] alternative: no coding-region masking needed, any WGA chemistry can be used, and full-length Smart-seq2 RNA (not 3′-biased).
- Demonstrated detection of a **trisomy-11 subclone in HCC38-BL lymphoblastoid cells** (10% frequency, confirmed by FISH) — first joint single-cell aneuploidy + dosage measurement.
- **Reversine-treated mouse 8-cell embryos**: reciprocal aneuploidies between sister blastomeres, with concordant chromosome-wide expression dosage in the *same* cells → expression dosing established within one division.
- MTAP–PCDH7 fusion at DNA and RNA level in the same HCC38 cells, with PacBio long-read confirmation.

## Variants and refinements

- **G&T-seq** ([[10-Summaries/macaulay-2015-gt-seq]]) — original DNA + RNA.
- **[[scnmt-seq]]** ([[10-Summaries/clark-2018-scnmt-seq]]) — inherits the separation chemistry; adds GpC methylation labeling for accessibility + endogenous CpG methylation.

## Contested points

- Plate-based throughput (172 cells in the original benchmark) is much lower than later combinatorial-indexing methods.
- Some RNA is lost to the gDNA supernatant during separation.

## Related

- [[dr-seq]]
- [[scwga]]
- [[mda]]
- [[malbac]]
- [[20-Entities/thierry-voet]]
- [[single-cell-multiomics]]
- [[40-Topics/single-cell-multiomics]]
- [[40-Topics/whole-genome-amplification]]
