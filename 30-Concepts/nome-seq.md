---
type: concept
title: NOMe-seq
aliases: [nucleosome occupancy and methylome sequencing, GpC methylation]
tags: [methylation, chromatin-accessibility, GpC, M.CviPI]
created: 2026-05-12
updated: 2026-10-12
---

# NOMe-seq

> Nucleosome Occupancy and Methylome sequencing. Uses the M.CviPI methyltransferase to deposit exogenous 5mC at accessible GpC dinucleotides, then bisulfite sequencing distinguishes endogenous CpG methylation from exogenous GpC methylation (= chromatin accessibility) ([[10-Summaries/pott-2017-elife|Pott 2017]]).

> [!abstract] 한눈에
> NOMe-seq는 M.CviPI로 열린 GpC에 외부 메틸기를 붙인 뒤 bisulfite sequencing으로 내재 CpG methylation과 GpC 표지(accessibility)를 한 read에서 함께 읽는 방법이다 ([[10-Summaries/pott-2017-elife|Pott 2017]]). 단일세포판(scNOMe-seq, scCOOL-seq)이 있지만, 뇌나 ESC처럼 non-CG methylation이 많은 세포에서는 내재 methylation과 섞일 수 있어 Tn5 기반 대안도 쓰인다 ([[10-Summaries/ludwig-2019-sc-chromatin-modifications-review|Ludwig 2019]]; [[10-Summaries/nichols-2025-scimetv3|sciMETv3]]).

## Definition

GpC methylation marks open regions; CpG methylation is the endogenous epigenetic mark. Single read provides both readouts.

## Why it matters

- Single-fiber co-measurement of accessibility and methylation.
- Foundation for the methyltransferase-based accessibility readouts used in [[30-Concepts/samosa]], [[30-Concepts/fiber-seq]] (EcoGII variant), and [[30-Concepts/stam-seq]].

## Single-cell variants

| Assay | Readouts | Notes | Source |
|---|---|---|---|
| scNOMe-seq | GpC accessibility + endogenous CpG methylation | M.CviPI treatment of isolated nuclei before FACS sorting and bisulfite conversion | ([[10-Summaries/pott-2017-elife\|Pott 2017]]; [[10-Summaries/ludwig-2019-sc-chromatin-modifications-review\|Ludwig 2019]]) |
| scCOOL-seq | GpC footprints + endogenous CpG methylation after scBS-seq | Additionally yields CNV and ploidy in preimplantation embryos | ([[10-Summaries/ludwig-2019-sc-chromatin-modifications-review\|Ludwig 2019]]) |
| Camellia-seq | GpC accessibility + lineage barcode + RNA + methylation | Adds GpC accessibility to a lineage-barcode assay | ([[10-Summaries/li-2023-darlin\|Li 2023]]) |

Other single-cell variants: scNMT-seq and [[30-Concepts/splicool-seq|SpliCOOL-seq]].

## Evidence and examples

- scNOMe-seq covers ~2.9% of GpCs and ~3.6% of CpGs per cell ([[10-Summaries/pott-2017-elife|Pott 2017]]).
- Only 32–44% (GM12878) and 26–37% (K562) of covered DHSs were accessible in a given cell ([[10-Summaries/pott-2017-elife|Pott 2017]]).

## Contested points

- **GpC versus Tn5 accessibility.** sciMET+ATAC encodes accessibility by Tn5 insertion rather than GpC methylation, avoiding the confound of endogenous non-CG methylation in brain and ESCs and giving enough per-cell accessibility signal for cell-level ATAC analysis ([[10-Summaries/nichols-2025-scimetv3|sciMETv3]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — How open chromatin is defined and measured.
> - `concept` [[30-Concepts/splicool-seq|SpliCOOL-seq]] — Single-cell GpC/CpG assay variant.
> - `concept` [[30-Concepts/fiber-seq|Fiber-seq]] — Methyltransferase (6mA) footprinting on long single fibres.
> - `concept` [[30-Concepts/samosa|SAMOSA]] — Single-molecule methyltransferase footprinting of oligonucleosomes.
> - `concept` [[30-Concepts/stam-seq|STAM-seq]] — Nanopore accessibility and methylation on the same fibre.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — Methylation chemistry, assays and analysis.

## All sources on this page

> [!info]- 4 summaries cited here
> - [[10-Summaries/li-2023-darlin|Li 2023]]
> - [[10-Summaries/ludwig-2019-sc-chromatin-modifications-review|Ludwig & Bintu 2019]]
> - [[10-Summaries/nichols-2025-scimetv3|Nichols 2025]]
> - [[10-Summaries/pott-2017-elife|Pott 2017]]
