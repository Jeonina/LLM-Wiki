---
type: concept
title: Lineage tracing with somatic mutations
aliases: [somatic lineage tracing, mutation-based lineage tracing]
tags: [lineage-tracing, somatic-mutation, phylogeny, development]
created: 2026-05-19
updated: 2026-05-19
---

# Lineage tracing with somatic mutations

> Using naturally-accumulating somatic mutations as endogenous lineage barcodes to reconstruct cell phylogenies in human tissue without engineered markers ([[10-Summaries/coorens-2021-nature]]; [[10-Summaries/lee-six-2018-hsc-dynamics]]).

## Definition

Every cell division has some probability of introducing a unique SNV, indel, or CNV that is inherited by daughter cells. Deep sequencing of clonal expansions thus recovers a phylogeny. Works in any human tissue; requires sensitive variant calling (PTA + duplex) for sparse expansions.

## Methods

- **Bulk colony / microdissection** — sequence many clonal colonies, infer phylogeny ([[10-Summaries/lee-six-2018-hsc-dynamics]]).
- **Single-cell** — scDNA-seq with PTA + duplex validation ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]).
- **Phylogenetic algorithms** — SCITE ([[10-Summaries/jahn-2016-scite]]), SiFit ([[10-Summaries/zafar-2017-sifit]]), SCARLET ([[10-Summaries/satas-2020-scarlet]]).

## Applications

- Human developmental phylogeny ([[10-Summaries/coorens-2021-nature]]).
- Hematopoietic stem cell dynamics ([[10-Summaries/lee-six-2018-hsc-dynamics]]).
- Cancer clonal evolution.

## Related

- [[30-Concepts/lineage-tracing]] · [[30-Concepts/somatic-mosaicism]] · [[30-Concepts/methylation-clones-epimutation]]
- [[40-Topics/somatic-mosaicism]] · [[40-Topics/scdna-seq]]
