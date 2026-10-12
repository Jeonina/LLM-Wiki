---
type: summary
title: "Ha 2023 — Comprehensive benchmarking and guidelines of mosaic variant calling strategies"
source: "[[00-Sources/papers/Comprehensive benchmarking and guidelines of mosaic variant calling strategies]]"
source_quality: full
source_sha256: "29aa4b28fae9c7ae7becd9f65d7495a77a7783f58cc726731076bc1f5f19cc6c"
aliases: ["Ha 2023", "mosaic-caller benchmark", "Yoo-Jin Ha"]
tags: [benchmark, mosaic-variant-calling, MosaicHunter, MosaicForecast, DeepMosaic, MuTect2, M2SMH, Kim-lab, Yonsei]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Ha et al. (2023) — *Comprehensive benchmarking and guidelines of mosaic variant calling strategies* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-023-02043-2)

> [!abstract] 한눈에
> Ha 등은 세포주 혼합으로 만든 reference standard에서 mosaic variant calling 전략 11가지를 처음으로 종합 benchmark했다. 단일 시료 mosaic SNV에는 MosaicForecast와 Mutect2 tumor-only가 가장 좋았고, caller 간 결과가 크게 달라 단순 교집합은 오히려 정확도를 떨어뜨렸다.

Ha, Kang, Kim, Kim, Jo and Kim (Yonsei, POSTECH) report the first comprehensive benchmark of 11 mosaic-variant-calling strategies on a constructed whole-exome-level reference standard built from controlled mixtures of six pre-genotyped normal cell lines. The reference comprises **354,258 control-positive mosaic SNVs/indels** and **33,111,725 control-negatives** across 39 mixtures spanning 0.5–56% VAF and three categories (M1/M2/M3 = 9/12/18 mixtures).

The 11 strategies cover single-sample callers (MosaicHunter, MosaicForecast, DeepMosaic, MuTect2-tumor-only, HaplotypeCaller-p20/p200), paired-sample callers (Mutect2, Strelka2), and modified variants (MosaicHunter-modified, Mutect2-modified, **M2S2MH** — an ensemble that integrates Mutect2 + Strelka2 + MosaicHunter with read-level filtration). The benchmark evaluates VAF coverage, sequencing-depth dependence, variant-type robustness, call-set consistency, control-balance sensitivity, and misclassification mode-by-mode. Key findings: MosaicForecast and Mutect2 tumor-only are best for single-sample mosaic SNVs at 4–25% VAF; M2S2MH gives near-perfect precision but lower sensitivity; callers are highly discordant, and naive intersection lowers accuracy while feature-level recombination improves it.

## Why this matters

The definitive benchmark for mosaic-variant calling, directly informing our review's §4 recommendation section. Companion to but distinct from the scWGS-specific benchmarks (which evaluate LiRA, SCAN-SNV, ProSolo). Anchors §4 (variant calling tools), §6 (limitations and best practices), and §7 (future perspectives — the combinatorial-caller paradigm is likely the practical baseline going forward).

---
**Source:** [DOI](https://doi.org/10.1038/s41592-023-02043-2) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37828153/)

## Related

- [[10-Summaries/dou-2020-mosaicforecast]]
- [[10-Summaries/luquette-2019-natcomm]]
- [[40-Topics/mosaic-variant-calling]]
