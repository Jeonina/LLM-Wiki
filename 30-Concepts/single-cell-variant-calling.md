---
type: concept
title: Single-cell variant calling
aliases: [scSNV calling, single-cell SNV detection, scDNA variant calling]
tags: [scDNA-seq, variant-calling, SNV, computational]
created: 2026-05-19
updated: 2026-05-19
---

# Single-cell variant calling

> Algorithms for detecting somatic single-nucleotide variants and indels from single-cell DNA sequencing data, which is dominated by amplification artifacts, allelic dropout, and uneven coverage that conventional bulk callers (GATK, MuTect2) handle poorly ([[10-Summaries/valecha-2022-scsnv-review]]; [[10-Summaries/lahnemann-2021-natcomm]]).

## Major tools

- **Monovar** ([[10-Summaries/zafar-2016-monovar]]) — first scSNV caller; multi-cell joint likelihood.
- **SCcaller** ([[10-Summaries/dong-2017-sccaller]]) — local-allele-frequency model.
- **ProSolo** ([[10-Summaries/sarah-2019-cell]]) — pairs bulk + single-cell.
- **MosaicHunter** ([[10-Summaries/huang-2017-mosaichunter]]) — control-free mosaic SNV detection.
- **MosaicForecast** ([[10-Summaries/dou-2020-mosaicforecast]]) — random-forest classifier.
- **DeepMosaic** ([[10-Summaries/yang-2023-deepmosaic]]) — deep-learning mosaic caller.
- **Monopogen** ([[10-Summaries/dou-2023-monopogen]]) — SNV calls from scRNA/scATAC.
- **SCOUT** ([[10-Summaries/tu-2021-scout-genotyper]]) — leverages local genome territory for genotyping.

## Benchmarks

[[10-Summaries/ha-2023-natmethods]] benchmarks 11 strategies on a constructed reference standard from 6 mixed cell lines.

## Related

- [[30-Concepts/scdna-seq]] · [[40-Topics/mosaic-variant-calling]] · [[30-Concepts/duplex-sequencing]]
- [[40-Topics/scdna-seq]] · [[40-Topics/mosaic-variant-calling]]
