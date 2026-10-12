---
type: concept
title: scEpi²-seq
aliases: [single-cell Epi² sequencing]
tags: [single-cell, multi-omics, histone-modifications, methylation, TAPS, sortChIC]
created: 2026-05-12
updated: 2026-10-12
---

# scEpi²-seq

> A single-cell multi-omics method that profiles a histone modification **and** DNA methylation **and** nucleosome positioning from the same cell. Combines sortChIC (pA-MNase + FACS) with TAPS conversion (bisulfite-free 5mC → uracil) ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).

> [!abstract] 한눈에
> scEpi²-seq는 sortChIC와 TAPS를 묶어 한 세포에서 histone modification, DNA methylation, nucleosome 위치를 함께 읽는 방법이다 ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]). bisulfite 대신 TAPS를 써서 barcoded adaptor를 살려 둔 것이 핵심이다 ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).

## Definition

Workflow: FACS-sort cells → bind to antibody-recruited pA-MNase → MNase digestion → adaptor ligation with cell-barcoded UMIs → pool → TAPS chemistry (without destroying barcoded adaptors, unlike bisulfite) → IVT/RT/PCR → Illumina sequencing ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]). Read-start distances reconstruct nucleosome positioning ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).

## Why it matters

- Bisulfite can't be combined with histone-modification adaptor-ligation workflows because it fragments DNA; TAPS preserves them ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).
- Joint per-cell readout of histone + methylation reveals mechanisms of methylation maintenance, such as nucleosome occupancy blocking DNMT1 ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).

## Evidence and examples

- Systems profiled: K562, RPE-1 hTERT FUCCI cells, mouse small intestine ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).
- Through S-phase, methylation drops by up to 12% at the nucleosome midpoint vs 4% at linker DNA — nucleosome occupancy blocks DNMT1 ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).
- Within H3K27me3 domains, 5mC differs between lineages at similar H3K27me3: B cells have the lowest H3K27me3 but the highest 5mC among immune cells, and goblet cells have higher 5mC than enteroendocrine cells ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).
- Methylation is therefore an **additive** regulatory layer over PRC2-marked facultative heterochromatin ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/sortchic|sortChIC]] — pA-MNase chromatin profiling of FACS-sorted single cells; the histone arm of scEpi²-seq.
> - `concept` [[30-Concepts/taps|TAPS]] — Bisulfite-free 5mC conversion that keeps barcoded adaptors intact.
> - `concept` [[30-Concepts/replication-timing|Replication timing]] — When genomic regions replicate in S-phase; late regions recover methylation last.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Single-cell profiling of histone marks.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — Methylation chemistry, assays and analysis.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Joint measurement of several layers in one cell.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]
