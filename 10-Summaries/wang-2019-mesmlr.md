---
type: summary
title: "Wang 2019 — Single-molecule long-read sequencing reveals the chromatin basis of gene expression (MeSMLR-seq)"
aliases: ["Wang 2019 MeSMLR-seq", "MeSMLR-seq", "methyltransferase single-molecule long-read"]
tags: [MeSMLR-seq, single-molecule, nanopore, M.CviPI, nucleosome-phasing, yeast, Au-lab, Ohio-State]
created: 2026-05-13
updated: 2026-05-13
sources: ["Yunhao_2019_GenomeResearch.pdf"]
---

Wang, Wang, Liu, Thurman, Powers, Zou, Zhao, Hefel, Li, Zabner and Au (Ohio State, Iowa) developed **MeSMLR-seq** (Methyltransferase treatment + Single-Molecule Long-Read sequencing), one of the foundational single-molecule long-read chromatin-accessibility methods. Protocol: spheroplast preparation (yeast cell-wall digestion via Zymolyase) → in-vivo M.CviPI GpC-methyltransferase treatment → genomic DNA extraction without PCR amplification → direct Oxford Nanopore sequencing → 5mC calling at GpC sites to map accessibility along long reads.

Applied to haploid *S. cerevisiae* (where single DNA molecules represent single cells), MeSMLR-seq profiled up to **356 nucleosomes per long read**, enabling investigation of the **combinatorics** of nucleosome arrangements around transcription start sites at single-molecule scale. Combined with scRNA-seq data, the method quantitatively related chromatin accessibility to gene transcription in heterogeneous scenarios, and revealed coupled accessibility changes for two neighboring glucose-transporter genes in response to glucose concentration changes.

## Why this matters

A foundational single-molecule long-read accessibility method (Q3 2019, predating SMAC-seq Q1 2020 and Fiber-seq Q3 2020). MeSMLR-seq established the core principle: methyltransferase footprinting + Nanopore long-reads → per-molecule combinatorial accessibility states. The yeast haploid system is uniquely powerful because one molecule = one cell, eliminating the bulk-averaging confound. Anchors §3.2 (single-molecule footprinting family, alongside SMAC-seq, Fiber-seq, SAMOSA, nanoNOMe, STAM-seq). The historical lineage: NOMe-seq (bulk bisulfite) → MeSMLR-seq (bulk Nanopore, yeast) → SMAC-seq (bulk Nanopore, dual MTase) → Fiber-seq (bulk PacBio, m6A) → single-cell Fiber-seq + targeted Fiber-seq.

## Related

- [[10-Summaries/shipony-2020-smac]]
- [[10-Summaries/stergachis-2020-fiberseq]]
- [[10-Summaries/lee-2020-nanonome]]
- [[10-Summaries/pott-2017-elife]]
- [[30-Concepts/single-molecule-footprinting]]
