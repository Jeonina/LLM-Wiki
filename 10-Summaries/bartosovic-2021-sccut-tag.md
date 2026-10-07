---
type: summary
title: "Bartosovic et al. 2021 — scCUT&Tag: single-cell CUT&Tag for histone modifications + TFs in tissue"
source: "[[00-Sources/papers/Single-cell CUT&Tag profiles histone modifications and transcription factors in complex tissues]]"
source_quality: full
source_sha256: "47eb90942afa4be200fc5fb39b61a86f29fc8d397911e70a63368e4a4cea2032"
source_kind: paper
author: "Marek Bartosovic, Mukund Kabbe, Gonçalo Castelo-Branco (corresponding)"
published: 2021-04-12
ingested: 2026-05-18
updated: 2026-10-07
doi: "10.1038/s41587-021-00869-9"
journal: "Nature Biotechnology"
tags: [scCUT&Tag, histone-modifications, transcription-factors, droplet, CUT&Tag, OLIG2, RAD21, Castelo-Branco-lab, oligodendrocyte-lineage, H3K4me3-breadth, ABC-model, HiChIP, 10x-scATAC]
entities: []
concepts:
  - "[[30-Concepts/cut-and-tag]]"
  - "[[30-Concepts/tn5-tagmentation]]"
  - "[[30-Concepts/transcription-factor-motif]]"
  - "[[30-Concepts/latent-semantic-indexing]]"
  - "[[30-Concepts/multimodal-integration-methods]]"
  - "[[30-Concepts/chromatin-loop]]"
  - "[[30-Concepts/gene-regulatory-network]]"
  - "[[30-Concepts/trajectory-inference]]"
topics:
  - "[[40-Topics/histone-modifications]]"
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Bartosovic et al. (2021) — *Single-cell CUT&Tag profiles histone modifications and transcription factors in complex tissues* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-021-00869-9) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33846645/)

# Bartosovic et al. 2021 — single-cell CUT&Tag

> scCUT&Tag runs antibody-directed pA–Tn5 tagmentation on bulk nuclei, then feeds the tagmented nuclei into the standard **10x Genomics Chromium scATAC-seq kit**, skipping the kit's own transposition step. The only real chemistry change is adding **1% BSA** to the buffers so nuclei do not clump. Applied to FACS-sorted cells from the juvenile mouse brain (Sox10:Cre/RCE reporter, P15 and P21–P25), it gives **47,340 single-cell profiles** across four histone marks, with a median of 98 (H3K36me3) to 453 (H3K27ac) unique fragments per cell. That is enough to call all major CNS cell types from a single mark, including the repressive H3K27me3. The authors then use the data for biology that needs cell-type-resolved chromatin: global mark levels per cell type, H3K4me3/H3K27me3 interplay at cell-type-specific promoters, H3K4me3 breadth increasing along OPC → MOL differentiation, single-cell OLIG2 and RAD21 binding, and enhancer–promoter loops predicted with the ABC model and checked against new oligodendrocyte H3K27ac HiChIP. The cost is sparsity: it resolves major cell types but not subtypes without help from scRNA-seq.

## Key claims

