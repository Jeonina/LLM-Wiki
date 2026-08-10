---
type: concept
title: CUT&Tag
aliases: [Cleavage Under Targets and Tagmentation]
tags: [histone-modifications, Tn5, Henikoff-lab, in-situ]
created: 2026-05-12
updated: 2026-08-10
---

# CUT&Tag

> An antibody-directed in-situ chromatin profiling method developed by Kaya-Okur/Henikoff (2019). Tethers a Tn5 transposase fused to protein A (pA-Tn5) to histone-modification-bound chromatin via primary + secondary antibody, then Mg²⁺-catalyzed tagmentation deposits sequencing adapters at target sites within intact nuclei.

## Definition

Workflow: light formaldehyde fixation → nuclei isolation → primary antibody → secondary antibody → pA-Tn5 binding → Mg²⁺-triggered tagmentation → SDS release → PCR with indexed primers → sequencing. The fusion protein remains bound to DNA after cleavage, so fragments are retained within intact cells — making the method single-cell-compatible.

## Why it matters

- Rapidly replacing ChIP-seq as the standard chromatin-profiling method.
- Single-cell-compatible (scCUT&Tag) and combinatorial-indexing-scalable (sciCUT&Tag).
- Underpins methods that profile DNA modifications at chromatin sites: [[30-Concepts/6-base-cut-and-tag]].

## Examples

- Standard reference: Kaya-Okur et al. 2019 *Nat Commun*.
- Single-cell scale: [[10-Summaries/janssens-2023-scicut-tag]] (sciCUT&Tag).
- DNA-modification extension: [[10-Summaries/tavares-2026-6-base-cut-tag]] (6-base-CUT&Tag).

## Founding results and single-cell lineage

- **Efficiency.** ~2 M CUT&Tag reads ≈ 8 M CUT&RUN ≈ 20 M ChIP-seq; ChIP-seq's H3K4me1 dynamic range is ~1/20 of CUT&Tag's, and only CUT&Tag reaches FRiP 0.6 ([[10-Summaries/kaya-okur-2019-cut-and-tag]]).
- **Why it is single-cell-compatible while CUT&RUN is not**: MNase releases fragments into the supernatant, whereas Tn5 stays bound so fragments are retained in the nucleus and adapters are added *in bulk* before cells are separated ([[10-Summaries/kaya-okur-2019-cut-and-tag]]).
- **Input range** 100,000 → 60 cells with near-identical H3K27me3 profiles; CTCF footprint ~80 bp vs ~45 bp MNase protection ([[10-Summaries/kaya-okur-2019-cut-and-tag]]).
- **The ATAC background is real and diagnostic.** Untethered pA-Tn5 binds exposed DNA, so every run carries a low-level accessibility signal; salt stringency controls it, and in single cells it appears as a nucleosomal fragment-length ladder in specific clusters ([[10-Summaries/kaya-okur-2019-cut-and-tag]]; QC procedure in [[10-Summaries/wu-2021-sccut-tag]]).
- **Repressive marks work best at single-cell scale** because feature breadth (~5 nucleosomes for H3K4me2 vs hundreds for H3K27me3 domains) compensates for sparse sampling — H3K27me3 types cells at 300–1,100 fragments per cell ([[10-Summaries/kaya-okur-2019-cut-and-tag]]; [[10-Summaries/wu-2021-sccut-tag]]).
- **Multiplexing routes**: barcoded adapters per antibody give direct co-localization of epitopes in the same cells ([[10-Summaries/gopalan-2022-multi-cut-and-tag]]), while adding surface protein enables computational interpolation of six marks per cell ([[10-Summaries/zhang-2022-sccut-tag-pro]]) — the latter explicitly *cannot* detect per-cell mark co-occurrence.

## Related

- [[30-Concepts/cut-and-run]] · [[30-Concepts/chic-seq]] · [[30-Concepts/chip-seq]] · [[30-Concepts/tn5-tagmentation]] · [[40-Topics/histone-modifications]] · [[20-Entities/steven-henikoff]]
- [[10-Summaries/kaya-okur-2019-cut-and-tag]] · [[10-Summaries/wu-2021-sccut-tag]] · [[10-Summaries/zhang-2022-sccut-tag-pro]] · [[10-Summaries/gopalan-2022-multi-cut-and-tag]]
