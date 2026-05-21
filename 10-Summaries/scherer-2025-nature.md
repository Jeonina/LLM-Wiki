---
type: summary
title: "Scherer 2025 — Clonal tracing with somatic epimutations reveals dynamics of blood ageing (EPI-Clone)"
source: "[[00-Sources/papers/Clonal tracing with somatic epimutations reveals dynamics of blood ageing]]"
aliases: ["EPI-Clone", "scTAM-seq lineage", "Scherer 2025"]
tags: [scTAM-seq, methylation, lineage-tracing, epimutation, hematopoiesis, clonal-hematopoiesis]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Scherer et al. (2025) — *Clonal tracing with somatic epimutations reveals dynamics of blood ageing (EPI-Clone)* — *Nature*. [DOI](https://doi.org/10.1038/s41586-025-09041-8)

Scherer, Singh, Braun and colleagues (Rodríguez-Fraticelli / Velten labs) developed EPI-Clone, a transgene-free single-cell lineage-tracing method that exploits stochastic somatic epimutations at static CpG sites as natural clonal barcodes, while simultaneously reading dynamic CpG sites as a differentiation-state readout. Built on scTAM-seq (single-cell Targeted Analysis of the Methylome, Mission Bio Tapestri platform), EPI-Clone profiles methylation of ~453 CpG sites in thousands of single cells with low dropout (~7%), distinguishing static CpGs (clone-informative, enriched in heterochromatin and late-replicating regions) from dynamic CpGs (state-informative, enriched in enhancer regions near lineage-specific TF binding sites).

Validated against LARRY-barcoded mouse HSCs, EPI-Clone correctly placed cells from expanded clones with AUC=0.79. Applied to mouse and human hematopoiesis, the platform captured hundreds of clonal differentiation trajectories across 230,358 cells from tens of individuals. In aging mice, myeloid bias and low output of old HSCs were restricted to a small number of expanded clones, while many "functionally young-like" clones persisted. In human aging, clones with and without known CHIP driver mutations participated in a continuous spectrum of age-related clonal expansions with similar lineage biases.

## Why this matters

The first method to read clonal identity and cellular state from a single methylation assay, without transgenic barcoding and without requiring driver-mutation calling. Demonstrates that the methylome itself encodes both layers of information jointly. Anchors §3.3 (DNA methylation), §5 (clonal hematopoiesis / aging applications), and the conceptual point in §2 that distinct modalities (sequence-based barcodes vs methylation-based barcodes vs natural mutations) can serve interchangeably for lineage tracing, with different trade-offs.

---
**Source:** [DOI](https://doi.org/10.1038/s41586-025-09041-8) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/40399669/)

---
**Source:** [DOI](https://doi.org/10.1038/s41586-025-09041-8) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/40399669/)

## Related

- scTAM seq
- [[30-Concepts/lineage-tracing-somatic-mutations]]
- [[30-Concepts/methylation-clones-epimutation]]
- [[10-Summaries/gaiti-2019-cll-epigenetic]]
- [[10-Summaries/coorens-2021-nature]]
