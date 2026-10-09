---
type: concept
title: Convolutional neural network
aliases: [CNN, deep convolutional network]
tags: [deep-learning, machine-learning, image-recognition, genomics]
created: 2026-05-12
updated: 2026-10-08
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


## Added 2026-10-08 — sequence models & foundation models

- DeepSEA (2015) used three convolution layers (320/480/960 kernels) over 1 kb to predict 919 chromatin features, showing that 1 kb context beats 200 bp and 500 bp inputs (P < 2.2e-16) ([[10-Summaries/zhou-2015-deepsea]])
- Basenji added seven densely connected dilated convolution layers to reach a ~32 kb receptive field; accuracy rose monotonically from one to seven dilated layers for all data types ([[10-Summaries/kelley-2018-basenji]])
- In the Nucleotide Transformer benchmark, supervised BPNet trained from scratch averaged MCC 0.665–0.683 across 18 tasks, a strong baseline that NT probing beat on only 8 tasks and NT fine-tuning on 12 ([[10-Summaries/dallatorre-2025-nucleotide-transformer]])
- SpliceAI, a task-specific CNN, still beat the best transformer DNA language model on splice-site annotation (mean PR AUC 0.960 vs 0.947) ([[10-Summaries/fishman-2025-gena-lm]]).

## Related

- [[30-Concepts/deephistone]] · [[30-Concepts/de-novo-motif-discovery]]
