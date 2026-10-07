---
type: summary
title: "Schwager et al. 2026 — Simultaneous single-cell profiling of chromatin, transcriptome and surface markers with OneCell CUT&Tag captures epigenomic reprogramming"
source: "[[00-Sources/papers/Simultaneous single-cell profiling of chromatin, transcriptome and surface markers with OneCell CUT&Tag captures epigenomic reprogramming]]"
source_kind: paper
author: "Anna Schwager, Eve Moutaux, Adeline Durand, Alexandra Van Keymeulen, Amélie Viaene, ... Déborah Bourc'his, Elisabetta Marangoni, Nicolas Servant, Cédric Blanpain, Leïla Perié, Céline Vallot (corresponding; 26 authors)"
published: 2026-08-12
ingested: 2026-10-07
doi: "10.1038/s41587-026-03259-1"
journal: "Nature Biotechnology (online 2026-08-12)"
tags: [OneCell-CUT&Tag, CUT&Tag, FLASH-seq, plate-based, low-input, H3K27me3, H3K4me1, multiome, index-sorting, zygote, mammary-gland, epigenomic-priming, MOFA, transdifferentiation]
entities: []
concepts: ["[[cut-and-tag]]", "[[joint-single-cell-multi-omics]]", "[[sortchic]]", "[[tn5-tagmentation]]", "[[pseudo-bulk]]", "[[trajectory-inference]]", "[[multimodal-integration-methods]]", "[[epigenetic-memory]]", "[[enhancer-states]]", "[[quality-control-metrics]]"]
topics: ["[[histone-modifications]]", "[[single-cell-multiomics]]"]
---

**Citation:** Schwager et al. (2026) — *Simultaneous single-cell profiling of chromatin, transcriptome and surface markers with OneCell CUT&Tag captures epigenomic reprogramming* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-026-03259-1)

# Schwager 2026 — OneCell CUT&Tag

> Most single-cell histone methods do the antibody step **in bulk before isolating cells**, so they need ≥10⁴–10⁵ input cells. OneCell CUT&Tag reverses the order: cells are **sorted or hand-pipetted one per well into 384-well plates first**, nuclei are held on carboxylic beads, and every CUT&Tag step through library PCR runs **inside that single well**. A fraction of the cytoplasm is moved to a mirror plate for full-length FLASH-seq RNA, and index-sort data supply surface markers. The result is matched histone mark + full transcriptome + surface phenotype for each cell, from inputs as low as one cell, at a depth (~26,000 unique fragments/cell on a cell line) where single-cell tracks can be read directly **without metacell or pseudobulk aggregation**. Applied to zygotes and mouse mammary gland, it finds basal cells with luminal-like epigenomes and an epigenome that changes **gradually** during basal→luminal transdifferentiation while the transcriptome **switches abruptly**.

## Key claims

