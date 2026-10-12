---
type: concept
title: Joint single-cell multi-omics
aliases: [joint multi-omics, paired multi-omics, same-cell multi-modal]
tags: [single-cell, multiomics, paired-measurement]
created: 2026-05-19
updated: 2026-10-12
---

# Joint single-cell multi-omics

> Single-cell methods that measure two or more molecular modalities from the same individual cell (or nucleus), as opposed to integrating mono-omic datasets computationally; the defining feature is *physical co-capture* of modalities within a single droplet, well or fiber ([[10-Summaries/wang-2023-multimodal-review|Wang 2023]]).

> [!abstract] 한눈에
> Joint multi-omics는 한 세포 안에서 DNA, RNA, accessibility, methylation, histone mark 같은 여러 층을 함께 읽는 방법이고, 따로 측정한 데이터를 계산으로 묶는 integration과는 다르다 ([[10-Summaries/wang-2023-multimodal-review|Wang 2023]]). 같은 세포에서 잰 modality끼리도 세포 정체성을 다르게 말할 수 있으며, 진짜 paired data가 부족하다는 점이 foundation model 학습의 제약이 된다 ([[10-Summaries/schwager-2026-onecell-cut-tag|OneCell CUT&Tag]]; [[10-Summaries/liu-2025-scmomer|scMomer]]).

## Definition

A joint multi-omic assay reads two or more of DNA sequence, RNA, chromatin accessibility, DNA methylation, histone modifications, surface protein, intracellular protein and 3D contacts within the same physical compartment ([[10-Summaries/wang-2023-multimodal-review|Wang 2023]]). This contrasts with **integration of unpaired data** (matrix factorization, manifold alignment), which infers joint structure from separately measured modalities ([[10-Summaries/wang-2023-multimodal-review|Wang 2023]]). See [[40-Topics/single-cell-multiomics]] for the methods landscape.

## Why it matters

- It pairs cause and effect at single-cell resolution: whether a given mutation alters the same cell's accessibility can only be answered by joint measurement (synthesis).
- It avoids the batch effects and clustering artifacts that can confound unpaired integration (synthesis).

## Variants

| Modalities | Assay | Design | Source |
|---|---|---|---|
| Genome + transcriptome | G&T-seq | — | ([[10-Summaries/macaulay-2015-gt-seq\|G&T-seq]]) |
| Genome + transcriptome | DR-seq | — | ([[10-Summaries/dey-2015-dr-seq\|DR-seq]]) |
| Genotype + transcriptome | GoT | — | ([[10-Summaries/nam-2019-got\|GoT]]) |
| Whole-genome DNA + RNA | DEFND-seq | Nucleosome depletion + 10x Multiome; genome-wide breadth, high allelic dropout | ([[10-Summaries/olsen-2025-defnd-seq\|DEFND-seq]]; [[10-Summaries/lindenhofer-2025-sdr-seq\|SDR-seq]]) |
| Targeted DNA + RNA | SDR-seq | Tapestri; targeted depth, low allelic dropout, per-cell zygosity | ([[10-Summaries/lindenhofer-2025-sdr-seq\|SDR-seq]]) |
| Whole-genome DNA + accessibility | wellDA-seq | Thousands of cells (22,123 cells from 11 breast tissues) | ([[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]]) |
| Long-read genotype + accessibility + transcriptome | SPLONGGET | Full-length transcripts in the same cell | ([[10-Summaries/pancikova-2025-splongget\|SPLONGGET]]) |
| Mutation + chromatin + RNA | Duplex-Multiome | — | ([[10-Summaries/kriz-2025-duplex-multiome\|Duplex-Multiome]]) |
| Chromatin accessibility + transcriptome | sci-CAR | — | ([[10-Summaries/cao-2018-sci-car\|sci-CAR]]) |
| Chromatin accessibility + transcriptome | SHARE-seq | — | ([[10-Summaries/ma-2020-share-seq\|SHARE-seq]]) |
| Methylation + chromatin + RNA | scNMT-seq | — | ([[10-Summaries/clark-2018-scnmt-seq\|scNMT-seq]]) |
| Accessibility + genome-wide methylation | sciMET+ATAC | Tagment native nuclei, then re-tagment after nucleosome disruption with a different index set | ([[10-Summaries/nichols-2025-scimetv3\|sciMETv3]]) |
| Transcriptome + methylome | scM&T-seq | 87 mESCs, analysed with a factor model | ([[10-Summaries/argelaguet-2018-mofa\|MOFA]]) |
| Histone mark + transcriptome + surface markers | OneCell CUT&Tag | H3K27me3 or H3K4me1, full-length FLASH-seq transcriptome and index-sorted surface markers matched by plate/well coordinates, from inputs as low as one cell | ([[10-Summaries/schwager-2026-onecell-cut-tag\|OneCell CUT&Tag]]) |
| Chromatin conformation + transcriptome | Paired Hi-C | Droplet Hi-C adapted to the 10x Multiome kit, with milder SDS, 0.6% formaldehyde and a revised cDNA preparation | ([[10-Summaries/chang-2025-droplet-hi-c\|Chang 2025]]) |

The two scalable droplet DNA + RNA designs trade **genome-wide breadth (high ADO)** against **targeted depth (low ADO, per-cell zygosity)** ([[10-Summaries/lindenhofer-2025-sdr-seq|SDR-seq]]).

## Evidence and examples

**Assay performance**

