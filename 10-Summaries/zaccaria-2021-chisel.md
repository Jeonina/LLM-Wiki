---
type: summary
title: "Zaccaria 2021 — Characterizing allele- and haplotype-specific copy numbers in single cells with CHISEL"
source: "[[00-Sources/papers/Characterizing allele- and haplotype-specific copy numbers in single cells with CHISEL]]"
aliases: ["Zaccaria 2021", "CHISEL", "allele-specific CNV scDNA"]
tags: [CHISEL, allele-specific-CNV, haplotype-phasing, scDNA-seq, breast-cancer, Raphael-lab, Princeton]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Zaccaria et al. (2021) — *Characterizing allele- and haplotype-specific copy numbers in single cells with CHISEL* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-020-0661-6)

Zaccaria and Raphael (Princeton) developed **CHISEL** (Copy-number Haplotypes Inferred in Single cells using Evolutionary Links), a computational method that infers **allele-specific** and **haplotype-specific** copy numbers in single cells from low-coverage (<0.05× per cell) scDNA-seq data — for instance, 10x Genomics Chromium single-cell CNV Solution datasets of ~2,000 cells.

The challenge: standard B-allele-frequency (BAF) methods break down at <0.05× coverage because individual SNPs are rarely covered. CHISEL aggregates germline SNP information across 50-kb haplotype blocks using reference-based phasing, then across the genome and across cells via global clustering. Five-step pipeline: (1) compute per-cell, per-bin read-depth ratio (RDR) and BAF; (2) globally cluster RDR+BAF jointly across the genome and across cells; (3) infer allele-specific copy numbers per cluster; (4) phase to haplotype-specific copy numbers using an evolutionary model; (5) cluster cells into tumor clones and reconstruct phylogeny.

Applied to 10 datasets of ~2,000 cells each from two breast-cancer patients, CHISEL identified extensive allele-specific aberrations: copy-neutral LOH, whole-genome doublings (WGDs), and **mirrored-subclonal CNAs** (the same total copy number but on opposite haplotypes in different clones — evidence of parallel/convergent evolution).

## Why this matters

CHISEL filled a fundamental gap: ultra-low-coverage barcode-based scDNA platforms (10x CNV Solution, Mission Bio Tapestri DNA, DLP+) produce coverage that breaks standard allele-specific CNV callers. CHISEL is the workhorse for tumor-evolution studies at scale (1000s of cells per patient). Anchors §3.1 (allele-specific CNV from sparse scDNA), §4 (variant-calling tool family for CNVs), and §5 (cancer biology — clonal evolution, WGD timing, convergent evolution).

---
**Source:** [DOI](https://doi.org/10.1038/s41587-020-0661-6) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32879467/)

## Related

- [[10-Summaries/laks-2019-cell]]
- [[10-Summaries/kim-2018-nature]]
- [[10-Summaries/kaufmann-2022-medicc2]]
- [[30-Concepts/copy-number-variation]]
