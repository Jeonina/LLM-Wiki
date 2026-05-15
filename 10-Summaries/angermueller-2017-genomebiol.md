---
type: summary
title: "Angermueller 2017 — DeepCpG: accurate prediction of single-cell DNA methylation states using deep learning"
aliases: ["DeepCpG", "Angermueller 2017"]
tags: [deep-learning, methylation, single-cell, computational, sequence-prediction, Stegle-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Christof_2017_GenomeBiology.pdf"]
---

**Citation:** Angermueller et al. (2017) — *DeepCpG: accurate prediction of single-cell DNA methylation states using deep learning* — *Genome Biology*. [DOI](https://doi.org/10.1186/s13059-017-1233-z)

Angermueller, Lee, Reik and Stegle developed DeepCpG, a deep-neural-network method that predicts missing single-cell methylation states from a combination of local DNA sequence and neighboring CpG methylation in the same and other cells. The model architecture has three modules: a CpG module (bidirectional GRU over neighboring CpG states across cells), a DNA module (CNN over local DNA sequence windows), and a Joint module that integrates both representations to predict per-cell-per-CpG methylation state.

DeepCpG addresses the central computational problem of single-cell methylome data: only 20–40% of CpGs are covered per cell in scBS-seq and 1–10% in scRRBS, leaving most sites as missing values. Standard cluster-level imputation loses cell-to-cell variability information; DeepCpG preserves per-cell information by jointly modeling sequence context and observed methylation in nearby cells. Validation across mES, human, and mouse single-cell methylomes shows substantially improved imputation accuracy versus prior methods, and the learned DNA-sequence motifs identify sequence determinants of methylation variability.

## Why this matters

A foundational deep-learning approach for the methylome — predating scBasset (Yuan 2022) and Enformer for accessibility, and predating scGPT (Cui 2024) for foundation-model single-cell biology. Anchors §4 (computational framework) and demonstrates the sequence-based-prediction approach to single-cell missing-data problems generalizes across modalities. Relevant to §6 (limitations): scWGS-based mutation detection at unsampled cells could in principle benefit from analogous models.

---
**Source:** [DOI](https://doi.org/10.1186/s13059-017-1233-z) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/28499443/)

## Related

- [[30-Concepts/dna-methylation]]
- [[10-Summaries/yuan-2022-natmethods]]
- [[10-Summaries/cui-2024-natmethods]]
- [[10-Summaries/deephistone-a-deep-learning-approach-to-predicting-histone-modifications]]
