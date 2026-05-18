---
type: summary
title: "Chen 2025 — High-resolution, noninvasive single-cell lineage tracing in mice and humans based on DNA methylation epimutations (MethylTree)"
source: "[[00-Sources/papers/High-resolution, noninvasive single-cell lineage tracing in mice and humans based on DNA methylation epimutations]]"
aliases: ["MethylTree", "Chen 2025", "methylation lineage tracing"]
tags: [methylation, lineage-tracing, epimutation, scBS-seq, MethylTree, hematopoiesis, Wang-lab]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/High-resolution, noninvasive single-cell lineage tracing in mice and humans based on DNA methylation epimutations]]"
---

**Citation:** Chen et al. (2025) — *High-resolution, noninvasive single-cell lineage tracing in mice and humans based on DNA methylation epimutations (MethylTree)* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-024-02567-1)

Chen, Fu, Chen, Li and Wang (Westlake University) developed MethylTree, a computational framework that infers cell-lineage phylogenies from single-cell DNA-methylation epimutations in sparse scBS-seq data. The central observation is that methylation epimutations occur at $\sim$0.001 per CpG per cell division — orders of magnitude higher than somatic SNV rates — making methylation a faster molecular clock than somatic mutations, at the cost of higher noise.

MethylTree addresses three challenges: (1) cell-type-specific methylation changes during differentiation must be separated from clone-stable epimutations; (2) global methylation modulation during development can disrupt epimutation signals; (3) sparse coverage (~5% of genome per cell in scBS-seq) yields highly missing-value matrices. The method uses Pearson-correlation similarity between cells corrected for measurement-noise heterogeneity, with iterative bias-correction to maximize lineage-similarity-matrix structure. Validation on simulated and HEK 293T-derived data showed near-100\% lineage-ordering accuracy at 5\% genomic coverage. Applied to mouse and human hematopoiesis, MethylTree recapitulated the differentiation hierarchy; applied to human embryos, the method revealed early fate commitment at the four-cell stage.

## Why this matters

A second methylation-based lineage-tracing approach (alongside EPI-Clone / Scherer 2025), with the distinction that MethylTree uses sparse genome-wide scBS-seq data rather than targeted scTAM-seq. Complementary trade-offs: scTAM-seq has higher per-locus depth at $\sim$453 chosen CpGs; MethylTree-on-scBS-seq has lower depth but genome-wide coverage. Anchors §3.3 (methylation-based lineage tracing) and §5 (development + hematopoiesis applications).

---
**Source:** [DOI](https://doi.org/10.1038/s41592-024-02567-1) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/39820752/)

## Related

- [[10-Summaries/scherer-2025-nature]]
- [[10-Summaries/coorens-2021-nature]]
- [[10-Summaries/lee-six-2018-nature]]
- [[30-Concepts/methylation-clones-epimutation]]
