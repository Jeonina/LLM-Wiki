---
type: summary
title: "Zhou et al. 2024 — scDMV: a zero–one inflated beta mixture model for DNA methylation variability with scBS-seq data"
source: "[[00-Sources/papers/scDMV_ a zero–one inflated beta mixture model for DNA methylation variability with scBS-seq data]]"
source_quality: full
source_sha256: "04508b36ac840475b2cda78ffab32cc86a88a46a1c89010bcf86bb9367d7011f"
source_kind: paper
author: "Yan Zhou, Ying Zhang, Minjiao Peng, Yaru Zhang, Chenghao Li, Lianjie Shu, Yaohua Hu, Jianzhong Su, Jinfeng Xu"
published: 2023-12-23
ingested: 2026-10-07
doi: "10.1093/bioinformatics/btad772"
journal: "Bioinformatics 40(1):btad772"
tags: [scDMV, differential-methylation, DMR, zero-one-inflated-beta, beta-binomial, EM-algorithm, Wald-test, scBS-seq, preimplantation-embryo, methylpy, CGmapTools]
entities: []
concepts: ["[[30-Concepts/scbs-seq]]", "[[30-Concepts/bisulfite-sequencing]]", "[[30-Concepts/cpg-island]]", "[[30-Concepts/pseudo-bulk]]"]
topics: ["[[40-Topics/dna-methylation]]", "[[40-Topics/computational-methods]]"]
---

**Citation:** Zhou et al. (2024) — *scDMV: a zero–one inflated beta mixture model for DNA methylation variability with scBS-seq data* — *Bioinformatics* 40(1):btad772. [DOI](https://doi.org/10.1093/bioinformatics/btad772)

# Zhou 2024 — scDMV

> Single-cell bisulfite data are sparse and per-cell regional methylation rates pile up at **exactly 0 or 1** (in the authors' real data, the 0 and 1 rates together exceed 0.9). scDMV calls **differentially methylated regions (DMRs) between two groups of cells** by modelling methylated read counts as binomial given a cell- and region-specific rate, and that rate as a **zero–one inflated beta** (point masses at 0 and 1 plus a beta component). Parameters are fit per region and group by EM; a **Wald test** on the group means plus a methylation-difference (Δ) cutoff defines DMRs. Comparators are two bulk-oriented tools, methylpy and CGmapTools.

## Key claims

- **Simulation (73 cells: 48 vs 25; 1,000 ten-CpG regions; five replicates)**: at P ≤ 0.01 and Δ ≥ 0, scDMV called 864/1,000 true DMRs in "difference" experiments and 1 in "indifference" (null) experiments; CGmapTools 549 / 10; methylpy 999 / **999** (i.e., no specificity). At Δ ≥ 0.2: scDMV 90, CGmapTools 21, methylpy 7, with no null calls. Simulated precision stayed above 0.98 for scDMV in all scenarios; methylpy's false positive rate was "notably high".
- **Real data (GSE81233; 25 four-cell vs 48 eight-cell embryo samples, hg19)**: precision is defined using a between-group test (calls assumed true) and a within-group split of 40 eight-cell samples into two groups of 20 (calls assumed false). At P cutoffs 0.001–0.01, scDMV precision >0.71 while the other methods did not reach 0.66; at P 0.05, scDMV >0.65 vs <0.59.
- **Biology at P ≤ 0.001, Δ ≥ 0.2**: 1,457 DMRs, **99.25% hypermethylated in 8-cell embryos** (consistent with the reported rise in global methylation from 4- to 8-cell); 49.69% intronic, 11.94% promoter, 4.95% in CpG islands. methylpy's DMRs were biased to CpG islands (9.02%) and shores (14.7%), attributed to its site-first-then-merge design.
- **Superset of CGmapTools**: scDMV's 1,457 DMRs include 512 of CGmapTools' 535 (95.7%); 308 shared DMR-genes. scDMV-specific DMR-genes are enriched for protein phosphorylation and nervous-system-development regulation.
- **Stated weakness**: region division is slow.

## Methods / evidence

Preprocessing: drop CpGs missing in >50% of samples; segment into regions ≤300 bp with ≥3 CpGs. Per region and group, EM estimates (π₀, π₁, α, β); the mean methylation and its variance (from the information matrix) feed a two-group Wald statistic. Δ is a weighted regional methylation difference. Annotation with ChIPseeker; GO via Metascape (biological process, BH-adjusted).

Weight: modest. Only two comparators, neither designed for single cells, and neither single-cell DMR/variability tool (e.g., scMET) is benchmarked. The simulation is generated from scDMV's own model, and its 0/1 fraction (~0.66) is well below the >0.9 the authors report for real data. Real-data "precision" treats every between-group call as true. Several citations in the clipping are visibly misattributed (e.g., Benjamini & Hochberg 1995 is cited for the embryo dataset and for methylation stability), so references should not be trusted without checking.

## Surprising or load-bearing bits

- **Methylpy, a standard bulk DMR caller, calls 999 of 1,000 null regions significant at Δ ≥ 0 in single-cell-like data** — treating cells as replicates under a bulk model is badly anti-conservative without an effect-size floor. (synthesis)
- **Precision falls as cutoffs tighten** in the real-data comparison (for scDMV and CGmapTools) — counter-intuitive, and a hint that the within-group "false positive" proxy behaves oddly. (synthesis)
- Despite the title's "variability", the test is for differences in **group mean** methylation; the zero–one inflation is a nuisance model rather than an analysis of cell-to-cell variability itself. (synthesis)

## Concepts touched

- [[scbs-seq]] — excess 0/1 regional rates and low coverage as the defining statistical problem.
- [[bisulfite-sequencing]] — region-level binomial counts of methylated vs total reads.
- [[cpg-island]] — DMR distribution relative to islands, shores, shelves and open sea.
- [[pseudo-bulk]] — the bulk-tool alternative it argues against (cells pooled as replicates).

## Connections to other sources

- Single-cell methylation variability/DMR models it does not benchmark: [[kapourani-2021-scmet]] (beta-binomial overdispersion; variable features), [[kremer-2024-methscan]] (variably methylated regions, smoothing).
- Imputation as an alternative response to sparsity: [[angermueller-2017-genomebiol]], [[zhao-2025-mambacpg]].
- scBS-seq origin: [[smallwood-2014-natmethods]]; developmental methylation context: [[smith-2013-methylation-development]].

## Open questions

- How does it compare with scMET or MethSCAn on the same data?
- Is the Wald test calibrated under real (>0.9) zero–one inflation, given simulations at ~0.66?
- Per-cell coverage heterogeneity is not weighted explicitly beyond read counts.

## Related

- [[kapourani-2021-scmet]] · [[kremer-2024-methscan]] · [[scbs-seq]] · [[40-Topics/dna-methylation]]
