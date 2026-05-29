---
type: topic
title: Somatic mosaicism
aliases: [mosaicism, post-zygotic variation topic]
tags: [mosaicism, genetics, development, aging]
created: 2026-05-11
updated: 2026-05-19
---

# Somatic mosaicism

> Every human is a mosaic of genetically distinct cells ([[10-Summaries/forsberg-2017-mosaicism-review]]; [[10-Summaries/cagan-2022-nature]]). The biological question driving most of the [[40-Topics/scdna-seq]] technology investment: how to detect, characterize, and understand the somatic variants that accumulate throughout life ([[10-Summaries/vijg-2020-cell]]) and shape both normal physiology (aging, [[30-Concepts/clonal-hematopoiesis|clonal hematopoiesis]] per [[10-Summaries/izzo-2024-got-cha]]) and disease (cancer per [[10-Summaries/shao-2025-scDNA-mosaicism-review]], neurodevelopmental disorders per [[10-Summaries/bizzotto-2022-brain-mosaicism-review]]).

## Core concepts

### Foundations

- [[30-Concepts/somatic-mosaicism]] — central concept.
- [[30-Concepts/post-zygotic-variation]] — broader unifying term.
- [[30-Concepts/microchimerism]] — distinct phenomenon (cells from a different individual).
- [[30-Concepts/developmental-mutation-timing]] — timing-to-tissue-distribution mapping.
- [[30-Concepts/gonadal-mosaicism]] — germline subclass; recurrence risk.

### Disease applications

- [[30-Concepts/clonal-hematopoiesis]] — mosaic HSC expansions detectable in blood; cardiovascular and leukemia risk.
- [[30-Concepts/calr-mutation]], [[30-Concepts/jak2-v617f]] — MPN driver mosaic mutations.
- [[30-Concepts/myeloproliferative-neoplasm]] — clinical disease class.

### Methods enabling mosaicism research

- [[30-Concepts/scdna-seq]] — single-cell DNA sequencing.
- [[30-Concepts/scwga]], [[30-Concepts/pta]] — high-coverage WGA.
- [[30-Concepts/duplex-sequencing]] — low-VAF variant detection.
- [[30-Concepts/lineage-tracing]] — endogenous mutations as lineage barcodes.

## Key entities

- [[20-Entities/christopher-walsh]] — brain mosaicism program.
- [[20-Entities/diane-d-shao]] — Walsh lab scDNA-seq review author.
- [[20-Entities/gilad-evrony]] — former Walsh postdoc; applications framework.
- [[20-Entities/lars-forsberg]] — health-and-disease mosaicism review author.
- [[20-Entities/james-lupski]] — clinical genetics of mosaicism; transmission risk.
- [[20-Entities/sara-bizzotto]] — Walsh lab; brain mosaicism review (Bizzotto/Walsh 2022).
- [[20-Entities/patrick-chinnery]] — mtDNA heteroplasmy single-cell biology.
- [[20-Entities/ludmil-alexandrov]] — mutational signatures and ultra-accurate duplex chemistry.
- [[20-Entities/tim-coorens]] — SMaHT duplex-seq benchmark.
- [[20-Entities/manolis-kellis]] — single-cell mosaicism in AD.
- [[20-Entities/smaht-network]] — NIH consortium for somatic mosaicism atlas.

## Sources, by sub-theme

### Mosaicism biology and clinical implications

- [[10-Summaries/forsberg-2017-mosaicism-review]] — health-and-disease perspective.
- [[10-Summaries/campbell-2015-mosaicism-review]] — transmission genetics, developmental timing.

### Methods reviews

- [[10-Summaries/shao-2025-scDNA-mosaicism-review]] — current scDNA-seq toolkit for mosaicism research.
- [[10-Summaries/evrony-2021-scDNA-applications-review]] — applications framework.
- [[10-Summaries/bizzotto-2022-brain-mosaicism-review]] — Bizzotto & Walsh 2022, NRN brain mosaicism review.
- [[10-Summaries/shao-2025-scDNA-mosaicism-review]] — Shao 2025 NRG scDNA-seq for mosaicism review.

### MPN as a tractable mosaicism disease model

