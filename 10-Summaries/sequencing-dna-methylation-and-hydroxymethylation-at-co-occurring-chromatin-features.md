---
type: summary
title: "Tavares et al. 2026 — 6-base-CUT&Tag: 5mC + 5hmC at targeted histone marks"
source: "[[00-Sources/papers/Sequencing DNA methylation and hydroxymethylation at co-occurring chromatin features]]"
source_kind: paper
author: "Rafael de Cesaris Araujo Tavares, Somdutta Dhir, Xuan He, Jack Monahan, Minna Taipale, Paula Golder, Aldo Ciau-Uitz, Walraj Gosal, David Tannahill, Shankar Balasubramanian (corresponding)"
published: 2026-02-10
ingested: 2026-05-12
doi: "10.1038/s41467-026-69429-6"
journal: "Nature Communications"
tags: [CUT&Tag, 6-base-seq, 5mC, 5hmC, histone-modifications, enhancers, biomodal, mESCs]
entities:
  - "[[20-Entities/shankar-balasubramanian]]"
  - "[[20-Entities/rafael-tavares]]"
  - "[[20-Entities/biomodal]]"
concepts:
  - "[[30-Concepts/6-base-cut-and-tag]]"
  - "[[30-Concepts/cut-and-tag]]"
  - "[[30-Concepts/5hmc]]"
  - "[[30-Concepts/dna-methylation]]"
  - "[[30-Concepts/histone-modifications]]"
  - "[[30-Concepts/enhancer-states]]"
topics:
  - "[[40-Topics/histone-modifications]]"
  - "[[40-Topics/dna-methylation]]"
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Tavares et al. (2026) — *6-base-CUT&Tag: 5mC + 5hmC at targeted histone marks* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-026-69429-6)

# Tavares et al. 2026 — 6-base-CUT&Tag

> Thesis: We have plenty of methods for measuring DNA methylation and chromatin features separately, but we lack a single-fragment readout that reveals **which DNA modifications co-occur with which histone modifications**. 6-base-CUT&Tag (6B-C&T) couples antibody-directed Tn5 tagmentation with biomodal's 6-base enzymatic conversion to deliver simultaneous G/A/T/C/5mC/5hmC sequencing of the DNA fragments tethered to a specific histone mark. In mESCs, this reveals that H3K4me1-marked nucleosomes preferentially retain both 5mC and 5hmC at primed enhancers — a signature missed by all prior bulk methylation methods.

## Key claims

- **Method**: pA-Tn5 with a uracil-containing hairpin mosaic-end adapter (ME2U) → tagmentation in CUT&Tag style → USER-digestion → 6-base enzymatic conversion (biomodal evoC kit). Circular dumbbell-like fragments resist exonuclease cleanup; scar sequences in the read identify valid double-tagmented molecules.
- 98–99.5% sensitivity for 5mC/5hmC detection in spike-in controls. Replicate reproducibility Pearson r ≥ 0.97. Concordance with CUT&Tag (genomic enrichment, r ≥ 0.86) and with bulk CUT&Tag-BS (CpG modification levels, r ≥ 0.83 for H3K4me1 and H3K27me3).
- Profiled four histone marks in mESCs: H3K27ac, H3K4me3, H3K4me1, H3K27me3. **Active marks (H3K4me3/H3K27ac/H3K4me1) have lower methylation and higher 5hmC/5mC ratio than repressive (H3K27me3)** at the same loci — a pattern invisible in whole-genome 6-base sequencing.
- **The headline finding**: **H3K4me1 at primed enhancers** carries the highest 5mC (~13%) and 5hmC (~4%) of any enhancer state. H3K4me1 + 5mC/5hmC together is a robust signature for primed vs active vs poised enhancers — a machine-learning classifier on this single mark outperforms one trained on whole-genome data.

## Methods / evidence

E14TG2A mESCs serum/LIF. pA-Tn5-ME2U transposome, primary antibody targeting (H3K4me3, H3K4me1, H3K27ac, H3K27me3, IgG control). Exonuclease enrichment (T7 Exo + RecJf + Exo I) for circularized molecules. Biomodal duet evoC kit for 6-base conversion. NextSeq 2000 paired-end sequencing. Spike-in fiducials: 5mC-methylated lambda, 5hmC oligo, unmodified pUC19.

## Surprising or load-bearing bits

- Bisulfite-based methods couldn't access this question because (a) bisulfite degrades DNA from the few molecules CUT&Tag produces and (b) bisulfite conflates 5mC and 5hmC. 6B-C&T removes both constraints.
- The H3K4me1 + 5mC/5hmC signature **functionally distinguishes** active, primed, and poised enhancers — extending the well-known H3K4me1-marks-all-enhancers fact with a methylation-state coordinate.
- This is methodological dependence on a vendor kit (biomodal evoC), which is also used in [[10-Summaries/direct-transposition-of-native-dna-for-sensitive-multimodal-single-molecule-sequencing]]'s SMRT-Tag — biomodal's chemistry is the underlying engine.

## Connections to other sources

- Single-cell counterpart: [[10-Summaries/simultaneous-single-cell-analysis-of-5mc-and-5hmc-with-simple-seq]] (SIMPLE-seq) does whole-genome 5mC + 5hmC in single cells but cannot target a specific histone modification.
- Methodological lineage from CUT&Tag (Kaya-Okur 2019); single-cell CUT&Tag in [[10-Summaries/scalable-single-cell-profiling-of-chromatin-modifications-with-scicut-tag]] (sciCUT&Tag).
- Connects [[40-Topics/dna-methylation]] and [[40-Topics/histone-modifications]] in the way [[40-Topics/single-cell-multiomics]] connects multiple modalities at the cell level — but here at the **fragment level**.

## Open questions

- Single-cell extension is the natural next step but not yet demonstrated.
- Generalization to transcription factors (not just histone marks): could 6B-C&T-with-TF-antibody reveal methylation states of TF-bound DNA?

---
**Source:** [DOI](https://doi.org/10.1038/s41467-026-69429-6)
## Related

- [[40-Topics/histone-modifications]] · [[40-Topics/dna-methylation]] · [[30-Concepts/6-base-cut-and-tag]] · [[30-Concepts/cut-and-tag]] · [[20-Entities/biomodal]]
