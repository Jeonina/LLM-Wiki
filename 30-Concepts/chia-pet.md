---
type: concept
title: ChIA-PET
aliases: [Chromatin Interaction Analysis with Paired-End Tag sequencing, HiChIP, PLAC-seq, protein-anchored interaction mapping]
tags: [3D-genome, ChIP, proximity-ligation, enhancer-promoter, CTCF, RNAPII]
created: 2026-08-13
updated: 2026-10-12
---

# ChIA-PET

> **Chromatin Interaction Analysis with Paired-End Tag sequencing** — chromatin immunoprecipitation combined with proximity ligation, so that only interactions involving a chosen protein are recovered ([[10-Summaries/li-2014-chia-pet|Li 2014]]).

> [!abstract] 한눈에
> ChIA-PET는 ChIP과 proximity ligation을 결합해 특정 단백질이 관여하는 chromatin 상호작용만 genome-wide로 찾는 방법이며, enhancer의 40% 이상이 가장 가까운 promoter를 조절하지 않는다는 것을 보여주었다 ([[10-Summaries/li-2014-chia-pet|Li 2014]]). 면역침강에 많은 세포가 필요해 single-cell 버전은 없고, 그 후속인 PLAC-seq·HiChIP은 single-cell loop caller를 평가하는 기준 자료로 쓰인다 ([[10-Summaries/yu-2021-snaphic|SnapHiC]]).

## Definition

ChIA-PET closes a gap on both sides of it. ChIP-chip, ChIP-PET, and [[chip-seq|ChIP-seq]] locate a factor's binding sites but cannot name the target gene of a distal site, nor say whether the site is functional. 3C is low-throughput; 4C and 5C cannot map interacting regions at high resolution genome-wide ([[10-Summaries/li-2014-chia-pet|Li 2014]]). ChIA-PET is unbiased, genome-wide, high-throughput, and de novo ([[10-Summaries/li-2014-chia-pet|Li 2014]]).

The protocol is described in three co-equal parts — wet lab, data analysis, and experimental verification ([[10-Summaries/li-2014-chia-pet|Li 2014]]).

## Why it matters

- **>40% of enhancers do not regulate their nearest promoter** — the empirical premise for why enhancer-to-gene assignment requires contact data rather than a proximity heuristic ([[10-Summaries/li-2014-chia-pet|Li 2014]]). See [[cis-regulatory-element]] and [[chromatin-loop]].
- Its descendants serve as the reference truth for single-cell loop callers ([[10-Summaries/yu-2021-snaphic|SnapHiC]]).

## Position among interaction assays

| Assay | What it recovers | Trade-off | Source |
|---|---|---|---|
| ChIP-chip, ChIP-PET, [[chip-seq\|ChIP-seq]] | A factor's binding sites | Cannot name the target gene of a distal site, nor say whether the site is functional | ([[10-Summaries/li-2014-chia-pet\|Li 2014]]) |
| 3C / 4C / 5C | Interactions at chosen loci | 3C is low-throughput; 4C and 5C cannot map interacting regions at high resolution genome-wide | ([[10-Summaries/li-2014-chia-pet\|Li 2014]]) |
| [[lieberman-aiden-2009-hic\|Hi-C]] | All contacts, protein-agnostic | Broader scope, lower resolution for any one protein | ([[10-Summaries/li-2014-chia-pet\|Li 2014]]) |
| ChIA-PET | Interactions involving a chosen protein | Higher resolution *associated with a protein of interest*, plus TF binding sites and interactions from one assay | ([[10-Summaries/li-2014-chia-pet\|Li 2014]]) |
| PLAC-seq, HiChIP | Protein-anchored interactions (descendants of ChIA-PET) | Used as reference truth for single-cell loop callers | ([[10-Summaries/yu-2021-snaphic\|SnapHiC]]) |
| [[single-cell-hi-c\|scHi-C]] | All contacts per cell | Protein-agnostic; the only 3D modality available at single-cell scale | (synthesis) |

## Evidence and examples

- **Three interaction classes**: enhancer–promoter, enhancer–enhancer, promoter–promoter ([[10-Summaries/li-2014-chia-pet|Li 2014]]).
- **Chromatin interaction networks are scale-free and hierarchical**, organised into function-enriched "chromatin communities" ([[10-Summaries/li-2014-chia-pet|Li 2014]]).
- Applied across ER-α, RNA polymerase II, CTCF and SMC1A in human MCF7, cancer cells, T cells, and mouse ESCs, NPCs, and B cells ([[10-Summaries/li-2014-chia-pet|Li 2014]]).
- Genome-wide Hi-C loop calls in GM12878 and K562 agreed strongly with three ENCODE CTCF/RAD21 ChIA-PET experiments ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).

## Contested points

- **The single-cell asymmetry.** Protein-anchored interaction mapping has **no single-cell member**, because immunoprecipitation requires many cells. Its descendants — PLAC-seq and HiChIP — therefore appear in the single-cell literature not as assays but as the **reference truth** against which single-cell loop callers are scored ([[10-Summaries/yu-2021-snaphic|SnapHiC]]). The single-cell 3D field traded the functional handle for per-cell resolution: [[single-cell-hi-c|scHi-C]] is protein-agnostic and is the only 3D modality available at single-cell scale. (synthesis)
- This mirrors the ChIP-to-[[cut-and-tag|CUT&Tag]] transition in the histone field, where a low-input tethering chemistry replaced immunoprecipitation and *did* reach single cells ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]) — no equivalent chemistry has yet rescued protein-anchored *interaction* mapping. (synthesis)

## Related

> [!cards]
> - `concept` [[30-Concepts/chromatin-loop|Chromatin loop]] — A focal point-to-point contact enriched above local background.
> - `concept` [[30-Concepts/chip-seq|ChIP-seq]] — The bulk standard for protein–DNA binding that ChIA-PET extends to interactions.
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — Protein-agnostic contact maps, the only 3D modality at single-cell scale.
> - `concept` [[30-Concepts/cis-regulatory-element|Cis-regulatory element]] — Enhancers and promoters whose targets ChIA-PET assigns.
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — The low-input tethering chemistry that replaced ChIP for histone marks.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Territories, compartments, TADs and loops.
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — How DNA packaging varies across fibers, haplotypes and cells.

## All sources on this page

> [!info]- 4 summaries cited here
> - [[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]
> - [[10-Summaries/li-2014-chia-pet|Li & Ruan 2014]]
> - [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]
> - [[10-Summaries/yu-2021-snaphic|Yu 2021]]
