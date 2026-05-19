---
type: summary
title: "Nagano 2013 — Single-cell Hi-C reveals cell-to-cell variability in chromosome structure"
source: "[[00-Sources/papers/Single-cell Hi-C reveals cell-to-cell variability in chromosome structure]]"
aliases: ["Nagano 2013", "scHi-C founding paper", "single-cell Hi-C"]
tags: [3D-genome, scHi-C, chromosome-conformation, Fraser-lab, Tanay-lab, Babraham]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Nagano et al. (2013) — *Single-cell Hi-C reveals cell-to-cell variability in chromosome structure* — *Nature*. [DOI](https://doi.org/10.1038/nature12593)

Nagano, Lubling, Stevens, Schoenfelder, Yaffe, Dean, Laue, Tanay and Fraser (Babraham, Weizmann, Cambridge) reported the founding single-cell Hi-C method. They modified the ensemble Hi-C protocol to perform chromatin cross-linking, BglII digestion, biotin fill-in, and proximity ligation *inside intact nuclei* rather than after dilution, then physically isolated individual nuclei under the microscope, reversed cross-links, and purified biotinylated ligation junctions. A second restriction (AluI) and unique 3-bp barcoded adapters allowed multiplexed Illumina sequencing of single-cell libraries.

Applied to mouse CD4+ Th1 cells, the method recovered up to ~30,000 distinct fragment-end pairs per cell. Single-cell Hi-C maps showed that megabase-scale topologically-associating-domain organization is largely preserved cell-to-cell, but larger-scale (chromosome-territory and inter-chromosomal) conformations are highly variable. Structural modeling of single X chromosomes from individual cells revealed cell-specific 3D folds despite preserved local domain structure. Active gene domains localized preferentially to territory boundaries — a feature stable across cells.

## Why this matters

Founding paper for single-cell 3D genome assay; the methodological ancestor of all later sciHi-C (Ramani 2017), Dip-C (Tan 2018), and sn-m3C-seq (Lee 2019) protocols. Establishes the central biological observation that 3D chromatin organization is highly cell-state-dependent and stochastic at long range — directly motivating §3.5's framing of 3D as the most cell-state-variable locus-state layer in our review.

---
**Source:** [DOI](https://doi.org/10.1038/nature12593) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/24067610/)

---
**Source:** [DOI](https://doi.org/10.1038/nature12593) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/24067610/)

## Related

- [[10-Summaries/ramani-2017-sci-hic]]
- [[10-Summaries/tan-2018-science]]
- [[10-Summaries/lee-2019-nature]]
- [[30-Concepts/3d-genome-single-cell]]
