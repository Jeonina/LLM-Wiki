---
type: topic
title: Single-cell ATAC-seq
aliases: [scATAC-seq, single-cell chromatin accessibility]
tags: [scATAC, chromatin-accessibility, cis-regulatory, software, transcription-factors]
created: 2026-05-12
updated: 2026-05-12
---

# Single-cell ATAC-seq

> scATAC-seq measures genome-wide chromatin accessibility in individual cells via Tn5 transposase preferential cutting at open chromatin. Per-cell data are extremely sparse (only ~0/1/2 reads possible per locus per diploid cell), so analysis methods aggregate signal across peaks sharing a motif, bin the genome into wider windows, or apply topic modeling — each method trading off resolution, scalability, and rare-cell-type sensitivity.

## Core concepts

- [[30-Concepts/scatac-seq]] — the assay itself
- [[30-Concepts/atac-seq]] — bulk progenitor
- [[30-Concepts/chromatin-accessibility]] — the underlying biological signal
- [[30-Concepts/tn5-tagmentation]] — the enzymatic basis
- [[30-Concepts/chromvar]] — TF motif aggregation
- [[30-Concepts/cistopic]] — LDA topic modeling
- [[30-Concepts/snapatac]] — peak-free 5-kb-window Jaccard clustering
- [[30-Concepts/episcanpy]] — scanpy-based unified epigenomics framework
- [[30-Concepts/scabc]] — weighted k-medoids clustering

## Key entities

- [[20-Entities/william-greenleaf]] — Greenleaf lab; scATAC-seq, chromVAR, µATAC-seq
- [[20-Entities/jason-buenrostro]] — Buenrostro; chromVAR co-author; foundational hematopoietic scATAC datasets
- [[20-Entities/stein-aerts]] — Aerts lab; cisTopic, SCENIC
- [[20-Entities/bing-ren]] — Ren lab; SnapATAC, atlas-scale scATAC
- [[20-Entities/fabian-theis]] — Theis lab; EpiScanpy, scanpy

## Sources, by sub-theme

### Foundational assay and analysis
- [[10-Summaries/chromvar-inferring-transcription-factor-associated-accessibility-from-single-cell-epigenomic-data]] — Schep/Greenleaf 2017. TF motif aggregation under sparsity.

### Clustering and dimensionality reduction
- [[10-Summaries/cistopic-cis-regulatory-topic-modeling-on-single-cell-atac-seq-data]] — Bravo/Aerts 2019. LDA topic modeling.
- [[10-Summaries/comprehensive-analysis-of-single-cell-atac-seq-data-with-snapatac]] — Fang/Ren 2021. Peak-free, Nyström-scaled to 1M cells.
- [[10-Summaries/unsupervised-clustering-and-epigenetic-classification-of-single-cells]] — Zamanighomi/Wong 2018. scABC weighted k-medoids.
- [[10-Summaries/episcanpy-integrated-single-cell-epigenomic-analysis]] — Danese/Theis 2021. Python framework.

### High-throughput platforms
- [[10-Summaries/high-throughput-chromatin-accessibility-profiling-at-single-cell-resolution]] — Mezger/Greenleaf 2018. µATAC-seq on ICELL8 nanowell array.

### Comparison to bulk
- [[10-Summaries/scatac-seq-generates-more-accurate-and-complete-regulatory-maps-than-bulk-atac-seq]] — Gur/Hughes 2025. Pseudo-bulked scATAC matches bulk ATAC and reveals within-population heterogeneity.

## Synthesized notes

None yet. A natural note: "How to choose a scATAC-seq analysis tool" — chromVAR for TF interpretation, cisTopic for trajectory-rich data with regulatory programs, SnapATAC for atlas-scale or rare-cell-type discovery, EpiScanpy for scanpy-native multi-omics workflows.

## Open questions

- Three-dimensional accessibility (combined ATAC + Hi-C in single cells) is now possible but the analysis tooling has not caught up.
- Most scATAC-seq tools are built on peak coordinates from aggregate signal — biasing toward abundant cell types. SnapATAC's peak-free approach is a partial solution but field still mostly peak-anchored.

## Related

- [[40-Topics/chromatin-architecture]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/histone-modifications]]
