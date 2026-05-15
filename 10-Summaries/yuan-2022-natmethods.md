---
type: summary
title: "Yuan & Kelley 2022 — scBasset: sequence-based modeling of single-cell ATAC-seq using convolutional neural networks"
aliases: ["scBasset", "Yuan 2022"]
tags: [scATAC-seq, deep-learning, CNN, sequence-based, computational]
created: 2026-05-13
updated: 2026-05-13
sources: ["Han_2022_NatureMethods.pdf"]
---

**Citation:** Yuan et al. (2022) — *scBasset: sequence-based modeling of single-cell ATAC-seq using convolutional neural networks* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-022-01562-8)

Yuan and Kelley (Calico Life Sciences) introduced scBasset, a sequence-based convolutional neural network that predicts single-cell chromatin accessibility from the underlying DNA sequence. The model takes a 1,344-bp DNA window around each peak's center as input, runs it through 8 convolutional blocks, then through a 32-dimensional bottleneck layer that learns a low-dimensional representation of the peak; a dense final layer connects the peak embedding to per-cell accessibility predictions. The cell-side parameters of the final layer serve as cell embeddings useful for clustering, denoising, integration, and TF activity inference.

scBasset achieves state-of-the-art performance on three benchmark datasets (Buenrostro 2018 hematopoiesis, 10x multiome PBMC, 10x multiome mouse brain) with auROC of 0.730–0.762 per peak on held-out peaks — within range of bulk DNase auROC despite the substantially noisier single-cell signal. The sequence-based approach outperforms peak-based methods (chromVAR, cisTopic, BROCKMAN) on cell-state representation, particularly in multiome data.

## Why this matters

Demonstrates that DNA sequence is a sufficient predictor of cell-type-specific accessibility, complementing the empirical approach taken by ATAC-peak-based methods. Anchors §4 (computational framework) and connects to sequence-based prediction tools more broadly (DeepHistone, Enformer, scGPT). Useful for the framing in §6 limitations: sequence determines a substantial fraction of accessibility but not all, and the residual is the cell-state-specific signal.

---
**Source:** [DOI](https://doi.org/10.1038/s41592-022-01562-8) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/35941239/)

---
**Source:** [DOI](https://doi.org/10.1038/s41592-022-01562-8) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/35941239/)

## Related

- [[10-Summaries/chromvar-inferring-transcription-factor-associated-accessibility-from-single-cell-epigenomic-data]]
- [[10-Summaries/cistopic-cis-regulatory-topic-modeling-on-single-cell-atac-seq-data]]
- [[10-Summaries/deephistone-a-deep-learning-approach-to-predicting-histone-modifications]]
