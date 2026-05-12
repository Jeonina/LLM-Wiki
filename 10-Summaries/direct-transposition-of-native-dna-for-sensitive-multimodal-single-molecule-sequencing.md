---
type: summary
title: "Nanda et al. 2024 — SMRT-Tag and SAMOSA-Tag: tagmentation for PacBio at 40 ng input"
source: "[[00-Sources/papers/Direct transposition of native DNA for sensitive multimodal single-molecule sequencing]]"
source_kind: paper
author: "Arjun S. Nanda, Ke Wu, Iryna Irkliyenko, Brian Woo, Megan S. Ostrowski, Andrew S. Clugston, Leanne C. Sayles, Lingru Xu, Ansuman T. Satpathy, Hao G. Nguyen, E. Alejandro Sweet-Cordero, Hani Goodarzi, Sivakanthan Kasinathan, Vijay Ramani (corresponding)"
published: 2024-05-09
ingested: 2026-05-12
doi: "10.1038/s41588-024-01748-0"
journal: "Nature Genetics"
tags: [PacBio, tagmentation, low-input, SMRT-Tag, SAMOSA-Tag, single-molecule, chromatin-accessibility, prostate-cancer-PDX]
entities:
  - "[[20-Entities/vijay-ramani]]"
  - "[[20-Entities/arjun-nanda]]"
  - "[[20-Entities/sivakanthan-kasinathan]]"
concepts:
  - "[[30-Concepts/smrt-tag]]"
  - "[[30-Concepts/samosa-tag]]"
  - "[[30-Concepts/samosa]]"
  - "[[30-Concepts/pacbio]]"
  - "[[30-Concepts/tn5-tagmentation]]"
  - "[[30-Concepts/single-molecule-footprinting]]"
  - "[[30-Concepts/fiber-seq]]"
topics:
  - "[[40-Topics/long-read-sequencing]]"
  - "[[40-Topics/single-cell-multiomics]]"
  - "[[40-Topics/chromatin-architecture]]"
---

# Nanda et al. 2024 — SMRT-Tag / SAMOSA-Tag

> Thesis: PacBio single-molecule sequencing needs 1–5 µg of DNA (150,000–750,000 cells) for PCR-free library prep — far too much for clinical biopsies, rare cell populations, or single cells. **SMRT-Tag** uses Tn5 tagmentation with hairpin PacBio adapters to make exonuclease-resistant circular molecules from as little as 40 ng (~7,000 cells), at near-equivalent variant-calling and CpG-methylation accuracy to gold-standard ligation-based PacBio. **SAMOSA-Tag** adds in-nucleus EcoGII methyltransferase footprinting to layer single-fiber chromatin accessibility onto the same workflow — applied to prostate-cancer patient-derived xenografts (PDXs) to uncover metastasis-associated global chromatin disorganization from 30–50k nuclei.

## Key claims

- **SMRT-Tag method**: Tn5 with hairpin PacBio adapters (uracil-containing) → tagmentation → gap repair (Phusion + Taq ligase, the optimal pair of 62 tested) → exonuclease digestion to enrich circular molecules → PacBio HiFi sequencing. **Adjustable fragment size** (2–6 kb) via Tn5:DNA ratio and temperature.
- **Genetic + epigenetic calling at 40 ng input**: SNV/indel/SV F1 scores comparable to ligation-based PacBio at matched coverage (e.g., 0.566 vs 0.664 for SNVs at low coverage; 0.983 vs 0.982 at 11.2× coverage). CpG methylation Pearson r=0.84 with bisulfite reference; AUC 0.935.
- **SAMOSA-Tag method**: in-nucleus EcoGII methylation (6mA marks accessible regions) + Tn5 hairpin tagmentation. Detects sequence + 5mC (CpG) + 6mA (accessibility) on the same PacBio fiber.
- **Prostate-cancer PDX application** (50,000 nuclei): single-fiber CTCF and nucleosome footprints; CpG methylation reduced inside CTCF motifs (consistent with CTCF binding); identifies metastasis-associated **global chromatin disorganization** that bulk ATAC-seq misses.
- Tagmentation produces oligonucleosomal-banding fragment size distribution — consistent with cuts adjacent to nucleosome barriers in the chromatin substrate.

## Methods / evidence

PacBio Sequel II/IIe. Tn5 triple-mutant for size tunability. Phusion/Taq vs T4/Ampligase gap-repair benchmark. HG002/3/4 trio for variant-calling validation; bisulfite-seq for methylation reference. OS152 osteosarcoma cells + mouse ESCs + prostate cancer PDXs for SAMOSA-Tag.

## Surprising or load-bearing bits

- **90–99% input reduction** for PacBio chromatin profiling: brings single-molecule methods within range of clinical samples and rare populations.
- The **circularization-by-hairpin-adapters** strategy adapts Tn5 (a short-read tool) to a long-read platform — clever cross-pollination. Note that DAF-seq ([[10-Summaries/elliott-2025-naturebiotechnology]]) uses a different chemistry (DddA deamination) for the same long-read-low-input goal.
- SAMOSA-Tag bridges chromatin biology and clinical genomics — the **prostate-cancer PDX result** is the proof-of-clinical-relevance application.

## Connections to other sources

- Direct extension of SAMOSA (Battaglia et al., Ramani lab) and Fiber-seq (Stergachis lab; see [[30-Concepts/fiber-seq]]).
- Conceptually parallel to [[10-Summaries/elliott-2025-naturebiotechnology]] (DAF-seq / scDAF-seq, Stergachis 2025) — both achieve low-input PacBio chromatin profiling but DAF-seq uses chemical deamination (amplifiable) and DAF-seq goes to single cells while SAMOSA-Tag is bulk-nuclei.
- Fits in the broader long-read epigenomics framework reviewed by [[10-Summaries/profiling-the-epigenome-using-long-read-sequencing]] (Liu/Conesa 2025).

## Open questions

- Single-cell SMRT-Tag/SAMOSA-Tag not yet demonstrated. The 40 ng floor still requires thousands of nuclei.
- SV calling F1 score at low coverage (0.225) lags ligation-based PacBio (0.389) due to shorter SMRT-Tag reads — SV calling needs full-length spanning reads.

## Related

- [[40-Topics/long-read-sequencing]] · [[30-Concepts/smrt-tag]] · [[30-Concepts/samosa-tag]] · [[30-Concepts/single-molecule-footprinting]]
