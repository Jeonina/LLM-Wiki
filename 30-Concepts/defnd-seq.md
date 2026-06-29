---
type: concept
title: DEFND-seq
aliases: [DEFND-seq, DNA and Expression Following Nucleosome Depletion]
tags: [single-cell-multiomics, DNA-RNA-coassay, nucleosome-depletion, 10x-genomics]
created: 2026-06-02
updated: 2026-06-02
---

# DEFND-seq

> A scalable droplet method for co-sequencing genomic DNA and RNA from the same single nucleus, by depleting nucleosomes and then running the nuclei through the **stock 10x Genomics Multiome (ATAC+GEX) kit** ([[10-Summaries/olsen-2025-defnd-seq]]).

## Definition

DEFND-seq (DNA and Expression Following Nucleosome Depletion) treats nuclei with lithium diiodosalicylate (the LAND method) to strip nucleosomes, exposing the genome so Tn5 tagments it uniformly rather than only at open chromatin ([[10-Summaries/olsen-2025-defnd-seq]]). The depleted nuclei then go through unmodified 10x Multiome microfluidics, yielding one mRNA library and one whole-genome gDNA library per nucleus ([[10-Summaries/olsen-2025-defnd-seq]]).

## Why it matters

- Repurposes a chromatin-accessibility platform into a genome+transcriptome co-assay on widely available 10x hardware with commercial kits — broad accessibility without new instruments ([[10-Summaries/olsen-2025-defnd-seq]]).
- Achieves coverage uniformity (100-kb CV ~0.6) comparable to dedicated scDNA methods like PTA and MDA but at >200× fewer reads per cell, while also reading RNA ([[10-Summaries/olsen-2025-defnd-seq]]).
- Library cost ~US$0.56/cell, scalable to ~40k nuclei per chip ([[10-Summaries/olsen-2025-defnd-seq]]).

## How it compares

- LAND nucleosome depletion beats crosslink+SDS (xSDS): more complex libraries, more uniform coverage, full-length cDNA (xSDS truncates cDNA) ([[10-Summaries/olsen-2025-defnd-seq]]).
- Higher unique transcripts and fragments than the scalable split-pool sci-L3 co-assay at matched depth ([[10-Summaries/olsen-2025-defnd-seq]]).
- **Whole-genome but high-ADO**, in contrast to the **targeted, low-ADO** [[30-Concepts/sdr-seq]] ([[10-Summaries/lindenhofer-2025-sdr-seq]]); see [[50-Notes/droplet-vs-single-molecule-scdna]].

## Examples

- In glioblastoma, linked focal *EGFR* amplification to one subclone and focal *PDGFRA* amplification to an OPC-like proneural RNA cluster, recapitulating the TCGA PDGFRA–proneural association at single-cell resolution ([[10-Summaries/olsen-2025-defnd-seq]]).
- Detected somatic SNVs (*EGFR*, *MAP2K3*, *PREX1*) and worked on >4-year cryopreserved tissue ([[10-Summaries/olsen-2025-defnd-seq]]).

## Related

- [[30-Concepts/joint-single-cell-multi-omics]] · [[30-Concepts/sdr-seq]] · [[30-Concepts/gt-seq]] · [[30-Concepts/dr-seq]] · [[30-Concepts/tn5-tagmentation]] · [[30-Concepts/pta]]
- [[40-Topics/single-cell-multiomics]] · [[40-Topics/scdna-cancer-applications]] · [[20-Entities/peter-a-sims]]
