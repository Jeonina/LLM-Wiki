---
type: concept
title: Structural variants
aliases: [SVs, large genomic rearrangements]
tags: [genome, SV, CNV, inversion, translocation, cancer]
created: 2026-05-12
updated: 2026-10-07
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

## Added 2026-10-07

Single-cell Hi-C contacts far from restriction cut sites, with soft-clipped junctions, can flag SV breakpoints at 1-bp resolution: in 63 K562 LiMCA cells map3C plus EagleC filtering gave 61 breakpoints, 23 matching WGS SVs (precision 0.30, recall 0.0033) ([[10-Summaries/galasso-2026-map3c]]).

Droplet Hi-C called SVs from CNV-corrected single-cell contact matrices with EagleC. In a primary glioblastoma it found a malignant-specific translocation that moved *IKZF1*, without its promoter, onto *EGFR* ecDNA, and *IKZF1* transcription dropped ([[10-Summaries/chang-2025-droplet-hi-c]]). Per-cell contact features (hub index, i.e. the Gini coefficient of interchromosomal contacts; copy number; *trans*-to-*cis* ratio) separated ecDNA from homogeneously staining regions (HSRs), which aggregate Hi-C and adjnTIF could not ([[10-Summaries/chang-2025-droplet-hi-c]]).

Long-read single-cell WGS (dMDA + PacBio HiFi) found an average of 5473 bulk-confirmed SVs per cell versus 327 in Illumina dMDA cells, with precision of 0.73 for deletions and 0.66 for insertions ([[10-Summaries/hard-2023-long-read-scwgs]]). Nearly all called inversions and duplications were false positives caused by intramolecular dMDA chimeras, so the method is not suited to those SV classes ([[10-Summaries/hard-2023-long-read-scwgs]]).

BreakDancer calls SVs from short-insert paired-end reads in two complementary ways. BreakDancerMax clusters anomalously mapped read pairs with a Poisson confidence score, covering deletions, insertions, inversions and intra- and inter-chromosomal translocations. BreakDancerMini runs a sliding-window Kolmogorov–Smirnov test on normal pairs to catch 10–100 bp indels; together they cover 10 bp–1 Mb ([[10-Summaries/chen-2009-breakdancer]]). Read-pair signal is geometrically limited: only 43.2% of 844 simulated chr17 SVs had two or more anomalous pairs at 100× physical coverage. Insertions longer than 100 bp were undetectable with 200 bp inserts and 50 bp reads ([[10-Summaries/chen-2009-breakdancer]]).

Long reads from a single-cell Multiome library can resolve transgene integration. SPLONGGET assembled the ~5 kb tisagenlecleucel (CTL019) CAR vector de novo with Flye from LTR-containing reads, then used supplementary alignments to place integration sites across nearly all chromosomes, consistent with a polyclonal CAR-T population ([[10-Summaries/pancikova-2025-splongget]]). Severus called 1,362 somatic SVs from pseudobulks of the same B-ALL samples ([[10-Summaries/pancikova-2025-splongget]]).

## Related

- [[40-Topics/somatic-mosaicism]] · [[40-Topics/long-read-sequencing]] · [[30-Concepts/somagauss-sv]] · [[40-Topics/somatic-mosaicism]]
- [[10-Summaries/eichler-2007-completing-sv-map]] · [[10-Summaries/spielmann-2018-sv-3d-genome]] · [[10-Summaries/lupianez-2015-tad-disruption]] · [[30-Concepts/topologically-associating-domain]]

## Added 2026-08-13

Why single-cell SV calling lagged single-cell CNV calling by a decade: **chimeras**. Chimera formation during φ29's branching amplification joins non-contiguous sequences, and this is named as the reason structural variations are difficult to observe at single-cell level, while CNVs from hundreds of kilobases to megabases are detectable relatively easily ([[10-Summaries/huang-2015-scwga-review]]).

Chimeras also appear as an **assembly-graph** problem rather than a calling problem. [[10-Summaries/chitsaz-2011-velvet-sc|Velvet-SC]] worked around them by discarding read pairing entirely; [[10-Summaries/bankevich-2012-spades|SPAdes]] promoted chimera detection and removal to a named pipeline stage and thereby recovered the use of read pairs ([[10-Summaries/chitsaz-2011-velvet-sc]]; [[10-Summaries/bankevich-2012-spades]]).

This is why [[30-Concepts/strand-seq|Strand-seq]] and scTRIP took a completely different route — template-strand inheritance rather than improved amplification — to single-cell SV detection ([[10-Summaries/falconer-2012-natmethods]]; [[10-Summaries/sanders-2020-sctrip]]). (synthesis)

Chimera *rate* is named as a WGA evaluation axis but no standard assay for measuring it exists in the corpus ([[10-Summaries/huang-2015-scwga-review]]). (synthesis)
