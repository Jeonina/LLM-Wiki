---
type: summary
title: "De Rop 2024 — Systematic benchmarking of single-cell ATAC-sequencing protocols (PUMATAC)"
source: "[[00-Sources/papers/Systematic benchmarking of single-cell ATAC-sequencing protocols]]"
source_quality: full
source_sha256: "5611cddf2a34a5d82ef82abbeceae099cbefc9022286b2bd9f06e423e2aea05d"
aliases: ["De Rop 2024", "PUMATAC benchmark", "scATAC-seq benchmark"]
tags: [scATAC-seq, benchmarking, computational, PBMC, PUMATAC, Aerts-lab, Heyn-lab]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** De Rop et al. (2024) — *Systematic benchmarking of single-cell ATAC-sequencing protocols (PUMATAC)* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-023-01881-x)

> [!abstract] 한눈에
> De Rop 등은 PBMC를 기준 시료로 8개 scATAC-seq 프로토콜을 47개 실험에서 비교하고 공통 전처리 파이프라인 PUMATAC을 공개했다. 라이브러리 복잡도와 tagmentation 특이성이 방법마다 달라 annotation과 peak calling 등 하위 분석이 영향을 받았고, 세포당 비용은 HyDrop이 가장 낮았다.

De Rop, Hulselmans, Flerin and colleagues (Aerts + Heyn labs) systematically benchmarked eight scATAC-seq protocols — 10x Genomics v1/v1.1/v2/multiome/mtscATAC, Bio-Rad ddSEQ, HyDrop, and s3-ATAC — across 47 experiments using PBMCs as a reference sample. The study developed PUMATAC, a universal preprocessing pipeline for scATAC-seq, which corrects for barcode-merging artifacts (especially in Bio-Rad data), unifies read alignment via bwa-mem2, and feeds into cisTopic-based clustering.

Three findings. (1) Significant differences in sequencing library complexity and tagmentation specificity exist across methods, with downstream consequences for cell-type annotation, genotype demultiplexing, peak calling, differential accessibility, and TF motif enrichment. (2) Per-cell cost is lowest for HyDrop (5× cheaper than Bio-Rad ddSEQ, 10× cheaper than 10x v2) and highest for s3-ATAC; 10x multiome costs 1.5× more than 10x v2 and is markedly less sensitive. (3) PUMATAC and the 169,000-cell PBMC benchmark dataset are released as a community resource.

## Why this matters

The first systematic benchmarking of scATAC-seq protocols against shared standards. Anchors §3.2 (chromatin accessibility) and §4 (computational framework) by providing the methods-comparison context that prior reviews (Klemm 2019, Baysoy 2023) lacked. Critical for any scATAC-seq experimental-design decision.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-023-01881-x) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37537502/)

## Related

- [[30-Concepts/scatac-seq]]
- [[10-Summaries/klemm-2019-chromatin-accessibility-review]]
- [[10-Summaries/granja-2021-archr]]
- [[10-Summaries/stuart-2021-natmethods]]
