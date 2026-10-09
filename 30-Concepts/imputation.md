---
type: concept
title: Imputation
aliases: [data smoothing, missing-value imputation, contact map imputation]
tags: [sparsity, single-cell, smoothing, scHi-C, denoising]
created: 2026-08-10
updated: 2026-10-09
---

# Imputation

> Filling in values that a sparse assay did not observe, so that per-cell structure becomes analysable. Necessary in single-cell Hi-C in particular, because sparsity compounds in two dimensions — 5–10% linear genome coverage becomes **0.25–1% of possible contacts** ([[zhou-2019-schicluster]]).

## Approaches

**Convolution plus random walk.** Replace each matrix element by a weighted average of its neighbourhood (sharing information along the linear genome), then apply random walk with restart (sharing among network neighbours), then keep only the **top 20% of imputed interactions** to strip coverage bias ([[zhou-2019-schicluster]]). All three steps are required; every one- and two-step combination underperforms ([[zhou-2019-schicluster]]). The approach requires dense matrices in memory, limiting resolution ([[zhang-2022-higashi]]).

**Hypergraph representation learning.** Model the whole dataset as one hypergraph — cells and genomic bins as nodes, each non-zero contact as a hyperedge — so imputation becomes hyperedge prediction and can **borrow from a cell's neighbours in embedding space** ([[zhang-2022-higashi]]). Sparse-native, and 30–43% better median similarity than random-walk imputation at the lowest coverage against imaging-derived ground truth ([[zhang-2022-higashi]]).

## What imputation buys

- Cell-type clustering that raw contact matrices cannot support ([[zhou-2019-schicluster]]).
- Per-cell A/B compartment scores and TAD-like domain boundaries, including boundaries that are **present/absent** across cells and boundaries that **slide** along the genome ([[zhang-2022-higashi]]).
- Cell-type-specific structure that is obscured in pooled maps — a boundary near *THBS2* visible per cell and invisible in the population contact map ([[zhang-2022-higashi]]).

## The standing concern

Smoothing that makes cells clusterable necessarily reduces apparent cell-to-cell variability, and the trade is not quantified in either framework ([[zhou-2019-schicluster]], [[zhang-2022-higashi]]). Borrowing across neighbours risks circularity — cells are imputed toward their neighbours, so measured variability is partly a function of the imputation ([[zhang-2022-higashi]]). Validation against orthogonal imaging data is what keeps the claims credible ([[zhang-2022-higashi]]).

Practical floor: clustering performance degrades below **25,000 contacts** per cell and collapses at 5,000 ([[zhou-2019-schicluster]]) — which is below what combinatorial-indexing scHi-C delivers ([[ramani-2017-scihi-c]]).

## Added 2026-10-07

Lähnemann et al. group scRNA-seq imputation into model-based, data-smoothing, data-reconstruction and external-reference (transfer) families, and warn that imputation from internal information alone is circular and can inflate gene–gene correlations ([[10-Summaries/lahnemann-2020-grand-challenges]]). They also recommend against using "dropout" as a catch-all for observed zeros, since it conflates technical and biological zeros ([[10-Summaries/lahnemann-2020-grand-challenges]]).

**Single-cell methylation imputation.** Across 13 scDNAm datasets, accuracy of five CpG imputers was governed more by sparsity and methylome Shannon entropy than by cell number or coverage; random CpG splits inflate scores relative to chromosome hold-out because neighbouring CpGs correlate; and no method finished whole-genome datasets above ~500 cells within 72 h ([[10-Summaries/liang-2026-scmeth-imputation-benchmark]]). Atlas-scale tools instead aggregate over windows and set missing values to zero without imputation ([[10-Summaries/rylaarsdam-2025-amethyst]]).

For scHi-C, Fast-Higashi computes a partial random walk with restart batch-wise inside its tensor-decomposition optimisation (correlation >0.9 with full RWR at batch size 32–64), trading imputation power for memory and speed ([[10-Summaries/zhang-2022-fast-higashi]]).

**Imputation trade-offs across modalities.** For scHi-C compartments, scDIAGRAM reports that imputation-based callers produce more homogeneous calls than the imaging ground truth (scHiCluster also unstable), motivating imputation-free calling ([[10-Summaries/peng-2026-scdiagram]]); for scHi-C loops, windowed RWR imputation remains the enabling step ([[10-Summaries/li-2022-snaphic2]]). For single-cell methylation, MambaCpG's bidirectional state-space model uses windows up to 1,024 CpGs and is top-ranked on large sparse datasets in its own benchmark ([[10-Summaries/zhao-2025-mambacpg]]), although an independent benchmark found no universal winner ([[10-Summaries/liang-2026-scmeth-imputation-benchmark]]).

