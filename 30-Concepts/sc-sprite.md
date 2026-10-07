---
type: concept
title: scSPRITE
aliases: []
tags: [3D-genome, single-cell, split-pool, multi-way-contacts]
created: 2026-05-12
updated: 2026-10-07
---

# scSPRITE

> Single-cell SPRITE (Split-Pool Recognition of Interactions by Tag Extension). Fragments cross-linked chromatin inside nuclei by restriction digestion (HpyCH4V), uses sonication only to release the crosslinked complexes onto beads, then split-pool-barcodes them ([[10-Summaries/arrastia-2022-scsprite]]) to capture **multi-way** (not just pairwise) chromatin contacts at single-cell resolution.

## Definition

Unlike ligation-based Hi-C methods that capture pairs of fragments, SPRITE-family methods preserve spatial clusters: DNA fragments from the same nuclear neighborhood end up in the same cluster, allowing higher-order contact frequency mapping.

## Why it matters

- Captures **more contacts per cell** than any ligation-based sc-Hi-C method (benchmark in [[10-Summaries/jiang-2026-stark-scnucleome]]).
- Reveals higher-order contacts (3+ partners) missed by pairwise methods.

## Added 2026-10-07

In scSPRITE, DNA is fragmented by in-nucleus restriction digestion (HpyCH4V, ~823 bp average fragment). Sonication is used afterwards to release crosslinked complexes onto NHS beads. Three in-nucleus split-pool rounds encode the cell and three bead rounds encode the spatial cluster ([[10-Summaries/arrastia-2022-scsprite]]). On 1,000 mESCs it reports an average of 34,992,080 pairwise contacts per cell from 83,318 reads per cell, versus 375,470 contacts from 751,172 reads in a published scHi-C dataset. 54% of its contacts are inter-chromosomal versus 6% for scHi-C ([[10-Summaries/arrastia-2022-scsprite]]).

A head-to-head comparison by the scNanoHi-C authors found that ~70% of effective scSPRITE reads in a cell sit in clusters of cardinality >10. These clusters decay more slowly with distance than bulk Hi-C, and scSPRITE's trans ratio is 54% versus 11% for scNanoHi-C. The authors interpret scSPRITE's high-cardinality clusters as mainly indirect and trans interactions, possibly mediated by subnuclear compartments ([[10-Summaries/li-2023-scnanohi-c]]).


## Related

- [[30-Concepts/single-cell-hi-c]] · [[40-Topics/3d-genome]]
