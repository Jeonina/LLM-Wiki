---
type: topic
title: Whole-genome amplification (scWGA)
aliases: [scWGA topic, WGA topic, whole-genome amplification methods]
tags: [scWGA, methods, amplification]
created: 2026-05-11
updated: 2026-05-11
---

# Whole-genome amplification (scWGA)

> The set of biochemical methods that bridge the ~6 pg of DNA in a single diploid cell to the input requirement of any sequencing platform. The defining technical challenge of [[40-Topics/scdna-seq]]: amplifying 10⁵- to 10⁶-fold without losing coverage uniformity, allelic balance, or per-base accuracy.

## Core concepts

### Method categories

- [[30-Concepts/scwga]] — umbrella concept; three chemistry categories.
- **PCR-based**: [[30-Concepts/dop-pcr]], PicoPLEX, [[30-Concepts/malbac]].
- **Isothermal (Φ29 polymerase)**: [[30-Concepts/mda]], [[30-Concepts/pta]].
- **Tn5 transposon-based**: [[30-Concepts/dlp-plus]], LIANTI, [[30-Concepts/meta-cs]].

### Alternatives that skip scWGA

- [[40-Topics/duplex-sequencing]] — bulk-DNA single-molecule methods.
- DNTR-seq (in [[10-Summaries/vandereyken-2023-scmultiomics-review]]) — direct nuclear DNA tagmentation, skipping WGA.

### Errors introduced by scWGA

- Allelic dropout / locus dropout.
- Allelic imbalance.
- Single-strand dropout (SSD) — leads to false positives that overwhelm true signal.
- Polymerase error (Taq much higher than Φ29).
- Chimera formation (strand-displacement).

## Key entities

- [[20-Entities/diane-d-shao]] — keystone 2025 review.
- [[20-Entities/charles-gawad]] — foundational 2016 review.
- [[20-Entities/christopher-walsh]] — early PTA adopter for neuron mosaicism.

## Sources, by sub-theme

### Comparative reviews

- [[10-Summaries/shao-2025-scDNA-mosaicism-review]] — current method comparison Table 1.
- [[10-Summaries/gawad-2016-scgenome-review]] — pre-PTA 3-category comparison.

### Multi-omic methods using specific scWGA chemistries

- [[10-Summaries/nam-2019-got]] — GoT (10x cDNA amplification, not classical scWGA but related).
- [[10-Summaries/izzo-2024-got-cha]] — GoT–ChA (gDNA locus amplification in droplets).
- [[10-Summaries/swanson-2025-daf-seq]] — scDAF-seq using PTA for genome-wide amplification.
- [[10-Summaries/vandereyken-2023-scmultiomics-review]] — G&T-seq family using MDA / PCR / DA-PCR.

## Synthesized notes

_None yet — natural target: "Choosing a scWGA method: tradeoffs and applications."_

## Open questions

- Whether MDA retains a niche given PTA's cost approaching MDA's.
- When to use scWGA-free approaches (DNTR-seq, duplex sequencing) — application-dependent, no consensus heuristic.
- Standardization of QC metrics and definitions (especially ADO) across methods — flagged in [[10-Summaries/gawad-2016-scgenome-review]], still partly unresolved.
- Coverage vs cell throughput operating points — DLP+ scales to >10⁴ cells very low coverage; PTA peaks at 384 cells at ~95%; how to choose for a given biology.

## Linked summaries (lint pass 2026-05-21)

- [[10-Summaries/debourcy-2014-plosone]] — de Bourcy 2014 — Quantitative comparison of single-cell WGA methods.

