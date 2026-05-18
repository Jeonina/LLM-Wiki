---
type: summary
title: "Schep et al. 2017 — chromVAR: TF motif accessibility from sparse single-cell data"
source: "[[00-Sources/papers/chromVAR_ inferring transcription-factor-associated accessibility from single-cell epigenomic data]]"
source_kind: paper
author: "Alicia N. Schep, Beijing Wu, Jason D. Buenrostro, William J. Greenleaf (corresponding)"
published: 2017-08-21
ingested: 2026-05-12
doi: "10.1038/nmeth.4401"
journal: "Nature Methods"
tags: [scATAC-seq, transcription-factors, motif-enrichment, Greenleaf-lab, hematopoiesis, AML]
entities:
  - "[[20-Entities/william-greenleaf]]"
  - "[[20-Entities/alicia-schep]]"
  - "[[20-Entities/jason-buenrostro]]"
concepts:
  - "[[30-Concepts/chromvar]]"
  - "[[30-Concepts/transcription-factor-motif]]"
  - "[[30-Concepts/scatac-seq]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/de-novo-motif-discovery]]"
topics:
  - "[[40-Topics/single-cell-atac-seq]]"
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Schep et al. (2017) — *chromVAR: TF motif accessibility from sparse single-cell data* — *Nature Methods*. [DOI](https://doi.org/10.1038/nmeth.4401)

# Schep et al. 2017 — chromVAR

> Thesis: scATAC-seq has fundamental sparsity — only 0, 1, or 2 reads per locus per cell because a diploid genome only has two copies. Per-locus analysis is therefore noise-dominated. **chromVAR aggregates accessibility across all peaks sharing a TF motif** (or any genomic annotation) and computes a bias-corrected deviation score per cell — controlling for GC content and mean accessibility — turning sparse single-cell data into a robust TF-motif × cell matrix that supports clustering, trajectory analysis, and de novo motif discovery.

## Key claims

- **Bias-corrected deviation**: for each motif and cell, compute (observed fragments in peaks containing motif − expected fragments) / expected. Then subtract the mean deviation from GC-content-matched and accessibility-matched background peak sets. Divide by background SD to get a *z*-score.
- **Robust at 10,000 fragments per cell** (typical scATAC yield): clustering accuracy matches deep bulk and outperforms PCA/peak-based approaches.
- Identifies known master regulators of hematopoiesis (HOXA9, SPI1/PU.1, TBX21, GATA1) and reconstructs major hematopoietic lineages in tSNE space.
- AML application: leukemic stem cells from two patient samples cluster between LMPPs and monocytes; AML blasts cluster with monocytes. SPI1 and CEBPA motifs distinguish stem-like vs differentiated AML — clinical-relevance demonstration.
- **k-mer-based de novo motif discovery**: use covariance between highly variable seed k-mers and their single-mismatch neighbors to construct position-weight matrices. Identifies motifs without prior annotation.
- TF footprint analysis on de novo motifs reveals atypical footprints (>20 bp) suggesting larger regulatory complexes than canonical single-TF binding.

## Methods / evidence

R package (github.com/GreenleafLab/chromVAR). cisBP database of human and mouse PWMs as default motif set. User-extensible to k-mers, ChIP-seq peaks, GWAS annotations. Validated by downsampling bulk hematopoiesis ATAC-seq (Buenrostro 2018) and on scATAC-seq from C1 Fluidigm.

## Surprising or load-bearing bits

- The **aggregate-over-shared-motif** trick is the methodological insight: sparsity at the per-peak level is fundamental and irreducible, but motifs share regulatory logic across thousands of peaks, so aggregation pulls signal out of noise.
- The **GC-content + mean-accessibility background matching** is the rigor that distinguishes chromVAR from naive motif-enrichment tools — without it, GC-biased PCR or Tn5 conditions would dominate the signal.
- chromVAR is **complementary, not competitive, with cell-clustering tools** like cisTopic and SnapATAC: it provides the TF interpretation layer on top of any clustering.

## Connections to other sources

- Widely used downstream of [[10-Summaries/cistopic-cis-regulatory-topic-modeling-on-single-cell-atac-seq-data]] (cisTopic), [[10-Summaries/comprehensive-analysis-of-single-cell-atac-seq-data-with-snapatac]] (SnapATAC), and [[10-Summaries/episcanpy-integrated-single-cell-epigenomic-analysis]] (EpiScanpy) for TF-motif interpretation.
- Used in [[10-Summaries/unsupervised-clustering-and-epigenetic-classification-of-single-cells]] (scABC) to assign TF activity to discovered clusters.
- Also used in [[10-Summaries/simultaneous-single-cell-analysis-of-5mc-and-5hmc-with-simple-seq]] (SIMPLE-seq) for motif analysis of methylation-state regions.
- Limitation noted by cisTopic: chromVAR averages motif effects across the dataset and cannot resolve the same motif's distinct usage at different developmental stages (e.g., GATA in HSC vs MEP).

## Open questions

- The within-cell aggregation can mask **co-binding** signals: chromVAR cannot directly resolve TF cooperativity from single-cell data, only motif-level activity.
- Cannot distinguish TFs sharing a motif (e.g., GATA1 vs GATA2). Integration with scRNA-seq for TF expression is the workaround.

---
**Source:** [DOI](https://doi.org/10.1038/nmeth.4401)
## Related

- [[40-Topics/single-cell-atac-seq]] · [[30-Concepts/chromvar]] · [[30-Concepts/transcription-factor-motif]] · [[20-Entities/william-greenleaf]]
