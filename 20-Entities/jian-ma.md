---
type: entity
title: Jian Ma
aliases: [Ma lab, CMU]
entity_kind: person
tags: [3D-genome, machine-learning, hypergraph, CMU]
created: 2026-08-10
updated: 2026-08-10
---

# Jian Ma

> Carnegie Mellon. Representation-learning approaches to 3D genome structure, particularly for sparse single-cell contact data.

## Mentions

- **2026-08-10** — Corresponding author of [[zhang-2022-higashi]], whose hypergraph formulation revealed present/absent and sliding TAD-like boundaries per cell.

## Related

- [[imputation]] · [[single-cell-hi-c]] · [[3d-genome]]

## Added 2026-08-13

Corresponding author of [[10-Summaries/xiong-2024-scghost]] (scGHOST), the first method for annotating **single-cell 3D genome subcompartments**. Subcompartments had resisted single-cell analysis for a coverage-arithmetic reason — bulk annotation needs ≥50M *trans* reads and scHi-C has almost none — so scGHOST substitutes graph-embedding structure via constrained random walks over [[10-Summaries/zhang-2022-higashi|Higashi]]-imputed maps.

Its most consequential finding: on HiRES joint RNA+Hi-C embryo data, **~50% of marker genes switch subcompartment before upregulation** and only 14% change synchronously.
