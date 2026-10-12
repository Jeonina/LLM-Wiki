---
type: concept
title: µATAC-seq
aliases: [micro-ATAC-seq, nano-well scATAC]
tags: [scATAC-seq, throughput, ICELL8, Greenleaf-lab]
created: 2026-05-12
updated: 2026-10-12
---

# µATAC-seq

> A high-throughput single-cell ATAC-seq implementation on the Takara ICELL8 5,184-nanowell platform. Integrates Hoechst/PI fluorescence imaging for live-cell QC before reagent deposition. ~1,800 cells/chip at ~$0.81/cell library cost ([[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]).

> [!abstract] 한눈에
> µATAC-seq는 ICELL8 5,184-nanowell chip에서 형광 imaging으로 살아 있는 단일 세포 well을 고른 뒤 Tn5 반응을 하는 scATAC-seq 구현이다. Chip당 약 1,800개 세포를 세포당 약 $0.81에 처리한다 ([[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]).

## Definition

Workflow: cells loaded under Poisson dilution → imaged for live single-cell wells → Tn5 transposition (40 nl per well) → EDTA quench → MgCl₂ neutralization → indexed PCR amplification → off-chip extraction by centrifugation ([[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]).

## Why it matters

- ~20-fold throughput improvement over Fluidigm C1 at lower per-cell cost ([[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]).
- Live-cell imaging compatibility enables multi-omic integration that combinatorial-indexing lacks ([[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]).
- Per-cell fragment yield (~14k) higher than combinatorial-indexing methods ([[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]).

## Examples

- 2,333 PBMCs from 3 donors → de novo clustering by hematopoietic cell type with PU.1, C/EBPα, RUNX1 motifs differential ([[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Genome-wide chromatin accessibility in individual cells via Tn5 insertion.
> - `concept` [[30-Concepts/icell8-nanowell|ICELL8 nanowell]] — Takara 5,184-nanowell dispensing platform with integrated imaging.
> - `concept` [[30-Concepts/tn5-tagmentation|Tn5 tagmentation]] — Simultaneous fragmentation and adapter insertion by Tn5 transposase.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Assays and analysis for sparse per-cell accessibility data.
> - `entity` [[20-Entities/sandy-klemm|Sandy Klemm]] — Greenleaf-lab co-first author on µATAC-seq.
> - `entity` [[20-Entities/william-greenleaf|William Greenleaf]] — Stanford genome scientist; co-developer of ATAC-seq.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]
