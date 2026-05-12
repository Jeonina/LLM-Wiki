---
type: concept
title: scSPRITE
aliases: []
tags: [3D-genome, single-cell, sonication, multi-way-contacts]
created: 2026-05-12
updated: 2026-05-12
---

# scSPRITE

> Single-cell SPRITE (Split-Pool Recognition of Interactions by Tag Extension). Uses sonication-based fragmentation of cross-linked chromatin to release entire spatial clusters of DNA, then split-pool-barcodes them to capture **multi-way** (not just pairwise) chromatin contacts at single-cell resolution.

## Definition

Unlike ligation-based Hi-C methods that capture pairs of fragments, SPRITE-family methods preserve spatial clusters: DNA fragments from the same nuclear neighborhood end up in the same cluster, allowing higher-order contact frequency mapping.

## Why it matters

- Captures **more contacts per cell** than any ligation-based sc-Hi-C method (benchmark in [[10-Summaries/harmonizing-single-cell-3d-genome-data-with-stark-and-scnucleome]]).
- Reveals higher-order contacts (3+ partners) missed by pairwise methods.

## Related

- [[30-Concepts/single-cell-hi-c]] · [[30-Concepts/3d-genome]] · [[40-Topics/3d-genome]]
