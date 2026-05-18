---
type: summary
title: "Stuart 2021 — Single-cell chromatin state analysis with Signac"
source: "[[00-Sources/papers/Single-cell chromatin state analysis with Signac]]"
aliases: ["Signac", "Stuart 2021"]
tags: [scATAC-seq, multi-omics, computational, Seurat, software]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/Single-cell chromatin state analysis with Signac]]"
---

**Citation:** Stuart et al. (2021) — *Single-cell chromatin state analysis with Signac* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-021-01282-5)

Stuart, Srivastava, Madad, Lareau and Satija (Satija lab) describe Signac, an R toolkit for end-to-end single-cell chromatin data analysis that interoperates with the Seurat package via a specialized ChromatinAssay class. Signac handles scATAC-seq, sciCUT&Tag, and related fragment-file inputs, performing peak calling, quantification, QC, dimension reduction (LSI), clustering, motif analysis, peak-to-gene linkage, and integration across modalities (mRNA, surface protein, mitochondrial genotype, CRISPR perturbations).

The paper demonstrates the framework on a 10x multiome PBMC dataset (10,466 cells with paired scRNA + scATAC), recovering canonical hematopoietic cell types, calling cell-type-specific peaks (improving sensitivity for rare populations such as γδ T cells), performing TF footprinting at EOMES/TBX21/TBX2 motifs, and producing peak-to-gene-expression linkage maps. Signac scales to >700,000 cells, supports tabix-indexed on-disk fragment storage, and integrates with chromVAR for motif deviation analysis.

## Why this matters

The de-facto computational backbone for most single-cell chromatin and joint multi-omics workflows since 2021. Anchors §4 (computational framework) alongside ArchR (Granja 2021) and chromVAR. Critical for analyses that pair sequence-based (genotype) data with chromatin state in the same cell — the joint-assay use cases that this review's locus-state framework foregrounds.

---
**Source:** [DOI](https://doi.org/10.1038/s41592-021-01282-5) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/34725479/)

---
**Source:** [DOI](https://doi.org/10.1038/s41592-021-01282-5) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/34725479/)

## Related

- [[20-Entities/satija-lab]]
- [[30-Concepts/scatac-seq]]
- [[30-Concepts/single-cell-multi-omics]]
- [[10-Summaries/jeffrey-2021-naturegenetics]]
- [[10-Summaries/marek-2021-naturebiotechnology]]
