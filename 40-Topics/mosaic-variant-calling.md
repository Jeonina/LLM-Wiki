---
type: topic
title: Mosaic variant calling
aliases: [mosaic SNV calling, low-VAF variant calling, mosaicism callers]
tags: [mosaicism, variant-calling, SNV, low-VAF, benchmarking]
created: 2026-05-19
updated: 2026-05-19
---

# Mosaic variant calling

> The algorithmic problem of detecting low-allele-frequency somatic variants from sequencing data — bulk DNA, single-cell DNA, or scRNA/scATAC. Mosaic variants violate the assumptions of germline callers (variant allele frequency ≪ 50%); specialized callers and reference benchmarks have proliferated ([[10-Summaries/ha-2023-natmethods]]).

## Core concepts

- [[30-Concepts/single-cell-variant-calling]] — the computational problem
- [[40-Topics/duplex-sequencing]] — fidelity at extreme low VAF
- [[30-Concepts/compounding-artifact]] — the failure mode of cascaded callers

## Callers

- [[10-Summaries/zafar-2016-monovar]] (Monovar) · [[10-Summaries/dong-2017-sccaller]] (SCcaller) · [[10-Summaries/sarah-2019-cell]] (ProSolo)
- [[10-Summaries/huang-2017-mosaichunter]] (MosaicHunter) · [[10-Summaries/dou-2020-mosaicforecast]] (MosaicForecast) · [[10-Summaries/yang-2023-deepmosaic]] (DeepMosaic)
- [[10-Summaries/dou-2023-monopogen]] (Monopogen) · [[10-Summaries/tu-2021-scout-genotyper]] (SCOUT)

## Benchmarks

- [[10-Summaries/ha-2023-natmethods]] — Ha 2023 comprehensive benchmark of 11 strategies.
- [[10-Summaries/zhang-2025-smaht-duplex-benchmark]] — SMaHT duplex-method cross-benchmark.

## Reviews

- [[10-Summaries/valecha-2022-scsnv-review]] · [[10-Summaries/lahnemann-2021-natcomm]] · [[10-Summaries/shao-2025-scDNA-mosaicism-review]]

## Open questions

- Per-cell call sensitivity at <1% VAF — still tool-dependent.
- Mutation-spectrum biases across callers — vary by tool.
- Integration with copy-number context — most callers ignore CNV state.

## Related

- [[40-Topics/somatic-mosaicism]] · [[40-Topics/scdna-seq]] · [[40-Topics/duplex-sequencing]]

## Linked summaries (lint pass 2026-05-21)

- [[10-Summaries/tu-2021-scout-genotyper]] — Tu 2021 — SCOUT genotyper using local genome territory.


## Added 2026-08-13

SCAN2 ([[10-Summaries/luquette-2021-scan2]]) is the PTA-native caller and the first to report a genome-wide single-neuron **indel** rate (≥2/year). Its more consequential result is a correction to a published biological constant: the neuronal SNV accumulation rate falls to **15 SNVs/year**, with the revision attributed to artifacts in older amplification chemistries.

That is the sharpest case in the corpus of chemistry determining a biological number — and it sits alongside the validation result from a decade earlier that only **19.4–27.0% of single-cell-only mutation calls survive orthogonal duplex confirmation** ([[10-Summaries/wang-2014-nuc-seq]]). Both point the same way: single-cell-only calls need an independent arbiter. (synthesis)

## Added 2026-08-17

[[10-Summaries/singer-2018-sciphi]] (SCIΦ) adds the joint-calling strategy the corpus was missing: rather than calling variants per cell or by pooling, use the **cell lineage tree as a prior** — a mutation can be assigned to a cell with very low or even zero variant-read support because the tree says it belongs there.

Its critique of the alternatives is precise ([[10-Summaries/singer-2018-sciphi]]): GATK and SAMtools assume bulk noise profiles; [[10-Summaries/zafar-2016-monovar|Monovar]] pools across cells but assumes independence across sites; [[10-Summaries/dong-2017-sccaller|SCcaller]] models local allelic amplification bias but works per cell, needs germline SNPs (unavailable for panel data), and **cannot recover mutations lost to dropout or LOH** — a structural limit of any per-cell caller, since an absent allele cannot be recovered from within one cell.

The risk is symmetric and unaddressed: when the tree is wrong, the same mechanism manufactures **correlated** false positives. (synthesis)
