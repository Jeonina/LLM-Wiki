---
type: summary
title: "de Bourcy 2014 — A Quantitative Comparison of Single-Cell Whole Genome Amplification Methods"
source: "[[00-Sources/papers/A Quantitative Comparison of Single-Cell Whole Genome Amplification Methods]]"
aliases: ["de Bourcy 2014", "Quake WGA comparison"]
tags: [scWGA, MDA, MALBAC, NEB-WGA, PicoPLEX, benchmark, Quake-lab, Stanford]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** de Bourcy et al. (2014) — *A Quantitative Comparison of Single-Cell Whole Genome Amplification Methods* — *PLOS One*. [DOI](https://doi.org/10.1371/journal.pone.0105585)

de Bourcy, De Vlaminck, Kanbar, Wang, Gawad and Quake (Stanford) performed the first systematic head-to-head benchmark of three single-cell whole-genome amplification chemistries: **MDA** (Multiple Displacement Amplification, Φ29-based), **MALBAC** (Multiple Annealing and Looping Based Amplification Cycles), and **PicoPLEX/NEB-WGA** (a hybrid PCR-based kit). Forty-one different reactions were run on bulk and single-cell *E. coli* templates across microfluidic-chamber (150 nL) and tube (50 μL) volumes, sequenced on Illumina MiSeq at 158× average depth.

Quantitative comparisons: coverage uniformity (Lorenz curves), reaction-gain-dependence of bias, read mappability, SNV detection sensitivity/specificity, CNV detection, *de novo* assembly contiguity, and background contamination level. Findings: (i) microfluidic reactions are dramatically more robust to contamination (0.035% unmapped reads vs >93% for tube MALBAC/NEB-WGA single-cell); (ii) MDA bias worsens monotonically with reaction gain — secondary MDA exaggerates bias; (iii) **no single method wins** — MDA best for SNV calling, MALBAC/NEB-WGA best for CNV calling with more uniform coverage; (iv) bias structure differs (low-frequency noise for MDA, high-frequency for MALBAC/NEB-WGA).

## Why this matters

Foundational benchmark for scWGA chemistry selection, predating the broader adoption of LIANTI (Chen 2017) and PTA (Gonzalez-Pena 2021). Anchors §3.1 chemistry-comparison discussion and provides the empirical basis for the "horses for courses" framing: chemistry choice depends on whether the downstream question is SNV vs CNV vs de-novo assembly. Important historical context: this paper is from the same Quake group that developed PicoPLEX/Fluidigm scATAC.

---
**Source:** [DOI](https://doi.org/10.1371/journal.pone.0105585) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/25136831/)

## Related

- [[10-Summaries/gonzalez-pena-2021-pnas]]
- [[10-Summaries/hou-2016-cellresearch]]
- [[30-Concepts/scwga]]
- [[30-Concepts/mda]]
