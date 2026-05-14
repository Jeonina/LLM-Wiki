---
title: LLM Wiki — scDNA-seq & Single-Cell Epigenomics
description: A living knowledge base on single-cell DNA sequencing, somatic mosaicism, and adjacent epigenomics.
updated: 2026-05-14
---

# LLM Wiki

A living knowledge base on **single-cell DNA sequencing**, **somatic mosaicism**, and **single-cell epigenomics** — built and maintained with the help of an LLM, following [Andrej Karpathy's LLM Wiki pattern](10-Summaries/example-llm-wiki).

> This wiki synthesizes ~130 papers spanning scDNA-seq methods, chromatin profiling, DNA methylation, multi-omics assays, and computational tools. Start from a topic below, or browse the [[catalog|full catalog]].

The central motivation: there is no DNA-centric locus-state framework that jointly interprets mutation + epigenome + RNA at single-cell scale. The wiki tracks the methods that get us closer to one — see [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|the synthesis gap note]] for the framing.

---

## Core Topics

### Single-Cell DNA Sequencing

The foundation: how to sequence a genome from one cell. Covers whole-genome amplification chemistries (MDA → MALBAC → LIANTI → **PTA**), variant calling, and error correction.

**Start here →** [[30-Concepts/scdna-seq]] · [[30-Concepts/scwga]] · [[30-Concepts/pta]]
**Key review →** [[10-Summaries/diane-2025-naturereviewsgenetics|Shao et al. 2025 (NRG)]]
**Foundational →** [[10-Summaries/charles-2016-naturereviewsgenetics|Gawad & Quake 2016]]

---

### Somatic Mosaicism & Lineage Tracing

Post-zygotic mutations as both disease drivers and natural lineage barcodes. From brain mosaicism to clonal hematopoiesis, from Peto's paradox to aging.

**Start here →** [[30-Concepts/somatic-mosaicism]] · [[30-Concepts/lineage-tracing]] · [[30-Concepts/clonal-hematopoiesis]]
**Key papers →** [[10-Summaries/lodato-2015-science|Lodato 2015]] · [[10-Summaries/coorens-2021-nature|Coorens 2021]] · [[10-Summaries/cagan-2022-nature|Cagan 2022]]
**Brain focus →** [[10-Summaries/taejeong-2018-science|Bae 2018]] · [[10-Summaries/taejeong-2022-science|Bae 2022]] · [[10-Summaries/miller-2022-nature|Miller 2022 (AD)]]

---

### Chromatin Accessibility (scATAC-seq)

Measuring open chromatin at single-cell resolution. Includes founding methods, computational tools, and histone modification profiling.

**Start here →** [[30-Concepts/scatac-seq]] · [[30-Concepts/chromatin-accessibility]] · [[30-Concepts/cut-and-tag]]
**Founding methods →** [[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]] · [[10-Summaries/cusanovich-2015-science|Cusanovich 2015 (sci-ATAC)]]
**Tools →** [[30-Concepts/chromvar]] · [[30-Concepts/cistopic]] · [[30-Concepts/snapatac]] · [[10-Summaries/jeffrey-2021-naturegenetics|ArchR]]

---

### DNA Methylation

From bisulfite sequencing to single-cell methylomes, 5hmC detection, and methylation-based lineage tracing (EPI-Clone, MethylTree).

**Start here →** [[30-Concepts/dna-methylation]] · [[30-Concepts/bisulfite-sequencing]] · [[30-Concepts/scbs-seq]]
**Foundational →** [[10-Summaries/smallwood-2014-natmethods|Smallwood 2014 (scBS-seq)]] · [[10-Summaries/schubeler-2015-nature|Schübeler 2015]]
**Lineage tracing →** [[10-Summaries/scherer-2025-nature|EPI-Clone (Scherer 2025)]] · [[10-Summaries/chen-2025-methyltree|MethylTree (Chen 2025)]]

---

### Single-Cell Transcriptomics (scRNA-seq foundations)

The transcriptomic axis underlying every multi-omics method. Why bulk RNA-seq averages away cell-type biology, and how scRNA-seq recovers it.

