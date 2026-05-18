---
type: summary
title: "Chen et al. 2017 — LIANTI: Linear Amplification via Transposon Insertion for single-cell WGA"
source: "[[00-Sources/papers/Single-cell whole-genome analyses by Linear Amplification via Transposon Insertion (LIANTI)]]"
source_kind: paper
author: "Chongyi Chen, Dong Xing, Longzhi Tan, Heng Li, Guangyu Zhou, Lei Huang, X. Sunney Xie (corresponding)"
published: 2017-04-15
ingested: 2026-05-18
ingest_depth: abstract+intro
doi: "10.1126/science.aak9787"
journal: "Science"
tags: [LIANTI, scWGA, Tn5-transposition, linear-amplification, T7-IVT, Xie-lab, CNV-resolution, SNV-fidelity]
entities: []
concepts:
  - "[[30-Concepts/scwga]]"
  - "[[30-Concepts/tn5-tagmentation]]"
topics:
  - "[[40-Topics/whole-genome-amplification]]"
---

**Citation:** Chen et al. (2017) — *LIANTI: Linear Amplification via Transposon Insertion for single-cell WGA* — *Science*. [DOI](https://doi.org/10.1126/science.aak9787)

# Chen et al. 2017 — LIANTI

> Thesis: existing scWGA methods (MDA, MALBAC, PCR-based) suffer from low CNV resolution and low SNV fidelity due to exponential amplification bias. LIANTI replaces exponential amplification with **linear amplification driven by T7 in vitro transcription** initiated from Tn5-inserted T7-promoter-carrying transposons. The result is unbiased copy-number profiling at kilobase resolution and high-fidelity SNV detection.

## Key claims (abstract + intro)

- **Chemistry**: a Tn5 transposome carrying a **T7 promoter** randomly fragments single-cell genomic DNA. Each fragment then becomes a linear-amplification template via T7 RNA polymerase. Amplified RNA is reverse-transcribed and sequenced.
- **Linear, not exponential**: amplification bias scales logarithmically rather than exponentially → uniform genomic coverage → CNV resolution to ~10–20 kb (vs ~1 Mb for prior methods).
- **High SNV fidelity**: error rate competitive with MDA's φ29-based fidelity (~10⁻⁶/base), but with the coverage uniformity of MALBAC.
- **Validated by detecting UV-induced SNV spectrum** in a single human cell after UV irradiation.

## Why this matters

LIANTI is one of the three foundational scWGA chemistries (alongside MDA and MALBAC) and the **template for later linear-amplification methods** including PTA. The transposon-based fragmentation lineage feeds into Tn5-based methods more broadly (ATAC-seq, sci-ATAC). Anchors the scWGA branch as the "linear amplification" choice in the trichotomy.

## Note on ingest depth

Abstract + intro only; PDF re-ingest will deepen the comparison vs MDA/MALBAC (Figs 2–4 quantitative metrics).

---
**Source:** [DOI](https://doi.org/10.1126/science.aak9787) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/28408603/)

## Related

- [[30-Concepts/scwga]] · [[30-Concepts/tn5-tagmentation]] · [[30-Concepts/pta]] · [[30-Concepts/dean-2002-mda|mda]]
- [[10-Summaries/dean-2002-mda]]
- [[40-Topics/whole-genome-amplification]]
