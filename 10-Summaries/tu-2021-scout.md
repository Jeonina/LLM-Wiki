---
type: summary
title: "Tu 2021 — SCOUT: accurate single-cell genotyping using local genome territory"
aliases: ["Tu 2021 SCOUT", "SCOUT genotyper"]
tags: [SCOUT, scDNA-SNV-calling, local-genome-territory, no-external-data, Xie-lab, Sichuan]
created: 2026-05-13
updated: 2026-05-13
sources: ["Accurate single-cell genotyping utilizing information from the local genome territory.md"]
---

**Citation:** Tu et al. (2021) — *SCOUT: accurate single-cell genotyping using local genome territory* — *?*.

Tu, Lu, Zhang, Huang, Xie (Sichuan University) developed **SCOUT** (Single Cell Genotyper Utilizing Information from Local Genome Territory), an scDNA SNV caller that does NOT require external bulk or other-cell data. Conditional local-smoothing mixture generative model classifies candidate SNVs into homozygous/heterozygous/intermediate/low-major-allele states using base counts from adjacent SNVs in the same cell. Improves F1 by 2.0–77.5% vs GATK/SCcaller/Monovar; 400% faster.

## Why this matters

Addresses the limitation of Monovar/SCcaller/SCAN-SNV which require external data. SCOUT operates on a single cell alone — useful for rare clones, minor subpopulations, or when bulk samples are unmatched. Anchors §4 (variant calling tool family).

---
**Source:** [Open paper](https://academic.oup.com/nar/article/49/10/e57/6146636)
## Related

- [[10-Summaries/zafar-2016-monovar]]
- [[10-Summaries/dong-2017-sccaller]]
- [[10-Summaries/ha-2023-natmethods]]
