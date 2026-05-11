---
type: topic
title: Single-cell multi-omics
aliases: [single-cell multiomics, sc-multiomics]
tags: [single-cell, methods, multiomics]
created: 2026-05-07
updated: 2026-05-11
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
- [[30-Concepts/dogma-seq]] — chromatin + RNA + protein trimodal platform; integrated with GoT–ChA via imputation in [[10-Summaries/franco-2024-nature]].
- [[30-Concepts/cite-seq]] — scRNA + surface protein via antibody-derived tags.
- [[30-Concepts/gt-seq]] — physical-separation scDNA + scRNA (G&T-seq).
- [[30-Concepts/spatial-multiomics]] — spatially-resolved multi-omic measurements.
- [[30-Concepts/chromatin-accessibility]] — readout layer.
- [[30-Concepts/chromatin-actuation]] — single-molecule refinement of accessibility.

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

## Sources, by sub-theme

### Genotype + transcriptome (droplet)

- [[10-Summaries/anna-2019-nature]] — GoT method paper; CALR-mutated MPN.

### Genotype + chromatin (droplet, gDNA capture)

- [[10-Summaries/franco-2024-nature]] — GoT–ChA; JAK2V617F MPN; cell-intrinsic chromatin priming of HSCs.

### Genotype + chromatin (single-molecule, deaminase)

- [[10-Summaries/elliott-2025-naturebiotechnology]] — DAF-seq / scDAF-seq; chromosome-length single-cell single-molecule chromatin maps.

### Reviews of the multi-omics landscape

- [[10-Summaries/alev-2023-naturereviewsmolecularcellbiology]] — Baysoy/Fan/Satija technological landscape.
- [[10-Summaries/katy-2023-naturereviewsgenetics]] — Vandereyken/Voet methods and applications, including spatial.
- [[10-Summaries/lukas-2023-naturereviewsgenetics]] — Heumos/Theis best-practices analysis recommendations.

## Synthesized notes

_None yet — the three methods papers cluster cleanly enough that a synthesis comparing droplet-scale vs single-molecule approaches would be a natural [[50-Notes/]] page once a fourth source lands._

## Open questions

- Where does scDAF-seq's per-cell ~99% genome coverage / ~10-cell throughput become more useful than GoT–ChA's ~38% genotyping / 10⁵-cell throughput? What experimental questions sit on each side of that line?
- All three current sources use **within-patient WT cells as comparators** (or, for DAF-seq, within-cell haplotypes). Are there single-cell multi-omic questions where this design doesn't apply?
- Imputation-based multi-omic integration (GoT–ChA + DOGMA-seq via mt-variants and surface proteins) works in MPN. How well does it generalize?
- For chromatin: bulk Fiber-seq → single-cell DAF-seq closed a major gap. What's the analogous gap for [[got]]/[[got-cha]] — is there a "single-molecule, per-fiber" extension waiting to be built?
