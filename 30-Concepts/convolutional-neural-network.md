---
type: concept
title: Convolutional neural network
aliases: [CNN, deep convolutional network]
tags: [deep-learning, machine-learning, image-recognition, genomics]
created: 2026-05-12
updated: 2026-10-12
---

# Convolutional neural network (CNN)

> A neural-network architecture using sliding convolutional filters (kernels) that learn local sequence/spatial patterns. Originally developed for image recognition, widely adopted in genomics where DNA sequence is naturally 1D and motif-like patterns are local.

> [!abstract] 한눈에
> CNN은 짧은 kernel을 서열 위로 밀어 가며 motif 같은 국소 패턴을 배우는 구조로, DeepSEA·Basenji 같은 서열→chromatin 예측 모델의 뼈대다 ([[10-Summaries/zhou-2015-deepsea|DeepSEA]]; [[10-Summaries/kelley-2018-basenji|Basenji]]). 지금도 task별 CNN이 transformer DNA language model과 비슷하거나 더 나은 성능을 내는 경우가 있다 ([[10-Summaries/fishman-2025-gena-lm|GENA-LM]]; [[10-Summaries/dallatorre-2025-nucleotide-transformer|Nucleotide Transformer]]).

## Definition

A CNN comprises convolutional layers (kernels of width 4 × length k for DNA), pooling layers (downsampling), and dense layers (final classification). Densely connected variants (DenseNet) connect each layer to all subsequent layers to alleviate vanishing gradients.

## Why it matters

In genomics, CNNs power DeepBind, DeepSEA, DanQ, DeepEnhancer, DeepHistone, Basenji, Enformer. They learn cis-regulatory motifs from data without prior annotation (see [[30-Concepts/de-novo-motif-discovery|de novo motif discovery]]).

## CNN models in genomics

| Model | Architecture | Input context | Output | Source |
|---|---|---|---|---|
| DeepSEA (2015) | Three convolution layers (320/480/960 kernels) | 1 kb | 919 chromatin features | ([[10-Summaries/zhou-2015-deepsea\|DeepSEA]]) |
| Basenji | Seven densely connected dilated convolution layers | ~32 kb receptive field | Coverage tracks | ([[10-Summaries/kelley-2018-basenji\|Basenji]]) |
| [[30-Concepts/deephistone\|DeepHistone]] | DenseNet-style CNN modules for sequence and accessibility | — | Histone marks | — |
| BPNet | Supervised CNN trained from scratch | — | — | ([[10-Summaries/dallatorre-2025-nucleotide-transformer\|Nucleotide Transformer]]) |
| SpliceAI | Task-specific CNN | — | Splice-site annotation | ([[10-Summaries/fishman-2025-gena-lm\|GENA-LM]]) |
| scBasset | Supervised CNN sequence model for scATAC | Short-range sequence context | — | ([[10-Summaries/fan-2026-gfetm\|GFETM]]) |

## Evidence and examples

**Context length**

- DeepSEA showed that 1 kb context beats 200 bp and 500 bp inputs (P < 2.2e-16) ([[10-Summaries/zhou-2015-deepsea|DeepSEA]]).
- In Basenji, accuracy rose monotonically from one to seven dilated layers for all data types ([[10-Summaries/kelley-2018-basenji|Basenji]]).

**CNNs as baselines for DNA language models**

- In the Nucleotide Transformer benchmark, supervised BPNet averaged MCC 0.665–0.683 across 18 tasks, a strong baseline that NT probing beat on only 8 tasks and NT fine-tuning on 12 ([[10-Summaries/dallatorre-2025-nucleotide-transformer|Nucleotide Transformer]]).
- SpliceAI still beat the best transformer DNA language model on splice-site annotation (mean PR AUC 0.960 vs 0.947) ([[10-Summaries/fishman-2025-gena-lm|GENA-LM]]).

**scATAC peak encoders**

- In the full GFETM preprint, GFETM is competitive with, not clearly better than, scBasset on clustering, and an ETM with a CNN peak encoder did worse than GFETM, though CNN designs were not explored thoroughly ([[10-Summaries/fan-2026-gfetm|GFETM]]).
- scBasset gave better marker enrichment within 1 kb of the TSS and GFETM beyond it, which the authors attribute to CNN receptive fields vs attention ([[10-Summaries/fan-2026-gfetm|GFETM]]).

## Contested points

- GFETM argues that CNN sequence models for scATAC such as scBasset are trained supervised and see only short-range sequence context, and proposes self-supervised, attention-based genome foundation models (DNABERT, DNABERT-2, Nucleotide Transformer, HyenaDNA) as the replacement peak-sequence encoder ([[10-Summaries/fan-2026-gfetm|GFETM]]). Its own results show GFETM only competitive with scBasset, and the BPNet and SpliceAI baselines above held up against transformers ([[10-Summaries/fan-2026-gfetm|GFETM]]; [[10-Summaries/dallatorre-2025-nucleotide-transformer|Nucleotide Transformer]]; [[10-Summaries/fishman-2025-gena-lm|GENA-LM]]), so the case for replacing CNNs is not settled (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/deephistone|DeepHistone]] — Two-stream CNN predicting histone marks from sequence and accessibility.
> - `concept` [[30-Concepts/de-novo-motif-discovery|De novo motif discovery]] — Learned first-layer filters act as de novo motifs.

## All sources on this page

> [!info]- 5 summaries cited here
> - [[10-Summaries/dallatorre-2025-nucleotide-transformer|Nucleotide Transformer 2025]]
> - [[10-Summaries/fan-2026-gfetm|Fan 2026]]
> - [[10-Summaries/fishman-2025-gena-lm|GENA-LM 2025]]
> - [[10-Summaries/kelley-2018-basenji|Basenji 2018]]
> - [[10-Summaries/zhou-2015-deepsea|DeepSEA 2015]]
