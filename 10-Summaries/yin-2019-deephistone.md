---
type: summary
title: "Yin et al. 2019 — DeepHistone: CNN prediction of 7 histone marks from DNA + DNase"
source: "[[00-Sources/papers/DeepHistone_ a deep learning approach to predicting histone modifications]]"
source_kind: paper
author: "Qijin Yin, Mengmeng Wu, Qiao Liu, Hairong Lv, Rui Jiang (corresponding)"
published: 2019-04-04
ingested: 2026-05-12
doi: "10.1186/s12864-019-5489-4"
journal: "BMC Genomics"
tags: [deep-learning, histone-modifications, ChIP-seq, DNase-seq, CNN, prediction, ENCODE]
entities:
  - "[[20-Entities/rui-jiang]]"
  - "qijin yin"
concepts:
  - "[[30-Concepts/deephistone]]"
  - "[[40-Topics/histone-modifications]]"
  - "[[30-Concepts/chip-seq]]"
  - "[[30-Concepts/dnase-seq]]"
  - "[[30-Concepts/convolutional-neural-network]]"
topics:
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Yin et al. (2019) — *DeepHistone: CNN prediction of 7 histone marks from DNA + DNase* — *BMC Genomics*. [DOI](https://doi.org/10.1186/s12864-019-5489-4)

# Yin et al. 2019 — DeepHistone

> Thesis: ChIP-seq mapping of histone marks across hundreds of cell types × tens of marks is too expensive to execute experimentally. **DeepHistone** is a densely-connected CNN that predicts seven histone modifications (H3K4me3, H3K4me1, H3K36me3, H3K27me3, H3K9me3, H3K27ac, H3K9ac) from DNA sequence + DNase-seq accessibility in a given cell type. The two-stream architecture (DNA module + DNase module + joint module) integrates sequence-intrinsic regulatory signatures with cell-type-specific chromatin context, outperforming sequence-only baselines and capturing functional SNPs.

## Key claims

- **Architecture**: a DNA module (CNN with one-hot-encoded 1 kb regions, densely connected blocks), a DNase module (parallel CNN on openness scores), and a joint module that fuses the two and outputs 7 parallel sigmoid predictions (one per histone mark, not mutually exclusive).
- **Performance**: outperforms baseline methods (logistic regression on TFs, linear regression on histone marks) both within-epigenome and across-epigenomes — i.e., trained on one cell type and tested on another.
- **Trained on Roadmap Epigenomics** ChIP-seq peaks from 21 (filtered to 15) epigenomes that had all 7 marks profiled. 7.6 M positive sites across ~3 billion candidate windows.
- **Sequence signatures**: the convolutional kernels learned by the DNA module correspond to known TF binding sites, validating that the model has captured biologically meaningful regulatory features.
- **Functional SNP discrimination**: DeepHistone scores can distinguish disease-associated SNPs from nearby non-functional variants, suggesting application as a regulatory-variant prioritization tool.

## Methods / evidence

PyTorch implementation. 200-bp scan windows over hg19 with step 200 bp; window labeled as positive if it overlaps a ChIP-seq peak by ≥100 bp. DNase fold-enrichment used as openness score. Adam optimizer, early stopping. Single GPU (NVIDIA GTX 1080Ti).

## Surprising or load-bearing bits

- The **hybrid sequence + accessibility input** is the methodological insight: pure sequence models (DeepBind, DeepSEA, DanQ) can't generate cell-type-specific predictions because DNA is the same in every cell. Adding DNase signal makes the prediction conditional on cell state.
- Multi-task learning (predicting 7 marks in parallel via 7 sigmoid outputs) is more efficient than 7 independent binary models and lets the model share representations across related marks.

## Connections to other sources

- Sits in the tooling stack for [[40-Topics/histone-modifications]] alongside single-cell experimental methods like [[10-Summaries/ku-2019-scchic-seq]] (scChIC-seq), [[10-Summaries/yeung-2023-scchix-seq]] (scChIX-seq), and [[10-Summaries/janssens-2023-scicut-tag]] (sciCUT&Tag).
- The accessibility input dependency means DeepHistone benefits directly from advances in cheaper accessibility profiling like [[10-Summaries/mezger-2018-microfluidic-atac]] (µATAC).
- Complementary to deep-learning models that predict expression from sequence alone (Enformer, Basenji) — DeepHistone predicts the chromatin layer those models also implicitly model.

## Open questions

- 2019 architecture; would benefit from modern transformer-style models (DNABERT, HyenaDNA) that can process longer sequences.
- Predictions are bulk-cell-type-level; single-cell extension non-trivial because DNase signal in single cells is sparse.

---
**Source:** [DOI](https://doi.org/10.1186/s12864-019-5489-4)
## Related

- [[40-Topics/histone-modifications]] · [[30-Concepts/deephistone]] · [[30-Concepts/convolutional-neural-network]] · [[30-Concepts/dnase-seq]]