- **Input and throughput**: from 1 cell up to ~10³ cells across multiple 384-well plates in 1.5 days; automation (VIAFLO 384 + I.DOT nanodispenser) raised throughput from one plate (384 cells) to four plates (1,536 cells) in 1.5 days and gave a 1.5× increase in single-cell coverage for H3K4me1.
- **Benchmark (MDA-MB-468, H3K27me3, depth equalized to 38,716 reads/cell)**: OneCell 26,008 median unique reads/cell, median FrIP 0.77; sortChIC 20,581 and 0.79; scChIP-seq 5,722; 10x droplet scCUT&Tag 5,156. Cells retained by the shared filter: 43/48 (90%) OneCell, 135/154 (88%) sortChIC, 7,846/317,486 barcodes (2%) scChIP-seq, 6,928/249,947 (3%) 10x scCUT&Tag. At this depth single-cell coverage tracks can be read at 1-Mb resolution.
- **Multiome yield on the cell line**: median 8,054 genes/cell, >15,000 unique DNA fragments in 82% of cells, and 77–85% of cells passing QC in both modalities depending on threshold.
- **Purity**: a species-mixing test on a patient-derived xenograft (n = 1,369 cells) detected no cross-species contamination across wells.
- **Tissue range**: fresh and frozen mouse and human tissue. Zygotes gave the highest metrics (15,590 median H3K27me3 fragments, 97,849 median H3K4me1 fragments, 13,712 genes); fresh mouse mammary gland 7,556 H3K27me3 fragments and 2,404 genes; a frozen human TNBC tumour 8,706 H3K4me1 fragments (nuclei, chromatin only).
- **Library concentration predicts sequencing success**: amplified DNA/cDNA concentration correlates with unique fragments/genes per cell, so it can serve as a cheap pre-sequencing QC.
- **Zygote**: 10 H3K27me3 and 14 H3K4me1 single-zygote profiles, each paired with a transcriptome, described by the authors as, to their knowledge, the first matched transcriptome + repressive/permissive epigenome from the same zygote. H3K4me1 is spread genome-wide without enhancer/promoter enrichment and does not correlate with expression. H3K27me3 forms multi-Mb domains and is negatively associated with expression. H3K27me3-marked genes are developmental, while unmarked genes are housekeeping.
- **Mammary gland (978 high-quality cells, 5 mice)**: cytometry and RNA annotations agree for 98% of cells. However, on average 9% of basal cells (by cytometry and RNA) fall in the ER⁻ luminal cluster in **both** H3K4me1 and H3K27me3 embeddings. This was reproducible in all five mice and not explained by sorting doublets. ER⁺ and ER⁻ luminal cells form a continuum epigenomically but are discrete transcriptomically.
- **MOFA (15 factors; 2 technical factors dropped)**: factor 7 is a multiomic basal factor (*Acta2*, *Krt14* expression; Trp63/Trp73 motifs in H3K4me1). Factor 2 is **epigenome-only**: an H3K4me1 profile in a basal subset, invisible at RNA level, enriched for Zfx (stemness), Trp63 (basal) and Tcfap2c (luminal) motifs. The authors read this as epigenomic priming.
- **Transplantation (10,000 YFP⁺ basal cells into cleared fat pads; 194 engrafted cells at day 4.5, 46 profiled jointly for H3K4me1 + RNA)**: 52% remained basal, 26% became ER⁻ and 13% ER⁺ luminal cells. H3K4me1 pseudotime is continuous while the RNA pseudotime is a binary switch. Transitioning cells are more proliferative, downregulate Tnf and p53 signalling, and upregulate *Axl* relative to ER⁻ luminal cells.

## Methods / evidence

Plate-based CUT&Tag with H3K27me3 or H3K4me1 antibodies and pA-Tn5 or in-house Nano-Tn5 (from the Bartosovic/Castelo-Branco plasmid). Protocol settings were 1% NP-40 and 27 PCR cycles. The transcriptome comes from adapted FLASH-seq on 1 µl of cytoplasmic supernatant. Preprocessing used a unified Nextflow scEpigenome pipeline (Bowtie2 barcode demux, STAR alignment, MAPQ ≥ 20, blacklist, optional MACS2) designed to accept data from any single-cell epigenomic technology. Downstream analysis used Seurat/Signac objects keyed by plate+well barcodes. It also used SnapATAC2 cosine spectral embedding on 5-kb bins, a ChromSCape-style correlation filter (which removed 108 cells), Harmony and Leiden, MOFA, destiny diffusion maps/DPT, and Wilcoxon DE + GSEA. References were bulk CUT&RUN on 50 pooled zygotes and published TACIT H3K4me1 zygote data.

Weight: the benchmark is unusually fair, with the same cell line, mark, pipeline and filtering, and depth equalized by subsampling OneCell to 46% of reads. However, OneCell contributes only 43 cells to it, so the comparison is per-cell quality, not throughput. The biology rests on modest numbers (24 zygotes; 46 day-4.5 cells). The authors state the priming result is not causal.

## Surprising or load-bearing bits

