---
type: summary
title: "Tang et al. 2024 — scCASE: accurate and interpretable enhancement for single-cell chromatin accessibility sequencing data"
source: "[[00-Sources/papers/scCASE_ accurate and interpretable enhancement for single-cell chromatin accessibility sequencing data]]"
source_quality: full
source_sha256: "09c92c4bd8e0a993d85ead1d49b07b55b6524e359c9cedc9e621a6fa271b2af7"
source_kind: paper
author: "Songming Tang, Xuejian Cui, Rongxiang Wang, Sijie Li, Siyu Li, Xin Huang, Shengquan Chen (corresponding)"
published: 2024-02-22
ingested: 2026-10-07
doi: "10.1038/s41467-024-46045-w"
journal: "Nature Communications 15:1629"
tags: [scCASE, scCASER, scATAC-seq, imputation, denoising, NMF, cell-similarity, reference-guided, TF-IDF, interpretability, computational-tool]
entities: []
concepts: ["[[scatac-imputation]]", "[[scopen]]", "[[scale]]", "[[scatac-seq]]", "[[chromatin-accessibility]]", "[[imputation]]", "[[jaccard-similarity]]", "[[pseudo-bulk]]", "[[batch-effect]]", "[[chromvar]]", "[[scabc]]", "[[episcanpy]]", "[[transcription-factor-motif]]", "[[clustering-algorithms]]"]
topics: ["[[single-cell-atac-seq]]", "[[computational-methods]]"]
---

