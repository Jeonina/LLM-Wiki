---
type: concept
title: GoT (Genotyping of Transcriptomes)
aliases: [Genotyping of Transcriptomes, GoT method]
tags: [single-cell, scRNA-seq, genotyping, droplet, method]
created: 2026-05-07
updated: 2026-10-12
---

# GoT (Genotyping of Transcriptomes)

> A droplet-based single-cell method that links somatic genotype to single-cell transcriptome by amplifying the mutation-containing transcript from 10x Genomics scRNA-seq cDNA, then assigning genotypes via shared cell barcodes ([[10-Summaries/nam-2019-got|Nam 2019]]).

> [!abstract] 한눈에
> GoT는 10x scRNA-seq cDNA에서 mutation이 있는 transcript를 표적 증폭하고 cell barcode로 genotype을 각 세포의 transcriptome에 연결하는 방법이다 ([[10-Summaries/nam-2019-got|Nam 2019]]). 발현이 높고 transcript 끝 가까이에 있는 locus에서는 잘 되지만, 발현이 낮거나 먼 locus에서는 효율이 크게 떨어져 이후 gDNA 기반 GoT–ChA로 이어졌다 ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [클론성 조혈 교재](../60-Explainers/clonal-hematopoiesis.html)
>
> [단일세포 multi-omics](../60-Explainers/single-cell-multiomics.html)
<!-- /explainer-links -->

## Definition

GoT modifies the standard 10x Genomics 3′/5′ scRNA-seq workflow by reserving ~10% of the cDNA after reverse transcription for **targeted amplification of the transcript that carries the mutation of interest** ([[10-Summaries/nam-2019-got|Nam 2019]]). After two PCR steps with a gene-specific primer and an Illumina P5/RPI-x primer pair, the targeted amplicon library is spiked back into the standard 10x library and sequenced together. Mutational status is read from the amplicon, and assigned to single-cell expression profiles via the shared 10x cell barcode (CBC) and UMI ([[10-Summaries/nam-2019-got|Nam 2019]]).

The output is **paired (genotype, transcriptome) per cell** for thousands of cells per sample, at ~88% genotyping rates in CD34+ MPN samples vs ~1.4% from standard 10x reads — a ~60× improvement ([[10-Summaries/nam-2019-got|Nam 2019]]).

## Why it matters

- It dissolves a long-standing problem in cancer/clonal-hematopoiesis genomics: **mutated and wild-type cells share surface markers, so you cannot sort them apart** to study how a mutation perturbs a specific cell type ([[10-Summaries/nam-2019-got|Nam 2019]]).
- With GoT, the wild-type cells in the same sample become an internal control, eliminating cross-patient confounders. This is what makes the cell-identity-dependent transcriptional findings (UPR in MkPs vs NF-κB in HSPCs) defensible ([[10-Summaries/nam-2019-got|Nam 2019]]).
- GoT is also the foundational method in the [[20-Entities/landau-lab|Landau Lab]] methods program, directly extended by [[30-Concepts/circularization-got]] (same paper) and [[30-Concepts/got-cha]] (Izzo 2024) ([[10-Summaries/nam-2019-got|Nam 2019]]; [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Variants and refinements

| Variant | Genotype source | What it adds | Source |
|---|---|---|---|
| Standard GoT | cDNA, gene-specific primer + Illumina sequencing | Works well for mutations within ~1.5 kb of a transcript end and on adequately expressed genes | ([[10-Summaries/nam-2019-got\|Nam 2019]]) |
| Multiplexed GoT | cDNA, multiple gene-specific primers in parallel | Demonstrated for CALR + NFE2 + SF3B1 simultaneously | ([[10-Summaries/nam-2019-got\|Nam 2019]]) |
| [[30-Concepts/circularization-got\|Circularization GoT]] | cDNA, circularization + inverse PCR | Genotypes loci distant from transcript ends (e.g. JAK2V617F) | ([[10-Summaries/nam-2019-got\|Nam 2019]]) |
| [[30-Concepts/got-cha\|GoT–ChA]] | gDNA | Replaces RNA with chromatin accessibility and cDNA capture with gDNA capture; supersedes circularization GoT for low-expression / distal-locus drivers, with ~38% JAK2 capture | ([[10-Summaries/izzo-2024-got-cha\|Izzo 2024]]) |
| [[30-Concepts/sdr-seq\|SDR-seq]] | Direct targeted gDNA (≤480 loci+genes on Tapestri) | Generalizes the genotype-to-transcriptome logic, capturing coding *and* noncoding variants rather than only those present in mRNA | ([[10-Summaries/lindenhofer-2025-sdr-seq\|Lindenhofer 2025]]) |

## Evidence and examples

- CALR-mutated essential thrombocythemia: 38,290 CD34+ cells, 88.7% genotyped, revealing differential UPR / NF-κB outputs by progenitor type ([[10-Summaries/nam-2019-got|Nam 2019]]).
- Multiplexed CALR + NFE2 + SF3B1 in a triple-mutant MF case, recovering nested clonal evolution ([[10-Summaries/nam-2019-got|Nam 2019]]).

## Contested points

- **The 88% figure is locus-favorable.** CALR is highly expressed in CD34+ progenitors and the mutation sits within ~1.5 kb of the transcript end ([[10-Summaries/nam-2019-got|Nam 2019]]). For drivers with low expression or distal mutation positions, genotyping efficiency falls sharply — JAK2-V617F, for example, is captured at only ~7–10% by cDNA-based methods ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]). This expression-and-distance ceiling motivated first [[circularization-got]] within the GoT framework, and then [[got-cha]], which sources genotype from gDNA instead of cDNA ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- The "1.4% vs 88%" comparison is against off-the-shelf 10x reads at the locus, not against the best alternative (TARGET-seq, plate-based methods). Throughput vs accuracy tradeoffs against plate-based methods are not directly benchmarked.

## Related

> [!cards]
> - `concept` [[30-Concepts/circularization-got|Circularization GoT]] — Inverse-PCR variant for loci far from transcript ends.
> - `concept` [[30-Concepts/got-cha|GoT–ChA]] — gDNA-based successor that pairs genotype with chromatin accessibility.
> - `concept` [[30-Concepts/sdr-seq|SDR-seq]] — Targeted joint gDNA + RNA readout on Tapestri.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — The readout GoT–ChA swaps in for RNA.
> - `concept` [[30-Concepts/single-molecule-footprinting|Single-molecule footprinting]] — Molecule-level readout of protein–DNA occupancy.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Joint measurement of several layers in one cell.
> - `entity` [[20-Entities/landau-lab|Landau lab]] — Lab that developed GoT and its successors.
> - `entity` [[20-Entities/anna-s-nam|Anna S. Nam]] — First author of GoT.
> - `entity` [[20-Entities/franco-izzo|Franco Izzo]] — First author of GoT–ChA.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
