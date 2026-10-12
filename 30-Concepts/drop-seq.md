---
type: concept
title: Drop-seq
aliases: [Drop-Seq, droplet scRNA-seq]
tags: [scRNA-seq, droplet-microfluidics, UMI, STAMP, founding-method]
created: 2026-05-14
updated: 2026-10-12
---

# Drop-seq

> A droplet-microfluidic scRNA-seq method that co-encapsulates single cells with barcoded oligo-dT-coated microparticles in nanoliter droplets, so that each cell's mRNA is captured on its companion bead for parallel, high-throughput transcriptome profiling ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).

> [!abstract] 한눈에
> Drop-seq는 세포 하나와 barcode가 달린 bead 하나를 nanoliter droplet에 함께 가둬 mRNA를 bead에 붙잡는 scRNA-seq 방법으로, 한 번에 수천 개 세포를 세포당 약 6.5센트에 분석할 수 있게 했다 ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]). bead + droplet + cell barcode라는 설계는 10x Chromium과 대부분의 droplet 기반 multi-omics 방법으로 이어졌지만, 3' 말단만 읽고 포획률이 약 13%에 그친다는 한계도 함께 물려받았다 ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]; [[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]).

## Definition

Drop-seq generates **STAMPs** (Single-cell Transcriptomes Attached to Microparticles) in four steps ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]):

1. A cell suspension and a bead suspension are co-flowed across an oil channel in a microfluidic device, forming ~1-nL droplets at more than 100,000 per minute ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).
2. Cells are lysed inside the droplets ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).
3. Poly-A mRNAs hybridise to the bead's oligo-dT primers, which also carry a constant adapter, a cell barcode unique to the bead (12 nt, ~17M combinations from split-pool synthesis) and a per-primer UMI (8 nt, random) ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).
4. Droplets are broken, STAMPs pooled, and reverse transcription and 3'-end library preparation run in bulk ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).

The cell of origin is recovered afterwards from the cell barcode embedded in each read ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).

## Why it matters

- **It opened the cell-atlas era.** Drop-seq and inDrop (Klein et al., same *Cell* issue) moved scRNA-seq from a few hundred to a few thousand cells per study to tens of thousands, at about $0.07 rather than $10+ per cell, which directly enabled the Human Cell Atlas, Tabula Muris/Sapiens and per-disease atlases ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]; atlas names and the $10+ figure: synthesis).
- **Its architecture is inherited.** The commercial 10x Genomics Chromium platform is a refinement of Drop-seq (gel beads instead of solid beads, dissolvable on activation), and most droplet-based multi-omics methods (10x Multiome, CITE-seq, GoT, DOGMA-seq, Tapestri DAb-seq) keep its bead + droplet + cell-barcode design ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]; [[10-Summaries/nam-2019-got|GoT]]).

## Bead architecture

Each bead carries millions of copies of one oligo with four concatenated parts, 5' to 3' ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]):

```
[PCR/sequencing primer site] [cell barcode 12nt] [UMI 8nt] [oligo-dT capture (T30)]
```

| Part | How it is made | What it does | Source |
|---|---|---|---|
| Cell barcode (12 nt) | Split-and-pool synthesis: beads split into four wells (A/G/C/T), one base added per well, pooled and re-split, 12 times, giving 4¹² = 16,777,216 barcodes | Identical on every primer of one bead, different between beads; identifies the cell | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]) |
| UMI (8 nt) | Eight rounds of degenerate synthesis, giving 4⁸ = 65,536 tags per bead | Separates PCR duplicates from genuine repeat captures; see [[30-Concepts/umi-molecular-barcoding\|UMI barcoding]] | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]; 4⁸ count: synthesis) |
| Oligo-dT | — | Captures poly-A mRNA | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]) |

This bead design is the conceptual basis for 10x gel beads, sciRNA-seq combinatorial barcodes and the bead-barcode component of nearly every droplet-based multi-omics method; the split-pool trick also seeds [[30-Concepts/combinatorial-indexing|combinatorial indexing]] ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).

## Key performance numbers

| Metric | Value | Source |
|---|---|---|
| Cells per 12-h run | ~10,000 | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]) |
| Cost per cell | ~$0.065 | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]) |
| Transcript capture rate | ~12.8% (UMI-collapsed); ddPCR-confirmed at 10.7% | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]) |
| Cell-barcode space | 4¹² ≈ 17M combinations | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]) |
| Doublet rate | 0.36% (at 12.5 cells/µL) to 11.3% (at 100 cells/µL) | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]) |
| Single-cell purity | 98.8% to 90.4% across the same range | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]) |

## Successors and variants

| Method | Builds on Drop-seq via | Adds | Source |
|---|---|---|---|
| inDrop (Klein 2015) | Same *Cell* issue, parallel invention | Hydrogel beads released by photocleavage | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]; bead release: synthesis) |
| 10x Chromium | Commercial gel-bead refinement | Higher capture, robust kits | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]; capture and kits: synthesis) |
| [[10-Summaries/nam-2019-got\|GoT]] | 10x backbone | Targeted DNA genotyping from cDNA | ([[10-Summaries/nam-2019-got\|GoT]]) |
| CITE-seq | 10x backbone | Surface-protein readout via antibody-DNA | (synthesis) |
| 10x Multiome | 10x backbone | Joint scRNA + scATAC from the same cell | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]) |
| DOGMA-seq | 10x backbone | Joint scRNA + scATAC + surface protein | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]) |
| Tapestri DAb-seq | Droplet backbone | scDNA targeted genotyping + protein | ([[10-Summaries/macosko-2015-drop-seq\|Macosko 2015]]) |

## Evidence and examples

- Human–mouse species-mixing experiments measured doublet rates of 0.36–11.3% and single-cell purity of 90–99%, depending on cell concentration ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).
- The 12.8% capture estimate was corroborated independently by ddPCR at 10.7% ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).
- [[10-Summaries/svensson-2017-power-analysis|Svensson 2017]] benchmarks Drop-seq against peer protocols ([[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]).
- [[10-Summaries/nam-2019-got|GoT]] is a direct methodological descendant, adding targeted genotyping to the 10x/Drop-seq backbone ([[10-Summaries/nam-2019-got|GoT]]).

## Limitations

- **3'-end only.** There is no isoform resolution; full-length protocols (Smart-seq2/3) trade throughput for transcript coverage ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).
- **Ambient RNA contamination.** Preparing the cell suspension releases mRNA from damaged cells; this background is captured non-specifically and inflates rare-cell expression of high-abundance markers, for example rod-cell genes appearing in non-rod retinal clusters ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).
- **Gene dropout.** The ~13% capture rate makes low-expressed genes systematically zero-inflated; see [[10-Summaries/svensson-2017-power-analysis|Svensson 2017]] for a quantitative benchmark ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]; [[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]).
- **Doublet–concentration tradeoff.** Pushing throughput raises the doublet rate (Poisson loading) ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]); doublet detection (Scrublet, DoubletFinder) is now standard post-processing (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/scrna-seq|scRNA-seq]] — Parent concept: sequencing the transcriptome of single cells.
> - `concept` [[30-Concepts/umi-molecular-barcoding|UMI molecular barcoding]] — The per-molecule barcoding mechanic Drop-seq put on every primer.
> - `concept` [[30-Concepts/combinatorial-indexing|Combinatorial indexing]] — The alternative scaling principle, with no droplets.

People: [[20-Entities/evan-macosko]] · [[20-Entities/aviv-regev]] · [[20-Entities/steven-mccarroll]]. Founding paper: [[10-Summaries/macosko-2015-drop-seq|Macosko 2015]].

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
> - [[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]