- [[10-Summaries/nam-2019-got]] — CALR-mutated MPN.
- [[10-Summaries/izzo-2024-got-cha]] — JAK2V617F MPN and clonal hematopoiesis.

### Duplex sequencing for low-VAF mutation detection

- [[10-Summaries/schmitt-2012-pnas]] — Schmitt/Loeb 2012. Original DS.
- [[10-Summaries/kennedy-2014-duplex-protocol]] — Kennedy 2014 founding DS bench protocol.
- [[10-Summaries/nandi-2025-udseq]] — UDSeq 2025.
- [[10-Summaries/abascal-2021-nanoseq]] — NanoSeq nuclear-genome DS.
- [[10-Summaries/zhang-2025-smaht-duplex-benchmark]] — SMaHT cross-method benchmark.

### Single-cell mosaicism studies

- [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] — Luquette 2025: PTA + duplex validation, 102 nuclei from lung+colon of 74-yo donor.
- [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] — companion PTA pipeline paper.
- [[10-Summaries/glynos-2023-mtdna-mosaicism]] — Glynos/Chinnery 2023: mouse mtDNA heteroplasmy variance increases through life.
- [[10-Summaries/kousi-2022-ad-mosaicism]] — Kousi/Kellis 2022: cell-type-specific AD mosaicism.
- [[10-Summaries/lodato-2017-aging-neurons]] — Lodato et al. 2018 aging-neuron mosaic mutation burden.
- [[10-Summaries/bae-2017-pregastrulation-mutations]] — Bae 2017: developmental mutation timing.

### Structural-variant somatic mosaicism

- [[10-Summaries/liu-2025-nanopore-lscc-svs]] — nanopore SomaGauss-SV in LSCC; smoking × deletion-burden correlation.

## Synthesized notes

_None yet._

## Open questions

- **Single-cell duplex sequencing** — duplex needs both strands; scWGA loses strand identity. Closing this gap is the single biggest method gap ([[40-Topics/duplex-sequencing]] open questions).
- Tissue-specific mosaic mutation rates: high in skin (UV) and intestine (turnover); uncertain in many other tissues.
- Clinical threshold (VAF, gene set) at which mosaicism becomes diagnostically actionable.
- Whether age-related mosaic accumulation *causes* aging-related disease or is a *biomarker* — distinction matters for therapeutic strategies.
- IRE1-XBP1 as a therapeutic target in CALR-mutant clonal hematopoiesis ([[10-Summaries/nam-2019-got]] hypothesis) — no clinical validation in wiki yet.
- Why CALR fitness advantage is differentiation-dependent in ET but already strong at HSPC level in MF.
- Whether JAK2V617F chromatin priming in HSCs is causal for clonal expansion or downstream of it ([[10-Summaries/izzo-2024-got-cha]]).
- Pre-implantation genetic screening from a single embryo cell — preprint stage; awaiting clinical validation ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Linked summaries (lint pass 2026-05-21)

- [[10-Summaries/ludwig-2020-mtscatac-seq]] — Ludwig 2020 — mtscATAC-seq: massively parallel mtDNA genotyping + chromatin in single cells.
- [[10-Summaries/oroak-2012-autism-targeted-seq]] — O'Roak 2012 — Multiplex targeted sequencing of recurrently mutated genes in ASD.
- [[10-Summaries/campbell-2015-mosaicism-review]] — Campbell 2015 — Somatic mosaicism: implications for disease and transmission (review).
- [[10-Summaries/mckenna-2016-science]] — McKenna 2016 — GESTALT: whole-organism lineage tracing by combinatorial genome editing.
- [[10-Summaries/forsberg-2017-mosaicism-review]] — Forsberg, Gisselsson & Dumanski 2017 NRG — structural-variant-centric framing of mosaicism; introduces ACE terminology; LOY as the most common human post-zygotic mutation.
- [[10-Summaries/hilal-2026-cardiac-somatic-review]] — Hilal, Arava & Choudhury 2026 — cardiovascular somatic-variation review; cardiomyocyte 4–30k SNVs/cell and CHIP→HFpEF/stroke links.
- [[10-Summaries/hsieh-2026-scmtmpm-scwmss]] — Hsieh 2026 — single-cell mtDNA mutational burden metrics (scmtMPM, scwMSS); negative selection at sub-threshold VAF.

