---
type: summary
title: "Ashuach et al. 2022 — PeakVI: A deep generative model for single-cell chromatin accessibility analysis"
source: "[[00-Sources/papers/PeakVI_ A deep generative model for single-cell chromatin accessibility analysis]]"
source_quality: full
source_sha256: "5116770c9e73d4554a1de0914a9d65558c0dacc8dccaf3964f0c607100186ef8"
source_kind: paper
author: "Tal Ashuach, Daniel A. Reidenbach, Adam Gayoso, Nir Yosef (corresponding)"
published: 2022-03
ingested: 2026-10-07
doi: "10.1016/j.crmeth.2022.100182"
journal: "Cell Reports Methods 2(3):100182"
tags: [PeakVI, scATAC-seq, VAE, scvi-tools, differential-accessibility, batch-correction, scArches, Bernoulli-model, reference-mapping]
entities: ["[[nir-yosef]]"]
concepts: ["[[scatac-seq]]", "[[chromatin-accessibility]]", "[[dimensionality-reduction]]", "[[batch-effect]]", "[[reference-atlas-mapping]]", "[[cell-type-annotation]]", "[[peak-calling]]", "[[cistopic]]", "[[chromvar]]", "[[scale]]", "[[latent-dirichlet-allocation]]"]
topics: ["[[single-cell-atac-seq]]", "[[computational-methods]]"]
---

