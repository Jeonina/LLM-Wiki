---
type: summary
title: "Ivanovic & El-Kebir 2025 — CNRein: an evolution-aware deep reinforcement learning algorithm for single-cell DNA copy number calling"
source: "[[00-Sources/papers/CNRein_ an evolution-aware deep reinforcement learning algorithm for single-cell DNA copy number calling]]"
source_quality: full
source_sha256: "23ad431429962cfb564d85a451b6cf30657d957e4a4c58424437c3ce7134042c"
source_kind: paper
author: "Stefan Ivanovic, Mohammed El-Kebir (corresponding)"
published: 2025-04-07
ingested: 2026-10-12
doi: "10.1186/s13059-025-03553-2"
journal: "Genome Biology"
aliases: ["Ivanovic 2025", "CNRein", "CNNaive"]
tags: [CNRein, haplotype-specific-copy-number, allele-specific-CNV, copy-number-calling, deep-reinforcement-learning, policy-gradient, evolutionary-model, CNA-tree, maximum-parsimony, whole-genome-doubling, 10x-CNV, DLP+, ACT, breast-cancer, ovarian-cancer, SIGNALS, CHISEL, Alleloscope, El-Kebir-lab]
entities: []
concepts: ["[[copy-number-variation]]", "[[phylogenetic-inference]]", "[[intratumor-heterogeneity]]", "[[whole-genome-doubling]]", "[[dlp-plus]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[cancer-clonal-evolution]]", "[[computational-methods]]", "[[scdna-cancer-applications]]"]
---

