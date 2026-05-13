---
type: summary
title: "Dey 2015 — DR-seq: integrated genome and transcriptome sequencing from the same cell"
aliases: ["Dey 2015 DR-seq", "DR-seq", "gDNA-mRNA Sequencing"]
tags: [DR-seq, parallel-scDNA-scRNA, no-physical-separation, quasilinear-amplification, founding-method, van-Oudenaarden-lab, Hubrecht]
created: 2026-05-13
updated: 2026-05-13
sources: ["Siddharth_2015_NatureBiotechnology.pdf"]
---

Dey, Kester, Spanjaard, Bienko and van Oudenaarden (Hubrecht Institute) developed **DR-seq (gDNA-mRNA Sequencing)**, a method for integrated scDNA + scRNA from the same cell **without physical separation** of the nucleic acids. Workflow: single-cell lysate + reverse transcription with a poly-A primer containing cell-specific barcodes and Illumina/T7 sequences → ssDNA cDNA mixed with gDNA → 7 rounds of **quasilinear whole-genome amplification** using an adapter with defined 5' end + random nucleotides → split into two tubes: one PCR-amplified for gDNA library, the other in-vitro-transcribed (T7) to produce aRNA for mRNA library. Mouse ESC validation showed comparable detection efficiency to standalone scRNA-seq and scDNA-seq, with the additional capability of correlating per-cell CNV to per-cell mRNA expression.

## Why this matters

The **third 2015 founding paper for parallel scDNA+scRNA**, alongside G&T-seq (Macaulay 2015, physical separation) and the Hou 2016 scTrio-seq triple-omics. DR-seq's no-separation design contrasts with G&T-seq's bead-based separation — establishing the "physical separation vs. in-tube amplification" dichotomy that Vandereyken 2023 review uses as a design-principle axis. Important historical citation in §3.1. Existing `dey2015` bibkey already present.

## Related

- [[10-Summaries/macaulay-2015-gt-seq]]
- [[10-Summaries/hou-2016-sctrio-seq]]
- [[10-Summaries/vandereyken-2023-scmultiomics-review]]
- [[30-Concepts/parallel-scDNA-scRNA]]
