---
type: summary
title: "Cao 2018 — Joint profiling of chromatin accessibility and gene expression in thousands of single cells (sci-CAR)"
source: "[[00-Sources/papers/Joint profiling of chromatin accessibility and gene expression in thousands of single cells]]"
aliases: ["sci-CAR", "Cao 2018"]
tags: [sci-CAR, joint-assay, scATAC-seq, scRNA-seq, combinatorial-indexing, Shendure-lab]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/Joint profiling of chromatin accessibility and gene expression in thousands of single cells]]"
---

**Citation:** Cao et al. (2018) — *Joint profiling of chromatin accessibility and gene expression in thousands of single cells (sci-CAR)* — *Science*. [DOI](https://doi.org/10.1126/science.aau0730)

Cao, Cusanovich, Ramani and colleagues (Shendure / Trapnell labs) introduced sci-CAR (single-cell combinatorial indexing chromatin accessibility and mRNA), the founding joint-assay method that profiles chromatin accessibility and gene expression from the same cell at thousand-cell scale via split-pool barcoding.

The chemistry: nuclei are extracted and distributed to a first set of wells where a first scRNA-seq index (poly-T RT primer) and a first scATAC-seq index (Tn5 transposase) are introduced simultaneously. After cDNA synthesis and tagmentation, nuclei are pooled, redistributed across a second set of wells, lysed, and a second scRNA-seq and scATAC-seq index added by PCR. The two-step combinatorial barcoding scheme produces per-cell unique barcodes that link RNA and ATAC reads back to their cell of origin.

Applied to A549 lung adenocarcinoma cells undergoing dexamethasone-induced glucocorticoid receptor activation, sci-CAR jointly profiled 11,296 cells with both modalities and reconstructed the pseudotemporal dynamics of chromatin accessibility and gene expression. Applied to adult mouse kidney, sci-CAR identified 14 cell types with both modalities recovered per cell.

## Why this matters

Founding joint scATAC + scRNA method, predating SHARE-seq, Paired-seq, and 10x multiome. Demonstrated at scale that combinatorial indexing supports joint-modality readouts and that the joint readout reveals regulatory dynamics neither modality alone exposes (chromatin accessibility leads transcription in the dexamethasone response). Anchors §2 (locus-state joint-assay table), §3.2 (accessibility), and §4 (integration tools).

---
**Source:** [DOI](https://doi.org/10.1126/science.aau0730) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/30166440/)

## Related

- [[30-Concepts/sci-car]]
- [[30-Concepts/joint-single-cell-multi-omics]]
- [[30-Concepts/combinatorial-indexing]]
- [[10-Summaries/share-seq-reveals-chromatin-potential-nature-reviews-genetics]]
- [[20-Entities/jay-shendure]]
