---
type: concept
title: CUT&Tag
aliases: [Cleavage Under Targets and Tagmentation]
tags: [histone-modifications, Tn5, Henikoff-lab, in-situ]
created: 2026-05-12
updated: 2026-10-12
---

# CUT&Tag

> An antibody-directed in-situ chromatin profiling method developed by Kaya-Okur and Henikoff (2019): a Tn5 transposase fused to protein A (pA-Tn5) is tethered to histone-modification-bound chromatin via a primary and secondary antibody, and Mg²⁺-catalysed tagmentation then deposits sequencing adapters at the target sites within intact nuclei ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]).

> [!abstract] 한눈에
> CUT&Tag는 항체로 pA-Tn5를 표적 chromatin에 붙인 뒤 그 자리에서 tagmentation을 일으키는 방법이며, fragment가 핵 안에 남기 때문에 single-cell로 확장된다 ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]). 다만 Tn5 때문에 열린 chromatin 쪽으로 신호가 치우치는 편향이 모든 데이터에 남는다 ([[10-Summaries/hu-2026-patty|PATTY]]).

## Definition

The standard reference is Kaya-Okur et al. 2019, *Nat Commun* ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]). The workflow is: light formaldehyde fixation → nuclei isolation → primary antibody → secondary antibody → pA-Tn5 binding → Mg²⁺-triggered tagmentation → SDS release → PCR with indexed primers → sequencing; the founding paper itself describes unfixed cells (see Contested points) ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]).

The fusion protein stays bound to DNA after cleavage, so fragments are retained within intact nuclei. CUT&RUN's MNase instead releases fragments into the supernatant; with CUT&Tag, adapters are added *in bulk* before cells are separated, which is why CUT&Tag is single-cell-compatible and CUT&RUN is not ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]).

## Why it matters

- It needs far fewer reads than older methods: ~2 M CUT&Tag reads ≈ 8 M CUT&RUN ≈ 20 M ChIP-seq ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]).
- It is rapidly replacing ChIP-seq as the standard chromatin-profiling method (synthesis).
- It scales to single cells (scCUT&Tag) and to combinatorial indexing (sciCUT&Tag) ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]; [[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]).
- It underpins methods that read DNA modifications at chromatin sites, such as [[30-Concepts/6-base-cut-and-tag|6-base-CUT&Tag]] ([[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]).

## Variants

| Variant | What changes | Scale / key number | Source |
|---|---|---|---|
| CoBATCH (independent pA-Tn5 design, 2019) | Protein A fused to the N-terminus of Tn5; one-tube library PCR; histone marks plus P300, CBP, EZH2 and NKX2-5 | As few as 100 cells | ([[10-Summaries/wang-2019-cobatch\|CoBATCH]]) |
| scCUT&Tag in nanowells | All steps through tagmentation in bulk, then single cells dispensed into a nanowell chip | — | ([[10-Summaries/kaya-okur-2019-cut-and-tag\|Kaya-Okur 2019]]; [[10-Summaries/wu-2021-sccut-tag\|Wu 2021]]) |
| Droplet scCUT&Tag | Bulk CUT&Tag with 1% BSA against nuclear clumping, then tagmented nuclei loaded into the 10x scATAC kit with its transposition step skipped | Median 98–453 unique fragments per cell across four histone marks; 47,340 mouse brain cells | ([[10-Summaries/bartosovic-2021-sccut-tag\|Bartosovic 2021]]) |
| sciCUT&Tag | Combinatorial indexing | — | ([[10-Summaries/janssens-2023-scicut-tag\|Janssens 2023]]) |
| Multi-CUT&Tag | Barcoded adapters per antibody give direct co-localisation of epitopes in the same cells | — | ([[10-Summaries/gopalan-2022-multi-cut-and-tag\|Gopalan 2022]]) |
| scCUT&Tag-pro | Adds surface protein, enabling computational interpolation of six marks per cell; cannot detect per-cell mark co-occurrence | Six marks per cell | ([[10-Summaries/zhang-2022-sccut-tag-pro\|Zhang 2022]]) |
| nano-CUT&Tag | Tagments first with P5-only adapters and linearly amplifies before a second P7 tagmentation, so single-insertion fragments become library molecules | H3K27me3 fragments per cell up 15.8-fold over scCUT&Tag; FrIP down from 69% to 39% | ([[10-Summaries/bartosovic-2022-nano-cut-tag\|Bartosovic 2022]]) |
| scNanoSeq-CUT&Tag | Nanopore readout with a single-adaptor pG-Tn5; reaches repeats and blacklist regions that short reads cannot map | Up to 13,373 unique reads per cell; 17,211 cells; five histone marks plus CTCF and RAD21 | ([[10-Summaries/li-2024-scnanoseq-cut-tag\|scNanoSeq-CUT&Tag]]) |
| OneCell CUT&Tag | Single cells sorted into 384-well plates before any antibody step; whole protocol per well, removing the ≥10⁴-cell input floor of bulk-targeting methods | 26,008 median unique reads per cell (FrIP 0.77) on MDA-MB-468 H3K27me3 | ([[10-Summaries/schwager-2026-onecell-cut-tag\|OneCell CUT&Tag]]) |
| 6-base-CUT&Tag | DNA-modification readout at the tagmented fragments | — | ([[10-Summaries/tavares-2026-6-base-cut-tag\|Tavares 2026]]) |

## Analysis of single-cell data

- A systematic benchmark recommends 100–200 kbp fixed bins, no feature selection, and TF-IDF followed by SVD or NMF ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]).
- Because pA-Tn5 is tethered to the epitope, TF events appear as narrow high-amplitude peaks rather than ATAC-style footprint dips ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).
- PATTY corrects the open-chromatin bias with a mark-specific logistic-regression model using CUT&Tag plus ATAC-seq signal, validated for H3K27me3, H3K27ac and H3K9me3 ([[10-Summaries/hu-2026-patty|PATTY]]).
- The ATAC background can be used as a QC axis in single cells ([[10-Summaries/wu-2021-sccut-tag|Wu 2021]]).

