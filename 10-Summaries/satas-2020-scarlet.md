---
type: summary
title: "Satas 2020 — SCARLET: Single-Cell Tumor Phylogeny Inference with Copy-Number Constrained Mutation Losses"
aliases: ["Satas 2020 SCARLET", "SCARLET", "loss-supported tumor phylogeny"]
tags: [SCARLET, tumor-phylogeny, SNV-CNA-integration, mutation-loss, Raphael-lab, Princeton, colorectal-cancer]
created: 2026-05-13
updated: 2026-05-13
sources: ["Gryte_2020_CellSystems.pdf"]
---

Satas, Zaccaria, Mon and Raphael (Princeton, Brown) developed **SCARLET** (Single-Cell Algorithm for Reconstructing Loss-supported Evolution of Tumors), a phylogenetic inference algorithm for single-cell DNA-seq data that **explicitly models loss of single-nucleotide variants (SNVs) due to overlapping copy-number aberrations (CNAs)**.

The problem: standard scDNA-seq phylogeny tools (SCITE, OncoNEM, Sci-Phi) assume the infinite-sites model — each SNV is gained at most once and never lost. But CNAs can delete genomic regions carrying SNVs, causing apparent state transitions from 1 → 0 that the infinite-sites model can't accommodate. SCARLET allows mutation losses constrained to loci where copy-number actually decreased, jointly using SNV and CNA observations to infer the phylogeny.

Benchmarked on simulated data, SCARLET outperforms existing methods on inferring both mutation order and per-cell mutation assignments. Applied to a single-cell colorectal-cancer dataset, SCARLET constructed a phylogeny *consistent* with observed CNAs and proposed an alternate origin for the patient's metastases — a clinically-relevant reinterpretation that infinite-sites methods missed.

## Why this matters

Methodological complement to MEDICC2 (Kaufmann 2022): MEDICC2 builds CN-only phylogenies; SCITE/OncoNEM build SNV-only phylogenies under infinite-sites; SCARLET jointly models both. Particularly relevant when the dataset is **droplet-based scDNA-seq with both SNV panel and CNA inference** (e.g., Mission Bio Tapestri DNA + Tapestri CNV). Anchors §4 (phylogenetic methods) and §5 (cancer-evolution applications). Important conceptual point for the review: the dependence between SNV-loss and CN-loss is a *real biological signal* that should be modeled, not a nuisance.

---
**Source:** [DOI](https://doi.org/10.1016/j.cels.2020.04.001) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32864481/)

## Related

- [[10-Summaries/zaccaria-2021-chisel]]
- [[10-Summaries/kaufmann-2022-medicc2]]
- [[10-Summaries/jahn-2016-scite]]
- [[40-Topics/scdna-cancer-applications]]
