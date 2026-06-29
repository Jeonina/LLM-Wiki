---
type: concept
title: SIMPLE-seq
aliases: [simultaneous profiling of epigenetic cytosine modifications by sequencing]
tags: [methylation, single-cell, 5mC, 5hmC, bisulfite-free, combinatorial-indexing]
created: 2026-05-12
updated: 2026-05-12
---

# SIMPLE-seq

> A bisulfite-free single-cell method for simultaneous detection of 5mC and 5hmC at single-base resolution. Sequentially labels 5hmC (ruthenate oxidation + indanedione) and 5mC (TET oxidation + borane reduction), encoding both as distinguishable C-to-T mutational signals on the same molecule.

## Definition

Combines TAPS chemistry (for 5mC → uracil conversion) with hmC-CATCH-style 5hmC labeling. A 5caC-pre-deposited primer encodes which conversion step each amplicon comes from, so 5mC and 5hmC signals are recoverable from a single library. Combinatorial-indexing tagmentation scales to 10⁴–10⁵ cells per experiment.

## Why it matters

5mC and 5hmC have distinct regulatory roles. Prior single-cell methods (scAba-seq, scBS-seq) detect one modification at a time, losing within-molecule co-occurrence information.

## Examples

- mESCs 2i→serum transition: cells with high "modification entropy" mark transient reprogramming midpoints. Type-2 5hmCG sites (paired with 5mCG) mark dynamic methylation.
- Human PBMCs and mouse cerebral cortex profiled in the same paper ([[10-Summaries/bai-2024-simple-seq]]).

## Related

- [[30-Concepts/taps]] · [[30-Concepts/5hmc]] · [[40-Topics/dna-methylation]] · [[30-Concepts/tet-enzymes]] · [[30-Concepts/combinatorial-indexing]]
