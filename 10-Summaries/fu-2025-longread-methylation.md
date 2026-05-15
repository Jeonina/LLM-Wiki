---
type: summary
title: "Fu 2025 — Computational analysis of DNA methylation from long-read sequencing"
aliases: ["Fu 2025 review", "long-read methylation computational review"]
tags: [review, DNA-methylation, long-read-sequencing, PacBio, ONT, computational-analysis, Sedlazeck-lab, Timp-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Yilei_2025_NatureReviewsGenetics.pdf"]
---

**Citation:** Fu et al. (2025) — *Computational analysis of DNA methylation from long-read sequencing* — *Nature Reviews Genetics*. [DOI](https://doi.org/10.1038/s41576-025-00822-5)

Fu, Timp and Sedlazeck (Baylor + Johns Hopkins + Rice) reviewed computational methods for DNA methylation analysis from long-read sequencing. Covers: (i) raw-signal-to-methylation calling (PacBio kinetic features via pulse width + interpulse duration; ONT current via HMMs and CNNs); (ii) detection of 5mC, 5hmC, 4mC, 6mA; (iii) sample comparison (DMR calling, longitudinal change); (iv) integration with structural variants, tandem repeats, and complex genomic regions where short-read bisulfite alignment fails; (v) cell-type diversity analysis from long-read methylation. Surveys tools including Nanopolish, DeepMod, DeepSignal, Megalodon, modkit, and the new generation of CNN-based callers.

## Why this matters

Critical §3.3 methodology reference for the long-read methylation arm — complementary to short-read bisulfite (Krueger Bismark 2011) and SMF (SMAC-seq/Fiber-seq family). Long-read methylation calling is the technical foundation for nanoNOMe, Fiber-seq, scNanoCOOL-seq, and any application that combines methylation with structural variation. Useful when arguing that scDNA-seq is moving toward long-read native modification calling (avoiding bisulfite damage).

---
**Source:** [DOI](https://doi.org/10.1038/s41576-025-00822-5) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/40155770/)

## Related

- [[10-Summaries/krueger-2011-bismark]]
- [[10-Summaries/lee-2020-nanonome]]
- [[10-Summaries/shipony-2020-smac]]
- [[10-Summaries/iqbal-2023-methylome-review]]
- [[30-Concepts/long-read-methylation-calling]]
