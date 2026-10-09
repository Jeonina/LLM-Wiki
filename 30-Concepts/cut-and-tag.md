---
type: concept
title: CUT&Tag
aliases: [Cleavage Under Targets and Tagmentation]
tags: [histone-modifications, Tn5, Henikoff-lab, in-situ]
created: 2026-05-12
updated: 2026-10-09
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

## Added 2026-10-07

Benchmarked against ENCODE ChIP-seq in K562, CUT&Tag recovered on average ~54% of ENCODE peaks for H3K27ac and H3K27me3 (max 63%), specifically the strongest and most accessible peaks, while reproducing ENCODE GO terms and TF motifs [[10-Summaries/abbasova-2025-cut-tag-encode-benchmark]]. For H3K27ac the expected signal-to-noise advantage over ChIP-seq was not observed (similar FRiP in overlapping regions), whereas H3K27me3 CUT&Tag gave about twice as many reads in overlapping intervals [[10-Summaries/abbasova-2025-cut-tag-encode-benchmark]]. HDAC inhibitors did not improve H3K27ac CUT&Tag [[10-Summaries/abbasova-2025-cut-tag-encode-benchmark]].

scNanoSeq-CUT&Tag ports single-cell CUT&Tag to nanopore with a single-adaptor pG-Tn5, giving up to 13,373 unique reads per cell across 17,211 cells, five histone marks plus CTCF and RAD21, and access to repeats and blacklist regions that short reads cannot map ([[10-Summaries/li-2024-scnanoseq-cut-tag]]). Merged tracks from as few as 146 cells were highly comparable with bulk ChIP-seq ([[10-Summaries/li-2024-scnanoseq-cut-tag]]).

**Independent pA-Tn5 design (CoBATCH, 2019).** Wang et al. fused protein A to the N-terminus of Tn5 for antibody-tethered tagmentation with one-tube library PCR, profiling histone marks from as few as 100 cells and also P300, CBP, EZH2 and NKX2-5 ([[10-Summaries/wang-2019-cobatch]]). The CoBATCH clipping cites CUT&RUN and ChIL-seq as precedents but not CUT&Tag, so it reads as a parallel development (synthesis).

**Plate-based variant that starts from single cells (OneCell CUT&Tag, 2026).** OneCell CUT&Tag sorts single cells into 384-well plates before any antibody step and runs the whole CUT&Tag protocol per well. This removes the ≥10⁴-cell input floor of bulk-targeting methods and yields 26,008 median unique reads/cell (FrIP 0.77) on MDA-MB-468 H3K27me3, against 5,156 for 10x droplet scCUT&Tag at equalized depth ([[10-Summaries/schwager-2026-onecell-cut-tag]]).

**Open-chromatin bias.** Because CUT&Tag uses Tn5, H3K27me3 libraries show false enrichment at active promoters: on average 18% of K562 H3K27me3 CUT&Tag peaks are absent from ChIP-seq and sit in ATAC-open regions, and the promoter excess persists across 277 datasets published since 2024, including high-salt protocols ([[10-Summaries/hu-2026-patty]]). PATTY corrects this with a mark-specific logistic-regression model using CUT&Tag plus ATAC-seq signal, validated for H3K27me3, H3K27ac and H3K9me3 ([[10-Summaries/hu-2026-patty]]). Deaminase-based DeChIC-seq reports low correlation with ATAC-seq, positioning it as an alternative without this bias ([[10-Summaries/shi-2026-dechic-seq]]).

A 2026 review catalogues 21 public scCUT&Tag-family datasets (2019–2025) spanning histone marks, CTCF/RAD21, Pol II, TFs, m6A and G-quadruplexes, typically with <10³ fragments per cell versus >10⁴ for scATAC-seq ([[10-Summaries/wu-2026-sccut-tag-review]]). Because pA-Tn5 is tethered to the epitope, TF events appear as narrow high-amplitude peaks rather than ATAC-style footprint dips ([[10-Summaries/wu-2026-sccut-tag-review]]). For analysis, a systematic benchmark recommends 100–200 kbp fixed bins, no feature selection, and TF-IDF followed by SVD or NMF ([[10-Summaries/raimundo-2023-schptm-benchmark]]).


Droplet scCUT&Tag runs bulk CUT&Tag with 1% BSA against nuclear clumping, then loads tagmented nuclei into the 10x scATAC kit with its transposition step skipped, giving a median 98–453 unique fragments per cell across four histone marks in 47,340 mouse brain cells ([[10-Summaries/bartosovic-2021-sccut-tag]]).

nano-CUT&Tag tagments first with P5-only adapters and linearly amplifies before a second P7 tagmentation, so single-insertion fragments become library molecules; H3K27me3 fragments per cell rose 15.8-fold over scCUT&Tag while FrIP fell from 69% to 39% ([[10-Summaries/bartosovic-2022-nano-cut-tag]]).

## Added 2026-10-09 — foundation-model gap evidence

- On Bartosovic 2021 mouse-brain scCUT&Tag downsampled to about 1,000 reads per cell, only scImpute raised H3K4me3 signal at neuronal ChIP-seq peaks, while scOpen and SCALEX improved clustering but spread Mbp signal into other clusters ([[10-Summaries/morenogonzalez-2025-schistone-imputation]])

## Related

- [[30-Concepts/cut-and-run]] · [[30-Concepts/chic-seq]] · [[30-Concepts/chip-seq]] · [[30-Concepts/tn5-tagmentation]] · [[40-Topics/histone-modifications]] · [[20-Entities/steven-henikoff]]
- [[10-Summaries/kaya-okur-2019-cut-and-tag]] · [[10-Summaries/wu-2021-sccut-tag]] · [[10-Summaries/zhang-2022-sccut-tag-pro]] · [[10-Summaries/gopalan-2022-multi-cut-and-tag]]
