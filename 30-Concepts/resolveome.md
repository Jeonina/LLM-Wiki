---
type: concept
title: "ResolveOME (PTA whole-genome + full-transcriptome single-cell)"
aliases: [ResolveOME, ResolveOme, ResolveOME amplification]
tags: [single-cell, PTA, whole-genome, transcriptome, DNA+RNA, multiomics, method]
created: 2026-06-26
updated: 2026-10-12
---

# ResolveOME (PTA whole-genome + full-transcriptome single-cell)

> A single-cell assay that pairs PTA-based whole-genome amplification with full-transcript RNA-seq from the same cell, reading a cell's genome-wide genotype (SNV/CNV) alongside the transcriptome that reports its identity and state ([[10-Summaries/marks-2023-resolveome|Marks 2023]]).

> [!abstract] 한눈에
> ResolveOME는 PTA로 증폭한 whole genome과 full-transcript RNA-seq를 같은 세포에서 함께 읽어, 유전체 전체의 point mutation과 그 세포의 정체성·상태를 연결하는 assay다 ([[10-Summaries/marks-2023-resolveome|Marks 2023]]). 다만 methylation이나 chromatin 같은 epigenetic layer는 측정하지 않는다 ([[10-Summaries/marks-2023-resolveome|Marks 2023]]).

## Definition

ResolveOME exploits primary template-directed amplification ([[pta]]) for accurate, complete-genome single-nucleotide-variation assessment in conjunction with full-transcript reverse transcription on the same cell ([[10-Summaries/marks-2023-resolveome|Marks 2023]]). It is commercialized by BioSkryb Genomics with the BaseJumper bioinformatics platform ([[10-Summaries/marks-2023-resolveome|Marks 2023]]). Unlike methylation-based triple-omics, ResolveOME measures the DNA *sequence* (not bisulfite-converted), preserving point-mutation information, but measures no epigenetic layer ([[10-Summaries/marks-2023-resolveome|Marks 2023]]).

## Why it matters

It realizes the DNA-first version of joint genotype+phenotype: genome-wide point mutations (not targeted loci, unlike [[got-cha]]; not CNV-only, unlike [[sctrio-seq]]) paired with a full transcriptome ([[10-Summaries/marks-2023-resolveome|Marks 2023]]). Its capability profile is fidelity (PTA) + co-presence (per cell) + phenotypic association (RNA) — three-of-three in the [[scdna-capabilities-framework]] for sequence variants ([[10-Summaries/marks-2023-resolveome|Marks 2023]]). The transcriptome supplies the cell-identity context needed to interpret a variant — genotype alone does not say which cell type carries it or what it does ([[10-Summaries/marks-2023-resolveome|Marks 2023]]).

## Variants and refinements

- **ResolveDNA** ([[10-Summaries/marks-2023-resolveome|Marks 2023]]) — the genome-only PTA arm; ResolveOME adds the transcriptome.
- **ResolveOME + downstream protein/epitope readouts** ([[10-Summaries/marks-2023-resolveome|Marks 2023]]) — vendor extensions melding additional layers; core paper is DNA + RNA.

## Evidence and examples

- AML quizartinib resistance: a FLT3 missense mutation co-detected with upregulation of AXL signal transduction in the same cell ([[10-Summaries/marks-2023-resolveome|Marks 2023]]).
- Primary breast cancer: oncogenic PIK3CA N345K plus heterogeneous chromosomal loss, interpreted through same-cell transcriptomic identity ([[10-Summaries/marks-2023-resolveome|Marks 2023]]).

## Contested points

- No epigenetic layer (no methylation, no chromatin) — regulatory consequences of variants are inferred from RNA, not measured directly ([[10-Summaries/marks-2023-resolveome|Marks 2023]]).
- Preprint status with cell-line and limited primary demonstrations; ADO, throughput, and cost at cohort scale not fully characterized ([[10-Summaries/marks-2023-resolveome|Marks 2023]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/pta|PTA]] — The WGA chemistry underpinning the genome arm.
> - `concept` [[30-Concepts/scdna-capabilities-framework|scDNA capabilities framework]] — ResolveOME = fidelity + co-presence + RNA association.
> - `concept` [[30-Concepts/got-cha|GoT-ChA]] — Targeted genotype + chromatin alternative; ResolveOME is genome-wide genotype + RNA.
> - `concept` [[30-Concepts/sctrio-seq|scTrio-seq]] — CNV + methylation + RNA precedent; ResolveOME swaps methylation for genome-wide SNV.
> - `concept` [[30-Concepts/scwga|scWGA]] — Methods that amplify the DNA of a single cell for whole-genome sequencing.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Two or more molecular modalities measured in the same cell.
> - `hub` [[40-Topics/scdna-cancer-applications|scDNA cancer applications]] — Intratumor heterogeneity, chemoresistance and clinical translation.
> - `entity` [[20-Entities/charles-gawad|Charles Gawad]] — Pediatric oncologist–scientist; PI at St Jude.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/marks-2023-resolveome|Marks 2023]]
