---
type: concept
title: CITE-seq
aliases: [Cellular Indexing of Transcriptomes and Epitopes by Sequencing]
tags: [multi-omics, scRNA-protein, antibody-derived-tags, method]
created: 2026-05-11
updated: 2026-05-11
---

# CITE-seq

> Single-cell multi-omic method that measures transcriptome and cell-surface protein expression from the same cell by labeling cells with **antibody-derived tags (ADTs)** — antibodies conjugated to oligonucleotides that are captured and sequenced alongside mRNA in a 10x droplet workflow.

## Definition

ADTs are antibodies conjugated to oligonucleotide barcodes with a polyA tail (so they're captured by oligo-dT primers in 10x scRNA-seq chemistry). After incubation with cells, the bound ADTs co-amplify with mRNA in the same droplet, producing per-cell counts of both transcripts and surface proteins ([[10-Summaries/baysoy-2023-multiomics-landscape]]).

Captures 100s–1000s of surface protein markers in panels.

## Why it matters

- Adds **direct protein-level phenotyping** to transcriptomic data — important for immune cell classification where surface markers are the canonical phenotype.
- Improves cell-type annotation accuracy over RNA-only.
- Compatible with downstream chromatin (DOGMA-seq) and genotype (GoT–ChA imputation) modalities — see [[dogma-seq]] and [[10-Summaries/izzo-2024-got-cha]].

## Variants and refinements

- **REAP-seq** — closely related antibody-tag platform.
- **TotalSeq** (BioLegend) — commercial ADT line.
- **DOGMA-seq** — trimodal extension adding chromatin.

## Contested points

- Specific binding vs background — non-specific antibody binding produces baseline ADT counts that complicate normalization.
- Limited to surface proteins — intracellular proteins not accessible.

## Examples

- Detailed immune cell phenotyping in tumor microenvironment studies.
- DOGMA-seq extension giving chromatin + RNA + protein in single cells.

## Related

- [[40-Topics/single-cell-multiomics]]
- [[dogma-seq]]
- [[40-Topics/single-cell-multiomics]]