## Evidence and examples

**Founding results**

- ChIP-seq's H3K4me1 dynamic range is ~1/20 of CUT&Tag's, and only CUT&Tag reaches FRiP 0.6 ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]).
- Inputs from 100,000 down to 60 cells gave near-identical H3K27me3 profiles ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]).
- The CTCF footprint is ~80 bp, against ~45 bp MNase protection ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]).
- Repressive marks work best at single-cell scale because feature breadth (~5 nucleosomes for H3K4me2 versus hundreds for H3K27me3 domains) compensates for sparse sampling; H3K27me3 types cells at 300–1,100 fragments per cell ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]; [[10-Summaries/wu-2021-sccut-tag|Wu 2021]]).

**Benchmarks against ChIP-seq**

- In K562, CUT&Tag recovered on average ~54% of ENCODE ChIP-seq peaks for H3K27ac and H3K27me3 (max 63%), specifically the strongest and most accessible peaks, while reproducing ENCODE GO terms and TF motifs ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]).
- For H3K27ac the expected signal-to-noise advantage over ChIP-seq was not observed (similar FRiP in overlapping regions), whereas H3K27me3 CUT&Tag gave about twice as many reads in overlapping intervals ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]).
- HDAC inhibitors did not improve H3K27ac CUT&Tag ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]).
- Merged scNanoSeq-CUT&Tag tracks from as few as 146 cells were highly comparable with bulk ChIP-seq ([[10-Summaries/li-2024-scnanoseq-cut-tag|scNanoSeq-CUT&Tag]]).

**Single-cell yield**

- OneCell CUT&Tag gave 26,008 median unique reads per cell against 5,156 for 10x droplet scCUT&Tag at equalised depth ([[10-Summaries/schwager-2026-onecell-cut-tag|OneCell CUT&Tag]]).
- A 2026 review catalogues 21 public scCUT&Tag-family datasets (2019–2025) spanning histone marks, CTCF/RAD21, Pol II, TFs, m6A and G-quadruplexes, typically with <10³ fragments per cell versus >10⁴ for scATAC-seq ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).
- On Bartosovic 2021 mouse-brain scCUT&Tag downsampled to about 1,000 reads per cell, only scImpute raised H3K4me3 signal at neuronal ChIP-seq peaks, while scOpen and SCALEX improved clustering but spread Mbp signal into other clusters ([[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025]]).

