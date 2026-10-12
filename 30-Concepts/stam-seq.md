---
type: concept
title: STAM-seq
aliases: [single-molecule targeted accessibility and methylation sequencing]
tags: [long-read, nanopore, plants, centromeres, adaptive-sampling]
created: 2026-05-12
updated: 2026-10-12
---

# STAM-seq

> A long-read chromatin-accessibility + methylation method for plants developed by Mo et al. 2023 (Zhai lab). Uses EcoGII 6mA labeling of accessible regions + nanopore sequencing + adaptive sampling to enrich highly repetitive regions (centromeres, telomeres, rDNAs) ([[10-Summaries/mo-2023-stam-seq|Mo 2023]]).

> [!abstract] 한눈에
> STAM-seq는 EcoGII로 열린 DNA에 6mA를 찍고 nanopore adaptive sampling으로 centromere·telomere·rDNA 같은 고반복 영역을 골라 읽어, 한 섬유 위의 accessibility와 내재 5mC를 함께 얻는 식물용 방법이다. 식물 centromere의 단일 분자 chromatin 지도를 처음 제시했다 ([[10-Summaries/mo-2023-stam-seq|Mo 2023]]).

## Definition

Workflow: nuclei isolation → EcoGII 6mA methylation → nanopore sequencing with adaptive sampling targeting HRRs ± 100 kb flanking. Modification-aware basecalling distinguishes 6mA (accessibility) from endogenous 5mC (methylation) on the same fiber ([[10-Summaries/mo-2023-stam-seq|Mo 2023]]).

## Why it matters

- 4.8× HRR enrichment via adaptive sampling without prior capture or amplification ([[10-Summaries/mo-2023-stam-seq|Mo 2023]]).
- Reveals strand-specific accessibility at *Arabidopsis* CEN180 centromeric repeats ([[10-Summaries/mo-2023-stam-seq|Mo 2023]]).
- First single-molecule chromatin map of plant centromeres, telomeres, and rDNAs ([[10-Summaries/mo-2023-stam-seq|Mo 2023]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/nanopore-adaptive-sampling|Nanopore adaptive sampling]] — Real-time read selection that enriches target regions without capture.
> - `concept` [[30-Concepts/highly-repetitive-regions|Highly repetitive regions]] — Centromeres, telomeres, rDNA and other repeat-rich regions.
> - `concept` [[30-Concepts/samosa|SAMOSA]] — EcoGII footprinting of oligonucleosomes on PacBio.
> - `concept` [[30-Concepts/fiber-seq|Fiber-seq]] — m6A stenciling of chromatin fibers read on long reads.
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — Technologies that read kilobase-to-megabase single molecules.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/mo-2023-stam-seq|Mo 2023]]
