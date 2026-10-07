---
type: concept
title: Quality Control Metrics
aliases: [QC metrics, library QC, spikiness]
tags: [QC, filtering, library-quality, benchmarking]
created: 2026-08-10
updated: 2026-10-07
---

# Quality Control Metrics

> The per-library and per-cell statistics used to decide which data enter an analysis. In single-cell work these are not hygiene — they materially determine the result, because a failed library and a biologically unusual cell are hard to distinguish.

## Common metrics

- **Spikiness** — bin-to-bin variation in read count, separating a genuinely segmented genome from a noisy library; combined with model log-likelihood, segment count and the Bhattacharyya distance between fitted distributions, then clustered to retain ~89% of libraries ([[bakker-2016-aneufinder]]).
- **MAD on a diploid chromosome** — the same diagnostic reached independently ([[zahn-2017-dlp]]).
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

## Added 2026-10-07

For WGBS, Bismark's bam2nuc module compares mono- and dinucleotide composition with genomic expectation (C depletion flags BS degradation; C enrichment flags poor conversion; G or AT skews flag polymerase bias), and filter_non_conversion removes reads with ≥3 unconverted CH cytosines [[10-Summaries/olova-2018-wgbs-library-bias]]. Requiring minimum per-CpG coverage (≥5 or ≥10×) reinforces coverage bias; averaging per-cytosine values within regions is less biased than pooling calls [[10-Summaries/olova-2018-wgbs-library-bias]].

scHi-C quality control is mostly static and empirical. Studies use per-cell contact cutoffs from 1,000 to 5,000, plus cis/trans >1, ≥95% uniquely mapped reads, short/long-range contact ratios and presence of all chromosomes ([[10-Summaries/dautle-2025-schic-review]]). GiniQC is described as the only package whose filtering accounts for contact type and coverage, which it does by measuring how clumped the trans contacts are ([[10-Summaries/dautle-2025-schic-review]]).

In scCUT&Tag, FRiP and TSS-enrichment thresholds must be set per target: H3K4me3 shows high TSS enrichment, H3K9me3 shows minimal enrichment, and for H3K27me3 a TSS chromatin silencing score is low at active genes, so scATAC cut-offs (FRiP <0.2, TSS enrichment <6–8×) do not transfer ([[10-Summaries/wu-2026-sccut-tag-review]]). Filtering scHPTM cells by coverage gives only modest gains (max 15% for ChromSCape_LSI on H3K4me1), so the benchmark advises removing only non-cell barcodes ([[10-Summaries/raimundo-2023-schptm-benchmark]]).


## Related

- [[doublet-detection]] · [[duplicate-marking]] · [[mappability]] · [[computational-methods]]
