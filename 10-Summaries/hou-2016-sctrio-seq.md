---
type: summary
title: "Hou 2016 — scTrio-seq: Triple omics (CNV + methylome + transcriptome) in single hepatocellular carcinoma cells"
source: "[[00-Sources/papers/Single-cell triple omics sequencing reveals genetic, epigenetic, and transcriptomic heterogeneity in hepatocellular carcinomas]]"
aliases: [Hou 2016, scTrio-seq]
tags: [scTrio-seq, joint-assay, triple-omics, single-cell-multiomics, scRRBS, CNV, hepatocellular-carcinoma, foundational]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Hou et al. (2016) — *scTrio-seq: Triple omics (CNV + methylome + transcriptome) in single hepatocellular carcinoma cells* — *?*. [DOI](https://doi.org/10.1038/cr.2016.23)

# Hou et al. 2016 — scTrio-seq

> Yu Hou, Huahu Guo, Chen Cao, Xianlong Li, Boqiang Hu, Ping Zhu, Xinglong Wu, Lu Wen, Fuchou Tang, Yanyi Huang, Jirun Peng. *Cell Research* **26**, 304–319 (Feb 2016). DOI: 10.1038/cr.2016.23.

## Thesis

First single-cell **triple-omics** assay that simultaneously yields (1) genomic copy-number variation, (2) DNA methylome, and (3) transcriptome from the same mammalian cell — and the first demonstration that **CNVs drive proportional changes in RNA expression but do NOT alter DNA methylation** within the same affected genomic regions, at single-cell resolution. Applied to 25 HCC tumor cells from one patient, identifying two subpopulations differentiated by CNV, methylation, and expression profiles concordantly.

## Mechanism

1. **Mild lysis** of cytoplasm only — keeps nucleus intact.
2. Centrifuge: **supernatant (mRNA) → scRNA-seq** (Tang-lab pipeline); **pellet (nucleus) → scRRBS** (single-cell Reduced Representation Bisulfite Sequencing).
3. CNV deduced from the scRRBS read distribution (after normalization against normal-liver-RRBS reference and HMM fitting) at 10-Mb resolution. The methylation arm doubles as the CNV signal because RRBS recovers >100,000 unique MspI fragments per cell.
4. Output per cell: ~1.5M CpGs, 6,179 genes, CNV map at 10-Mb resolution.

## Key claims

1. **HepG2 benchmarking**: scTrio-seq methylome levels and patterns match standard scRRBS; gene-expression detection matches standard scRNA-seq; CNV calls at 10-Mb resolution match bulk genome sequencing and SNP array.
2. **Promoter methylation ↔ expression**: negatively correlated within single cells (replicates bulk knowledge).
3. **Gene-body methylation ↔ expression**: positively correlated, increasing toward 3′. **First global demonstration of this relationship in single cells.**
4. **CNV ↔ expression**: Pearson r ≈ 0.68 ± 0.07 in HepG2, ≈ 0.73 ± 0.04 in HCC cells. **CNVs drive proportional expression dosage at single-cell resolution.**
5. **CNV ↔ methylation**: r ≈ 0.05 ± 0.02 — i.e., **no relationship**. Copy-number gains/losses do not directly perturb the methylation level of the affected regions. This is a key biological finding only visible because all three layers are in the same cell.
6. **HCC subpopulations**: 25 patient HCC cells split into two clusters by CNV, by methylation, and by transcriptome — all three modalities give *identical* clusterings. Subpopulation I (minor fraction) carries extra copies of chr 8, 11, 20; expresses invasion markers; downregulates complement / innate-immunity genes (likely immune-evasive).
7. **Locus-level integration**: ANO1 (gene-body hypomethylated, lower expression in subpop I) and S100A11 (promoter-hypomethylated, higher expression in subpop I) — direct demonstration that DMR context (gene body vs promoter) flips the sign of the methylation→expression relationship at individual loci.

## Surprising / load-bearing

- **The mosaicism × epigenetics × DNA-centric novelty PI is pushing for is exactly this paper's framing.** scTrio-seq is the closest existing precedent for "mutation + epi + DNA-centric at single-cell resolution" — except it uses CNV instead of point mutations, and it's tumor-only. The wiki's somatic-mosaicism + epi synthesis can lean on this paper as the methodological proof-of-concept that all three layers can be jointly read.
- **Methylation arm doing double duty for CNV** is a clever piece of design that means scTrio-seq is *cheaper* than scNMT-seq for the layers it provides — but it pays for that with no chromatin accessibility (scNMT-seq has that instead of CNV).
- For §4.6 of the review, scTrio-seq is the **triple-omics anchor** alongside scNMT-seq. The contrast (CNV vs accessibility) is the key axis to articulate.

## Entities / concepts touched

[[scdna-seq]] · [[scbs-seq]] · [[dna-methylation]] · [[single-cell-multiomics]] · [[cpg-island]] · [[mutational-signatures]] · [[20-Entities/xiaoying-fan]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/dna-methylation]]

## Related summaries

- [[scnmt-seq-enables-joint-profiling-of-chromatin-accessibility-dna-methylation-and-transcription-in-single-cells]] — alternative triple-omics with accessibility instead of CNV.
- [[g-t-seq-parallel-sequencing-of-single-cell-genomes-and-transcriptomes]] — DNA+RNA joint, predecessor in DNA-anchored chemistry.
- [[high-throughput-single-cell-dna-methylation-and-chromatin-accessibility-co-profiling-with-splicool-seq]] — SpliCOOL-seq, later scaled DNA-methylation + accessibility co-assay.

---
**Source:** [Open paper](https://www.nature.com/articles/cr201623)
