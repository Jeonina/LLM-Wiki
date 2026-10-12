---
type: concept
title: Imputation
aliases: [data smoothing, missing-value imputation, contact map imputation]
tags: [sparsity, single-cell, smoothing, scHi-C, denoising]
created: 2026-08-10
updated: 2026-10-12
---

# Imputation

> Filling in values that a sparse assay did not observe, so that per-cell structure becomes analysable. Necessary in single-cell Hi-C in particular, because sparsity compounds in two dimensions — 5–10% linear genome coverage becomes **0.25–1% of possible contacts** ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]).

> [!abstract] 한눈에
> Imputation은 희소한 single-cell 데이터에서 관측되지 않은 값을 채워 세포 단위 구조를 분석 가능하게 만드는 작업이고, 2차원으로 희소성이 겹치는 scHi-C에서 특히 필요하다 ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]). 다만 이웃 세포에서 정보를 빌리는 만큼 세포 간 차이를 줄이고 순환 논리에 빠질 위험이 있어, 독립적인 imaging이나 bulk 데이터와의 검증이 핵심이다 ([[10-Summaries/zhang-2022-higashi|Higashi]]; [[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]).

## Definition

Imputation fills in values that a sparse assay did not observe, so that per-cell structure becomes analysable ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]). Lähnemann et al. group scRNA-seq imputation into model-based, data-smoothing, data-reconstruction and external-reference (transfer) families ([[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]). They recommend against using "dropout" as a catch-all for observed zeros, since it conflates technical and biological zeros ([[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]).

## Why it matters

- Imputation makes cell-type clustering possible where raw contact matrices cannot support it ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]).
- It yields per-cell A/B compartment scores and TAD-like domain boundaries, including boundaries that are **present/absent** across cells and boundaries that **slide** along the genome ([[10-Summaries/zhang-2022-higashi|Higashi]]).
- It reveals cell-type-specific structure that is obscured in pooled maps — a boundary near *THBS2* visible per cell and invisible in the population contact map ([[10-Summaries/zhang-2022-higashi|Higashi]]).
- For scHi-C loops, windowed RWR imputation remains the enabling step ([[10-Summaries/li-2022-snaphic2|SnapHiC2]]).

## Approaches

### Single-cell Hi-C

| Approach | Example | What it does | Source |
|---|---|---|---|
| Convolution plus random walk | [[10-Summaries/zhou-2019-schicluster\|scHiCluster]] | Replaces each matrix element by a weighted average of its neighbourhood (sharing information along the linear genome), applies random walk with restart (sharing among network neighbours), then keeps only the **top 20% of imputed interactions** to strip coverage bias; all three steps are required, and every one- and two-step combination underperforms | ([[10-Summaries/zhou-2019-schicluster\|scHiCluster]]) |
| Hypergraph representation learning | [[10-Summaries/zhang-2022-higashi\|Higashi]] | Models the whole dataset as one hypergraph — cells and genomic bins as nodes, each non-zero contact as a hyperedge — so imputation becomes hyperedge prediction and can **borrow from a cell's neighbours in embedding space**; sparse-native | ([[10-Summaries/zhang-2022-higashi\|Higashi]]) |
| Partial RWR inside tensor decomposition | [[10-Summaries/zhang-2022-fast-higashi\|Fast-Higashi]] | Computes a partial random walk with restart batch-wise inside its tensor-decomposition optimisation, trading imputation power for memory and speed | ([[10-Summaries/zhang-2022-fast-higashi\|Fast-Higashi]]) |
| RWR as a loop-calling front end | [[10-Summaries/yu-2021-snaphic\|SnapHiC]], [[10-Summaries/li-2022-snaphic2\|SnapHiC2]] | RWR, introduced for scHi-C clustering by scHiCluster, is reused for loop calling: per-cell RWR (restart probability 0.05) on a binary 10-kb contact graph, followed by distance-stratified *z*-score normalisation; SnapHiC2 uses windowed RWR | ([[10-Summaries/zhou-2019-schicluster\|scHiCluster]]; [[10-Summaries/yu-2021-snaphic\|SnapHiC]]; [[10-Summaries/li-2022-snaphic2\|SnapHiC2]]) |
| Downstream of imputed maps | [[10-Summaries/xiong-2024-scghost\|scGHOST]] | Consumes Higashi-imputed maps and layers graph embedding on top | ([[10-Summaries/xiong-2024-scghost\|scGHOST]]) |

A review groups scHi-C imputation into five families: random walk, Gaussian convolution, Bayesian hierarchical, deep learning and LDA topics ([[10-Summaries/dautle-2025-schic-review|Dautle 2025]]).

### Single-cell DNA methylation

