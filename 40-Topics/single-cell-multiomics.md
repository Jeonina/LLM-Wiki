---
type: topic
title: Single-cell multi-omics
aliases: [single-cell multiomics, sc-multiomics]
tags: [single-cell, methods, multiomics]
created: 2026-05-07
updated: 2026-05-12
---

# Single-cell multi-omics

> Methods that measure two or more molecular modalities (DNA sequence, RNA, chromatin accessibility, surface protein, methylation, …) in the same single cell, enabling joint analysis that uncoupled single-modality assays cannot.

The recurring tension is **breadth vs depth**: droplet platforms scale to 10⁵+ cells but profile each modality coarsely; single-molecule and plate-based platforms profile deeply but at much lower cell number. The wiki's current sources span both ends of that spectrum.

## Core concepts

- [[30-Concepts/single-cell-multiomics]] — umbrella concept.
- [[30-Concepts/got]] — single-cell genotype + transcriptome on droplet 10x scRNA-seq.
- [[30-Concepts/got-cha]] — single-cell genotype + chromatin accessibility on droplet 10x scATAC-seq, via gDNA capture.
- [[30-Concepts/circularization-got]] — extension of GoT for distal mutation loci.
- [[30-Concepts/daf-seq]] — single-cell, single-molecule chromatin + DNA sequence at near-nucleotide resolution via deaminase footprinting.
- [[30-Concepts/fiber-seq]] — bulk single-molecule chromatin via methyltransferase stenciling; methodological ancestor of DAF-seq.
- [[30-Concepts/single-molecule-footprinting]] — the broader method class.
- [[30-Concepts/dogma-seq]] — chromatin + RNA + protein trimodal platform; integrated with GoT–ChA via imputation in [[10-Summaries/izzo-2024-got-cha]].
- [[30-Concepts/cite-seq]] — scRNA + surface protein via antibody-derived tags.
- [[30-Concepts/g-t-seq]] — G&T-seq, physical-separation scDNA + scRNA (1st joint DNA+RNA assay).
- [[30-Concepts/dr-seq]] — DR-seq, one-pot quasilinear scDNA + scRNA alternative to G&T-seq.
- [[30-Concepts/sci-car]] — sci-CAR, combinatorial-indexing scATAC + scRNA at thousands of cells.
- [[30-Concepts/share-seq]] — SHARE-seq, split-pool scATAC + scRNA at tens of thousands of cells; introduces chromatin-potential framework.
- [[30-Concepts/scnmt-seq]] — scNMT-seq, first single-cell triple-omics (methylation + accessibility + RNA).
- [[30-Concepts/sctrio-seq]] — scTrio-seq, alternative triple-omics (CNV + methylation + RNA); closest existing precedent for DNA-anchored mutation + epi + transcriptome.
- [[30-Concepts/igs]] — IGS, in-situ genome sequencing for spatial 3D-DNA at single-cell resolution.
- [[30-Concepts/gt-seq]] — alias kept for legacy backlinks; canonical page is [[30-Concepts/g-t-seq]].
- [[30-Concepts/spatial-multiomics]] — spatially-resolved multi-omic measurements.
- [[30-Concepts/chromatin-accessibility]] — readout layer.
- [[30-Concepts/chromatin-actuation]] — single-molecule refinement of accessibility.
- [[30-Concepts/simple-seq]] — joint 5mC + 5hmC in single cells.
- [[30-Concepts/splicool-seq]] — 5mC + accessibility (GpC) in single cells, high throughput.
- [[30-Concepts/scepi2-seq]] — single-cell histone mark + 5mC.
- [[30-Concepts/6-base-cut-and-tag]] — fragment-level histone mark + 5mC + 5hmC (bulk).
- [[30-Concepts/scchix-seq]] — two histone marks per cell with computational deconvolution.
- [[30-Concepts/scicut-tag]], [[30-Concepts/multi-tag]] — combinatorial-indexing single-cell CUT&Tag, multi-epitope.
- [[30-Concepts/samosa-tag]], [[30-Concepts/smrt-tag]] — long-read multi-modal chromatin.

## Key entities

- [[20-Entities/dan-a-landau]] — leads the GoT → GoT–ChA methods program at the Landau Lab.
- [[20-Entities/franco-izzo]] — first author of GoT–ChA; co-author on the original GoT.
- [[20-Entities/anna-s-nam]] — first author of the original GoT paper.
- [[20-Entities/landau-lab]] — group behind GoT, circularization GoT, and GoT–ChA.
- [[20-Entities/elliott-g-swanson]] — co-first author of DAF-seq.
- [[20-Entities/andrew-b-stergachis]] — senior author of DAF-seq and developer of Fiber-seq.
- [[20-Entities/thierry-voet]] — KU Leuven; G&T-seq co-developer.
- [[20-Entities/rong-fan]] — Yale; spatial multi-omics.
- [[20-Entities/rahul-satija]] — NYGC; Seurat integration toolkit.
- [[20-Entities/fabian-theis]] — Helmholtz Munich; best-practices recommendations.
- [[20-Entities/alexander-van-oudenaarden]] — sortChIC, scChIX-seq, scEpi²-seq.
- [[20-Entities/chengqi-yi]] — SIMPLE-seq joint 5mC+5hmC.
- [[20-Entities/xiaoying-fan]] — SpliCOOL-seq.
- [[20-Entities/shankar-balasubramanian]] — 6-base-CUT&Tag.
- [[20-Entities/steven-henikoff]] — sciCUT&Tag, MulTI-Tag.
- [[20-Entities/vijay-ramani]] — SMRT-Tag, SAMOSA-Tag.

