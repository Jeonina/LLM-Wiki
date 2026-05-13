---
type: summary
title: "Cui 2024 — scGPT: toward building a foundation model for single-cell multi-omics using generative AI"
aliases: ["scGPT", "Cui 2024", "single-cell foundation model"]
tags: [foundation-model, generative-AI, single-cell, multi-omics, transformer, computational]
created: 2026-05-13
updated: 2026-05-13
sources: ["Haotian_2024_NatureMethods.pdf"]
---

Cui, Wang, Maan and colleagues (Wang lab, Vector Institute / Toronto) introduced scGPT, a transformer-based foundation model pretrained on $\sim$33 million scRNA-seq cells from 51 organs/tissues and 441 studies via the CELLxGENE collection. The model uses a custom attention mask suitable for non-sequential omics data and is pretrained in a self-supervised manner to jointly learn cell embeddings and gene embeddings; downstream tasks (cell-type annotation, multi-batch integration, multi-omic integration, perturbation-response prediction, gene-regulatory network inference) are addressed by fine-tuning.

Benchmarking shows scGPT outperforming task-specific models on cell-type annotation in held-out datasets (e.g., MS dataset accuracy 0.85, tumor-infiltrating myeloid generalization), with the fine-tuned model also outperforming Geneformer, TOSICA, and scBERT on classification metrics. Demonstrates that pretrained foundation models trained at sufficient scale ($\sim$10$^7$ cells, $\sim$10$^8$ parameters) inherit generalist capabilities that fine-tuning can specialize.

## Why this matters

A representative foundation-model approach to single-cell biology. Anchors §4 (computational framework) and §7 (future perspectives) by exemplifying where the field is heading: large pretrained models, transfer learning, joint representation across modalities. Useful for the §7 framing of where computational methods will go.

## Related

- [[10-Summaries/yuan-2022-natmethods]]
- [[10-Summaries/stuart-2021-natmethods]]
- [[30-Concepts/single-cell-foundation-models]]
