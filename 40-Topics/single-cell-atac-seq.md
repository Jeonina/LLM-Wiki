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
- [[30-Concepts/scatac-imputation]] — dropout recovery / denoising landscape
- [[30-Concepts/scopen]] — regularized NMF imputation
- [[30-Concepts/scale]] — VAE + Gaussian Mixture Model deep generative method

## Key entities

- [[20-Entities/william-greenleaf]] — Greenleaf lab; scATAC-seq, chromVAR, µATAC-seq
- [[20-Entities/jason-buenrostro]] — Buenrostro; chromVAR co-author; foundational hematopoietic scATAC datasets
- [[20-Entities/stein-aerts]] — Aerts lab; cisTopic, SCENIC
- [[20-Entities/bing-ren]] — Ren lab; SnapATAC, atlas-scale scATAC
- [[20-Entities/fabian-theis]] — Theis lab; EpiScanpy, scanpy

## Sources, by sub-theme

### Foundational assay and analysis
- [[10-Summaries/schep-2017-chromvar]] — Schep/Greenleaf 2017. TF motif aggregation under sparsity.

### Clustering and dimensionality reduction
- [[10-Summaries/bravo-2019-cistopic]] — Bravo/Aerts 2019. LDA topic modeling.
- [[10-Summaries/fang-2021-snapatac]] — Fang/Ren 2021. Peak-free, Nyström-scaled to 1M cells.
- [[10-Summaries/zamanighomi-2018-scabc]] — Zamanighomi/Wong 2018. scABC weighted k-medoids.
- [[10-Summaries/danese-2021-episcanpy]] — Danese/Theis 2021. Python framework.

### High-throughput platforms
- [[10-Summaries/mezger-2018-microfluidic-atac]] — Mezger/Greenleaf 2018. µATAC-seq on ICELL8 nanowell array.

### Comparison to bulk
- [[10-Summaries/gur-2025-scatac-vs-bulk]] — Gur/Hughes 2025. Pseudo-bulked scATAC matches bulk ATAC and reveals within-population heterogeneity.

### Imputation and denoising
- [[10-Summaries/li-2021-scopen]] — Li/Costa 2021. scOpen: regularized NMF imputation; lowest memory; Runx1 in kidney fibrosis.
- [[10-Summaries/xiong-2019-scale]] — Xiong/Zhang 2019. SCALE: VAE + GMM; interpretable latent features; reveals batch effects.

## Synthesized notes

None yet. A natural note: "How to choose a scATAC-seq analysis tool" — chromVAR for TF interpretation, cisTopic for trajectory-rich data with regulatory programs, SnapATAC for atlas-scale or rare-cell-type discovery, EpiScanpy for scanpy-native multi-omics workflows.

## Open questions

- Three-dimensional accessibility (combined ATAC + Hi-C in single cells) is now possible but the analysis tooling has not caught up.
- Most scATAC-seq tools are built on peak coordinates from aggregate signal — biasing toward abundant cell types. SnapATAC's peak-free approach is a partial solution but field still mostly peak-anchored.

## Related

- [[40-Topics/chromatin-architecture]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/histone-modifications]]

## Linked summaries (lint pass 2026-05-21)

- [[10-Summaries/mezger-2018-microfluidic-atac]] — Mezger 2018 — µATAC-seq: high-throughput nanoliter scATAC.
- [[10-Summaries/derop-2024-natbiotech]] — De Rop 2024 — PUMATAC: systematic benchmarking of scATAC protocols.
- [[10-Summaries/luo-2024-scatac-benchmark]] — Luo 2024 — Benchmarking computational methods for single-cell chromatin data.


## Added 2026-08-13

A computational route to accessibility where the assay is unavailable: ISON infers **spatial** chromatin accessibility from spatial transcriptomics plus single-cell multiome, and reports that the inference recovers regulatory signal better than sparse direct measurement ([[10-Summaries/debnath-2026-ison]]).

It also fills a capability gap in motif-based accessibility analysis: because paralogous TFs share motifs, [[30-Concepts/chromvar|chromVAR]]-style methods cannot separate them, whereas joint expression + accessibility modelling can estimate spot-level TF activity **distinguishing TFs within the same family** ([[10-Summaries/debnath-2026-ison]]).
