---
type: summary
title: "Kerpedjiev et al. 2018 — HiGlass: web-based visual exploration and analysis of genome interaction maps"
source: "[[00-Sources/papers/HiGlass_ web-based visual exploration and analysis of genome interaction maps]]"
source_kind: paper
author: "Peter Kerpedjiev, Nezar Abdennur, Fritz Lekschas, ... Leonid A. Mirny, Peter J. Park, Nils Gehlenborg (corresponding)"
published: 2018-08-24
ingested: 2026-08-10
doi: "10.1186/s13059-018-1486-1"
journal: "Genome Biology"
tags: [HiGlass, visualization, composable-linked-views, multiscale, TAD-callers, Nipbl, cohesin, 4D-Nucleome]
entities: ["[[leonid-mirny]]", "[[peter-park]]"]
concepts: ["[[topologically-associating-domain]]", "[[chromatin-compartments]]", "cohesin", "data visualization", "[[single-cell-hi-c]]"]
topics: ["[[3d-genome]]", "[[computational-methods]]"]
---

**Citation:** Kerpedjiev et al. (2018) — *HiGlass: web-based visual exploration and analysis of genome interaction maps* — *Genome Biology* 19, 125. [DOI](https://doi.org/10.1186/s13059-018-1486-1)

# Kerpedjiev 2018 — HiGlass

> Continuous pan-and-zoom over Hi-C maps, road-map style, with **composable linked views**: each view is a set of 1D and 2D tracks on shared genomic axes, and views can be arranged, resized and linked by location, by zoom, or by both — then shared as a URL.

## Key claims

- **The gap it fills.** Juicebox and Genome Contact Map Explorer allow synchronized exploration of multiple maps, but none provided an interface for **dynamically arranging views and customizing what is synchronized** (locus, zoom level, sample), and none offered continuous panning and zooming of the kind familiar from web geographic maps.
- **The linking taxonomy** is the conceptual contribution: two views may be independent, linked by both zoom and location (identical scale and position — for sample comparison), linked by zoom only (same scale, free position — for comparing distinct loci), or linked by location only (overview and detail). A **viewport projection** draws the extent of one view inside another.
- **Application 1 — cohesin loss.** Re-analysing induced Δ*Nipbl* deletion in adult mouse hepatocytes, linked views show **TADs disappearing in the gene-poor chr14:80–100 Mb region while A/B compartmental checkerboarding remains intact**, and in the gene-rich region upstream, compartmentalization is *enhanced* with a finer A/B subdivision.
- **A new feature found by browsing.** Off-diagonal "blotches" appear in the mutant: strengthened interactions between pairs of short active (A-compartment) regions, aligned with **long multi-exonic, transcriptionally active genes**. Overlaying RNA-seq and ChIP-seq tracks established the association — a finding reached by visual exploration, not by a caller.
- **Application 2 — caller comparison.** Eight linked views, each showing one TAD caller's output over the matrix it was called on, reveal **little consistency between callers and large variation in called TAD size**. Seven callers (Arrowhead, HiCseg, InsulationScore, TADBit, TADtree, Domain Caller, Armatus) are shown side by side across replicates.
- Runs at higlass.io on public data, or locally via a **Docker container** for private data, and can be **embedded as a component** in other applications. Every view composition is shareable by hyperlink.
- Motivating context: 4D Nucleome and ENCODE generating Hi-C at scale across cell lines and conditions, with the stated open challenges of unambiguous feature identification, new feature discovery, relating Hi-C features to epigenetic profiles, and assessing perturbation effects.

## Methods / evidence

A tool paper evidenced by demonstration rather than benchmark: two use cases (the Δ*Nipbl* re-analysis and the TAD-caller comparison), each with an interactive published configuration URL so the figure is reproducible as a live view. Data binned at multiple resolutions from 1 kb, served through the [[abdennur-2020-cooler|cooler]] multi-resolution format.

## Surprising or load-bearing bits

- **The TAD-caller comparison is the most consequential figure in this paper and it is a negative result about the field, not about the tool.** Seven callers on the same matrix produce inconsistent domains of widely varying size. TADs, as measured, are substantially method-dependent — which reframes every "TAD boundary" claim in this wiki as conditional on the caller. It contextualizes [[dixon-2012-tads|Dixon's]] own caveat that cell-type differences in domain calls may be noise, and it is the reason [[zhang-2022-higashi|Higashi]] reports insulation scores rather than discrete boundaries.
- **The Δ*Nipbl* result separates the two levels of 3D organization mechanistically**: removing cohesin loading erases TADs while *strengthening* compartments. TADs and compartments are not a nested hierarchy of the same process — they are produced by different mechanisms (loop extrusion vs. phase separation/affinity), and the two can move in opposite directions.
- **Visualization as a discovery instrument, not a presentation step.** The transcription-linked off-diagonal blotches were found by looking, then confirmed with tracks. Papers rarely document this honestly; here the workflow is the argument.
- **Sharing a view composition by URL is a reproducibility mechanism.** A figure whose exact data, resolution, position and linking state are recoverable from a link is a stronger artefact than a static panel — the practice worth importing regardless of tool.
- The tool depends on **precomputed multi-resolution data** ([[abdennur-2020-cooler|`.mcool`]]); the interaction model is only possible because zoom levels are stored rather than computed on demand.

## Entities mentioned

- [[leonid-mirny]], [[peter-park]] — senior co-authors; the same group behind cooler and much of 4D Nucleome's computational infrastructure.

## Concepts touched

- [[topologically-associating-domain]] — the caller-dependence result is a direct qualification of the concept.
- cohesin — the Δ*Nipbl* dissociation of TADs from compartments.
- data visualization — composable linked views as a reusable interface pattern.

## Connections to other sources

- Storage layer: [[abdennur-2020-cooler]]; pipelines producing the input: [[servant-2015-hicpro]], [[durand-2016-juicer]].
- Features being visualized: [[lieberman-aiden-2009-hic]] (compartments), [[dixon-2012-tads]] (domains).
- Disease-context maps of the kind it is used to inspect: [[lupianez-2015-tad-disruption]], [[spielmann-2018-sv-3d-genome]].

## Open questions

- **Why the TAD callers disagree is not diagnosed here** — the paper shows the inconsistency and leaves the resolution to the field. No source in this corpus settles which definition should be canonical.
- Whether the transcription-associated off-diagonal blotches are a general feature or specific to cohesin depletion is raised by analogy to two other studies and not resolved.

## Related

- [[abdennur-2020-cooler]] · [[topologically-associating-domain]] · [[dixon-2012-tads]] · [[3d-genome]]
