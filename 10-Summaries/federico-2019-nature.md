---
type: summary
title: "Gaiti 2019 — Epigenetic evolution and lineage histories of chronic lymphocytic leukaemia"
source: "[[00-Sources/papers/Epigenetic evolution and lineage histories of chronic lymphocytic leukaemia]]"
aliases: [Gaiti 2019, CLL epimutation, Federico 2019, Landau methylome lineage]
tags: [single-cell-methylation, epimutation, lineage-tracing, CLL, multi-omics, foundational]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Gaiti et al. (2019) — *Epigenetic evolution and lineage histories of chronic lymphocytic leukaemia* — *Nature*. [DOI](https://doi.org/10.1038/s41586-019-1198-z)

# Gaiti et al. 2019 — Epimutation as a molecular clock

> Federico Gaiti, Ronan Chaligne, Hongcang Gu, Ryan M. Brand, Steven Kothen-Hill, Rafael C. Schulman, Kirill Grigorev, Davide Risso, Kyu-Tae Kim, Alessandro Pastore, Kevin Y. Huang, Alicia Alonso, Caroline Sheridan, Nathaniel D. Omans, Evan Biederstedt, Kendell Clement, Lili Wang, Joshua A. Felsenfeld, Erica B. Bhavsar, Martin J. Aryee, John N. Allan, Richard Furman, Andreas Gnirke, Catherine J. Wu, Alexander Meissner\*, **Dan A. Landau\***. *Nature* **569**, 576–580 (23 May 2019). DOI: 10.1038/s41586-019-1198-z.

## Thesis

**Single-cell DNA methylation (epimutation) rate serves as a molecular clock** for reconstructing cell lineage histories at high resolution. Multiplexed scRRBS on 2,652 cells (831 normal B cells + 1,821 CLL cells from 12 patients) shows CLL has **consistently increased epimutation rate with low cell-to-cell variability** — indicating shared replicative history from a common malignant founder. The methylation-based lineage tree shape (earlier branching, faster drift) is consistent with rapid post-malignant-transformation expansion. **Joint scRRBS + scRNA-seq + genotype** integration shows that SF3B1-mutated subclones segregate into distinct methylation-defined clades.

## Method

1. Multiplexed scRRBS protocol — pooled barcoded single-cell libraries.
2. 18 samples: 3 healthy donor B-cell populations (NBC + intMBC + hiMBC + B), 12 CLL patients (7 M-CLL IGHV-mutated, 5 U-CLL unmutated).
3. **Epimutation rate** = proportion of discordant reads (PDR) per CpG per cell — captures cell-to-cell methylation variation.
4. **Four-gamete test** at single-CpG resolution to identify low-epimutation CpGs (likely under active regulatory protection).
5. Joint single-cell DNA methylation + RNA-seq (separate aliquots from same cell, via G&T-seq-style separation) integration on 4 patients.
6. **Maximum-likelihood lineage tree** inferred from methylation-based distances.

## Key claims

- **CLL has higher PDR (~0.28) than normal B cells (~0.20)**, P = 0.0003. Cell-to-cell variability in PDR is *lower* in CLL than normal B → consistent with shared clonal origin.
- Low-epimutation CpGs are enriched at TF binding motifs (SP1, SP2, KLF5, HINFP, NFKB1, MYBL1, NFATC1, FOXC1) → preserved methylation under regulatory selection.
- **Higher epimutation rate ↔ higher transcriptional entropy** in CLL: integrative scDNAme + scRNAseq shows the most epimutation-prone cells also have most expression heterogeneity.
- **Methylation-based lineage trees** of CLL show **earlier branching + rapid drift** vs normal B cells; max tree depth in CLL ~3× normal; Robinson-Foulds distance and patristic distance both elevated.
- **SF3B1-mutated subclones in CLL12** segregate into a distinct methylation clade with estimated emergence at 2,180 ± 219 days (~6 years) before sampling — clonal-evolution timing from methylation alone.
- After ibrutinib treatment, lymphocytosis-displaced cells are preferentially expelled from lymph nodes — methylation lineages identify the displaced subsets.

## Surprising / load-bearing for the review

- **The most explicit demonstration of epigenetic lineage tracing in human disease.** For §4.5 (Lineage Reconstruction), this is the methylation-clock anchor alongside [[mitochondrial-lineage-tracing|mtDNA lineage]] and [[lineage-tracing|CRISPR scar lineage]].
- **Landau-lab provenance**: this paper is from the same group as [[got|GoT]] (2019) and [[got-cha|GoT-ChA]] (2024). Together they establish the Landau lab's "Personalized Cancer Lineage" program — methylation lineage + genotype lineage + chromatin lineage. The review's §4.6 joint-assay coverage benefits from grouping these three Landau papers together.
- The **single-cell SF3B1 subclone timing finding** (~6 years of pre-clinical evolution) is consequential clinically: CLL is genetically silent for years while accumulating methylation drift.

## Entities / concepts touched

[[dna-methylation]] · [[scbs-seq]] · [[lineage-tracing]] · [[clonal-hematopoiesis]] · [[20-Entities/dan-a-landau]] · [[20-Entities/landau-lab]] · [[20-Entities/alexander-meissner]] · [[40-Topics/dna-methylation]] · [[40-Topics/hematopoietic-malignancies]]

## Related summaries

- [[anna-2019-nature]] — GoT, same Landau lab, contemporaneous methods development.
- [[franco-2024-nature]] — GoT-ChA, same Landau lab, joint genotype + chromatin.
- [[hongshan-2013-genomeresearch]] — scRRBS predecessor.

---
**Source:** [DOI](https://doi.org/10.1038/s41586-019-1198-z) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/31092926/)
