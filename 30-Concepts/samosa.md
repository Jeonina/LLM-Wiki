---
type: concept
title: SAMOSA
aliases: [single-molecule adenine-methylated oligonucleosome sequencing assay]
tags: [PacBio, chromatin-accessibility, single-molecule, EcoGII, Ramani-lab]
created: 2026-05-12
updated: 2026-10-12
---

# SAMOSA

> A single-molecule chromatin-accessibility method developed by the Ramani lab that uses in-nucleus EcoGII methyltransferase to mark accessible (nucleosome-free) regions with 6mA, then PacBio sequencing to read accessibility patterns along kilobase-length single fibers.

> [!abstract] 한눈에
> SAMOSA는 EcoGII로 accessible DNA에 6mA를 표시하고 PacBio로 읽어 kilobase 길이의 단일 fiber에서 nucleosome 배치를 보는 방법이다. 원 논문 protocol은 MNase로 풀어낸 oligonucleosome을 methylation하므로 nucleosome register는 잡지만 TF footprint는 잡지 못한다 ([[10-Summaries/abdulhay-2020-samosa|Abdulhay 2020]]).

## Definition

EcoGII non-specifically methylates A bases in accessible regions; protected (nucleosome- or TF-bound) regions remain unmodified. PacBio detects 6mA via polymerase-kinetic signatures.

**Correction from the full text:** in the original SAMOSA protocol EcoGII methylates oligonucleosomes after MNase release from nuclei (fragments ~500 bp–2 kb), so it captures nucleosome registers but not TF footprints; input was 100 × 10⁶ K562 cells ([[10-Summaries/abdulhay-2020-samosa|Abdulhay 2020]]). Its Results show H3K36me3 enriched for irregular and short regular fibres, which runs against the Introduction's framing of long regular arrays in elongating chromatin ([[10-Summaries/abdulhay-2020-samosa|Abdulhay 2020]]).

## Why it matters

- Single-fiber chromatin maps reveal co-occurrence of nucleosomes, TF binding, and CpG methylation on the same molecule.
- Bulk-only by default; [[30-Concepts/samosa-tag]] reduces input via tagmentation.

## Related

> [!cards]
> - `concept` [[30-Concepts/samosa-tag|SAMOSA-Tag]] — Low-input SAMOSA via SMRT-Tag tagmentation, from 30k–50k nuclei.
> - `concept` [[30-Concepts/fiber-seq|Fiber-seq]] — m6A stencilling of protein occupancy on chromatin fibers.
> - `concept` [[30-Concepts/single-molecule-footprinting|Single-molecule footprinting]] — The class of per-fiber accessibility assays read by long reads.
> - `concept` [[30-Concepts/pacbio|PacBio]] — Single-molecule real-time long-read sequencing platform.
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — PacBio HiFi and ONT reads of kilobases or longer.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/abdulhay-2020-samosa|Abdulhay 2020]]
