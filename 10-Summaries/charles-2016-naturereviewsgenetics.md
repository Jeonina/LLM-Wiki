---
type: summary
title: "Gawad, Koh & Quake 2016 — Single-cell genome sequencing: current state of the science"
source: "[[00-Sources/papers/Single-cell genome sequencing_ current state of the science]]"
source_kind: paper
author: "Charles Gawad, Winston Koh, Stephen R. Quake"
published: 2016-03
ingested: 2026-05-11
doi: "10.1038/nrg.2015.16"
journal: "Nature Reviews Genetics 17:175–188"
tags: [review, scDNA-seq, scWGA, microbial-genomics, cancer, foundational-review]
entities:
  - "[[20-Entities/charles-gawad]]"
  - "[[20-Entities/stephen-quake]]"
concepts:
  - "[[30-Concepts/scdna-seq]]"
  - "[[30-Concepts/scwga]]"
  - "[[30-Concepts/mda]]"
  - "[[30-Concepts/malbac]]"
  - "[[30-Concepts/dop-pcr]]"
  - "[[30-Concepts/somatic-mosaicism]]"
topics:
  - "[[40-Topics/scdna-seq]]"
  - "[[40-Topics/whole-genome-amplification]]"
---

**Citation:** Gawad et al. (2016) — *Single-cell genome sequencing: current state of the science* — *Nature Reviews Genetics*. [DOI](https://doi.org/10.1038/nrg.2015.16)

# Gawad, Koh & Quake 2016 — Single-cell genome sequencing: current state of the science

> Thesis: single-cell genomics rests on four technical pillars — cell isolation, whole-genome amplification (WGA), genome interrogation, and bias correction — and the field circa 2016 had reached the point where microbial dark matter and intra-tumor heterogeneity were tractable, but each WGA method (DOP-PCR / MDA / MALBAC / PicoPLEX) involved hard tradeoffs between coverage, uniformity, and error rate.

## Key claims

- **Four technical challenges** of single-cell genomics: (1) physical cell isolation, (2) WGA to acquire sufficient DNA, (3) cost-effective genome interrogation, (4) bias/error correction.
- **Three WGA categories** (Fig 2):
  - **Pure PCR (DOP-PCR)**: low coverage, low non-uniformity, high false-positive rate.
  - **Isothermal (MDA / Φ29)**: high coverage, high non-uniformity, low false-positive rate.
  - **Hybrid (MALBAC, PicoPLEX)**: intermediate coverage, low non-uniformity, intermediate false-positive rate.
- **No clear winner** — method choice depends on application (CNV detection favors uniform methods; SNV detection favors high-coverage methods).
- **Errors during scWGA**: loss of coverage, decreased coverage uniformity, allelic imbalance, allelic dropout (ADO), amplification errors, chimeras.
- **SNV calling strategies**: use bulk sample as reference; require 2-3 cells to share a variant; molecular barcoding.
- **Clonal structure determination** from single-cell data: distance-based (Jaccard) or model-based (mixture models with EM) clustering.
- **Two major applications classes**: (a) microbial "dark matter" (TM7, OP11, TM6, SR1 phyla — previously unculturable, now genome-assembled from single cells), (b) intra-tumor heterogeneity in cancer.
- **Microfluidics dramatically reduce contamination and improve uniformity** of WGA reactions vs traditional tube-volume reactions.

## Methods / evidence

Synthesizing review with extensive comparison tables across published single-cell cancer studies (Table 1) including isolation method, WGA method, cells passed QC, regions sequenced, false-positive rate, coverage breadth, ADO rate, false-negative rate.

## Surprising or load-bearing bits

- **The asymmetry between SNV and CNV detection requirements** — uniformity for CNVs, coverage for SNVs — is why no single WGA method is universally best. This drove the field toward hybrid methods (MALBAC) and ultimately to [[30-Concepts/pta]] in [[10-Summaries/diane-2025-naturereviewsgenetics]], which approaches both ends of the tradeoff.
- **Microbial dark matter** (TM7 etc.): the conceptual breakthrough that genome assembly of unculturable bacteria is possible through single-cell sequencing of clinically-obtained samples. This application class is largely absent from the [[10-Summaries/diane-2025-naturereviewsgenetics]] update — current scDNA-seq is dominated by mosaicism and lineage tracing in human tissues.
- **Quake-Gawad benchmarking** of MDA vs MALBAC at the *E. coli* single-cell level — found microfluidics-volume MDA and MALBAC had comparable bias; in microliter volumes MDA bias depended on gain while MALBAC was gain-independent.

## Entities mentioned

- [[20-Entities/charles-gawad]] — first author; now PI at St Jude.
- [[20-Entities/stephen-quake]] — senior author; Stanford bioengineering / HHMI; co-developed microfluidic single-cell genomics.

## Concepts touched

- [[30-Concepts/scdna-seq]] — foundational review of the field.
- [[30-Concepts/scwga]], [[30-Concepts/mda]], [[30-Concepts/malbac]], [[30-Concepts/dop-pcr]] — the 2016 method landscape.
- [[30-Concepts/somatic-mosaicism]] — cancer applications.

## Connections to other sources

- **Updated and effectively superseded by** [[10-Summaries/diane-2025-naturereviewsgenetics]] — the 2025 review covers PTA, duplex sequencing, and computational advances that didn't exist in 2016.
- **Methodological grandparent of** [[10-Summaries/anna-2019-nature]] (GoT) — though GoT is targeted genotyping rather than scWGA, it is also a Quake-era droplet-platform innovation.
- **Mosaicism framing inherited by** [[10-Summaries/lars-2017-naturereviewsgenetics]] and [[10-Summaries/ian-2015-trendsingenetics]].

## Open questions

- (At time of writing) — how to scale to thousands of cells without sacrificing per-cell quality. Largely answered by [[30-Concepts/dlp-plus]] and droplet ATAC-style platforms in subsequent years.
- Standardization of QC and ADO definitions across studies — flagged by Gawad/Quake here, still partly unresolved in 2025.

---
**Source:** [DOI](https://doi.org/10.1038/nrg.2015.16)
