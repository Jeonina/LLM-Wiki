---
type: summary
title: "Abdennur & Mirny 2020 — Cooler: scalable storage for Hi-C data and other genomically labeled arrays"
source: "[[00-Sources/papers/Cooler_ scalable storage for Hi-C data and other genomically labeled arrays]]"
source_kind: paper
author: "Nezar Abdennur, Leonid A. Mirny"
published: 2019-07-10
ingested: 2026-08-10
doi: "10.1093/bioinformatics/btz540"
journal: "Bioinformatics"
tags: [cooler, file-format, HDF5, sparse-matrix, COO, CSR, 4D-Nucleome, mcool, multi-resolution]
entities: ["[[leonid-mirny]]"]
concepts: ["[[single-cell-hi-c]]", "[[hi-c-normalization]]", "[[data-standards]]", "[[chromatin-compartments]]"]
topics: ["[[3d-genome]]", "[[computational-methods]]"]
---

**Citation:** Abdennur & Mirny (2020) — *Cooler: scalable storage for Hi-C data and other genomically labeled arrays* — *Bioinformatics* 36, 311–316. [DOI](https://doi.org/10.1093/bioinformatics/btz540)

# Abdennur 2020 — Cooler

> Hi-C matrices are overwhelmingly empty, and storing them densely makes storage cost grow as resolution improves. Cooler defines a **sparse, self-describing, HDF5-based format** for genomically labeled arrays: a bin table, a pixel table of non-zero elements referencing it, and a chromosome table. Adopted as the standard of the **NIH 4D Nucleome Consortium**.

## Key claims

- **The sparsity argument, quantified**: one billion contacts binned at 1 kb on the human genome fills **less than 0.03%** of the available matrix elements. Contacts also cluster near the *cis* diagonal, so density is highly non-uniform — dense storage pays for emptiness twice.
- **The data model** — genomically labeled sparse arrays (GLSA). A single BEDPE-like table duplicates bin attributes many times over; Cooler splits it into a **bin table** (one row per genomic interval, with arbitrary extra columns like normalization weights or compartment eigenvectors), a **pixel table** holding only non-zero elements as (bin1_id, bin2_id, value), and a **chromosome table**. This is the classic coordinate-list (COO) sparse representation. The same model already underlay [[servant-2015-hicpro|HiC-Pro]]'s text output.
- **Symmetric matrices store only the upper triangle**, halving the pixel table and guaranteeing a unique representation.
- **Indexing makes it a hybrid COO–CSR format**: pixels are sorted lexicographically by bin1 then bin2, so the bin1_id column can be replaced by an offset array (`indexes/bin1_offset`, the CSR `indptr`), giving row-level random access. A parallel `chrom_offset` indexes the bin table.
- **HDF5 chosen deliberately over custom binary formats** (butlr, `.hic`, MRH): those organize data efficiently and permit random access, but their **strict byte layouts cannot accommodate new data types or metadata**. HDF5 is self-describing and hierarchical, so the format can absorb new columns and annotations without a spec revision.
- **Column-oriented storage** (a table is a group of equal-length 1D arrays) rather than HDF5 compound types — chosen for cheap column addition/removal, efficient column slicing and better compression. The trade is no random row insertion, judged acceptable because raw datasets are write-once.
- **Flavors**: a standard single-resolution `.cool`, and a multi-resolution **`.mcool`** ("zoomified") holding several resolutions in one file, which is what makes interactive multiscale browsing in [[kerpedjiev-2018-higlass|HiGlass]] possible.
- Ships a Python library and a CLI (`cload` to aggregate paired tags, `load` for pre-binned matrices, plus coarsen, merge, balance and range-query commands), with 2D range selectors materializing results as NumPy arrays, SciPy sparse matrices or pandas data frames.

## Methods / evidence

A specification paper: the argument is the data model plus the published schema, supported by supplementary size/sparsity comparisons against dense HDF5 alternatives. The strongest external evidence is adoption — 4D Nucleome standardization and the tool ecosystem (HiGlass, cooltools, HiCExplorer) that reads it.

## Surprising or load-bearing bits

- **Sparse storage is not only about disk.** The paper's sharper point is algorithmic: matrix balancing and PCA can be **adapted to operate on non-zero elements alone**, so the format choice determines which algorithms are feasible at high resolution. Dense storage does not just cost space, it forecloses analysis.
- **Extra columns on the bin table are where derived signals live** — normalization weights, A/B compartment eigenvectors — travelling with the matrix rather than in a separate file. That is a small design decision with an outsized effect on reproducibility: the balancing weights that produced a figure are inside the file.
- **`.mcool` is why multiscale browsing works at all.** Zoom levels are precomputed and stored, so panning a Hi-C map behaves like panning a road map instead of re-binning on demand — the direct enabler of [[kerpedjiev-2018-higlass|HiGlass]]'s interaction model.
- **Directly relevant to single-cell Hi-C**: per-cell maps from [[ramani-2017-scihi-c|sciHi-C]] hold ~8,000 contacts each, so a dense representation is essentially all zeros. The format's design target — arbitrary sparsity patterns and any resolution — is what makes thousands of single-cell coolers tractable, and imputation methods like [[zhou-2019-schicluster|scHiCluster]] and [[zhang-2022-higashi|Higashi]] read and write them.
- The model is explicitly **not Hi-C-specific**: any binned pairwise genomic association (linkage disequilibrium, genetic interaction) fits. Naming the abstraction rather than the assay is why it generalized.
- The `::` resource-path syntax (file path plus HDF5 group path) means one file can hold many named matrices — resolutions, replicates, conditions — addressed individually.

## Entities mentioned

- [[leonid-mirny]] — co-author; also co-author of [[lieberman-aiden-2009-hic]] and the polymer-physics side of the field.

## Concepts touched

- [[data-standards]] — a community standard adopted by consortium rather than imposed by a single tool.
- [[hi-c-normalization]] — balancing weights stored as bin-table columns alongside the data.

## Connections to other sources

- Data model inherited from [[servant-2015-hicpro]]; competing binary format from [[durand-2016-juicer]] (`.hic`).
- Visualization built directly on it: [[kerpedjiev-2018-higlass]].
- Single-cell consumers: [[ramani-2017-scihi-c]], [[zhou-2019-schicluster]], [[zhang-2022-higashi]].
- Assay origin: [[lieberman-aiden-2009-hic]].

## Open questions

- Two standards coexist — `.cool`/`.mcool` and Juicer's `.hic` — so conversion remains a routine step and tool compatibility remains a practical constraint. The paper argues for interoperability but does not resolve the split.
- No random row insertion means incremental updates to a cooler require rewriting; a genuine limitation for streaming or continuously accumulating datasets, acknowledged as an accepted trade.

## Related

- [[kerpedjiev-2018-higlass]] · [[servant-2015-hicpro]] · [[single-cell-hi-c]] · [[3d-genome]]
