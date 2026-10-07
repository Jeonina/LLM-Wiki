---
type: summary
title: "Wang et al. 2019 — CoBATCH for High-Throughput Single-Cell Epigenomic Profiling"
source: "[[00-Sources/papers/CoBATCH for High-Throughput Single-Cell Epigenomic Profiling]]"
source_quality: full
source_sha256: "2835696ee4d3e67ac13d368daac6263d22cebd313b2f8a5cb768f6ba53681108"
source_kind: paper
author: "Qianhao Wang, Haiqing Xiong, Shanshan Ai, Xianhong Yu, Yaxi Liu, Jiejie Zhang, Aibin He (corresponding)"
published: 2019-10
ingested: 2026-10-07
doi: "10.1016/j.molcel.2019.07.015"
journal: "Molecular Cell 76(1):206-216.e7"
tags: [CoBATCH, in-situ-ChIP, pA-Tn5, combinatorial-indexing, histone-modifications, H3K27ac, H3K36me3, Pol-II, endothelial-cells, low-input, single-cell-ChIP]
entities: []
concepts: ["[[cut-and-tag]]", "[[tn5-tagmentation]]", "[[combinatorial-indexing]]", "[[chip-seq]]", "[[cut-and-run]]", "[[scchic-seq]]", "[[enhancer-states]]", "[[cistopic]]", "[[latent-dirichlet-allocation]]", "[[cis-regulatory-element]]"]
topics: ["[[histone-modifications]]", "[[single-cell-multiomics]]"]
---

