---
type: concept
title: "ResolveOME (PTA whole-genome + full-transcriptome single-cell)"
aliases: [ResolveOME, ResolveOme, ResolveOME amplification]
tags: [single-cell, PTA, whole-genome, transcriptome, DNA+RNA, multiomics, method]
created: 2026-06-26
updated: 2026-06-26
---

# ResolveOME (PTA whole-genome + full-transcriptome single-cell)

> A single-cell assay that pairs PTA-based whole-genome amplification with full-transcript RNA-seq from the same cell, reading a cell's genome-wide genotype (SNV/CNV) alongside the transcriptome that reports its identity and state ([[10-Summaries/marks-2023-resolveome]]).

## Definition

ResolveOME exploits primary template-directed amplification ([[pta]]) for accurate, complete-genome single-nucleotide-variation assessment in conjunction with full-transcript reverse transcription on the same cell ([[10-Summaries/marks-2023-resolveome]]). It is commercialized by BioSkryb Genomics with the BaseJumper bioinformatics platform ([[10-Summaries/marks-2023-resolveome]]). Unlike methylation-based triple-omics, ResolveOME measures the DNA *sequence* (not bisulfite-converted), preserving point-mutation information, but measures no epigenetic layer ([[10-Summaries/marks-2023-resolveome]]).

## Why it matters

It realizes the DNA-first version of joint genotype+phenotype: genome-wide point mutations (not targeted loci, unlike [[got-cha]]; not CNV-only, unlike [[sctrio-seq]]) paired with a full transcriptome ([[10-Summaries/marks-2023-resolveome]]). Its capability profile is fidelity (PTA) + co-presence (per cell) + phenotypic association (RNA) — three-of-three in the [[scdna-capabilities-framework]] for sequence variants ([[10-Summaries/marks-2023-resolveome]]). The transcriptome supplies the cell-identity context needed to interpret a variant — genotype alone does not say which cell type carries it or what it does ([[10-Summaries/marks-2023-resolveome]]).

## Variants and refinements

- **ResolveDNA** ([[10-Summaries/marks-2023-resolveome]]) — the genome-only PTA arm; ResolveOME adds the transcriptome.
- **ResolveOME + downstream protein/epitope readouts** ([[10-Summaries/marks-2023-resolveome]]) — vendor extensions melding additional layers; core paper is DNA + RNA.

## Contested points

- No epigenetic layer (no methylation, no chromatin) — regulatory consequences of variants are inferred from RNA, not measured directly ([[10-Summaries/marks-2023-resolveome]]).
- Preprint status with cell-line and limited primary demonstrations; ADO, throughput, and cost at cohort scale not fully characterized ([[10-Summaries/marks-2023-resolveome]]).

## Examples

- AML quizartinib resistance: a FLT3 missense mutation co-detected with upregulation of AXL signal transduction in the same cell ([[10-Summaries/marks-2023-resolveome]]).
- Primary breast cancer: oncogenic PIK3CA N345K plus heterogeneous chromosomal loss, interpreted through same-cell transcriptomic identity ([[10-Summaries/marks-2023-resolveome]]).

## Related

- [[pta]] — the WGA chemistry underpinning the genome arm
- [[scdna-capabilities-framework]] — ResolveOME = fidelity + co-presence + RNA association
- [[got-cha]] — targeted genotype + chromatin alternative; ResolveOME is genome-wide genotype + RNA
- [[sctrio-seq]] — CNV + methylation + RNA precedent; ResolveOME swaps methylation for genome-wide SNV
- [[scwga]]
- [[40-Topics/single-cell-multiomics]]
- [[40-Topics/scdna-cancer-applications]]
- [[20-Entities/charles-gawad]]
