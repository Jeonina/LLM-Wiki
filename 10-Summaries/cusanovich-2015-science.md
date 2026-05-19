---
type: summary
title: "Cusanovich 2015 — Multiplex single-cell profiling of chromatin accessibility by combinatorial cellular indexing"
source: "[[00-Sources/papers/Multiplex single-cell profiling of chromatin accessibility by combinatorial cellular indexing]]"
aliases: ["sci-ATAC-seq founding paper", "Cusanovich 2015"]
tags: [scATAC-seq, combinatorial-indexing, accessibility, Shendure-lab]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Cusanovich et al. (2015) — *Multiplex single-cell profiling of chromatin accessibility by combinatorial cellular indexing* — *Science*. [DOI](https://doi.org/10.1126/science.aab1601)

Cusanovich and colleagues (Shendure lab) introduced sci-ATAC-seq (single-cell combinatorial indexing ATAC-seq), the first scATAC-seq method that does not require physical compartmentalization of single cells. Permeabilized nuclei are distributed across 96 wells, where Tn5 transposases pre-loaded with barcoded adaptors tag accessible chromatin in bulk. Nuclei are then pooled, re-distributed across a second 96-well plate, and a second barcode is added by PCR. The combinatorial barcoding scheme means that each cell receives a unique well-pair-defined barcode combination from which its identity can be recovered.

Validated on mixed GM12878/HEK293T and GM12878/HL-60 cell populations, sci-ATAC-seq distinguished cell types unambiguously: 93% of barcode combinations had >90% reads mapping to a single genome (Patski or GM12878), and reads from human single cells overlapped reference DHS maps at 20–34-fold enrichment. The method profiled 15,000+ single cells per assay and identified coordinated chromatin-accessibility modules within and between cell types.

## Why this matters

The first published combinatorial-indexing scATAC-seq method, complementary to the contemporaneous droplet-based scATAC-seq (Buenrostro 2015). Combinatorial indexing scales throughput linearly with well count rather than droplet count, enabling million-cell experiments at modest cost. Anchors §3.2 (chromatin accessibility) alongside Buenrostro 2015, Cusanovich 2018 (mouse atlas), and the SHARE-seq/sci-CAR joint-assay extensions.

---
**Source:** [DOI](https://doi.org/10.1126/science.aab1601) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/25953818/)

## Related

- [[30-Concepts/scatac-seq]]
- [[30-Concepts/combinatorial-indexing]]
- [[20-Entities/jay-shendure]]
- [[10-Summaries/cao-2018-sci-car]]
