---
type: concept
title: DR-seq
aliases: [DR-seq, gDNA-mRNA sequencing, one-pot joint genome-transcriptome]
tags: [joint-assay, single-cell-multiomics, scDNA, scRNA-seq, quasilinear-amplification, method]
created: 2026-05-12
updated: 2026-05-12
---

# DR-seq (gDNA-mRNA sequencing)

> One-pot single-cell joint DNA + RNA assay that avoids physical separation by performing **MALBAC-style quasilinear amplification on both DNA and ssDNA cDNA simultaneously**, then splitting the sample for separate RNA (via IVT) and DNA (via PCR) library preparation.

## Definition

Dey et al. 2015 ([[10-Summaries/dey-2015-dr-seq]]). Cell lysed with poly-T primer carrying cell-barcode + T7 promoter (Ad-1x); RT performed in situ. Seven rounds of quasilinear amplification with a random-8-mer adaptor (Ad-2) amplify both gDNA and cDNA together. Sample split: half → IVT-based RNA library (only T7-bearing cDNA amplicons transcribed); half → PCR-based DNA library. **DNA reads from coding regions must be computationally masked** because they could come from either gDNA or cDNA.

## Why it matters

- **One-pot alternative to [[g-t-seq|G&T-seq]]** — simpler workflow, less material loss, no physical separation step.
- **Length-based identifiers (LBIs)**: the genomic priming position of the first Ad-2 amplicon serves as a UMI surrogate, reducing CV for ~80% of genes. Matches CEL-seq with random-sequence UMIs.
- Demonstrated that **DNA copy-number variation strongly drives expression** at single-cell resolution in SK-BR-3 breast cancer cells (CNV calls confirmed by DNA FISH at four loci, Kolmogorov–Smirnov *P* > 0.01 with FISH distributions).
- Observed **inverse relationship between expression variability and copy number** — high-CV genes on low-copy regions, suggesting CNVs may drive expression-level variability.

## Variants and refinements

- **DR-seq** ([[10-Summaries/dey-2015-dr-seq]]).
- Conceptual successor with three modalities: [[sctrio-seq]] (adds methylation).

## Contested points

- Coding-region masking limits SNV detection from coding regions of the DNA half.
- RNA reads are 3′-biased (CEL-seq lineage), unlike G&T-seq's full-length Smart-seq2 coverage.
- Quasilinear amplification GC bias slightly higher than MALBAC alone.

## Related

- [[g-t-seq]]
- [[malbac]]
- [[scwga]]
- [[umi-molecular-barcoding]]
- [[20-Entities/alexander-van-oudenaarden]]
- [[single-cell-multiomics]]
- [[40-Topics/single-cell-multiomics]]
- [[40-Topics/whole-genome-amplification]]
