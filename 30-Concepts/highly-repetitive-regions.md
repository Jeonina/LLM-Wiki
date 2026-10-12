---
type: concept
title: Highly repetitive regions (HRRs)
aliases: [HRR, repetitive DNA, satellite repeats]
tags: [genomics, repeats, centromeres, telomeres, rDNA, long-read]
created: 2026-05-12
updated: 2026-10-12
---

# Highly repetitive regions (HRRs)

> Genomic regions composed of tandem or interspersed repetitive sequences — centromeres (alpha-satellite in human, CEN180 in *Arabidopsis*), telomeres, rDNA arrays, segmental duplications — that short-read sequencing cannot uniquely map, so long-read sequencing is essential ([[10-Summaries/mo-2023-stam-seq|STAM-seq]]).

> [!abstract] 한눈에
> HRR은 centromere, telomere, rDNA array, segmental duplication처럼 반복 서열로 이루어진 영역으로, short read로는 고유하게 mapping되지 않아 long read가 필요하다 ([[10-Summaries/mo-2023-stam-seq|STAM-seq]]). single-cell HiFi는 short read가 놓치는 변이를 이 영역에서 찾아냈고, DNA language model 학습에서는 반복 서열을 넣을지가 설계 선택이 된다 ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]; [[10-Summaries/li-2026-generator|GENERator]]).

## Definition

HRRs include constitutive heterochromatin at centromeres, the ~5–15 kb telomere repeats (TTAGGG)ₙ, the 45S rDNA arrays at nucleolar organizer regions, and segmental duplications scattered through euchromatin (synthesis).

## Why it matters

- Telomere-to-telomere genome assemblies (CHM13 for human, Col-CEN/Col-PEK for *Arabidopsis*) revealed HRR sequence for the first time (synthesis; Col-CEN/Col-PEK used in [[10-Summaries/mo-2023-stam-seq|STAM-seq]]).
- HRR epigenetic profiling (methylation, accessibility) was a blind spot of short-read methods ([[10-Summaries/mo-2023-stam-seq|STAM-seq]]).
- Long-read methods like [[30-Concepts/stam-seq]] and [[30-Concepts/nanopore-adaptive-sampling|adaptive sampling]] now enable single-molecule HRR analysis ([[10-Summaries/mo-2023-stam-seq|STAM-seq]]).

## Evidence and examples

**Variant calling with single-cell long reads**

- Single-cell HiFi data found 284k high-confidence SNVs per cell that escaped Illumina bulk calling, 6336 of them in health-relevant 'dark' genic regions such as *NBPF8* and *CDC73* ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).
- On average 4770 tandem-repeat alleles per cell were genotyped consistently with bulk ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).

**Repeats in DNA language-model training**

- Training a DNA language model on whole eukaryotic genomes rather than annotated gene loci gave lower pre-training loss but worse downstream performance, because repeats, homopolymers and N runs are easy to predict and depress loss without carrying functional signal ([[10-Summaries/li-2026-generator|GENERator]]).
- Genos filtered sequence far from gene boundaries during its first pre-training stage but removed all such filtering for its 2.6-trillion-token continued pre-training, deliberately exposing the model to distal intergenic regions, segmental duplications and transposable elements ([[10-Summaries/lin-2025-genos|Genos]]).

## Contested points

- **Include or exclude repeats in pre-training?** GENERator found whole-genome training with repeats hurt downstream performance ([[10-Summaries/li-2026-generator|GENERator]]), while Genos deliberately exposed its model to segmental duplications and transposable elements in continued pre-training ([[10-Summaries/lin-2025-genos|Genos]]); the two report different designs rather than a head-to-head test (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/stam-seq|STAM-seq]] — Long-read accessibility and methylation profiling of plant centromeres, telomeres and rDNA.
> - `concept` [[30-Concepts/nanopore-adaptive-sampling|Nanopore adaptive sampling]] — Real-time read rejection that enriches target regions such as HRRs.
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — PacBio HiFi and nanopore reads long enough to span repeats.

## All sources on this page

> [!info]- 4 summaries cited here
> - [[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]
> - [[10-Summaries/li-2026-generator|GENERator 2026]]
> - [[10-Summaries/lin-2025-genos|Genos 2026]]
> - [[10-Summaries/mo-2023-stam-seq|Mo 2023]]
