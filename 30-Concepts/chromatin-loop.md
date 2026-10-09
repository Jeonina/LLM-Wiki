---
type: concept
title: Chromatin loop
aliases: [chromatin loops, enhancer-promoter loop, loop calling, HiCCUPS]
tags: [3D-genome, chromatin-loop, loop-extrusion, CTCF, enhancer-promoter]
created: 2026-08-13
updated: 2026-10-08
---

# Chromatin loop

> A focal, point-to-point contact between two genomic loci that is enriched above its local background — operationally, a peak in a contact matrix rather than a domain or a compartment.

## Definition

Loops sit at the finest scale of the 3D hierarchy, below [[topologically-associating-domain|TADs]] and [[chromatin-compartments|compartments]]. Most are attributed to loop extrusion halted at convergently oriented CTCF sites, which is why **CTCF motif orientation doubles as a precision metric**: among loops with CTCF at both anchors, 63.6–78.7% are convergent ([[10-Summaries/yu-2021-snaphic]]). Functionally, the loops of interest are enhancer–promoter contacts — and the reason they must be measured rather than inferred from proximity is that **over 40% of enhancers do not regulate their nearest promoter** ([[10-Summaries/li-2014-chia-pet]]).

## How loops are detected

Two lineages, distinguished by whether a protein is used as an anchor:

| Route | Logic | Resolution / scope | Source |
|---|---|---|---|
| Protein-anchored ([[chia-pet|ChIA-PET]], HiChIP, PLAC-seq) | Immunoprecipitate a factor, then proximity-ligate | Higher resolution, restricted to one protein's interactions | ([[10-Summaries/li-2014-chia-pet]]) |
| Protein-agnostic (Hi-C → HiCCUPS, Fit-Hi-C, FastHiC, HiC-ACT) | Focal enrichment against local background in the full contact matrix | Genome-wide, needs deep coverage | ([[10-Summaries/lieberman-aiden-2009-hic]]; [[10-Summaries/durand-2016-juicer]]) |

Protein-anchored assays have **no single-cell member** — immunoprecipitation requires many cells — so single-cell loop calling is entirely protein-agnostic, and the protein-anchored assays instead serve as the reference truth against which single-cell callers are scored ([[10-Summaries/yu-2021-snaphic]]). (synthesis)

## Loop calling from single-cell data

Applying bulk callers to pooled [[single-cell-hi-c|scHi-C]] needs >500–1,000 cells ([[10-Summaries/yu-2021-snaphic]]). [[10-Summaries/yu-2021-snaphic|SnapHiC]] avoids pooling: it imputes each cell separately by random walk with restart, then runs a paired *t*-test **across cells** at each bin pair, converting cell-to-cell variance into statistical power. From 75 cells it calls 1,050–1,420 loops where HiCCUPS calls 0–10 ([[10-Summaries/yu-2021-snaphic]]).

The advantage is specifically a low-*n* advantage: in oligodendrocytes, where 1,038 cells aggregated to bulk-equivalent depth (~278M intrachromosomal reads), bulk tools matched it ([[10-Summaries/yu-2021-snaphic]]).

## Limits

- Single-cell loop callers output **cell-type-level** loop lists, not per-cell loops — loop variability between individual cells remains unmeasured ([[10-Summaries/yu-2021-snaphic]]). (synthesis)
- Loops are too sparse to reconstruct higher-order structure: cliques built from SnapHiC calls never exceeded order 3, which is why [[multi-way-chromatin-interaction|multi-way interaction]] detection needs its own statistic ([[10-Summaries/park-2026-mintsc]]).
- Reference loop sets come from bulk assays, so a genuinely single-cell-specific loop is scored as a false positive by construction ([[10-Summaries/yu-2021-snaphic]]). (synthesis)

## Added 2026-10-07

