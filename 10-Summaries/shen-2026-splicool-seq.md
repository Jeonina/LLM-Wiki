---
type: summary
title: "Shen et al. 2026 — SpliCOOL-seq: scalable single-cell methylation + accessibility via split-pool barcoding"
source: "[[00-Sources/papers/High‐throughput single‐cell DNA methylation and chromatin accessibility co‐profiling with SpliCOOL‐seq]]"
source_kind: paper
author: "Qingmei Shen, Enze Deng, Ling Luo, Jingna Zhang, Qifeng Yang, Dan Su, Xiaoying Fan (corresponding)"
published: 2026-04-01
ingested: 2026-05-12
doi: "10.1002/ctm2.70584"
journal: "Clinical and Translational Medicine"
tags: [DNA-methylation, chromatin-accessibility, single-cell, multiomics, LUAD, split-pool, Tn5, GpC-methylation]
entities:
  - "[[20-Entities/xiaoying-fan]]"
  - "qingmei shen"
concepts:
  - "[[30-Concepts/splicool-seq]]"
  - "[[30-Concepts/nome-seq]]"
  - "[[30-Concepts/combinatorial-indexing]]"
  - "[[30-Concepts/dna-methylation]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/lung-adenocarcinoma]]"
  - "[[30-Concepts/epigenetic-aging]]"
topics:
  - "[[40-Topics/dna-methylation]]"
  - "[[40-Topics/single-cell-multiomics]]"
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Shen et al. (2026) — *SpliCOOL-seq: scalable single-cell methylation + accessibility via split-pool barcoding* — *Clinical and Translational Medicine*. [DOI](https://doi.org/10.1002/ctm2.70584)

# Shen et al. 2026 — SpliCOOL-seq

> Thesis: Existing single-cell joint methylation + chromatin-accessibility methods (scCOOL-seq, scNOMe-seq, scNMT-seq, iscCOOL-seq, snmCAT-seq, scNOMeRe-seq) are stuck at the cell-lysate scale of hundreds of cells per experiment. sciMETv3 hit the next step but used cell-indexed Tn5 with fragmentation variability between cells. SpliCOOL-seq combines (a) in-situ GpC methylation as the accessibility readout, (b) **universal (unindexed) Tn5 tagmentation** for uniform fragmentation across cells, and (c) split-pool ligation-based combinatorial barcoding — yielding thousands of cells per experiment with both whole-genome WCG (endogenous) methylation and GCH (nucleosome-depletion region, NDR) accessibility.

## Key claims

- **Two-round split-pool barcoding** via T4 ligase after universal Tn5 tagmentation. Bisulfite conversion follows barcoding. Yields cells × WCG/GCH matrix.
- Distinguishes lung-cancer cell types (GM12878, NIH/3T3, A549, NCI-H460, SK-MES) by integrated WCG + GCH + NDR signal.
- **Decitabine vs 5-azacytidine** both cause large-scale demethylation, but in **divergent patterns** detectable only with this scale of single-cell joint readout. This contradicts the assumption that HMAs are interchangeable.
- Applied to primary LUAD tissue: identifies tumor subclones within a single lesion, discovers methylation biomarkers (FAM124B, SFN, OR7E47P) associated with patient survival. Functional follow-up: CRISPR knockout of SFN reduces A549/H460 proliferation and increases apoptosis.
- Tumor subclones show **accelerated epigenetic aging** and elevated mitotic activity — links epigenetic aging clocks to cancer progression.

## Methods / evidence

In-situ GpC methyltransferase (M.CviPI) marks accessible regions. Formaldehyde fixation. Nucleosome depletion by mild SDS. Universal-adapter Tn5 tagmentation. T4 DNA ligase two-round barcoding (~20k nuclei per first-round well; ~12 cells/well in second round). Bisulfite conversion + Klenow random priming. Library prep on SURFSeq 5000. Companion scATAC-seq on 10X for cross-comparison. scAge framework + 450k TCGA-LUAD reference for epigenetic-aging analysis. MethSCAn for DMRs.

## Surprising or load-bearing bits

- **Universal Tn5** is the methodological key: by removing per-cell Tn5 barcoding, fragmentation variability is eliminated and almost all data can serve the GCH (accessibility) module simultaneously with WCG (methylation). This addresses the main limitation of sciMETv2/v3.
- The two-DNMT-inhibitor divergent-demethylation finding is therapeutically consequential. It implies azacitidine and decitabine could produce different clinical responses through different epigenetic effects, even though both are nominally "hypomethylating agents."
- The epigenetic-aging-as-tumor-marker framing fits a broader thread: methylation is a clock and a state.

## Connections to other sources

- Direct lineage from scCOOL-seq (Guo et al.) and scNMT-seq (Clark et al.); cites these as precursors.
- Builds on universal-Tn5 logic that also appears in [[10-Summaries/swanson-2025-daf-seq]] (DAF-seq) — though there it's chemical (deaminase) rather than enzymatic.
- Complements [[10-Summaries/bai-2024-simple-seq]] (SIMPLE-seq does 5mC+5hmC at base resolution; SpliCOOL-seq does 5mC+accessibility at higher throughput).
- The "viral mimicry"/HMA framing connects to [[10-Summaries/hunt-2022-sctem-seq]] (scTEM-seq + decitabine in AML).

## Open questions

- The two-HMA divergence: what is the mechanistic basis? Authors propose chromatin-context differences but don't define them.
- Generalization beyond LUAD; primary samples are tumor-only — no matched paired normal.

---
**Source:** [DOI](https://doi.org/10.1002/ctm2.70584)
## Related

- [[40-Topics/dna-methylation]] · [[40-Topics/single-cell-multiomics]] · [[30-Concepts/nome-seq]] · [[30-Concepts/combinatorial-indexing]] · [[30-Concepts/epigenetic-aging]]
