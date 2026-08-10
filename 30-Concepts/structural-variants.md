---
type: concept
title: Structural variants
aliases: [SVs, large genomic rearrangements]
tags: [genome, SV, CNV, inversion, translocation, cancer]
created: 2026-05-12
updated: 2026-08-10
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

## Definition, mechanisms and interpretation

- **Scope.** SV = "all genomic changes that are not single base-pair substitutions" — insertions, deletions, inversions, duplications, translocations, including CNVs ([[10-Summaries/eichler-2007-completing-sv-map]]). CNV is the *unbalanced* subset; inversions, reciprocal translocations and copy-number-neutral insertions are **balanced** ([[10-Summaries/spielmann-2018-sv-3d-genome]]).
- **Balanced SV is systematically under-ascertained.** 1–20% of all SV was estimated to be balanced and invisible to array methods ([[10-Summaries/eichler-2007-completing-sv-map]]); array CGH additionally has "low efficacy in mosaic individuals," and short-read WGS misses breakpoints in the repetitive regions where breakpoints preferentially occur ([[10-Summaries/spielmann-2018-sv-3d-genome]]).
- **Five phenotypic mechanisms**: gene dosage, gene disruption, fusion genes at junctions, position effects on nearby regulation, and unmasking of recessive alleles on the remaining allele ([[10-Summaries/eichler-2007-completing-sv-map]]) — the last of which is what [[10-Summaries/smukowski-heil-2023-loh|LOH]] does somatically.
- **Position relative to TAD boundaries determines pathogenicity**, not size or copy-number direction: intra-TAD SVs alter enhancer dosage, while inter-TAD SVs cause TAD fusion, neo-TAD formation or TAD shuffling ([[10-Summaries/spielmann-2018-sv-3d-genome]]; causally demonstrated in [[10-Summaries/lupianez-2015-tad-disruption]]).
- **De novo SV rates are unresolved.** Estimates range 0.05–0.16 per generation, and three analyses of the same ASD dataset reached three different conclusions about non-coding SV contribution ([[10-Summaries/spielmann-2018-sv-3d-genome]]).
- **Frequency of 3D position effects is phenotype-specific**: ~7% of balanced translocations in neurodevelopmental disorders disrupt TADs, but **57%** of congenital limb-malformation CNVs act through cis-regulatory position effects ([[10-Summaries/spielmann-2018-sv-3d-genome]]).

## Related

- [[40-Topics/somatic-mosaicism]] · [[40-Topics/long-read-sequencing]] · [[30-Concepts/somagauss-sv]] · [[40-Topics/somatic-mosaicism]]
- [[10-Summaries/eichler-2007-completing-sv-map]] · [[10-Summaries/spielmann-2018-sv-3d-genome]] · [[10-Summaries/lupianez-2015-tad-disruption]] · [[30-Concepts/topologically-associating-domain]]