SnapHiC-G drops SnapHiC's local background and tests promoter–enhancer bin pairs against a global distance-stratified background with a one-sample t-test across cells, recovering 79.3% of 38,588 reference interactions in 742 mESCs versus ≤16% for SnapHiC and bulk callers on pseudo-bulk ([[10-Summaries/liu-2024-snaphic-g]]). Only ~21% of its method-specific calls have CTCF at both anchors, consistent with local-maximum callers favouring structural loops and global tests capturing enhancer–promoter contacts ([[10-Summaries/liu-2024-snaphic-g]]).

Single-cell scSPRITE data suggest long- and short-range enhancer contacts can be alternatives rather than simultaneous. Cells in which *Nanog* contacts the super-enhancer 300 kb upstream (159 of 308 covered cells), or *Tbx3* contacts *Lhx5* 760 kb away (152 of 301), show short-range contacts about three times less often (P < 0.001). The two states occur at similar frequencies ([[10-Summaries/arrastia-2022-scsprite]]).

**Single-cell loop calling at 5 kb.** SnapHiC2 called 294 5-kb loops on chr3 from 742 mESCs where pooled HiCCUPS called 6 (default) or 24 (lenient), with F1 0.271 vs 0.013/0.060 against a bulk/HiChIP reference ([[10-Summaries/li-2022-snaphic2]]). It detected the CRISPR-validated Sox2 enhancer–promoter loop from 100 cells, versus ≥500–600 for HiCCUPS ([[10-Summaries/li-2022-snaphic2]]). CUT&RUN combined with native ChIP distinguishes direct CTCF anchors from indirect contact partners at near base-pair resolution ([[10-Summaries/skene-2017-cut-and-run]]).

The founding kilobase-resolution loop catalogue is Rao et al.: HiCCUPS called 9,448 loops in GM12878 in situ Hi-C at 5 kb, 98% of them shorter than 2 Mb ([[10-Summaries/rao-2014-in-situ-hic]]). 86–87% of loop anchors bind CTCF, RAD21 and SMC3, and among 4,322 loops with a single CTCF motif at each anchor, 92% are in convergent orientation (25% expected by chance) ([[10-Summaries/rao-2014-in-situ-hic]]). Loops were called against the local neighbourhood rather than the genome-wide average. The authors argue that global-background calls implying more than 100,000 loops mostly capture same-domain pairs ([[10-Summaries/rao-2014-in-situ-hic]]).

Loops are tied to gene regulation: 2,854 of 9,448 GM12878 loops join a promoter and an enhancer (30% vs 7% expected), and promoters with a loop are 6-fold more highly expressed ([[10-Summaries/rao-2014-in-situ-hic]]). Loops in neighbouring domains rarely overlap (4-fold fewer than random), and 38% of loops sit at the corners of contact domains, the so-called "loop domains" ([[10-Summaries/rao-2014-in-situ-hic]]).

A 2025 survey names SnapHiC2 as the only pipeline built to call loops from single-cell Hi-C. It resolves loops at up to 5 kb and does not require imputation ([[10-Summaries/dautle-2025-schic-review]]).


In budding yeast, Micro-C found contacts spread through gene bodies rather than preferential promoter–terminator contacts. Compaction also fell with transcription, the opposite of reported gene loops, so the authors favour "gene crumples" (globules); the gene-looping factor mutant *ssu72-2* only modestly reduced global compaction ([[10-Summaries/hsieh-2015-micro-c]]).

## Added 2026-10-08 — sequence models & foundation models

- Training EpiGePT with a cosine loss that aligns attention maps with HiChIP loops raised enhancer–promoter auPRC on Gasperini CRISPRi pairs at 24–40 kb from 0.652 to 0.695 ([[10-Summaries/gao-2024-epigept]]).
- Fine-tuned for loop calling, HiCFoundation reached mean F1 81.6% on deep maps and 75.1% on 1/16-downsampled maps against consensus HiCCUPS loops, with 90.4% and 81.8% of its calls CTCF-supported at both anchors ([[10-Summaries/wang-2026-hicfoundation]]).

## Related

- [[single-cell-hi-c]] · [[chia-pet]] · [[chromatin-compartments]] · [[topologically-associating-domain]] · [[multi-way-chromatin-interaction]] · [[cis-regulatory-element]] · [[40-Topics/3d-genome]]
