---
type: concept
title: Allele-specific methylation
aliases: [ASM, ASM-QTL]
tags: [methylation, haplotype, imprinting, long-read]
created: 2026-05-12
updated: 2026-10-07
---

# Allele-specific methylation (ASM)

> Differential DNA methylation between the two parental alleles at the same locus. Arises from genomic imprinting, X-inactivation, or **sequence-context-driven** methylation differences linked to nearby SNVs (ASM-QTLs).

## Definition

Detection requires haplotype-phased reads. Long-read sequencing (PacBio, ONT) spans haplotype blocks and identifies ASM directly; short-read bisulfite requires special pipelines for ASM at known heterozygous sites.

## Why it matters

ASM-QTLs are emerging as a regulatory mechanism for expression variability. A deCODE genetics study (cited in [[10-Summaries/liu-2025-long-read-epigenome-review]]) identified ASM-QTLs as drivers of expression variability in cis-regulatory regions for hematological traits.

## Added 2026-10-07

**Short-read routes to ASM.** Bis-SNP calls heterozygous SNPs (including C/T) directly from bisulfite reads, enabling ASM analysis without a separate genotyping assay ([[10-Summaries/liu-2012-bis-snp]]). In single cells, scDEEP-mC produces ~1 million allele-resolved CpGs per cell (~10,000 with both strands, allowing hemi-methylation), resolves imprinted *Gnas* DMRs from one cell, and infers X-inactivation state by rank-2 NMF even without phased SNPs (R² = 0.99 vs ground truth) ([[10-Summaries/spix-2025-scdeep-mc]]).


## Related

- [[40-Topics/long-read-sequencing]] · [[40-Topics/dna-methylation]] · [[40-Topics/long-read-sequencing]]
