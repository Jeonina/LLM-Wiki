---
type: concept
title: Doublet Detection
aliases: [doublets, collisions, multiplets]
tags: [QC, artefacts, single-cell, barcoding]
created: 2026-08-10
updated: 2026-10-12
---

# Doublet Detection

> Two cells sharing one barcode produce a chimeric profile that clustering will place somewhere plausible and wrong ([[10-Summaries/cao-2019-moca|Cao 2019]]; [[10-Summaries/jones-2020-cassiopeia|Cassiopeia]]). Every single-cell platform generates them; the rate and the detectability differ by platform (synthesis).

> [!abstract] 한눈에
> Doublet은 두 세포가 한 barcode를 공유해 생긴 chimeric profile로, combinatorial indexing에서는 몇 % 수준으로 생기며 같은 종 안의 충돌은 species-mixing 대조군으로 보이지 않는다 ([[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]). 처리하지 않으면 가짜 cluster나 lineage tree의 잘못된 관계로 남기 때문에, 물리적 이미징, 계산적 점수, phylogeny 모델 안에서의 직접 모델링 등으로 다룬다 ([[10-Summaries/cao-2019-moca|Cao 2019]]; [[10-Summaries/zafar-2019-siclonefit|SiCloneFit]]).

## Definition

A doublet (or collision, multiplet) is two or more cells sharing one barcode. **Combinatorial indexing** produces collisions at the birthday-problem rate given nuclei per well ([[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]; [[10-Summaries/cao-2019-moca|Cao 2019]]). In lineage tracing there are **two distinct levels** — intra-doublets from a cell's own molecules, and inter-doublets between clones — handled separately ([[10-Summaries/jones-2020-cassiopeia|Cassiopeia]]).

## Why it matters

- Whole clusters can be doublet artefacts: one 40-cluster analysis discarded a cluster with a 52% detected doublet rate, and 13% of 655 subclusters were annotated as artefacts under a >10% predicted-doublet rule ([[10-Summaries/cao-2019-moca|Cao 2019]]).
- In lineage tracing a doublet's chimeric character vector is placed on the tree, producing a false relationship rather than an obvious outlier ([[10-Summaries/jones-2020-cassiopeia|Cassiopeia]]).
- In CellPhy's simulations, cell doublets lowered phylogenetic accuracy for every method tested; the authors recommend removing doublets with scDNA-seq-specific detectors before building trees ([[10-Summaries/kozlov-2022-cellphy|CellPhy]]).

## Approaches

| Approach | Example | How it works | Source |
|---|---|---|---|
| Species-mixing control | [[10-Summaries/ramani-2017-scihi-c\|sciHi-C]] | Measures cross-species collisions; within-species collisions stay invisible | ([[10-Summaries/ramani-2017-scihi-c\|Ramani 2017]]) |
| Computational doublet score | Scrublet in [[10-Summaries/cao-2019-moca\|sci-RNA-seq3]] | Flags likely doublets; cluster-level rules discard artefact clusters | ([[10-Summaries/cao-2019-moca\|Cao 2019]]) |
| Physical prevention | [[10-Summaries/zahn-2017-dlp\|DLP]]; [[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]] | On-chip or nanowell imaging keeps only single-cell wells before library construction | ([[10-Summaries/zahn-2017-dlp\|Zahn 2017]]; [[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]]) |
| CNA-profile correlation | [[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]] | Removes non-diploid subclones whose consensus CNA profile correlates with an aneuploid subclone but with a smaller log2 ratio, as tumour–diploid doublets | ([[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]]) |
| Count thresholds + genotype score | [[10-Summaries/pancikova-2025-splongget\|SPLONGGET]] | >20,000 RNA UMIs or >60,000 DNA reads, validated by haplotype ratio in a copy-neutral LOH region (chr3) | ([[10-Summaries/pancikova-2025-splongget\|SPLONGGET]]) |
| Read density | [[10-Summaries/schneider-2024-scabsolute\|scAbsolute]] | Separates single cells from multiplets even when CN profiles look identical | ([[10-Summaries/schneider-2024-scabsolute\|scAbsolute]]) |
| Doublets modelled inside the phylogeny | [[10-Summaries/zafar-2019-siclonefit\|SiCloneFit]]; [[10-Summaries/sollier-2023-compass\|COMPASS]] | Each cell gets a second clone indicator (SiCloneFit); cells carrying mutations from different lineages are explained as doublets (COMPASS) | ([[10-Summaries/zafar-2019-siclonefit\|SiCloneFit]]; [[10-Summaries/sollier-2023-compass\|COMPASS]]) |
| Assumed removed upstream | [[10-Summaries/malikic-2019-phiscs\|PhISCS]] | Requires doublet-free input; named as its main limitation | ([[10-Summaries/malikic-2019-phiscs\|PhISCS]]) |

## Evidence and examples

**Rates**

- Species mixing measured 4.53%/4.40% collisions in sciHi-C ([[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]), and 3% in sci-RNA-seq3 ([[10-Summaries/cao-2019-moca|Cao 2019]]).
- Within-species collisions are invisible to species-mixing controls and are expected at a similar rate ([[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]).
- Scrublet found 4.3% likely doublets, implying ~10.3% including within-cluster doublets ([[10-Summaries/cao-2019-moca|Cao 2019]]).

**Detection and modelling results**

- On a 370-cell ovarian dataset, SiCloneFit and SCG agreed on 17 doublets, with SCG calling 11 more ([[10-Summaries/zafar-2019-siclonefit|SiCloneFit]]).
- Modelling doublets in amplicon scDNA phylogenetics removed apparent mutation recurrences: COMPASS trees for TP53-mutated MPNs were more compact than originally published ([[10-Summaries/sollier-2023-compass|COMPASS]]).
- In SPLONGGET long-read Multiome data, Scrublet "proved to be ineffective"; tumour cells carry only the retained haplotype in the chr3 copy-neutral LOH region, so cells with an intermediate haplotype ratio and high counts were flagged as tumour–normal doublets ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).
- scAbsolute's read-density measure separated G1 single cells from deliberately plated 2–5-cell multiplets (6N–12N) with 97% accuracy; the authors propose it for doublet detection in future droplet-based, amplification-free protocols ([[10-Summaries/schneider-2024-scabsolute|scAbsolute]]).

## Contested points

- **Atlas subtype counts are likely inflated.** Subtype counts from atlases without a doublet rule such as Cao 2019's should be read as upper bounds (synthesis).
- **Model doublets or remove them first?** SiCloneFit models doublets directly ([[10-Summaries/zafar-2019-siclonefit|SiCloneFit]]), whereas PhISCS assumes they were removed beforehand ([[10-Summaries/malikic-2019-phiscs|PhISCS]]) and CellPhy recommends removal before tree building ([[10-Summaries/kozlov-2022-cellphy|CellPhy]]).
- **Generic detectors do not transfer to every assay.** Scrublet was used on sci-RNA-seq3 ([[10-Summaries/cao-2019-moca|Cao 2019]]) but was ineffective on long-read Multiome data ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]), so assay-specific signals (genotype, CN profile, read density) may be needed (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/quality-control-metrics|Quality control metrics]] — Per-library and per-cell statistics that decide which data enter an analysis.
> - `concept` [[30-Concepts/combinatorial-indexing|Combinatorial indexing]] — Split-pool barcoding, whose collision rate sets the doublet floor.
> - `concept` [[30-Concepts/cell-type-annotation|Cell type annotation]] — Assigning identity to clusters, which doublet clusters corrupt.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — The tool layer: aligners, callers, imputers and integrators.

## All sources on this page

> [!info]- 11 summaries cited here
> - [[10-Summaries/cao-2019-moca|Cao 2019]]
> - [[10-Summaries/jones-2020-cassiopeia|Jones 2020]]
> - [[10-Summaries/kozlov-2022-cellphy|Kozlov 2022]]
> - [[10-Summaries/malikic-2019-phiscs|Malikic 2019]]
> - [[10-Summaries/pancikova-2025-splongget|Pančíková 2025 (bioRxiv preprint)]]
> - [[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]
> - [[10-Summaries/schneider-2024-scabsolute|Schneider 2024]]
> - [[10-Summaries/sollier-2023-compass|Sollier 2023]]
> - [[10-Summaries/wang-2024-wellda-seq|Wang 2024]]
> - [[10-Summaries/zafar-2019-siclonefit|Zafar 2019]]
> - [[10-Summaries/zahn-2017-dlp|Zahn 2017]]
