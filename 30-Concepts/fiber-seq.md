---
type: concept
title: Fiber-seq
aliases: [fiber-seq]
tags: [single-molecule, chromatin, methyltransferase, footprinting, method]
created: 2026-05-07
updated: 2026-05-07
---

# Fiber-seq

> Single-molecule chromatin footprinting method developed in the [[20-Entities/andrew-b-stergachis|Stergachis lab]] that uses an N6-adenine methyltransferase (m6A) to stencil protein occupancy onto chromatin fibers, then reads the methyl marks with long-read sequencing — predecessor of [[daf-seq]].

## Definition

In nuclei, a non-specific m6A methyltransferase modifies adenines in accessible (TF/nucleosome-free) DNA. Long-read sequencing platforms (PacBio, Nanopore) can read m6A directly, so the resulting methylation pattern along an individual fiber is a chromatin footprint at near-nucleotide resolution ([[10-Summaries/elliott-2025-naturebiotechnology]] context).

## Why it matters

Fiber-seq gave the field the first **bulk single-molecule chromatin architecture maps**: TF cooperativity, nucleosome positioning, regulatory-element co-actuation along the same fiber. But it has a structural ceiling: **m6A marks are erased during DNA amplification**, so Fiber-seq cannot be applied to single cells. Each cell yields one or two fibers per locus and there is no way to amplify them up.

[[daf-seq]] inherits the conceptual framework — single-molecule footprinting as the unit of chromatin analysis — and replaces the chemistry with one (cytidine deamination) whose marks are sequence changes that *do* survive amplification.

## Variants and refinements

- Used in [[10-Summaries/elliott-2025-naturebiotechnology]] as the bulk reference for benchmarking DAF-seq accessibility, nucleosome positioning, and co-actuation calls.
- The COLO829 BL/T low-VAF variant analysis was originally proposed using Fiber-seq on each cell line separately; DAF-seq extended it to direct measurement on the BL/T mixture.

## Contested points

- Bulk-only nature is the central limitation; not contested but acknowledged.
- m6A read accuracy depends on long-read base-caller models, which evolve over time.

## Examples

- Identifying the chr.17:19447245–19447246 CC>TT somatic CTCF-ablating variant in COLO829T melanoma cells ([[10-Summaries/elliott-2025-naturebiotechnology]] panel referencing prior work).

## Related

- [[daf-seq]] — direct successor; replaces methylation marks with deaminations.
- [[single-molecule-footprinting]]
- [[chromatin-actuation]]
- [[20-Entities/andrew-b-stergachis]]
- [[40-Topics/chromatin-architecture]]