- **Protocol.** Bulk CUT&Tag (primary antibody overnight, guinea pig anti-rabbit secondary, pA–Tn5 at 300 mM NaCl, tagmentation 1 h at 37 °C) on 150,000 sorted cells, then the 10x scATAC-seq v1 or v1.1 kit from step 2 ("Generation & barcoding"), with 16–20 final PCR cycles. BSA cut nuclear clumping without visibly changing bulk tagmentation efficiency or signal distribution. An optional qPCR cycle check against IgG CUT&Tag flags failed experiments before loading the chip.
- **Cell-line proof of concept.** On a mix of mESC, NIH-3T3 and Oli-neu cells, H3K27me3 scCUT&Tag in two technical replicates (v1 and v1.1 kits) gave 4,872 and 3,873 cells with 597 and 568 unique fragments per cell. LSI + UMAP + Leiden clustering on 5-kb bins separated 3T3 cells and two subclusters each of Oli-neu and mESC. Pseudobulk tracks matched ENCODE ChIP-seq and CUT&Run, and merging about 200–500 3T3 cells or 20–50 mESCs gave profiles comparable to the bulk references.
- **Brain dataset and QC.** H3K4me3 and H3K27me3 were profiled in GFP+ and GFP− cells at P15 and GFP+ cells at P25, and H3K27ac and H3K36me3 in P25 GFP+ cells only. Between 39.4% and 85.6% of fragments fell in narrow peaks, and fragment lengths showed sub-, mono-, di- and tri-nucleosome sizes for all marks. Cells were called manually from reads per barcode and fraction of reads in peaks, not by Cell Ranger.
- **Against earlier single-cell H3K27me3 methods.** Compared with iCell8 scCUT&Tag (Kaya-Okur 2019) and droplet scChIP-seq (Grosselin 2019), scCUT&Tag had similar or higher specificity (fraction of fragments in peaks), equal or fewer unique fragments per cell, and more cells per experiment. Fingerprint plots showed better signal-to-noise than scChIP-seq and specificity similar to iCell8 scCUT&Tag.
- **Cell identity from one mark.** Bins of 5 kb (H3K4me3, H3K27ac, H3K27me3) or 50 kb (H3K36me3) recovered MOL, astrocytes, olfactory ensheathing cells, vascular cells and OPC/COP/NFOL in the GFP+ fraction, and excitatory and inhibitory neurons, astrocytes and microglia in the GFP− fraction. H3K27me3 clusters were annotated by the *absence* of the repressive mark near marker genes. Clusters reproduced across biological replicates, cell-type proportions matched scRNA-seq of the same sorted cells, and an unexpected large astrocyte population appeared in the GFP+ fraction.
- **Integration with scRNA-seq.** H3K4me3 co-embedded with the Zeisel adolescent brain atlas by CCA. Metagene scores from 100 marker genes per type were enriched in active-mark clusters and depleted in H3K27me3. Co-embedding with an oligodendrocyte scRNA-seq dataset split the apparently uniform MOL cluster into subpopulations enriched for MOL1, MOL2 and MOL5 module genes. That subtype structure was **not** visible from scCUT&Tag alone.
- **Global mark levels differ by cell type.** Using unique reads per cell as a proxy for total modification, H3K27me3 was higher in oligodendrocytes, microglia and a subset of neurons, and H3K36me3 was higher in OPC/COP–NFOL. The authors argue this is not a permeability or tagmentation artefact because no cell type was enriched across all marks.
- **H3K4me3/H3K27me3 interplay.** At cell-type-specific H3K4me3 promoters, H3K27me3 was depleted where H3K4me3 was present. OPC-specific genes lost H3K27me3 in MOLs but not in astrocytes, which the authors read as H3K27me3 not being needed to silence OPC genes during MOL differentiation. Astrocyte genes kept H3K27me3 in OPCs and MOLs but had higher H3K4me3 in OPCs than in MOLs, suggesting astrocytes and OPCs are epigenetically related.
- **H3K4me3 breadth tracks differentiation.** Marker-gene promoters had broader H3K4me3 on average. Breadth was largest in astrocytes and oligodendrocytes and smallest in VLMCs and OPCs. Ordering OPC and MOL cells by MOL-signature signal, cross-checked with slingshot pseudotime, showed H3K4me3 breadth at MOL promoters increasing gradually cell by cell.
- **Transcription factors.** OLIG2 and RAD21 scCUT&Tag in P25 GFP+ cells gave median 48 and 240 unique reads per cell. OLIG2 split into an OLG cluster and a depth-defined "low binder" cluster. RAD21 separated astrocytes, OLG and OEC. Clusters were annotated through binding at H3K4me3-defined promoters and by CCA co-embedding with H3K27ac. MEME found CTCF as the top RAD21 motif, and a CAGMTG E-box plus a SOX-like motif (ACARWR) for OLIG2.
- **Enhancer–promoter loops.** The ABC model, run on oligodendrocyte H3K27ac scCUT&Tag, P50 cortex scATAC-seq and neural-progenitor Hi-C, predicted ~200,000 loops in OLG. Predictions agreed with ABC on bulk OLG CUT&Run and were robust down to 100 cells (74.4% overlap with the full dataset). Pileups on new primary-OPC H3K27ac HiChIP, against mESC HiChIP, showed the loops were oligodendrocyte-specific. Filtering by OLG H3K4me3 at the promoter left 61,000 loops, and also requiring RAD21 at both anchors left ~5,000 loops with stronger HiChIP signal. Cicero on scCUT&Tag gave 14,322 co-accessible pairs (score >0.2) in MOLs, with modest overlap and different loop lengths from ABC, but both recovered known *Sox10* enhancers.

