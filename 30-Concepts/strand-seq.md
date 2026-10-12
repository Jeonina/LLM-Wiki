---
type: concept
title: Strand-seq
aliases: [strand sequencing, BrdU-strand-seq]
tags: [scDNA-seq, structural-variants, haplotype, sister-chromatid]
created: 2026-05-19
updated: 2026-10-12
---

# Strand-seq

> Single-cell DNA sequencing method that distinguishes parental Watson and Crick strands by selectively sequencing one (BrdU-labeled) strand per chromosome per cell ([[10-Summaries/falconer-2012-natmethods|Falconer 2012]]). Enables high-resolution detection of structural variants, sister-chromatid exchanges, and haplotype phasing in single cells.

> [!abstract] 한눈에
> Strand-seq는 BrdU로 한 번 분열시킨 세포에서 새로 합성된 가닥을 제거하고 부모 가닥만 읽어, 염색체마다 어느 가닥을 물려받았는지를 단일 세포 수준에서 알아내는 방법이다. 이 정보로 inversion, translocation, sister-chromatid exchange를 찾고 haplotype을 phasing한다 ([[10-Summaries/falconer-2012-natmethods|Falconer 2012]]; [[10-Summaries/sanders-2020-sctrip|Sanders 2020]]).

## Method

Cells are grown for one division in BrdU-containing medium, then BrdU-labeled strands are selectively nicked. Sequencing of the surviving (parental) strand gives a per-cell strand inheritance pattern that reveals which chromatid each homolog inherited ([[10-Summaries/falconer-2012-natmethods|Falconer 2012]]).

## Applications

- Detection of inversions, translocations, and sister-chromatid exchanges at single-cell resolution ([[10-Summaries/sanders-2020-sctrip|Sanders 2020]]).
- Haplotype-resolved genome assembly ([[10-Summaries/falconer-2012-natmethods|Falconer 2012]]).
- Genome stability assays ([[10-Summaries/falconer-2012-natmethods|Falconer 2012]]).
- Standard processing workflow: MosaiCatcher v2 runs from raw Strand-seq FASTQ to haplotype-phased single-cell SV calls in one run, with automatic library QC, SV genotyping (ArbiGent) and nucleosome-occupancy functional analysis (scNOVA) ([[10-Summaries/weber-2023-mosaicatcher-v2|Weber 2023]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/structural-variants|Structural variants]] — Large genomic rearrangements: deletions, insertions, duplications, inversions, translocations.
> - `hub` [[40-Topics/scdna-seq|Single-cell DNA sequencing]] — Technologies that interrogate the DNA of single cells.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/falconer-2012-natmethods|Falconer 2012]]
> - [[10-Summaries/sanders-2020-sctrip|Sanders 2020]]
> - [[10-Summaries/weber-2023-mosaicatcher-v2|Weber 2023]]
