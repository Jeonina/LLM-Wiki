---
type: concept
title: scRNA-seq (single-cell RNA sequencing)
aliases: [single-cell RNA-seq, scRNA-Seq, single-cell transcriptomics, mRNA-Seq from one cell]
tags: [transcriptomics, single-cell, sequencing-modality, founding-concept]
created: 2026-05-14
updated: 2026-05-14
---

# scRNA-seq

> Sequencing of the polyadenylated (and increasingly the total) mRNA content of individual cells, producing a per-cell × per-gene expression matrix that resolves cell-type heterogeneity invisible to bulk RNA-seq.

## Definition

scRNA-seq captures and amplifies the mRNA from one cell at a time, then sequences the resulting cDNA library. Each transcript is tagged with two pieces of information that are absent from bulk RNA-seq: a **cell barcode** identifying the cell of origin and (in modern protocols) a **[[30-Concepts/umi-molecular-barcoding|UMI]]** identifying the individual mRNA molecule before PCR amplification. Output is a sparse cells × genes count matrix, typically containing tens of thousands of cells and 1,000–10,000 detected genes per cell.

## Why it matters

Bulk RNA-seq reports the **arithmetic mean** of expression across all input cells. This mean is misleading whenever the sample contains a mixture of cell types or cell states — which is essentially every biological tissue. Three concrete failure modes of bulk RNA-seq that scRNA-seq fixes:

1. **Cell-type composition confounding.** A change in bulk expression of gene *X* may reflect an actual change in transcription per cell, or merely a shift in the proportion of cells that express *X*. Bulk cannot disambiguate.
2. **Rare-population invisibility.** A transcriptional program present in 1% of cells contributes ~1% to the bulk signal — below typical detection thresholds. scRNA-seq resolves populations down to ~0.1% with sufficient cell numbers ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]).
3. **State-transition averaging.** Cells along a developmental trajectory have continuously varying expression. Bulk collapses the trajectory to a single point; scRNA-seq preserves the gradient and supports pseudotime ordering.

For the scDNA/multi-omics wiki, scRNA-seq is the **transcriptomic axis** in every joint-omics method: it is what GoT genotypes against, what DR-seq / G&T-seq / scTrio-seq couple to scDNA, what SHARE-seq and 10x Multiome couple to chromatin accessibility, and what CITE-seq couples to surface protein. Without scRNA-seq there is no single-cell multi-omics.

## History

- **2009 — Tang et al.** ([[10-Summaries/tang-2009-scrna-seq]]): first whole-transcriptome mRNA-Seq from a single mouse blastomere. Plate-based, SMART template-switching cDNA synthesis, ~75% more genes detected than microarray on the same cell.
- **2011–2014**: Plate-based protocols mature — Smart-seq, CEL-seq, MARS-seq, STRT-seq. Throughput in the hundreds to low thousands of cells.
- **2015 — Drop-seq and inDrop**: Droplet-microfluidic scRNA-seq ([[10-Summaries/macosko-2015-drop-seq|Macosko 2015]], Klein et al. 2015) drops per-cell cost ~100× and enables 10,000+ cells per experiment.
- **2016+ — Commercial 10x Genomics Chromium** democratises the droplet approach; sci-RNA-seq and SPLiT-seq pioneer combinatorial-indexing-based scaling without microfluidics.
- **2017 — Svensson et al.** ([[10-Summaries/svensson-2017-power-analysis]]) benchmark 15 protocols on ERCC spike-ins, quantifying the sensitivity–throughput tradeoff.
- **2020s**: Full-length UMI protocols (Smart-seq3), spatial transcriptomics (Visium, Slide-seq, MERFISH), and multi-modal extensions (10x Multiome, DOGMA-seq, CITE-seq).

## Method axes

scRNA-seq protocols differ along several design axes that matter for review framing:

| Axis | Options | Tradeoff |
|---|---|---|
| Cell isolation | FACS · Fluidigm C1 · droplets · combinatorial indexing · nanowells | Throughput vs. control over individual cells |
| Transcript coverage | 3'-end · 5'-end · full-length | Throughput vs. isoform resolution |
| Amplification chemistry | PCR (SMART) · IVT (CEL-seq) | Bias vs. linear quantification |
| Quantification | Read counts · UMI-collapsed counts | Saturation behavior, see [[30-Concepts/umi-molecular-barcoding]] |
| Throughput per run | 10² (plate) → 10³ (microfluidic) → 10⁴–10⁵ (droplet) → 10⁶ (combinatorial) | Cells per experiment vs. per-cell quality |
| Cost per cell | $10+ (plate, full-length) → ~$0.05 (droplet) | Coverage vs. atlas-scale |

## Limitations

- **Dropout / technical zeros**: capture efficiency is typically 10–25% of endogenous mRNA molecules (quantified by [[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]); absent counts ≠ absent expression.
- **Loss of spatial context**: dissociation destroys tissue architecture (motivating spatial transcriptomics).
- **mRNA-only readout**: misses regulatory state (chromatin, methylation), genotype, protein. Motivates multi-omics extensions.
- **Cell-state perturbation**: dissociation stress induces immediate-early genes (Fos, Jun) — a confound for activation signatures.
- **Cost per gene per cell**: still substantially higher than bulk; large studies tradeoff between cell number and per-cell coverage.

## Bulk RNA-seq vs. scRNA-seq (review framing)

The argument structure for an introduction section:

1. **Bulk RNA-seq** mixes the transcriptomes of millions of cells in one sample and measures the population mean. It is cheap, deep, and quantitative — and blind to cell-type composition.
2. **For homogeneous samples** (cell lines, sorted populations), bulk is fine.
3. **For heterogeneous tissue** (tumor, brain, immune system, development), bulk's mean is a fiction — no individual cell expresses the bulk profile.
4. **scRNA-seq** restores cell-level resolution at a cost: each cell is sampled shallowly (10–25% of its transcripts), so technical noise is high per cell but population structure is recoverable across thousands of cells.
5. **For somatic mutation work** specifically: bulk RNA-seq cannot tell you *which cell type* carries a mutational signature in its expression program. Methods like [[30-Concepts/got|GoT]] need scRNA-seq as their substrate.

## Related

- [[10-Summaries/tang-2009-scrna-seq]] · [[10-Summaries/macosko-2015-drop-seq]] · [[10-Summaries/svensson-2017-power-analysis]]
- [[30-Concepts/drop-seq]] · [[30-Concepts/umi-molecular-barcoding]] · [[30-Concepts/combinatorial-indexing]]
- [[30-Concepts/pseudo-bulk]] — aggregation of scRNA-seq back to a bulk-like profile, used for differential expression at cell-type resolution
- [[40-Topics/single-cell-multiomics]]
- [[40-Topics/single-cell-multiomics]]
- [[30-Concepts/got]] — scRNA-seq + targeted DNA genotyping
- [[30-Concepts/cite-seq]] — scRNA-seq + surface protein
- [[30-Concepts/dogma-seq]] · [[30-Concepts/scnmt-seq]] · [[30-Concepts/sci-car]] — multi-modal extensions
