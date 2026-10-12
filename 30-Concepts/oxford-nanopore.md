---
type: concept
title: Oxford Nanopore Technologies
aliases: [ONT, nanopore sequencing, nanopore]
tags: [long-read, sequencing, direct-RNA, methylation]
created: 2026-05-12
updated: 2026-10-12
---

# Oxford Nanopore Technologies (ONT)

> A long-read sequencing platform that threads native single DNA or RNA molecules through nanopores embedded in a membrane, reading sequence directly from changes in ionic current ("squiggles") as bases pass through. No amplification required; modifications detectable directly ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu 2025]]).

> [!abstract] 한눈에
> ONT는 native DNA·RNA 분자를 nanopore에 통과시키며 이온 전류 변화로 서열을 읽는 long-read 플랫폼이라, 증폭 없이 5mC·6mA 같은 변형을 직접 검출한다 ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu 2025]]). 단편 길이와 무관하게 긴 read를 읽을 수 있어 single-cell에서도 allele-specific accessibility, multi-way 3D 접촉, 전장 전사체를 한 라이브러리에서 얻는 데 쓰인다 ([[10-Summaries/li-2025-scnanoatac-seq2|scNanoATAC-seq2]]; [[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]; [[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [Long-read 시퀀싱 교재](../60-Explainers/long-read-sequencing.html)
<!-- /explainer-links -->

## Definition

ONT instruments range from portable MinION/Flongle to PromethION. Read lengths routinely 10–100 kb; ultra-long reads reach >1 Mb. Accuracy improved from ~85% (R7) to >99% (R10.4.1). Adaptive sampling enables real-time read selection ([[30-Concepts/nanopore-adaptive-sampling|adaptive sampling]]).

## Why it matters

- Direct detection of 5mC, 5hmC, 6mA, 4mC via current-signature modeling (Nanopolish → Dorado/Remora) ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu 2025]]).
- Telomere-to-telomere genome assemblies (CHM13).
- Real-time targeted sequencing via adaptive sampling enables HRR-focused experiments ([[10-Summaries/mo-2023-stam-seq|STAM-seq]]).

## Applications

| Application | Assay | What nanopore reads add | Source |
|---|---|---|---|
| Epigenomics of plant HRRs | STAM-seq | Adaptive sampling for centromere/telomere/rDNA epigenomics | ([[10-Summaries/mo-2023-stam-seq\|STAM-seq]]) |
| Somatic SV detection | — | Long reads for somatic SVs in laryngeal squamous carcinoma | ([[10-Summaries/liu-2025-nanopore-lscc-svs\|Liu 2025 (LSCC)]]) |
| Epigenome profiling (review) | — | ONT epigenomics reviewed | ([[10-Summaries/liu-2025-long-read-epigenome-review\|Liu 2025]]) |
| Allele-specific single-cell accessibility | scNanoATAC-seq2 | Long reads tag alleles for imprinting and X-inactivation analysis | ([[10-Summaries/li-2025-scnanoatac-seq2\|scNanoATAC-seq2]]) |
| Single-cell multi-way 3D genome | scNanoHi-C | Reads ~3-kb amplicons of Hi-C concatemers | ([[10-Summaries/li-2023-scnanohi-c\|scNanoHi-C]]) |
| Single-cell genome + accessibility + full-length transcripts | SPLONGGET | Reads a 200 bp to >10 kb DNA library independent of fragment length | ([[10-Summaries/pancikova-2025-splongget\|SPLONGGET]]) |

## Evidence and examples

- scNanoATAC-seq2 yields allele-tagging rates of 96.8% in C57×CAST and 47% in C57×DBA embryos, enabling allele-specific accessibility analysis of imprinting and X inactivation at single-cell resolution ([[10-Summaries/li-2025-scnanoatac-seq2|scNanoATAC-seq2]]).
- scNanoHi-C runs on PromethION R9.4.1 at ~USD 3 per cell when ~500 cells share a run ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).
- SPLONGGET couples 10x Genomics barcoding with Nanopore sequencing, retaining all tagmentation fragments so that one single-cell library yields whole-genome coverage, chromatin accessibility and full-length transcripts ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).
- SPLONGGET gives 79–93% of the genome at ≥5× per time-point library versus 6% for the same library read with short reads ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).
- Applied to one paediatric B-ALL across four time points, SPLONGGET reports parallel CD19 immune-escape evolution (preprint) ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).

## Contested points

- The SPLONGGET findings come from a preprint and a single patient, so they await peer-reviewed replication (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/nanopore-adaptive-sampling|Nanopore adaptive sampling]] — Real-time rejection of non-target reads.
> - `concept` [[30-Concepts/pacbio|PacBio]] — The other long-read platform, with kinetic modification detection.
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — Long-read platforms and what they measure.

## All sources on this page

> [!info]- 6 summaries cited here
> - [[10-Summaries/li-2023-scnanohi-c|Li 2023]]
> - [[10-Summaries/li-2025-scnanoatac-seq2|Li 2025]]
> - [[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]]
> - [[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]
> - [[10-Summaries/mo-2023-stam-seq|Mo 2023]]
> - [[10-Summaries/pancikova-2025-splongget|Pančíková 2025 (bioRxiv preprint)]]