**Documented imputation artefacts.** Measured against bulk Hi-C, Higashi-imputed aggregate maps look blurry and show recurrent over-enriched off-diagonal blocks across all five Kim2020 cell types, which the authors attribute to over-imputation driven by outlier cells ([[10-Summaries/zheng-2022-bandnorm-scvi-3d]]). Higashi and scHiCluster both inflate the similarity of the rare IMR90 population to other cell types, because borrowing from neighbours homogenizes cells that are poorly separated ([[10-Summaries/zheng-2022-bandnorm-scvi-3d]]). A non-imputing scaling method (BandNorm) recovered more bulk TAD boundaries (85.71% vs 60% median for GM12878) and more top bulk interactions ([[10-Summaries/zheng-2022-bandnorm-scvi-3d]]).

For scHi-C, imputation methods fall into five families: random walk, Gaussian convolution, Bayesian hierarchical, deep learning and LDA topics ([[10-Summaries/dautle-2025-schic-review]]). Each has a stated failure mode. Random walks are biased toward neighbouring observations, and Gaussian smoothing can over-smooth high-frequency regions such as heterochromatin ([[10-Summaries/dautle-2025-schic-review]]). The authors warn that neighbour-based imputation dilutes high-frequency contacts and raises false positives. They propose clustering cells first and then imputing within clusters, iteratively ([[10-Summaries/dautle-2025-schic-review]]).

Model-based imputation of whole missing assays: MOFA imputes masked values from its shared factors (Y = ZWᵀ), and on CLL data it beat feature-wise mean, SoftImpute and kNN imputation and was more robust than GFA, both for scattered missing values and for entirely missing drug-response assays ([[10-Summaries/argelaguet-2018-mofa]]).

## Added 2026-10-08 — sequence models & foundation models

- CpGPT imputed array probes held out of pretraining at MAE 0.081 (unseen input and target) and rebuilt 450k profiles from MSA-overlapping probes at MAE 0.031 zero-shot, against about 0.33–0.37 for sample-mean baselines ([[10-Summaries/delimacamillo-2024-cpgpt]]).
- MethylGPT predicted masked CpG values on held-out samples with Pearson R 0.929 and MAE 0.074, but only within its fixed 49,156-CpG vocabulary ([[10-Summaries/ying-2024-methylgpt]]).

## Added 2026-10-09 — foundation-model gap evidence

- Bulk epigenome imputation can be pretrained self-supervised by masking whole assays and recovering full-depth tracks from downsampled ones; CANDI does this over 35 ENCODE assays and returns calibrated per-bin uncertainty ([[10-Summaries/foroozandeh-2025-candi]])
- On scHPTM data, imputation helps mostly at mid depth (about 1,000 reads per cell) and can lower fidelity on high-quality data; scImpute is best for signal enrichment and scOpen/SCALEX for clustering, and no method does both ([[10-Summaries/morenogonzalez-2025-schistone-imputation]])

## Related

- [[single-cell-hi-c]] · [[scatac-imputation]] · [[dimensionality-reduction]] · [[computational-methods]]

## Added 2026-08-13

Random walk with restart, introduced for scHi-C clustering by [[10-Summaries/zhou-2019-schicluster|scHiCluster]], is reused for a different downstream task in [[10-Summaries/yu-2021-snaphic|SnapHiC]]: per-cell RWR (restart probability 0.05) on a binary 10-kb contact graph, followed by distance-stratified *z*-score normalisation, as the front end of loop calling ([[10-Summaries/yu-2021-snaphic]]).

[[10-Summaries/xiong-2024-scghost|scGHOST]] instead consumes [[10-Summaries/zhang-2022-higashi|Higashi]]-imputed maps and layers graph embedding on top — inheriting whatever Higashi gets wrong ([[10-Summaries/xiong-2024-scghost]]). (synthesis)

A sharper claim about imputation appears outside 3D genomics: ISON's *inferred* spatial chromatin accessibility recovers *cis*-eQTL and Hi-C-supported regulatory links **better than the directly measured** spatial ATAC, because the measurement is so dropout-ridden ([[10-Summaries/debnath-2026-ison]]). The caveat is circularity — the strong correlation numbers use MAGIC-imputed data as ground truth ([[10-Summaries/debnath-2026-ison]]). (synthesis)