- Paired Hi-C gave 12,361 joint profiles from mouse cortex at 42,210 Hi-C read pairs and a median of 3,914 UMIs per cell ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]).
- sciMET+ATAC had 5,305 cells pass both modalities, with lower per-modality quality (TSS enrichment 5.2) than unimodal assays ([[10-Summaries/nichols-2025-scimetv3|sciMETv3]]).
- Re-analysis of public scHi-C datasets found that multi-omic scHi-C protocols such as sn-m3C-seq and HiRES capture as many contacts per cell, with similar cis/trans ratios, as contact-only protocols (no significant difference) ([[10-Summaries/dautle-2025-schic-review|Dautle 2025]]).

**Biological findings**

- In mouse mammary gland, on average 9% of cells called basal by cytometry and RNA fell in the ER⁻ luminal cluster in both histone embeddings, reproducibly across five mice ([[10-Summaries/schwager-2026-onecell-cut-tag|OneCell CUT&Tag]]).
- wellDA-seq maps epigenomic phenotypes directly onto copy-number-defined subclones and finds evidence for both genetic hardwiring and epigenetic plasticity ([[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]).
- SPLONGGET targets genotype-to-phenotype questions, such as splice-site immune-escape mutations, that need full-length transcripts in the same cell ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).
- In scM&T-seq data from 87 mESCs, one factor shared across RNA and methylation at promoters, enhancers and CpG islands explained 7% of RNA variance but 53–72% of methylation variance, and tracked the naive → primed pluripotency transition ([[10-Summaries/argelaguet-2018-mofa|MOFA]]).

**Joint data as training data for sequence and foundation models**

- Borzoi's authors found that accessibility data improved RNA-seq predictions and proposed single-cell multiome (ATAC + RNA) data as valuable joint training data for sequence-to-function models ([[10-Summaries/linder-2025-borzoi|Borzoi]]).
- Because truly paired RNA + ATAC data are scarce, scMomer pretrains its fusion stage on scCLIP's pseudo-paired fetal atlas (RNA and ATAC cells matched only by cell-type label), then distils ATAC knowledge into an RNA-only path ([[10-Summaries/liu-2025-scmomer|scMomer]]).
- scDynOmics pretrains on 752,155 public mouse joint RNA + ATAC cells (SHARE-seq, SNARE-seq, sci-CAR, Paired-seq, ISSAAC-seq, 10x Multiome), treating promoter accessibility as analogous to unspliced pre-mRNA in an RNA-velocity view ([[10-Summaries/yu-2026-scdynomics|scDynOmics]]).

## Contested points

- **Same-cell modalities can disagree on identity.** The OneCell CUT&Tag mammary-gland result shows that co-capture does not guarantee concordant cell-type calls ([[10-Summaries/schwager-2026-onecell-cut-tag|OneCell CUT&Tag]]).
- **Joint capture can cost per-modality quality.** sciMET+ATAC is weaker per modality than unimodal assays ([[10-Summaries/nichols-2025-scimetv3|sciMETv3]]), and the Paired Hi-C authors flag Hi-C library complexity as the main limitation ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]); multi-omic scHi-C, by contrast, showed no contact deficit ([[10-Summaries/dautle-2025-schic-review|Dautle 2025]]).
- **Breadth versus depth in DNA + RNA.** Whole-genome droplet designs accept high allelic dropout, while targeted designs give per-cell zygosity on fewer loci ([[10-Summaries/lindenhofer-2025-sdr-seq|SDR-seq]]).
- **Pseudo-pairing is a stand-in, not a substitute.** scMomer's pseudo-paired cells are matched only by cell-type label ([[10-Summaries/liu-2025-scmomer|scMomer]]), so they cannot carry cell-level coupling between modalities (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/defnd-seq|DEFND-seq]] — Droplet co-sequencing of genomic DNA and RNA from the same nucleus via the stock 10x Multiome kit.
> - `concept` [[30-Concepts/sdr-seq|SDR-seq]] — Targeted droplet DNA + RNA on Tapestri, with per-cell variant zygosity.
> - `concept` [[30-Concepts/allele-dropout|Allele dropout]] — One allele failing to amplify, the cost of genome-wide breadth.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multi-omics]] — Methods that measure two or more modalities in the same cell.
> - `note` [[50-Notes/regulatory-layers-overview|Regulatory layers]] — The five (or six) axes of epigenome interpretation.
> - `note` [[50-Notes/droplet-vs-single-molecule-scdna|Droplet vs single-molecule scDNA]] — The breadth/depth tradeoff between scDNA architectures.

## All sources on this page

> [!info]- 20 summaries cited here
> - [[10-Summaries/argelaguet-2018-mofa|Argelaguet 2018]]
> - [[10-Summaries/cao-2018-sci-car|Cao 2018]]
> - [[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]
> - [[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]
> - [[10-Summaries/dautle-2025-schic-review|Dautle 2025]]
> - [[10-Summaries/dey-2015-dr-seq|Dey 2015]]
> - [[10-Summaries/kriz-2025-duplex-multiome|Kriz 2025]]
> - [[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]
> - [[10-Summaries/linder-2025-borzoi|Borzoi 2025]]
> - [[10-Summaries/liu-2025-scmomer|scMomer 2025]]
> - [[10-Summaries/ma-2020-share-seq|Ma 2020]]
> - [[10-Summaries/macaulay-2015-gt-seq|Macaulay 2015]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
> - [[10-Summaries/nichols-2025-scimetv3|Nichols 2025]]
> - [[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]
> - [[10-Summaries/pancikova-2025-splongget|Pančíková 2025 (bioRxiv preprint)]]
> - [[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]
> - [[10-Summaries/wang-2023-multimodal-review|Wang 2023]]
> - [[10-Summaries/wang-2024-wellda-seq|Wang 2024]]
> - [[10-Summaries/yu-2026-scdynomics|scDynOmics 2026]]
