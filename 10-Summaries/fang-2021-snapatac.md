---
type: summary
title: "Fang et al. 2021 — SnapATAC: peak-free scATAC-seq analysis to 1 M cells"
source: "[[00-Sources/papers/Comprehensive analysis of single cell ATAC-seq data with SnapATAC]]"
source_kind: paper
author: "Rongxin Fang, Sebastian Preissl, ... Joseph R. Ecker, Bing Ren (corresponding)"
published: 2021-02-26
ingested: 2026-05-12
doi: "10.1038/s41467-021-21583-9"
journal: "Nature Communications"
tags: [scATAC-seq, Ren-lab, Nyström-method, mouse-brain, MOp, peak-free, cellular-heterogeneity]
entities:
  - "[[20-Entities/bing-ren]]"
  - "[[20-Entities/rongxin-fang]]"
  - "[[20-Entities/sebastian-preissl]]"
  - "[[20-Entities/joseph-ecker]]"
concepts:
  - "[[30-Concepts/snapatac]]"
  - "[[30-Concepts/scatac-seq]]"
  - "[[30-Concepts/jaccard-similarity]]"
  - "[[30-Concepts/nystrom-method]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/cis-regulatory-element]]"
topics:
  - "[[40-Topics/single-cell-atac-seq]]"
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Fang et al. (2021) — *SnapATAC: peak-free scATAC-seq analysis to 1 M cells* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-021-21583-9)

# Fang et al. 2021 — SnapATAC

> Thesis: scATAC-seq analysis pipelines that depend on pre-defined accessibility peaks bias clustering toward abundant cell types and miss rare populations whose signal is too sparse to define peaks. **SnapATAC** discards peaks entirely and instead bins the genome into uniform 5 kb windows, computes pairwise Jaccard similarities between cells, and uses the ensemble **Nyström method** to scale low-rank embedding to a million cells. Applied to 55,592 nuclei from mouse secondary motor cortex (MOp), it discovers ~370,000 candidate cis-regulatory elements across 31 cell populations including subpopulations that constitute <0.1% of cells.

## Key claims

- **Peak-free representation**: 5 kb bins → binary vectors → Jaccard similarity → regression-normalized for sequencing depth → eigenvector decomposition for dimensionality reduction. No peak-calling step before clustering.
- **Ensemble Nyström method**: compute embedding on a sampled subset of "landmark" cells, project remaining cells to that embedding. Reduces complexity from O(n²) to scalable in n. Multiple sampling rounds combined via consensus improve reproducibility.
- **Benchmark**: outperforms LSA and cisTopic on simulated and real scATAC-seq for accuracy (ARI, NMI), sensitivity, scalability, and reproducibility (Wilcoxon p < 0.01 across coverage levels).
- **Off-peak reads contribute signal**: removing reads outside pre-defined peaks degrades clustering. Off-peak reads correlate with Hi-C compartment-A density — they carry euchromatin signal that distinguishes cell types.
- **Mouse MOp application**: 31 cell populations, ~370k cREs, identification of rare neuronal subtypes (Sst, Vip, L6b, L6.CT) that alternative methods (LSA, cisTopic) miss.
- Incorporates Harmony for batch correction, integration with scRNA-seq via Seurat, Cicero-style enhancer-target gene linking via logistic regression on imputed scRNA-seq.

## Methods / evidence

Snap file format for storing single-cell accessibility. SnapTools for preprocessing (alignment, deduplication, barcode filtering). 5 kb bin size chosen by systematic benchmarking. Comparators: LSA, cisTopic. Datasets: simulated downsampled bulk ATAC-seq from 10 cell types; ~1,400 C1-Fluidigm cells (10 cell types); 4,792 PBMCs; ~80k mouse atlas cells; 9,529 mouse MOp cells; simulated 1 M cells.

## Surprising or load-bearing bits

- **Reads outside peaks are signal, not noise** — the field's standard practice of restricting to peak windows discards useful information. SnapATAC challenges this norm with quantitative evidence: off-peak signal aligns with Hi-C compartment A.
- The Nyström approximation argument scales the method to a million cells on standard hardware — making atlas-scale scATAC-seq tractable.
- Rare-cell-type discovery (<0.1%) is the headline application: in mouse MOp, certain interneuron subtypes are detectable only by SnapATAC's bin-level signal, not peak-level.

## Connections to other sources

- Compared head-to-head with [[10-Summaries/bravo-2019-cistopic]] (cisTopic) and LSA — the "three major scATAC-seq methods" of 2018–2021.
- Inherited and extended by snapATAC2 (Python, Rust backend), which is cited and used in [[10-Summaries/shen-2026-splicool-seq]].
- Compatible with cell-type annotation pipelines from [[10-Summaries/danese-2021-episcanpy]] (EpiScanpy) and clustering frameworks from [[10-Summaries/schep-2017-chromvar]] (chromVAR).

## Open questions

- 5-kb bin choice is empirical. For highly specific cell types whose distinguishing accessibility is sub-1-kb, finer bins may be needed.
- The "off-peak signal" argument depends on the bin size; at very fine bin resolution most signal is sparse and the argument is weaker.

---
**Source:** [DOI](https://doi.org/10.1038/s41467-021-21583-9)
## Related

- [[40-Topics/single-cell-atac-seq]] · [[30-Concepts/snapatac]] · [[30-Concepts/jaccard-similarity]] · [[20-Entities/bing-ren]]
