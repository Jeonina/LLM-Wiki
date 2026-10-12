---
type: concept
title: Allele-specific methylation
aliases: [ASM, ASM-QTL]
tags: [methylation, haplotype, imprinting, long-read]
created: 2026-05-12
updated: 2026-10-12
---

# Allele-specific methylation (ASM)

> Differential DNA methylation between the two parental alleles at the same locus. Arises from genomic imprinting, X-inactivation, or **sequence-context-driven** methylation differences linked to nearby SNVs (ASM-QTLs) ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu 2025]]).

> [!abstract] 한눈에
> ASM은 같은 locus에서 두 부모 allele의 DNA 메틸화가 서로 다른 현상이며, 검출하려면 haplotype이 phasing된 read가 필요하다. long-read는 이를 직접 읽고, short-read bisulfite와 single-cell 방법은 Bis-SNP나 scDEEP-mC 같은 별도 분석으로 접근한다 ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu 2025]]; [[10-Summaries/liu-2012-bis-snp|Bis-SNP]]; [[10-Summaries/spix-2025-scdeep-mc|scDEEP-mC]]).

## Definition

Detection requires haplotype-phased reads. Long-read sequencing (PacBio, ONT) spans haplotype blocks and identifies ASM directly; short-read bisulfite requires special pipelines for ASM at known heterozygous sites ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu 2025]]).

**Short-read routes to ASM.** Bis-SNP calls heterozygous SNPs (including C/T) directly from bisulfite reads, enabling ASM analysis without a separate genotyping assay ([[10-Summaries/liu-2012-bis-snp|Bis-SNP]]). In single cells, scDEEP-mC produces ~1 million allele-resolved CpGs per cell (~10,000 with both strands, allowing hemi-methylation), resolves imprinted *Gnas* DMRs from one cell, and infers X-inactivation state by rank-2 NMF even without phased SNPs (R² = 0.99 vs ground truth) ([[10-Summaries/spix-2025-scdeep-mc|scDEEP-mC]]).

## Why it matters

ASM-QTLs are emerging as a regulatory mechanism for expression variability. A deCODE genetics study (cited in [[10-Summaries/liu-2025-long-read-epigenome-review|Liu 2025]]) identified ASM-QTLs as drivers of expression variability in cis-regulatory regions for hematological traits.

## Related

> [!cards]
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — PacBio and ONT reads that span haplotype blocks.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — Methylation biology and methylome methods.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/liu-2012-bis-snp|Liu 2012]]
> - [[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]]
> - [[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]
