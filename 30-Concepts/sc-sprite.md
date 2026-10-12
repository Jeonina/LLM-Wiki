---
type: concept
title: scSPRITE
aliases: []
tags: [3D-genome, single-cell, split-pool, multi-way-contacts]
created: 2026-05-12
updated: 2026-10-12
---

# scSPRITE

> Single-cell SPRITE (Split-Pool Recognition of Interactions by Tag Extension). Fragments cross-linked chromatin inside nuclei by restriction digestion (HpyCH4V), uses sonication only to release the crosslinked complexes onto beads, then split-pool-barcodes them to capture **multi-way** (not just pairwise) chromatin contacts at single-cell resolution ([[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]).

> [!abstract] 한눈에
> scSPRITE는 crosslink된 chromatin 복합체를 세포 단위와 공간 cluster 단위로 split-pool barcoding해, 쌍이 아닌 여러 조각 사이의 multi-way contact를 single-cell 수준에서 잡는 방법이다 ([[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]). 세포당 contact 수는 가장 많지만, 큰 cluster의 상당 부분은 간접적이거나 trans 상호작용일 수 있다는 해석이 있다 ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]; [[10-Summaries/li-2023-scnanohi-c|Li 2023]]).

## Definition

Unlike ligation-based Hi-C methods that capture pairs of fragments, SPRITE-family methods preserve spatial clusters: DNA fragments from the same nuclear neighborhood end up in the same cluster, allowing higher-order contact frequency mapping.

## Why it matters

- Captures **more contacts per cell** than any ligation-based sc-Hi-C method ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).
- Reveals higher-order contacts (3+ partners) missed by pairwise methods.

## Protocol

- **Fragmentation.** DNA is fragmented by in-nucleus restriction digestion (HpyCH4V, ~823 bp average fragment) ([[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]).
- **Release.** Sonication is used afterwards to release crosslinked complexes onto NHS beads ([[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]).
- **Two-stage barcoding.** Three in-nucleus split-pool rounds encode the cell and three bead rounds encode the spatial cluster ([[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]).

## Evidence and examples

- On 1,000 mESCs scSPRITE reports an average of 34,992,080 pairwise contacts per cell from 83,318 reads per cell, versus 375,470 contacts from 751,172 reads in a published scHi-C dataset ([[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]).
- 54% of its contacts are inter-chromosomal versus 6% for scHi-C ([[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]).
- In a head-to-head comparison by the scNanoHi-C authors, ~70% of effective scSPRITE reads in a cell sit in clusters of cardinality >10; these clusters decay more slowly with distance than bulk Hi-C, and scSPRITE's trans ratio is 54% versus 11% for scNanoHi-C ([[10-Summaries/li-2023-scnanohi-c|Li 2023]]).

## Contested points

- **What the high-cardinality clusters mean.** The scNanoHi-C authors interpret scSPRITE's high-cardinality clusters as mainly indirect and trans interactions, possibly mediated by subnuclear compartments ([[10-Summaries/li-2023-scnanohi-c|Li 2023]]).
- **Contact counts are not like-for-like.** The scSPRITE count is n-choose-2 pairs per cluster, so it is not directly comparable with ligation-based counts ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — The family of methods profiling chromatin contacts in single cells.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Territories, compartments, TADs and loops in the nucleus.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]
> - [[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]
> - [[10-Summaries/li-2023-scnanohi-c|Li 2023]]
