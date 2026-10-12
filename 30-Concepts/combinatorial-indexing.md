---
type: concept
title: Combinatorial indexing
aliases: [split-pool barcoding, sci-method, combinatorial barcoding]
tags: [single-cell, library-prep, scalability, throughput]
created: 2026-05-12
updated: 2026-10-12
---

# Combinatorial indexing

> A single-cell library-preparation strategy that uses multiple rounds of split-pool barcoding to give each cell a unique combination of barcodes — scaling cell numbers exponentially with the number of split-pool rounds ([[10-Summaries/mulqueen-2018-sci-met|Mulqueen 2018]]; [[10-Summaries/yadav-2025-scffpe-atac|Yadav 2025]]).

> [!abstract] 한눈에
> Combinatorial indexing은 세포를 여러 번 나눠 담고 모으면서 라운드마다 barcode를 붙여, 적은 수의 oligo로 수만에서 수십만 세포를 구분하는 방법이다 ([[10-Summaries/nichols-2025-scimetv3|Nichols 2025]]). 처리량은 well 수와 well당 핵 수로 정해지고, collision rate는 그중 well당 핵 수와 핵 준비 화학 같은 상류 단계에 크게 좌우된다 ([[10-Summaries/mulqueen-2018-sci-met|Mulqueen 2018]]).

## Definition

Cells are partitioned into N wells, each receiving a unique first-round barcode; cells are then pooled and re-partitioned into M wells with second-round barcodes. Two rounds therefore yield N × M cell-distinguishable barcode combinations from N + M synthesized oligos (synthesis).

Throughput algebra is `N × D`: wells in the second indexing stage × pre-indexed nuclei per well, and the collision rate is tunable by D ([[10-Summaries/mulqueen-2018-sci-met|Mulqueen 2018]]).

## Why it matters

- It scales single-cell methods to 10⁴–10⁶ cells per experiment at low cost (synthesis); sciMETv3 reached >140,000 human cortex methylomes from one preparation ([[10-Summaries/nichols-2025-scimetv3|Nichols 2025]]).
- It is used in [[30-Concepts/simple-seq]] (5mC + 5hmC), [[30-Concepts/splicool-seq]] (5mC + accessibility), [[30-Concepts/scicut-tag]] (histone modifications), sciATAC-seq, sci-MET (DNA methylation), Sci-LIANTI and others (synthesis).
- At sciMETv3 scale (145,219 cells) the data need purpose-built tooling, since most single-cell methylation packages could not hold even 1346 cells ([[10-Summaries/rylaarsdam-2025-amethyst|Amethyst]]).

## Implementations

| Method | Layer | Indexing design | Scale and collisions | Source |
|---|---|---|---|---|
| [[30-Concepts/scicut-tag\|sciCUT&Tag]] | Histone modifications | 96 first-round barcodes × 5,184 [[30-Concepts/icell8-nanowell\|ICELL8 nanowells]] | ~40k cells per chip | see [[30-Concepts/scicut-tag]] |
| CoBATCH | Histone modifications | Barcoded PA-Tn5 transposomes (T5/T7) per well of a first 96-well plate holding 200–2,000 cells; i5/i7 PCR indices on 20–25 cells per well of a second plate | ~2,400 cells per 96-well plate; ~7% species-mixing collision rate | ([[10-Summaries/wang-2019-cobatch\|CoBATCH]]) |
| scFFPE-ATAC | Chromatin accessibility | 64 Tn5 sample indexes plus three 96-well ligation rounds | 56,623,104 barcode combinations per run; estimated 2.77% collision rate for 50,000 input cells (SHARE-seq birthday-paradox formula) | ([[10-Summaries/yadav-2025-scffpe-atac\|Yadav 2025]]) |
| sci-MET | DNA methylation | Cytosine-depleted transposome adaptors that survive bisulfite conversion; second adaptor added after conversion by two to four rounds of random priming — a hybrid of indexed tagmentation and PBAT | 7.3% collision rate with crosslinking + SDS | ([[10-Summaries/mulqueen-2018-sci-met\|Mulqueen 2018]]) |
| sciMETv3 | DNA methylation | Three tiers: an in situ ligation barcode between indexed tagmentation and PCR indexing | Nuclei per final well raised from 15–60 (sciMETv2) to ~600–1,000; >140,000 methylomes; doublet bound 3.4% | ([[10-Summaries/nichols-2025-scimetv3\|Nichols 2025]]) |
| sciMET-cap | Targeted DNA methylation | One hybrid-capture reaction on a pooled, combinatorially indexed sciMETv2 library, so a single capture serves thousands of cells | Probes did not saturate at ~4,000 cells per capture | ([[10-Summaries/acharya-2024-scimet-cap\|sciMET-cap]]) |

## Evidence and examples

- In sci-MET, nucleosome depletion with lithium-3,5-diiodosalicylate gave a 22% barcode collision rate — unusable — while crosslinking + SDS gave 7.3%, in line with other sci- protocols ([[10-Summaries/mulqueen-2018-sci-met|Mulqueen 2018]]).
- sci-MET efficiency across runs varied from 33.5% to 78.5%, a difference confounded with nucleosome-depletion chemistry (LAND vs xSDS) and run design ([[10-Summaries/mulqueen-2018-sci-met|Mulqueen 2018]]).
- sciMET-cap probes did not saturate when the cell count was doubled to about 4,000 per capture ([[10-Summaries/acharya-2024-scimet-cap|sciMET-cap]]).

## Contested points

- **Upstream sample prep sets the doublet rate.** Because nucleosome-depletion chemistry changed sci-MET's collision rate from 7.3% to 22% ([[10-Summaries/mulqueen-2018-sci-met|Mulqueen 2018]]), an apparently upstream choice determines the doublet rate of the whole experiment (synthesis).
- **Input requirement.** CoBATCH's stated limitation is a starting requirement of ≥~10,000 cells ([[10-Summaries/wang-2019-cobatch|CoBATCH]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/icell8-nanowell|ICELL8 nanowell]] — Nanowell chip used as the second indexing round in sciCUT&Tag.
> - `concept` [[30-Concepts/scicut-tag|sciCUT&Tag]] — Combinatorially indexed single-cell CUT&Tag for histone marks.
> - `concept` [[30-Concepts/simple-seq|SIMPLE-seq]] — Joint 5mC + 5hmC profiling by combinatorial indexing.
> - `concept` [[30-Concepts/splicool-seq|SpliCOOL-seq]] — Joint 5mC + accessibility profiling by combinatorial indexing.

## All sources on this page

> [!info]- 6 summaries cited here
> - [[10-Summaries/acharya-2024-scimet-cap|Acharya 2024]]
> - [[10-Summaries/mulqueen-2018-sci-met|Mulqueen 2018]]
> - [[10-Summaries/nichols-2025-scimetv3|Nichols 2025]]
> - [[10-Summaries/rylaarsdam-2025-amethyst|Rylaarsdam 2025]]
> - [[10-Summaries/wang-2019-cobatch|Wang 2019]]
> - [[10-Summaries/yadav-2025-scffpe-atac|Yadav 2025]]
