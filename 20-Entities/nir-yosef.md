---
type: entity
title: Nir Yosef
aliases: [Yosef lab]
entity_kind: person
tags: [computational-biology, single-cell, probabilistic-models]
created: 2026-08-10
updated: 2026-08-10
---

# Nir Yosef

> Computational single-cell biology; probabilistic and algorithmic methods for large single-cell datasets.

## Mentions

- **2026-08-10** — Corresponding author of [[jones-2020-cassiopeia]], a maximum-parsimony suite scaling to 50,000 cells.

## Related

- [[phylogenetic-inference]] · [[lineage-tracing]] · [[computational-methods]]

## Added 2026-08-17

Corresponding author of [[10-Summaries/gayoso-2021-totalvi]] (totalVI), the deep-generative model for CITE-seq. Its distinguishing contribution is not the neural network but the **protein background model**: antibody counts carry a large ambient / non-specifically-bound component that RNA counts do not, and totalVI separates protein signal into background and foreground inside the generative model rather than as a preprocessing step.

Part of the scvi-tools framework, which also produces [[10-Summaries/ashuach-2023-multivi]] — so the CITE-seq and RNA+ATAC problems share a codebase and a modelling philosophy.
