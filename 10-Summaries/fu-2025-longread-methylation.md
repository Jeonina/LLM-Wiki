---
type: summary
title: "Fu, Timp & Sedlazeck 2025 — Computational analysis of DNA methylation from long-read sequencing"
source: "[[00-Sources/papers/Computational analysis of DNA methylation from long-read sequencing]]"
source_quality: full
source_sha256: "fb77e7868b1d8ab5bec3468c73d0522b270e98210ec33209eaf5f6d1bea99fac"
source_kind: paper
author: "Yilei Fu, Winston Timp, Fritz J. Sedlazeck"
published: 2025-09
ingested: 2026-05-11
doi: "10.1038/s41576-025-00822-5"
journal: "Nature Reviews Genetics 26:620–634"
tags: [review, DNA-methylation, long-read-sequencing, PacBio, ONT, computational]
entities:
  - "[[20-Entities/fritz-sedlazeck]]"
  - "[[20-Entities/winston-timp]]"
concepts:
  - "[[40-Topics/dna-methylation]]"
  - "[[40-Topics/long-read-sequencing]]"
  - "[[30-Concepts/bisulfite-sequencing]]"
topics:
---

**Citation:** Fu et al. (2025) — *Computational analysis of DNA methylation from long-read sequencing* — *Nature Reviews Genetics*. [DOI](https://doi.org/10.1038/s41576-025-00822-5)

# Fu, Timp & Sedlazeck 2025 — Computational analysis of DNA methylation from long-read sequencing

> Thesis: long-read sequencing platforms (PacBio HiFi, Oxford Nanopore) directly detect methylation marks (5mC, 5hmC, 6mA, 4mC) from raw signals without bisulfite conversion. This sidesteps the alignment problems of bisulfite-based short-read methylation calling and enables joint analysis of methylation with structural variation and tandem repeats. The remaining bottleneck is computational: methylation callers must keep pace with rapidly evolving sequencing chemistry.

## Key claims

- **Bisulfite sequencing's structural problem**: converts unmethylated C→U→T, creating a three-base genome alignment problem that degrades mapping in repeats and structural variants. EM-seq and TAPS-seq are enzymatic alternatives but still produce short-read data with limited isoform/SV resolution.
- **Microarrays** (Illumina EPIC/450K) measure only ~935,000 of ~28 million CpGs — limited to pre-selected sites.
- **Long-read direct methylation detection**:
  - **PacBio HiFi**: pulse-width and inter-pulse duration during base incorporation are altered by methylation; calling uses kinetic features.
  - **ONT**: electrolytic current through the nanopore changes with modification state; calling uses HMMs / CNNs / Transformers from raw signal.
- **No base conversion** → standard reference alignment → mappable in repeats, SVs, and tandem repeats that bisulfite methods cannot resolve.
- **Modifications detectable**: 5mC, 5hmC, 6mA, 4mC, with varying accuracy across platforms.
- **Computational tool landscape** is rapidly evolving — each major chemistry generation requires new callers (e.g., Nanopolish, DeepSignal, DeepMod2, Rockfish and Dorado for ONT; Jasmine and ccsmeth for PacBio).

## Methods / evidence

Computational-methods-focused review. Authors are at major long-read centers (Baylor, Johns Hopkins). *(not found in source clipping — unverified)* Disclosed industry ties to PacBio and ONT.

## Surprising or load-bearing bits

- **The three-base alignment problem** of bisulfite-converted reads is a structural argument for long-read methods that is often underappreciated. It means bisulfite sequencing is *systematically* biased away from repetitive regions of the genome — exactly the regions where methylation has key roles (transposon silencing, satellite repeats).
- **Long-read methylation calling treats methylation as a sequencing-feature-detection problem** (signal kinetics or pore current) rather than as a base-conversion problem. This is conceptually parallel to how [[10-Summaries/swanson-2025-daf-seq]] treats deaminations as sequence features that survive amplification — both reframings exploit modern sequencing's ability to read modifications directly rather than infer them.
- **Methylation + structural variation simultaneously** is a key downstream capability: imprinted regions, repeat-expansion disorders, and X-inactivation can be characterized in single experiments.

## Entities mentioned

- [[20-Entities/fritz-sedlazeck]] — senior author; Baylor; long-read methods PI.
- [[20-Entities/winston-timp]] — co-senior; Johns Hopkins; nanopore methylation pioneer.

## Concepts touched

- [[40-Topics/dna-methylation]] — measurement modalities updated to current long-read era.
- [[40-Topics/long-read-sequencing]] — PacBio + ONT capabilities.
- [[30-Concepts/bisulfite-sequencing]] — predecessor with structural limitations.

## Connections to other sources

- **Methodological successor to** [[10-Summaries/smith-2013-methylation-development]] (Smith & Meissner) — Smith & Meissner provide the biology of methylation; Yilei et al. provide the current measurement and computational toolkit.
- **Complementary to** [[10-Summaries/swanson-2025-daf-seq]] (DAF-seq) in conceptual structure: both use long-read sequencing to read DNA modifications (m6A in Fiber-seq, methylation in PacBio/ONT) directly without amplification erasure issues — though DAF-seq sidesteps amplification erasure by using *sequence changes* rather than modifications.

## Open questions

- Methylation calling accuracy benchmarking across platforms and tools — no community-accepted gold-standard benchmark yet.
- 5hmC detection is ONT-only (PacBio currently cannot detect it) and hard to benchmark because of its low abundance; PacBio callers appear more accurate than ONT for 6mA.
- Single-cell long-read methylation — the review notes that single-cell protocols usually require amplification, which makes native long-read methylation detection impossible without chemical treatment; an intersection of [[40-Topics/scdna-seq]] and long-read methylation that remains open.

---
**Source:** [DOI](https://doi.org/10.1038/s41576-025-00822-5)
