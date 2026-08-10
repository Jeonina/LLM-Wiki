---
type: summary
title: "Nandi et al. 2025 — UDSeq: universal duplex sequencing at ~2.5×10⁻⁹/bp"
source: "[[00-Sources/papers/A Universal Duplex Sequencing Approach for Accurate Detection of Somatic Mutations]]"
source_kind: paper
author: "Shuvro P. Nandi, ... Joseph G. Gleeson, Ludmil B. Alexandrov (corresponding)"
published: 2025-09-16
ingested: 2026-05-12
doi: "10.1101/2025.09.14.676103"
journal: "bioRxiv (preprint)"
tags: [duplex-sequencing, UDSeq, low-input, mutational-signatures, Alexandrov-lab]
entities:
  - "[[20-Entities/ludmil-alexandrov]]"
  - "[[20-Entities/joseph-gleeson]]"
concepts:
  - "[[40-Topics/duplex-sequencing]]"
  - "[[30-Concepts/mutational-signatures]]"
  - "[[30-Concepts/umi-molecular-barcoding]]"
topics:
  - "[[40-Topics/somatic-mosaicism]]"
---

**Citation:** Nandi et al. (2025) — *UDSeq: universal duplex sequencing at ~2.5×10⁻⁹/bp* — *bioRxiv (preprint)*. [DOI](https://doi.org/10.1101/2025.09.14.676103)

# Nandi et al. 2025 — UDSeq: universal duplex sequencing at ~2.5×10⁻⁹/bp

> Thesis: Existing duplex methods either need micrograms of DNA, lose duplex pairs through inefficient library conversion, or restrict the genomic footprint. **UDSeq** replaces these with random fragmentation + efficient UMI ligation + quantitative input control to produce near-complete exome/genome duplex coverage from **as little as 100 pg** of DNA with an error rate of ~2.5×10⁻⁹ per bp — making it a scalable platform for mutational-signature analysis of normal tissues, environmental exposures, and rare clinical samples.

## Key claims

- Sperm-DNA benchmark estimates UDSeq error at **~2.5×10⁻⁹ per bp**, well below typical somatic mutation rates and similar to NanoSeq.
- **Up to 4× more usable duplex molecules** than prior duplex protocols at matched input — yield is the practical bottleneck of duplex chemistry, and library conversion + ligation efficiency are the two levers.
- Demonstrated capture of exposure-specific mutational signatures in cell lines and rodent models from heterogeneous, non-clonally-expanded cell populations — i.e., reads mutational-signature biology directly from primary tissue without clonal organoid expansion.
- Cross-species profiling: works on rodent samples; protocol is publishable as a benchtop method with QC checkpoints (fragment size, ligation yield, conversion rate, duplication rate).

## Methods / evidence

UDSeq couples random shearing with adapter ligation that places UMIs on both strands, then standard duplex pipeline. Cost-effective relative to fixed-panel duplex assays. Benchmarked in sperm (low expected mutation burden), cancer-cell-line mixtures with known signatures (e.g., aristolochic acid, UV, tobacco), and rodent tissues with known carcinogen exposures.

## Surprising or load-bearing bits

- The 100 pg input ceiling is the headline: previous duplex methods (Schmitt-style DS) needed 1–3 μg. This brings duplex within reach of FACS-sorted small populations and biopsy specimens.
- Patent-encumbered: Alexandrov lab has filed multiple US provisional applications and one European patent on the chemistry. Worth flagging if anyone in the wiki wants to build on this in industry.

## Connections to other sources

- Direct evolution of [[10-Summaries/kennedy-2014-duplex-protocol]] — Kennedy/Loeb 2014 was 2.5×10⁻⁶/bp; UDSeq is **1,000× more accurate**.
- One of six methods benchmarked in [[10-Summaries/zhang-2025-smaht-duplex-benchmark]] would be the natural place for cross-method comparison (UDSeq is too new to appear there).
- Complements scDNA-seq approaches in [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] — DS captures signatures at the tissue level; scDNA-seq captures clonality at the cell level.

## Open questions

- Preprint; not yet peer-reviewed.
- Single-cell extension untested. Like all DS methods, requires intact dsDNA, so scWGA artifacts on single strands remain incompatible.

---
**Source:** [DOI](https://doi.org/10.1101/2025.09.14.676103)
## Related

- [[40-Topics/duplex-sequencing]] · [[30-Concepts/mutational-signatures]] · [[40-Topics/duplex-sequencing]] · [[10-Summaries/zhang-2025-smaht-duplex-benchmark]]
