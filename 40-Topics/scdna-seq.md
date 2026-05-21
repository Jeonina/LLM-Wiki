---
type: topic
title: Single-cell DNA sequencing (scDNA-seq)
aliases: [scDNA-seq topic]
tags: [single-cell, scDNA-seq, methods]
created: 2026-05-11
updated: 2026-05-11
---

# Single-cell DNA sequencing (scDNA-seq)

> The umbrella topic for technologies that interrogate single-cell genomes — either via [[scwga]] + scWGS or via [[duplex-sequencing]] of bulk DNA at single-molecule resolution. Two decades of technological iteration have brought the field from low-coverage DOP-PCR (2008) through MDA / MALBAC (2010s) to PTA + duplex sequencing (2020s), finally making routine human-tissue mosaicism and lineage-tracing studies feasible.

The topic is organized by **capability** ([[30-Concepts/scdna-capabilities-framework]]) rather than purely by chemistry — fidelity, co-presence, phenotypic association — and by **application**: mosaicism, lineage tracing, cancer clonal evolution, pre-implantation screening, microbial dark matter.

## Core concepts

### The technology

- [[30-Concepts/scdna-seq]] — umbrella for the method class.
- [[30-Concepts/scwga]] — whole-genome amplification, the central technical challenge.
- [[30-Concepts/mda]], [[30-Concepts/pta]], [[30-Concepts/malbac]], [[30-Concepts/dop-pcr]], [[30-Concepts/dlp-plus]], [[30-Concepts/meta-cs]] — specific WGA methods.
- [[30-Concepts/duplex-sequencing]] — single-molecule error correction.
- [[30-Concepts/scdna-capabilities-framework]] — Evrony fidelity / co-presence / phenotypic association.

### Multi-omic extensions

- [[30-Concepts/got]], [[30-Concepts/got-cha]] — genotype-phenotype linking on droplet platforms.
- [[30-Concepts/daf-seq]] — single-molecule chromatin + DNA sequence.
- [[30-Concepts/gt-seq]] — physical separation of DNA and RNA.

### Applications

- [[30-Concepts/somatic-mosaicism]]
- [[30-Concepts/lineage-tracing]]
- [[30-Concepts/clonal-hematopoiesis]]
- [[30-Concepts/developmental-mutation-timing]]

## Key entities

- [[20-Entities/diane-d-shao]] — first author of the keystone 2025 review.
- [[20-Entities/christopher-walsh]] — Walsh lab; brain mosaicism program.
- [[20-Entities/charles-gawad]] — foundational 2016 review; pediatric oncology methods.
- [[20-Entities/stephen-quake]] — microfluidic single-cell genomics pioneer.
- [[20-Entities/gilad-evrony]] — applications-framework architect.
- [[20-Entities/dan-a-landau]] — Landau Lab; GoT / GoT–ChA methods.
- [[20-Entities/thierry-voet]] — G&T-seq; KU Leuven LISCO.
- [[20-Entities/andrew-b-stergachis]] — Fiber-seq / DAF-seq lineage.

## Sources, by sub-theme

### Methods reviews (scDNA-seq landscape)

- [[10-Summaries/shao-2025-scDNA-mosaicism-review]] — keystone 2025 review; current state of the field.
- [[10-Summaries/gawad-2016-scgenome-review]] — foundational 2016 review; pre-PTA landscape.
- [[10-Summaries/evrony-2021-scDNA-applications-review]] — applications/capabilities framework.

### Multi-omic extensions (primary papers)

- [[10-Summaries/nam-2019-got]] — GoT method paper.
- [[10-Summaries/izzo-2024-got-cha]] — GoT–ChA method paper.
- [[10-Summaries/swanson-2025-daf-seq]] — DAF-seq / scDAF-seq method paper.

### Multi-omics surveys

- [[10-Summaries/vandereyken-2023-scmultiomics-review]] — single-cell and spatial multi-omics methods.
- [[10-Summaries/baysoy-2023-multiomics-landscape]] — multi-omics technological landscape.
- [[10-Summaries/heumos-2023-best-practices]] — best practices for single-cell analysis.

## Synthesized notes

_None yet — natural promotion targets: (a) droplet-scale vs single-molecule scDNA-seq tradeoffs; (b) the PTA inflection point that enabled current applications; (c) "what capability does my question need?" decision tree from the Evrony framework._

## Open questions

- Where does scDAF-seq (single-cell, single-molecule, ~99% genome) win over GoT–ChA (10⁵ cells, single chromatin modality)? ([[10-Summaries/swanson-2025-daf-seq]] vs [[10-Summaries/izzo-2024-got-cha]])
- Throughput vs depth: DLP+ scales to >10⁴ cells at very low coverage; PTA peaks at ~384 cells at ~95%. The right operating point for a given biological question is rarely benchmarked.
- Can single-cell duplex sequencing be made cost-competitive for cohort-scale studies?
- How well does imputation-based multi-omic integration (e.g., GoT–ChA + DOGMA via mt-variant bridges) generalize beyond MPN?
- Is there a "single-molecule, per-fiber" extension of GoT / GoT–ChA waiting to be built — the analog to what DAF-seq is to Fiber-seq?

## Linked summaries (lint pass 2026-05-21)

- [[10-Summaries/garvin-2015-natmethods]] — Garvin 2015 — Ginkgo: interactive analysis of single-cell CNVs.
- [[10-Summaries/wang-2020-scope]] — Wang 2020 — SCOPE: normalization and copy-number estimation for scDNA-seq.