## Contested points

- **The ATAC background is real and diagnostic.** Untethered pA-Tn5 binds exposed DNA, so every run carries a low-level accessibility signal; salt stringency controls it, and in single cells it appears as a nucleosomal fragment-length ladder in specific clusters ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]; [[10-Summaries/wu-2021-sccut-tag|Wu 2021]]).
- **Open-chromatin bias persists in current protocols.** On average 18% of K562 H3K27me3 CUT&Tag peaks are absent from ChIP-seq and sit in ATAC-open regions, and the promoter excess persists across 277 datasets published since 2024, including high-salt protocols ([[10-Summaries/hu-2026-patty|PATTY]]). Deaminase-based DeChIC-seq reports low correlation with ATAC-seq, which positions it as an alternative without this bias ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]).
- **The signal-to-noise advantage depends on the mark.** The founding paper's large advantage over ChIP-seq ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]) did not hold for H3K27ac in the ENCODE comparison ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]) (synthesis).
- **Fixation.** This page's workflow lists light formaldehyde fixation, but the founding paper describes permeabilised, unfixed cells ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]); protocols may differ (synthesis).
- **Co-occurrence needs barcoded adapters.** scCUT&Tag-pro interpolates marks computationally and explicitly *cannot* detect per-cell mark co-occurrence ([[10-Summaries/zhang-2022-sccut-tag-pro|Zhang 2022]]), whereas Multi-CUT&Tag measures it directly ([[10-Summaries/gopalan-2022-multi-cut-and-tag|Gopalan 2022]]).
- **Yield versus specificity.** nano-CUT&Tag raised fragments per cell 15.8-fold but FrIP fell from 69% to 39% ([[10-Summaries/bartosovic-2022-nano-cut-tag|Bartosovic 2022]]).
- **CoBATCH as a parallel development.** The CoBATCH clipping cites CUT&RUN and ChIL-seq as precedents but not CUT&Tag, so it reads as a parallel development ([[10-Summaries/wang-2019-cobatch|CoBATCH]]) (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/cut-and-run|CUT&RUN]] — The pA-MNase predecessor; releases fragments, so it does not adapt to single cells.
> - `concept` [[30-Concepts/chic-seq|ChIC-seq]] — The original antibody-tethered MNase method behind CUT&RUN and CUT&Tag.
> - `concept` [[30-Concepts/chip-seq|ChIP-seq]] — The bulk-cell standard CUT&Tag is benchmarked against.
> - `concept` [[30-Concepts/tn5-tagmentation|Tn5 tagmentation]] — Simultaneous fragmentation and adapter insertion; also the source of the ATAC background.
> - `concept` [[30-Concepts/6-base-cut-and-tag|6-base-CUT&Tag]] — 5mC and 5hmC at the fragments tethered to a histone mark.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone marks and the methods that profile them in single cells.

People: [[20-Entities/steven-henikoff|Steven Henikoff]].

## All sources on this page

> [!info]- 17 summaries cited here
> - [[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]
> - [[10-Summaries/bartosovic-2021-sccut-tag|Bartosovic 2021]]
> - [[10-Summaries/bartosovic-2022-nano-cut-tag|Bartosovic 2022]]
> - [[10-Summaries/gopalan-2022-multi-cut-and-tag|Gopalan 2022]]
> - [[10-Summaries/hu-2026-patty|Hu 2026]]
> - [[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]
> - [[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]
> - [[10-Summaries/li-2024-scnanoseq-cut-tag|Li 2024]]
> - [[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025 SCIBED]]
> - [[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]
> - [[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]
> - [[10-Summaries/shi-2026-dechic-seq|Shi 2026]]
> - [[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]
> - [[10-Summaries/wang-2019-cobatch|Wang 2019]]
> - [[10-Summaries/wu-2021-sccut-tag|Wu 2021]]
> - [[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]
> - [[10-Summaries/zhang-2022-sccut-tag-pro|Zhang 2022]]
