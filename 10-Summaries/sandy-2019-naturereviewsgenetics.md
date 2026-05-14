---
type: summary
title: "Klemm, Shipony & Greenleaf 2019 — Chromatin accessibility and the regulatory epigenome"
source: "[[00-Sources/papers/Sandy_2019_NatureReviewsGenetics]]"
source_kind: paper
author: "Sandy L. Klemm, Zohar Shipony, William J. Greenleaf"
published: 2019-04
ingested: 2026-05-11
doi: "10.1038/s41576-018-0089-8"
journal: "Nature Reviews Genetics 20:207–220"
tags: [review, chromatin-accessibility, atac-seq, dnase-seq, regulatory-epigenome]
entities:
  - "[[20-Entities/william-greenleaf]]"
concepts:
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/atac-seq]]"
  - "[[30-Concepts/dnase-seq]]"
  - "[[30-Concepts/single-molecule-footprinting]]"
topics:
  - "[[40-Topics/chromatin-architecture]]"
---

# Klemm, Shipony & Greenleaf 2019 — Chromatin accessibility and the regulatory epigenome

> Thesis: chromatin accessibility — the physical access of macromolecules to chromatinized DNA — is a dynamic, regulated state that integrates nucleosome occupancy, TF binding, and architectural proteins. ~2–3% of the genome is accessible, but it captures >90% of TF binding. Accessibility is both an *output* of cell identity (reflecting TF-nucleosome competition) and an *input* to gene regulation, making it the most informative single epigenetic readout of regulatory state.

## Key claims

- **Accessibility = TF–nucleosome competition.** Nucleosomes occlude DNA; TFs displace nucleosomes through binding. The accessibility landscape reflects the *dynamic equilibrium* of this competition, not a static structure.
- **ENCODE finding**: ~2–3% of the genome is in accessible chromatin, but this 2–3% contains >90% of TF binding events. Accessibility is a near-complete proxy for regulatory potential.
- **Three measurement chemistries**:
  - **DNase-seq** — DNase I hypersensitive sites; original ENCODE assay.
  - **ATAC-seq** — Tn5 transposase tagmentation into accessible regions; high-efficiency (works with ~500 cells), simple workflow.
  - **MNase-seq / NOMe-seq / footprinting variants** — methyltransferase- and nuclease-based methods including the precursors of [[fiber-seq]] and [[daf-seq]].
- **Pioneer factors** initiate accessibility remodeling at otherwise nucleosome-bound sites by penetrating compact chromatin.
- **Single-cell ATAC-seq** (scATAC-seq) and single-molecule approaches enable per-cell and per-fiber resolution — the techniques on which [[got-cha]] and [[daf-seq]] subsequently build.
- **Most accessible regions are distal enhancers** (>80%), not promoters — the regulatory action is in long-range contacts.

## Methods / evidence

Comprehensive synthesizing review. Greenleaf lab is the originating group for ATAC-seq (Buenrostro et al. 2013), so this review reflects deep methodological ownership of the field.

## Surprising or load-bearing bits

- **ATAC-seq's 500-cell input requirement** democratized chromatin profiling — DNase-seq required millions of cells, restricting it to bulk tissue and cell lines. ATAC-seq made chromatin profiling possible for clinical samples and ultimately for single cells (scATAC-seq) and droplet-scale platforms.
- **Accessibility as TF-nucleosome equilibrium** (not as a static state) is the conceptual frame for understanding how transient stimuli can rapidly remodel chromatin. This frames [[10-Summaries/franco-2024-nature]]'s JAK2V617F findings: pro-inflammatory TF activity shifts the equilibrium, producing the observed accessibility changes.
- **The 80%-distal observation**: regulatory elements are mostly far from promoters, which has consequences for variant interpretation and for chromatin-conformation methods.

## Entities mentioned

- [[20-Entities/william-greenleaf]] — senior author; Stanford; co-developer of ATAC-seq.

## Concepts touched

- [[30-Concepts/chromatin-accessibility]] — central concept; this review is the canonical reference.
- [[30-Concepts/atac-seq]] — defined here in the field-review context.
- [[30-Concepts/dnase-seq]] — predecessor assay.
- [[30-Concepts/single-molecule-footprinting]] — emerging at time of writing; now mature in [[10-Summaries/elliott-2025-naturebiotechnology]].

## Connections to other sources

- **Methodological foundation for** [[10-Summaries/franco-2024-nature]] (GoT–ChA — droplet scATAC with genotype integration) and [[10-Summaries/elliott-2025-naturebiotechnology]] (DAF-seq — single-molecule footprinting at chromosome scale).
- **Complementary to** [[10-Summaries/alev-2023-naturereviewsmolecularcellbiology]] and [[10-Summaries/katy-2023-naturereviewsgenetics]] — both later multi-omics reviews cover chromatin as one of several modalities.

## Open questions

- TF footprinting from chromatin accessibility data is statistically subtle — different methods produce different footprint calls. (The single-molecule resolution of [[daf-seq]] partly addresses this.)
- How accessibility relates to 3D genome organization — touched on but not the focus of this review.
- Single-cell quantitative dynamics — how fast does accessibility change in response to perturbation? Largely an open question for biology, partially addressable now with paired multi-omic time courses.

---
**Source:** [DOI](https://doi.org/10.1038/s41576-018-0089-8)
