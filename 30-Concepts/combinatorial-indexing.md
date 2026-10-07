---
type: concept
title: Combinatorial indexing
aliases: [split-pool barcoding, sci-method, combinatorial barcoding]
tags: [single-cell, library-prep, scalability, throughput]
created: 2026-05-12
updated: 2026-10-07
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

## Added 2026-10-07

CoBATCH applied two-round combinatorial indexing to histone marks. Barcoded PA-Tn5 transposomes (T5/T7) are loaded per well of a first 96-well plate holding 200–2,000 cells, and i5/i7 PCR indices are added on 20–25 cells per well of a second plate. This gives ~2,400 cells per 96-well plate at a ~7% species-mixing collision rate ([[10-Summaries/wang-2019-cobatch]]). Its stated limitation is a starting requirement of ≥~10,000 cells ([[10-Summaries/wang-2019-cobatch]]).

scFFPE-ATAC combines 64 Tn5 sample indexes with three 96-well ligation rounds for 56,623,104 barcode combinations per run, estimating a 2.77% collision rate for 50,000 input cells with the SHARE-seq birthday-paradox formula ([[10-Summaries/yadav-2025-scffpe-atac]]). On the analysis side, sciMETv3-scale combinatorial methylation data (145,219 cells) required purpose-built tooling, since most single-cell methylation packages could not hold even 1346 cells ([[10-Summaries/rylaarsdam-2025-amethyst]]).

**Three-tier indexing for methylation.** sciMETv3 adds an in situ ligation barcode between indexed tagmentation and PCR indexing, raising nuclei per final well from 15–60 (sciMETv2) to ~600–1,000 and enabling >140,000 human cortex methylomes from one preparation with a doublet bound of 3.4% ([[10-Summaries/nichols-2025-scimetv3]]).

sciMET-cap runs one hybrid-capture reaction on a pooled, combinatorially indexed sciMETv2 library, so a single capture serves thousands of cells ([[10-Summaries/acharya-2024-scimet-cap]]). Capture probes did not saturate when the cell count was doubled to about 4,000 per capture ([[10-Summaries/acharya-2024-scimet-cap]]).


## Related

- [[30-Concepts/icell8-nanowell]] · [[30-Concepts/scicut-tag]] · [[30-Concepts/simple-seq]] · [[30-Concepts/splicool-seq]]

## Added 2026-08-13

Extended to bisulfite sequencing by sci-MET, via **cytosine-depleted transposome adaptors** that survive conversion; the second adaptor is added after conversion by two to four rounds of random priming, making sci-MET a hybrid of indexed tagmentation and PBAT ([[10-Summaries/mulqueen-2018-sci-met]]).

**Nucleosome depletion chemistry silently sets the collision rate.** Lithium-3,5-diiodosalicylate gave a 22% barcode collision rate — unusable — while crosslinking + SDS gave 7.3%, in line with other sci- protocols ([[10-Summaries/mulqueen-2018-sci-met]]). An apparently upstream sample-prep choice determines the doublet rate of the whole experiment. (synthesis)

Throughput algebra is `N × D`: wells in the second indexing stage × pre-indexed nuclei per well; collision rate is tunable by D ([[10-Summaries/mulqueen-2018-sci-met]]). Efficiency across runs varied from 33.5% to 78.5%, a difference confounded with nucleosome-depletion chemistry (LAND vs xSDS) and run design ([[10-Summaries/mulqueen-2018-sci-met]]).
