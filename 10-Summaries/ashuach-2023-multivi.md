---
type: summary
title: "Ashuach 2023 — MultiVI: deep generative model for the integration of multimodal data"
source: "[[00-Sources/papers/MultiVI_ deep generative model for the integration of multimodal data]]"
source_quality: full
source_sha256: "3cf54e18f15100186320972cec1e3356c0a1b327a989d566834d043210062a71"
aliases: ["MultiVI", "Ashuach 2023", "scvi-tools MultiVI"]
tags: [MultiVI, deep-learning, multimodal-integration, VAE, scvi-tools, Yosef-lab, computational]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Ashuach et al. (2023) — *MultiVI: deep generative model for the integration of multimodal data* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-023-01909-9)

Ashuach, Gabitto, Koodli, Saldi, Jordan and Yosef (UC Berkeley, Allen Institute, Weizmann) developed **MultiVI**, a probabilistic deep generative model for the joint analysis of multimodal single-cell data — primarily scRNA-seq + scATAC-seq, extensible to surface protein abundance. MultiVI builds modality-specific variational autoencoders (scVI for expression, PeakVI for accessibility, totalVI for protein), then aligns their latent representations into a single joint space via an adversarial penalty that prevents modality-specific separation.

Critical capability: MultiVI handles **paired and unpaired** data jointly. Cells with only one modality (single-modality datasets) can be embedded into the same joint space as paired multiome cells; the missing modality can be probabilistically imputed with calibrated uncertainty. Benchmarked on 10x PBMC multiome data: library-size correlation 0.97 (RNA) / 0.91 (ATAC) against observed UMI counts; MultiVI and Cobolt both outperform gene-scoring and WNN on latent-space mixing; imputation reaches Spearman 0.57 (RNA) and AUPRC 0.41 (ATAC).

## Why this matters

Computational anchor for §4 (multimodal integration), filling the niche left by MOFA (linear factor analysis) and Seurat-WNN (graph-based) with a probabilistic deep-learning approach. The paired+unpaired flexibility is critical for mosaicism work where joint scWGS+scATAC paired data is essentially nonexistent — MultiVI offers a path to leverage abundant single-modality data alongside scarce paired data. Companion to Cobolt and scGPT in our computational section.

---
**Source:** [DOI](https://doi.org/10.1038/s41592-023-01909-9) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37386189/)

## Related

- [[10-Summaries/argelaguet-2019-nature]]
- [[10-Summaries/stuart-2021-natmethods]]
- [[30-Concepts/multimodal-integration-methods]]