**Citation:** Wang et al. (2019) — *CoBATCH for High-Throughput Single-Cell Epigenomic Profiling* — *Molecular Cell* 76:206-216.e7. [DOI](https://doi.org/10.1016/j.molcel.2019.07.015)

# Wang 2019 — CoBATCH

> Fuse **protein A to the N-terminus of Tn5 (PA-Tn5, "PAT")**, let an antibody tether it to a histone mark or chromatin-binding protein in permeabilized cells, and activate tagmentation: the released fragments already carry adapters, so library prep is one-tube PCR with no DNA extraction, end repair or ligation. Run in bulk on ≥100 cells this is "*in situ* ChIP"; add **two rounds of combinatorial barcoding** (barcoded PAT-T5/T7 transposomes per well of a first 96-well plate, then i5/i7 PCR indices on 20–25 cells per well of a second plate) and it becomes **CoBATCH** — combinatorial barcoding and targeted chromatin release — at ~2,400 cells per 96-well plate and ~12,000 unique non-duplicated reads per cell. The showcase is H3K27ac in ~3,000 Cdh5-traced endothelial cells from ten E16.5 mouse organs, which cluster by enhancer module and function rather than by organ.

## Key claims

- **Low-input *in situ* ChIP works from 100 cells** for H3K27ac, H3K27me3 and H3K4me3 in mouse ESCs, judged against ENCODE peaks and TSS heatmaps; at ~5M unique non-duplicated reads, peak sets are reproducible across cell-number groups and with public data.
- **It covers repressive as well as active marks**: H3K27me3 enrichment shows the approach is not restricted to open-chromatin regions that overlap ATAC-seq signal.
- **Works on intact single embryos**: H3K4me3 and H3K27ac from single gastrulating embryos at E6.5 (~660 cells), E7.0 (~4,500 cells) and E7.75 (~15,000 cells), reproducible across replicates, with stage-appropriate GO terms for H3K27ac peaks ("gastrulation" at E6.5, "mesoderm development" at E7.0).
- **Non-histone targets too**: P300, CBP and EZH2 from 100 ESCs resemble bulk ChIP-seq (P300/CBP with higher signal-to-noise), and NKX2-5 from a single E9.25 heart gave better signal-to-noise than bulk ChIP-seq that pooled ten hearts.
- **Barcode collisions ~7%** in a 1:1 mouse ESC / human HEK293T species-mixing test (collision = <80% of reads to one species).
- **Native and fixed protocols agree**: H3K27ac CoBATCH retained 2,161 (native) and 2,388 (fixed) ESCs at a 3,000-read cutoff, with Spearman 0.90 between conditions; mean unique reads were ~12,000/cell (native) and 9,247/cell (fixed), and aggregates resemble bulk ESC ChIP-seq.
- **Versus scChIC-seq**: CoBATCH reports markedly more non-duplicated reads per cell, higher mapping rate and less read redundancy, but slightly higher FRiP for scChIC-seq. The comparison (Table S3) is H3K27ac in 2,161 ESCs vs scChIC-seq H3K4me3 in 281 human white blood cells, and FRiP was computed differently in the two studies.
- **Endothelial heterogeneity is functional, not organ-of-origin**: 3,057 H3K27ac ECs passed filtering (74 small intestine to 480 limb muscle); LSI on 20,112 peaks for 2,758 cells gave three major clades from four enhancer modules — C1 immune/lymphocyte activation (FOS-JUN, IRF4 motifs), C2 coronary vasculature/EndMT/brain development (enriched for kidney and heart ECs), C3a enriched for brain and kidney ECs. The authors conclude ECs do not cluster by organ.
- **Pol II and H3K36me3 CoBATCH on 1,240 E16.5 cardiac Cdh5-traced cells** (852 Pol II, mean 9,452 reads; 388 H3K36me3, mean 7,525 reads), analysed with cisTopic, resolved macrophage-like (*Irf8*), mesenchymal (*Col1a1*), arterial (*Ephb2*) and venous (*Ephb4*) clusters. Some H3K36me3 "venous" cells carried *Ephb2* signal, which suggests more venous heterogeneity than Pol II shows.

## Methods / evidence

In-house His-PA-Tn5 expressed in BL21(DE3), assembled with barcoded T5/T7 adaptors. Single-cell workflow: permeabilization (fixed cells: SDS/62 °C chromatin opening), ConA beads, primary antibody, then cells FACS-sorted at 2,000/well into wells pre-loaded with barcoded PAT, tagmentation at 37 °C (25 °C native), pooling, re-sorting 20–25 cells/well for indexed PCR. Analysis: Bowtie2 to mm10, MAPQ>30, Picard dedup, MACS2 `--broad`; LSI (TF-IDF + SVD) and MDS for ECs; cisTopic (15 topics) + UMAP + densityClust for Pol II/H3K36me3; GREAT for GO. Low-input quality judged by ROC/AUC against ENCODE peaks within ±2 kb of TSSs.

Weight: a solid methods paper with broad target coverage, but benchmarking is thin. The only head-to-head single-cell comparison is against scChIC-seq data from a different mark, cell type and FRiP definition, and there is no comparison with bulk-sorted reference populations for the EC biology. The authors have filed a patent.

## Surprising or load-bearing bits

- **Pre-loading barcoded transposomes is the CoBATCH trick.** The cell barcode is carried by the PA-Tn5 complex itself, so the antibody-targeting step stays in bulk and the barcoding is done during tethering. This is the same logic later used by sciCUT&Tag-style designs. (synthesis)
- **The stated limitation is input, not throughput**: CoBATCH needs at least ~10,000 starting cells and is not suited to samples of tens of cells such as preimplantation embryos. The authors sketch two plate-based variants (tagment then sort singly, or sort singly then tagment with a per-well barcode), which is essentially the design space that later low-input plate methods occupy. (synthesis)
- **Single-embryo NKX2-5 beating ten-heart bulk ChIP** is a strong demonstration of the signal-to-noise advantage of tethered tagmentation over immunoprecipitation for transcription factors.
- **Left forebrain ECs clustered with liver and lung ECs**, apart from right forebrain and hindbrain. The paper reports this as surprising and does not explain it, so it may be a batch or sampling effect. (synthesis)
- The intro of the clipping cites CUT&RUN and ChIL-seq as immunoprecipitation-free precedents and does not mention CUT&Tag. PA-Tn5 tethering here appears as a parallel development to [[kaya-okur-2019-cut-and-tag]]. (synthesis)

## Concepts touched

- [[cut-and-tag]] / [[tn5-tagmentation]] — independent PA-Tn5 tethered-tagmentation design, applied to histone marks, co-activators, PRC2 and a cardiac TF.
- [[combinatorial-indexing]] — two-round barcoding (transposome barcode × PCR index) borrowed from sci-ATAC-seq for histone marks.
- [[chip-seq]] / [[cut-and-run]] / [[scchic-seq]] — the immunoprecipitation and MNase-based predecessors it is positioned against.
- [[enhancer-states]] / [[cis-regulatory-element]] — H3K27ac as a surrogate for active enhancers, used for dynamic gastrulation enhancers and EC modules.
- [[cistopic]] / [[latent-dirichlet-allocation]] — topic modelling carried over from scATAC to Pol II and H3K36me3 single-cell data.

## Connections to other sources

- Same PA-Tn5 principle, Henikoff lab: [[kaya-okur-2019-cut-and-tag]]; later single-cell descendants [[bartosovic-2021-sccut-tag]], [[wu-2021-sccut-tag]], [[bartosovic-2022-nano-cut-tag]], [[janssens-2023-scicut-tag]] (combinatorial indexing at higher scale), [[zhang-2022-sccut-tag-pro]].
- Predecessors it benchmarks or discusses: [[ku-2019-scchic-seq]] (the head-to-head comparison), [[rotem-2015-drop-chip]] (~800 reads/cell, which CoBATCH cites as limiting).
- Combinatorial-indexing template: [[cusanovich-2015-sciatac]].
- Analysis tools used: [[bravo-2019-cistopic]], [[mclean-2010-great]].
- Later low-input plate design that explicitly cites CoBATCH-type methods as input-hungry: [[schwager-2026-onecell-cut-tag]].

## Open questions

- How does CoBATCH's ~7% collision rate scale when the second-round plate count goes up to the stated ~20,000-cell configuration (ten 96-well or three 384-well plates)?
- Is the "ECs do not cluster by organ" result robust to batch effects, given that each organ was dissected, digested and sorted separately?
- The fixed-cell protocol uses SDS and heat to open chromatin. How much does fixation bias the recovered H3K27ac landscape beyond the 0.90 correlation shown in ESCs?

## Related

- [[40-Topics/histone-modifications]] · [[cut-and-tag]] · [[combinatorial-indexing]] · [[ku-2019-scchic-seq]]
