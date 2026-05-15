---
type: summary
title: "Shao et al. 2025 — Advances in single-cell DNA sequencing for somatic mosaicism"
source: "[[00-Sources/papers/Diane_2025_NatureReviewsGenetics]]"
source_kind: paper
author: "Diane D. Shao, Andrea J. Kriz, Daniel A. Snellings, Zinan Zhou, Yifan Zhao, Liz Enyenihi, Christopher Walsh"
published: 2025-11
ingested: 2026-05-11
doi: "10.1038/s41576-025-00832-3"
journal: "Nature Reviews Genetics 26:761–774"
tags: [review, scDNA-seq, scWGA, mosaicism, lineage-tracing, keystone-review]
entities:
  - "[[20-Entities/diane-d-shao]]"
  - "[[20-Entities/christopher-walsh]]"
concepts:
  - "[[30-Concepts/scdna-seq]]"
  - "[[30-Concepts/scwga]]"
  - "[[30-Concepts/mda]]"
  - "[[30-Concepts/pta]]"
  - "[[30-Concepts/malbac]]"
  - "[[30-Concepts/dop-pcr]]"
  - "[[30-Concepts/dlp-plus]]"
  - "[[30-Concepts/meta-cs]]"
  - "[[30-Concepts/duplex-sequencing]]"
  - "[[30-Concepts/somatic-mosaicism]]"
  - "[[30-Concepts/lineage-tracing]]"
topics:
  - "[[40-Topics/scdna-seq]]"
  - "[[40-Topics/somatic-mosaicism]]"
  - "[[40-Topics/whole-genome-amplification]]"
---

