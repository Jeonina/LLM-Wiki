---
type: concept
title: Methylation clones and epimutation lineage tracing
aliases: [epimutation lineage tracing, methylation clones, epi-clone]
tags: [methylation, lineage-tracing, epimutation, single-cell]
created: 2026-05-19
updated: 2026-05-19
---

# Methylation clones and epimutation lineage tracing

> Heritable, mitotically-propagated changes in DNA methylation state at individual CpGs ("epimutations") serve as endogenous lineage markers in human cells where engineered barcoding is not feasible. Methods like Epi-CLONE and MethylTree reconstruct clonal genealogies from methylation patterns at clock-like CpGs ([[10-Summaries/chen-2025-methyltree]]; [[10-Summaries/xiao-2025-epitrace]]).

## Underlying biology

Epimutations accumulate at predictable rates at clock-like CpGs (e.g., ELOVL2, scaffold ICRs). Maintenance errors of DNMT1 during replication produce these — they are heritable but not deterministic ([[10-Summaries/kim-2017-methylation-memory-review]]).

## Methods

- **MethylTree** — phylogenetic inference from scBS-seq methylation patterns ([[10-Summaries/chen-2025-methyltree]]).
- **EpiTrace** — chromatin-accessibility-based epigenetic age estimation, parallel to methylation clones ([[10-Summaries/xiao-2025-epitrace]]).
- **Epi-CLONE** — methylation lineage tracing in human stem cells ([[10-Summaries/gaiti-2019-cll-epigenetic]] precedent in CLL).

## Why it matters

Methylation-based lineage tracing works in human tissue without genetic engineering. It complements somatic-mutation-based lineage tracing ([[30-Concepts/lineage-tracing]]) — methylation is denser but noisier; mutations are sparser but more confident.

## Related

- [[30-Concepts/lineage-tracing]] · [[30-Concepts/epigenetic-memory]] · [[30-Concepts/epigenetic-aging]]
- [[40-Topics/dna-methylation]]
