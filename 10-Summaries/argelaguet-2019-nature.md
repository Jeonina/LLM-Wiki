---
type: summary
title: "Argelaguet 2019 — Multi-omics profiling of mouse gastrulation at single cell resolution"
aliases: ["scNMT-seq gastrulation", "Argelaguet 2019"]
tags: [scNMT-seq, joint-assay, methylation, accessibility, transcriptome, gastrulation, MOFA]
created: 2026-05-13
updated: 2026-05-13
sources: ["Ricard_2019_Nature.pdf"]
---

Argelaguet, Clark and colleagues (Reik / Stegle / Marioni labs) applied scNMT-seq (single-cell Nucleosome, Methylome and Transcriptome sequencing) to 1,105 single cells from mouse embryos at four developmental stages (E4.5, E5.5, E6.5, E7.5) spanning the exit from pluripotency through primary germ-layer specification.

Three findings. (1) Global methylation rises from ~25% (E4.5) to ~75% (E7.5) in embryonic tissues, driven by a de novo wave at CpG-poor loci between E4.5 and E5.5; chromatin accessibility declines more gradually from ~38% to ~30%. (2) Lineage-specific methylation and accessibility patterns emerge at enhancer marks (distal H3K27ac peaks) — mesoderm- and endoderm-committed cells undergo coordinated TET-mediated demethylation and accessibility gain at lineage-specific enhancers, while ectodermal cells inherit the methylation/accessibility landscape established already in the early epiblast. (3) Multi-Omics Factor Analysis (MOFA) jointly decomposed RNA, methylation, and accessibility, identifying six factors with the first two capturing the emergence of the three germ layers and linking gene-expression variation to coordinated enhancer-mark changes; promoter or H3K4me3-marked changes contributed little to lineage variance.

## Why this matters

The canonical demonstration that triple-modality single-cell readout (transcriptome + methylome + accessibility) on the same cell resolves the asymmetric epigenetic programs of germ-layer specification. Establishes that ectoderm priming and mesendoderm reprogramming follow distinct epigenetic logic — a finding only resolvable when the three modalities are read jointly per cell. Anchors §2 (locus-state joint-assay), §3.3 (methylation), §5 (development applications), and the introduction of MOFA as a standard joint-modality factor model in §4.

## Related

- [[30-Concepts/scnmt-seq]]
- [[30-Concepts/joint-single-cell-multi-omics]]
- [[10-Summaries/scnmt-seq-enables-joint-profiling]]
- [[10-Summaries/chongyuan-2018-naturecommunications]]
- [[20-Entities/wolf-reik]]
