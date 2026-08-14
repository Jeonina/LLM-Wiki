---
type: concept
title: Combinatorial indexing
aliases: [split-pool barcoding, sci-method, combinatorial barcoding]
tags: [single-cell, library-prep, scalability, throughput]
created: 2026-05-12
updated: 2026-05-12
---

# Combinatorial indexing

> A single-cell library-preparation strategy that uses multiple rounds of split-pool barcoding to give each cell a unique combination of barcodes — scaling cell numbers exponentially with the number of split-pool rounds.

## Definition

Cells are partitioned into N wells, each receiving a unique first-round barcode; cells are then pooled and re-partitioned into M wells with second-round barcodes. With N × M possible barcode combinations, two rounds yield N×M cell-distinguishable barcode combinations from N+M synthesized oligos.

## Why it matters

- Scales single-cell methods to 10⁴–10⁶ cells per experiment at low cost.
- Used in [[30-Concepts/simple-seq]] (5mC + 5hmC), [[30-Concepts/splicool-seq]] (5mC + accessibility), [[30-Concepts/scicut-tag]] (histone modifications), sciATAC-seq, sci-MET (DNA methylation), Sci-LIANTI, etc.

## Examples

- 96 (first round) × 5,184 ICELL8 nanowells (second round) → 40k cells/chip in [[30-Concepts/scicut-tag]].

## Related

- [[30-Concepts/icell8-nanowell]] · [[30-Concepts/scicut-tag]] · [[30-Concepts/simple-seq]] · [[30-Concepts/splicool-seq]]

## Added 2026-08-13

Extended to bisulfite sequencing by sci-MET, via **cytosine-depleted transposome adaptors** that survive conversion; the second adaptor is added after conversion by five rounds of random priming, making sci-MET a hybrid of indexed tagmentation and PBAT ([[10-Summaries/mulqueen-2018-sci-met]]).

**Nucleosome depletion chemistry silently sets the collision rate.** Lithium-3,5-diiodosalicylate gave a 22% barcode collision rate — unusable — while crosslinking + SDS gave 7.3%, in line with other sci- protocols ([[10-Summaries/mulqueen-2018-sci-met]]). An apparently upstream sample-prep choice determines the doublet rate of the whole experiment. (synthesis)

Throughput algebra is `N × D`: wells in the second indexing stage × pre-indexed nuclei per well; collision rate is tunable by D ([[10-Summaries/mulqueen-2018-sci-met]]). Efficiency across runs varied from 33.5% to 78.5% with no stated chemistry change ([[10-Summaries/mulqueen-2018-sci-met]]).
