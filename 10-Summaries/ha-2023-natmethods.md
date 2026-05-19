---
type: summary
title: "Ha 2023 — Comprehensive benchmarking and guidelines of mosaic variant calling strategies"
source: "[[00-Sources/papers/Comprehensive benchmarking and guidelines of mosaic variant calling strategies]]"
aliases: ["Ha 2023", "mosaic-caller benchmark", "Yoo-Jin Ha"]
tags: [benchmark, mosaic-variant-calling, MosaicHunter, MosaicForecast, DeepMosaic, MuTect2, M2SMH, Kim-lab, Yonsei]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Ha et al. (2023) — *Comprehensive benchmarking and guidelines of mosaic variant calling strategies* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-023-02043-2)

Ha, Kang, Kim, Kim, Jo and Kim (Yonsei, POSTECH) report the first comprehensive benchmark of 11 mosaic-variant-calling strategies on a constructed whole-exome-level reference standard built from controlled mixtures of six pre-genotyped normal cell lines. The reference comprises **354,258 control-positive mosaic SNVs/indels** and **33,111,725 control-negatives** across 39 mixtures spanning 0.5–56% VAF and three composition classes (M1/M2/M3 = 2-/3-/6-line mixtures).

The 11 strategies cover single-sample callers (MosaicHunter, MosaicForecast, DeepMosaic, MuTect2-tumor-only, HaplotypeCaller-p20/p200), paired-sample callers (Mutect2, Strelka2), and modified variants (MosaicHunter-modified, Mutect2-modified, **M2SMH** — a meta-strategy that intersects Mutect2 + Strelka2 + MosaicHunter). The benchmark evaluates VAF coverage, sequencing-depth dependence, variant-type robustness, call-set consistency, control-balance sensitivity, and misclassification mode-by-mode. Key recommendations: M2SMH is the best general-purpose strategy; MosaicHunter performs best at low VAF (<5%); paired-sample design is critical when bias from matched controls is unavoidable; combinatorial caller usage outperforms any single method.

## Why this matters

The definitive benchmark for mosaic-variant calling, directly informing our review's §4 recommendation section. Companion to but distinct from the scWGS-specific benchmarks (which evaluate LiRA, SCAN-SNV, ProSolo). Anchors §4 (variant calling tools), §6 (limitations and best practices), and §7 (future perspectives — the combinatorial-caller paradigm is likely the practical baseline going forward).

---
**Source:** [DOI](https://doi.org/10.1038/s41592-023-02043-2) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37828153/)

## Related

- [[10-Summaries/dou-2020-mosaicforecast]]
- [[10-Summaries/luquette-2019-natcomm]]
- [[40-Topics/mosaic-variant-calling]]
