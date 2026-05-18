---
type: summary
title: "Lu 2024 — Cancer phylogenetic inference using copy number alterations detected from DNA sequencing data"
source: "[[00-Sources/papers/Cancer phylogenetic inference using copy number alterations detected from DNA sequencing data]]"
aliases: ["Lu 2024 review", "Bingxin Lu", "CNA phylogeny review"]
tags: [review, CNA-phylogeny, cancer-evolution, tumor-heterogeneity, MEDICC, Lu-lab, Surrey]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/Cancer phylogenetic inference using copy number alterations detected from DNA sequencing data]]"
---

**Citation:** Lu et al. (2024) — *Cancer phylogenetic inference using copy number alterations detected from DNA sequencing data* — *CancerPathogenesisTherapy*. [DOI](https://doi.org/10.1016/j.cpt.2024.04.003)

Lu (Surrey) reviews cancer phylogenetic-inference methods that use **copy-number alterations (CNAs) — alone or jointly with SNVs/SVs — as evolutionary markers**. The review surveys distance-based methods (MP, ML, Bayesian likelihood approaches), categorizes methods by marker type (CNA-only, CNA+SNV, CNA+SV) and tree type (sample tree, clone tree, mutation tree), and discusses challenges across three axes: input data (segmentation noise, allele-specific phasing), evolutionary models (rate parameters, parallel evolution, WGD), and inference algorithms (long-branch attraction, scalability).

Application sections cover: intratumor heterogeneity (ITH) characterization, metastasis seeding inference, treatment-resistance evolution, early cancer-development reconstruction (clonal hematopoiesis to overt malignancy). Lu notes that there have been no systematic reviews specifically of CNA-based phylogeny methods despite ~10 years of activity (Schwarz/MEDICC 2014 → CHISEL → MEDICC2 → SCARLET → many others).

## Why this matters

A dedicated review of CNA-phylogenetic methods complementing Mallory 2020 (CNA-detection methods) and Vandereyken/Voet 2023 (multi-omics overall). Anchors §4 (phylogenetic methods family) and §5 (cancer-evolution applications). Useful framing for the review's §4 organization: separates CNA-only methods (MEDICC2) from joint SNV+CNA methods (SCARLET) from SV-aware methods.

---
**Source:** [DOI](https://doi.org/10.1016/j.cpt.2024.04.003) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/39872371/)

## Related

- [[10-Summaries/mallory-2020-cna-review]]
- [[10-Summaries/kaufmann-2022-medicc2]]
- [[10-Summaries/satas-2020-scarlet]]
- [[40-Topics/scdna-cancer-applications]]
