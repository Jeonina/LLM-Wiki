---
type: topic
title: Single-cell DNA sequencing (scDNA-seq)
aliases: [single-cell DNA sequencing, scDNA-seq, scDNAseq]
tags: [single-cell, scDNA-seq, methods]
created: 2026-05-11
updated: 2026-06-29
---

# Single-cell DNA sequencing (scDNA-seq)

> Umbrella term for technologies that interrogate the DNA of single cells — either by amplifying single-cell genomes ([[scwga]] + scWGS) or by reading single DNA molecules with strand-paired error correction ([[40-Topics/duplex-sequencing]]) — providing single-cell-level resolution of somatic genomic variation that bulk DNA sequencing cannot detect.

Two decades of technological iteration brought the field from low-coverage DOP-PCR (2008) through MDA / MALBAC (2010s) to PTA + duplex sequencing (2020s), finally making routine human-tissue mosaicism and lineage-tracing studies feasible ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). The topic is organized by **capability** ([[30-Concepts/scdna-capabilities-framework]]) rather than purely by chemistry — fidelity, co-presence, phenotypic association — and by **application**: mosaicism, lineage tracing, cancer clonal evolution, pre-implantation screening, microbial dark matter ([[10-Summaries/evrony-2021-scDNA-applications-review]]).

## The two methodological branches

scDNA-seq encompasses two methodological branches ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]):

1. **scWGA + scWGS** — amplify the single-cell genome via [[scwga]] (DOP-PCR, MDA, PTA, MALBAC, LIANTI, DLP+, etc.) then perform standard short-read or long-read sequencing on the amplicon. Variants are assigned to specific cells but suffer amplification-induced errors (allelic dropout, single-strand dropout, polymerase error) ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
2. **Single-molecule duplex sequencing** — barcode both Watson and Crick strands of bulk DNA and sequence them paired; variants must agree across strands to be called, achieving error rates as low as ~10⁻¹⁶ (HiDEF-seq) ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). Most variants can be detected only at the per-molecule level, not assigned to specific cells — except [[meta-cs]], which performs duplex sequencing on single cells ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

[[10-Summaries/evrony-2021-scDNA-applications-review]] frames the scDNA-seq design space through three capabilities: **fidelity** (detecting low-mosaicism variants), **co-presence** (which variants co-occur in the same cell), and **phenotypic association** (linking genotype to other modalities like RNA, chromatin, protein) ([[10-Summaries/evrony-2021-scDNA-applications-review]]).

## Why it matters

The human genome is 20–50× larger than the transcribed or chromatin-accessible genomes, and each genomic locus has only two molecules per cell, so scDNA-seq requires either amplification (introducing errors) or single-molecule chemistry (sacrificing per-cell assignment) ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). For two decades this was the major obstacle — scRNA-seq and scATAC-seq matured years ahead of scDNA-seq for this reason ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Core concepts

### The technology

- [[30-Concepts/scwga]] — whole-genome amplification, the central technical challenge.
- [[30-Concepts/mda]], [[30-Concepts/pta]], [[30-Concepts/malbac]], [[30-Concepts/dop-pcr]], [[30-Concepts/dlp-plus]], [[30-Concepts/meta-cs]] — specific WGA methods; LIANTI and PicoPLEX also belong to the scWGA + scWGS branch ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- [[40-Topics/duplex-sequencing]] — single-molecule error correction; the single-molecule branch also includes BotSeqS, NanoSeq, CODEC, HiDEF-seq, and SMM-seq, plus [[meta-cs]] for single-cell duplex ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- [[30-Concepts/scdna-capabilities-framework]] — Evrony fidelity / co-presence / phenotypic association ([[10-Summaries/evrony-2021-scDNA-applications-review]]).

### Multi-omic extensions

- [[30-Concepts/got]], [[30-Concepts/got-cha]] — genotype-phenotype linking on droplet platforms ([[got]] = genotype + RNA; [[got-cha]] = genotype + chromatin) ([[10-Summaries/nam-2019-got]], [[10-Summaries/izzo-2024-got-cha]]).
- [[30-Concepts/daf-seq]] — single-molecule chromatin + DNA sequence ([[10-Summaries/swanson-2025-daf-seq]]).
- [[30-Concepts/gt-seq]] — physical separation of DNA and RNA ([[gt-seq]]).

### Applications

- [[40-Topics/somatic-mosaicism]] — detection of low-VAF variants in single cells ([[10-Summaries/forsberg-2017-mosaicism-review]], [[10-Summaries/campbell-2015-mosaicism-review]]).
- [[30-Concepts/lineage-tracing]] — natural mutation accumulation (~2–4 per division) as endogenous lineage markers in human tissue ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- [[40-Topics/clonal-hematopoiesis]]
- [[30-Concepts/developmental-mutation-timing]]
- **Pre-implantation genetic screening** — aneuploidy and CNV detection from single embryonic cells ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- **Cancer subclonal evolution** — joint detection of mutations and inference of clonal hierarchy ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

### Worked examples

- Walsh lab tracking human cortical neuron lineages via [[pta]] of single neurons ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- 40% of mid-gestation human prenatal neurons harbor complex CNV (Diane 2025 preprint reference) ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- 49% of single cells in human early cleavage-stage embryos shown aneuploid by DOP-PCR ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

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

### Mosaicism context

- [[10-Summaries/forsberg-2017-mosaicism-review]] — somatic mosaicism review.
- [[10-Summaries/campbell-2015-mosaicism-review]] — somatic mosaicism review.

### Copy-number tooling (lint pass 2026-05-21)

- [[10-Summaries/garvin-2015-natmethods]] — Garvin 2015 — Ginkgo: interactive analysis of single-cell CNVs.
- [[10-Summaries/wang-2020-scope]] — Wang 2020 — SCOPE: normalization and copy-number estimation for scDNA-seq.

## Synthesized notes

_None yet — natural promotion targets: (a) droplet-scale vs single-molecule scDNA-seq tradeoffs; (b) the PTA inflection point that enabled current applications; (c) "what capability does my question need?" decision tree from the Evrony framework._

## Open questions

- Where does scDAF-seq (single-cell, single-molecule, ~99% genome) win over GoT–ChA (10⁵ cells, single chromatin modality)? ([[10-Summaries/swanson-2025-daf-seq]] vs [[10-Summaries/izzo-2024-got-cha]])
- Throughput vs depth: PTA peaks at ~384 cells at ~95% coverage while DLP+ scales to >10,000 cells at very low per-cell coverage; the right operating point for a given biological question is rarely benchmarked ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- The "fidelity vs co-presence vs phenotypic association" tradeoff means no single method is universally best ([[10-Summaries/evrony-2021-scDNA-applications-review]]).
- Cost: duplex sequencing and PTA are both ~$5–20/cell, keeping cohort-scale studies expensive — can single-cell duplex sequencing be made cost-competitive? ([[10-Summaries/shao-2025-scDNA-mosaicism-review]])
- How well does imputation-based multi-omic integration (e.g., GoT–ChA + DOGMA via mt-variant bridges) generalize beyond MPN?
- Is there a "single-molecule, per-fiber" extension of GoT / GoT–ChA waiting to be built — the analog to what DAF-seq is to Fiber-seq?

## Related

- [[scwga]]
- [[40-Topics/duplex-sequencing]]
- [[mda]], [[pta]], [[malbac]], [[dop-pcr]], [[dlp-plus]], [[meta-cs]]
- [[40-Topics/somatic-mosaicism]]
- [[lineage-tracing]]
- [[scdna-capabilities-framework]]
- [[40-Topics/whole-genome-amplification]]
