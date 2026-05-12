---
type: summary
title: "Mezger et al. 2018 — µATAC-seq: 5,184 nano-wells, ~1,800 cells/chip, $0.81/cell"
source: "[[00-Sources/papers/High-throughput chromatin accessibility profiling at single-cell resolution]]"
source_kind: paper
author: "Anja Mezger, Sandy Klemm, Ishminder Mann, Kara Brower, Alain Mir, Magnolia Bostick, Andrew Farmer, Polly Fordyce, Sten Linnarsson, William Greenleaf (corresponding)"
published: 2018-09-07
ingested: 2026-05-12
doi: "10.1038/s41467-018-05887-x"
journal: "Nature Communications"
tags: [scATAC-seq, nanowell, ICELL8, throughput, fluorescence-imaging, PBMC, Greenleaf-lab, Klemm]
entities:
  - "[[20-Entities/william-greenleaf]]"
  - "[[20-Entities/anja-mezger]]"
  - "[[20-Entities/sandy-klemm]]"
  - "[[20-Entities/sten-linnarsson]]"
concepts:
  - "[[30-Concepts/micro-atac-seq]]"
  - "[[30-Concepts/icell8-nanowell]]"
  - "[[30-Concepts/scatac-seq]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/tn5-tagmentation]]"
topics:
  - "[[40-Topics/single-cell-atac-seq]]"
  - "[[40-Topics/chromatin-architecture]]"
---

# Mezger et al. 2018 — µATAC-seq

> Thesis: scATAC-seq on Fluidigm C1 captures only ~96 cells per run and costs are high; combinatorial indexing scales further but produces fewer fragments per cell and is incompatible with live-cell fluorescence imaging. **µATAC-seq** runs scATAC-seq on the Takara ICELL8 5,184-nanowell platform with fluorescence-imaging-guided reagent deposition, yielding up to ~1,800 cells per chip at ~$0.81/cell library cost and ~14k fragments per cell — a **~20-fold throughput improvement** without sacrificing per-cell quality.

## Key claims

- **Throughput**: 5,184 nano-wells per chip; ~35% (~1,800) wells contain a single live cell under Poisson loading. Hoechst/PI dual staining + microscopy identifies live single cells before reagent deposition.
- **Library quality**: 14,300 fragments per human cell, 8,100 per mouse cell — **higher than Fluidigm C1** (5,800 fragments / GM12878) and combinatorial indexing (2,500 fragments / GM12878).
- **Reagent fidelity**: barnyard human/mouse cell mixing shows <0.2% double-species wells. Polymerase choice (e2Tak vs Q5) gives 97.9% concordance — robust to thermocycling chemistry.
- **PBMC application**: 2,333 single PBMCs from three donors. **De novo clustering** of isolated B/T/CD4+/CD8+/monocyte cells co-clusters precisely with bulk PBMCs (PU.1, C/EBPα, RUNX1 motifs differentially accessible across types).
- **Live-cell compatibility**: nano-well isolation preserves whole cells for downstream multi-omic assays (vs combinatorial-indexing which lyses cells). Foundation for multi-omics on the same platform.

## Methods / evidence

ICELL8 platform (Takara Bio USA) with Hoechst/propidium-iodide live/dead imaging. On-chip Tn5 transposition → PCR with 72 i5 × 72 i7 indexed primers. Off-chip extraction by centrifugation. ChromVar analysis for cell-type clustering.

## Surprising or load-bearing bits

- The **fluorescence-imaging + addressable reagent deposition** combination is the methodological insight: prior nano-well scATAC could not do quality control on live single cells before sequencing; µATAC can.
- Cost-per-cell of $0.81 in 2018 was the lowest on the market; combinatorial indexing was cheaper per fragment but couldn't preserve cell-imaging metadata.
- The Klemm authorship link is notable — Klemm/Greenleaf 2019 NRG chromatin-accessibility review ([[10-Summaries/sandy-2019-naturereviewsgenetics]]) was written in part on the basis of this platform.

## Connections to other sources

- Bridges Fluidigm-C1-era scATAC ([[10-Summaries/chromvar-inferring-transcription-factor-associated-accessibility-from-single-cell-epigenomic-data]] used C1 data) and combinatorial-indexing scATAC (used in [[10-Summaries/comprehensive-analysis-of-single-cell-atac-seq-data-with-snapatac]] for atlas-scale work).
- Same ICELL8 platform used by [[10-Summaries/scalable-single-cell-profiling-of-chromatin-modifications-with-scicut-tag]] (sciCUT&Tag) and by SpliCOOL-seq–style approaches. Demonstrates the platform's extensibility beyond ATAC.
- Complements [[10-Summaries/sandy-2019-naturereviewsgenetics]] (Klemm/Greenleaf chromatin-accessibility review).

## Open questions

- ICELL8 is single-vendor (Takara); platform availability and ongoing support are dependencies.
- Throughput improvement is incremental relative to combinatorial indexing's atlas-scale capability; µATAC's niche is quality-controlled, imageable, lower-throughput experiments.

## Related

- [[40-Topics/single-cell-atac-seq]] · [[30-Concepts/micro-atac-seq]] · [[30-Concepts/icell8-nanowell]] · [[20-Entities/william-greenleaf]] · [[20-Entities/sandy-klemm]]
