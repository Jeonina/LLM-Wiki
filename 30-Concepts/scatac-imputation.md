---
type: concept
title: scATAC-seq imputation and denoising
aliases: [scATAC imputation, chromatin accessibility imputation, dropout recovery scATAC]
tags: [scATAC-seq, imputation, denoising, dropout, benchmarking]
created: 2026-06-02
updated: 2026-10-12
---

# scATAC-seq imputation and denoising

> Computational recovery of missing open-chromatin signal in scATAC-seq, whose count matrices are extremely sparse (~3–7% non-zero) because each diploid peak has at most two capturable Tn5 cut sites, most lost during library preparation ([[10-Summaries/li-2021-scopen|scOpen]]).

> [!abstract] 한눈에
> scATAC-seq 행렬은 0이 아닌 값이 3–7%뿐이라, imputation은 각 세포에서 각 영역이 실제로 열려 있는지를 추정해 dropout을 메우는 작업이다 ([[10-Summaries/li-2021-scopen|scOpen]]). 행렬 분해와 VAE에서 시작해 DNA 서열을 쓰는 foundation model로 넘어가고 있지만, 복원된 신호가 진짜인지 지어낸 것인지 가릴 기준은 아직 없다 ([[10-Summaries/tang-2024-sccase|scCASE]]; [[10-Summaries/fan-2026-gfetm|GFETM]]; [[10-Summaries/li-2021-scopen|scOpen]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [scATAC-seq 희소성 시뮬레이터](../60-Explainers/single-cell-atac-seq.html)
<!-- /explainer-links -->

## Definition

Imputation/denoising methods estimate the true accessibility status of each region in each cell from the observed sparse matrix, mitigating dropout before downstream clustering, visualization, motif analysis, and *cis*-regulatory prediction ([[10-Summaries/li-2021-scopen|scOpen]]). Assuming only ~25% of accessible DNA is sequenced, ~56% of accessible sites get zero cut sites under a binomial model — the dropout problem these methods address ([[10-Summaries/li-2021-scopen|scOpen]]).

## Why it matters

- Sparsity is worse than scRNA-seq and confounds distance metrics, making clustering and co-accessibility unreliable on raw matrices ([[10-Summaries/xiong-2019-scale|SCALE]]).
- Imputation strongly improves correlation-based *cis*-regulatory prediction (Cicero) because dropouts at two regions are independent — the same logic as MAGIC for scRNA-seq gene–gene interactions ([[10-Summaries/li-2021-scopen|scOpen]]).
- Enhancement can reduce the sequencing-depth confound in the leading principal component ([[10-Summaries/tang-2024-sccase|scCASE]]).
- Despite this, imputation was historically "widely ignored" in standard pipelines like Signac and ArchR ([[10-Summaries/li-2021-scopen|scOpen]]).

## Methods

| Method | Approach | Notes | Source |
|---|---|---|---|
| [[30-Concepts/scopen\|scOpen]] | Regularized NMF on a TF-IDF binary matrix (low-rank reconstruction) | Lowest memory, highest AUPR in its benchmark | ([[10-Summaries/li-2021-scopen\|scOpen]]) |
| [[30-Concepts/scale\|SCALE]] | VAE + Gaussian Mixture Model | Deep learning; interpretable latent features; GPU-bound | ([[10-Summaries/xiong-2019-scale\|SCALE]]) |
| cisTopic-impute ([[30-Concepts/cistopic\|cisTopic]]) | Multiplies topic-cell × region-topic LDA distributions into a predictive matrix | Runtime scales poorly with reads | ([[10-Summaries/bravo-2019-cistopic\|cisTopic]]) |
| scCASE | NMF whose reconstruction target is the data smoothed through an iteratively updated cell-to-cell similarity matrix Z, which starts from Jaccard similarity; enhanced output is XZ | Works differently from scOpen's low-rank reconstruction | ([[10-Summaries/tang-2024-sccase\|scCASE]]) |
| scCASER | scCASE plus a bulk, paired pseudo-bulk or self-pseudo-bulk reference | Reference-guided variant | ([[10-Summaries/tang-2024-sccase\|scCASE]]) |
| PeakVI | Deep generative model | Denoised accessibility estimates | ([[10-Summaries/ashuach-2022-peakvi\|PeakVI]]) |
| EpiAgent | Decodes all cCREs from a transformer cell embedding (foundation model) | — | ([[10-Summaries/chen-2025-epiagent\|EpiAgent]]) |
| EpiZoo | DNA sequence-aware foundation model, fine-tuned for masked-signal recovery | — | ([[10-Summaries/li-2026-epizoo\|EpiZoo]]) |
| GFETM | Embedded topic model trained jointly with a genome foundation model over peak sequences | Imputes accessibility at unseen peaks; CellSpace, SIMBA and PeakVI cannot do this task | ([[10-Summaries/fan-2026-gfetm\|GFETM]]) |
| SUCCEED prior | Pre-trained DNA sequence model used as a prior for ATAC denoising | — | ([[10-Summaries/sun-2026-succeed\|SUCCEED]]) |
| Repurposed scRNA-seq imputers | MAGIC, SAVER, scImpute, DCA, scBFA | Generally underfit scATAC sparsity and can introduce false signals | ([[10-Summaries/xiong-2019-scale\|SCALE]]; [[10-Summaries/li-2021-scopen\|scOpen]]) |

## Evidence and examples

**Matrix-factorization and generative methods**

- Across eight real datasets scCASE averaged +13.89% ARI and +24.41% silhouette over the second-best method, out of SCALE, scBFA, scOpen and scBasset ([[10-Summaries/tang-2024-sccase|scCASE]]).
- scCASER's reference raised average ARI by a further 9.05% ([[10-Summaries/tang-2024-sccase|scCASE]]).
- scCASE enhancement lowered the PC1–depth correlation by 45.6% in a bone-marrow dataset and by 19.6% in a mouse lung dataset ([[10-Summaries/tang-2024-sccase|scCASE]]).
- PeakVI's denoised accessibility estimates stayed consistent when 10–90% of non-zero observations were removed (MSE 0.06 to 0.17) ([[10-Summaries/ashuach-2022-peakvi|PeakVI]]).

**Foundation and sequence models**

- EpiAgent imputes by decoding all cCREs from a transformer cell embedding, improving NMI by 11.123% and ARI by 18.605% on average over raw data, whereas scCASE and scOpen were unstable ([[10-Summaries/chen-2025-epiagent|EpiAgent]]).
- Fine-tuned EpiZoo recovered 50%-masked scATAC signal with the highest clustering NMI and a median cell-type-level PCC of 0.874, ahead of EpiAgent, scOpen and scCASE ([[10-Summaries/li-2026-epizoo|EpiZoo]]).
- In leave-one-chromosome-out tests on Buenrostro 2018, GFETM's top-K precision at unseen peaks beat scBasset by about 10% (K = 5), 6% (K = 10) and 3% (K = 20) ([[10-Summaries/fan-2026-gfetm|GFETM]]).
- GFETM's denoised matrix raised marker-gene enrichment of differential peaks over raw counts, with gains mostly >10 kb from the TSS, while scBasset was better within 1 kb ([[10-Summaries/fan-2026-gfetm|GFETM]]).
- With a SUCCEED sequence prior, ATAC denoising beat AtacWorks at all depths down to 0.2 M reads (peak-calling AUPRC 0.38 vs 0.17 without the prior on held-out erythroid cells) and reconstructed scATAC profiles from single-cell input comparable to ~300 cells ([[10-Summaries/sun-2026-succeed|SUCCEED]]).

**Beyond accessibility**

- scATAC-derived imputers beat scRNA-derived ones on narrow-peak histone marks (H3K4me3, H3K4me1; Wilcoxon P < 0.05) but not on broad H3K9me3, which the authors attribute to broad domains giving dense, correlated bin matrices ([[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025]]).

## Contested points

- **Help or hallucination.** Imputation can induce false signals, and the field lacks a definitive rule for when recovery is trustworthy vs hallucinated ([[10-Summaries/li-2021-scopen|scOpen]]).
- **Over-smoothing can be quantified rather than just flagged.** scCASE defines over-, under- and smoothing scores and reports over-smoothing when the NMF rank K < 7 and added noise when K > 20, while results stay stable for λ between 10⁵ and 10⁸ ([[10-Summaries/tang-2024-sccase|scCASE]]).
- **scOpen vs SCALE.** scOpen reports beating SCALE; SCALE's strengths are interpretability and batch-effect detection rather than raw AUPR ([[10-Summaries/li-2021-scopen|scOpen]]; [[10-Summaries/xiong-2019-scale|SCALE]]).
- **Rankings depend on who runs the benchmark.** scCASE reports beating scOpen ([[10-Summaries/tang-2024-sccase|scCASE]]), while EpiAgent found both scCASE and scOpen unstable ([[10-Summaries/chen-2025-epiagent|EpiAgent]]) and EpiZoo ranked itself ahead of EpiAgent, scOpen and scCASE ([[10-Summaries/li-2026-epizoo|EpiZoo]]); each new method wins its own benchmark, so no cross-paper ranking is settled (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/scopen|scOpen]] — Regularized NMF imputation of TF-IDF-transformed binary scATAC matrices.
> - `concept` [[30-Concepts/scale|SCALE]] — VAE with a Gaussian-mixture prior for sparse scATAC-seq.
> - `concept` [[30-Concepts/cistopic|cisTopic]] — LDA topic modelling of cells and regions in scATAC-seq.
> - `concept` [[30-Concepts/snapatac|SnapATAC]] — Peak-free scATAC-seq pipeline built on 5-kb bins and Jaccard similarity.
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Genome-wide chromatin accessibility in individual cells.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — Whether a region of DNA is open or closed to regulatory machinery.
> - `concept` [[30-Concepts/allele-dropout|Allele dropout]] — Loss of one allele during single-cell amplification, a related dropout failure mode.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Chromatin accessibility in single cells and the sparsity that imputation addresses.

## All sources on this page

> [!info]- 10 summaries cited here
> - [[10-Summaries/ashuach-2022-peakvi|Ashuach 2022]]
> - [[10-Summaries/bravo-2019-cistopic|Bravo González-Blas 2019]]
> - [[10-Summaries/chen-2025-epiagent|Chen 2025]]
> - [[10-Summaries/fan-2026-gfetm|Fan 2026]]
> - [[10-Summaries/li-2021-scopen|Li 2021]]
> - [[10-Summaries/li-2026-epizoo|EpiZoo 2026]]
> - [[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025 SCIBED]]
> - [[10-Summaries/sun-2026-succeed|SUCCEED 2026]]
> - [[10-Summaries/tang-2024-sccase|Tang 2024]]
> - [[10-Summaries/xiong-2019-scale|Xiong 2019]]
