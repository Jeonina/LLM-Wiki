---
type: summary
title: "Wang 2020 — SCOPE: normalization and copy-number estimation for scDNA-seq"
aliases: ["Wang Jiang 2020 SCOPE", "SCOPE"]
tags: [SCOPE, scDNA-seq, CNV-calling, normalization, EM-algorithm, ploidy-estimation, Jiang-lab, UNC]
created: 2026-05-13
updated: 2026-05-13
sources: ["Rujin_2020_CellSystems.pdf"]
---

**Citation:** Wang et al. (2020) — *SCOPE: normalization and copy-number estimation for scDNA-seq* — *Cell Systems*. [DOI](https://doi.org/10.1016/j.cels.2020.03.005)

Wang, Lin and Jiang (UNC Chapel Hill) developed **SCOPE**, a normalization and copy-number estimation method for sparse, noisy scDNA-seq data. Three key features: (i) a **Poisson latent factor model** for normalization that borrows information across cells and genomic regions, using in-silico-identified negative-control diploid cells to estimate bias; (ii) an **EM algorithm embedded in normalization** that accounts for aberrant copy-number states and directly estimates ploidy without post-hoc adjustment; (iii) **cross-sample segmentation** to identify breakpoints shared across cells with the same genetic background. Benchmarked on cancer-genomics scDNA-seq datasets, SCOPE produces accurate copy-number estimates and recovers subclonal structure where Ginkgo and SCNV (which assume diploid baselines) fail.

## Why this matters

A §4 computational-tools anchor in the scDNA-seq CNV-calling family alongside Ginkgo, HMMcopy, AneuFinder, CHISEL (Zaccaria 2021), and the more recent MEDICC2 (Kaufmann 2022). SCOPE addresses the specific failure mode that bias-correction methods can over-correct ploidy in aneuploid tumors. Important when discussing CNV-calling methodology in §4 cancer applications.

---
**Source:** [DOI](https://doi.org/10.1016/j.cels.2020.03.005) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32437686/)

---
**Source:** [DOI](https://doi.org/10.1016/j.cels.2020.03.005) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32437686/)

## Related

- [[10-Summaries/zaccaria-2021-chisel]]
- [[10-Summaries/kaufmann-2022-medicc2]]
- [[10-Summaries/lu-2024-cnaphylogeny-review]]
- [[10-Summaries/mallory-2020-cna-review]]
- [[30-Concepts/scDNA-CNV-calling]]