- MambaCpG's bidirectional state-space model uses windows up to 1,024 CpGs and is top-ranked on large sparse datasets in its own benchmark ([[10-Summaries/zhao-2025-mambacpg|MambaCpG]]).
- Atlas-scale tools instead aggregate over windows and set missing values to zero without imputation ([[10-Summaries/rylaarsdam-2025-amethyst|Amethyst]]).
- Bulk-array foundation models impute masked or held-out CpGs: CpGPT on probes held out of pretraining and on 450k profiles rebuilt from overlapping probes ([[10-Summaries/delimacamillo-2024-cpgpt|CpGPT]]), and MethylGPT within its fixed 49,156-CpG vocabulary ([[10-Summaries/ying-2024-methylgpt|MethylGPT]]).

### Other modalities and whole missing assays

- **Model-based imputation of whole missing assays.** MOFA imputes masked values from its shared factors (Y = ZWᵀ) ([[10-Summaries/argelaguet-2018-mofa|MOFA]]).
- **Self-supervised bulk epigenome imputation.** Pretraining can mask whole assays and recover full-depth tracks from downsampled ones; CANDI does this over 35 ENCODE assays and returns calibrated per-bin uncertainty ([[10-Summaries/foroozandeh-2025-candi|CANDI]]).
- **Single-cell histone modifications.** scImpute is best for signal enrichment and scOpen/SCALEX for clustering, and no method does both ([[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025]]).
- **Spatial chromatin accessibility.** ISON infers spatial chromatin accessibility rather than measuring it ([[10-Summaries/debnath-2026-ison|ISON]]); see also [[scatac-imputation]].

## Evidence and examples

**Single-cell Hi-C**

