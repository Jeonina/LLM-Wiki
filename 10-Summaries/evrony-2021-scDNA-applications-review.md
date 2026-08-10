---
type: summary
title: "Evrony, Hinch & Luo 2021 — Applications of single-cell DNA sequencing"
source: "[[00-Sources/papers/Applications of Single-Cell DNA Sequencing]]"
source_kind: paper
author: "Gilad D. Evrony, Anjali Gupta Hinch, Chongyuan Luo"
published: 2021
ingested: 2026-05-11
doi: "10.1146/annurev-genom-111320-090436"
journal: "Annual Review of Genomics and Human Genetics 22:171–197"
tags: [review, scDNA-seq, applications-framework, somatic-mosaicism, lineage-tracing]
entities:
  - "[[20-Entities/gilad-evrony]]"
concepts:
  - "[[40-Topics/scdna-seq]]"
  - "[[40-Topics/somatic-mosaicism]]"
  - "[[30-Concepts/lineage-tracing]]"
  - "[[30-Concepts/scdna-capabilities-framework]]"
topics:
---

**Citation:** Evrony et al. (2021) — *Applications of single-cell DNA sequencing* — *Annu Rev Genomics Hum Genet*. [DOI](https://doi.org/10.1146/annurev-genom-111320-090436)

# Evrony, Hinch & Luo 2021 — Applications of single-cell DNA sequencing

> Thesis: rather than reviewing scDNA-seq technologies, frame the field through three core *capabilities* that scDNA-seq uniquely enables across applications: **fidelity** (detecting low-mosaicism features below the noise floor of bulk sequencing), **co-presence** (determining which variants co-occur in the same cell), and **phenotypic association** (linking single-cell genotype to single-cell phenotype). Every scDNA-seq application is distinguished by which subset of these capabilities it depends on.

## Key claims

- **Fidelity capability**: bulk sequencing error is a constant fraction of coverage, so detection of rare variants is fundamentally floor-limited. scDNA-seq breaks the floor by reading single molecules / single cells where the variant is at 100% rather than at 1/(2N) of the bulk read pool.
- **Co-presence capability**: only single-cell DNA reading tells you whether two variants are on the same haplotype/cell or different. This is the basis of clonal lineage reconstruction.
- **Phenotypic association**: linking single-cell genotype to other single-cell readouts (RNA, chromatin, surface protein, spatial location). This is the explicit goal of [[30-Concepts/got]], [[30-Concepts/got-cha]], and methods that pair scDNA with scRNA / scATAC.
- **Application catalog**: somatic mutation and mosaicism, organismal development, germ cell mutation and development, fertility, cancer, epigenetic regulation, genome organization, microbiology.
- The framework is **technology-agnostic**: it lets you ask "what capability does this question need?" before choosing whether duplex sequencing, scWGA-based scDNA-seq, or paired multi-omic measurement is the right tool.

## Methods / evidence

Conceptual/synthesizing review. Reorganizes the scDNA-seq literature around capabilities rather than chemistry.

## Surprising or load-bearing bits

- **The capabilities framework is the highest-leverage organizing principle for this corpus.** It distinguishes "what does this study need?" from "what does this method do?" — a separation the older technology-organized reviews ([[10-Summaries/gawad-2016-scgenome-review]]) collapse.
- **No single scDNA-seq method possesses all three capabilities on a genome-wide scale.** Duplex sequencing has fidelity and co-presence within a molecule but loses per-cell assignment; scWGA + scWGS has phenotypic association potential but suffers from fidelity floor due to amplification errors. Method choice is application-driven.
- **Pre-implantation genetic screening** is highlighted as a clinical application where all three capabilities matter simultaneously and where existing methods struggle.

## Entities mentioned

- [[20-Entities/gilad-evrony]] — first author; NYU. Background in human brain mosaicism (former Walsh lab).

## Concepts touched

- [[30-Concepts/scdna-capabilities-framework]] — fidelity / co-presence / phenotypic association.
- [[40-Topics/scdna-seq]]
- [[40-Topics/somatic-mosaicism]]
- [[30-Concepts/lineage-tracing]]

## Connections to other sources

- **Conceptually parallel to** [[10-Summaries/shao-2025-scDNA-mosaicism-review]] — both organize the scDNA-seq field, but Diane 2025 is technology-organized and Gilad 2021 is application/capability-organized. Reading them together gives both axes.
- **Framework applies to** [[10-Summaries/nam-2019-got]] (GoT — *phenotypic association*), [[10-Summaries/izzo-2024-got-cha]] (GoT–ChA — *phenotypic association*), [[10-Summaries/swanson-2025-daf-seq]] (scDAF-seq — *fidelity + co-presence + phenotypic association* via deamination footprints).
- **Provides the application context for** [[10-Summaries/forsberg-2017-mosaicism-review]] and [[10-Summaries/campbell-2015-mosaicism-review]] mosaicism biology.

## Open questions

- The framework is useful but applied unevenly across the field — many papers don't make explicit which capability they rely on, making method-to-application mapping fuzzier than it should be.
- As multimodal single-cell methods mature, the "phenotypic association" capability becomes a continuum rather than a binary — needs refinement.

---
**Source:** [DOI](https://doi.org/10.1146/annurev-genom-111320-090436)
