---
type: concept
title: G&T-seq
aliases: [Genome and Transcriptome sequencing, G and T-seq, GnT-seq, G&T-seq]
tags: [multi-omics, scDNA-scRNA, physical-separation, joint-assay, foundational, method]
created: 2026-05-11
updated: 2026-10-12
---

# G&T-seq (Genome and Transcriptome sequencing)

> Plate-based single-cell joint DNA + RNA method that **physically separates** poly(A) mRNA (on oligo-dT magnetic beads) from genomic DNA (in the supernatant) before independent library preparation. Introduced by Macaulay et al. 2015 ([[10-Summaries/macaulay-2015-gt-seq|Macaulay 2015]]); developed in the [[20-Entities/thierry-voet|Voet lab]] at KU Leuven. Provides the cleanest separation of DNA and RNA modalities at single-cell scale, compatible with any choice of WGA chemistry, and is the methodological root of [[scnmt-seq]] (which inherits the separation chemistry) ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).

> [!abstract] 한눈에
> G&T-seq는 한 세포에서 poly(A) mRNA를 oligo-dT bead로 떼어 내고 남은 genomic DNA를 따로 증폭해, DNA와 RNA를 각각 최적의 protocol로 읽는 plate 기반 방법이다 ([[10-Summaries/macaulay-2015-gt-seq|Macaulay 2015]]). 분리 덕분에 어떤 WGA chemistry든 쓸 수 있지만, plate 기반이라 처리량이 낮고 bead 세척 과정에서 DNA 손실이 생긴다 ([[10-Summaries/macaulay-2016-gt-seq-protocol|Macaulay 2016]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 multi-omics](../60-Explainers/single-cell-multiomics.html)
<!-- /explainer-links -->

## Definition

Macaulay et al. 2015 ([[10-Summaries/macaulay-2015-gt-seq|Macaulay 2015]]). In G&T-seq:

1. Single cell lysed in a multiwell plate.
2. Biotinylated oligo-dT magnetic beads capture poly(A) mRNA.
3. Supernatant — containing genomic and mitochondrial DNA — is moved to a fresh well for [[scwga]] (MDA preferred for SNV / deep coverage; PicoPlex/PCR preferred for CNV; or DA-PCR).
4. On-bead mRNA undergoes Smart-seq2 reverse transcription → full-length cDNA → Nextera XT.
5. Both fractions are sequenced independently and merged computationally by well/cell.

The separation-before-amplification design gives three advantages over the one-pot [[30-Concepts/dr-seq|DR-seq]] alternative: no coding-region masking needed, any WGA chemistry can be used, and full-length Smart-seq2 RNA (not 3′-biased).

## Why it matters

- **Early same-cell DNA + RNA assay with physical separation** — compatible with any WGA chemistry and automatable; the protocol itself cites DR-seq and microfluidic methods as other same-cell DNA + RNA approaches ([[10-Summaries/macaulay-2016-gt-seq-protocol|Macaulay 2016]]).
- **Modality independence**: each fraction can be processed by the best-of-class single-modality protocol — G&T-seq doesn't force a compromise on either RNA or DNA quality.
- **Compatible with long-read sequencing** of the RNA fraction for isoform detection.

## Variants and refinements

| Variant | How DNA and RNA are separated | What it adds | Source |
|---|---|---|---|
| G&T-seq | Oligo-dT bead capture of mRNA; DNA in supernatant | Original DNA + RNA | ([[10-Summaries/macaulay-2015-gt-seq\|Macaulay 2015]]; protocol [[10-Summaries/macaulay-2016-gt-seq-protocol\|Macaulay 2016]]) |
| [[scnmt-seq\|scNMT-seq]] | Inherits the separation chemistry | Adds GpC methylation labeling for accessibility + endogenous CpG methylation | ([[10-Summaries/clark-2018-scnmt-seq\|Clark 2018]]) |
| SIDR-seq, DNTR-seq | Nuclear-cytosolic partitioning | DNTR-seq uses direct Tn5 tagmentation of nuclear DNA instead of WGA, sidestepping WGA artifacts at the cost of lower coverage breadth | ([[10-Summaries/vandereyken-2023-scmultiomics-review\|Vandereyken 2023]]) |
| [[30-Concepts/dr-seq\|DR-seq]] | Pre-amplification then split | One-pot alternative | — |

## Evidence and examples

- Demonstrated detection of a **trisomy-11 subclone in HCC38-BL lymphoblastoid cells** (10% frequency, confirmed by FISH) ([[10-Summaries/macaulay-2015-gt-seq|Macaulay 2015]]; marked unverified against the source clipping in that summary).
- **Reversine-treated mouse 8-cell embryos**: reciprocal aneuploidies between sister blastomeres, with concordant chromosome-wide expression dosage in the *same* cells → expression dosing established within one division ([[10-Summaries/macaulay-2015-gt-seq|Macaulay 2015]]).
- MTAP–PCDH7 fusion captured at DNA and RNA level in the same HCC38 cells, with PacBio long-read confirmation ([[10-Summaries/macaulay-2015-gt-seq|Macaulay 2015]]).
- Studies of clonal architecture in cancer using paired DNA+RNA from G&T-seq.

## Contested points

- Plate-based throughput limits — 172 cells in the original benchmark; 96 cells take about 3 days even on a liquid-handling robot ([[10-Summaries/macaulay-2016-gt-seq-protocol|Macaulay 2016]]), far below later combinatorial-indexing methods.
- Beadwash losses reduce per-cell DNA yield vs nuclear-cytosolic partitioning methods; the authors also note that separation "may contribute further" to allelic dropout ([[10-Summaries/macaulay-2016-gt-seq-protocol|Macaulay 2016]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/dr-seq|DR-seq]] — One-pot DNA + RNA alternative with pre-amplification then split.
> - `concept` [[30-Concepts/scnmt-seq|scNMT-seq]] — Descendant that adds methylation and accessibility.
> - `concept` [[30-Concepts/scwga|scWGA]] — Single-cell whole-genome amplification for the DNA fraction.
> - `concept` [[30-Concepts/mda|MDA]] — Isothermal WGA preferred for SNVs and deep coverage.
> - `concept` [[30-Concepts/malbac|MALBAC]] — Quasi-linear WGA chemistry.
> - `hub` [[40-Topics/scdna-seq|scDNA-seq]] — Single-cell DNA sequencing methods and analysis.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Joint measurement of several layers in one cell.
> - `hub` [[40-Topics/whole-genome-amplification|Whole-genome amplification]] — WGA chemistries and their artefacts.
> - `entity` [[20-Entities/thierry-voet|Thierry Voet]] — KU Leuven lab where G&T-seq was developed.

## All sources on this page

> [!info]- 4 summaries cited here
> - [[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]
> - [[10-Summaries/macaulay-2015-gt-seq|Macaulay 2015]]
> - [[10-Summaries/macaulay-2016-gt-seq-protocol|Macaulay 2016]]
> - [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]