## Methods / evidence

Mice: Sox10:Cre × RCE:loxP (EGFP), both sexes. FACS on DAPI−/GFP± cells after Miltenyi neural tissue dissociation and myelin debris removal. In-house pA–Tn5 (6×His–TEV–3×Flag–pA–Tn5, from Addgene #124601 and #79107) loaded with Tn5ME-A/B adapters. Processing: Cell Ranger-ATAC v1.2.0, MACS peaks, Seurat/Signac (LSI, UMAP, SNN, Leiden), slingshot, MEME vs JASPAR, deepTools, coolpuppy and cooler for HiChIP pileups, HiC-Pro and Juicebox for HiChIP, Snakemake. Supporting data generated in-house: Oli-neu and OPC H3K27me3 CUT&Run, OPC H3K27ac CUT&Tag, scRNA-seq of GFP+ cells (~7,000 cells, two replicates) and H3K27ac HiChIP from cultured OPCs (three replicates). Marker regions: Wilcoxon rank-sum (Seurat FindAllMarkers). Data: GEO GSE163532. Code: github.com/Castelo-Branco-lab/scCut-Tag_2020. Protocol: protocols.io (doi 10.17504/protocols.io.bqbnmsme).

Weight: a strong methods-plus-resource paper for one tissue (juvenile mouse brain, oligodendrocyte-focused) with good orthogonal validation: bulk ChIP-seq/CUT&Run concordance, matched scRNA-seq proportions, and a new HiChIP dataset to test loop predictions. The comparison with earlier single-cell methods is descriptive (violin and fingerprint plots on public data), not a matched-depth benchmark. Several biological readings (global mark levels, breadth, OPC–astrocyte relationship) are correlational and depend on fragment counts as a proxy for modification abundance. Small internal inconsistencies: Methods give an ABC score cutoff of >0.2 but Statistics give >0.02; the text cites Extended Data Fig. 2 for the GFP+ astrocyte population that is shown in Extended Data Fig. 5; and the Animals section lists P4–P6 and P21–25 sacrifice ages although the main experiments use P15. (synthesis)

## Limitations

**Authors' own:**
- Fragment counts per cell are low, so scCUT&Tag separates major cell types but does not find subpopulations unsupervised. Oligodendrocyte heterogeneity at the H3K4me3 level appeared only after integration with scRNA-seq.
- TF scCUT&Tag is sparser than histone scCUT&Tag. RAD21 could not separate vascular cells or OPCs, the smallest populations, and manual annotation from TF data is hard, so TF clusters were annotated through histone-mark data.
- Differences in global signal per cell type could in principle reflect permeability or tagmentation efficiency; the authors argue against this but do not rule it out experimentally.
- Causal links between modifications and expression need same-cell multiomics (scCUT&Tag plus RNA), which this method does not provide.

**Reviewer notes:**
- Each mark comes from different cells, so "interplay" analyses (H3K4me3 vs H3K27me3, bivalency) are cluster-level pseudobulk comparisons, not same-cell co-occupancy. (synthesis)
- The OLIG2 "low binder" cluster is defined partly by sequencing depth, so its biological meaning (non-OLG cells) rests on co-embedding with H3K27ac rather than on OLIG2 signal itself. (synthesis)
- ABC loop validation uses HiChIP from cultured OPCs (mixed OPC and differentiated cells) and Hi-C from neural progenitors, so cell-type matching to in vivo MOLs is approximate. (synthesis)

## Surprising or load-bearing bits

- **The method is a protocol hack on commercial hardware.** No new barcoding chemistry: bulk CUT&Tag plus 1% BSA, then the 10x scATAC kit with the transposition step skipped. That explains why it spread quickly as the droplet default for single-cell CUT&Tag. (synthesis)
- **A repressive mark identifies cell types.** H3K27me3 clusters are annotated by where the mark is *absent*, which is the same logic later developed as a silencing score in [[wu-2021-sccut-tag]].
- **Fragment count as biology.** Treating unique reads per cell as total modification abundance (H3K27me3 high in oligodendrocytes and microglia) is a reusable but risky idea, since it confounds biology with per-cell capture. (synthesis)
- **100 cells suffice for ABC predictions** (74.4% overlap with the full set), and RAD21 at both anchors is the filter that most sharpens HiChIP support.
- **OPCs and astrocytes look epigenetically close** at H3K4me3, consistent with PRC2/EED loss pushing OPCs toward astrocyte fate.

## Entities mentioned

- Castelo-Branco lab (Karolinska Institutet) — developers; no entity page yet.
- 10x Genomics Chromium scATAC-seq kit — barcoding platform reused as is.

## Concepts touched

- [[cut-and-tag]] — the bulk chemistry scaled to droplets in tissue.
- [[tn5-tagmentation]] — pA–Tn5 tagmentation done before droplet encapsulation, replacing the kit's own Tn5 step.
- [[latent-semantic-indexing]] / [[dimensionality-reduction]] / [[clustering-algorithms]] — LSI + UMAP + Leiden on 5-kb or 50-kb bins.
- [[multimodal-integration-methods]] — CCA co-embedding of scCUT&Tag with scRNA-seq and across marks and TFs.
- [[transcription-factor-motif]] / [[de-novo-motif-discovery]] — MEME on OLIG2 and RAD21 pseudobulk peaks (CTCF, CAGMTG, SOX-like).
- [[chromatin-loop]] / [[gene-regulatory-network]] — ABC and Cicero loop predictions from scCUT&Tag, filtered by H3K4me3 and RAD21.
- [[trajectory-inference]] — slingshot pseudotime ordering for H3K4me3 breadth along OPC → MOL.

## Connections to other sources

- Bulk chemistry: [[kaya-okur-2019-cut-and-tag]] (also the iCell8 scCUT&Tag comparator); CUT&Run references from [[skene-2017-cut-and-run]].
- Earlier droplet ChIP lineage compared against: [[rotem-2015-drop-chip]]; other 2019 single-cell histone methods cited: [[ku-2019-scchic-seq]], [[wang-2019-cobatch]].
- Parallel same-year droplet/nanowell scCUT&Tag focused on H3K27me3: [[wu-2021-sccut-tag]].
- Analysis stack: [[stuart-2021-natmethods]] (Signac), [[butler-2018-seurat-cca]] (CCA integration), [[pliner-2018-cicero]] (co-accessibility loops); platform ancestry in [[buenrostro-2015-nature]].
- Successors: [[bartosovic-2022-nano-cut-tag]] (same lab, multi-mark + ATAC per cell, addressing the one-mark-per-cell limit), [[janssens-2023-scicut-tag]], [[zhang-2022-sccut-tag-pro]], [[gopalan-2022-multi-cut-and-tag]], [[li-2024-scnanoseq-cut-tag]].
- Later evaluations: [[schwager-2026-onecell-cut-tag]] benchmarks against 10x droplet scCUT&Tag; [[raimundo-2023-schptm-benchmark]] and [[wu-2026-sccut-tag-review]] treat it as a reference dataset and assay; [[abbasova-2025-cut-tag-encode-benchmark]] gives the bulk CUT&Tag limits it inherits.
- MNase vs Tn5 chemistry comparison: [[50-Notes/mnase-vs-tn5-chromatin]].

## Open questions

- How much of the per-cell-type difference in fragment counts is modification abundance versus accessibility or tagmentation bias? A spike-in or same-cell normalisation would answer this. (synthesis)
- Does H3K4me3 broadening along OPC → MOL hold with same-cell RNA, or is it partly an artefact of more fragments in differentiated cells? (synthesis)
- Which ABC cutoff (0.2 or 0.02) produced the ~200,000 loops?

## Related

- [[30-Concepts/cut-and-tag]] · [[40-Topics/histone-modifications]] · [[30-Concepts/transcription-factor-motif]] · [[40-Topics/chromatin-architecture]]
- [[10-Summaries/bartosovic-2022-nano-cut-tag]] · [[10-Summaries/janssens-2023-scicut-tag]] · [[10-Summaries/ku-2019-scchic-seq]] · [[10-Summaries/yeung-2023-scchix-seq]] · [[10-Summaries/wu-2021-sccut-tag]]
