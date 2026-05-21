---
type: concept
title: GoT (Genotyping of Transcriptomes)
aliases: [Genotyping of Transcriptomes, GoT method]
tags: [single-cell, scRNA-seq, genotyping, droplet, method]
created: 2026-05-07
updated: 2026-05-07
---

# GoT (Genotyping of Transcriptomes)

> A droplet-based single-cell method that links somatic genotype to single-cell transcriptome by amplifying the mutation-containing transcript from 10x Genomics scRNA-seq cDNA, then assigning genotypes via shared cell barcodes.

## Definition

GoT modifies the standard 10x Genomics 3′/5′ scRNA-seq workflow by reserving ~10% of the cDNA after reverse transcription for **targeted amplification of the transcript that carries the mutation of interest** ([[10-Summaries/nam-2019-got]]). After two PCR steps with a gene-specific primer and an Illumina P5/RPI-x primer pair, the targeted amplicon library is spiked back into the standard 10x library and sequenced together. Mutational status is read from the amplicon, and assigned to single-cell expression profiles via the shared 10x cell barcode (CBC) and UMI.

The output is **paired (genotype, transcriptome) per cell** for thousands of cells per sample, at ~88% genotyping rates in CD34+ MPN samples vs ~1.4% from standard 10x reads — a ~60× improvement.

## Why it matters

It dissolves a long-standing problem in cancer/clonal-hematopoiesis genomics: **mutated and wild-type cells share surface markers, so you cannot sort them apart** to study how a mutation perturbs a specific cell type. With GoT, the wild-type cells in the same sample become an internal control, eliminating cross-patient confounders. This is what makes the cell-identity-dependent transcriptional findings in [[10-Summaries/nam-2019-got]] (UPR in MkPs vs NF-κB in HSPCs) defensible.

GoT is also the foundational method in the [[20-Entities/landau-lab|Landau Lab]] methods program, directly extended by [[30-Concepts/circularization-got]] (same paper) and [[30-Concepts/got-cha]] (Franco 2024).

## Variants and refinements

- **Standard GoT** ([[10-Summaries/nam-2019-got]]) — gene-specific primer + Illumina sequencing; works well for mutations within ~1.5 kb of a transcript end and on adequately expressed genes.
- **Multiplexed GoT** ([[10-Summaries/nam-2019-got]]) — multiple gene-specific primers in parallel; demonstrated for CALR + NFE2 + SF3B1 simultaneously.
- **[[30-Concepts/circularization-got]]** ([[10-Summaries/nam-2019-got]]) — circularization + inverse PCR to genotype loci distant from transcript ends (e.g. JAK2V617F).
- **[[30-Concepts/got-cha]]** ([[10-Summaries/izzo-2024-got-cha]]) — replaces RNA with chromatin accessibility and cDNA capture with gDNA capture; supersedes circularization GoT for low-expression / distal-locus drivers.

## Contested points

- The "1.4% vs 88%" comparison is against off-the-shelf 10x reads at the locus, not against the best alternative (TARGET-seq, plate-based methods). Throughput vs accuracy tradeoffs against plate-based methods are not directly benchmarked.
- Genotyping efficiency drops sharply for loci > 1.5 kb from transcript ends or genes with low expression — limitations explicitly addressed by circularization GoT and then more cleanly by GoT–ChA.

## Examples

- CALR-mutated essential thrombocythemia: 38,290 CD34+ cells, 88.7% genotyped, revealing differential UPR / NF-κB outputs by progenitor type ([[10-Summaries/nam-2019-got]]).
- Multiplexed CALR + NFE2 + SF3B1 in a triple-mutant MF case, recovering nested clonal evolution ([[10-Summaries/nam-2019-got]]).

## Related

- [[circularization-got]]
- [[got-cha]]
- [[chromatin-accessibility]]
- [[single-molecule-footprinting]]
- [[40-Topics/single-cell-multiomics]]
- [[20-Entities/landau-lab]]
- [[20-Entities/anna-s-nam]]
- [[20-Entities/franco-izzo]]
