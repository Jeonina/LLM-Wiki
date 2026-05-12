---
type: summary
title: "Jiang et al. 2026 — STARK + scNucleome: unified pipeline and atlas for sc3DG-seq"
source: "[[00-Sources/papers/Harmonizing single-cell 3D genome data with STARK and scNucleome]]"
source_kind: paper
author: "Wen-Jie Jiang, KangWen Cai, YuanChen Sun, An Liu, HanWen Zhu, RuiXiang Gao, Chunge Zhong, Nana Wei, Futing Lai, Teng Fei, Yu-Juan Wang, Xiaoqi Zheng, Ming Xu, Hua-Jun Wu (corresponding)"
published: 2026-01-21
ingested: 2026-05-12
doi: "10.1186/s13059-026-03938-x"
journal: "Genome Biology"
tags: [3D-genome, single-cell-HiC, software, benchmarking, EmptyCells, SSCE, atlas]
entities:
  - "[[20-Entities/hua-jun-wu]]"
  - "[[20-Entities/wen-jie-jiang]]"
concepts:
  - "[[30-Concepts/stark]]"
  - "[[30-Concepts/single-cell-hi-c]]"
  - "[[30-Concepts/3d-genome]]"
  - "[[30-Concepts/sscce]]"
  - "[[30-Concepts/empty-cells-algorithm]]"
  - "[[30-Concepts/topologically-associating-domain]]"
topics:
  - "[[40-Topics/3d-genome]]"
  - "[[40-Topics/chromatin-architecture]]"
---

# Jiang et al. 2026 — STARK + scNucleome

> Thesis: 15+ sc3DG-seq technologies exist (scHi-C, snHi-C, sciHi-C, Dip-C, sn-m3C, HiRES, scSPRITE, scNanoHi-C, Droplet/Paired Hi-C, GAGE-seq, LiMCA, …), each with its own data format and idiosyncratic processing. No unified analysis framework exists. **STARK** (Structural Topology Analysis and Rich Knowledge base) provides standardized preprocessing, quality control, and downstream analysis for all sc3DG-seq data types. STARK is paired with **scNucleome**, a publicly accessible repository of uniformly processed sc3DG-seq datasets — the "single-cell 3D genome atlas."

## Key claims

- **STARK framework** with three modules: (1) Preprocess (sequencing QC, alignment, demultiplexing, .cool file generation, Hi-C correction); (2) Cell QC (EmptyCells algorithm filters by contact count + Monte Carlo simulation; metrics include GiniQC, short-/mid-/long-range contact rates, and the novel **Spatial Structure Capture Efficiency / SSCE**); (3) Downstream Analysis (imputation, clustering, aggregation, A/B compartments, TADs, loops, 3D structure reconstruction).
- **EmptyCells** algorithm: distinguishes real cells from empty barcodes in high-throughput sc3DG-seq. Critical step missing from prior tools — analogous to EmptyDrops in scRNA-seq.
- **SSCE metric**: integrates multiple topological features (TAD recovery, compartment recovery, loop signal) to quantify each single cell's structural-information capture. Complements simple contact-count metrics — rescues cells with few contacts but informative structural patterns.
- **Cross-platform benchmark**: 15 technologies compared on read-level efficiency, library complexity, genome coverage, GiniQC. **scSPRITE** has highest average contacts per cell (sonication-based capture preserves spatial clusters); **snHi-C** has second-highest, leveraging whole-genome amplification. Tradeoffs in cells/experiment vs contacts/cell are quantified.
- Built-in computational optimizations: parallel processing, Monte Carlo acceleration.

## Methods / evidence

Comprehensive benchmark on published sc3DG-seq datasets (Table 1 enumerates the 15 technologies). EmptyCells uses Monte Carlo simulation against an empty-barcode null. SSCE combines TAD, compartment, and loop scores into a unified structural metric.

## Surprising or load-bearing bits

- **scSPRITE captures more contacts per cell than any ligation-based method** because sonication preserves entire spatial clusters of chromatin (rather than pairs of ligated fragments). This is a genuine throughput advantage and points to a future direction beyond ligation-based 3C variants.
- The introduction of **SSCE** as a structural-quality metric solves a real measurement problem: cells with few contacts can still be informative if those contacts span TAD boundaries or loop anchors. Contact-count alone biases toward shallow data.
- scNucleome positions itself as the "scTL atlas" of 3D-genome data — analogous to TabulaSapiens for transcriptomics. Publicly accessible uniformly processed data accelerates future cross-study work.

## Connections to other sources

- Operationalizes the conceptual framework laid out in [[10-Summaries/navigating-the-3d-genome-at-single-cell-resolution-techniques-computation-and-mechanistic-landscapes]] (Hong/Dao 2025 review).
- Multi-omics methods like sn-m3C-seq (Hi-C + methylation) and HiRES (Hi-C + RNA) are processed by STARK, sitting at the intersection with [[40-Topics/dna-methylation]] and [[40-Topics/single-cell-multiomics]].
- Independent of but conceptually parallel to the [[10-Summaries/episcanpy-integrated-single-cell-epigenomic-analysis]] (EpiScanpy) approach for scATAC-seq / scBS-seq harmonization — both are "unified pipeline + atlas" responses to method fragmentation.

## Open questions

- Long-read sc3DG methods (scNanoHi-C) are processed in STARK but not deeply benchmarked; the long-read advantage is most visible in higher-order contacts that ligation methods miss.
- 3D structure reconstruction from sparse data remains hard; STARK supports it but the result quality depends heavily on imputation choices.

## Related

- [[40-Topics/3d-genome]] · [[30-Concepts/stark]] · [[30-Concepts/empty-cells-algorithm]] · [[30-Concepts/sscce]]
