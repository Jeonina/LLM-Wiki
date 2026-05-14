---
type: summary
title: "Janssens et al. 2023 — sciCUT&Tag: combinatorial indexing for 40,000 cells/chip"
source: "[[00-Sources/papers/Scalable single-cell profiling of chromatin modifications with sciCUT&Tag]]"
source_kind: paper
author: "Derek H. Janssens, Jacob E. Greene, Steven J. Wu, Christine A. Codomo, Samuel S. Minot, Scott N. Furlan, Kami Ahmad, Steven Henikoff (corresponding)"
published: 2023-11-07
ingested: 2026-05-12
doi: "10.1038/s41596-023-00905-9"
journal: "Nature Protocols"
tags: [CUT&Tag, single-cell, combinatorial-indexing, Tn5, ICELL8, Henikoff-lab, PBMC, MulTI-Tag]
entities:
  - "[[20-Entities/steven-henikoff]]"
  - "[[20-Entities/derek-janssens]]"
  - "[[20-Entities/kami-ahmad]]"
concepts:
  - "[[30-Concepts/scicut-tag]]"
  - "[[30-Concepts/cut-and-tag]]"
  - "[[30-Concepts/combinatorial-indexing]]"
  - "[[30-Concepts/multi-tag]]"
  - "[[30-Concepts/histone-modifications]]"
topics:
  - "[[40-Topics/histone-modifications]]"
  - "[[40-Topics/single-cell-multiomics]]"
---

# Janssens et al. 2023 — sciCUT&Tag

> Thesis: scCUT&Tag droplet-based platforms are expensive per cell and limited in chemistry control. **sciCUT&Tag** uses **two-round combinatorial indexing** (96-well plate first round of pA-Tn5 indexed tagmentation + 5,184-well ICELL8 second round of PCR indexing) to scale to ~40,000 cells per chip at ~$0.11/cell — a ~8× cost reduction vs droplets — while maintaining higher per-cell read counts (~2,100 reads/cell for H3K27me3 vs 1,110 for original scCUT&Tag).

## Key claims

- **Workflow**: lightly cross-link nuclei → bind to WGA-magnetic beads → bulk primary+secondary antibody → array in 96-well plate → barcoded pA-Tn5 tagmentation per well → pool → ICELL8 dispense at 12–24 cells/nanowell → SDS release → PCR with second-round barcode → SPRI cleanup → sequence. ~1.5 days end-to-end by a research technician.
- **Per-cell yield**: median 2,116 reads/cell for H3K27me3 in human PBMCs (vs ~1,110 for original scCUT&Tag, comparable to linear-amplification methods that bolster reads/cell).
- **Throughput**: ~40,000 cells/chip with 12–24 cells/nanowell loading; **collision rate 16–17%** at this density (acceptable when SNP-based collision removal is used).
- **SNP-based collision removal**: dispense two donors' cells together; reads carrying inconsistent SNPs across the same barcode flag collisions. Built-in quality control.
- **PBMC application**: H3K27me3 and H3K4me1-2-3 in PBMCs from two healthy donors. Single-cell profiles of either mark are sufficient for high-resolution clustering and de novo cell-type identification (T cells, B cells, monocytes, NK cells).
- **MulTI-Tag extension**: sciCUT&Tag is the underlying single-cell partitioning for **MulTI-Tag** (multi-target identification by tagmentation) — multiplexes several chromatin epitopes within the same cell via different antibody-barcoded Tn5 complexes.

## Methods / evidence

ICELL8 nanowell platform (Takara). Standardized protocol with optimization for nuclei loading (12–24 cells/well) to balance throughput vs collision rate. Demonstrated on mixed-donor human PBMCs and previously on human ES → endoderm/mesoderm/neuroectoderm differentiation (MulTI-Tag).

## Surprising or load-bearing bits

- The **collision-removal-by-SNPs** approach turns the multi-donor mix from a complication into a quality-control feature. Genotype information is essentially free additional metadata that filters out doublets.
- The combinatorial-indexing × ICELL8 approach achieves what droplet platforms cannot: simultaneous high throughput and tight per-cell chemistry control (each nanowell is a discrete tagmentation reaction).
- Order-of-magnitude cost-per-cell reduction matters for atlas-scale projects ($4,400 to profile 40,000 cells via sciCUT&Tag vs $34,000 via droplet).

## Connections to other sources

- Henikoff-lab method derivative chain: ChIC (Schmid 2004) → CUT&RUN (Skene & Henikoff 2017) → CUT&Tag (Kaya-Okur 2019) → scCUT&Tag (Wu 2021) → sciCUT&Tag (this paper) → MulTI-Tag (Janssens 2022).
- Competes with [[10-Summaries/scchix-seq-infers-dynamic-relationships-between-histone-modifications-in-single-cells]] (scChIX-seq, MNase-based, deconvolution-style multiplexing) and the Zhao-lab scChIC-seq family in [[10-Summaries/single-cell-chromatin-immunocleavage-sequencing-scchic-seq-to-profile-histone-modification]].
- Same ICELL8 platform as [[10-Summaries/high-throughput-chromatin-accessibility-profiling-at-single-cell-resolution]] (µATAC-seq, Greenleaf 2018) — the nanowell device has become a shared substrate for single-cell chromatin methods.

## Open questions

- Tn5 cuts within nucleosomes can degrade chromatin organization information; MNase-based methods like sortChIC preserve nucleosome positioning better.
- Atlas-scale multi-mark cataloging (e.g., 50 marks × tissue × donor) remains expensive even at $0.11/cell.

---
**Source:** [DOI](https://doi.org/10.1038/s41596-023-00905-9)
## Related

- [[40-Topics/histone-modifications]] · [[30-Concepts/scicut-tag]] · [[30-Concepts/cut-and-tag]] · [[30-Concepts/multi-tag]] · [[20-Entities/steven-henikoff]]