## Sources, by sub-theme

### Foundational joint DNA + RNA assays (one cell)

- [[10-Summaries/macaulay-2015-gt-seq]] — Macaulay 2015: G&T-seq, separation-based scDNA + scRNA; trisomy-11 subclone in HCC38-BL.
- [[10-Summaries/dey-2015-dr-seq]] — Dey 2015: DR-seq, one-pot scDNA + scRNA; CNVs drive expression variability.

### Joint chromatin + RNA (accessibility-anchored)

- [[10-Summaries/cao-2018-sci-car]] — Cao 2018: sci-CAR, scATAC + scRNA at thousands of cells.
- [[10-Summaries/ma-2020-share-seq]] — Ma 2020 (NRG perspective): SHARE-seq, chromatin potential framework.

### Triple-omics (methylation + accessibility + RNA, or CNV + methylation + RNA)

- [[10-Summaries/clark-2018-scnmt-seq]] — Clark 2018: scNMT-seq, first triple-omics; methylation-accessibility coupling strengthens along differentiation.
- [[10-Summaries/hou-2016-sctrio-seq]] — Hou 2016: scTrio-seq; CNVs drive expression but not methylation; HCC subpopulation analysis.

### Spatial single-cell DNA

- [[10-Summaries/andrewc-2020-science]] — Payne 2021: IGS (In Situ Genome Sequencing); 3D-resolved single-cell genomes.

### Genotype + transcriptome (droplet)

- [[10-Summaries/nam-2019-got]] — GoT method paper; CALR-mutated MPN.

### Genotype + chromatin (droplet, gDNA capture)

- [[10-Summaries/izzo-2024-got-cha]] — GoT–ChA; JAK2V617F MPN; cell-intrinsic chromatin priming of HSCs.

### Genotype + chromatin (single-molecule, deaminase)

- [[10-Summaries/swanson-2025-daf-seq]] — DAF-seq / scDAF-seq; chromosome-length single-cell single-molecule chromatin maps.

### Reviews of the multi-omics landscape

- [[10-Summaries/baysoy-2023-multiomics-landscape]] — Baysoy/Fan/Satija technological landscape.
- [[10-Summaries/vandereyken-2023-scmultiomics-review]] — Vandereyken/Voet methods and applications, including spatial.
- [[10-Summaries/heumos-2023-best-practices]] — Heumos/Theis best-practices analysis recommendations.
- [[10-Summaries/wang-2023-multimodal-review]] — Wang/Jin methods catalog + integration tool taxonomy (matrix factorization vs manifold alignment vs deep generative).

### Methylation × chromatin / histone-mark single-cell methods

- [[10-Summaries/bai-2024-simple-seq]] (SIMPLE-seq).
- [[10-Summaries/shen-2026-splicool-seq]] (SpliCOOL-seq).
- [[10-Summaries/geisenberger-2025-scepi2-seq]] (scEpi²-seq).
- [[10-Summaries/tavares-2026-6-base-cut-tag]] (6-base-CUT&Tag).
- [[10-Summaries/yeung-2023-scchix-seq]] (scChIX-seq).
- [[10-Summaries/janssens-2023-scicut-tag]] (sciCUT&Tag).

### Long-read multi-modal chromatin

- [[10-Summaries/abdulhay-2020-samosa]] (SAMOSA-Tag).

## Synthesized notes

_None yet — the three methods papers cluster cleanly enough that a synthesis comparing droplet-scale vs single-molecule approaches would be a natural [[50-Notes/]] page once a fourth source lands._

## Open questions

- Where does scDAF-seq's per-cell ~99% genome coverage / ~10-cell throughput become more useful than GoT–ChA's ~38% genotyping / 10⁵-cell throughput? What experimental questions sit on each side of that line?
- All three current sources use **within-patient WT cells as comparators** (or, for DAF-seq, within-cell haplotypes). Are there single-cell multi-omic questions where this design doesn't apply?
- Imputation-based multi-omic integration (GoT–ChA + DOGMA-seq via mt-variants and surface proteins) works in MPN. How well does it generalize?
- For chromatin: bulk Fiber-seq → single-cell DAF-seq closed a major gap. What's the analogous gap for [[got]]/[[got-cha]] — is there a "single-molecule, per-fiber" extension waiting to be built?
