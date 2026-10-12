---
type: concept
title: Quality Control Metrics
aliases: [QC metrics, library QC, spikiness]
tags: [QC, filtering, library-quality, benchmarking]
created: 2026-08-10
updated: 2026-10-12
---

# Quality Control Metrics

> The per-library and per-cell statistics used to decide which data enter an analysis. In single-cell work these are not hygiene — they materially determine the result, because a failed library and a biologically unusual cell are hard to distinguish (synthesis; see [[10-Summaries/zhou-2019-schicluster|scHiCluster]]; [[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]).

> [!abstract] 한눈에
> QC metric은 어떤 library와 세포를 분석에 넣을지 정하는 통계이고, single-cell에서는 실패한 library와 생물학적으로 특이한 세포를 가리기 어려워 결과 자체를 좌우한다. 예를 들어 single-cell Hi-C clustering을 가장 크게 움직이는 요인은 생물학보다 coverage 차이다 ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]).

## Definition

Quality control metrics are the per-library and per-cell statistics used to decide which data enter an analysis. They differ by assay: copy-number noise for scWGS, collision rates for combinatorial indexing, contact statistics for scHi-C, conversion and composition checks for WGBS, and target-specific enrichment for scCUT&Tag (see table below).

## Why it matters

- **Coverage heterogeneity is the leading factor driving single-cell Hi-C clustering results**, ahead of biology, and it is not removable by dropping PC1 ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]).
- **A "cellular index" is not a cell.** Coverage per index is bimodal, with the low mode representing barcoded free DNA rather than intact nuclei ([[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]).
- **Within-species barcode collisions are invisible** to species-mixing controls and are estimated at ~4.5% ([[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]).
- **Cell-type assignment can come from the data**: three of twenty "tumour" cells were reassigned as normal on their mutation profiles alone ([[10-Summaries/xu-2012-single-cell-exome-kidney|Xu 2012]]).
- Publishing the artefact rule matters — 13% of subtypes annotated as likely doublet artefacts, with the threshold stated ([[10-Summaries/cao-2019-moca|Cao 2019]]). See [[doublet-detection]].

## Metrics by assay

| Assay | Metric | What it flags or reports | Source |
|---|---|---|---|
| scWGS (copy number) | **Spikiness** — bin-to-bin variation in read count — combined with model log-likelihood, segment count and the Bhattacharyya distance between fitted distributions, then clustered | Separates a genuinely segmented genome from a noisy library; retained ~89% of libraries | ([[10-Summaries/bakker-2016-aneufinder\|AneuFinder]]) |
| scWGS (copy number) | MAD on a diploid chromosome | The same diagnostic, reached independently | ([[10-Summaries/zahn-2017-dlp\|Zahn 2017]]) |
| Plate-based scWGS | Imaging before library construction | Distinguishes single cells from doublets and debris at the bench rather than computationally | ([[10-Summaries/zahn-2017-dlp\|Zahn 2017]]; [[10-Summaries/laks-2019-dlp-plus\|Laks 2019]]) |
| Any short-read library | Pre- versus post-filter profiles on one page | Makes the effect of preprocessing directly visible | ([[10-Summaries/chen-2018-fastp\|fastp]]) |
| Combinatorial indexing | Species-mixing collision rate | 0.006–0.008% for sciHi-C; 3% for sci-RNA-seq3 | ([[10-Summaries/ramani-2017-scihi-c\|Ramani 2017]]; [[10-Summaries/cao-2019-moca\|Cao 2019]]) |
| scHi-C | cis:trans ratio | Per-cell Hi-C quality; ~4.4 in sciHi-C | ([[10-Summaries/ramani-2017-scihi-c\|Ramani 2017]]) |
| scHi-C | Per-cell contact cutoffs from 1,000 to 5,000, plus cis/trans >1, ≥95% uniquely mapped reads, short/long-range contact ratios and presence of all chromosomes | Static, empirical filters used across studies | ([[10-Summaries/dautle-2025-schic-review\|Dautle 2025]]) |
| scHi-C | GiniQC | How clumped the trans contacts are; described as the only package whose filtering accounts for contact type and coverage | ([[10-Summaries/dautle-2025-schic-review\|Dautle 2025]]) |
| WGBS | Bismark bam2nuc | Mono- and dinucleotide composition versus genomic expectation: C depletion flags BS degradation; C enrichment flags poor conversion; G or AT skews flag polymerase bias | ([[10-Summaries/olova-2018-wgbs-library-bias\|Olova 2018]]) |
| WGBS | Bismark filter_non_conversion | Removes reads with ≥3 unconverted CH cytosines | ([[10-Summaries/olova-2018-wgbs-library-bias\|Olova 2018]]) |
| scCUT&Tag | FRiP and TSS enrichment, set per target | H3K4me3 shows high TSS enrichment, H3K9me3 minimal enrichment; for H3K27me3 a TSS chromatin silencing score is low at active genes | ([[10-Summaries/wu-2026-sccut-tag-review\|Wu 2026]]) |

## Evidence and examples

- For WGBS, requiring minimum per-CpG coverage (≥5 or ≥10×) reinforces coverage bias; averaging per-cytosine values within regions is less biased than pooling calls ([[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]).
- Filtering scHPTM cells by coverage gives only modest gains (max 15% for ChromSCape_LSI on H3K4me1), so the benchmark advises removing only non-cell barcodes ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]).

## Contested points

- **Thresholds do not transfer between assays.** scATAC cut-offs (FRiP <0.2, TSS enrichment <6–8×) do not transfer to scCUT&Tag, where thresholds must be set per target ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).
- **scHi-C QC is mostly static and empirical**, with GiniQC the exception that accounts for contact type and coverage ([[10-Summaries/dautle-2025-schic-review|Dautle 2025]]).
- **Strict filtering can add bias.** Minimum-coverage filters reinforce WGBS coverage bias ([[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]), and coverage filtering of scHPTM cells gives only modest gains ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]); both argue against aggressive filtering as a default (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/doublet-detection|Doublet detection]] — Finding barcodes that hold more than one cell.
> - `concept` [[30-Concepts/duplicate-marking|Duplicate marking]] — Flagging PCR and optical duplicates before calling.
> - `concept` [[30-Concepts/mappability|Mappability]] — How uniquely reads can be placed, which shapes coverage QC.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — Analysis tools across the single-cell layers.

## All sources on this page

> [!info]- 12 summaries cited here
> - [[10-Summaries/bakker-2016-aneufinder|Bakker 2016]]
> - [[10-Summaries/cao-2019-moca|Cao 2019]]
> - [[10-Summaries/chen-2018-fastp|Chen 2018]]
> - [[10-Summaries/dautle-2025-schic-review|Dautle 2025]]
> - [[10-Summaries/laks-2019-dlp-plus|Laks 2019]]
> - [[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]
> - [[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]
> - [[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]
> - [[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]
> - [[10-Summaries/xu-2012-single-cell-exome-kidney|Xu 2012]]
> - [[10-Summaries/zahn-2017-dlp|Zahn 2017]]
> - [[10-Summaries/zhou-2019-schicluster|Zhou 2019]]
