---
type: summary
title: "Li et al. 2021 — scOpen: regularized NMF imputation for scATAC-seq"
source: "[[00-Sources/papers/Chromatin-accessibility estimation from single-cell ATAC-seq data with scOpen]]"
source_kind: paper
author: "Zhijian Li, Christoph Kuppe, Susanne Ziegler, Mingbo Cheng, Nazanin Kabgani, Sylvia Menzel, Martin Zenke, Rafael Kramann, Ivan G. Costa (corresponding)"
published: 2021-11-04
ingested: 2026-06-02
doi: "10.1038/s41467-021-26530-2"
journal: "Nature Communications"
tags: [scATAC-seq, imputation, NMF, denoising, kidney-fibrosis, footprinting, Costa-lab]
entities:
  - "[[20-Entities/ivan-costa]]"
concepts:
  - "[[30-Concepts/scopen]]"
  - "[[30-Concepts/scatac-imputation]]"
  - "[[30-Concepts/scatac-seq]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/allele-dropout]]"
  - "[[30-Concepts/transcription-factor-motif]]"
concepts_secondary:
  - "[[30-Concepts/chromvar]]"
  - "[[30-Concepts/cistopic]]"
topics:
  - "[[40-Topics/single-cell-atac-seq]]"
---

**Citation:** Li et al. (2021) — *Chromatin-accessibility estimation from single-cell ATAC-seq data with scOpen* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-021-26530-2)

# Li et al. 2021 — scOpen

> Thesis: scATAC-seq matrices are catastrophically sparse (~3% non-zero entries; only 0–2 cut sites possible per peak per diploid cell, most lost during library prep). **scOpen** imputes and denoises the open-chromatin matrix via *regularized non-negative matrix factorization* (NMF) on a TF-IDF-transformed binary matrix, with automatic rank selection by knee detection. It improves clustering, visualization, *cis*-regulatory interaction prediction, and footprinting — and unlike SCALE or cisTopic, makes no distributional assumption and carries the lowest memory footprint.

## Key claims

- scATAC-seq is far sparser than scRNA-seq (3–7% non-zeros vs >10%) because of higher dimensionality (>10^6 regions) and severe dropout; assuming 25% of accessible DNA is sequenced, ~56% of accessible sites get zero cut sites (binomial dropout).
- scOpen pipeline: binarize → TF-IDF weighting → regularized NMF (nuclear-norm / L2 regularization, λ=1 default) solved by cyclic coordinate descent → outputs both an imputed matrix and a low-dimensional (rank-*k*) reduced matrix. Time complexity O((m+n)k) per iteration.
- Regularization is the methodological differentiator: scOpen is "the only method performing regularization of estimated models to prevent over-fitting" — overfitting being a known failure mode of single-cell imputation.
- Benchmarked against 8 imputation methods (MAGIC, SAVER, scImpute, DCA, scBFA, cisTopic-impute, SCALE, imputePCA) on 4 labeled datasets: scOpen had highest mean AUPR for recovering true OC regions, best silhouette score, and best/near-best ARI clustering — with lowest memory (≥2× less than cisTopic/MAGIC/SCALE) and tractable runtime on 10k-cell PBMC data.
- Also beats dimension-reduction pipelines (cisTopic, SnapATAC, Cusanovich2018/LSI); the low-dim scOpen matrix cuts clustering memory >1000× vs full imputed matrices.
- Biology: applied to a 30,129-cell mouse kidney UUO fibrosis time course (day 0/2/10). scOpen + HINT-ATAC footprinting + ArchR peak-to-gene links identified **Runx1 as the key TF driving fibroblast→myofibroblast differentiation**, regulating *Twist2* and *Tgfbr1*; validated by immunostaining and retroviral overexpression in human PDGFRb+ fibroblasts.

## Methods / evidence

Python package (github.com/CostaLab/scopen). Benchmarks used external labels (FACS-sorted bulk ATAC peak calls as ground truth). Imputation improves downstream tools chromVAR, Cicero ([[10-Summaries/schep-2017-chromvar]]), scABC. Cicero co-accessibility validated against GM12878 Hi-C and ChIA-PET.

## Surprising or load-bearing bits

- The dropout-correction argument for *cis*-regulatory prediction: because dropouts at two regions are independent, imputation strongly improves correlation-based co-accessibility (Cicero) — exactly the MAGIC-on-scRNA gene–gene story, ported to chromatin.
- Imputation/denoising had been "widely ignored" in scATAC-seq pipelines (Signac, ArchR) despite far worse sparsity than scRNA-seq — scOpen makes the case it should be a default step.
- The same sparsity problem applies to scChIP-seq, scCUT&Tag, scBisulfite-seq — flagged as future imputation targets.

## Entities mentioned

- [[20-Entities/ivan-costa]] — corresponding author; also author of HINT-ATAC footprinting.
- Rafael Kramann, Christoph Kuppe — kidney fibrosis biology (Aachen).

## Concepts touched

- [[30-Concepts/scopen]] — the method this paper defines.
- [[30-Concepts/scatac-imputation]] — scOpen is a leading entry; defines the benchmark.
- [[30-Concepts/scatac-seq]] · [[30-Concepts/allele-dropout]] — quantifies the dropout problem.

## Connections to other sources

- Direct competitor/benchmark of [[10-Summaries/xiong-2019-scale]] (SCALE, VAE+GMM) and [[10-Summaries/bravo-2019-cistopic]] (cisTopic-impute) — scOpen claims to beat both on AUPR, memory, and (vs cisTopic) runtime scaling.
- Improves downstream [[10-Summaries/schep-2017-chromvar]] (chromVAR) and Cicero outputs.
- Compared against dimension-reduction in [[10-Summaries/fang-2021-snapatac]] (SnapATAC) and [[10-Summaries/cusanovich-2015-sciatac]] (LSI lineage).
- Shares the sparsity framing with [[10-Summaries/gur-2025-scatac-vs-bulk]].

## Open questions

- Imputation can induce false signals (Andrews & Hemberg); scOpen argues regularization mitigates this but doesn't fully resolve when imputation helps vs misleads.
- Generalization of NMF imputation to scChIP/scCUT&Tag/scBisulfite remains untested.

---
**Source:** [DOI](https://doi.org/10.1038/s41467-021-26530-2)
## Related

- [[40-Topics/single-cell-atac-seq]] · [[30-Concepts/scopen]] · [[30-Concepts/scatac-imputation]] · [[30-Concepts/chromvar]] · [[20-Entities/ivan-costa]]
