---
type: concept
title: DEFND-seq
aliases: [DEFND-seq, DNA and Expression Following Nucleosome Depletion]
tags: [single-cell-multiomics, DNA-RNA-coassay, nucleosome-depletion, 10x-genomics]
created: 2026-06-02
updated: 2026-10-12
---

# DEFND-seq

> A scalable droplet method for co-sequencing genomic DNA and RNA from the same single nucleus, by depleting nucleosomes and then running the nuclei through the **stock 10x Genomics Multiome (ATAC+GEX) kit** ([[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]).

> [!abstract] 한눈에
> DEFND-seq는 nucleosome을 제거한 핵을 수정하지 않은 10x Multiome kit에 넣어, 한 핵에서 whole-genome DNA와 mRNA를 함께 읽는 droplet 방법이다 ([[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]). 범용 10x 장비로 규모를 키울 수 있지만, targeted 방법인 SDR-seq에 비해 allelic dropout이 높다는 trade-off가 있다 ([[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]).

## Definition

DEFND-seq (DNA and Expression Following Nucleosome Depletion) treats nuclei with lithium diiodosalicylate (the LAND method) to strip nucleosomes, exposing the genome so [[30-Concepts/tn5-tagmentation|Tn5]] tagments it uniformly rather than only at open chromatin ([[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]). The depleted nuclei then go through unmodified 10x Multiome microfluidics, yielding one mRNA library and one whole-genome gDNA library per nucleus ([[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]).

## Why it matters

- Repurposes a chromatin-accessibility platform into a genome+transcriptome co-assay on widely available 10x hardware with commercial kits — broad accessibility without new instruments ([[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]).
- Achieves coverage uniformity (100-kb CV ~0.6) comparable to dedicated scDNA methods like [[30-Concepts/pta|PTA]] and MDA but at >200× fewer reads per cell, while also reading RNA ([[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]).
- Library cost ~US$0.56/cell, scalable to ~40k nuclei per chip ([[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]).

## How it compares

- **Nucleosome-depletion chemistry:** LAND beats crosslink+SDS (xSDS), giving more complex libraries, more uniform coverage and full-length cDNA (xSDS truncates cDNA) ([[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]).
- **Against split-pool co-assays:** higher unique transcripts and fragments than the scalable split-pool sci-L3 co-assay at matched depth ([[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]).
- **Against targeted droplet co-assays:** **whole-genome but high-ADO**, in contrast to the **targeted, low-ADO** [[30-Concepts/sdr-seq|SDR-seq]] ([[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]); see [[50-Notes/droplet-vs-single-molecule-scdna]].

## Evidence and examples

- In glioblastoma, DEFND-seq linked focal *EGFR* amplification to one subclone and focal *PDGFRA* amplification to an OPC-like proneural RNA cluster, recapitulating the TCGA PDGFRA–proneural association at single-cell resolution ([[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]).
- It detected somatic SNVs (*EGFR*, *MAP2K3*, *PREX1*) and worked on >4-year cryopreserved tissue ([[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/joint-single-cell-multi-omics|Joint single-cell multi-omics]] — Measuring two or more modalities from the same cell rather than integrating separate datasets.
> - `concept` [[30-Concepts/sdr-seq|SDR-seq]] — Targeted droplet DNA+RNA method; the low-ADO counterpart to DEFND-seq.
> - `concept` [[30-Concepts/gt-seq|G&T-seq]] — Plate-based DNA+RNA method that physically separates mRNA from gDNA.
> - `concept` [[30-Concepts/dr-seq|DR-seq]] — One-pot DNA+RNA assay using quasilinear amplification of both.
> - `concept` [[30-Concepts/tn5-tagmentation|Tn5 tagmentation]] — Simultaneous fragmentation and adapter insertion by Tn5.
> - `concept` [[30-Concepts/pta|PTA]] — Primary template amplification, a dedicated scWGA comparator.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multi-omics]] — Methods that measure two or more modalities in the same cell.
> - `hub` [[40-Topics/scdna-cancer-applications|scDNA-seq in cancer applications]] — Intratumor heterogeneity, chemoresistance and clonal tools in cancer.

People: [[20-Entities/peter-a-sims]].

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]
> - [[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]
