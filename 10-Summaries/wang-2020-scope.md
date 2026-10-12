---
type: summary
title: "Wang 2020 — SCOPE: normalization and copy-number estimation for scDNA-seq"
source: "[[00-Sources/papers/SCOPE_ A Normalization and Copy-Number Estimation Method for Single-Cell DNA Sequencing]]"
source_quality: full
source_sha256: "4a0ac34c6f75aee0ca98991617d4ccaf6838cde95cd6373fe4a46057f554e2f1"
aliases: ["Wang Jiang 2020 SCOPE", "SCOPE"]
tags: [SCOPE, scDNA-seq, CNV-calling, normalization, EM-algorithm, ploidy-estimation, Jiang-lab, UNC]
created: 2026-05-13
updated: 2026-10-12
---

**Citation:** Wang et al. (2020) — *SCOPE: normalization and copy-number estimation for scDNA-seq* — *Cell Systems*. [DOI](https://doi.org/10.1016/j.cels.2020.03.005)

> [!abstract] 한눈에
> SCOPE는 Poisson latent factor model과 정상 diploid 대조 세포를 이용해 희소하고 노이즈가 많은 scDNA-seq 데이터를 정규화하고, EM으로 ploidy를 직접 추정하며 세포 간 공통 breakpoint를 분할하는 CNV 추정 방법이다. diploid 기준선을 가정하는 Ginkgo가 실패하는 경우에도 subclone 구조를 복원했다.

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
- [[10-Summaries/wesley-2026-songbird]] — on a DLP+ ploidy ladder, SCOPE called 2× and 3× hTERT wells as copy number 2.
- scDNA CNV calling
