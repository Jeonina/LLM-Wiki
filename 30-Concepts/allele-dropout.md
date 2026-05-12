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
- MDA suffers high ADO rates; PTA's quasi-linear amplification reduces it substantially ([[10-Summaries/diane-2025-naturereviewsgenetics]]).
- Variant callers like [[30-Concepts/scout-variant-caller]] flag potential ADO loci based on local context.

## Related

- [[30-Concepts/scwga]] · [[30-Concepts/mda]] · [[30-Concepts/pta]] · [[30-Concepts/scout-variant-caller]] · [[40-Topics/whole-genome-amplification]]
