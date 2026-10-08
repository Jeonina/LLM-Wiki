---
type: concept
title: Single-molecule chromatin footprinting
aliases: [single-molecule footprinting, single-fiber footprinting]
tags: [chromatin, single-molecule, method-class]
created: 2026-05-07
updated: 2026-10-07
paper_section: ["3.2.1"]
---

# Single-molecule chromatin footprinting

> A class of chromatin assays that mark accessible DNA on individual nuclear fibers (rather than across an ensemble) and read those marks with long-read sequencing, recovering per-fiber maps of nucleosome positioning, TF occupancy, and regulatory-element actuation.

## Definition

Population/ensemble assays — DNase-seq, ATAC-seq, ChIP-seq — average chromatin states across many cells and many fibers, smearing out cooperativity and per-fiber heterogeneity. Single-molecule footprinting marks each fiber's accessible bases and sequences each fiber individually, so the *pattern* of marks along one DNA molecule reports the *configuration* of bound proteins on that molecule ([[10-Summaries/swanson-2025-daf-seq]] introduction).

Two main chemistries:

- **Methyltransferase stenciling** — m6A on accessible adenines ([[fiber-seq]]). m6A read natively on long reads is erased by amplification → bulk-only; GpC methyltransferase marks read by bisulfite or EM-seq survive amplification and work in single cells ([[10-Summaries/pott-2017-elife]]) and on short-read amplicons ([[10-Summaries/doughty-2024-smf-tf]]).
- **Deaminase stenciling** — C→T on accessible cytidines ([[daf-seq]]). Marks are sequence changes → survive amplification → single-cell-extensible.

## Why it matters

Aggregate chromatin assays cannot disentangle:

- **TF cooperativity** (whether TFs bind together vs independently along the same fiber);
- **Haplotype-specific actuation** (whether the two homologous chromosomes within a cell carry different chromatin states);
- **Regulatory-element co-actuation domains** (whether two enhancers fire on the same fiber or different fibers).

These are precisely the readouts that single-molecule footprinting recovers — and the readouts on which [[10-Summaries/swanson-2025-daf-seq]] reports surprising findings (180,000× cooperative interactions; ~61% haplotype-vs-haplotype divergence within one cell).

## Variants and refinements

**Methyltransferase stenciling (m6A-based, amplification-erased, bulk-only)**:

- **[[fiber-seq]]** ([[10-Summaries/andrewb-2020-science]]) — the field's first usable single-molecule chromatin readout; Hia5 m6A on accessible adenines + PacBio CCS.
- **[[samosa]]** ([[10-Summaries/abdulhay-2020-samosa]]) — EcoGII m6dA footprinting of MNase-solubilised oligonucleosomes (~500 bp–2 kb) read natively on PacBio; clusters fibres into seven regularity/NRL patterns but does not resolve TF footprints, because methylation follows solubilisation.
- **[[samosa-tag]]** — adapter-tagmented SAMOSA variant for targeted regions.
- **[[stam-seq]]** ([[10-Summaries/mo-2023-stam-seq]]) — Fiber-seq-style m6A stenciling adapted to *Arabidopsis* centromeres / telomeres / rDNA; demonstrates the chemistry generalizes to non-mammalian chromatin.
- **[[smrt-tag]]** ([[10-Summaries/nanda-2024-smrt-tag]]) — Tn5-tagmentation front end for SMRT footprinting; multimodal applications for adjacent assays.
- **Targeted Fiber-seq** ([[10-Summaries/bohaczuk-2024-targeted-fiberseq]]) — CRISPR–Cas9 excision of 100–250 kb loci from m6A-stencilled nuclei (HLS-CATCH), ~10-fold median enrichment and 101–164× single-molecule coverage, with per-fiber CTCF footprinting at single motifs.

**Deaminase stenciling (sequence-encoded, amplification-survivable, single-cell-extensible)**:

- **[[daf-seq]]** ([[10-Summaries/swanson-2025-daf-seq]]) — SsDddA cytidine deamination; bulk and single-cell variants; extends single-molecule footprinting to chromosome-length single-cell coverage.
- **FOODIE** ([[10-Summaries/he-2024-foodie]]) — DddB dsDNA-deaminase footprinting after Tn5 tagmentation, read on short-read Illumina; per-footprint binding fractions and pairwise TF cooperativity (γ = ad/bc); scFOODIE types cells, then pools them; from the Xie lab (Peking University).

## Contested points

- Long-read sequencing depth requirements are substantial — single-cell footprinting at chromosome scale (scDAF-seq) needs tens to hundreds of Gb per cell.
- Comparison to ensemble methods is sometimes apples-to-oranges: per-molecule and per-cell reports answer different questions than per-population reports.

## Examples

- TF cooperativity quantified at single-nucleotide resolution on the NAPA promoter ([[10-Summaries/swanson-2025-daf-seq]]).
- Per-cell, per-haplotype regulatory-element actuation maps in lymphoblastoid GM24385 ([[10-Summaries/swanson-2025-daf-seq]]).
- Amplicon GpC-SMF on engineered TetO/ISRE reporters links single-molecule TF/nucleosome configurations to expression; apparent cooperativity arises from BAF-mediated nucleosome destabilisation (Greenleaf + Bintu labs, [[10-Summaries/doughty-2024-smf-tf]]).

## Related

- [[fiber-seq]]
- [[daf-seq]]
- [[chromatin-accessibility]]
- [[chromatin-actuation]]
- [[40-Topics/chromatin-architecture]]