**Citation:** Shao et al. (2025) — *Advances in single-cell DNA sequencing for somatic mosaicism* — *Nature Reviews Genetics*. [DOI](https://doi.org/10.1038/s41576-025-00832-3)

# Shao et al. 2025 — Advances in single-cell DNA sequencing for somatic mosaicism

> Thesis: scDNA-seq has historically lagged behind scRNA-seq and scATAC because the human genome is 20–50× larger than the transcribed/accessible genomes and each locus is represented by only two molecules per cell — so single-cell whole-genome amplification (scWGA) is required and unavoidable. Recent advances (PTA, duplex sequencing, computational error correction) have finally made scDNA-seq tractable, enabling somatic mosaicism research, lineage tracing in human tissues, and pre-implantation genetic screening.

## Key claims

- **scDNA-seq is now an umbrella term** covering both (a) scWGA + scWGS and (b) single-molecule duplex sequencing of bulk DNA. Both give single-cell-level variation; the latter sacrifices the per-cell assignment in exchange for lower input requirements.
- **scWGA technology comparison (Table 1)**:
  - **DOP-PCR**: PCR-based, low coverage (20–25%), high uniformity, low cost (~$20).
  - **PicoPLEX**: PCR-based with looped products, medium coverage (35–45%).
  - **MALBAC**: PCR-based with looped products, medium coverage (55–60%).
  - **MDA**: Isothermal Φ29-based, medium coverage (70–75%), low allelic balance, high uniformity issues.
  - **PTA**: Isothermal Φ29 + chain terminators producing short amplicons that favor priming from the native template, **high coverage (~95%)**, high uniformity, high allelic balance — current gold standard.
  - **LIANTI**: Tn5-based linear amplification via transposon insertion, high coverage (80–85%), not commercially available, complex protocol.
  - **DLP+**: Tn5-based microfluidic, **>10,000 cells throughput** at very low coverage per cell.
- **Duplex sequencing variants**: Y-adaptor (BotSeqS), Tn5-based (META-CS — the only one applicable to single cells), quadruplex adaptor (CODEC), circularized (HiDEF-seq on PacBio, SMM-seq on Illumina). Error rates as low as ~7 × 10⁻¹⁶ for HiDEF-seq.
- **Errors in scWGA**: allelic dropout (50% chance false-negative), allelic imbalance, single-strand dropout (25% chance false-positive — from ~70,000 daily ssDNA lesions per cell), polymerase errors. **False positives are the dominant problem** because overamplified errors overwhelm true biological signal.
- **CNV callers** (Table 2): Ginkgo, SCOPE, deepCNA (read-depth-only); CHISEL, Alleloscope, HiScanner (read-depth + B-allele frequency for allele-specific copy number).
- **SNV callers**: SCcaller (MDA), SCAN2 (PTA), duplex-specific callers.
- **Application axes (Fig 1c)**: cell number vs sequencing depth tradeoff — few cells + deep coverage for SNV/indel signatures, many cells + shallow coverage for lineage tracing and mutation hotspots.

## Methods / evidence

This is a synthesizing review from the Walsh lab (Boston Children's), which has been a leader in human brain mosaicism studies. The review systematizes the field through a comparison table of scWGA methods, a workflow diagram, and a depth-vs-cells application matrix.

## Surprising or load-bearing bits

- **Single-strand dropout (SSD) as a major source of false positives** is named explicitly: ~70,000 single-strand lesions per cell per day means that without duplex-sequencing protection, the false-positive rate at the single-cell level is catastrophic. This explains why duplex sequencing is increasingly seen as the future direction, not just an option.
- **PTA's mechanism** — exonuclease-resistant terminators that produce short amplicons, biasing Φ29 toward priming on the native template — is the key innovation that elevated coverage from MDA's ~70–75% to PTA's ~95% while preserving allelic balance. This is *why* PTA dominates current scDNA-seq workflows including [[10-Summaries/elliott-2025-naturebiotechnology|scDAF-seq]].
- **Lineage tracing in human tissue is now technically possible** through the natural accumulation of ~2–4 mutations per cell division. The Walsh lab has used this to track human brain progenitor lineages without genetic manipulation.
- **40% of mid-gestation human prenatal neurons harbor complex CNV** per a Walsh lab preprint cited here — somatic genome variability is much higher in development than previously appreciated, and resolves after birth.

## Entities mentioned

- [[20-Entities/diane-d-shao]] — first author, Boston Children's / Harvard.
- [[20-Entities/christopher-walsh]] — senior author, longtime PI of human brain mosaicism studies.

## Concepts touched

- [[30-Concepts/scdna-seq]] — defined here as the umbrella for scWGA+scWGS and single-molecule duplex methods.
- [[30-Concepts/scwga]] — three categories: PCR-based, isothermal, Tn5-based.
- [[30-Concepts/mda]], [[30-Concepts/pta]], [[30-Concepts/malbac]], [[30-Concepts/dop-pcr]], [[30-Concepts/dlp-plus]], [[30-Concepts/meta-cs]] — individual methods.
- [[30-Concepts/duplex-sequencing]] — single-molecule strand-pairing strategy for SNV calling.
- [[30-Concepts/somatic-mosaicism]] — the central biology motivation.
- [[30-Concepts/lineage-tracing]] — natural mutation accumulation as endogenous lineage marker.

## Connections to other sources

- **Synthesizes and supersedes** [[10-Summaries/charles-2016-naturereviewsgenetics]] (Gawad/Quake): nine years on, PTA + duplex sequencing have replaced the MDA/MALBAC tradeoffs that dominated the 2016 landscape.
- **Defines the framework that places** [[10-Summaries/elliott-2025-naturebiotechnology]] (scDAF-seq) in context — scDAF-seq uses PTA for amplification, which is exactly the scWGA breakthrough Diane 2025 highlights as enabling the current generation of scDNA-seq applications.
- **Complements** [[10-Summaries/lars-2017-naturereviewsgenetics]] (mosaicism biology) and [[10-Summaries/ian-2015-trendsingenetics]] (mosaicism implications) — those provide the biological context; Diane 2025 provides the technical framework now mature enough to answer the questions those reviews raised.
- **Conceptually parallel to** [[10-Summaries/gilad-2021-annualreviewofgenomicsandhumangenetics]] (Evrony et al.) which provides the applications-focused framework (fidelity / co-presence / phenotypic association).

## Open questions

- The clinical promise of unbiased pre-implantation genetic screening from a single embryo cell — currently demonstrated in preprint, not yet validated in clinical trials.
- Single-cell + single-molecule combined approaches: scDAF-seq is one direction, but is there an analogous "scDNA-seq + chromatin in the same cell" that matches the depth of duplex sequencing while keeping single-cell resolution?
- Throughput vs depth: DLP+ scales to >10,000 cells at very low per-cell coverage; PTA peaks at ~384 cells per run. The right operating point for a given biological question is rarely benchmarked.

---
**Source:** [DOI](https://doi.org/10.1038/s41576-025-00832-3)
