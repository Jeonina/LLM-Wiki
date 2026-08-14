---
type: concept
title: Allele dropout
aliases: [ADO]
tags: [single-cell, scWGA, amplification-bias]
created: 2026-05-12
updated: 2026-05-12
---

# Allele dropout (ADO)

> A failure mode of single-cell whole-genome amplification (scWGA) where one of the two parental alleles at a heterozygous locus fails to amplify, causing a heterozygous variant to appear homozygous in sequencing data.

## Definition

ADO arises during the earliest rounds of amplification when one strand or one parental molecule fails to template polymerase extension. Once the bias is established, it propagates through all subsequent cycles.

## Why it matters

- ADO is the primary source of false-negative SNV calls in scDNA-seq.
- MDA suffers high ADO rates; PTA's quasi-linear amplification reduces it substantially ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- Variant callers like [[30-Concepts/scout-variant-caller]] flag potential ADO loci based on local context.

## Related

- [[30-Concepts/scwga]] · [[30-Concepts/mda]] · [[30-Concepts/pta]] · [[30-Concepts/scout-variant-caller]] · [[40-Topics/whole-genome-amplification]]

## Added 2026-08-13

The most careful early ADO treatment in the corpus measures it **four independent ways** rather than assuming a literature value: TaqMan genotyping of 46 common-heterozygous loci, targeted resequencing of 96 such loci, wild-type-allele loss at called mutations, and the clone-inference model's own estimate of intraclonal dropout ([[10-Summaries/gawad-2014-all-clonal-origins]]). The first and third concurred at 23–24% median; resequencing read higher at 33%; after a 30% ADO filter the median fell to 20%. Primary patient samples ran modestly above the 15.6% of an LCL control ([[10-Summaries/gawad-2014-all-clonal-origins]]).

ADO directly limits clone detection: **ADO >0.3 or fewer than 10 mutations per sample causes clone-number underestimation** ([[10-Summaries/gawad-2014-all-clonal-origins]]).

Input copy number is the most direct lever on ADO. G2/M-sorted nuclei give four template copies per locus and drop ADO to **9.73 ± 2.19%**, versus 7–46% in prior MDA work ([[10-Summaries/wang-2014-nuc-seq]]).
