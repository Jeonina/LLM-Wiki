---
type: summary
title: "Xiong et al. 2019 — SCALE: VAE + Gaussian Mixture Model for scATAC-seq"
source: "[[00-Sources/papers/SCALE method for single-cell ATAC-seq analysis via latent feature extraction]]"
source_kind: paper
author: "Lei Xiong, Kui Xu, Kang Tian, Yanqiu Shao, Lei Tang, Ge Gao, Michael Zhang, Tao Jiang, Qiangfeng Cliff Zhang (corresponding)"
published: 2019-10-08
ingested: 2026-06-02
doi: "10.1038/s41467-019-12630-7"
journal: "Nature Communications"
tags: [scATAC-seq, deep-learning, VAE, gaussian-mixture-model, imputation, clustering, batch-effects]
entities:
  - "[[20-Entities/qiangfeng-cliff-zhang]]"
concepts:
  - "[[30-Concepts/scale]]"
  - "[[30-Concepts/scatac-imputation]]"
  - "[[30-Concepts/scatac-seq]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/chromvar]]"
topics:
  - "[[40-Topics/single-cell-atac-seq]]"
---

**Citation:** Xiong et al. (2019) — *SCALE method for single-cell ATAC-seq analysis via latent feature extraction* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-019-12630-7)

# Xiong et al. 2019 — SCALE

> Thesis: scATAC-seq data are near-binary and even sparser than scRNA-seq, so scRNA-seq tools underfit. **SCALE** combines a variational autoencoder (VAE) with a *Gaussian Mixture Model* (GMM) prior over the latent space, yielding latent features that simultaneously support visualization, clustering, and denoising/imputation — and, because the GMM disentangles the latent dimensions, exposes interpretable features that map onto cell types and even batch effects.

## Key claims

- The GMM prior is the key advance over a plain VAE: a single isotropic Gaussian (as in scVI) underfits sparse data; a mixture of Gaussians gives a tighter posterior and learns disentangled, interpretable latent dimensions. Ablating the GMM degrades SCALE to scVI-level performance.
- Architecture: encoder 3200-1600-800-400 (ReLU), 10-dim latent on a GMM manifold, single-layer Bernoulli decoder back to peaks. Trained by maximizing the ELBO (reconstruction + KL-to-GMM).
- Across six mixture datasets (Leukemia, GM12878/HEK293T, GM12878/HL-60, InSilico, Splenocyte, Forebrain) SCALE gave the best overall clustering (ARI/NMI/F1) vs scABC, SC3, scVI, cisTopic, TF-IDF, Cicero.
- Denoising: SCALE-imputed single cells correlate best with their cell-type "meta-cells" vs scRNA-seq imputers (scImpute, SAVER, MAGIC, scVI) — while preserving within-type variation rather than over-smoothing.
- Imputation improves downstream chromVAR motif discovery (Forebrain: 52 → 105 significant motifs; recovered Mafb/Hoxd9 in microglia, Dlx2/Lhx8/Arx in MGE pathway).
- On the Pi-ATAC mouse breast-tumor data SCALE separated Epcam+ tumor from CD45+ immune cells from chromatin alone — comparable to the protein-indexed experimental method — and recovered immune (Runx1, PU.1-IRF, SpiB) vs tumor (Ets1, Nrf2) motifs.
- Disentangled features can flag **batch effects** (plate-specific features in the Pi-ATAC data) so they can be excluded from embedding/clustering. Scales to the ~80k-cell mouse sci-ATAC atlas (~1.5 h, ~2 GB).

## Methods / evidence

PyTorch + scikit-learn (github.com/jsxlei/SCALE). Cluster number can be auto-chosen via Tracy-Widom eigenvalue thresholding (as in SC3). Robust to simulated dropout up to ~0.6 corruption. GPU used for the two deep methods (SCALE, DCA).

## Surprising or load-bearing bits

- The interpretability angle: because each latent dimension is a separate Gaussian directly wired to output peaks, SCALE features can be read as biological programs *or* as technical artifacts (plate/batch) — a rare combination of generative power and interpretability.
- A clean demonstration that scRNA-seq imputers (MAGIC, scVI) actively harm scATAC-seq analysis (they made misclassified subgroups *less* similar to their true types) — motivating ATAC-specific tooling.

## Entities mentioned

- [[20-Entities/qiangfeng-cliff-zhang]] — corresponding author (Tsinghua).
- scVI (Lopez/Yosef) — the VAE baseline SCALE improves on.

## Concepts touched

- [[30-Concepts/scale]] — the method this paper defines.
- [[30-Concepts/scatac-imputation]] — SCALE is the deep-learning entry in the benchmark.
- [[30-Concepts/chromvar]] — downstream beneficiary of imputation.

## Connections to other sources

- Direct competitor of [[10-Summaries/li-2021-scopen]] (scOpen, regularized NMF) and [[10-Summaries/bravo-2019-cistopic]] (cisTopic, LDA). scOpen later reports beating SCALE on AUPR and memory; SCALE is a GPU/deep-learning approach with memory limits on very large data.
- Benchmarked against [[10-Summaries/zamanighomi-2018-scabc]] (scABC) and [[10-Summaries/schep-2017-chromvar]] (chromVAR).
- Conceptual sibling of [[10-Summaries/fang-2021-snapatac]] for dimension reduction; precursor approach to deep generative ATAC tools (scBasset).

## Open questions

- SCALE was not designed to *remove* batch effects, only to reveal them — explicit batch-correction modeling left for future work.
- GPU memory caps the number of cells per run; large atlases need quick-mode/subsampling.

---
**Source:** [DOI](https://doi.org/10.1038/s41467-019-12630-7)
## Related

- [[40-Topics/single-cell-atac-seq]] · [[30-Concepts/scale]] · [[30-Concepts/scatac-imputation]] · [[30-Concepts/chromvar]] · [[20-Entities/qiangfeng-cliff-zhang]]
