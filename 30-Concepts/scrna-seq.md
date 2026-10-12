---
type: concept
title: scRNA-seq (single-cell RNA sequencing)
aliases: [single-cell RNA-seq, scRNA-Seq, single-cell transcriptomics, mRNA-Seq from one cell]
tags: [transcriptomics, single-cell, sequencing-modality, founding-concept]
created: 2026-05-14
updated: 2026-10-12
---

# scRNA-seq

> Sequencing of the polyadenylated (and increasingly the total) mRNA content of individual cells, producing a per-cell × per-gene expression matrix that resolves cell-type heterogeneity invisible to bulk RNA-seq ([[10-Summaries/tang-2009-scrna-seq|Tang 2009]]; [[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).

> [!abstract] 한눈에
> scRNA-seq는 세포 하나하나의 mRNA를 cell barcode와 UMI로 표지해 읽어, bulk 평균에 가려진 cell type 구성과 희귀 집단, 분화 경로를 드러내는 방법이다 ([[10-Summaries/tang-2009-scrna-seq|Tang 2009]]; [[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]). 대신 세포당 transcript의 일부만 포착되므로 검출되지 않은 것이 곧 발현이 없다는 뜻은 아니다 ([[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]).

## Definition

scRNA-seq captures and amplifies the mRNA from one cell at a time, then sequences the resulting cDNA library ([[10-Summaries/tang-2009-scrna-seq|Tang 2009]]). Each transcript carries two tags that bulk RNA-seq lacks: a **cell barcode** identifying the cell of origin and, in modern protocols, a **[[30-Concepts/umi-molecular-barcoding|UMI]]** identifying the individual mRNA molecule before PCR amplification ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]). The output is a sparse cells × genes count matrix, typically with tens of thousands of cells and 1,000–10,000 detected genes per cell (synthesis).

## Why it matters

Bulk RNA-seq reports the **arithmetic mean** of expression across all input cells, which misleads whenever the sample mixes cell types or states — essentially every biological tissue (synthesis). scRNA-seq fixes three failure modes of bulk:

1. **Cell-type composition confounding.** A change in bulk expression of gene *X* may reflect a real change in transcription per cell or merely a shift in the proportion of cells that express *X*; bulk cannot tell them apart (synthesis).
2. **Rare-population invisibility.** A programme present in 1% of cells contributes ~1% to the bulk signal, below typical detection thresholds; scRNA-seq resolves rare populations given enough cells (synthesis). In the Drop-seq retina atlas, clusters as small as 0.1–0.9% of input emerged as cell numbers grew ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).
3. **State-transition averaging.** Cells along a developmental trajectory vary continuously; bulk collapses the trajectory to one point, while scRNA-seq preserves the gradient and supports pseudotime ordering (synthesis).

For this scDNA/multi-omics wiki, scRNA-seq is the **transcriptomic axis** of every joint-omics method: it is what [[30-Concepts/got|GoT]] genotypes against, what DR-seq / G&T-seq / scTrio-seq couple to scDNA, what SHARE-seq and 10x Multiome couple to chromatin accessibility, and what [[30-Concepts/cite-seq|CITE-seq]] couples to surface protein (synthesis). Without scRNA-seq there is no single-cell multi-omics (synthesis).

### Bulk RNA-seq vs. scRNA-seq (review framing)

The argument structure for an introduction section (synthesis):

1. **Bulk RNA-seq** mixes the transcriptomes of millions of cells in one sample and measures the population mean. It is cheap, deep and quantitative — and blind to cell-type composition.
2. **For homogeneous samples** (cell lines, sorted populations), bulk is fine.
3. **For heterogeneous tissue** (tumour, brain, immune system, development), bulk's mean is a fiction — no individual cell expresses the bulk profile.
4. **scRNA-seq** restores cell-level resolution at a cost: each cell is sampled shallowly (roughly 0.5–10% of its transcripts captured; [[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]), so technical noise is high per cell but population structure is recoverable across thousands of cells.
5. **For somatic mutation work**, bulk RNA-seq cannot tell you *which cell type* carries a mutational signature in its expression programme; methods like [[30-Concepts/got|GoT]] need scRNA-seq as their substrate.

## Method axes

scRNA-seq protocols differ along several design axes that matter for review framing (synthesis):

| Axis | Options | Tradeoff | Source |
|---|---|---|---|
| Cell isolation | FACS · Fluidigm C1 · droplets · combinatorial indexing · nanowells | Throughput vs. control over individual cells | (synthesis) |
| Transcript coverage | 3'-end · 5'-end · full-length | Throughput vs. isoform resolution | (synthesis) |
| Amplification chemistry | PCR (SMART) · IVT (CEL-seq) | Bias vs. linear quantification | (synthesis) |
| Quantification | Read counts · UMI-collapsed counts | Saturation behaviour, see [[30-Concepts/umi-molecular-barcoding]] | ([[10-Summaries/svensson-2017-power-analysis\|Svensson 2017]]) |
| Throughput per run | 10² (plate) → 10³ (microfluidic) → 10⁴–10⁵ (droplet) → 10⁶ (combinatorial) | Cells per experiment vs. per-cell quality | (synthesis) |
| Cost per cell | $10+ (plate, full-length) → ~$0.05 (droplet) | Coverage vs. atlas scale | (synthesis) |

### History

- **2009 — Tang et al.**: first whole-transcriptome mRNA-Seq from a single mouse blastomere; plate-based, with anchored oligo(dT) reverse transcription, terminal-transferase poly(A) tailing and PCR amplification ([[10-Summaries/tang-2009-scrna-seq|Tang 2009]]).
- **2011–2014**: plate-based protocols mature — Smart-seq, CEL-seq, MARS-seq, STRT-seq — with throughput in the hundreds to low thousands of cells (synthesis).
- **2015 — Drop-seq and inDrop**: droplet-microfluidic scRNA-seq (Macosko 2015; Klein et al. 2015) cuts per-cell cost ~100× and enables 10,000+ cells per experiment ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).
- **2016+**: commercial 10x Genomics Chromium democratises the droplet approach; sci-RNA-seq and SPLiT-seq pioneer [[30-Concepts/combinatorial-indexing|combinatorial-indexing]] scaling without microfluidics (synthesis).
- **2017 — Svensson et al.** benchmark 15 protocols on ERCC spike-ins, quantifying the sensitivity–throughput tradeoff ([[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]).
- **2020s**: full-length UMI protocols (Smart-seq3), spatial transcriptomics (Visium, Slide-seq, MERFISH) and multimodal extensions (10x Multiome, [[30-Concepts/dogma-seq|DOGMA-seq]], [[30-Concepts/cite-seq|CITE-seq]]) (synthesis).

## Evidence and examples

- On a single blastomere, Tang 2009 detected ~75% more genes than microarray on the same cell ([[10-Summaries/tang-2009-scrna-seq|Tang 2009]]).
- Drop-seq made droplet scRNA-seq practical at 10,000+ cells per experiment ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]); see [[30-Concepts/drop-seq]].
- Capture efficiency is roughly 0.5–10% of input molecules, with endogenous mRNA at ~5–10% of smFISH counts ([[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]).

## Contested points and limitations

- **Dropout / technical zeros.** At 0.5–10% capture, absent counts ≠ absent expression ([[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]).
- **Loss of spatial context.** Dissociation destroys tissue architecture, which motivates spatial transcriptomics (synthesis).
- **mRNA-only readout.** It misses regulatory state (chromatin, methylation), genotype and protein, which motivates multi-omics extensions such as [[30-Concepts/scnmt-seq|scNMT-seq]] and [[30-Concepts/sci-car|sci-CAR]] (synthesis).
- **Cell-state perturbation.** Dissociation stress induces immediate-early genes (Fos, Jun), a confound for activation signatures (synthesis).
- **Cost per gene per cell** is still substantially higher than bulk, so large studies trade cell number against per-cell coverage (synthesis).
- **Cell-type-resolved differential expression** often aggregates cells back to a bulk-like profile ([[30-Concepts/pseudo-bulk|pseudo-bulk]]) (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/drop-seq|Drop-seq]] — Droplet-microfluidic scRNA-seq with barcoded beads.
> - `concept` [[30-Concepts/umi-molecular-barcoding|UMI / molecular barcoding]] — Per-molecule tags that collapse PCR duplicates.
> - `concept` [[30-Concepts/combinatorial-indexing|Combinatorial indexing]] — Split-pool barcoding that scales without microfluidics.
> - `concept` [[30-Concepts/pseudo-bulk|Pseudo-bulk]] — Aggregation of scRNA-seq back to a bulk-like profile for differential expression at cell-type resolution.
> - `concept` [[30-Concepts/got|GoT]] — scRNA-seq plus targeted DNA genotyping.
> - `concept` [[30-Concepts/cite-seq|CITE-seq]] — scRNA-seq plus surface protein.
> - `concept` [[30-Concepts/dogma-seq|DOGMA-seq]] — RNA, accessibility and protein from the same cell.
> - `concept` [[30-Concepts/scnmt-seq|scNMT-seq]] — RNA, methylation and accessibility from the same cell.
> - `concept` [[30-Concepts/sci-car|sci-CAR]] — Joint RNA and accessibility by combinatorial indexing.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multi-omics]] — Assays that pair the transcriptome with other modalities.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]
> - [[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]
> - [[10-Summaries/tang-2009-scrna-seq|Tang 2009]]
