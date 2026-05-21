---
type: summary
title: "Ma 2020 — Chromatin Potential Identified by Shared Single-Cell Profiling of RNA and Chromatin (SHARE-seq)"
source: "[[00-Sources/papers/Chromatin Potential Identified by Shared Single-Cell Profiling of RNA and Chromatin]]"
aliases: ["Ma 2020", "SHARE-seq", "Buenrostro 2020 SHARE"]
tags: [SHARE-seq, joint-assay, scATAC, scRNA, chromatin-priming, Regev-lab, Buenrostro-lab]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Ma et al. (2020) — *Chromatin Potential Identified by Shared Single-Cell Profiling of RNA and Chromatin (SHARE-seq)* — *Cell*. [DOI](https://doi.org/10.1016/j.cell.2020.09.056)

Ma, Zhang, LaFave, Earl, Chiang, Hu, Ding, Brack, Kartha, Tay, Law, Lareau, Hsu, Regev and Buenrostro (Broad, Harvard, MIT) developed **SHARE-seq** (Simultaneous High-throughput ATAC and RNA Expression with sequencing), a highly scalable combinatorial-indexing protocol measuring chromatin accessibility and gene expression in the same single cell. They produced 34,774 joint profiles from mouse tissues including skin, brain and lung.

Three central findings: (1) cell states defined by chromatin and by expression are correlated but distinct — chromatin captures cell-fate priming that transcript profiles miss; (2) lineage-determining genes are marked by **Domains Of Regulatory Chromatin** (DORCs) — clusters of cis-regulatory peaks that overlap super-enhancers; (3) DORC accessibility *precedes* gene expression at lineage-commitment decisions, so chromatin "foreshadows" cell fate. The authors introduce a computational quantity called *chromatin potential* and use it to predict cell-fate outcomes.

## Why this matters

Founding paper for joint scATAC+scRNA at high throughput; technical ancestor of 10x Multiome. Establishes the empirical case that chromatin accessibility is a *predictive* (not just descriptive) feature of cell state, which directly supports our review's locus-state framework: accessibility is informative about future cell-state trajectories, not only present identity. Anchors §3.2 (Fiber-seq / accessibility) and §4 (multimodal integration). Anti-anchor for §3 conclusion: joint scATAC+scRNA exists at scale, but scATAC + scWGS at the same single cell remains unsolved.

---
**Source:** [DOI](https://doi.org/10.1016/j.cell.2020.09.056) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33098772/)

---
**Source:** [DOI](https://doi.org/10.1016/j.cell.2020.09.056) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33098772/)

## Related

- [[10-Summaries/buenrostro-2015-nature]]
- [[10-Summaries/cao-2018-sci-car]]
- argelaguet 2020 nrg
- joint assays chromatin expression
