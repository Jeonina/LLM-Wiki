---
type: summary
title: "Yeung et al. 2023 — scChIX-seq: computational deconvolution of two histone marks per cell"
source: "[[00-Sources/papers/scChIX-seq infers dynamic relationships between histone modifications in single cells]]"
source_kind: paper
author: "Jake Yeung, Maria Florescu, Peter Zeller, Buys Anton de Barbanson, Max D. Wellenstein, Alexander van Oudenaarden (corresponding)"
published: 2023-01-02
ingested: 2026-05-12
doi: "10.1038/s41587-022-01560-3"
journal: "Nature Biotechnology"
tags: [single-cell, histone-modifications, multi-modal, sortChIC, LDA, mouse-bone-marrow, macrophage]
entities:
  - "[[20-Entities/alexander-van-oudenaarden]]"
  - "[[20-Entities/jake-yeung]]"
concepts:
  - "[[30-Concepts/scchix-seq]]"
  - "[[30-Concepts/sortchic]]"
  - "[[30-Concepts/latent-dirichlet-allocation]]"
  - "[[40-Topics/histone-modifications]]"
  - "[[30-Concepts/chromatin-velocity]]"
topics:
  - "[[40-Topics/single-cell-multiomics]]"
---

**Citation:** Yeung et al. (2023) — *scChIX-seq: computational deconvolution of two histone marks per cell* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-022-01560-3)

# Yeung et al. 2023 — scChIX-seq

> Thesis: Most single-cell histone-modification methods (scChIC-seq, scCUT&Tag, scCUT&RUN) profile one mark per cell, forcing inter-cell comparisons across separate experiments. **scChIX-seq** multiplexes two histone-mark antibodies in the same cell during sortChIC, then computationally **deconvolves the superimposed cut-site profiles** using single-incubated training datasets — assigning each fragment probabilistically to its source mark. This unlocks **per-cell relationships between marks** (mutually exclusive vs co-occurring) and supports "chromatin velocity" analysis.

## Key claims

- **Three-dataset design**: two single-incubated reference datasets (one antibody each) + one double-incubated test dataset. LDA learns cell-type-specific topic models for each mark separately; the deconvolution step selects which pair of LDA topic combinations best fits each double-incubated cell.
- **Per-fragment assignment** via parameter *p* (expected fraction of fragments at a locus belonging to mark 1). p=0 or p=1 = locus is mark-specific; p=0.5 = co-occurring.
- **Simulation benchmark**: handles mutually exclusive (1% overlap), intermediate (50%), and correlated (99%) cases. Confidence intervals ±0.05.
- **Validated on H3K27me3 + H3K9me3** in FACS-sorted mouse bone marrow B cells, granulocytes, NK cells. FDRs of 10%, 3%, 1% respectively. Recovers known mutually exclusive relationship; finds cell-type-specific transitions at *Bcl2* and *Crim1* loci. H3K9me3-specific regions have lower GC content and longer distance to TSS than H3K27me3-specific regions (consistent with established biology).
- **H3K4me1 + H3K27me3** in bone marrow: joint UMAP transfers cell labels between modalities; resolves pro-B vs B cells via *IgK*-locus chromatin transitions consistent with B-cell development.
- **Macrophage in vitro differentiation**: coordinated H3K4me1 and H3K36me3 dynamics + computed **chromatin velocity** linking active marks.

## Methods / evidence

sortChIC platform (FACS + pA-MNase) with antibody multiplexing. LDA topic modeling per single-incubated dataset. Statistical deconvolution: cluster-pair selection + per-fragment probabilistic assignment. Comparison to multi-CUT&TAG shows higher fragments-per-cell sensitivity.

## Surprising or load-bearing bits

- The **training-data-driven deconvolution** approach is the methodological insight: instead of trying to label antibodies independently (chemically hard), let the chromatin profile itself disambiguate. Works because pure H3K27me3 and pure H3K9me3 cells have different enough genome-wide patterns to fit two distinct LDA models.
- **Chromatin velocity** — coordinated dynamics of marks within a single cell over a differentiation trajectory — is conceptually analogous to RNA velocity but for the chromatin layer. Suggestive of a unified framework for multi-modal velocity.

## Connections to other sources

- Methodological precursor: [[10-Summaries/ku-2019-scchic-seq]] (scChIC-seq, single-mark version from Zhao lab).
- Same lab as [[10-Summaries/geisenberger-2025-scepi2-seq]] (scEpi²-seq, van Oudenaarden), which adds 5mC to the sortChIC framework. scChIX + scEpi² → joint histone + histone + 5mC in single cells is the implicit roadmap.
- Compares favorably to multi-CUT&TAG (Henikoff lab) — see [[10-Summaries/janssens-2023-scicut-tag]].
- LDA used here is the same algorithm as [[10-Summaries/bravo-2019-cistopic]] (cisTopic) — a notable instance of topic modeling generalizing across single-cell modalities.

## Open questions

- Requires per-pair training datasets; cost scales with the number of mark combinations.
- Deconvolution accuracy degrades as the two marks become more correlated; in the limit of fully overlapping marks, the method cannot distinguish them.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-022-01560-3)
## Related

- [[40-Topics/histone-modifications]] · [[30-Concepts/scchix-seq]] · [[30-Concepts/sortchic]] · [[30-Concepts/chromatin-velocity]] · [[20-Entities/alexander-van-oudenaarden]]
