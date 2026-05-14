---
type: summary
title: "Iqbal 2023 — Computational Methods for Single-cell DNA Methylome Analysis"
aliases: ["Iqbal 2023", "Wanding Zhou methylome review", "scDNA methylome review"]
tags: [review, single-cell-methylome, computational-tools, scBS-seq, Zhou-lab, UPenn, CHOP]
created: 2026-05-13
updated: 2026-05-13
sources: ["Waleed_2023_GenomicsProteomicsBioinformatics.pdf"]
---

Iqbal and Zhou (CHOP + UPenn) surveyed the current state of **computational tools for single-cell DNA methylome data analysis**. The review covers the full processing pipeline: data preprocessing (Bismark, BS-Seeker, BSMAP), quality control (Bismark-style mapping-efficiency metrics), imputation (Melissa, Epiclomal, DeepCpG), dimensionality reduction (PCA on methylation rates, NMF), cell clustering (BackSPIN, PDclust, Epiclomal, Melissa), supervised cell annotation, cell-lineage reconstruction (MethylTree, EPI-Clone), gene-activity scoring, and integration with transcriptome data.

Key unique aspects discussed: (i) bulk-vs-single-cell methylome analysis differences (Table 1 with 8 comparison axes); (ii) the uneven CpG distribution problem (CpG islands vs sparse CpG, late-replicating vs early-replicating regions); (iii) non-traditional uses of methylation data — copy-number annotation, somatic-mutation identification, sex-chromosome epigenetic mosaicism; (iv) co-assay integration when methylation is jointly assayed with RNA, accessibility, or Hi-C.

## Why this matters

A field-defining review of the §4 methylation-computational tool landscape, complementing the Liu/Conesa 2025 long-read review and the Fu/Sedlazeck 2025 long-read review. Particularly useful for the review's organization because Iqbal & Zhou explicitly map analysis steps to tool choices — providing the scaffold for our §4 methylation subsection. Anchors §3.3 (methylation analysis) and §4 (computational methods).

---
**Source:** [DOI](https://doi.org/10.1016/j.gpb.2022.05.007) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/35718270/)

---
**Source:** [DOI](https://doi.org/10.1016/j.gpb.2022.05.007) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/35718270/)

## Related

- [[10-Summaries/kapourani-2019-melissa]]
- [[10-Summaries/desouza-2020-epiclomal]]
- [[10-Summaries/kapourani-2021-scmet]]
- [[10-Summaries/chen-2025-methyltree]]
- [[20-Entities/wanding-zhou]]
