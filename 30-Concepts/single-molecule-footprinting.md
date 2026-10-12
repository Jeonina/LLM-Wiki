---
type: concept
title: Single-molecule chromatin footprinting
aliases: [single-molecule footprinting, single-fiber footprinting]
tags: [chromatin, single-molecule, method-class]
created: 2026-05-07
updated: 2026-10-12
paper_section: ["3.2.1"]
---

# Single-molecule chromatin footprinting

> A class of chromatin assays that mark accessible DNA on individual nuclear fibers (rather than across an ensemble) and read those marks with long-read sequencing, recovering per-fiber maps of nucleosome positioning, TF occupancy, and regulatory-element actuation ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).

> [!abstract] 한눈에
> Single-molecule footprinting은 한 DNA 분자 위에 열린 염기를 표지하고 분자 하나하나를 읽어, 그 분자에 단백질이 어떤 배치로 붙어 있었는지를 복원하는 방법군이다. m6A 표지는 증폭되면 지워져 bulk에 머물지만, deaminase가 남기는 C→T 표지는 서열 변화라 증폭을 견디고 single cell로 확장된다 ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]; [[10-Summaries/he-2024-foodie|He 2024]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [염색질 구조 교재](../60-Explainers/chromatin-architecture.html)
<!-- /explainer-links -->

## Definition

Population/ensemble assays — DNase-seq, ATAC-seq, ChIP-seq — average chromatin states across many cells and many fibers, smearing out cooperativity and per-fiber heterogeneity ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]). Single-molecule footprinting marks each fiber's accessible bases and sequences each fiber individually, so the *pattern* of marks along one DNA molecule reports the *configuration* of bound proteins on that molecule ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]] introduction).

Two main chemistries:

- **Methyltransferase stenciling** — m6A on accessible adenines ([[fiber-seq]]). m6A read natively on long reads is erased by amplification → bulk-only ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]); GpC methyltransferase marks read by bisulfite or EM-seq survive amplification and work in single cells ([[10-Summaries/pott-2017-elife|Pott 2017]]) and on short-read amplicons ([[10-Summaries/doughty-2024-smf-tf|Doughty 2024]]).
- **Deaminase stenciling** — C→T on accessible cytidines ([[daf-seq]]). Marks are sequence changes → survive amplification → single-cell-extensible ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).

## Why it matters

Aggregate chromatin assays cannot disentangle ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]):

- **TF cooperativity** (whether TFs bind together vs independently along the same fiber);
- **Haplotype-specific actuation** (whether the two homologous chromosomes within a cell carry different chromatin states);
- **Regulatory-element co-actuation domains** (whether two enhancers fire on the same fiber or different fibers).

These are precisely the readouts that single-molecule footprinting recovers, and the readouts on which DAF-seq reports surprising findings: a 180,000× cooperative interaction and ~61% haplotype-vs-haplotype divergence within one cell ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).

## Methods

