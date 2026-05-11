---
type: topic
title: Chromatin architecture
aliases: [chromatin biology, chromatin organization]
tags: [chromatin, regulation, single-molecule]
created: 2026-05-07
updated: 2026-05-07
---

# Chromatin architecture

> How DNA is packaged with proteins (nucleosomes, TFs, cohesin/CTCF, polycomb, …) along chromosomes, and how that packaging is heterogeneous across fibers, haplotypes, and cells. The single-molecule branch of this topic is moving fast: Fiber-seq → DAF-seq closes the gap from bulk to single-cell single-molecule resolution.

## Core concepts

- [[30-Concepts/chromatin-accessibility]] — whether DNA is "open" for binding; measured by ATAC-seq, DNase-seq, or single-molecule footprinting.
- [[30-Concepts/chromatin-actuation]] — single-molecule refinement: per-fiber binary state of "open + bound."
- [[30-Concepts/single-molecule-footprinting]] — the method class.
- [[30-Concepts/atac-seq]] — Tn5 transposase tagmentation of accessible chromatin; the workhorse assay.
- [[30-Concepts/dnase-seq]] — original ENCODE accessibility assay; largely superseded by ATAC-seq.
- [[30-Concepts/fiber-seq]] — bulk single-molecule via m6A methyltransferase stenciling.
- [[30-Concepts/daf-seq]] — single-cell single-molecule via cytidine deaminase footprinting.

## Key entities

- [[20-Entities/andrew-b-stergachis]] — UW Genome Sciences PI; developer of Fiber-seq and senior author of DAF-seq.
- [[20-Entities/elliott-g-swanson]] — co-first author of DAF-seq.
- [[20-Entities/william-greenleaf]] — Stanford; co-developer of ATAC-seq; senior author of canonical accessibility review.

## Sources, by sub-theme

### Single-molecule chromatin profiling

- [[10-Summaries/elliott-2025-naturebiotechnology]] — DAF-seq / scDAF-seq; chromosome-length single-cell single-molecule chromatin maps.

### Single-cell chromatin profiling (droplet ATAC-seq integrated with genotyping)

- [[10-Summaries/franco-2024-nature]] — GoT–ChA; droplet-scale chromatin accessibility tied to JAK2V617F genotype.

### Reviews

- [[10-Summaries/sandy-2019-naturereviewsgenetics]] — Klemm/Shipony/Greenleaf canonical chromatin accessibility review.

## Synthesized notes

_None yet._

## Open questions

- **Why is intra-cell haplotype divergence (~61%) almost equal to inter-cell divergence (~63%)?** ([[10-Summaries/elliott-2025-naturebiotechnology]] reports this but does not explain it. Implication: regulatory-element actuation may be closer to a stochastic per-fiber event than a programmed per-cell state.)
- **Co-actuation domains of ~100 kb** mirror cohesin loops at single-fiber resolution ([[10-Summaries/elliott-2025-naturebiotechnology]]) — but causality (do cohesin loops *cause* co-actuation, or just correlate?) is not directly tested.
- How well do single-molecule chromatin readouts ([[daf-seq]]) reconcile with droplet-scale ([[got-cha]]) data — i.e., when scDAF-seq reports 63% inter-cell actuation divergence, what would scATAC-seq from the same cells say?
- Generalization of scDAF-seq beyond GM24385 lymphoblastoid cells to primary tissue and disease contexts.
