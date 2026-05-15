---
type: summary
title: "Pott 2017 — Simultaneous measurement of chromatin accessibility, DNA methylation and nucleosome phasing in single cells (scNOMe-seq)"
aliases: ["scNOMe-seq", "Pott 2017"]
tags: [scNOMe-seq, methylation, accessibility, nucleosome, joint-assay, NOMe-seq]
created: 2026-05-13
updated: 2026-05-13
sources: ["Sebastian_2017_eLife.pdf"]
---

**Citation:** Pott et al. (2017) — *Simultaneous measurement of chromatin accessibility, DNA methylation and nucleosome phasing in single cells (scNOMe-seq)* — *eLife*. [DOI](https://doi.org/10.7554/eLife.23203)

Pott adapted the bulk Nucleosome Occupancy and Methylome (NOMe)-seq method to single cells, demonstrating that a single bisulfite-sequencing experiment can read three layers of chromatin state from individual cells: chromatin accessibility (via exogenous GpC methylation footprinting), endogenous CpG methylation, and nucleosome phasing.

The chemistry: nuclei are treated with M.CviPI, a GpC methyltransferase that methylates accessible GpC dinucleotides in vivo, then sorted by FACS, bisulfite-converted, and sequenced. CpG methylation reports endogenous 5mC; GpC methylation reports accessibility because nucleosomal DNA is protected from M.CviPI; the spacing between accessible GpC patches reports nucleosome phasing on individual molecules.

scNOMe-seq recovers DNase-hypersensitivity-site accessibility at single-cell resolution in GM12878 and K562 cells, detects single-molecule CTCF footprints within individual accessible loci, and estimates average nucleosome phasing distances per cell. The single-read structure is informative: each multi-GpC read independently reports accessibility at multiple positions, allowing per-read footprinting and per-locus actuated-vs-closed determination that count-based scATAC-seq cannot make.

## Why this matters

The original NOMe-seq single-cell adaptation, predating Fiber-seq's m6A-based footprinting (Stergachis 2020) and inheriting the GpC-methyltransferase chemistry that Clark et al.~later integrated into scNMT-seq. Anchors §3.2 (chromatin accessibility — the methylation-footprinting axis) and §3.3 (methylation joint readouts). Demonstrates that joint methylome + accessibility on the same single cell is achievable with a single bisulfite-sequencing assay.

---
**Source:** [DOI](https://doi.org/10.7554/eLife.23203) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/28653622/)

---
**Source:** [DOI](https://doi.org/10.7554/eLife.23203) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/28653622/)

## Related

- [[30-Concepts/nome-seq]]
- [[30-Concepts/single-molecule-footprinting]]
- [[10-Summaries/scnmt-seq-enables-joint-profiling-of-chromatin-accessibility-dna-methylation-and-transcription-in-single-cells]]
- [[10-Summaries/andrewb-2020-science]]
