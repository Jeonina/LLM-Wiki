---
type: concept
title: Chromatin loop
aliases: [chromatin loops, enhancer-promoter loop, loop calling, HiCCUPS]
tags: [3D-genome, chromatin-loop, loop-extrusion, CTCF, enhancer-promoter]
created: 2026-08-13
updated: 2026-10-12
---

# Chromatin loop

> A focal, point-to-point contact between two genomic loci that is enriched above its local background — operationally, a peak in a contact matrix rather than a domain or a compartment ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).

> [!abstract] 한눈에
> Chromatin loop는 contact matrix에서 주변 배경보다 강하게 나타나는 두 locus 사이의 점 모양 접촉이며, 대부분 convergent CTCF 자리에서 멈춘 loop extrusion으로 설명된다 ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]). 단일 세포 데이터에서는 SnapHiC 계열이 세포 간 변이를 통계적 검정력으로 바꿔 소수의 세포로도 loop를 부르지만, 결과는 세포 하나가 아니라 세포 유형 수준의 loop 목록이다 ([[10-Summaries/yu-2021-snaphic|SnapHiC]]; [[10-Summaries/li-2022-snaphic2|SnapHiC2]]).

## Definition

Loops sit at the finest scale of the 3D hierarchy, below [[topologically-associating-domain|TADs]] and [[chromatin-compartments|compartments]] (synthesis). Most are attributed to loop extrusion halted at convergently oriented CTCF sites, which is why **CTCF motif orientation doubles as a precision metric**: among loops with CTCF at both anchors, 63.6–78.7% are convergent ([[10-Summaries/yu-2021-snaphic|SnapHiC]]). Loops are called against the local neighbourhood rather than the genome-wide average; the authors of the founding kilobase-resolution catalogue argue that global-background calls implying more than 100,000 loops mostly capture same-domain pairs ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).

## Why it matters

- Functionally, the loops of interest are enhancer–promoter contacts, and they must be measured rather than inferred from proximity because **over 40% of enhancers do not regulate their nearest promoter** ([[10-Summaries/li-2014-chia-pet|Li 2014]]).
- Loops are tied to gene regulation: 2,854 of 9,448 GM12878 loops join a promoter and an enhancer (30% vs 7% expected), and promoters with a loop are 6-fold more highly expressed ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).

## How loops are detected

Two lineages, distinguished by whether a protein is used as an anchor:

| Route | Logic | Resolution / scope | Source |
|---|---|---|---|
| Protein-anchored ([[chia-pet\|ChIA-PET]], HiChIP, PLAC-seq) | Immunoprecipitate a factor, then proximity-ligate | Higher resolution, restricted to one protein's interactions | ([[10-Summaries/li-2014-chia-pet\|Li 2014]]) |
| Protein-agnostic (Hi-C → HiCCUPS, Fit-Hi-C, FastHiC, HiC-ACT) | Focal enrichment against local background in the full contact matrix | Genome-wide, needs deep coverage | ([[10-Summaries/lieberman-aiden-2009-hic\|Lieberman-Aiden 2009]]; [[10-Summaries/durand-2016-juicer\|Juicer]]) |

Protein-anchored assays have **no single-cell member**, because immunoprecipitation requires many cells, so single-cell loop calling is entirely protein-agnostic and the protein-anchored assays instead serve as the reference truth against which single-cell callers are scored ([[10-Summaries/yu-2021-snaphic|SnapHiC]]) (synthesis).

### Single-cell loop callers

Applying bulk callers to pooled [[single-cell-hi-c|scHi-C]] needs >500–1,000 cells ([[10-Summaries/yu-2021-snaphic|SnapHiC]]).

| Caller | Approach | Key result | Source |
|---|---|---|---|
| SnapHiC | Imputes each cell separately by random walk with restart, then runs a paired *t*-test **across cells** at each bin pair against local background, converting cell-to-cell variance into statistical power | From 75 cells calls 1,050–1,420 loops where HiCCUPS calls 0–10 | ([[10-Summaries/yu-2021-snaphic\|SnapHiC]]) |
| SnapHiC2 | Single-cell loop calling at 5 kb; a 2025 survey names it the only pipeline built to call loops from single-cell Hi-C, and it does not require imputation | 294 5-kb loops on chr3 from 742 mESCs where pooled HiCCUPS called 6 (default) or 24 (lenient); F1 0.271 vs 0.013/0.060 against a bulk/HiChIP reference | ([[10-Summaries/li-2022-snaphic2\|SnapHiC2]]; [[10-Summaries/dautle-2025-schic-review\|Dautle 2025]]) |
| SnapHiC-G | Drops SnapHiC's local background and tests promoter–enhancer bin pairs against a global distance-stratified background with a one-sample *t*-test across cells | Recovers 79.3% of 38,588 reference interactions in 742 mESCs, versus ≤16% for SnapHiC and bulk callers on pseudo-bulk | ([[10-Summaries/liu-2024-snaphic-g\|SnapHiC-G]]) |

### Sequence and foundation models

- Training EpiGePT with a cosine loss that aligns attention maps with HiChIP loops raised enhancer–promoter auPRC on Gasperini CRISPRi pairs at 24–40 kb from 0.652 to 0.695 ([[10-Summaries/gao-2024-epigept|EpiGePT]]).
- Fine-tuned for loop calling, HiCFoundation reached mean F1 81.6% on deep maps and 75.1% on 1/16-downsampled maps against consensus HiCCUPS loops, with 90.4% and 81.8% of its calls CTCF-supported at both anchors ([[10-Summaries/wang-2026-hicfoundation|HiCFoundation]]).

