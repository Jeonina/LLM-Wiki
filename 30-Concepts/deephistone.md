---
type: concept
title: DeepHistone
aliases: []
tags: [deep-learning, histone-modifications, prediction, ChIP-seq, DNase-seq]
created: 2026-05-12
updated: 2026-10-12
---

# DeepHistone

> A two-stream CNN that predicts seven histone modifications (H3K4me3, H3K4me1, H3K36me3, H3K27me3, H3K9me3, H3K27ac, H3K9ac) from DNA sequence + DNase-seq chromatin accessibility in a given cell type ([[10-Summaries/yin-2019-deephistone|Yin 2019]]).

> [!abstract] 한눈에
> DeepHistone은 DNA 서열과 DNase-seq accessibility를 각각 CNN으로 읽은 뒤 합쳐 일곱 가지 histone modification을 예측하는 모델이다 ([[10-Summaries/yin-2019-deephistone|Yin 2019]]). 모든 세포 유형과 mark에 ChIP-seq을 하기 어려운 빈틈을 계산으로 메우려는 시도다 ([[10-Summaries/yin-2019-deephistone|Yin 2019]]).

## Definition

Three modules: DNA module (CNN on one-hot-encoded 1 kb regions, densely connected blocks), DNase module (parallel CNN on openness scores), Joint module (concatenates features, outputs 7 parallel sigmoids). Trained on Roadmap Epigenomics 15-epigenome ChIP-seq data.

## Why it matters

- Reduces experimental cost: ChIP-seq across all cell types × marks is impractical; DeepHistone fills gaps computationally.
- Learned sequence kernels correspond to known TF binding motifs — biologically interpretable.
- Functional SNP prioritization application.

## Examples

- [[10-Summaries/yin-2019-deephistone|Yin 2019]].

## Related

> [!cards]
> - `concept` [[30-Concepts/convolutional-neural-network|Convolutional neural network]] — The architecture behind both DeepHistone streams.
> - `concept` [[30-Concepts/chip-seq|ChIP-seq]] — The histone-mark training data DeepHistone predicts.
> - `concept` [[30-Concepts/dnase-seq|DNase-seq]] — The accessibility input to the DNase module.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone marks and the methods that profile them in single cells.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/yin-2019-deephistone|Yin 2019]]
