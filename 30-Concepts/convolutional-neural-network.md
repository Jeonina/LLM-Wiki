---
type: concept
title: Convolutional neural network
aliases: [CNN, deep convolutional network]
tags: [deep-learning, machine-learning, image-recognition, genomics]
created: 2026-05-12
updated: 2026-10-07
---

# Convolutional neural network (CNN)

> A neural-network architecture using sliding convolutional filters (kernels) that learn local sequence/spatial patterns. Originally developed for image recognition, widely adopted in genomics where DNA sequence is naturally 1D and motif-like patterns are local.

## Definition

A CNN comprises convolutional layers (kernels of width 4 × length k for DNA), pooling layers (downsampling), and dense layers (final classification). Densely connected variants (DenseNet) connect each layer to all subsequent layers to alleviate vanishing gradients.

## Why it matters

In genomics, CNNs power DeepBind, DeepSEA, DanQ, DeepEnhancer, DeepHistone, Basenji, Enformer. They learn cis-regulatory motifs from data without prior annotation.

## Examples

- [[30-Concepts/deephistone]] uses DenseNet-style CNN modules for sequence and accessibility.

## Added 2026-10-07

GFETM argues that CNN sequence models for scATAC such as scBasset are trained supervised and see only short-range sequence context, and proposes self-supervised, attention-based genome foundation models (DNABERT, DNABERT-2, Nucleotide Transformer, HyenaDNA) as the replacement peak-sequence encoder ([[10-Summaries/fan-2026-gfetm]]). In the full preprint, GFETM is competitive with, not clearly better than, scBasset on clustering, and an ETM with a CNN peak encoder did worse than GFETM, though CNN designs were not explored thoroughly ([[10-Summaries/fan-2026-gfetm]]). scBasset gave better marker enrichment within 1 kb of the TSS and GFETM beyond it, which the authors attribute to CNN receptive fields vs attention ([[10-Summaries/fan-2026-gfetm]]).


## Related

- [[30-Concepts/deephistone]] · [[30-Concepts/de-novo-motif-discovery]]
