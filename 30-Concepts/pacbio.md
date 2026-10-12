---
type: concept
title: PacBio
aliases: [Pacific Biosciences, SMRT sequencing]
tags: [long-read, sequencing, HiFi, methylation]
created: 2026-05-12
updated: 2026-10-12
---

# PacBio (Pacific Biosciences) SMRT sequencing

> A long-read sequencing platform based on **single-molecule real-time (SMRT)** observation of DNA polymerase incorporating fluorescent nucleotides into a single template held in a zero-mode waveguide (ZMW). Circular consensus sequencing (CCS) reads multiple passes of the same circularized molecule and consensus-calls for high accuracy.

> [!abstract] 한눈에
> PacBio는 ZMW 안에서 polymerase가 형광 nucleotide를 붙이는 과정을 실시간으로 관찰하는 long-read 플랫폼이고, 같은 분자를 여러 번 읽어 정확도를 높이며 kinetic 신호로 5mC·6mA를 별도 처리 없이 검출한다 ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu 2025]]). 증폭한 단일 세포에도 적용되어, Illumina 데이터의 32% 양으로 germline SNV를 더 정밀하게 잡았다 ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [Long-read 시퀀싱 교재](../60-Explainers/long-read-sequencing.html)
<!-- /explainer-links -->

## Definition

PacBio Sequel II/IIe/Revio instruments. **HiFi reads**: ≥5 CCS passes yields >99% per-read accuracy. Read length 5–20 kb. Kinetic signatures (interpulse distance, pulse width) detect 5mC and 6mA without separate library prep ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu 2025]]).

## Why it matters

- Direct methylation detection via kinetic analysis (Primrose for 5mC, Fibertools for 6mA) ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu 2025]]).
- PCR-free workflows preserve native modifications ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu 2025]]).
- High accuracy plus long reads make PacBio HiFi the de facto standard for clinical-grade variant calling and genome assembly.

## Applications

- DAF-seq / scDAF-seq ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).
- SAMOSA ([[10-Summaries/abdulhay-2020-samosa|SAMOSA]]).
- PacBio epigenomics is reviewed in [[10-Summaries/liu-2025-long-read-epigenome-review|Liu 2025]].
- Single-cell WGS of dMDA-amplified cells ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).

## Evidence and examples

- PacBio HiFi has been applied to amplified single human cells: five dMDA-amplified T cells gave up to 20 Gb of HiFi data (>QV20) per cell from one 8M SMRT cell and up to 40% genome coverage ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).
- With 32% of the Illumina data volume, single-cell HiFi SNV calling matched Illumina germline SNV yield with higher precision (0.86 vs 0.74) ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/oxford-nanopore|Oxford Nanopore Technologies]] — The other long-read platform, reading ionic current.
> - `concept` [[30-Concepts/single-molecule-footprinting|Single-molecule chromatin footprinting]] — Methyltransferase or deaminase marks read on single fibres.
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — Long-read platforms and what they measure.

## All sources on this page

> [!info]- 4 summaries cited here
> - [[10-Summaries/abdulhay-2020-samosa|Abdulhay 2020]]
> - [[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]
> - [[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
