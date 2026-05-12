---
type: concept
title: SCOUT (Single Cell Genotyper Utilizing Information from Local Genome Territory)
aliases: [SCOUT]
tags: [single-cell, variant-calling, scWGA, software]
created: 2026-05-12
updated: 2026-05-12
---

# SCOUT

> A single-cell SNV caller (Tu et al. 2021) that classifies each candidate locus into homozygous, heterozygous, intermediate, or low-major-allele states using a four-component multinomial model that borrows information from **adjacent loci within the same cell** (local-territory smoothing).

## Definition

For each candidate SNV at locus *s*, SCOUT estimates the multinomial allele-success probability *p* and the latent genotype *Z_s* ∈ {0,1,2,3} by fitting a model that pools information from neighboring SNVs (30 kb window) with exponentially decaying weights.

## Why it matters

- Independent of external bulk data — important for minor-clone variants or rare mutations not in bulk reference.
- 2–77.5% F1 improvement over GATK, SCcaller, Monovar.
- 400% faster than alternative single-cell callers.

## Examples

- [[10-Summaries/accurate-single-cell-genotyping-utilizing-information-from-the-local-genome-territory]].

## Related

- [[30-Concepts/monovar]] · [[30-Concepts/sccaller]] · [[30-Concepts/allele-dropout]] · [[30-Concepts/scwga]] · [[40-Topics/scdna-seq]]
