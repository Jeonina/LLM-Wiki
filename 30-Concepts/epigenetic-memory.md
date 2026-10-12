---
type: concept
title: Epigenetic memory
aliases: [cellular memory, methylation memory]
tags: [methylation, stem-cells, cancer, iPSC, inheritance]
created: 2026-05-12
updated: 2026-10-12
---

# Epigenetic memory

> The mitotically heritable record of past cellular states encoded in DNA methylation, histone modifications, and chromatin organization. Cells "remember" their developmental history, tissue of origin, and exposure history even after dedifferentiation or reprogramming ([[10-Summaries/kim-2017-methylation-memory-review|Kim 2017]]).

> [!abstract] 한눈에
> Epigenetic memory는 DNA methylation과 chromatin 상태로 세포가 과거의 발생 이력과 기원 조직을 분열 후에도 기억하는 현상이다 ([[10-Summaries/kim-2017-methylation-memory-review|Kim 2017]]). Lineage barcode를 정답으로 쓴 mouse HSC 실험에서는 같은 clone끼리 유전자 발현보다 CpG methylation이 훨씬 더 비슷했다 ([[10-Summaries/li-2023-darlin|DARLIN]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 DNA methylation](../60-Explainers/dna-methylation.html)
<!-- /explainer-links -->

## Definition

Memory is enforced by **maintenance machinery**: DNMT1+UHRF1 at the replication fork, polycomb (H3K27me3) and trithorax (H3K4me3) systems, heterochromatin self-templating. Stable but not absolute: extended reprogramming or cancer-associated remodeling can erase memory partially.

## Why it matters

- **iPSCs retain methylation signatures** of donor cells and preferentially differentiate back toward original lineage ([[10-Summaries/kim-2017-methylation-memory-review|Kim 2017]]).
- **Cancer cells retain methylation** of their tissue of origin even at metastatic sites — enables [[30-Concepts/cancer-of-unknown-primary]] tissue classification by methylation pattern (EPICUP).
- **MSCs** show methylation patterns that reflect their cell type of origin and remain stable through long-term culture, a quality-control marker ([[10-Summaries/kim-2017-methylation-memory-review|Kim 2017]]).

## Evidence and examples

- With CRISPR lineage barcodes as ground truth, clonally related mouse HSCs were significantly more similar in genome-wide CpG methylation (p = 1.2 × 10⁻¹⁰; 19 of 21 clones individually significant) but barely or not at all in gene expression (p = 0.049) or GpC accessibility (p = 0.34) ([[10-Summaries/li-2023-darlin|DARLIN]]).
- The 279 clone-differential CpG regions were not near differentially regulated genes or GO-enriched, which the authors read as random loci ([[10-Summaries/li-2023-darlin|DARLIN]]).
- This complements the earlier finding that sister cells share fate bias not visible in scRNA-seq ([[10-Summaries/weinreb-2020-larry|LARRY]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/dnmt|DNMT]] — DNA methyltransferases that write and maintain methylation.
> - `concept` [[30-Concepts/cancer-of-unknown-primary|Cancer of unknown primary]] — Tissue-of-origin classification from retained methylation.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — Methylation chemistry, assays and single-cell readouts.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/kim-2017-methylation-memory-review|Kim & Costello 2017]]
> - [[10-Summaries/li-2023-darlin|Li 2023]]
> - [[10-Summaries/weinreb-2020-larry|Weinreb 2020]]
