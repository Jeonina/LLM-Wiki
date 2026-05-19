---
type: summary
title: "Lareau 2021 — Massively parallel single-cell mitochondrial DNA genotyping and chromatin profiling (mtscATAC-seq)"
source: "[[00-Sources/papers/Massively parallel single-cell mitochondrial DNA genotyping and chromatin profiling]]"
aliases: [Lareau 2021, mtscATAC-seq, Caleb 2021]
tags: [mtDNA, mitochondrial-heteroplasmy, lineage-tracing, scATAC-seq, joint-assay, single-cell-multiomics, foundational]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Lareau et al. (2021) — *Massively parallel single-cell mitochondrial DNA genotyping and chromatin profiling (mtscATAC-seq)* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-020-0645-6)

# Lareau et al. 2021 — mtscATAC-seq

> Caleb A. Lareau, Leif S. Ludwig, Christoph Muus, Satyen H. Gohil, Tongtong Zhao, Zachary Chiang, Karin Pelka, Jeffrey M. Verboon, Wendy Luo, Elena Christian, Daniel Rosebrock, Gad Getz, Genevieve M. Boland, Fei Chen, Jason D. Buenrostro, Nir Hacohen, Catherine J. Wu, **Martin J. Aryee\***, **Aviv Regev\***, **Vijay G. Sankaran\***. *Nature Biotechnology* **39**, 451–461 (April 2021). DOI: 10.1038/s41587-020-0645-6.

## Thesis

**mtscATAC-seq** is a modified 10x Genomics droplet scATAC-seq protocol that **retains and amplifies mitochondrial DNA fragments** alongside accessible nuclear chromatin. By formaldehyde fixation + mild lysis with Tween-20, mtscATAC-seq achieves **~20× higher mtDNA coverage per cell (mean 191× vs 9.6× standard scATAC)** while preserving high-quality chromatin accessibility profiles in 73% of peak signal. Combined with the **mgatk** computational toolkit, this enables **lineage tracing via somatic mtDNA mutations + concurrent chromatin state in thousands of single cells**.

## Mechanism

1. Cells fixed in 0.1–1% formaldehyde → minimizes mtDNA cross-contamination between cells (3× reduction).
2. Mild lysis with Omni-style buffer (digitonin omitted) + 0.1% Tween-20 → retains mitochondria in nuclear pellet.
3. Standard 10x Chromium scATAC-seq tagmentation + barcoding.
4. Computational read-assignment strategy: reads mapping to both mtDNA and NUMTs (nuclear mtDNA insertions) are strictly assigned to mtDNA based on uniform coverage characteristics.
5. **mgatk** variant calling uses across-cell variance (variance-mean ratio) + strand bias to call high-confidence mtDNA variants from heteroplasmy.

## Key claims

- **818 GM11906 cells with 8344A>G heteroplasmy** (MERRF mitochondrial disorder) — broad heteroplasmy distribution 0–100%, median 38%; matches bulk and family studies. Demonstrates single-cell measurement of pathogenic heteroplasmy distributions.
- Identified **co-occurring 8344A>G + 8202T>C subclonal lineages** (cells that switched between mutated and wild-type 8344 with consistent 8202 → indicates at least two subclonal lineages diverged from the cell-line founder).
- 48 high-confidence mtDNA variants in 855 TF1 cells → reconstructed phylogenetic tree of 12 subclones via shared variants. Compares favorably to supervised colony-based identification.
- **Joint readout of chromatin + mtDNA-defined clone**: heteroplasmy-binned cells show distinct promoter accessibility patterns at NR2F2, TRMT5, SENP5, NCBP2-AS2 loci. MEF2A and MEF2C TF activity correlated with heteroplasmy.
- Applied to cancer (CLL, melanoma) and in-vitro hematopoietic differentiation.

## Surprising / load-bearing for the review

- **The mtDNA-as-lineage-marker × scATAC-seq joint readout is foundational for §4.5 (Lineage Reconstruction)**. mtDNA heteroplasmy is endogenous (no engineered barcodes needed), high copy number (~2–10× nuclear), and mutation rate 10× nuclear — making it the natural single-cell-friendly lineage marker. The Lareau/Sankaran lineage of mtscATAC-seq → ReDeeM → MAESTER is the mtDNA-based lineage tracing pillar of the field.
- For the [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|synthesis note]]: mtscATAC-seq is **a single-cell joint (DNA mutation, chromatin) assay** — but restricted to mtDNA. It illustrates that joint mutation + epi is *easy* when the DNA target is mtDNA (high-copy, easily captured); the hard case is nuclear point mutations.

## Entities / concepts touched

[[mitochondrial-heteroplasmy]] · [[mitochondrial-lineage-tracing]] · [[scatac-seq]] · [[lineage-tracing]] · [[single-cell-multiomics]] · [[20-Entities/jason-buenrostro]] · [[40-Topics/single-cell-multiomics]]

## Related summaries

- [[10-Summaries/glynos-2023-mtdna-mosaicism]] — Glynos/Chinnery mouse mtDNA heteroplasmy variance, complementary biology.
- [[franco-2024-nature]] — GoT-ChA, alternative single-cell SNV + chromatin (targeted nuclear loci).

---
**Source:** [DOI](https://doi.org/10.1038/s41587-020-0645-6) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32788668/)
