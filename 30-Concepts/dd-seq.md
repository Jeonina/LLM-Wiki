---
type: concept
title: "D&D-seq (docking and deamination followed by sequencing)"
aliases: [D&D-seq, DD-seq, docking and deamination, scD&D-seq, D&D-GoT-ChA]
tags: [single-cell, DNA-protein-interaction, transcription-factor, base-editor, CTCF, method]
created: 2026-06-26
updated: 2026-10-12
---

# D&D-seq (docking and deamination followed by sequencing)

> A single-cell immuno-tethering method that records where a DNA-binding protein is bound on the genome by fusing an antibody-binding nanobody to a cytosine deaminase (DddA), which writes C→U (read as C→T) edits into protein-bound sites — adding a direct **DNA–protein interaction / transcription-factor-binding** readout to single-cell genome and multi-omic workflows ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]).

> [!abstract] 한눈에
> D&D-seq는 항체에 붙는 nanobody–DddA 융합 효소로 단백질이 결합한 자리의 C를 T로 바꿔 기록하므로, scATAC이 보지 못하는 "어떤 단백질이 실제로 붙어 있는가"를 DNA 서열에 남긴다 ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]). 다만 세포 하나당 edit가 드물어 해석은 아직 cluster나 pseudobulk 수준에 머문다 ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]).

## Definition

D&D-seq couples a secondary nanobody (which binds an antibody against the protein of interest) to the double-stranded-DNA cytosine deaminase DddA ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]). The enzyme is split: an inactive nanobody-DddA_NT fusion is reconstituted only when the separately supplied C-terminal peptide and Zn²⁺ are added, preventing nonspecific deamination ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]). At antibody-bound genomic sites the reconstituted enzyme stencils cytosines (TpC/CpC context) as C→U, surviving amplification as C→T sequence changes that mark binding footprints ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]). Because the readout is written into the DNA sequence, it integrates with scATAC-seq, PTA-based WGS, and combinatorial-barcoding multi-omic protocols ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]).

## Why it matters

Chromatin accessibility ([[chromatin-accessibility]]) tells you a region is *open*; D&D-seq tells you *which protein is actually bound there* — a distinction scATAC cannot make ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]). For the wiki's regulatory-layers framing it supplies a distinct sixth axis — TF/DNA-protein occupancy — see [[50-Notes/regulatory-layers-overview]] (synthesis).

## Variants and refinements

| Variant | Readout | What it adds | Source |
|---|---|---|---|
| Bulk D&D-seq | CTCF/GATA1/GATA2 targets (plus the remodeler p300) in K562 | Validated against ENCODE ChIP-seq | ([[10-Summaries/chi-2026-dd-seq\|Chi 2026]]) |
| D&D-seq + WGS (PTA) | Genome-wide binding | Includes non-accessible chromatin | ([[10-Summaries/chi-2026-dd-seq\|Chi 2026]]) |
| scD&D-seq | Integrated into 10x scATAC-seq | Per-cell binding (pseudobulk/metacell aggregation, ≥250 cells for robust footprints) | ([[10-Summaries/chi-2026-dd-seq\|Chi 2026]]) |
| D&D-GoT-ChA | Composed with [[got-cha]] genotyping | Same-cell **genotype + TF binding**; applied to an IDH2^R140Q CHIP patient | ([[10-Summaries/chi-2026-dd-seq\|Chi 2026]]) |

**Sibling method — [[dechic-seq|DeChIC-seq]].** DeChIC-seq also tethers DddA via antibody to write C→U edits at protein-bound chromatin, but uses a protein A–DddA fusion whose activity is switched off at pH 8.0 and on at pH 6.4, rather than a split nanobody–DddA ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]). It is run one cell per tube with META-CS-based WGA instead of in multiomic droplet workflows ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]).

## Evidence and examples

- By coupling to whole-genome sequencing, D&D-seq captures binding in **inactive/heterochromatic compartments** (CTCF peaks overlapping H3K9me3/H3K27me3) that accessibility assays miss entirely ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]).
- In benchmarking, scD&D-seq reached ~57% FRiP for CTCF vs ~14% for uliCUT&RUN, and achieved higher motif specificity than scCUT&Tag ([[cut-and-tag]]), whose peaks are confounded by open-chromatin bleed-through ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]).
- Binding is validated by de novo motif recovery ([[transcription-factor-motif]]) ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]).
- IDH2^R140Q clonal hematopoiesis: 33% of 15,807 cells genotyped, mutant cells enriched in the CD8 T compartment, and mutant T cells show disrupted CTCF binding vs wild-type ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]).
- scD&D CTCF + scATAC fed to the C.Origami pipeline reconstructs Hi-C-like 3D contact maps from single-cell input ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]).

## Contested points

- Per-cell edit sparsity means true single-cell-resolution binding is not yet achieved — interpretation is cluster/pseudobulk-level ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]).
- TpC sequence-context bias and moderate single-cell GATA1 sensitivity limit uniform applicability across factors ([[10-Summaries/chi-2026-dd-seq|Chi 2026]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/got-cha|GoT–ChA]] — Composes with D&D-seq as D&D-GoT-ChA (genotype + TF binding).
> - `concept` [[30-Concepts/daf-seq|DAF-seq]] — Shares the "stencil epigenetic state into DNA via deamination" design (accessibility vs protein occupancy).
> - `concept` [[30-Concepts/dechic-seq|DeChIC-seq]] — Sibling antibody-tethered DddA method with pH-switched activity.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — D&D distinguishes bound from merely open.
> - `concept` [[30-Concepts/transcription-factor-motif|Transcription factor motif]] — Binding validated by de novo motif recovery.
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — Antibody-tethered alternative D&D-seq outperforms on specificity.
> - `note` [[50-Notes/regulatory-layers-overview|Regulatory layers]] — TF occupancy as a distinct regulatory axis.
> - `entity` [[20-Entities/landau-lab|Landau Lab]] — Lab behind D&D-seq.
> - `hub` [[40-Topics/3d-genome|3D genome]] — scD&D CTCF enables single-cell 3D structure prediction.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Joint measurement of several layers in the same cell.
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — Accessibility, histone marks and 3D genome structure.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/chi-2026-dd-seq|Chi 2026]]
> - [[10-Summaries/shi-2026-dechic-seq|Shi 2026]]
