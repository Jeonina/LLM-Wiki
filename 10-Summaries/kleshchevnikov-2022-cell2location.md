---
type: summary
title: "Kleshchevnikov et al. 2022 — Cell2location maps fine-grained cell types in spatial transcriptomics"
source: "[[00-Sources/papers/Cell2location maps fine-grained cell types in spatial transcriptomics]]"
source_kind: paper
author: "Vitalii Kleshchevnikov, Artem Shmatko, Emma Dann, … Roser Vento-Tormo, Moritz Gerstung, Louisa James, Oliver Stegle, Omer Ali Bayraktar (corresponding)"
published: 2022-01-13
ingested: 2026-08-17
doi: "10.1038/s41587-021-01139-4"
journal: "Nature Biotechnology 40:661–671"
tags: [cell2location, deconvolution, Bayesian, spatial-transcriptomics, astrocyte-subtypes, germinal-center, lymphoid-follicle]
entities: ["[[oliver-stegle]]"]
concepts: ["[[spatial-multiomics]]", "[[multimodal-integration-methods]]", "[[cell-type-annotation]]", "[[pseudo-bulk]]"]
topics: ["[[single-cell-multiomics]]", "[[computational-methods]]"]
---

**Citation:** Kleshchevnikov et al. (2022) — *Cell2location maps fine-grained cell types in spatial transcriptomics* — *Nature Biotechnology* 40, 661–671. [DOI](https://doi.org/10.1038/s41587-021-01139-4)

# Kleshchevnikov 2022 — cell2location

> Spot-based spatial transcriptomics measures **mixtures**, not cells. cell2location is the Bayesian deconvolution answer: estimate the abundance of each reference cell type at each location, **accounting for technical variation** and **borrowing statistical strength across locations** — the second of which is what lets it resolve *fine-grained* subtypes that per-spot methods cannot.

## Key claims

- **Borrowing strength across locations is the mechanism.** A single spot has too few counts to distinguish closely related subtypes; a model that shares information across the tissue can, because subtypes have spatially coherent distributions.
- **Technical variation is modelled explicitly**, not normalised away beforehand.
- **Three tissues, three kinds of hard result**: (1) mouse brain — fine **regional astrocyte subtypes** across thalamus and hypothalamus, i.e. subtypes of a cell class usually treated as homogeneous; (2) human lymph node — spatial mapping of a **rare pre-germinal-center B cell population**; (3) human gut — fine immune populations resolved within lymphoid follicles.
- **Higher sensitivity and resolution than existing tools** for integrating single-cell and spatial transcriptomics.
- Positioned as a general-purpose tool for mapping tissue architecture comprehensively, not a single-tissue method.

## Methods / evidence

Bayesian model evaluated on three tissues chosen to pose different difficulties — regional gradients within a glial class, a rare transient B-cell state, and dense immune structure. Validation is by recovery of known anatomy plus discovery of populations verifiable against independent single-cell references.

Weight: the three-tissue design is the strength. As with all deconvolution methods, the answer is conditional on the single-cell reference supplied — a subtype absent from the reference cannot be mapped.

## Surprising or load-bearing bits

- **Deconvolution and alignment are different problems with different failure modes.** [[biancalani-2021-tangram|Tangram]] maps *individual cells* onto positions; cell2location estimates *proportions* per location. When spots contain many cells, proportions are the honest output; when the technology approaches single-cell resolution, mapping is. Which tool is appropriate is a property of the assay, not a matter of taste. (synthesis)
- **Rare-population recovery is the demanding test**, and pre-germinal-center B cells are a good one: transient, low-abundance, and transcriptionally close to their neighbours. Statistical strength across locations is exactly what makes this possible.
- **Astrocyte regional subtypes** is a biological finding delivered by a methods paper — the discovery that a "uniform" glial class has spatially patterned states.
- **The reference dependency is structural.** Deconvolution answers "how much of each *known* type is here", so novel or reference-absent states are silently redistributed among known ones. The same limitation applies to [[kang-2021-symphony|Symphony]]'s frozen reference and to [[song-2021-scgcn|scGCN]]'s label transfer — the whole reference-based family shares it. (synthesis)
- **Stegle and Gerstung as coauthors** connect this to the probabilistic-modelling line that also produced [[argelaguet-2020-mofa-plus|MOFA+]].

## Entities mentioned

- [[oliver-stegle]] — coauthor; Bayesian latent-variable models for genomics.

## Concepts touched

- [[spatial-multiomics]] — deconvolution as the complement to alignment.
- [[cell-type-annotation]] — cell-type abundance rather than per-cell labels.

## Connections to other sources

- Alignment-based counterpart, published three months earlier: [[biancalani-2021-tangram]].
- Used as a baseline (via the RCTD family of deconvolution approaches) by [[debnath-2026-ison]].
- Probabilistic-modelling relatives: [[argelaguet-2020-mofa-plus]], [[gayoso-2021-totalvi]], [[ashuach-2023-multivi]].
- Spatial assay landscape: [[zhao-2022-nature]] (slide-DNA-seq), [[cardilla-2025-spatial-methylome]], [[andrewc-2020-science]] (in-situ genome sequencing), [[vandereyken-2023-spatial-multiomics]].
- Reference-dependent methods sharing its structural limitation: [[kang-2021-symphony]], [[song-2021-scgcn]].
- Best practices: [[heumos-2023-best-practices]].

## Open questions

- **Reference completeness bounds everything.** No deconvolution method can report a cell type it was not given.
- Fine-grained subtype resolution depends on how distinguishable subtypes are in the reference; the limit is not characterised as a function of transcriptional distance.
- Spatial coherence is used as statistical strength, which risks smoothing away genuinely scattered rare cells — the flip side of the mechanism that finds rare *clustered* ones. (synthesis)

## Related

- [[biancalani-2021-tangram]] · [[spatial-multiomics]] · [[40-Topics/single-cell-multiomics]]
