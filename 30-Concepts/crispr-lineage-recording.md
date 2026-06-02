---
type: concept
title: CRISPR lineage recording
aliases: [evolvable barcodes, CRISPR recorder, molecular recording, synthetic evolvable barcodes]
tags: [lineage-tracing, CRISPR, synthetic-barcodes, phylogenetics, prime-editing, base-editing]
created: 2026-06-02
updated: 2026-06-02
---

# CRISPR lineage recording

> A class of *prospective, evolvable* synthetic lineage-tracing systems in which Cas9 (or relatives) progressively accumulates heritable edits in a transgenic reporter, so the order of edits reconstructs a cell-division phylogeny ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).

## Definition

Inducible Cas9 plus single-guide RNAs generate double-strand breaks in a multi-target reporter cassette; error-prone repair (typically non-homologous end joining) writes a different sequence in each cell, and repeated cutting makes the barcode *evolvable* — accumulating new mutations over time to diversify the record ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]). Slightly mismatched guides tune editing rate for temporal resolution ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).

## Why it matters

- Enables reconstruction of detailed phylogenetic trees — up to whole-organism scale — rather than just clonal grouping ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).
- Distinguished from *static* synthetic barcodes (one immutable label/cell) and from *retrospective* natural-variant tracing ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).

## Variants and refinements

- **Diversity-boosting nucleases**: self-homing hgRNAs (self-targeting → enormous diversity, used for organism-wide trees); base editors (substitutions, not deletions); Cas12a (cuts outside its guide-recognized sequence) ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).
- **Writer fusions**: Cas9 + template-independent polymerase (TdT) adds insertions, used to trace fetal→adult HSC transition; prime-editing-based recording writes known "symbols," enabling probe-based spatial readout (PE-tracer) ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).
- **Cas9-independent**: T7-polymerase (TRACE) or SceI (SMALT) fused to cytidine deaminases for continuous editing ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).

## Contested points

- Original tandem-target reporters suffer inter-site deletions that collapse effective diversity, low reporter expression causing scRNA-seq dropout, and low editing efficiency leaving unedited cells ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).
- Bioinformatic interpretation of sparse edits across many alleles is the main downstream bottleneck ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]); CRISPR-aware phylogenetic models (Cassiopeia, STARTLE) enforce edit irreversibility and model dropout ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).

## Related

- [[30-Concepts/lineage-tracing]] · [[30-Concepts/phylogenetic-inference]] · [[30-Concepts/lineage-tracing-somatic-mutations]]
- [[40-Topics/single-cell-lineage-tracing]] · [[20-Entities/jay-shendure]]
