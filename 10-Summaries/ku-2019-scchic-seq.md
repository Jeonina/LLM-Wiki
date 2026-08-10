---
type: summary
title: "Ku et al. 2019 — scChIC-seq: antibody-MNase-fusion for single-cell histone marks"
source: "[[00-Sources/papers/Single-cell chromatin immunocleavage sequencing (scChIC-seq) to profile histone modification]]"
source_kind: paper
author: "Wai Lim Ku, Kosuke Nakamura, Weiwu Gao, Kairong Cui, Gangqing Hu, Qingsong Tang, Bing Ni, Keji Zhao (corresponding)"
published: 2019-03-28
ingested: 2026-05-12
doi: "10.1038/s41592-019-0361-7"
journal: "Nature Methods"
tags: [histone-modifications, single-cell, MNase, ChIC, H3K4me3, H3K27me3, white-blood-cells, Zhao-lab]
entities:
  - "[[20-Entities/keji-zhao]]"
  - "wai lim ku"
concepts:
  - "[[30-Concepts/scchic-seq]]"
  - "[[30-Concepts/chic-seq]]"
  - "[[30-Concepts/cut-and-run]]"
  - "[[40-Topics/histone-modifications]]"
  - "mnase"
topics:
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Ku et al. (2019) — *scChIC-seq: antibody-MNase-fusion for single-cell histone marks* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-019-0361-7)

# Ku et al. 2019 — scChIC-seq

> Thesis: ChIP-seq is not single-cell-tractable because of cross-linking, sonication, and immunoprecipitation losses. Schmid et al.'s original ChIC method (chromatin immunocleavage) used antibody-tethered MNase to cut at target sites without ChIP. **scChIC-seq** adapts ChIC for single cells using a covalent antibody-MNase conjugate (or protein-A-MNase + antibody complex) plus selective PCR amplification of the small target fragments, profiling H3K4me3 and H3K27me3 in ~285 single human white blood cells per experiment and clustering them by chromatin state into the major immune lineages.

## Key claims

- **Method**: covalent antibody-MNase (or pA-MNase) recruited to histone-mark sites, MNase cleaves locally. **Both target and non-target fragments are recovered and ligated to adaptors**, then size-selective PCR preferentially amplifies the smaller target fragments. Compared to CUT&RUN, scChIC supports formaldehyde-fixed cells and either covalent or pA-MNase strategies.
- **Bulk validation**: H3K4me3 ChIC reads in 100–3,000 NIH 3T3 cells correlate with bulk ChIP-seq at r=0.9; 80–85% peak overlap. Enriched around TSSs as expected.
- **Single-cell H3K4me3 on WBCs**: ~285 cells × ~100,000 unique reads/cell. 24,819 pooled peaks; 61% overlap with bulk H3K4me3. Per-cell sensitivity ~10% (top 10% of cells reach 18%) — i.e., ~5,000 peaks called per cell.
- **Single-cell H3K27me3 on WBCs**: 106 cells × ~131,000 reads/cell. 21,465 pooled peaks; 50% overlap with bulk; 9.5% per-cell sensitivity.
- **Clustering**: SC3 clustering on 242 informative H3K4me3 cells yields 7 clusters, 5 with significant marker peaks → identified as monocytes (15), B cells (12), T cells (41), NK cells (43). Genome-browser tracks at marker genes confirm cell-type-specific H3K4me3 patterns.
- Variable and co-methylated H3K4me3 peaks correlate with gene expression covariance → cell-to-cell heterogeneity in H3K4me3 predicts heterogeneity in expression.

## Methods / evidence

NIH 3T3, mESC, naive CD4 T cells for bulk validation. Single-cell sorting + MNase digestion + Proteinase K + adaptor ligation + selective PCR amplification (small target fragments) + gel-based size selection. SC3 clustering for cell-type assignment. Bulk ChIP-seq from ENCODE WBC and prior literature as reference.

## Surprising or load-bearing bits

- The **selective-PCR amplification of small fragments** is the key insight: target sites have shorter ChIC fragments because cuts are concentrated; non-target sites give longer/random fragments. PCR conditions selectively amplify the short window, enriching signal-to-noise without the need for fragment isolation in solution (the CUT&RUN strategy).
- One of the first methods to demonstrate that **histone-modification ChIP-style readout can be done at single-cell scale** — opens the door to scChIC-seq, sortChIC, scCUT&Tag, sciCUT&Tag, scChIX-seq, MulTI-Tag, etc.

## Connections to other sources

- Direct ancestor of [[10-Summaries/yeung-2023-scchix-seq]] (scChIX-seq, also based on MNase/sortChIC) and [[10-Summaries/geisenberger-2025-scepi2-seq]] (scEpi²-seq, also sortChIC-based).
- Methodological alternative to CUT&RUN and the Tn5-based scCUT&Tag family ([[10-Summaries/janssens-2023-scicut-tag]]).
- WBC clustering by H3K4me3 alone parallels the µATAC-seq PBMC result ([[10-Summaries/mezger-2018-microfluidic-atac]]): different epigenetic modalities recover the same immune-cell lineage structure.

## Open questions

- Throughput limit (~285 cells/run). Newer methods (sciCUT&Tag) push this to ~40,000 cells/chip.
- Two histone marks per run, not multiplexed within a cell. scChIX-seq later solves this with computational deconvolution.

---
**Source:** [DOI](https://doi.org/10.1038/s41592-019-0361-7)
## Related

- [[40-Topics/histone-modifications]] · [[30-Concepts/scchic-seq]] · [[30-Concepts/chic-seq]] · [[20-Entities/keji-zhao]]
