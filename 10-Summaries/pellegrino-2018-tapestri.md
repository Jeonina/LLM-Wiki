---
type: summary
title: "Pellegrino 2018 — High-throughput single-cell DNA sequencing of acute myeloid leukemia tumors with droplet microfluidics"
source: "[[00-Sources/papers/High-throughput single-cell DNA sequencing of acute myeloid leukemia tumors with droplet microfluidics]]"
aliases: ["Pellegrino 2018", "Tapestri", "Mission Bio scDNA", "MissionBio"]
tags: [Tapestri, MissionBio, droplet-scDNA, AML, targeted-panel, clonal-evolution, Eastburn]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Pellegrino et al. (2018) — *High-throughput single-cell DNA sequencing of acute myeloid leukemia tumors with droplet microfluidics* — *Genome Research*. [DOI](https://doi.org/10.1101/gr.232272.117)

Pellegrino, Sciambi, Treusch, Durruthy-Durruthy, Gokhale, Jacob, Chen, Geis, Oldham, Matthews, Kantarjian, Futreal, Patel, Jones, Takahashi and Eastburn (Mission Bio + MD Anderson) developed the founding **droplet-based high-throughput single-cell DNA sequencing** workflow — now commercialized as the Mission Bio Tapestri platform. Two-step droplet workflow: (1) encapsulate single cells with protease for cell-identifying lysis; (2) merge with PCR reagent + cell-identifying barcoded hydrogel beads for amplification of a custom amplicon panel.

The two-step design (with protease pre-lysis) raised genomic-DNA detection rate from ~5% to ~98% — overcoming the genomic-DNA-amplification problem that prevented scDNA equivalents of scRNA Drop-seq. Demonstration: longitudinal AML samples (diagnosis, remission, relapse) from two patients sequenced across >16,000 cells at 62 amplicons covering 23 commonly-mutated genes. The platform identified rare pathogenic clones during complete remission and resolved sub-clonal evolution invisible to bulk WGS.

## Why this matters

The technological ancestor of every targeted-panel droplet scDNA platform deployed today in cancer genomics (Tapestri DNA, Tapestri DNA+Protein, Mission Bio CNV). Anchors §3.1 (targeted-panel scDNA chemistries), §4 (variant-calling at the panel level), and §5 (cancer clonal-evolution applications). The targeted-panel paradigm is the practical workhorse for clinical scDNA — distinct from low-coverage genome-wide platforms (10x CNV, DLP+) which serve a different question. Methodological lineage continues: Tapestri DNA+ATAC (Hu/Buenrostro), Tapestri DNA+ChIP, Mission Bio CRISPR-screen scDNA.

---
**Source:** [DOI](https://doi.org/10.1101/gr.232272.117) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/30087104/)

---
**Source:** [DOI](https://doi.org/10.1101/gr.232272.117) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/30087104/)

## Related

- [[10-Summaries/kim-2018-tnbc-chemoresistance]]
- frankell 2019 nature
- laks 2019 cell
- [[40-Topics/scdna-cancer-applications]]
