---
type: summary
title: "Sun 2025 — scMitoMut for calling mitochondrial lineage-related mutations in single cells"
source: "[[00-Sources/papers/scMitoMut for calling mitochondrial lineage-related mutations in single cells]]"
aliases: ["Sun 2025 scMitoMut", "scMitoMut", "Perié-lab mtDNA"]
tags: [scMitoMut, mtDNA, lineage-tracing, beta-binomial, scATAC-seq, multiome, Perie-lab, Institut-Curie]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Sun et al. (2025) — *scMitoMut for calling mitochondrial lineage-related mutations in single cells* — *Briefings in Bioinformatics*. [DOI](https://doi.org/10.1093/bib/bbaf072)

Sun, van Ginneken and Perié (Institut Curie, Sorbonne) developed **scMitoMut**, an R/Bioconductor toolkit for calling mtDNA lineage-related mutations from single-cell sequencing data. The method uses a **beta-binomial distribution** to assign each mutation a per-cell *q-value*, replacing the standard allele-frequency-threshold approach used by maegatk (MAESTER), mgatk and similar tools.

Three-step framework: (1) define wild-type allele per locus without a reference genome (highest-median-allele-frequency across cells); (2) define WT reference-cell set via binomial-mixture-model classifier, fit beta-binomial parameters to those cells; (3) call mutations using the beta-binomial *q-value*, accounting for sequencing depth and WT read count via FDR-controlled multi-test correction.

Validated on: (i) single-cell DNA sequencing of mixed cell lines (high sensitivity for small clones); (ii) human colorectal cancer scATAC-seq (more mutations detected than state-of-the-art); (iii) 10x Genomics multiome datasets (effective lineage-distance measurement between blood and brain tissue cells).

## Why this matters

A 2025 advance over MAESTER (Miller 2022) and mgatk (Lareau 2021) on the same problem: per-cell statistically-controlled mtDNA mutation calling. The beta-binomial framework parallels developments in scRNA-seq SNV calling. Particularly useful for our review's argument that single-cell mtDNA mosaicism quantification is becoming statistically rigorous, not just heuristic. Anchors §3.1 (mtDNA variant detection) and §4 (variant-calling tools).

---
**Source:** [DOI](https://doi.org/10.1093/bib/bbaf072) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/40036721/)

---
**Source:** [DOI](https://doi.org/10.1093/bib/bbaf072) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/40036721/)

## Related

- lareau 2021 natbiotech
- [[10-Summaries/miller-2022-maester]]
- [[10-Summaries/glynos-2023-mtdna-mosaicism]]
- [[30-Concepts/mitochondrial-lineage-tracing]]