- **The input bottleneck is about the order of steps, not chemistry.** Methods that do bulk antibody targeting before single-cell isolation (droplet, combinatorial indexing, sortChIC, T-ChIC) inherit ≥10⁴-cell input floors. Moving isolation to the first step removes the floor at the cost of throughput (~10³ cells). (synthesis)
- **Per-cell depth vs cell number is the real trade-off.** Droplet methods retained thousands of cells at ~5,000 reads each, while OneCell and sortChIC retained tens to hundreds at ~20,000–26,000 reads. The paper argues the latter is what makes **cell-level cross-modality comparison** possible without metacells. (synthesis on top of reported numbers)
- **Epigenome and transcriptome can disagree about cell identity, reproducibly.** The 9% of basal cells with luminal-like chromatin is the type of finding that metacell or pseudobulk integration would average away. This is a concrete argument for truly joint single-cell assays over computational pairing. (synthesis)
- **Gradual chromatin, abrupt RNA during fate conversion** reverses the intuition that chromatin opening is a fast first step. In this system H3K4me1 remodelling runs as a continuum across transitioning cells while the transcriptome flips. (synthesis; the authors describe the two as "not in complete synchrony")
- Zygotic H3K4me1 lacks the enhancer/promoter focus of differentiated cells, so H3K4me1 should not be used as an enhancer proxy at that stage.

## Concepts touched

- [[cut-and-tag]] — a plate-based, single-cell-from-start variant. CUT&Tag chemistry is unchanged; the novelty is the workflow order and bead handling.
- [[joint-single-cell-multi-omics]] — histone mark + full-length RNA + index-sorted surface markers, matched by well coordinates.
- [[sortchic]] — the closest performer in the benchmark (similar depth and FrIP, but ≥10⁴ cell input).
- [[pseudo-bulk]] — explicitly positioned as unnecessary at OneCell depth.
- [[trajectory-inference]] — separate H3K4me1 and RNA diffusion pseudotimes show asynchronous remodelling.
- [[multimodal-integration-methods]] — MOFA used to separate modality-specific from shared factors.
- [[epigenetic-memory]] / [[enhancer-states]] — "epigenomic priming" of basal cells as a ready state for luminal programs (speculative, per authors).

## Connections to other sources

- Benchmarked against 10x droplet scCUT&Tag ([[bartosovic-2021-sccut-tag]]) and sortChIC ([[30-Concepts/sortchic]]); Nano-Tn5 reagent from [[bartosovic-2022-nano-cut-tag]].
- CUT&Tag lineage: [[kaya-okur-2019-cut-and-tag]], [[wu-2021-sccut-tag]], [[janssens-2023-scicut-tag]], [[zhang-2022-sccut-tag-pro]] (surface protein + chromatin via antibody tags, a different route to phenotype pairing than index sorting).
- High-throughput, input-hungry combinatorial predecessor: [[wang-2019-cobatch]]. CoBATCH's own limitations section proposed sort-first plate variants, which is essentially the route OneCell takes. (synthesis)
- Integration and analysis tools: [[argelaguet-2020-mofa-plus]], [[zhang-2024-snapatac2]], [[korsunsky-2019-harmony]], [[stuart-2021-natmethods]] (Signac).
- Related histone-modification single-cell methods: [[ku-2019-scchic-seq]], [[yeung-2023-scchix-seq]], [[rotem-2015-drop-chip]].

## Open questions

- Does epigenomic priming in basal cells predict which cells transdifferentiate? The paper shows co-occurrence only and calls for perturbation studies.
- Can the plate format scale beyond ~10³ cells per run without losing the per-cell depth that justifies it?
- How do the frozen-tissue, chromatin-only profiles (no RNA) compare in identity calls with fresh multiome profiles from the same tissue?
- The epigenome/RNA discordance is shown for H3K4me1 and H3K27me3. Would an active promoter mark (H3K4me3/H3K27ac) track RNA more tightly?

## Related

- [[40-Topics/histone-modifications]] · [[40-Topics/single-cell-multiomics]] · [[cut-and-tag]] · [[wang-2019-cobatch]]
