---
type: summary
title: "Heumos 2023 — Best practices for single-cell analysis across modalities"
source: "[[00-Sources/papers/Best practices for single-cell analysis across modalities]]"
aliases: ["Heumos 2023 best practices", "single-cell best practices NRG"]
tags: [best-practices, scRNA-seq, scATAC-seq, multimodal, doublet-detection, normalization, Theis-lab, Helmholtz-Munich]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/Best practices for single-cell analysis across modalities]]"
---

**Citation:** Heumos et al. (2023) — *Best practices for single-cell analysis across modalities* — *Nature Reviews Genetics*. [DOI](https://doi.org/10.1038/s41576-023-00586-w)

Heumos, Schaar, Lance et al. (Theis lab; Helmholtz Munich + TU Munich) compiled "best practices" recommendations for unimodal and multimodal single-cell analysis. Synthesizes independent benchmarking studies into comprehensive workflows: scRNA-seq (raw counts → high-quality cellular data via ambient-RNA removal with SoupX/CellBender, doublet detection with scDblFinder, normalization, variance stabilization), chromatin accessibility, surface protein, adaptive immune receptor (TCR/BCR) repertoires, spatial. Includes a companion online "Single-Cell Best Practices" book with 50+ chapters. Functions as an entry-point for novices and a current-practice guide for advanced users.

## Why this matters

The standard 2023 community-consensus best-practices reference for analysis workflows. Cite when describing analysis pipelines in §4 — especially for the scRNA arm of multimodal data — because individual tool citations are too granular. Companion to Vandereyken 2023 (NRG) which covers methods/applications, and Baysoy 2023 (NRMCB) which covers technology landscape. Useful for §6 limitations when discussing analysis-tool fragmentation.

---
**Source:** [DOI](https://doi.org/10.1038/s41576-023-00586-w) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37002403/)

---
**Source:** [DOI](https://doi.org/10.1038/s41576-023-00586-w) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37002403/)

## Related

- [[10-Summaries/vandereyken-2023-scmultiomics-review]]
- [[10-Summaries/baysoy-2023-multiomics-landscape]]
- [[10-Summaries/xiao-2024-multiomics-benchmark]]
- [[10-Summaries/luo-2024-scatac-benchmark]]
