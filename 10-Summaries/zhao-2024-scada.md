---
type: summary
title: "Zhao et al. 2024 — scaDA: A novel statistical method for differential analysis of single-cell chromatin accessibility sequencing data"
source: "[[00-Sources/papers/scaDA_ A novel statistical method for differential analysis of single-cell chromatin accessibility sequencing data]]"
source_kind: paper
author: "Fengdi Zhao, Xin Ma, Bing Yao, Qing Lu, Li Chen"
published: 2024-08-02
ingested: 2026-10-07
doi: "10.1371/journal.pcbi.1011854"
journal: "PLOS Computational Biology 20(8):e1011854"
tags: [scaDA, scATAC-seq, differential-accessibility, ZINB, empirical-Bayes, dispersion-shrinkage, composite-test, sc-multiome, Alzheimers, microglia, GWAS-enrichment]
entities: []
concepts: ["[[scatac-seq]]", "[[chromatin-accessibility]]", "[[cis-regulatory-element]]", "[[alzheimers-disease]]", "[[pseudo-bulk]]"]
topics: ["[[single-cell-atac-seq]]", "[[computational-methods]]"]
---

**Citation:** Zhao et al. (2024) — *scaDA: A novel statistical method for differential analysis of single-cell chromatin accessibility sequencing data* — *PLOS Computational Biology* 20(8):e1011854. [DOI](https://doi.org/10.1371/journal.pcbi.1011854)

# Zhao 2024 — scaDA

> scaDA reframes scATAC-seq differential accessibility (DA) as a **differential-distribution** problem. Each peak's counts are modelled as **zero-inflated negative binomial (ZINB)** with mean μ, prevalence of excess zeros p and dispersion φ; a 3-d.f. likelihood-ratio test asks whether *any* of the three differs between two groups. What separates scaDA from a plain ZINB(μ, φ, p) LRT is estimation: an **empirical-Bayes log-normal prior shrinks φ** across peaks (posterior mode by Newton–Raphson), followed by iterative re-estimation of μ and p. The authors present it as, to their knowledge, the first method to test distribution (not just mean) differences in scATAC DA; it wins on power and FDR control in ZINB simulations and on a proxy "true discovery rate" in three multiome-type datasets, including Alzheimer's disease microglia.

## Key claims

- **Distributions differ in more than the mean.** In 10x "Human Brain 3K" (cerebellum multiome; 3,233 cells, 88,843 peaks; 8 cell types with >100 cells retained of 14 annotated), cell types differ in μ, p and φ in varied patterns — e.g., lower dispersion in cOPC than granule neurons with similar μ and p — motivating a composite test.
- **Log-normal dispersion prior is empirically grounded**: log φ estimates in granule neurons are approximately Gaussian (mean 0.03, SD 0.57).
- **Simulations (ZINB, parameters from granule neurons; 4,000 peaks, 100 cells/group, 20% DA, log2FC 0.5–3.0).** vs ZINB-based LRTs: scaDA ranks second only to the matched single-parameter test when differences are mean-only or prevalence-only, and is best when dispersion-only or all three differ; it beats the identical-hypothesis ZINB(μ, φ, p) throughout. vs published methods (NegBin, edgeR, MAST, scATAC-pro [Wilcoxon], Signac [logistic regression]): most powerful in all scenarios except prevalence-only, where it is second to scATAC-pro; MAST is often runner-up. Advantages shrink as cells per group rise to 200/300.
- **FDR control** (scenario 4, log2FC 2.5): scaDA's observed FDR is closest to nominal; scATAC-pro, edgeR and MAST are overly conservative; NegBin is badly inflated (and edgeR also inflated at 200/300 cells).
- **Better estimation explains the gain**: correlation of true vs estimated φ 0.443 (scaDA) vs 0.303 (ZINB(μ, φ, p)), with lower MSE for all three parameters.
- **Real data, top-20% TDR (mean across cell types):** Human Brain 3K 0.81 vs 0.64–0.72 for others (power at 100%: 0.51 vs 0.22–0.34); Human PBMC 10K (12,012 cells, 14 cell types) 0.57 vs 0.40–0.49 (power 0.24 vs 0.09–0.16); Human AD (191,890 nuclei from 20 prefrontal-cortex samples, 12 AD / 8 control, 3 batches; RNA and ATAC profiled separately) 0.77 vs 0.16–0.65 (power 0.69 vs 0.09–0.35). scaDA also had the lowest across-cell-type TDR variability in most comparisons.
- **AD microglia biology**: across 34 AD-vs-control pairwise comparisons, scaDA peaks show the highest enrichment for 10 AD-relevant GO terms (cognition, amyloid-β metabolism, synaptic signalling, adaptive immunity), with NegBin failing to hit any; meta-analysed GWAX AD SNP enrichment (1,302 SNPs at p < 1×10⁻⁴ vs 10× negative controls) gives scaDA logOR 1.97 (p = 0.026), edgeR 1.88 (p = 0.037), MAST and scATAC-pro non-significant, NegBin and Signac no hits.

## Methods / evidence

Per-peak ZINB fit by EM (`pscl::zeroinfl`); log-normal hyperparameters from the median and corrected variance of log φ across peaks; posterior-mode φ by Newton–Raphson; bounded iterative refinement of μ and p (≤100 iterations, tol 1e-6); LRT pooled vs per-group parameters, χ² with 3 d.f.; Benjamini–Hochberg FDR. Real-data "truth": peaks within ±25 kb (50-kb window) of DE genes (Wilcoxon on RNA, or on Signac `GeneActivity()` ATAC-derived pseudo-expression for the AD data) are "true differential"; peaks near non-DE genes are "non-differential". Implemented as an R package.

Weight: simulations draw from the ZINB model scaDA assumes, which favours ZINB-based methods. The real-data benchmark is a proxy: proximity to DE genes is a weak label, and in the AD dataset the "expression" used to define truth is itself derived from ATAC counts near TSSs — partially circular with any accessibility-based DA method. (synthesis) No comparison against pseudobulk DA or generative models such as PeakVI. Analysis is two-group only.

## Surprising or load-bearing bits

- **scATAC sparsity**: the authors cite ~3% non-zero entries in peak-by-cell matrices vs >10% for scRNA-seq gene matrices — a quantitative reason RNA DE tools transfer poorly.
- **μ and p are nearly collinear in sparse ATAC**: under low counts prevalence ≈ mean, and under binarisation they are equivalent — so "differential prevalence" and "differential mean" are hard to separate in practice. (Stated in the source; implication for interpretation is synthesis.)
- **Dispersion as a DA signal**: a peak can be differentially *variable* across cells without a mean change; only methods testing φ can see it — a chromatin analogue of differential-variability tests in methylation. (synthesis)

## Concepts touched

- [[scatac-seq]] / [[chromatin-accessibility]] — count model and DA testing for sparse peak matrices.
- [[alzheimers-disease]] — microglia DA peaks enriched for AD GO terms and AD GWAX SNPs.
- [[cis-regulatory-element]] — DA peaks as candidate cell-type or disease-specific CREs.
- [[pseudo-bulk]] — the main alternative DA strategy, not benchmarked here. (synthesis)

## Connections to other sources

- Competing DA approaches: Signac logistic regression [[stuart-2021-natmethods]]; ArchR Wilcoxon [[granja-2021-archr]]; generative single-region DA with Bayesian FDR [[ashuach-2022-peakvi]] (which reports similar over-calling by Wilcoxon/GLM). (synthesis)
- Multiome context: [[hao-2021-seurat-wnn]] (WNN pipeline used for preprocessing).
- Benchmark context: [[luo-2024-scatac-benchmark]]; differential-variability analogue in methylation: [[kapourani-2021-scmet]].
- Co-accessibility extension proposed: [[pliner-2018-cicero]].

## Open questions

- Would a binarised Bernoulli model (as in PeakVI) lose the dispersion signal scaDA exploits, or is φ mostly noise at typical depths? (synthesis)
- Covariates and multi-factor designs (batch, donor) are not supported; the AD analysis sidesteps batch by within-batch pairwise comparisons.
- Peaks are tested independently; a multivariate co-accessibility test is proposed but not built.

## Related

- [[ashuach-2022-peakvi]] · [[stuart-2021-natmethods]] · [[scatac-seq]] · [[40-Topics/single-cell-atac-seq]]
