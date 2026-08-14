---
type: concept
title: Single-cell variant calling
aliases: [scSNV calling, single-cell SNV detection, scDNA variant calling]
tags: [scDNA-seq, variant-calling, SNV, computational]
created: 2026-05-19
updated: 2026-08-10
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

## The bulk null model these tools reject

- **GATK is the substrate and the assumption.** Its locus-based traversal (all reads spanning each base, plus reference-ordered data) is the data model every single-cell caller inherits; what they replace is its **diploid, uniform-coverage prior**, which WGA violates ([[10-Summaries/mckenna-2010-gatk]]).
- The demonstration genotyper in that paper is explicitly naïve — 99.76% concordance but only 81.70% dbSNP rate against ~90% expected, i.e. an honestly-reported false-positive problem ([[10-Summaries/mckenna-2010-gatk]]).
- **Multi-locus traversals were never implemented** in the original framework and were flagged as memory-expensive — which is why haplotype-aware and phasing-based methods needed separate engineering rather than a walker ([[10-Summaries/mckenna-2010-gatk]]).
- **LOH detection reuses the same logic in reverse**: restrict to ancestral heterozygous sites, then read allele fraction, calling tracts from ≥3 consecutive deviating SNPs ([[10-Summaries/smukowski-heil-2023-loh]]). In single cells this collides with allele dropout, which produces the identical signature.
- **Clone-level aggregation is the amplification-free alternative** to per-cell calling: cluster on copy number, treat each clone as pseudo-bulk, then call SNVs, breakpoints and allele-specific copy number per clone ([[10-Summaries/laks-2019-dlp-plus]]).

## Related

- [[40-Topics/scdna-seq]] · [[40-Topics/mosaic-variant-calling]] · [[40-Topics/duplex-sequencing]]
- [[40-Topics/scdna-seq]] · [[40-Topics/mosaic-variant-calling]]
- [[10-Summaries/mckenna-2010-gatk]] · [[10-Summaries/smukowski-heil-2023-loh]] · [[10-Summaries/laks-2019-dlp-plus]]

## Added 2026-08-13

SCAN2 extends the SCAN line from SNVs to **indels** and is matched to [[30-Concepts/pta|PTA]] rather than MDA ([[10-Summaries/luquette-2021-scan2]]). The consequence is not just a new variant class but a revised biological constant: neuronal somatic SNV accumulation drops to **15 SNVs/year**, with the revision attributed to artifacts in the older amplification chemistries ([[10-Summaries/luquette-2021-scan2]]). Somatic indels accumulate at ≥2/year per neuron and may have larger functional impact per event ([[10-Summaries/luquette-2021-scan2]]).

Indels were effectively unmeasurable before PTA because MDA's polymerase-slippage artifacts sit on top of the indel signal — getting a rate at all is a chemistry result as much as an algorithm result. (synthesis)

**Validation is the recurring weak point.** Duplex sequencing of nuc-seq calls found that only **19.4–27.0% of single-cell-only ("de novo") mutations validated**, against 90.5–64.8% of subclonal and 94.4–99.7% of clonal calls ([[10-Summaries/wang-2014-nuc-seq]]). Read the other way: the majority of single-cell-only calls are artifact even in a high-quality library — which is why the field converged on orthogonal duplex confirmation ([[50-Notes/single-cell-duplex-sequencing]]). (synthesis)

The abundance-inversion problem these callers negotiate — where an artifact in a well-amplified region outweighs a true signal in a poorly-amplified one — was first named a decade earlier in [[30-Concepts/single-cell-genome-assembly|single-cell assembly]] ([[10-Summaries/peng-2012-idba-ud]]). (synthesis)
