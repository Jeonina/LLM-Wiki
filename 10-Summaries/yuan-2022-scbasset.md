---
type: summary
title: "Yuan & Kelley 2022 — scBasset: sequence-based modeling of single-cell ATAC-seq using convolutional neural networks"
source: "[[00-Sources/papers/scBasset_ sequence-based modeling of single-cell ATAC-seq using convolutional neural networks]]"
source_quality: full
source_sha256: "8b12dc6b66cedc777d5729ff207f6f205cfbbd62c776b124e6e3dd9af5728cee"
aliases: ["scBasset", "Yuan 2022"]
tags: [scATAC-seq, deep-learning, CNN, sequence-based, computational]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Yuan & Kelley (2022) — *scBasset: sequence-based modeling of single-cell ATAC-seq using convolutional neural networks* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-022-01562-8)

Yuan and Kelley (Calico Life Sciences) introduced scBasset, a sequence-based convolutional neural network that predicts single-cell chromatin accessibility from the underlying DNA sequence. The model takes a 1,344-bp DNA window around each peak's center as input, runs it through 8 convolutional blocks, then through a 32-dimensional bottleneck layer that learns a low-dimensional representation of the peak; a dense final layer connects the peak embedding to per-cell accessibility predictions. The cell-side parameters of the final layer serve as cell embeddings useful for clustering, denoising, integration, and TF activity inference.

scBasset achieves state-of-the-art performance on three benchmark datasets (Buenrostro 2018 hematopoiesis, 10x multiome PBMC, 10x multiome mouse brain) with held-out-peak auROC of 0.662–0.734 per peak (0.640–0.762 per cell) across the three datasets. The sequence-based approach outperforms existing methods (chromVAR, cisTopic, SCALE, scDEC, peakVI) on cell-state representation, particularly in multiome data.

## Why this matters

Demonstrates that DNA sequence is a sufficient predictor of cell-type-specific accessibility, complementing the empirical approach taken by ATAC-peak-based methods. Anchors §4 (computational framework) and connects to sequence-based prediction tools more broadly (DeepHistone, Enformer, scGPT). Useful for the framing in §6 limitations: sequence determines a substantial fraction of accessibility but not all, and the residual is the cell-state-specific signal.

---
**Source:** [DOI](https://doi.org/10.1038/s41592-022-01562-8) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/35941239/)

---
**Source:** [DOI](https://doi.org/10.1038/s41592-022-01562-8) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/35941239/)

## Later comparisons

- [[fan-2026-gfetm]] (GFETM) benchmarks against scBasset on the same three datasets: competitive on clustering, better on unseen cells (scBasset must be fine-tuned because cell embeddings are parameters), on leave-one-chromosome-out peak imputation, and on marker enrichment >1 kb from the TSS; scBasset is better within 1 kb and about 3× faster.

## Related

- [[10-Summaries/schep-2017-chromvar]]
- [[10-Summaries/bravo-2019-cistopic]]
- [[10-Summaries/yin-2019-deephistone]]
