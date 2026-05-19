---
type: summary
title: "Lee 2020 — Simultaneous profiling of chromatin accessibility and methylation on human cell lines with nanopore sequencing (nanoNOMe)"
source: "[[00-Sources/papers/Simultaneous profiling of chromatin accessibility and methylation on human cell lines with nanopore sequencing]]"
aliases: ["Lee 2020 nanoNOMe", "nanoNOMe", "long-read NOMe"]
tags: [nanoNOMe, nanopore, methylation, accessibility, long-read, joint-assay, Timp-lab, JHU, breast-cancer]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Lee et al. (2020) — *Simultaneous profiling of chromatin accessibility and methylation on human cell lines with nanopore sequencing (nanoNOMe)* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-020-01000-7)

Lee, Razaghi, Gilpatrick, Molnar, Gershman, Sadowski, Sedlazeck, Hansen, Simpson and Timp (Johns Hopkins / OICR) developed **nanoNOMe**, which adapts NOMe-seq (M.CviPI GpC labeling of open chromatin) to **Oxford Nanopore** long-read sequencing. Unlike bisulfite-NOMe-seq, nanoNOMe directly reads m5C modifications at both CpG (endogenous) and GpC (exogenous accessibility marker) positions on native, unfragmented DNA — preserving long-range linkage information across >10 kb reads.

Applied to four cell lines (GM12878, MCF-10A, MCF-7, MDA-MB-231) at 103× coverage. ROC AUC 0.908 for CpG and 0.984 for GpC methylation calling (LLR-based). Long reads enable: (i) per-molecule footprinting of protein binding and nucleosomes; (ii) **haplotype-resolved phased epigenomes** — chromosome-level allele-specific profiles of both methylation and accessibility, including repetitive regions and structural variants unreachable by short reads; (iii) cancer-vs-normal differential methylation and accessibility at single-molecule resolution.

## Why this matters

nanoNOMe sits in the long-read joint-assay family alongside SMAC-seq (Shipony 2020, bulk Nanopore), SAMOSA (Abdulhay 2020, PacBio), Fiber-seq (Stergachis 2020, bulk PacBio), and HiDef-seq (Liu 2024, duplex). The unique contribution: **phased epigenome** at chromosome scale on standard human cell lines including cancer models. Anchors §3.3 (joint methylome + accessibility) and §3.2 (single-molecule footprinting), and supports our review's argument that long-read joint assays are the practical path to phased multi-layer locus-state observation in single molecules (though not yet in single cells at scale).

---
**Source:** [DOI](https://doi.org/10.1038/s41592-020-01000-7) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33230324/)

---
**Source:** [DOI](https://doi.org/10.1038/s41592-020-01000-7) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33230324/)

## Related

- [[10-Summaries/shipony-2020-smac]]
- [[10-Summaries/andrewb-2020-science]]
- [[10-Summaries/clark-2018-scnmt]]
- [[30-Concepts/joint-methylome-assays]]
