---
type: concept
title: Quality Control Metrics
aliases: [QC metrics, library QC, spikiness]
tags: [QC, filtering, library-quality, benchmarking]
created: 2026-08-10
updated: 2026-08-10
---

# Quality Control Metrics

> The per-library and per-cell statistics used to decide which data enter an analysis. In single-cell work these are not hygiene — they materially determine the result, because a failed library and a biologically unusual cell are hard to distinguish.

## Common metrics

- **Spikiness** — bin-to-bin variation in read count, separating a genuinely segmented genome from a noisy library; combined with model log-likelihood, segment count and the Bhattacharyya distance between fitted distributions, then clustered to retain ~89% of libraries ([[bakker-2016-aneufinder]]).
- **MAD on a diploid chromosome** — the same diagnostic reached independently, used with a MAD < 0.15 filter ([[zahn-2017-dlp]]).
- **Pre- versus post-filter profiles** on one page, so the effect of preprocessing is directly visible ([[chen-2018-fastp]]).
- **Species-mixing collision rate** — 0.006–0.008% for sciHi-C ([[ramani-2017-scihi-c]]), 3% for sci-RNA-seq3 ([[cao-2019-moca]]).
- **cis:trans ratio** as a per-cell Hi-C quality measure, ~4.4 in sciHi-C ([[ramani-2017-scihi-c]]).
- **Imaging before library construction**, distinguishing single cells from doublets and debris at the bench rather than computationally ([[zahn-2017-dlp]], [[laks-2019-dlp-plus]]).

## Why it is a substantive step

- **Coverage heterogeneity is the leading factor driving single-cell Hi-C clustering results**, ahead of biology, and it is not removable by dropping PC1 ([[zhou-2019-schicluster]]).
- **A "cellular index" is not a cell.** Coverage per index is bimodal, with the low mode representing barcoded free DNA rather than intact nuclei ([[ramani-2017-scihi-c]]).
- **Within-species barcode collisions are invisible** to species-mixing controls and are estimated at ~4.5% ([[ramani-2017-scihi-c]]).
- **Cell-type assignment can come from the data**: three of twenty "tumour" cells were reassigned as normal on their mutation profiles alone ([[xu-2012-single-cell-exome-kidney]]).
- Publishing the artefact rule matters — 13% of subtypes annotated as likely doublet artefacts, with the threshold stated ([[cao-2019-moca]]). See [[doublet-detection]].

## Related

- [[doublet-detection]] · [[duplicate-marking]] · [[mappability]] · [[computational-methods]]
