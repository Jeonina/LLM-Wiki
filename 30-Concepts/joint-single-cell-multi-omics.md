---
type: concept
title: Joint single-cell multi-omics
aliases: [joint multi-omics, paired multi-omics, same-cell multi-modal]
tags: [single-cell, multiomics, paired-measurement]
created: 2026-05-19
updated: 2026-10-08
---

# Joint single-cell multi-omics

> Single-cell methods that measure two or more molecular modalities from the same individual cell (or nucleus) — as opposed to integrating mono-omic datasets computationally. The defining feature is *physical co-capture* of modalities within a single droplet, well, or fiber. See [[40-Topics/single-cell-multiomics]] for the methods landscape and [[10-Summaries/wang-2023-multimodal-review]] for the catalog.

## Definition

A joint multi-omic assay reads ≥2 of: DNA sequence, RNA, chromatin accessibility, DNA methylation, histone modifications, surface protein, intracellular protein, 3D contacts — within the same physical compartment. This contrasts with **integration of unpaired data** (matrix factorization, manifold alignment) which infers joint structure from separately-measured modalities ([[10-Summaries/wang-2023-multimodal-review]]).

## Why it matters

- Pairs cause and effect at single-cell resolution — e.g., does this mutation alter this cell's accessibility? Only joint measurement can answer.
- Avoids batch effects and clustering artifacts that can confound unpaired integration (synthesis).

## Variants

- **Joint genome + transcriptome** — G&T-seq ([[10-Summaries/macaulay-2015-gt-seq]]), DR-seq ([[10-Summaries/dey-2015-dr-seq]]), GoT ([[10-Summaries/nam-2019-got]]).
- **Scalable droplet DNA + RNA** — DEFND-seq (whole-genome, nucleosome depletion + 10x Multiome, [[10-Summaries/olsen-2025-defnd-seq]]) and SDR-seq (targeted, Tapestri, low allelic dropout, [[10-Summaries/lindenhofer-2025-sdr-seq]]); these trade off **genome-wide breadth (high ADO)** vs **targeted depth (low ADO, per-cell zygosity)** ([[10-Summaries/lindenhofer-2025-sdr-seq]]).
- **Joint chromatin + transcriptome** — sci-CAR ([[10-Summaries/cao-2018-sci-car]]), SHARE-seq ([[10-Summaries/ma-2020-share-seq]]).
- **Joint methylation + chromatin + RNA** — scNMT-seq ([[10-Summaries/clark-2018-scnmt-seq]]).
- **Joint mutation + chromatin + RNA** — Duplex-Multiome ([[10-Summaries/kriz-2025-duplex-multiome]]).

## Added 2026-10-07

Paired Hi-C joins chromatin conformation and transcriptome in the same nucleus by adapting Droplet Hi-C to the 10x Multiome kit, with milder SDS, 0.6% formaldehyde and a revised cDNA preparation ([[10-Summaries/chang-2025-droplet-hi-c]]). Mouse cortex gave 12,361 joint profiles at 42,210 Hi-C read pairs and a median of 3,914 UMIs per cell; the authors flag Hi-C library complexity as the main limitation ([[10-Summaries/chang-2025-droplet-hi-c]]).

OneCell CUT&Tag matches a histone mark (H3K27me3 or H3K4me1), full-length FLASH-seq transcriptome and index-sorted surface markers in the same cell by plate/well coordinates, from inputs as low as one cell ([[10-Summaries/schwager-2026-onecell-cut-tag]]). In mouse mammary gland, on average 9% of cells called basal by cytometry and RNA fell in the ER⁻ luminal cluster in both histone embeddings, reproducibly across five mice. This shows that modalities measured in the same cell can disagree on identity ([[10-Summaries/schwager-2026-onecell-cut-tag]]).

wellDA-seq jointly measures whole-genome DNA and chromatin accessibility in the same single cells at a scale of thousands of cells (22,123 cells from 11 breast tissues). This maps epigenomic phenotypes directly onto copy-number-defined subclones, and the authors find evidence for both genetic hardwiring and epigenetic plasticity ([[10-Summaries/wang-2024-wellda-seq]]).

Long-read genotype + accessibility + transcriptome profiling (SPLONGGET) targets genotype-to-phenotype questions such as splice-site immune-escape mutations that need full-length transcripts in the same cell ([[10-Summaries/pancikova-2025-splongget]]).

sciMET+ATAC obtains chromatin accessibility and genome-wide methylation from the same cells by tagmenting native nuclei, then re-tagmenting after nucleosome disruption with a different index set; 5,305 cells passed both modalities, with lower per-modality quality (TSS enrichment 5.2) than unimodal assays ([[10-Summaries/nichols-2025-scimetv3]]).

Re-analysis of public scHi-C datasets found that multi-omic scHi-C protocols, such as sn-m3C-seq and HiRES, capture as many contacts per cell, with similar cis/trans ratios, as protocols that measure contacts only (no significant difference) ([[10-Summaries/dautle-2025-schic-review]]).

An early factor-model analysis of same-cell transcriptome + methylome data (scM&T-seq, 87 mESCs) found one factor shared across RNA and methylation at promoters, enhancers and CpG islands, explaining 7% of RNA variance but 53–72% of methylation variance and tracking the naive → primed pluripotency transition ([[10-Summaries/argelaguet-2018-mofa]]).

## Added 2026-10-08 — sequence models & foundation models

- Borzoi's authors found that accessibility data improved RNA-seq predictions and proposed single-cell multiome (ATAC + RNA) data as valuable joint training data for sequence-to-function models ([[10-Summaries/linder-2025-borzoi]])
- Because truly paired RNA+ATAC data are scarce, scMomer pretrains its fusion stage on scCLIP's pseudo-paired fetal atlas (RNA and ATAC cells matched only by cell-type label) and then distils ATAC knowledge into an RNA-only path ([[10-Summaries/liu-2025-scmomer]])
- scDynOmics pretrains on 752,155 public mouse joint RNA+ATAC cells (SHARE-seq, SNARE-seq, sci-CAR, Paired-seq, ISSAAC-seq, 10x Multiome), treating promoter accessibility as analogous to unspliced pre-mRNA in an RNA-velocity view ([[10-Summaries/yu-2026-scdynomics]])

## Related

- [[40-Topics/single-cell-multiomics]] · [[40-Topics/single-cell-multiomics]] · [[30-Concepts/defnd-seq]] · [[30-Concepts/sdr-seq]] · [[30-Concepts/allele-dropout]] · [[50-Notes/regulatory-layers-overview]] · [[50-Notes/droplet-vs-single-molecule-scdna]]
