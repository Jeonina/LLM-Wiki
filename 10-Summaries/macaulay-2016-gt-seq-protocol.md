---
type: summary
title: "Macaulay et al. 2016 — G&T-seq protocol: parallel sequencing of single-cell genomes and transcriptomes"
source: "[[00-Sources/papers/Separation and parallel sequencing of the genomes and transcriptomes of single cells using G&T-seq]]"
source_kind: paper
author: "Iain C. Macaulay, Mabel J. Teng, Wilfried Haerty, Parveen Kumar, Chris P. Ponting, Thierry Voet (corresponding)"
published: 2016-09-29
ingested: 2026-05-18
ingest_depth: abstract+intro
doi: "10.1038/nprot.2016.138"
journal: "Nature Protocols"
tags: [G&T-seq, single-cell-multiomics, WGA, Smart-seq2, oligo-dT-bead, protocol, Voet-lab]
entities: []
concepts:
  - "[[30-Concepts/gt-seq]]"
  - "[[40-Topics/single-cell-multiomics]]"
  - "[[30-Concepts/scwga]]"
topics:
  - "[[40-Topics/single-cell-multiomics]]"
---

**Citation:** Macaulay et al. (2016) — *G&T-seq protocol: parallel sequencing of single-cell genomes and transcriptomes* — *Nature Protocols*. [DOI](https://doi.org/10.1038/nprot.2016.138)

# Macaulay et al. 2016 — G&T-seq Nature Protocols version

> Thesis: this is the **Nature Protocols** companion to the 2015 G&T-seq method paper (Macaulay et al. 2015 *Nat Methods*) — a detailed bench protocol for separating polyA(+) mRNA from genomic DNA in a single cell using **modified oligo-dT magnetic-bead capture**, then independently performing WGA on the DNA and Smart-seq2 WTA on the RNA. Crucially, no microfluidics needed — manual or robotic execution.

## Key claims (abstract + intro)

- **Physical separation rather than co-amplification**: oligo-dT bead capture pulls polyA(+) mRNA off the cell lysate; remaining gDNA stays in supernatant. The two molecule classes never share a reaction.
- **WGA-method agnostic**: works with MDA, PCR-WGA, or DA-PCR (PicoPLEX, MALBAC). MDA recommended for SNV discovery; PCR-based for CNV profiling.
- **Smart-seq2 transcriptome arm**: full-length cDNA via template-switching; thousands of detected transcripts per cell at comparable depth to standalone Smart-seq2.
- **Throughput**: 8 cells in ~3 days manual; **96 cells in same timeframe with liquid-handling robot**.
- **Integration with bioinformatics**: SNVs and CNVs from DNA arm can be cross-referenced with expression from RNA arm in same cell — enables direct genotype-to-phenotype mapping.

## Why this matters

G&T-seq is the **canonical genome+transcriptome single-cell method** without microfluidics dependence. The 2016 protocol consolidates the bench procedure and made the technique broadly adoptable. Anchors the multi-omics branch of the wiki alongside scNMT-seq (Clark 2018), DR-seq (Dey 2015), and scTrio-seq (Hou 2016).

## Note on ingest depth

Abstract + introduction only; full PDF re-ingest will deepen the bench-step-by-step methods + troubleshooting tables.

---
**Source:** [DOI](https://doi.org/10.1038/nprot.2016.138) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/27684873/)

## Related

- [[30-Concepts/gt-seq]] · [[40-Topics/single-cell-multiomics]] · [[30-Concepts/scwga]]
- [[10-Summaries/clark-2018-scnmt-seq]] · [[10-Summaries/dey-2015-dr-seq]] · [[10-Summaries/hou-2016-sctrio-seq]]
- [[40-Topics/single-cell-multiomics]]
