---
type: summary
title: "Luquette et al. 2025 — PTA + duplex validation across 102 nuclei from lung and colon"
source: "[[00-Sources/papers/A comprehensive view of somatic mosaicism by single-cell DNA analysis]]"
source_kind: paper
author: "Lovelace J. Luquette, Tim H. H. Coorens, ... Dan Landau, Peter J. Park, Flora M. Vaccarino, Christopher Walsh, Alexej Abyzov (corresponding)"
published: 2025-11-03
ingested: 2026-05-12
doi: "10.1101/2025.10.31.685648"
journal: "bioRxiv (preprint)"
tags: [scDNA-seq, PTA, duplex-validation, somatic-mosaicism, SMaHT, APOBEC, tobacco-signatures, lineage-tracing]
entities:
  - "[[20-Entities/lovelace-luquette]]"
  - "[[20-Entities/alexej-abyzov]]"
  - "[[20-Entities/peter-park]]"
  - "[[20-Entities/flora-vaccarino]]"
  - "[[20-Entities/christopher-walsh]]"
  - "[[20-Entities/dan-a-landau]]"
  - "[[20-Entities/smaht-network]]"
concepts:
  - "[[30-Concepts/pta]]"
  - "[[40-Topics/duplex-sequencing]]"
  - "[[40-Topics/somatic-mosaicism]]"
  - "[[30-Concepts/lineage-tracing]]"
  - "[[30-Concepts/mutational-signatures]]"
  - "[[40-Topics/clonal-hematopoiesis]]"
topics:
  - "[[40-Topics/somatic-mosaicism]]"
  - "[[40-Topics/scdna-seq]]"
---

**Citation:** Luquette et al. (2025) — *PTA + duplex validation across 102 nuclei from lung and colon* — *bioRxiv (preprint)*. [DOI](https://doi.org/10.1101/2025.10.31.685648)

# Luquette et al. 2025 — PTA + duplex validation across 102 nuclei from lung and colon

> Thesis: A scalable single-cell pipeline (PTA scWGA → deep sequencing → duplex-sequencing validation of bulk DNA) can deliver a **comprehensive view of somatic mosaicism** — SNVs, indels, CNVs, aneuploidies, structural rearrangements, embryonic lineage — from a single individual. Applied to 102 nuclei from postmortem lung and colon of a 74-year-old male, the approach exposes organ- and cell-type-specific mutation burdens, APOBEC and tobacco signatures, T-cell receptor rearrangements (reading immune lineage straight from genomic DNA), and reconstructible cellular ancestries traced from the zygote.

## Key claims

- **Burden and spectrum heterogeneity** across organs and individual cells. Tobacco signatures appear in lung as expected. APOBEC activity detected in both organs at single-cell resolution.
- **Structural heterogeneity**: aneuploidies, loss of chromosome Y (LOY), and chromosomal rearrangements detected in nuclei from both lung and colon. T-cell-receptor (TCR) rearrangements identify T cells by their genomic signature alone — a useful internal control.
- **Embryonic lineage reconstruction**: shared early-embryonic mutations across cells allow reconstruction of cellular ancestries from the zygote. Validated independently by bulk sequencing.
- Duplex sequencing of matched bulk validates that the PTA-derived SNV calls are not amplification artifacts. The pipeline cross-validates within a single tissue.
- The headline framing: only scDNA-seq + duplex together capture the **full spectrum** of mosaicism types (SNVs + CNVs + SVs + aneuploidy + lineage) — bulk WGS misses cell-resolved signal; bulk duplex misses lineage; single-cell alone risks amplification artifacts.

## Methods / evidence

102 PTA-amplified nuclei from postmortem lung and colon of one 74-yo male donor. Sequencing depth optimized for variant calling. Duplex sequencing of matched bulk used as the orthogonal validator. SMaHT-consortium pipeline.

## Surprising or load-bearing bits

- Reading T-cell identity from rearranged TCR loci in genomic DNA is a useful demonstration: **somatic genome content alone can identify cell lineage** in some cases, complementing transcriptome-based labeling.
- The lung-vs-colon contrast in mutation burden gives a clean within-individual exposure-vs-baseline comparison (smoker's lung carrying tobacco signature; colon as a quasi-control).
- Together with [[10-Summaries/zhang-2025-smaht-duplex-benchmark]] (six duplex methods benchmark), this paper defines the **SMaHT methodological core**: PTA-scDNA-seq for single-cell, duplex for bulk validation.

## Connections to other sources

- Direct extension of [[10-Summaries/shao-2025-scDNA-mosaicism-review]]'s PTA-as-inflection-point framing: PTA + duplex is the current frontier.
- Complements [[10-Summaries/bizzotto-2022-brain-mosaicism-review]] (Bizzotto/Walsh on brain) by extending the lineage-tracing logic from brain to peripheral tissues.
- TCR-rearrangement detection echoes lineage-tracing themes in [[10-Summaries/nam-2019-got]] (GoT) and [[10-Summaries/izzo-2024-got-cha]] (GoT–ChA), though those infer lineage from genotyped variants rather than rearrangements.

## Open questions

- N=1 individual. Generalization to other donors and tissues remains for the SMaHT atlas papers.
- Sample is postmortem (74-yo); fresh-tissue dynamics untested.

---
**Source:** [DOI](https://doi.org/10.1101/2025.10.31.685648)
## Related

- [[40-Topics/somatic-mosaicism]] · [[30-Concepts/pta]] · [[40-Topics/duplex-sequencing]] · [[20-Entities/smaht-network]]
