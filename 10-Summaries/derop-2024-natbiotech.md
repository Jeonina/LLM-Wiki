---
type: summary
title: "De Rop 2024 — Systematic benchmarking of single-cell ATAC-sequencing protocols (PUMATAC)"
source: "[[00-Sources/papers/Systematic benchmarking of single-cell ATAC-sequencing protocols]]"
aliases: ["De Rop 2024", "PUMATAC benchmark", "scATAC-seq benchmark"]
tags: [scATAC-seq, benchmarking, computational, PBMC, PUMATAC, Aerts-lab, Heyn-lab]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** De Rop et al. (2024) — *Systematic benchmarking of single-cell ATAC-sequencing protocols (PUMATAC)* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-023-01881-x)

De Rop, Hulselmans, Flerin and colleagues (Aerts + Heyn labs) systematically benchmarked eight scATAC-seq protocols — 10x Genomics v1/v1.1/v2/multiome/mtscATAC, Bio-Rad ddSEQ, HyDrop, and s3-ATAC — across 47 experiments using PBMCs as a reference sample. The study developed PUMATAC, a universal preprocessing pipeline for scATAC-seq, which corrects for barcode-merging artifacts (especially in Bio-Rad data), unifies read alignment via bwa-mem2, and feeds into cisTopic-based clustering.

Three findings. (1) Significant differences in sequencing library complexity and tagmentation specificity exist across methods, with downstream consequences for cell-type annotation, genotype demultiplexing, peak calling, differential accessibility, and TF motif enrichment. (2) Per-cell cost varies from $0.05 (HyDrop) to $3.80 (s3-ATAC) at fixed cell yields, with 10x v2/multiome and HyDrop offering favorable cost/quality trade-offs. (3) PUMATAC and the 169,000-cell PBMC benchmark dataset are released as a community resource.

## Why this matters

The first systematic benchmarking of scATAC-seq protocols against shared standards. Anchors §3.2 (chromatin accessibility) and §4 (computational framework) by providing the methods-comparison context that prior reviews (Klemm 2019, Baysoy 2023) lacked. Critical for any scATAC-seq experimental-design decision.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-023-01881-x) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37537502/)

## Related

- [[30-Concepts/scatac-seq]]
- [[10-Summaries/sandy-2019-naturereviewsgenetics]]
- [[10-Summaries/jeffrey-2021-naturegenetics]]
- [[10-Summaries/stuart-2021-natmethods]]