## Evidence and examples

**The founding catalogue and CTCF anchors**

- HiCCUPS called 9,448 loops in GM12878 in situ Hi-C at 5 kb, 98% of them shorter than 2 Mb ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).
- CUT&RUN combined with native ChIP distinguishes direct CTCF anchors from indirect contact partners at near base-pair resolution ([[10-Summaries/skene-2017-cut-and-run|Skene 2017]]).
- 86–87% of loop anchors bind CTCF, RAD21 and SMC3, and among 4,322 loops with a single CTCF motif at each anchor, 92% are in convergent orientation (25% expected by chance) ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).
- Loops in neighbouring domains rarely overlap (4-fold fewer than random), and 38% of loops sit at the corners of contact domains, the so-called "loop domains" ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).

**Single-cell calling**

- SnapHiC's advantage is specifically a low-*n* advantage: in oligodendrocytes, where 1,038 cells aggregated to bulk-equivalent depth (~278M intrachromosomal reads), bulk tools matched it ([[10-Summaries/yu-2021-snaphic|SnapHiC]]).
- SnapHiC2 detected the CRISPR-validated Sox2 enhancer–promoter loop from 100 cells, versus ≥500–600 for HiCCUPS ([[10-Summaries/li-2022-snaphic2|SnapHiC2]]).
- Only ~21% of SnapHiC-G's method-specific calls have CTCF at both anchors, consistent with local-maximum callers favouring structural loops and global tests capturing enhancer–promoter contacts ([[10-Summaries/liu-2024-snaphic-g|SnapHiC-G]]).

**Enhancer contacts in single cells**

- scSPRITE data suggest long- and short-range enhancer contacts can be alternatives rather than simultaneous: cells in which *Nanog* contacts the super-enhancer 300 kb upstream (159 of 308 covered cells), or *Tbx3* contacts *Lhx5* 760 kb away (152 of 301), show short-range contacts about three times less often (P < 0.001), and the two states occur at similar frequencies ([[10-Summaries/arrastia-2022-scsprite|scSPRITE]]).

**Gene loops in yeast**

- In budding yeast, Micro-C found contacts spread through gene bodies rather than preferential promoter–terminator contacts, and compaction fell with transcription, the opposite of reported gene loops; the authors favour "gene crumples" (globules), and the gene-looping factor mutant *ssu72-2* only modestly reduced global compaction ([[10-Summaries/hsieh-2015-micro-c|Micro-C]]).

## Contested points

- **Cell-type-level, not per-cell.** Single-cell loop callers output cell-type-level loop lists, not per-cell loops, so loop variability between individual cells remains unmeasured ([[10-Summaries/yu-2021-snaphic|SnapHiC]]) (synthesis).
- **Too sparse for higher-order structure.** Cliques built from SnapHiC calls never exceeded order 3, which is why [[multi-way-chromatin-interaction|multi-way interaction]] detection needs its own statistic ([[10-Summaries/park-2026-mintsc|MINTsC]]).
- **Reference sets are bulk.** Reference loop sets come from bulk assays, so a genuinely single-cell-specific loop is scored as a false positive by construction ([[10-Summaries/yu-2021-snaphic|SnapHiC]]) (synthesis).
- **Local vs global background.** Rao et al. argue that global-background calls mostly capture same-domain pairs ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]), while SnapHiC-G uses a global background deliberately to capture enhancer–promoter contacts that local-maximum callers miss ([[10-Summaries/liu-2024-snaphic-g|SnapHiC-G]]); which background is right depends on whether structural loops or regulatory contacts are the target (synthesis).
- **Gene loops vs gene crumples.** Yeast Micro-C does not support preferential promoter–terminator gene loops ([[10-Summaries/hsieh-2015-micro-c|Micro-C]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/topologically-associating-domain|Topologically associating domain]] — Self-interacting domains whose corners often carry loops.
> - `concept` [[30-Concepts/chromatin-compartments|Chromatin compartments]] — Mb-scale A/B blocks at the coarse end of the 3D hierarchy.
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — The family of assays single-cell loop callers run on.
> - `concept` [[30-Concepts/chia-pet|ChIA-PET]] — Protein-anchored proximity ligation; a bulk reference for loop calls.
> - `concept` [[30-Concepts/multi-way-chromatin-interaction|Multi-way chromatin interaction]] — Three or more loci in simultaneous contact in one nucleus.
> - `concept` [[30-Concepts/cis-regulatory-element|Cis-regulatory element]] — Enhancers and promoters joined by regulatory loops.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromatin folding from compartments to loops, in bulk and single cells.

## All sources on this page

> [!info]- 14 summaries cited here
> - [[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]
> - [[10-Summaries/dautle-2025-schic-review|Dautle 2025]]
> - [[10-Summaries/durand-2016-juicer|Durand 2016]]
> - [[10-Summaries/gao-2024-epigept|EpiGePT 2024]]
> - [[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]
> - [[10-Summaries/li-2014-chia-pet|Li & Ruan 2014]]
> - [[10-Summaries/li-2022-snaphic2|Li 2022]]
> - [[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]
> - [[10-Summaries/liu-2024-snaphic-g|Liu 2024]]
> - [[10-Summaries/park-2026-mintsc|Park 2026]]
> - [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]
> - [[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]
> - [[10-Summaries/wang-2026-hicfoundation|HiCFoundation 2026]]
> - [[10-Summaries/yu-2021-snaphic|Yu 2021]]
