---
type: concept
title: Highly repetitive regions (HRRs)
aliases: [HRR, repetitive DNA, satellite repeats]
tags: [genomics, repeats, centromeres, telomeres, rDNA, long-read]
created: 2026-05-12
updated: 2026-10-08
---

# Highly repetitive regions (HRRs)

> Genomic regions composed of tandem or interspersed repetitive sequences — centromeres (alpha-satellite in human, CEN180 in *Arabidopsis*), telomeres, rDNA arrays, segmental duplications. Short-read sequencing cannot uniquely map within HRRs; long-read sequencing is essential.

## Definition

HRRs include constitutive heterochromatin at centromeres, the ~5–15 kb telomere repeats (TTAGGG)ₙ, the 45S rDNA arrays at nucleolar organizer regions, and segmental duplications scattered through euchromatin.

## Why it matters

- Telomere-to-telomere genome assemblies (CHM13 for human, Col-CEN/Col-PEK for *Arabidopsis*) revealed HRR sequence for the first time.
- HRR epigenetic profiling (methylation, accessibility) was a blind spot of short-read methods.
- Long-read methods like [[30-Concepts/stam-seq]] and adaptive sampling now enable single-molecule HRR analysis.

## Added 2026-10-07

Single-cell HiFi data resolved variation that short reads miss: 284k high-confidence SNVs per cell escaped Illumina bulk calling (6336 of them in health-relevant 'dark' genic regions such as *NBPF8* and *CDC73*), and on average 4770 tandem-repeat alleles per cell were genotyped consistently with bulk ([[10-Summaries/hard-2023-long-read-scwgs]]).


## Added 2026-10-08 — sequence models & foundation models

- Training a DNA language model on whole eukaryotic genomes rather than annotated gene loci gave lower pre-training loss but worse downstream performance, because repeats, homopolymers and N runs are easy to predict and depress loss without carrying functional signal ([[10-Summaries/li-2026-generator]]).
- Genos filtered sequence far from gene boundaries during its first pre-training stage but removed all such filtering for its 2.6-trillion-token continued pre-training, deliberately exposing the model to distal intergenic regions, segmental duplications and transposable elements ([[10-Summaries/lin-2025-genos]]).

## Related

- [[40-Topics/long-read-sequencing]] · [[30-Concepts/nanopore-adaptive-sampling]] · [[40-Topics/long-read-sequencing]]
