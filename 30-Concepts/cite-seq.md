---
type: concept
title: CITE-seq
aliases: [Cellular Indexing of Transcriptomes and Epitopes by Sequencing]
tags: [multi-omics, scRNA-protein, antibody-derived-tags, method]
created: 2026-05-11
updated: 2026-05-11
---

# CITE-seq

> Single-cell multi-omic method that measures transcriptome and cell-surface protein expression from the same cell by labeling cells with **antibody-derived tags (ADTs)** — antibodies conjugated to oligonucleotides that are captured and sequenced alongside mRNA in a 10x droplet workflow.

## Definition

ADTs are antibodies conjugated to oligonucleotide barcodes with a polyA tail (so they're captured by oligo-dT primers in 10x scRNA-seq chemistry). After incubation with cells, the bound ADTs co-amplify with mRNA in the same droplet, producing per-cell counts of both transcripts and surface proteins ([[10-Summaries/baysoy-2023-multiomics-landscape]]).

Captures 100s–1000s of surface protein markers in panels.

## Why it matters

- Adds **direct protein-level phenotyping** to transcriptomic data — important for immune cell classification where surface markers are the canonical phenotype.
- Improves cell-type annotation accuracy over RNA-only.
- Compatible with downstream chromatin (DOGMA-seq) and genotype (GoT–ChA imputation) modalities — see [[dogma-seq]] and [[10-Summaries/izzo-2024-got-cha]].

## Variants and refinements

- **REAP-seq** — closely related antibody-tag platform.
- **TotalSeq** (BioLegend) — commercial ADT line.
- **DOGMA-seq** — trimodal extension adding chromatin.

## Contested points

- Specific binding vs background — non-specific antibody binding produces baseline ADT counts that complicate normalization.
- Limited to surface proteins — intracellular proteins not accessible.

## Examples

- Detailed immune cell phenotyping in tumor microenvironment studies.
- DOGMA-seq extension giving chromatin + RNA + protein in single cells.

## Related

- [[40-Topics/single-cell-multiomics]]
- [[dogma-seq]]
- [[40-Topics/single-cell-multiomics]]

## Added 2026-08-17

Two 2021 methods and one 2022 successor define the computational side of CITE-seq, and they disagree productively.

**Protein has a noise problem RNA does not.** Antibody counts carry a large ambient / non-specifically-bound **background** component — systematic and additive, not statistical noise — so treating it as noise inflates apparent expression in every negative population. [[10-Summaries/gayoso-2021-totalvi|totalVI]] separates protein signal into background and foreground inside the generative model ([[10-Summaries/gayoso-2021-totalvi]]). This is the CITE-seq analogue of the ambient-RNA problem. (synthesis)

**Post-hoc contextualisation breaks at scale.** With a handful of markers you can cluster on RNA and inspect protein afterwards; at **208–228 antibodies** ([[10-Summaries/gayoso-2021-totalvi]]; [[10-Summaries/hao-2021-seurat-wnn]]) that sequential approach "biases the analysis to one modality and becomes increasingly inefficient" ([[10-Summaries/gayoso-2021-totalvi]]).

**Three approaches, four months apart, from different traditions:**

| Method | Tradition | Distinctive property |
|---|---|---|
| [[10-Summaries/hao-2021-seurat-wnn]] (WNN) | nearest-neighbour graph | per-cell modality weights; 211,000-cell / 228-antibody PBMC reference atlas |
| [[10-Summaries/gayoso-2021-totalvi]] | deep generative | protein background model; each cell a *distribution* in latent space |
| [[10-Summaries/lakkis-2022-scipenn]] | deep learning | censored loss merges **partially overlapping antibody panels**; returns **uncertainty**; faster than both |

**Predicting protein from RNA alone** — training on a CITE-seq reference and applying to cheaper scRNA-seq — is now a standard capability ([[10-Summaries/lakkis-2022-scipenn]]; also achievable by reference mapping, [[10-Summaries/kang-2021-symphony]]). Only sciPENN returns a confidence estimate, so elsewhere an imputed protein value is indistinguishable from a measured one in the output matrix. (synthesis) See [[reference-atlas-mapping]].
