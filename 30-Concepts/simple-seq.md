---
type: concept
title: SIMPLE-seq
aliases: [simultaneous profiling of epigenetic cytosine modifications by sequencing]
tags: [methylation, single-cell, 5mC, 5hmC, bisulfite-free, combinatorial-indexing]
created: 2026-05-12
updated: 2026-10-12
---

# SIMPLE-seq

> A bisulfite-free single-cell method for simultaneous detection of 5mC and 5hmC at single-base resolution. Sequentially labels 5hmC (ruthenate oxidation + indanedione) and 5mC (TET oxidation + borane reduction), encoding both as distinguishable C-to-T mutational signals on the same molecule ([[10-Summaries/bai-2024-simple-seq|Bai 2024]]).

> [!abstract] 한눈에
> SIMPLE-seq는 bisulfite 없이 한 분자 위의 5mC와 5hmC를 단일 염기 해상도로 함께 읽는 single-cell 방법이다. 두 수식을 서로 구별되는 C-to-T 신호로 바꾸고 combinatorial indexing으로 수천 개 세포를 한 번에 처리한다 ([[10-Summaries/bai-2024-simple-seq|Bai 2024]]).

## Definition

Combines [[taps|TAPS]] chemistry (for 5mC → uracil conversion) with hmC-CATCH-style 5hmC labeling. A 5caC-pre-deposited primer encodes which conversion step each amplicon comes from, so 5mC and 5hmC signals are recoverable from a single library. Combinatorial indexing allows thousands of single cells per experiment (~100,000 nuclei can be tagged after two rounds of ligation barcoding) ([[10-Summaries/bai-2024-simple-seq|Bai 2024]]).

## Why it matters

5mC and [[5hmc|5hmC]] have distinct regulatory roles. Prior single-cell methods (scAba-seq, scBS-seq) detect one modification at a time, losing within-molecule co-occurrence information ([[10-Summaries/bai-2024-simple-seq|Bai 2024]]).

## Examples

- mESCs 2i→serum transition: cells with high "modification entropy" mark transient reprogramming midpoints. Type-2 5hmCG sites (paired with 5mCG) mark dynamic methylation ([[10-Summaries/bai-2024-simple-seq|Bai 2024]]).
- Human PBMCs and mouse cerebral cortex profiled in the same paper ([[10-Summaries/bai-2024-simple-seq|Bai 2024]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/taps|TAPS]] — Bisulfite-free 5mC chemistry: TET oxidation, then pyridine-borane reduction.
> - `concept` [[30-Concepts/5hmc|5hmC]] — The oxidative intermediate TET enzymes make from 5mC.
> - `concept` [[30-Concepts/tet-enzymes|TET enzymes]] — Dioxygenases that oxidize 5mC to 5hmC and onward.
> - `concept` [[30-Concepts/combinatorial-indexing|Combinatorial indexing]] — Split-pool barcoding that gives each cell a unique barcode combination.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC biology and the methods that measure it.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/bai-2024-simple-seq|Bai 2024]]
