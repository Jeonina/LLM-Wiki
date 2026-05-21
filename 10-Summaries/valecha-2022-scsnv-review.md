---
type: summary
title: "Valecha 2022 — Somatic variant calling from single-cell DNA sequencing data"
source: "[[00-Sources/papers/Somatic variant calling from single-cell DNA sequencing data]]"
aliases: ["Valecha 2022", "Posada scDNA review", "scSNV caller review"]
tags: [review, scDNA-SNV-calling, allelic-dropout, amplification-error, Posada-lab, CSBJ]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Valecha et al. (2022) — *Somatic variant calling from single-cell DNA sequencing data* — *ComputationalStructuralBiotechnologyJournal*. [DOI](https://doi.org/10.1016/j.csbj.2022.06.013)

Valecha and Posada (Universidade de Vigo) reviewed computational approaches for **somatic single-nucleotide variant (SNV) calling from scDNA-seq data**. The review categorizes the technical biases scWGA introduces — allele dropout (ADO), allelic imbalance (AI), locus dropout (LDO), amplification errors — and surveys the eight major SNV-caller families designed to handle them: Monovar (multi-cell pooled likelihood), SCcaller (local-bias correction), SCAN-SNV (sequencing-context-aware), ProSolo (combined bulk+single-cell), LiRA (linkage-disequilibrium phasing), SCIΦ (joint inference with tree), SecedoTree, Conbase.

Performance comparison via three axes: statistical performance (sensitivity, FDR, FP rate), speed benchmark, and modeling philosophy (genotype-likelihood vs phylogeny-aware). Conclusion: no single caller is universally best; choice depends on (a) scWGA chemistry (MDA vs MALBAC vs PTA), (b) coverage depth, (c) whether bulk control is available, (d) whether tree inference is needed simultaneously.

## Why this matters

A focused review of scDNA SNV calling that complements Lähnemann 2017 (broader scWGS challenges), Gawad 2016 (foundational), and Ha 2023 (mosaic-caller benchmark for bulk). Anchors §4 (SNV-calling tool family) and §6 (limitations). Useful for the review's tone-setting on scWGS variant calling: the field has many tools, all with known weaknesses, and consensus across multiple callers is the de-facto best practice.

---
**Source:** [DOI](https://doi.org/10.1016/j.csbj.2022.06.013) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/35782734/)

---
**Source:** [DOI](https://doi.org/10.1016/j.csbj.2022.06.013) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/35782734/)

## Related

- [[10-Summaries/zafar-2016-monovar]]
- [[10-Summaries/dong-2017-sccaller]]
- [[10-Summaries/luquette-2019-natcomm]]
- lahnemann 2021 natrev
- [[40-Topics/mosaic-variant-calling]]