| Method | Chemistry | Readout | What it adds | Source |
|---|---|---|---|---|
| [[fiber-seq\|Fiber-seq]] | Hia5 m6A on accessible adenines | PacBio CCS, native (bulk-only) | The field's first usable single-molecule chromatin readout | ([[10-Summaries/andrewb-2020-science\|Stergachis 2020]]) |
| [[samosa\|SAMOSA]] | EcoGII m6dA on MNase-solubilised oligonucleosomes (~500 bp–2 kb) | PacBio, native | Clusters fibres into seven regularity/NRL patterns; does not resolve TF footprints, because methylation follows solubilisation | ([[10-Summaries/abdulhay-2020-samosa\|Abdulhay 2020]]) |
| [[samosa-tag\|SAMOSA-Tag]] | Adapter-tagmented SAMOSA variant | PacBio, native | Targeted regions | ([[10-Summaries/nanda-2024-smrt-tag\|Nanda 2024]]) |
| [[stam-seq\|STAM-seq]] | Fiber-seq-style m6A stenciling | Nanopore | Adapted to *Arabidopsis* centromeres / telomeres / rDNA; shows the chemistry generalizes to non-mammalian chromatin | ([[10-Summaries/mo-2023-stam-seq\|Mo 2023]]) |
| [[smrt-tag\|SMRT-Tag]] | Tn5-tagmentation front end for SMRT footprinting | PacBio | Multimodal applications for adjacent assays | ([[10-Summaries/nanda-2024-smrt-tag\|Nanda 2024]]) |
| Targeted Fiber-seq | m6A-stencilled nuclei, CRISPR–Cas9 excision of 100–250 kb loci (HLS-CATCH) | PacBio HiFi | ~10-fold median enrichment, 101–164× single-molecule coverage, per-fiber CTCF footprinting at single motifs | ([[10-Summaries/bohaczuk-2024-targeted-fiberseq\|Bohaczuk 2024]]) |
| GpC-SMF / scNOMe-seq | GpC methyltransferase, read by bisulfite or EM-seq | Short read; single cells and amplicons | Marks survive amplification | ([[10-Summaries/pott-2017-elife\|Pott 2017]]; [[10-Summaries/doughty-2024-smf-tf\|Doughty 2024]]) |
| [[daf-seq\|DAF-seq]] | SsDddA cytidine deamination | PacBio long read; bulk and single-cell (PTA) variants | Extends single-molecule footprinting to chromosome-length single-cell coverage | ([[10-Summaries/swanson-2025-daf-seq\|Swanson 2025]]) |
| FOODIE | DddB dsDNA-deaminase footprinting after Tn5 tagmentation | Short-read Illumina | Per-footprint binding fractions and pairwise TF cooperativity (γ = ad/bc); scFOODIE types cells, then pools them; Xie lab (Peking University) | ([[10-Summaries/he-2024-foodie\|He 2024]]) |

Methyltransferase stenciling with native m6A is amplification-erased and bulk-only; deaminase stenciling is sequence-encoded, amplification-survivable and single-cell-extensible ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).

## Evidence and examples

- TF cooperativity quantified at single-nucleotide resolution on the NAPA promoter ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- Per-cell, per-haplotype regulatory-element actuation maps in lymphoblastoid GM24385 ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- Amplicon GpC-SMF on engineered TetO/ISRE reporters links single-molecule TF/nucleosome configurations to expression; apparent cooperativity arises from BAF-mediated nucleosome destabilisation (Greenleaf + Bintu labs) ([[10-Summaries/doughty-2024-smf-tf|Doughty 2024]]).

## Contested points

- Long-read sequencing depth requirements are substantial — single-cell footprinting at chromosome scale (scDAF-seq) needs tens to hundreds of Gb per cell ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- Comparison to ensemble methods is sometimes apples-to-oranges: per-molecule and per-cell reports answer different questions than per-population reports (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/fiber-seq|Fiber-seq]] — m6A stenciling of chromatin fibers read on long reads.
> - `concept` [[30-Concepts/daf-seq|DAF-seq]] — Deaminase stenciling that survives amplification and reaches single cells.
> - `concept` [[30-Concepts/samosa|SAMOSA]] — EcoGII footprinting of oligonucleosomes on PacBio.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — Whether DNA is open or nucleosome-wrapped.
> - `concept` [[30-Concepts/chromatin-actuation|Chromatin actuation]] — A regulatory element open and bound on one fiber.
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — How DNA packaging with proteins varies along chromosomes and between cells.

## All sources on this page

> [!info]- 9 summaries cited here
> - [[10-Summaries/abdulhay-2020-samosa|Abdulhay 2020]]
> - [[10-Summaries/andrewb-2020-science|Stergachis 2020]]
> - [[10-Summaries/bohaczuk-2024-targeted-fiberseq|Bohaczuk 2024]]
> - [[10-Summaries/doughty-2024-smf-tf|Doughty 2024]]
> - [[10-Summaries/he-2024-foodie|He 2024]]
> - [[10-Summaries/mo-2023-stam-seq|Mo 2023]]
> - [[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]
> - [[10-Summaries/pott-2017-elife|Pott 2017]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