**Citation:** Ivanovic & El-Kebir (2025) — *CNRein: an evolution-aware deep reinforcement learning algorithm for single-cell DNA copy number calling* — *Genome Biology*. [DOI](https://doi.org/10.1186/s13059-025-03553-2)

# Ivanovic 2025 — CNRein

> Haplotype-specific copy-number callers for low-pass scDNA-seq (CHISEL, SIGNALS, Alleloscope) fit each cell more or less on its own, so measurement noise turns into spurious cell-specific CNAs that no plausible evolutionary history would produce. **CNRein** instead learns, per tumour, a generative model of CNA evolution: a copy-number profile is built from the normal cell by a sequence of haplotype-specific segmental gains/losses (or a WGD), each step's probability given by a convolutional neural network. The network is trained by policy-gradient reinforcement learning to maximize the probability of all cells' read depth and BAF. Each cell then gets the profile that best balances its own data with the shared model. The premise is that one should infer cell-specific CNAs only on strong evidence and otherwise prefer shared clonal structure.

> [!abstract] 한눈에
> CNRein은 강화학습으로 종양별 CNA 진화 생성 모델을 학습해, 저심도 scDNA-seq에서 haplotype별 copy number를 세포 간 공유 구조로 정규화하며 호출한다. 시뮬레이션에서 SIGNALS와 CHISEL보다 정확했고, 두 도구가 사실상 모든 세포에 고유 프로파일을 부여해 이질성을 과대평가함을 보였다.

## Key claims

- **Evolution as a regularizer.** Existing haplotype-specific callers do not use evolutionary constraints to estimate profiles jointly across cells. In CNRein the level of heterogeneity comes from training on the data, not from *post hoc* clustering of called profiles. The method is unsupervised and does not need normal cells, so FACS-sorted tumour-only data work.
- **Simulations (20 instances, 1000 cells, 27,283 bins of 100 kb, half with truncal WGD, noise based on patient S0):** median accuracy (exact unordered allele-specific CN per bin) 0.956 for CNRein vs 0.882 SIGNALS and 0.857 CHISEL; median L1 error 0.064 vs 0.191 CHISEL and 0.315 SIGNALS. Lower error also held for focal CNAs (<5 Mb) and haplotype-specific CN.
- **Number of unique profiles.** In one instance with 490 true unique profiles, CNRein inferred 565, while SIGNALS and CHISEL inferred a unique profile for every one of the 1000 cells. Across instances CNRein matched the true count with Pearson r = 0.98 and median error 6.92%, against r = −0.28 (SIGNALS) and −0.59 (CHISEL), both with 110% median error.
- **Parsimony (Lazac trees, ZCNT distance).** Median parsimony score 1012 for CNRein (r = 0.95 with truth) vs 248,891 SIGNALS and 52,370 CHISEL; median ground truth was 736, so CNRein is still less parsimonious than the truth. CNRein also beat CHISEL's clustered output, VICTree, and the same methods on CNAsim simulations (supplement).
- **Ovarian cancer OV2295, DLP+ (617 cells of 890, 0.1–0.4×):** Alleloscope predicted no WGD; the other methods called WGD in many cells. CNRein fit read depth significantly better than CHISEL and Alleloscope and no differently from SIGNALS. Largest clone: 41 cells (CNRein), 9 (CHISEL), 2 (Alleloscope); SIGNALS gave every cell a unique profile. Parsimony: 7163 (CNRein) vs 34,529 (SIGNALS) and 13,769 (CHISEL); Alleloscope scored 4149, which the authors attribute to its missed WGD.
- **Orthogonal SNV check.** Somatic SNVs are not used by any method. Of 14,068 OV2295 SNVs, 2,801 likely truncal ones should show VAF peaks at 1/3 and 2/3 in {2,1} regions; they did for CNRein, SIGNALS and CHISEL, not for Alleloscope (single peak near 1/2). A bootstrapped log-likelihood ratio favoured CNRein over Alleloscope (12,635.36) and CHISEL (3,418.66), and SIGNALS slightly over CNRein (−1,033.42, p = 0.0051).
- **Breast cancer S0, 10x Chromium CNV (10,202 cells over five sections, 0.01–0.05×; 785 cells compared with all four methods):** largest identical-profile set 276 cells (CNRein) vs 1, 17 and 5 (SIGNALS, CHISEL, Alleloscope); unique profiles 206 vs 785, 737 and 747. CNNaive, the same pipeline without the evolutionary model, gave 628. Parsimony 397 vs 40,222, 8506 and 2076. On 755 likely truncal SNVs, LLR favoured CNRein over SIGNALS (145.26, p = 0.0062) and CHISEL (1,093.83); Alleloscope was slightly but not significantly better (−35.24, p = 0.205).
- **Cross-technology consistency, breast cancer TN3:** ACT (1101 cells, 0.005–0.015×) and 10x (1070 cells, 0.01–0.07×) data gave 119 and 90 unique profiles. UMAP + DBSCAN found four shared clusters with similar proportions: 41/41/6/12% for ACT and 40/38/8/14% for 10x.

## Methods / evidence

Three stages. (i) Data processing from a barcoded BAM: 100-kb bins, GC and mappability correction, segmentation, SNPs by bcftools, phasing with SHAPEIT4 and the 1000 Genomes panel; outputs are segment read depths, haplotype-specific counts, and cell- and segment-specific variances for read depth and BAF. (ii) **CNNaive** calls each cell alone, estimating ploidy from low-noise regions. (iii) The RL stage. The likelihood is Gaussian in read depth and BAF. A profile's prior is the summed probability of all CNA-tuple sequences (WGD flag, haplotype, start, end, change of −5 to +5) that generate it from the normal profile; per-haplotype CN is capped at 19. The CNN predicts start, then end, then value, then a stop decision. The reward weights each cell's fit by the inverse of its current marginal probability, so the model covers all cells instead of collapsing onto one profile. Training is guided by CNNaive profiles via importance sampling. Implemented in PyTorch, run on a 12-core laptop with 96 GB RAM and no GPU.

Evidence is a simulator from the same authors plus CNAsim, and three real tumours without ground truth. Real-data evaluation uses three proxies: fit to read depth, truncal-SNV VAF consistency (a test for sensitivity), and tree parsimony (a test for specificity). Alleloscope could not be run on the simulations, which lack BAM/FASTQ files. Competitor outputs on S0 and OV2295 were supplied by the SIGNALS team.

## Limitations

**Authors' own:**
- No ground truth on real data and no single perfect metric, so sensitivity and specificity are judged indirectly.
- Optimization depends on CNNaive's initial profiles; accepting other initial calls (e.g. SIGNALS) would be useful.
- Parsimony scores remain meaningfully above the ground truth in simulation; post-processing such as SCICoNE-style MCMC on CNA trees, or adapting GFlowNets, could help.
- Sex chromosomes are excluded.
- Doublets and S-phase cells are not identified; CNRein still produces profiles for them.
- Copy numbers that differ by a constant factor (e.g. (1,2) vs (2,4)) cannot be told apart by the SNV test.
- Models are trained per patient; sharing parameters across a cohort is future work.

**Reviewer notes:**
- The main simulator is the authors' own and generates profiles by sequential CNAs on clones, which is close to CNRein's generative model; the CNAsim results are only in the supplement. (synthesis)
- Parsimony rewards shared structure by construction, so lower scores partly measure the regularizer itself. Extra clonal sharing on S0 is supported mainly by fewer unique profiles, not by independent evidence of clone identity. (synthesis)
- Evaluation covers three tumours from two cancer types; the comparator tools were run by their developers' team or with outside advice, not under one pipeline. (synthesis)

## Surprising or load-bearing bits

- **SIGNALS and CHISEL gave essentially every cell its own profile** (1000 of 1000 in simulation; 785 of 785 for SIGNALS on S0), and their tree parsimony was tens to hundreds of times worse than the truth. Reading clones directly off per-cell calls therefore overstates heterogeneity.
- The ablation is clean: CNNaive (same data model, no evolution) gave 628 unique profiles on S0, CNRein 206. The drop comes from the evolutionary model.
- The reward's inverse-marginal weighting is what stops reinforcement learning from putting all probability on one best profile. This differs from GFlowNets, which make terminal-state probabilities proportional to fixed rewards.
- The disagreement between methods on DLP+ ovarian data (whether WGD occurred) was far larger than on 10x breast data, where the methods mostly agreed.

## Concepts touched

- [[copy-number-variation]] — haplotype-specific CN calling that is regularized by a learned evolutionary model.
- [[phylogenetic-inference]] — CNA trajectories from the normal cell, with parsimony of Lazac trees used as an evaluation metric.
- [[intratumor-heterogeneity]] — argues that per-cell callers inflate heterogeneity; finds more heterogeneity in OV2295 and more shared clonal structure in S0.
- [[whole-genome-doubling]] — WGD is a CNA action in the model; Alleloscope's missed WGD on OV2295 is the largest method disagreement.
- [[dlp-plus]] — OV2295 DLP+ data are one of the benchmarks.
- [[sequencing-depth-and-coverage]] — works at 0.005–0.4× per cell across ACT, 10x and DLP+.

## Connections to other sources

- Benchmarked against [[zaccaria-2021-chisel]] (CHISEL); CNRein had lower simulation error and a better SNV fit on both real datasets. The S0 10x breast data are probably the same public 10x sample used by CHISEL and by [[liu-2024-cot]] (synthesis).
- Same goal as [[kuipers-2025-scicone]]: shared evolutionary history denoises shallow per-cell CN calls. SCICoNE uses MCMC over CNA trees on total CN; CNRein uses RL over CNA trajectories on haplotype-specific CN, and names SCICoNE-style MCMC as a possible post-processing step.
- Real data from [[laks-2019-dlp-plus]] (OV2295). SIGNALS, the main comparator, is the caller used in [[mcpherson-2025-ongoing-wgd]].
- Earlier total-CN callers cited: [[garvin-2015-natmethods]] (Ginkgo), [[wang-2020-scope]] (SCOPE); RNA-based CNA inference ([[gao-2021-copykat]], [[tickle-2019-infercnv]]) gives only qualitative calls.
- Same senior author: [[el-kebir-2018-sphyr]] (SNV phylogeny under loss and error).
- CN phylogeny context: [[kaufmann-2022-medicc2]], [[lu-2024-cnaphylogeny-review]], [[mallory-2020-cna-review]].

## Open questions

- How much of the improvement holds on simulators unrelated to CNRein's generative assumptions. (synthesis)
- Whether cohort-level training can learn general CNA evolution patterns, as the authors propose.
- Joint SNV + CNA inference and doublet/S-phase detection are planned, not done.

## Related

- [[copy-number-variation]] · [[phylogenetic-inference]] · [[zaccaria-2021-chisel]] · [[kuipers-2025-scicone]] · [[40-Topics/cancer-clonal-evolution]]
