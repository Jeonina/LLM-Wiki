---
type: concept
title: Chromatin loop
aliases: [chromatin loops, enhancer-promoter loop, loop calling, HiCCUPS]
tags: [3D-genome, chromatin-loop, loop-extrusion, CTCF, enhancer-promoter]
created: 2026-08-13
updated: 2026-08-13
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

## Related

- [[single-cell-hi-c]] · [[chia-pet]] · [[chromatin-compartments]] · [[topologically-associating-domain]] · [[multi-way-chromatin-interaction]] · [[cis-regulatory-element]] · [[40-Topics/3d-genome]]