- Higashi gave 30–43% better median similarity than random-walk imputation at the lowest coverage, against imaging-derived ground truth ([[10-Summaries/zhang-2022-higashi|Higashi]]).
- Fast-Higashi's partial RWR correlated >0.9 with full RWR at batch size 32–64 ([[10-Summaries/zhang-2022-fast-higashi|Fast-Higashi]]).
- Practical floor: scHiCluster clustering degrades below **25,000 contacts** per cell and collapses at 5,000 ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]) — which is below what combinatorial-indexing scHi-C delivers ([[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]).
- Measured against bulk Hi-C, Higashi-imputed aggregate maps look blurry and show recurrent over-enriched off-diagonal blocks across all five Kim2020 cell types, which the authors attribute to over-imputation driven by outlier cells ([[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]).
- Higashi and scHiCluster both inflate the similarity of the rare IMR90 population to other cell types, because borrowing from neighbours homogenizes cells that are poorly separated ([[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]).
- A non-imputing scaling method (BandNorm) recovered more bulk TAD boundaries (85.71% vs 60% median for GM12878) and more top bulk interactions ([[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]).
- For scHi-C compartments, imputation-based callers produce more homogeneous calls than the imaging ground truth, with scHiCluster also unstable ([[10-Summaries/peng-2026-scdiagram|scDIAGRAM]]).

**Single-cell DNA methylation**

- Across 13 scDNAm datasets, accuracy of five CpG imputers was governed more by sparsity and methylome Shannon entropy than by cell number or coverage ([[10-Summaries/liang-2026-scmeth-imputation-benchmark|Liang 2026]]).
- Random CpG splits inflate scores relative to chromosome hold-out, because neighbouring CpGs correlate ([[10-Summaries/liang-2026-scmeth-imputation-benchmark|Liang 2026]]).
- No method finished whole-genome datasets above ~500 cells within 72 h ([[10-Summaries/liang-2026-scmeth-imputation-benchmark|Liang 2026]]).
- CpGPT imputed array probes held out of pretraining at MAE 0.081 (unseen input and target) and rebuilt 450k profiles from MSA-overlapping probes at MAE 0.031 zero-shot, against about 0.33–0.37 for sample-mean baselines ([[10-Summaries/delimacamillo-2024-cpgpt|CpGPT]]).
- MethylGPT predicted masked CpG values on held-out samples with Pearson R 0.929 and MAE 0.074 ([[10-Summaries/ying-2024-methylgpt|MethylGPT]]).

**Other modalities**

- On CLL data, MOFA beat feature-wise mean, SoftImpute and kNN imputation and was more robust than GFA, both for scattered missing values and for entirely missing drug-response assays ([[10-Summaries/argelaguet-2018-mofa|MOFA]]).
- On scHPTM data, imputation helps mostly at mid depth (about 1,000 reads per cell) and can lower fidelity on high-quality data ([[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025]]).
- ISON's *inferred* spatial chromatin accessibility recovers *cis*-eQTL and Hi-C-supported regulatory links **better than the directly measured** spatial ATAC, because the measurement is so dropout-ridden ([[10-Summaries/debnath-2026-ison|ISON]]).

## Contested points

- **Smoothing trades variability for clusterability.** Smoothing that makes cells clusterable necessarily reduces apparent cell-to-cell variability, and the trade is not quantified in either scHiCluster or Higashi ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]; [[10-Summaries/zhang-2022-higashi|Higashi]]).
- **Circularity.** Borrowing across neighbours risks circularity — cells are imputed toward their neighbours, so measured variability is partly a function of the imputation ([[10-Summaries/zhang-2022-higashi|Higashi]]). In scRNA-seq, imputation from internal information alone is circular and can inflate gene–gene correlations ([[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]). Validation against orthogonal imaging data is what keeps the Higashi claims credible ([[10-Summaries/zhang-2022-higashi|Higashi]]).
- **Neighbour-based imputation dilutes high-frequency contacts.** Random walks are biased toward neighbouring observations, and Gaussian smoothing can over-smooth high-frequency regions such as heterochromatin ([[10-Summaries/dautle-2025-schic-review|Dautle 2025]]). The review's authors warn that neighbour-based imputation raises false positives and propose clustering cells first and then imputing within clusters, iteratively ([[10-Summaries/dautle-2025-schic-review|Dautle 2025]]).
- **Imputation-free alternatives.** scDIAGRAM's finding that imputation-based compartment callers are over-homogeneous motivates imputation-free calling ([[10-Summaries/peng-2026-scdiagram|scDIAGRAM]]), and BandNorm's non-imputing scaling outperformed Higashi and scHiCluster on bulk TAD recovery ([[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]).
- **Memory limits.** scHiCluster's approach requires dense matrices in memory, limiting resolution ([[10-Summaries/zhang-2022-higashi|Higashi]]).
- **No universal winner for methylation.** MambaCpG is top-ranked in its own benchmark ([[10-Summaries/zhao-2025-mambacpg|MambaCpG]]), although an independent benchmark found no universal winner ([[10-Summaries/liang-2026-scmeth-imputation-benchmark|Liang 2026]]).
- **Fixed vocabularies.** MethylGPT imputes only within its fixed 49,156-CpG vocabulary ([[10-Summaries/ying-2024-methylgpt|MethylGPT]]).
- **Errors propagate downstream.** scGHOST inherits whatever Higashi gets wrong, because it consumes Higashi-imputed maps ([[10-Summaries/xiong-2024-scghost|scGHOST]]; [[10-Summaries/zhang-2022-higashi|Higashi]]) (synthesis).
- **Imputed data as ground truth.** ISON's strong correlation numbers use MAGIC-imputed data as ground truth, so the claim that inference beats measurement is partly circular ([[10-Summaries/debnath-2026-ison|ISON]]) (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — Methods that profile chromatin contacts per cell, the assay where imputation is most needed.
> - `concept` [[30-Concepts/scatac-imputation|scATAC-seq imputation and denoising]] — Recovering missing open-chromatin signal in extremely sparse scATAC-seq matrices.
> - `concept` [[30-Concepts/dimensionality-reduction|Dimensionality reduction]] — Projecting single-cell measurements into a few coordinates for clustering and visualization.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — The aligners, callers, imputers and integrators that turn raw sequencing into results.

## All sources on this page

> [!info]- 20 summaries cited here
> - [[10-Summaries/argelaguet-2018-mofa|Argelaguet 2018]]
> - [[10-Summaries/dautle-2025-schic-review|Dautle 2025]]
> - [[10-Summaries/debnath-2026-ison|Debnath 2026]]
> - [[10-Summaries/delimacamillo-2024-cpgpt|CpGPT 2024]]
> - [[10-Summaries/foroozandeh-2025-candi|Foroozandeh 2025 CANDI]]
> - [[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]
> - [[10-Summaries/li-2022-snaphic2|Li 2022]]
> - [[10-Summaries/liang-2026-scmeth-imputation-benchmark|Liang 2026]]
> - [[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025 SCIBED]]
> - [[10-Summaries/peng-2026-scdiagram|Peng 2026]]
> - [[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]
> - [[10-Summaries/rylaarsdam-2025-amethyst|Rylaarsdam 2025]]
> - [[10-Summaries/xiong-2024-scghost|Xiong 2024]]
> - [[10-Summaries/ying-2024-methylgpt|MethylGPT 2024]]
> - [[10-Summaries/yu-2021-snaphic|Yu 2021]]
> - [[10-Summaries/zhang-2022-fast-higashi|Zhang 2022]]
> - [[10-Summaries/zhang-2022-higashi|Zhang 2022]]
> - [[10-Summaries/zhao-2025-mambacpg|Zhao 2025]]
> - [[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]
> - [[10-Summaries/zhou-2019-schicluster|Zhou 2019]]
