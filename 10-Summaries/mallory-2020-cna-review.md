---
type: summary
title: "Mallory 2020 — Assessing the performance of methods for copy number aberration detection from single-cell DNA sequencing data"
source: "[[00-Sources/papers/Methods for copy number aberration detection from single-cell DNA-sequencing data]]"
source_quality: full
source_sha256: "31f1a93b00056820f79a526b9ddc291051543a805b5dec097a1ccb6f838d6192"
aliases: ["Mallory 2020 review", "scDNA CNA methods review", "Nakhleh CNA review"]
tags: [review, CNA-detection, scDNA-seq, segmentation, tumor-evolution, Nakhleh-lab, Rice, Navin-lab]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Mallory et al. (2020) — *Assessing the performance of methods for copy number aberration detection from single-cell DNA sequencing data* — *PLOS Computational Biology* 16(7):e1008012. [DOI](https://doi.org/10.1371/journal.pcbi.1008012)

Mallory, Edrisi, Navin and Nakhleh (Rice, MD Anderson) reviewed eight methods for detecting copy-number aberrations (CNAs) from scDNA-seq data, categorizing them along a seven-step pipeline: (1) binning, (2) GC correction, (3) mappability correction, (4) removal of outlier bins, (5) removal of outlier cells, (6) segmentation, (7) absolute copy-number calling. The review covers HMMcopy, AneuFinder, Ginkgo, SCNV, CopyNumber, SCOPE, CHISEL, and SCICoNE.

Three segmentation paradigms compared: (i) **sliding-window**: statistical testing for windows whose read counts differ from the rest of the genome; (ii) **objective-function** approaches (e.g., Ginkgo's circular binary segmentation); (iii) **hidden Markov models**: probabilistic state inference per bin. The review also discusses ploidy-handling (most methods assume diploid baseline — problematic for tumor data with WGD or aneuploidy), evaluation strategies in the absence of ground truth, and downstream phylogenetic inference from CNA profiles.

## Why this matters

The canonical review for the §4 CNA-detection tool family. Important supplement: this review covers CHISEL (then a preprint) but pre-dates the published CHISEL (Zaccaria 2021), MEDICC2 (Kaufmann 2022), and DLP+/laks-style ultra-low-coverage methods that defined post-2020 practice. So our review should treat Mallory 2020 as the foundational survey AND note the post-publication developments. Anchors §4 (CNA-detection tools) and §5 (cancer applications). Provides the seven-step framework that we may adopt for the §4 organization.

---
**Source:** [DOI](https://doi.org/10.1371/journal.pcbi.1008012) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32658894/)

---
**Source:** [DOI](https://doi.org/10.1186/s13059-020-02119-8) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32807205/)

## Related

- [[10-Summaries/zaccaria-2021-chisel]]
- [[10-Summaries/kaufmann-2022-medicc2]]
- laks 2019 cell
- [[40-Topics/scdna-cancer-applications]]
- [[20-Entities/nicholas-navin]]
