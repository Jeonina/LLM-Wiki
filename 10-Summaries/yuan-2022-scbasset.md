---
type: summary
title: "Yuan 2022 — scBasset: sequence-based deep CNN modeling of scATAC-seq"
source: "[[00-Sources/papers/scBasset_ sequence-based modeling of single-cell ATAC-seq using convolutional neural networks]]"
aliases: ["Yuan 2022 scBasset", "scBasset"]
tags: [scBasset, scATAC-seq, deep-learning, CNN, sequence-based, TF-activity, Calico]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/scBasset_ sequence-based modeling of single-cell ATAC-seq using convolutional neural networks]]"
---

**Citation:** Yuan et al. (2022) — *scBasset: sequence-based deep CNN modeling of scATAC-seq* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-022-01562-8)

Yuan and Kelley (Calico Life Sciences) introduced **scBasset**, a sequence-based convolutional neural network for modeling scATAC-seq. The architecture extends the Basset CNN: input is a 1,344-bp DNA sequence around each accessibility peak; eight convolutional blocks produce a peak embedding; a final dense layer with a bottleneck of size 32 connects the embedding to per-cell accessibility predictions (one task per cell). The 32-dim final-layer weights serve as cell embeddings for clustering/visualization. Benchmarked on Buenrostro2018 hematopoiesis, 10x Multiome PBMC, and 10x Multiome mouse brain: scBasset achieves competitive auROC (0.762, 0.640, 0.701 per cell) and outperforms sequence-free baselines on cell embedding, denoising, integration with scRNA-seq, and TF-activity inference.

## Why this matters

Establishes the sequence-as-prior paradigm for scATAC-seq analysis — a contrast to peak-by-cell matrix methods (cisTopic, SCALE, chromVAR) and a foundation for cross-cell-type generalization. Anchors §4 (computational analysis of scATAC-seq) alongside SnapATAC2 (Zhang 2024). Useful when arguing that scATAC-seq analysis is shifting from clustering/matrix-factorization toward representation-learning on sequence — important context for any §6 future-perspective discussion of foundation models for chromatin.

## Related

- [[10-Summaries/zhang-2024-snapatac2]]
- [[10-Summaries/buenrostro-2015-nature]]
- [[10-Summaries/luo-2024-scatac-benchmark]]
- [[10-Summaries/cao-2022-glue]]
- [[30-Concepts/scatac-analysis-methods]]

---
**Source:** [DOI](https://doi.org/10.1038/s41592-022-01562-8) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/35941239/)