**Citation:** Ashuach et al. (2022) — *PeakVI: A deep generative model for single-cell chromatin accessibility analysis* — *Cell Reports Methods* 2(3):100182. [DOI](https://doi.org/10.1016/j.crmeth.2022.100182)

# Ashuach 2022 — PeakVI

> PeakVI is the scATAC-seq member of scvi-tools: a variational autoencoder that treats each peak-by-cell observation as **Bernoulli**, factorised into three probabilities — the region is truly accessible in this cell state (decoder output), the region gets tagmented (a learned per-region factor capturing width/sequence bias), and the fragment gets captured (a per-cell factor from an auxiliary network, tracking library size). Conditioning on batch yields a batch-corrected latent space, and sampling from the variational posterior yields denoised accessibility estimates that support **single-region differential accessibility** with a Bayesian FDR — which, in the paper's tests, calls zero regions in a replicate-vs-replicate negative control where a Signac-style GLM calls 910 and a Wilcoxon test (ArchR-style) 6,761.

## Key claims

- **Learned nuisance factors track real confounders.** On 10x PBMC multiome data, the region factor sits around 0.5 for most regions, is higher for wider regions, and tops out near ~0.75 — read by the authors as an implicit global penalty reflecting the assay's false negatives. The cell factor tracks empirical library size but saturates, so cells with genuinely less accessible chromatin are not over-penalised.
- **Robust to sparsity.** Randomly zeroing 10–90% of non-zero observations gave mean squared error of 0.06 (10% removed) to 0.17 (90% removed) relative to estimates from the full data; corrupted estimates were biased low, as expected for one-directional (false-negative) corruption.
- **Stable across hyperparameters.** A grid over learning rate, hidden layers, dropout, minibatch size and weight decay (3 runs each) showed defaults perform well without tuning, also at 50% and 10% retained observations.
- **Latent space vs. RNA ground truth (10x PBMC):** fraction of chromatin-kNN that share the RNA-based cluster — PeakVI and cisTopic outperform LSA, SCALE and chromVAR, PeakVI marginally ahead of cisTopic. LSA and SCALE were most sensitive to library size (Geary's C); chromVAR insensitive.
- **Batch correction vs. biology (hematopoiesis data, GEO GSE129785; kNN label-enrichment scores):** LSA, cisTopic and no-batch PeakVI separate sorted cell types well (9.1, 9.13, 9.42) but also separate batches (2.33, 2.28, 2.39); chromVAR and SCALE mix batches best (1.57, 1.59) but separate cell types worse (5.78, 7.03); Iterative LSA underperforms on both. **Replicate-batch PeakVI** gives the best balance (9.04 cell type, 1.85 batch); full-batch PeakVI 8.37 / 1.88.
- **Denoised effect sizes amplify signal and suppress noise.** Estimated vs empirical effects correlate 0.97 in biological comparisons but 0.52 in artifactual (replicate) comparisons; split-replicate reproducibility is 0.95 for PeakVI estimates vs 0.66 for empirical effects. Estimated effects have wider distributions than empirical ones in biological comparisons and similar or narrower in artifactual ones.
- **Well-calibrated DA calls.** Replicate-vs-replicate within NK cells: PeakVI 0 regions, GLM 910, Wilcoxon 6,761. Sorted NK vs B cells: PeakVI 11,362 (16.5%), GLM 33,679 (48.9%), Wilcoxon 26,410 (19.7%). Against bulk ATAC-seq (GSE118189, DESeq2) as reference, effect-size correlation was 0.74 for PeakVI vs 0.48 (GLM) and 0.52 (Wilcoxon); 86% of PeakVI and Wilcoxon calls were also bulk-differential vs 65.6% for GLM; overlap odds ratios 1.92 / 1.93 / 1.47.
- **Annotation two ways.** (i) scArches-style projection of a 10x PBMC query onto a hematopoiesis reference — query cells map only onto PBMC regions of the reference, not progenitors — with labels transferred by cluster majority vote; (ii) de novo annotation via one-sided cluster-marker DA + enrichr/ARCHS4 gene signatures, recovering B, NK, CD4+ T, Treg and pDC labels. A B-cell sub-split (1,043 DA regions; 207 vs 836) resolves naive (TCL1A, YBX3, SATB1…) vs memory (AIM2, CD80…) B cells.

## Methods / evidence

Model: Bernoulli likelihood on binarised peak-by-cell counts; encoder/decoder fully connected blocks (dropout, layer norm) whose size scales with the number of input regions; AdamW (lr 1e-4, weight decay 1e-3, minibatch 128), ≤500 epochs with early stopping on validation reconstruction loss (50-epoch patience), KL warm-up. DA: sample cells with replacement from each group, draw from each cell's posterior, average accessibility probabilities; effect = absolute difference; significance = proportion of paired draws with |difference| > δ (default 0.05), Bayes factor, and the Lopez et al. Bayesian FDR procedure. Hematopoiesis matrix filtered from 571,400 to 133,962 regions (detected in ≥0.1% of cells). Competing methods run with recommended settings: cisTopic v0.3.0 (WarpLDA; 100 and 40 topics), chromVAR v1.12.0 (JASPAR2016, 386 motifs), LSA (tf-idf + TruncatedSVD, 50 components), SCALE v1.0.4.

Weight: a fair, multi-angle benchmark on two real datasets — the authors explicitly rejected simulation because bulk-derived simulators produce unrealistically sparse covariance. Ground truth is indirect (paired RNA clusters, FACS labels, bulk ATAC). Comparisons are against 2019–2021 methods; batch mixing is assessed on only four unsorted PBMC batches.

## Surprising or load-bearing bits

- **Absolute-difference effect size** is chosen deliberately over fold-change: 0.01→0.21 counts the same as 0.7→0.9, damping the instability of ratios at low detection rates.
- **Standard tests are badly overpowered on scATAC**: thousands of "significant" regions between technical replicates for Wilcoxon. Any DA list from per-cell tests without a generative or pseudobulk correction deserves suspicion. (synthesis)
- **Region-width factor** is a learned stand-in for the bias that peak-width normalisation tries to fix by hand.
- The authors' stated limitation is real: PeakVI depends on **upstream peak calls**, so rare populations whose peaks were never called are invisible, and multiple datasets must share a jointly-called peak set before integration.

## Concepts touched

- [[dimensionality-reduction]] / [[batch-effect]] — VAE latent with batch covariates; the "replicate-batch" configuration as a middle ground between no and full correction.
- [[reference-atlas-mapping]] — scArches transfer for scATAC.
- [[cell-type-annotation]] — reference-based + de novo (DA → gene signatures) two-step scheme.
- [[peak-calling]] — dependence on upstream peaks as the principal limitation.
- [[cistopic]], [[chromvar]], [[scale]], [[latent-dirichlet-allocation]] — benchmarked comparators.

## Connections to other sources

- Benchmarked comparators summarised here: [[bravo-2019-cistopic]], [[schep-2017-chromvar]], [[xiong-2019-scale]]; LSA as used in [[stuart-2021-natmethods]] (Signac) and [[granja-2021-archr]] (ArchR; Iterative LSA).
- Same model family: [[gayoso-2021-totalvi]] (RNA + protein) and its multimodal successor [[ashuach-2023-multivi]] (RNA + ATAC), which reuses this ATAC likelihood. (synthesis)
- Contrasts with peak-free featurisation in [[de-boer-2018-brockman]] (k-mers around insertion sites) and [[fang-2021-snapatac]] (bins) — the alternative answer to PeakVI's peak-dependence limitation. (synthesis)
- Later scATAC benchmarking: [[luo-2024-scatac-benchmark]]; dedicated scATAC DA method: [[zhao-2024-scada]].
- Imputation-oriented alternative: [[li-2021-scopen]].
- Later used as the main transfer baseline by [[fan-2026-gfetm]] (GFETM), which reports better zero-shot cross-tissue and human→mouse transfer and better unseen-cell generalisation than PeakVI.

## Open questions

- How does PeakVI's DA calibration compare with pseudobulk approaches, which the paper does not benchmark? (synthesis)
- The binarisation discards count information; whether that matters at higher per-cell coverage is not tested. (synthesis)
- Rare-population sensitivity is bounded by the peak set; no peak-calling-aware extension is offered.

## Related

- [[ashuach-2023-multivi]] · [[gayoso-2021-totalvi]] · [[bravo-2019-cistopic]] · [[40-Topics/single-cell-atac-seq]]
