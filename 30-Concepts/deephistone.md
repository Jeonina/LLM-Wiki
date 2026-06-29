---
type: concept
title: DeepHistone
aliases: []
tags: [deep-learning, histone-modifications, prediction, ChIP-seq, DNase-seq]
created: 2026-05-12
updated: 2026-05-12
---

# DeepHistone

> A two-stream CNN that predicts seven histone modifications (H3K4me3, H3K4me1, H3K36me3, H3K27me3, H3K9me3, H3K27ac, H3K9ac) from DNA sequence + DNase-seq chromatin accessibility in a given cell type.

## Definition

Three modules: DNA module (CNN on one-hot-encoded 1 kb regions, densely connected blocks), DNase module (parallel CNN on openness scores), Joint module (concatenates features, outputs 7 parallel sigmoids). Trained on Roadmap Epigenomics 15-epigenome ChIP-seq data.

## Why it matters

- Reduces experimental cost: ChIP-seq across all cell types × marks is impractical; DeepHistone fills gaps computationally.
- Learned sequence kernels correspond to known TF binding motifs — biologically interpretable.
- Functional SNP prioritization application.

## Examples

- [[10-Summaries/yin-2019-deephistone]].

## Related

- [[40-Topics/histone-modifications]] · [[30-Concepts/chip-seq]] · [[30-Concepts/dnase-seq]] · [[30-Concepts/convolutional-neural-network]] · [[40-Topics/histone-modifications]]
