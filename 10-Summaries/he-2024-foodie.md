---
type: summary
title: "He 2024 — FOODIE: genome-wide single-cell/single-molecule footprinting of TFs with deaminase"
aliases: ["He 2024 FOODIE", "FOODIE"]
tags: [FOODIE, single-molecule-footprinting, deaminase, DddB, single-cell-genomics, TF-binding, cooperativity, Xie-lab, Peking]
created: 2026-05-13
updated: 2026-05-13
sources: ["Runsheng_2024_PNAS.pdf"]
---

**Citation:** He et al. (2024) — *FOODIE: genome-wide single-cell/single-molecule footprinting of TFs with deaminase* — *PNAS*. [DOI](https://doi.org/10.1073/pnas.2423270121)

He, Dong, Wang, Xie et al. (Xie lab; Peking University) developed **FOODIE** (FOOtprinting with DeaminasE), a single-molecule/single-cell TF footprinting method using **DddB**, a double-stranded DNA cytosine deaminase that converts cytosine to uracil in accessible (unbound) regions while bound regions are protected. Unlike DddA (which acts only on cytosine preceded by thymine, limiting motif coverage), DddB has broad sequence compatibility. Workflow: Tn5 tagmentation of open chromatin → in-situ DddB deamination → amplification → sequencing where C→T conversion ratio reveals binding footprints. FOODIE achieves near-single-base resolution, requires fewer cells than ChIP-seq/DNase-seq, and detects TF binding cooperativity (positive or negative) between adjacent TFs from individual fibers. Single-cell FOODIE enables cell-type-specific TF footprint detection in heterogeneous tissue (e.g., brain). The authors built a scalable FOODIE database across cell lines.

## Why this matters

Independent contemporary of DAF-seq (Swanson 2025) — both use dsDNA deaminases for chromatin footprinting, but FOODIE focuses on TF-resolution mapping while DAF-seq emphasizes haplotype-resolved chromatin fiber architecture. Anchors §3.3 (SMF — deaminase generation) alongside DAF-seq, SAMOSA, Fiber-seq, nanoNOMe. The brain application directly supports §5 mosaicism arguments — different cell types in heterogeneous tissue have distinct TF footprints. Existing bibkey `he2024foodie` may need to be added.

---
**Source:** [DOI](https://doi.org/10.1073/pnas.2423270121) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/39689177/)

---
**Source:** [DOI](https://doi.org/10.1073/pnas.2423270121) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/39689177/)

## Related

- [[10-Summaries/swanson-2025-daf-seq]]
- [[10-Summaries/doughty-2024-smf-tf]]
- [[10-Summaries/altemose-2022-dimelo-seq]]
- [[10-Summaries/peter-2024-brain-fiberseq]]
- [[30-Concepts/single-molecule-footprinting]]
