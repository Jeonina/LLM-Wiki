---
type: concept
title: TAPS
aliases: [TET-assisted pyridine borane sequencing]
tags: [methylation, bisulfite-free, 5mC, TET, base-resolution]
created: 2026-05-12
updated: 2026-10-12
---

# TAPS

> A bisulfite-free chemistry that detects 5mC at single-base resolution by **TET oxidation of 5mC to 5caC**, then **pyridine-borane reduction of 5caC to DHU** (which reads as T); developed by the [[chun-xiao-song|Chun-Xiao Song]] lab and used in scEpi²-seq and other methods that need to preserve DNA integrity ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]; [[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]).

> [!abstract] 한눈에
> TAPS는 TET로 5mC를 5caC까지 산화한 뒤 pyridine borane으로 환원해, 수식된 염기만 T로 읽히게 하는 bisulfite-free 5mC 검출 화학이다. DNA를 거의 손상시키지 않아 single-cell barcode가 살아남지만, 단독으로는 5mC와 5hmC를 구별하지 못한다 ([[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]; [[10-Summaries/bai-2024-simple-seq|Bai 2024]]).

## Definition

Sequential enzymatic + chemical reactions: [[tet-enzymes|TET enzymes]] oxidize 5mC → 5fC → 5caC → (borane reduction) → DHU; the unmodified C remains unchanged, and the modified base is the one converted ([[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]). TET-mediated oxidation of 5mC to [[5hmc|5hmC]] was first shown for TET1 ([[10-Summaries/tahiliani-2009-tet1-5hmc|Tahiliani 2009]]). After PCR, 5mC sites appear as C→T conversions, but **DNA is not degraded** as it is by [[bisulfite-sequencing|bisulfite]] ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]; [[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]).

## Why it matters

Bisulfite degrades up to 90% of input DNA and destroys the small fragments and cell-barcode adaptors used in single-cell methods that ligate barcodes before conversion; TAPS preserves them, which is what lets scEpi²-seq read histone marks and 5mC together ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).

## Methods built on TAPS

| Method | What TAPS is paired with | What it adds | Source |
|---|---|---|---|
| scEpi²-seq | sortChIC histone-mark profiling | Joint single-cell methylation + histone-mark profiling | ([[10-Summaries/geisenberger-2025-scepi2-seq\|Geisenberger 2025]]) |
| [[simple-seq\|SIMPLE-seq]] | hmC-CATCH 5hmC labeling | TAPS labels 5mC; 5mC and 5hmC from the same molecule | ([[10-Summaries/bai-2024-simple-seq\|Bai 2024]]) |
| scTAPS / scCAPS+ | Barcoded Tn5 fragmentation, pooling of 96 barcoded cells *before* the conversion chemistry | TAPS and CAPS+ chemistry in single cells | ([[10-Summaries/chen-2025-sctaps-sccaps-plus\|Chen 2025]]) |

EM-seq is the fully enzymatic counterpart: TET2 and T4-BGT protect 5mC/5hmC and APOBEC3A deaminates unmodified C, so modified bases read as C as in bisulfite data and existing pipelines apply unchanged, unlike TAPS, whose modified bases read as T ([[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]).

## Evidence and examples

- **Direct conversion preserves complexity.** TAPS converts the modified base (5mC/5hmC → T) rather than unmodified cytosine, so mapping reaches 93.0% (scTAPS) and 89.4% (scCAPS+) ([[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]).
- **Quantified accuracy.** Spike-in conversion rates: scTAPS 5mCG 96.6% / 5hmCG 85.0%; scCAPS+ 5hmCG 93.0%. False positives 0.19% and 0.38% on unmodified C, and 0.25% on 5mCG for scCAPS+ ([[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]).
- **Depth over throughput.** 2.0–2.3 M CpG sites covered per cell (8.08–10.88% of all CpGs), against 1.96%/0.79% for the higher-throughput SIMPLE-seq, which also needs a standard curve to correct its ~87% 5mC conversion ([[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]).

## Contested points

- TAPS does not distinguish 5mC from 5hmC alone; pairing with hmC-CATCH (in SIMPLE-seq) or with sequential blocking can resolve them ([[10-Summaries/bai-2024-simple-seq|Bai 2024]]; [[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]).
- scTAPS/scCAPS+ trade throughput for per-cell CpG depth relative to SIMPLE-seq ([[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/bisulfite-sequencing|Bisulfite sequencing]] — The standard methylation chemistry TAPS replaces.
> - `concept` [[30-Concepts/5hmc|5hmC]] — The oxidative intermediate TET enzymes make from 5mC.
> - `concept` [[30-Concepts/tet-enzymes|TET enzymes]] — Dioxygenases that oxidize 5mC to 5hmC and onward.
> - `concept` [[30-Concepts/simple-seq|SIMPLE-seq]] — Joint single-cell 5mC and 5hmC built on TAPS chemistry.
> - `entity` [[20-Entities/chun-xiao-song|Chun-Xiao Song]] — Oxford (Ludwig); developer of TAPS.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC biology and the methods that measure it.

## All sources on this page

> [!info]- 5 summaries cited here
> - [[10-Summaries/bai-2024-simple-seq|Bai 2024]]
> - [[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]
> - [[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]
> - [[10-Summaries/tahiliani-2009-tet1-5hmc|Tahiliani 2009]]
> - [[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]
