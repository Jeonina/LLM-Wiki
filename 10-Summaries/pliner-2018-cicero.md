---
type: summary
title: "Pliner et al. 2018 — Cicero predicts cis-regulatory DNA interactions from single-cell chromatin accessibility data"
source: "[[00-Sources/papers/Cicero Predicts cis-Regulatory DNA Interactions from Single-Cell Chromatin Accessibility Data]]"
source_kind: paper
author: "Hannah A. Pliner, Jonathan S. Packer, José L. McFaline-Figueroa, Darren A. Cusanovich, Riza M. Daza, Delasa Aghamirzaie, Sanjay Srivatsan, Xiaojie Qiu, Dana Jackson, Anna Minkina, Andrew C. Adey, Frank J. Steemers, Jay Shendure, Cole Trapnell (corresponding)"
published: 2018-09-06
ingested: 2026-08-10
doi: "10.1016/j.molcel.2018.06.044"
journal: "Molecular Cell"
tags: [Cicero, co-accessibility, scATAC-seq, cis-regulation, chromatin-hubs, myoblast-differentiation, enhancer-gene-linking]
entities: ["[[cole-trapnell]]", "[[jay-shendure]]"]
concepts: ["[[chromatin-accessibility]]", "[[scatac-seq]]", "[[cis-regulatory-element]]", "[[enhancer-states]]", "[[topologically-associating-domain]]"]
topics: ["[[chromatin-architecture]]", "[[computational-methods]]", "[[single-cell-multiomics]]"]
---

> ⚠️ **Source caveat.** The clipping in `00-Sources/` captured the article front matter — journal metadata, related-article links, highlights and keywords — but not the Results or Methods. The claims below are limited to what the source states; the co-accessibility statistic, benchmarks against Hi-C/ChIA-PET, and quantitative results are **not** in this source and are deliberately not asserted. Re-clip the full text before extending this page.

**Citation:** Pliner et al. (2018) — *Cicero predicts cis-regulatory DNA interactions from single-cell chromatin accessibility data* — *Molecular Cell* 71, 858–871.e8. [DOI](https://doi.org/10.1016/j.molcel.2018.06.044)

# Pliner 2018 — Cicero

> Linking a regulatory element to the gene it controls — potentially hundreds of kilobases away — is the standing difficulty in regulatory genomics. Cicero's move is to exploit variation *between cells*: peaks that open and close together across a population of single cells are inferred to be **co-accessible**, and co-accessibility is used as evidence of a *cis*-regulatory relationship.

## Key claims

*(Per the source caveat, these are the paper's stated contributions as given in its highlights and framing.)*

- **The problem**: linking regulatory DNA elements to their target genes, which may be located hundreds of kilobases away, remains challenging.
- **Cicero connects regulatory DNA elements to target genes** — from chromatin accessibility alone, with no conformation assay required.
- **Co-accessible elements form chromatin hubs** — the links are not merely pairwise but organize into groups of jointly varying elements.
- **Chromatin hubs are co-regulated during skeletal muscle development**, demonstrated in myoblast differentiation.
- Cicero can reveal the mechanisms of *cis*-regulation on a genome-wide scale.
- Published alongside the Cusanovich et al. single-cell atlas of *in vivo* mammalian chromatin accessibility from the same group — the method and the atlas-scale data it was built for arrived together.
- Framed as a machine-learning approach (per the source's keywords: chromatin accessibility, ATAC-seq, single-cell, co-accessibility, myoblast differentiation, machine learning).

## Methods / evidence

Not available from this source clipping beyond the myoblast-differentiation application named in the highlights.

## Surprising or load-bearing bits

- **Cell-to-cell variation is turned from noise into the measurement.** scATAC-seq's per-cell sparsity is normally the problem to be worked around; Cicero uses the covariance structure that sparsity creates — which elements happen to be open in the same cells — as the signal. That inverts the usual framing and is why the method needs many cells rather than deep cells.
- **It infers regulatory linkage without measuring conformation**, so it is an alternative route to the same question [[lieberman-aiden-2009-hic|Hi-C]] and its descendants address by proximity ligation. Two independent measurement modalities converging on enhancer–promoter assignment is what makes either credible; where they disagree is informative about what "interaction" means in each.
- **"Hubs" rather than pairs** matters for interpretation: if regulatory elements co-vary in groups, the enhancer–promoter relationship is many-to-many, not a set of independent links. That is the accessibility-data analogue of a [[topologically-associating-domain|TAD]] as a regulatory neighbourhood.
- **Its most consequential downstream role in this corpus is as infrastructure.** [[kamimoto-2023-celloracle|CellOracle]] uses Cicero explicitly to distinguish accessible promoters from distal enhancers when building its base gene-regulatory network, and [[bravo-2023-scenicplus|SCENIC+]] addresses the same enhancer-identification step with its own machinery. Cicero became a component of the GRN-inference stack rather than an endpoint.

## Entities mentioned

- [[cole-trapnell]] — corresponding author; Monocle lineage, which Cicero is built on top of.
- [[jay-shendure]] — co-author; the sciATAC data this was designed for.

## Concepts touched

- [[cis-regulatory-element]] — co-accessibility as evidence for element-to-gene assignment.
- [[scatac-seq]] — per-cell sparsity repurposed as the source of covariance signal.

## Connections to other sources

- Assay and atlas context: [[cusanovich-2015-sciatac]]; same-issue companion atlas from the same group.
- Consumed as a component by [[kamimoto-2023-celloracle]]; parallel approach in [[bravo-2023-scenicplus]].
- The conformation-based route to the same question: [[lieberman-aiden-2009-hic]], [[dixon-2012-tads]], [[durand-2016-juicer]].
- Region-to-gene annotation alternative: [[mclean-2010-great]].

## Open questions

- **This page is incomplete pending a full-text clipping** — the co-accessibility statistic, distance normalization, validation against conformation data, and the myoblast results are all outside the source.
- The general open question the approach raises: co-accessibility is a correlation across cells, and correlated opening does not establish physical or functional interaction. What fraction of co-accessible links correspond to real regulatory relationships is not answerable from this source.

## Related

- [[cis-regulatory-element]] · [[kamimoto-2023-celloracle]] · [[bravo-2023-scenicplus]] · [[chromatin-architecture]]
