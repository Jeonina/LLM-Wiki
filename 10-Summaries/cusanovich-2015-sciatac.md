---
type: summary
title: "Cusanovich 2015 — sci-ATAC-seq: multiplex single-cell chromatin accessibility by combinatorial indexing"
aliases: ["Cusanovich 2015 sci-ATAC-seq", "sci-ATAC-seq", "combinatorial indexing scATAC"]
tags: [sci-ATAC-seq, combinatorial-indexing, scATAC-seq, Tn5, founding-method, Shendure-lab, Trapnell-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Darren_2015_Science.pdf"]
---

Cusanovich, Daza, Adey et al. (Shendure, Trapnell labs; UW + OHSU + Illumina) introduced **sci-ATAC-seq**, the founding **combinatorial cellular indexing** scATAC-seq method. Nuclei are distributed across 96 wells where barcoded Tn5 transposomes molecularly tag chromatin in bulk; nuclei are then pooled and redistributed into a second 96-well plate for PCR with indexed primers. Each nucleus traverses a unique combination of well barcodes, enabling deconvolution without physical compartmentalization. Profiled >15,000 single cells from human and mouse cell-line mixtures with ~73% PCR-duplication rate and high mapping specificity. Cells cluster by chromatin-accessibility landscape and resolve modules of coordinately regulated accessibility within and between cell types.

## Why this matters

The companion founding scATAC-seq paper to Buenrostro 2015 (Fluidigm-based). sci-ATAC-seq's combinatorial-indexing architecture (no compartmentalization) became the dominant scalable model — directly underlying sci-ATAC-seq3, snmC-seq, sci-fate, and most large brain atlases. Anchors §3.2 alongside Buenrostro 2015. Essential citation when describing the scATAC-seq founding moment — both methods appeared in the same Science issue (22 May 2015).

## Related

- [[10-Summaries/buenrostro-2015-nature]]
- [[10-Summaries/zhang-2024-snapatac2]]
- [[10-Summaries/luo-2024-scatac-benchmark]]
- [[20-Entities/jay-shendure]]
- [[30-Concepts/combinatorial-indexing]]
