---
type: summary
title: "Doughty 2024 — Single-molecule footprinting links TF binding to gene expression"
source: "[[00-Sources/papers/Single-molecule states link transcription factor binding to gene expression]]"
aliases: ["Doughty 2024 SMF", "TF-SMF"]
tags: [SMF, single-molecule-footprinting, TF-binding, enhancer-promoter, M.CviPI, Greenleaf-lab, Bintu-lab, Stanford]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/Single-molecule states link transcription factor binding to gene expression]]"
---

**Citation:** Doughty et al. (2024) — *Single-molecule footprinting links TF binding to gene expression* — *Nature*. [DOI](https://doi.org/10.1038/s41586-024-08219-w)

Doughty, Hinks, Schaepe et al. (Greenleaf, Bintu labs; Stanford) applied **single-molecule footprinting (SMF)** with M.CviPI GpC methyltransferase to engineered enhancer–promoter constructs in K562 cells, simultaneously measuring TF occupancy, nucleosome state, and gene expression on the same single chromatin fibers. The reporter system places 0–8 TetO sites upstream of a minCMV-citrine promoter; M.CviPI methylates accessible GpCs, enzymatic conversion reads accessibility per molecule. Analysis of 26,365,210 single molecules revealed substantial heterogeneity in TF/nucleosome configurations on identical sequences; the authors decomposed TF strength into binding and activation terms, showed that average TF occupancy linearly determines promoter activity, and built thermodynamic and kinetic models predicting both enhancer microstates and gene-expression dynamics from sequence alone.

## Why this matters

Anchors §3.3 (single-molecule footprinting — SMAC-seq/Fiber-seq/nanoNOMe/SAMOSA family) at the application end. While most SMF papers focus on assay development, Doughty 2024 demonstrates SMF's *causal* power: by perturbing TF concentration and motif number while reading single-molecule occupancy, the paper builds first-principles models linking sequence → chromatin state → expression. Important reference when arguing SMF is uniquely positioned to dissect cis-regulatory mechanism — a feature scATAC/scChIP cannot offer.

## Related

- [[10-Summaries/shipony-2020-smac]]
- [[10-Summaries/lee-2020-nanonome]]
- [[10-Summaries/peter-2024-brain-fiberseq]]
- [[10-Summaries/bohaczuk-2024-targeted-fiberseq]]
- [[30-Concepts/single-molecule-footprinting]]

---
**Source:** [DOI](https://doi.org/10.1038/s41586-024-08219-w) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/39567683/)
