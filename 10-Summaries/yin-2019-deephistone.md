---
type: summary
title: "Yin 2019 — DeepHistone: deep learning for histone modification prediction"
aliases: ["Yin 2019 DeepHistone", "DeepHistone"]
tags: [DeepHistone, deep-learning, histone-modification, CNN, DNA-sequence, DNase-seq, Jiang-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["DeepHistone_ a deep learning approach to predicting histone modifications.md"]
---

Yin, Wu, Liu, Lv, Jiang (Tsinghua) developed **DeepHistone**, a deep CNN integrating DNA sequence + chromatin accessibility (DNase-seq) to predict 7 histone modifications (H3K4me3, H3K4me1, H3K36me3, H3K27me3, H3K9me3, H3K27ac, H3K9ac). Three modules: DNA module (densely connected CNN on one-hot sequence), DNase module (same architecture on openness scores), Joint module (concatenation + 7 sigmoid outputs). Outperforms baselines within and across epigenomes. Sequence signatures extracted match known TF binding sites.

## Why this matters

A bulk-data deep-learning approach for histone-modification imputation — useful when ChIP-seq is unavailable. Could complement scATAC-based chromatin-state inference. Marginal relevance to scDNA-mosaicism review but worth noting in §4 computational methods if histone-mark imputation is discussed.

---
**Source:** [Open paper](https://link.springer.com/article/10.1186/s12864-019-5489-4)
## Related

- [[10-Summaries/yuan-2022-scbasset]]
- [[10-Summaries/klemm-2019-chromatin-accessibility-review]]
