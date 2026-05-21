---
type: concept
title: Single-molecule chromatin footprinting
aliases: [single-molecule footprinting, single-fiber footprinting]
tags: [chromatin, single-molecule, method-class]
created: 2026-05-07
updated: 2026-05-07
---

# Single-molecule chromatin footprinting

> A class of chromatin assays that mark accessible DNA on individual nuclear fibers (rather than across an ensemble) and read those marks with long-read sequencing, recovering per-fiber maps of nucleosome positioning, TF occupancy, and regulatory-element actuation.

## Definition

Population/ensemble assays — DNase-seq, ATAC-seq, ChIP-seq — average chromatin states across many cells and many fibers, smearing out cooperativity and per-fiber heterogeneity. Single-molecule footprinting marks each fiber's accessible bases and sequences each fiber individually, so the *pattern* of marks along one DNA molecule reports the *configuration* of bound proteins on that molecule ([[10-Summaries/swanson-2025-daf-seq]] introduction).

Two main chemistries:

- **Methyltransferase stenciling** — m6A on accessible adenines ([[fiber-seq]]). Marks erased by amplification → bulk-only.
- **Deaminase stenciling** — C→T on accessible cytidines ([[daf-seq]]). Marks are sequence changes → survive amplification → single-cell-extensible.

## Why it matters

Aggregate chromatin assays cannot disentangle:

- **TF cooperativity** (whether TFs bind together vs independently along the same fiber);
- **Haplotype-specific actuation** (whether the two homologous chromosomes within a cell carry different chromatin states);
- **Regulatory-element co-actuation domains** (whether two enhancers fire on the same fiber or different fibers).

These are precisely the readouts that single-molecule footprinting recovers — and the readouts on which [[10-Summaries/swanson-2025-daf-seq]] reports surprising findings (180,000× cooperative interactions; ~61% haplotype-vs-haplotype divergence within one cell).

## Variants and refinements

- **[[fiber-seq]]** — bulk m6A; the field's first usable single-molecule chromatin readout.
- **[[daf-seq]]** — bulk and single-cell SsDddA cytidine deamination; extends single-molecule footprinting to chromosome-length single-cell coverage.

## Contested points

- Long-read sequencing depth requirements are substantial — single-cell footprinting at chromosome scale (scDAF-seq) needs tens to hundreds of Gb per cell.
- Comparison to ensemble methods is sometimes apples-to-oranges: per-molecule and per-cell reports answer different questions than per-population reports.

## Examples

- TF cooperativity quantified at single-nucleotide resolution on the NAPA promoter ([[10-Summaries/swanson-2025-daf-seq]]).
- Per-cell, per-haplotype regulatory-element actuation maps in lymphoblastoid GM24385 ([[10-Summaries/swanson-2025-daf-seq]]).

## Related

- [[fiber-seq]]
- [[daf-seq]]
- [[chromatin-accessibility]]
- [[chromatin-actuation]]
- [[40-Topics/chromatin-architecture]]