**Start here →** [[30-Concepts/scrna-seq]] · [[30-Concepts/drop-seq]] · [[30-Concepts/umi-molecular-barcoding]]
**Founding →** [[10-Summaries/tang-2009-scrna-seq|Tang 2009 (first scRNA-seq)]] · [[10-Summaries/macosko-2015-drop-seq|Drop-seq (Macosko 2015)]]
**Benchmark →** [[10-Summaries/svensson-2017-power-analysis|Svensson 2017 power analysis]]

---

### Multi-Omics Joint Assays

Methods that read two or more modalities from the same cell: genotype + transcriptome (GoT), genotype + chromatin (GoT-ChA), triple-omics, and beyond.

**Start here →** [[30-Concepts/single-cell-multiomics]] · [[30-Concepts/got]] · [[30-Concepts/got-cha]]
**GoT family →** [[10-Summaries/anna-2019-nature|Nam 2019]] · [[10-Summaries/franco-2024-nature|Izzo 2024]] · [[10-Summaries/cortes-lopez-2023-cellstemcell|GoT-Splice]]
**DNA + Epigenome →** [[10-Summaries/elliott-2025-naturebiotechnology|DAF-seq]] · [[10-Summaries/andrea-2025-biorxiv|Duplex-Multiome]]

---

### Long-Read & Single-Molecule Methods

PacBio and Nanopore approaches that capture chromatin state, methylation, and structural variants on native DNA molecules.

**Start here →** [[30-Concepts/long-read-sequencing]] · [[30-Concepts/fiber-seq]] · [[30-Concepts/daf-seq]]
**Key papers →** [[10-Summaries/andrewb-2020-science|Fiber-seq (Stergachis 2020)]] · [[10-Summaries/altemose-2022-dimelo-seq|DiMeLo-seq]] · [[10-Summaries/nanda-2024-smrt-tag|SMRT-Tag]]

---

### 3D Genome at Single-Cell Resolution

Chromatin conformation capture (Hi-C) adapted for single cells, haplotype-resolved structures, and computational harmonization.

**Start here →** [[30-Concepts/3d-genome]] · [[30-Concepts/single-cell-hi-c]] · [[30-Concepts/dip-c]]
**Founding →** [[10-Summaries/nagano-2013-nature|Nagano 2013]] · [[10-Summaries/tan-2018-science|Dip-C (Tan 2018)]]

---

### Duplex Sequencing

Ultra-accurate error correction by reading both strands of a DNA molecule. Essential for detecting rare somatic variants.

**Start here →** [[30-Concepts/duplex-sequencing]] · [[30-Concepts/nanoseq]] · [[30-Concepts/codec]]
**Founding →** [[10-Summaries/schmitt-2012-pnas|Schmitt & Loeb 2012]] · [[10-Summaries/kennedy-2014-duplex-protocol|Kennedy 2014]]
**Benchmark →** [[10-Summaries/zhang-2025-smaht-duplex-benchmark|SMaHT Benchmark (Zhang 2025)]]

---

## Browse the wiki

| | |
|---|---|
| [[catalog\|Papers]] | All ~130 paper summaries, organized by topic |
| [[20-Entities/index\|People & labs]] | Researchers, labs, consortia |
| [[30-Concepts/index\|Concepts]] | Definitions: methods, terms, ideas |
| [[40-Topics/index\|Topics]] | Broad themes that gather concepts and papers |

---

## Synthesis & open threads

- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|Mosaicism × Epigenome: The Synthesis Gap]] — the central conceptual note; updated 2026-05-13 after Duplex-Multiome closes the method gap.
- [[50-Notes/open-questions]] — tensions and gaps surfaced during ingest, by domain
- [[50-Notes/synthesis-targets]] — clusters of papers ripe for a written synthesis

---

## How this wiki works

Three layers, never mixed:

1. **Sources** (`00-Sources/`) — immutable raw inputs (papers, articles, data). Read-only.
2. **Wiki** (`10-Summaries/`, `20-Entities/`, `30-Concepts/`, `40-Topics/`, `50-Notes/`) — distillation, linked into a graph.
3. **Schema** ([[CLAUDE]] + `90-Meta/templates/`) — the conventions the maintainer follows.

The maintainer reads each new source in full, writes a summary, and **touches 5–15 other pages** per ingest to weave it into the graph. See [[log|the ingest log]] for a chronological record.

---

*This wiki is a personal research tool. Papers are summarized by an LLM; always verify against the original sources. Last updated 2026-05-14.*
