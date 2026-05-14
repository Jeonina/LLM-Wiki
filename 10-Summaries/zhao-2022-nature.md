---
type: summary
title: "Zhao 2022 — Spatial genomics enables multi-modal study of clonal heterogeneity in tissues (slide-DNA-seq)"
aliases: ["slide-DNA-seq", "Zhao 2022", "spatial scDNA"]
tags: [slide-DNA-seq, spatial-genomics, scDNA, cancer, CNV, Chen-lab, Buenrostro-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Tongtong_2022_Nature.pdf"]
---

Zhao, Chiang, Morriss and colleagues (Chen + Buenrostro labs, Broad Institute) introduced slide-DNA-seq, a spatial single-cell DNA-sequencing method that captures genome-wide DNA from intact tissue sections with spatial registration. The chemistry extends Slide-seq's barcoded-bead arrays (originally developed for spatial transcriptomics) to DNA: a section of fresh-frozen tissue is laid onto a 3-mm array of $\sim$10-µm polystyrene beads, each carrying a unique spatial barcode; tissue DNA is Tn5-tagmented in situ, captured by bridge oligonucleotide hybridization onto the beads, ligated, photocleaved, and amplified into a sequencing library with bead-barcode-resolved spatial coordinates.

Applied to a mouse cerebellum control and to a primary human cancer + mouse-model metastasis (Kras${}^{G12D/+}$;Trp53${}^{-/-}$), slide-DNA-seq spatially mapped CNV-defined tumor clones within tissue architecture. Distinct subclonal CNV patterns occupy distinct spatial neighborhoods, and integration with spatial transcriptomics on adjacent sections links clone-specific CNV alterations to clone-specific gene-expression and tumor-microenvironment patterns.

## Why this matters

The first scalable spatial scDNA-seq method, complementary to in-situ genome sequencing (Payne 2021 IGS) for the spatial axis of single-cell genomics. Anchors §3.5 (3D genome and spatial) and §5 (cancer applications). Particularly relevant for understanding spatially-constrained somatic mosaicism (developmental founder clones, focal cortical malformations) and tumor evolution.

---
**Source:** [DOI](https://doi.org/10.1038/s41586-021-04217-4) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/34912115/)

---
**Source:** [DOI](https://doi.org/10.1038/s41586-021-04217-4) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/34912115/)

## Related

- [[30-Concepts/spatial-scdna]]
- [[10-Summaries/andrewc-2020-science]]
- [[10-Summaries/kim-2018-cell]]
- [[20-Entities/jason-buenrostro]]
- [[20-Entities/fei-chen]]
