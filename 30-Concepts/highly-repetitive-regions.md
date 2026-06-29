---
type: concept
title: Highly repetitive regions (HRRs)
aliases: [HRR, repetitive DNA, satellite repeats]
tags: [genomics, repeats, centromeres, telomeres, rDNA, long-read]
created: 2026-05-12
updated: 2026-05-12
---

# Highly repetitive regions (HRRs)

> Genomic regions composed of tandem or interspersed repetitive sequences — centromeres (alpha-satellite in human, CEN180 in *Arabidopsis*), telomeres, rDNA arrays, segmental duplications. Short-read sequencing cannot uniquely map within HRRs; long-read sequencing is essential.

## Definition

HRRs include constitutive heterochromatin at centromeres, the ~5–15 kb telomere repeats (TTAGGG)ₙ, the 45S rDNA arrays at nucleolar organizer regions, and segmental duplications scattered through euchromatin.

## Why it matters

- Telomere-to-telomere genome assemblies (CHM13 for human, Col-CEN/Col-PEK for *Arabidopsis*) revealed HRR sequence for the first time.
- HRR epigenetic profiling (methylation, accessibility) was a blind spot of short-read methods.
- Long-read methods like [[30-Concepts/stam-seq]] and adaptive sampling now enable single-molecule HRR analysis.

## Related

- [[40-Topics/long-read-sequencing]] · [[30-Concepts/nanopore-adaptive-sampling]] · [[40-Topics/long-read-sequencing]]