**Citation:** Tang et al. (2024) — *scCASE: accurate and interpretable enhancement for single-cell chromatin accessibility sequencing data* — *Nature Communications* 15, 1629. [DOI](https://doi.org/10.1038/s41467-024-46045-w)

# Tang 2024 — scCASE

> scCAS imputation methods before this one (SCALE, scBFA, scOpen, scBasset) enhance the matrix **peak-wise**, ignoring the most obvious source of information about a dropout — the same peak in similar cells. scCASE makes cell-to-cell similarity a learned object: an NMF whose reconstruction target is the data **smoothed through an iteratively updated similarity matrix Z**, with Z itself tied to the cell embeddings. The final output is simply **XZ** — raw data re-weighted by learned neighbours. A variant, **scCASER**, pins part of the NMF basis to a factorization of external (bulk or pseudo-bulk) reference data.

## Key claims

- **Model.** Peaks accessible in <1% of cells are filtered, then TF-IDF transformed. The loss is ‖X(Z∘R) − WH‖²_F + λ‖Z − HᵀH‖²_F + γ₁‖W‖²_F + γ₂‖H‖²_F, where Z (n×n, columns sum to 1) is cell similarity, R is a binomially sampled 0/1 matrix, W the peak projection and H the cell embedding. The Hadamard mask R exists to stop similar cells from receiving **entirely identical** read counts, i.e. a built-in guard against collapsing heterogeneity.
- **Interpretability comes from the NMF factors**: a column of W matched to the embedding component most active in a cell type gives that type's "specific peaks". For monocytes in the Blood dataset, the top 100 such peaks give GREAT top-five terms that are all bacterial-response / immune-regulation pathways, and individual peaks fall in *SLC11A1* and near *TREM1*.
- **Clustering gains**: across the eight real datasets, scCASE averaged **+13.89% ARI and +24.41% silhouette** versus the second-best method per dataset, and beat raw data and every baseline at *p* < 0.05 (one-sided paired Wilcoxon). It stayed best on Muto and PBMC, two datasets labelled from paired scRNA-seq rather than from scCAS itself.
- **Depth confound partly removed**: the correlation between PC1 (TF-IDF + SVD) and sequencing depth exceeds 0.8 in Blood and 0.7 in LungA on raw data; scCASE reduces it by **45.6%** and **19.6%** respectively. An optional extended model (Supplementary Text S3) removes the strong PC–depth correlation more completely.
- **Robustness**: on LungA, clustering ARI stayed stable as extra dropout was injected from 0% to 80%, as cell-type imbalance was varied, and as cells were subsampled from 3,671 to 367. scBFA and scBasset were excluded from these tests because they could not finish LungA within 48 h under a 256 GB memory cap.
- **Batches**: scCASE beats baselines on two concatenated datasets (Mixed-protocols: 10X + snATAC mouse brain; Mixed-tissues: LungA + Spleen); an optional extension corrects batch effects (better kBET and batch ASW), merging L2/3 IT cells from two batches into one Louvain cluster.
- **scCASER**: adding a reference raised average ARI by 9.05%, AMI 4.04%, FMI 5.70% and silhouette 3.19% over scCASE. References can be bulk ATAC (17 haematopoietic cell types for Blood/BM0828), pseudo-bulk from a paired dataset of the same tissue (WholeBrainA/B, LungA/B), or **pseudo-bulk self-reference** built from clustering the target itself (Spleen, LargeIntestine). Degrading the Spleen self-reference from 11 to 8, 6 or 4 clusters lowered performance but still beat scCASE without reference.

## Methods / evidence

Thirteen datasets: one simCAS simulation (5 clusters × 500 cells, 15,000 peaks), eight public scCAS datasets (human bone-marrow Blood and its BM0828 subset; six adult-mouse tissue datasets from the Cusanovich mouse atlas), two multiome datasets annotated from RNA (Muto kidney, 10x PBMC), and two mixed datasets. Baselines, all run at defaults: **SCALE, scBFA, scOpen, scBasset**. Metrics: cell-wise and peak-wise auPRC/auROC on the simulation; ARI/AMI/FMI after PCA-50 + Louvain with binary search to the true cluster number; silhouette on 1 − Pearson distances (following scOpen's protocol). Downstream biology: GREAT, SNPsea (79 human tissues), partitioned LDSC on blood phenotypes, scABC + chromVAR motif analysis (35 of the top 50 variable motifs in Blood linked to blood cells in the literature). Z is initialised from the cell–cell **Jaccard similarity**; W, H from conventional NMF; the latent dimension K from ASTER's estimate of cell-type number; λ default 10⁶.

Weight: a standard methods-paper benchmark by the developers — the clustering metrics measure agreement with labels that were themselves mostly derived from scCAS clustering, which the authors acknowledge and partly address with the two RNA-labelled datasets. The ground-truth accuracy test is simulation-only. (synthesis)

## Surprising or load-bearing bits

- **The output is XZ, not WH.** The NMF reconstruction is a scaffold for learning Z; the enhanced matrix is the observed data aggregated over learned neighbours. That makes scCASE closer to a learned kNN-smoothing (MAGIC-like) than to scOpen's low-rank reconstruction, despite both being "NMF methods". (synthesis)
- **Over-smoothing is measured, not assumed away.** The authors define over-, under- and smoothing scores and show over-smoothing appears when K < 7, while K > 20 adds noise; λ across 10⁵–10⁸ barely changes results; random initialisation of H badly degrades Z, but random Z initialisation does not cause over-smoothing.
- **Self-reference is a reference without external data**: clustering the target, pseudo-bulking, and feeding that back as prior still improves metrics. That is arguably a second round of smoothing by cluster label, so gains on cluster-agreement metrics are partly circular. (synthesis)
- **Scaling**: going from 20k to 100k cells, peak memory rose 7.67× for scCASE versus 8.62× for scOpen; scBFA ran out of memory at 100k cells. The authors themselves describe compute efficiency as only "comparable".
- The paper's stated limitations: linear model (no nonlinear patterns), modest speed (GPU suggested), and possible extension to spatial and multi-omics data.

## Concepts touched

- [[scatac-imputation]] — adds a cell-similarity-learning NMF method and a reference-guided variant to the family.
- [[scopen]] — the closest relative (regularized NMF); scCASE reuses scOpen's evaluation protocol and beats it in this benchmark.
- [[scale]] — VAE baseline; GPU-based, so lower CPU memory.
- [[jaccard-similarity]] — initialisation of the similarity matrix Z.
- [[pseudo-bulk]] — used to construct paired and self-references for scCASER.
- [[batch-effect]] — optional extension corrects protocol batches.
- [[chromvar]] / [[scabc]] / [[episcanpy]] — downstream motif, cluster-specific-peak and preprocessing tools.

## Connections to other sources

- Benchmarks directly against [[li-2021-scopen]], [[xiong-2019-scale]] and [[yuan-2022-scbasset]]; follows scOpen's silhouette/clustering protocol.
- Uses [[danese-2021-episcanpy]] for preprocessing and differential peaks, [[zamanighomi-2018-scabc]] + [[schep-2017-chromvar]] for motif analysis.
- Topic-model alternative for imputation: [[bravo-2019-cistopic]].
- scATAC foundations behind the data: [[buenrostro-2015-nature]], [[cusanovich-2015-sciatac]].

## Open questions

- Whether enhancement improves *biology* (e.g., co-accessibility, rare-state detection) rather than agreement with existing labels is not directly tested beyond enrichment analyses. (synthesis)
- The random mask R prevents identical profiles but its sampling rate's effect on heterogeneity is not reported in the main text.
- scCASER's gain depends on reference completeness; how a reference containing cell types *absent* from the target would bias enhancement is not examined. (synthesis)

## Related

- [[scatac-imputation]] · [[scopen]] · [[li-2021-scopen]] · [[40-Topics/single-cell-atac-seq]]
