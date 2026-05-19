---
type: concept
title: Allele-specific methylation
aliases: [ASM, ASM-QTL]
tags: [methylation, haplotype, imprinting, long-read]
created: 2026-05-12
updated: 2026-05-12
---

# Allele-specific methylation (ASM)

> Differential DNA methylation between the two parental alleles at the same locus. Arises from genomic imprinting, X-inactivation, or **sequence-context-driven** methylation differences linked to nearby SNVs (ASM-QTLs).

## Definition

Detection requires haplotype-phased reads. Long-read sequencing (PacBio, ONT) spans haplotype blocks and identifies ASM directly; short-read bisulfite requires special pipelines for ASM at known heterozygous sites.

## Why it matters

ASM-QTLs are emerging as a regulatory mechanism for expression variability. A deCODE genetics study (cited in [[10-Summaries/liu-2025-long-read-epigenome-review]]) identified ASM-QTLs as drivers of expression variability in cis-regulatory regions for hematological traits.

## Related

- [[30-Concepts/long-read-sequencing]] · [[30-Concepts/dna-methylation]] · [[40-Topics/long-read-sequencing]]
