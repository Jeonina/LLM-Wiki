---
type: concept
title: CITE-seq
aliases: [Cellular Indexing of Transcriptomes and Epitopes by Sequencing]
tags: [multi-omics, scRNA-protein, antibody-derived-tags, method]
created: 2026-05-11
updated: 2026-10-12
---

# CITE-seq

> Single-cell multi-omic method that measures transcriptome and cell-surface protein expression from the same cell by labelling cells with antibody-derived tags (ADTs) — antibodies conjugated to oligonucleotides that are captured and sequenced alongside mRNA in a 10x droplet workflow ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]).

> [!abstract] 한눈에
> CITE-seq은 oligo가 붙은 항체(ADT)로 세포 표면 단백질을 표지해 같은 세포의 전사체와 함께 시퀀싱하는 방법이다 ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]). 항체 수가 수백 개로 늘면서 분석은 RNA와 단백질을 함께 다루는 모델로 옮겨 갔고, 단백질 신호에 섞인 background를 어떻게 다루고 예측값의 신뢰도를 어떻게 줄지가 쟁점이다 ([[10-Summaries/gayoso-2021-totalvi|totalVI]]; [[10-Summaries/lakkis-2022-scipenn|sciPENN]]).

## Definition

ADTs are antibodies conjugated to oligonucleotide barcodes with a polyA tail, so they are captured by oligo-dT primers in 10x scRNA-seq chemistry ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]). After incubation with cells, the bound ADTs co-amplify with mRNA in the same droplet, producing per-cell counts of both transcripts and surface proteins ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]). Panels capture hundreds to thousands of surface protein markers (synthesis).

## Why it matters

- It adds direct protein-level phenotyping to transcriptomic data, which matters for immune cell classification where surface markers are the canonical phenotype (synthesis).
- It improves cell-type annotation accuracy over RNA-only data (synthesis).
- It is compatible with downstream chromatin (DOGMA-seq) and genotype (GoT–ChA imputation) modalities ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]); see [[dogma-seq]] and [[40-Topics/single-cell-multiomics]].

## Variants and platforms

- **REAP-seq** — a closely related antibody-tag platform for scRNA + protein ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]).
- **TotalSeq** (BioLegend) — a commercial ADT line (synthesis).
- **DOGMA-seq** — a trimodal extension adding chromatin, giving chromatin + RNA + protein in single cells ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- **ADT paired with DNA, not RNA** — on Tapestri, ADT surface-marker counts are captured alongside targeted DNA amplicons ([[10-Summaries/gillman-2026-scarce|SCARCE]]).

## Computational methods

Two 2021 methods and one 2022 successor define the computational side of CITE-seq, and they disagree productively ([[10-Summaries/hao-2021-seurat-wnn|Seurat WNN]]; [[10-Summaries/gayoso-2021-totalvi|totalVI]]; [[10-Summaries/lakkis-2022-scipenn|sciPENN]]).

| Method | Tradition | Distinctive property | Source |
|---|---|---|---|
| [[10-Summaries/hao-2021-seurat-wnn\|Seurat WNN]] | Nearest-neighbour graph | Per-cell modality weights; 211,000-cell / 228-antibody PBMC reference atlas | ([[10-Summaries/hao-2021-seurat-wnn\|Seurat WNN]]) |
| [[10-Summaries/gayoso-2021-totalvi\|totalVI]] | Deep generative | Protein background model; each cell a *distribution* in latent space | ([[10-Summaries/gayoso-2021-totalvi\|totalVI]]) |
| [[10-Summaries/lakkis-2022-scipenn\|sciPENN]] | Deep learning | Censored loss merges partially overlapping antibody panels; returns uncertainty; faster than both | ([[10-Summaries/lakkis-2022-scipenn\|sciPENN]]) |

- **Protein has a noise problem RNA does not.** Antibody counts carry a large ambient / non-specifically-bound background component — systematic and additive, not statistical noise — so treating it as noise inflates apparent expression in every negative population (synthesis). totalVI separates protein signal into background and foreground inside the generative model ([[10-Summaries/gayoso-2021-totalvi|totalVI]]). This is the CITE-seq analogue of the ambient-RNA problem (synthesis).
- **Post-hoc contextualisation breaks at scale.** With a handful of markers you can cluster on RNA and inspect protein afterwards; at 208–228 antibodies ([[10-Summaries/gayoso-2021-totalvi|totalVI]]; [[10-Summaries/hao-2021-seurat-wnn|Seurat WNN]]) that sequential approach "biases the analysis to one modality and becomes increasingly inefficient" ([[10-Summaries/gayoso-2021-totalvi|totalVI]]).
- **Predicting protein from RNA alone** — training on a CITE-seq reference and applying it to cheaper scRNA-seq — is now a standard capability ([[10-Summaries/lakkis-2022-scipenn|sciPENN]]), also achievable by reference mapping ([[10-Summaries/kang-2021-symphony|Symphony]]); see [[reference-atlas-mapping]].

## Evidence and examples

- CITE-seq is used for detailed immune cell phenotyping in tumour-microenvironment studies (synthesis).
- SCARCE uses Tapestri ADT counts (CLR normalisation, SCINA labels, manual cluster calls) to define cell types for somatic-variant enrichment tests ([[10-Summaries/gillman-2026-scarce|SCARCE]]).
- GoT–ChA integrates with DOGMA-seq via mitochondrial-variant and cell-surface-protein imputation ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Contested points

- **Specific binding versus background.** Non-specific antibody binding produces baseline ADT counts that complicate normalization (synthesis); totalVI models this background explicitly ([[10-Summaries/gayoso-2021-totalvi|totalVI]]).
- **Limited to surface proteins.** Intracellular proteins are not accessible (synthesis).
- **Confidence on imputed protein.** Seurat 4 returns no confidence estimate and totalVI's prediction intervals are badly under-covered ([[10-Summaries/lakkis-2022-scipenn|sciPENN]]), so only sciPENN gives a usable confidence on an imputed protein value (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/dogma-seq|DOGMA-seq]] — Trimodal chromatin + RNA + protein extension.
> - `concept` [[30-Concepts/reference-atlas-mapping|Reference atlas mapping]] — Projecting query cells, and predicting protein, from a reference.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Measuring several molecular layers in the same cell.

## All sources on this page

> [!info]- 7 summaries cited here
> - [[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]
> - [[10-Summaries/gayoso-2021-totalvi|Gayoso 2021]]
> - [[10-Summaries/gillman-2026-scarce|Gillman 2026]]
> - [[10-Summaries/hao-2021-seurat-wnn|Hao 2021]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/kang-2021-symphony|Kang 2021]]
> - [[10-Summaries/lakkis-2022-scipenn|Lakkis 2022]]
