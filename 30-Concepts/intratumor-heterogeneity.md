---
type: concept
title: Intratumor Heterogeneity
aliases: [intratumour heterogeneity, ITH, subclonal structure, clonal architecture]
tags: [cancer, clonal-evolution, subclones, single-cell]
created: 2026-08-10
updated: 2026-08-10
---

# Intratumor Heterogeneity

> Genetic and phenotypic variation between cells within one tumour. The reason single-cell cancer genomics exists, and — importantly — a quantity whose measured magnitude depends heavily on how many cells were sequenced.

## Detection is sampling-limited

- **17 cells found no subclonal structure** in a clear cell renal carcinoma: PCA and neighbour-joining both showed diffuse diversity without discernible subpopulations, interpreted as fast malignant transition followed by passenger accumulation ([[xu-2012-single-cell-exome-kidney]]).
- **6,000 cells at 0.05× gives ~0.05% subclone sensitivity**, and costs the same as ten cells at 30× ([[zahn-2017-dlp]]). The two results are compatible; the resolution differs by two orders of magnitude (synthesis).
- Clones at 6% and 4% of a xenograft were resolvable in 296 cells, and were undetectable in the merged profile of the same libraries ([[zahn-2017-dlp]]).

## Karyotype-level heterogeneity

56% of cells in a chromosomally unstable lymphoma carried a unique karyotype, invisible to array CGH on the same tumour ([[bakker-2016-aneufinder]]); see [[chromosomal-instability]].

## Population recurrence does not predict the individual tumour

A textbook ccRCC lacked both canonical drivers — no *VHL* coding mutation, *PBRM1* only at <4% allele frequency and no chromosome 3 LOH — while genes rarely mutated at the population level (*AHNAK*, *SRGAP3*) carried high-frequency mutant alleles ([[xu-2012-single-cell-exome-kidney]]). This is the argument for individual-level rather than panel-based molecular diagnosis (synthesis).

## Consequences

- Mutations at different allele frequencies show different mutation spectra, read as selection during progression ([[xu-2012-single-cell-exome-kidney]]).
- Fitness-associated alterations can be identified from lineage structure and predict patient survival ([[wang-2021-medalt]]).
- Bulk deconvolution cannot recover what pooling destroys — the clearest demonstration being minor clones absent from a merged genome built from the very cells that contain them ([[zahn-2017-dlp]]).

## Related

- [[chromosomal-instability]] · [[copy-number-variation]] · [[phylogenetic-inference]] · [[cancer-clonal-evolution]]
