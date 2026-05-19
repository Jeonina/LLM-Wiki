---
type: concept
title: Structural variants
aliases: [SVs, large genomic rearrangements]
tags: [genome, SV, CNV, inversion, translocation, cancer]
created: 2026-05-12
updated: 2026-05-12
---

# Structural variants (SVs)

> Large (>50 bp by some definitions; >1 kb by others) genomic rearrangements: deletions, insertions, duplications, inversions, translocations, tandem repeats. Major drivers of cancer and developmental disease, harder to detect than SNVs with short-read sequencing.

## Definition

SVs include:
- **Deletions** / **insertions** (>50 bp)
- **Duplications** (often tandem)
- **Inversions** (reversed orientation)
- **Translocations** (inter-chromosomal)
- **Mobile element insertions** (LINE-1, Alu, SVA)
- **Repeat expansions** (HD CAG, FXTAS CGG, somatic STR expansions in cancer)

## Why it matters

- Cause many monogenic diseases (Duchenne deletions, hemophilia A inversion, *MYC* translocations in lymphoma).
- Drive cancer (TP53 deletions, BCR-ABL fusion in CML).
- Often **larger functional impact per event than SNVs** but harder to detect.
- Long-read sequencing dramatically improves SV detection sensitivity.

## Examples

- [[10-Summaries/liu-2025-nanopore-lscc-svs]] uses nanopore for somatic SV detection in LSCC; finds smoking × deletion-burden correlation and a repeat-expansion regulating *TP53BP2*/*FBXO28*.
- [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] detects chromosomal rearrangements (including TCR loci) at single-cell scale.

## Related

- [[30-Concepts/somatic-mosaicism]] · [[30-Concepts/long-read-sequencing]] · [[30-Concepts/somagauss-sv]] · [[40-Topics/somatic-mosaicism]]
