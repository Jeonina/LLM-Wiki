---
type: summary
title: "Bartosovic et al. 2022 — nano-CUT&Tag: multimodal single-cell chromatin profiling with nanobody-Tn5 fusions"
source: "[[00-Sources/papers/Multimodal chromatin profiling using nanobody-based single-cell CUT&Tag]]"
source_quality: full
source_sha256: "a545df459414ee8f6191b897d8073479b946929b4a246d8c90c1c57282fba150"
source_kind: paper
author: "Marek Bartosovic, Gonçalo Castelo-Branco (corresponding)"
published: 2022-12-19
ingested: 2026-05-18
updated: 2026-10-07
doi: "10.1038/s41587-022-01535-4"
journal: "Nature Biotechnology"
aliases: [nano-CT, nano-CUT&Tag, nanobody scCUT&Tag]
tags: [nano-CUT&Tag, nanobody-Tn5, multimodal, single-cell, H3K27ac, H3K27me3, ATAC, oligodendrocyte, chromatin-velocity, Castelo-Branco-lab, 10x-Chromium, orphan-tagmentation]
entities: []
concepts:
  - "[[30-Concepts/cut-and-tag]]"
  - "[[40-Topics/histone-modifications]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/chromatin-velocity]]"
  - "[[30-Concepts/tn5-tagmentation]]"
  - "[[30-Concepts/multimodal-integration-methods]]"
  - "[[30-Concepts/trajectory-inference]]"
  - "[[30-Concepts/latent-semantic-indexing]]"
  - "[[30-Concepts/enhancer-states]]"
topics:
  - "[[40-Topics/chromatin-architecture]]"
  - "[[40-Topics/single-cell-multiomics]]"
---

**Citation:** Bartosovic & Castelo-Branco (2022) — *Multimodal chromatin profiling using nanobody-based single-cell CUT&Tag* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-022-01535-4) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/36536074/)

# Bartosovic et al. 2022 — nano-CUT&Tag (nano-CT)

> nano-CT replaces the protein A–Tn5 plus secondary-antibody step of scCUT&Tag with **Tn5 fused to secondary nanobodies** that bind either mouse (ms-Tn5, nanobody TP1170) or rabbit (rb-Tn5, nanobody TP897) IgG. Each fusion is loaded with a differently barcoded P5 adapter, so two histone marks raised in different host species can be tagged in the same nucleus and demultiplexed by barcode. An optional first step with barcoded, unfused Tn5 adds ATAC, giving **three modalities per cell** on the 10x Chromium scATAC v1.1 platform. The second change is in library construction: a **P5-only first tagmentation, linear amplification in the droplet, then a second P7 tagmentation after barcoding**, so single ("orphan") insertions also become library molecules. This raises fragments per cell by more than tenfold over scCUT&Tag, at the cost of a lower fraction of reads in peaks (FrIP). Applied to P19 mouse brain (ATAC + H3K27ac + H3K27me3), it resolves more clusters than unimodal data, shows chromatin opening slightly before H3K27ac gain in the oligodendrocyte lineage, finds two sequential waves of H3K27me3 deposition, and runs scVelo on ATAC/H3K27ac as a "chromatin velocity".

## Key claims

- **Simpler protocol, lower input.** Because the nanobody binds the primary antibody monovalently, antibody and nano-Tn5 incubations are combined and the secondary-antibody step is dropped. Nuclei recovery was 28 to 68%. Bulk-scale profiling worked from ~25,000 cells, against 1 million or 150,000 cells for earlier Chromium scCUT&Tag protocols. One chip can be loaded from as little as 25,000 input nuclei for two marks without ATAC, though 50,000 gives a more complex library. Adding ATAC first causes more nuclei loss and clumping, so the three-modality version needs at least 200,000 cells. The Discussion summarises this as a ~5-fold reduction in input.
- **Two-step tagmentation drives the gain.** The new protocol cut bulk library PCR from 15 cycles to around 6 at similar yield, which the authors say cannot be explained by the linear pre-amplification step alone (qPCR curves compare scCUT&Tag, scCUT&Tag + linear pre-amplification and nano-CT). The nucleosome ladder typical of scCUT&Tag libraries is absent. Linear-amplification duplicates were minimal, 0.11–0.14% of total reads.
- **Unimodal H3K27me3 benchmark (P19 brain).** 6,798 cells with a median of 3,720 unique fragments, a **15.8-fold** increase over scCUT&Tag on the same platform and tissue. FrIP fell about 1.7-fold, from 69% to 39%, with the same peak-calling parameters. 13 clusters on a 5-kb bin matrix (LSI + UMAP). Raw matrices merged with the 2021 scCUT&Tag data intermixed without integration. nano-CT split astroependymal cells into four sub-clusters and VLMCs into three, and resolved the oligodendrocyte lineage from H3K27me3 alone, which scCUT&Tag managed only after scRNA-seq integration. Marker-bin capture rate was 23.1% against 6.6%. Background was higher than scCUT&Tag but below ENCODE H3K27me3 ChIP-seq (fingerprint analysis).
- **Multimodal yield.** 13,428 cells (two-modality) and 5,157 cells (three-modality), of which 11,981 (89.2%) and 4,434 (85.9%) passed QC in all modalities. Median fragments per cell were 6,123–14,496 (printed "1,4496") for H3K27ac and 1,832–6,510 for H3K27me3 in nano-CT, against 315–547 and 217–329 in scCUT&Tag. The gap held after downsampling to 30 million reads per sample (median 2,949 vs 221 for H3K27me3). FrIP was lower: 35.9–52.4% (H3K27ac) and 36.3–48.9% (H3K27me3) for nano-CT, against 51.2–62.1% and 67.9–69.9% for scCUT&Tag. Adding modalities modestly increased noise.
- **Against multi-CUT&Tag.** Median reads per cell were 9,135 (H3K27ac) and 3,201 (H3K27me3) in nano-CT, against 95 and 428 in multi-CUT&Tag.
- **Specificity checks.** H3K27me3, but not ATAC or H3K27ac, covers the *HoxA*–*HoxD* clusters, which are silent in rostral CNS. A PCA of pseudo-bulk tracks co-clusters populations by modality whether the data came from scCUT&Tag or nano-CT. H3K27ac and H3K27me3 tracks correlate within mark, not across. Yet in telencephalic astrocytes **1,093 peaks overlapped between the two marks, 4.4% of H3K27ac peaks and 11.5% of H3K27me3 peaks**, a co-occurrence seen specifically in nano-CT.
- **Cross-talk is one-directional.** ATAC runs first, and its signal matched standalone 10x scATAC regardless of local H3K27ac. H3K27ac signal was slightly affected by overlapping ATAC signal in highly accessible regions.
- **Modalities are not equally informative.** At similar fragment counts, clustering gave 15 ATAC, 28 H3K27ac and 24 H3K27me3 clusters. Major classes (neurons, oligodendrocytes, astroependymal, immune, vascular) agree across all three, but pericytes and vascular smooth muscle cells separate only in H3K27ac. The authors conclude histone marks can be more informative about identity than open chromatin, given similar data quality.
- **Integrated analysis.** WNN on all three matrices largely recapitulated the per-modality clusters. Among top LSI-loading regions, H3K27ac and ATAC overlapped most (10,601 regions), and 9,463 regions varied in all three. *Foxg1* is open and acetylated in telencephalic astrocytes but H3K27me3-marked in non-telencephalic astrocytes; *Lhx2*, *Foxb1* and *Irx2* differ similarly, which the authors read as an epigenetic record of astrocyte developmental origin.
- **Opening precedes acetylation.** Along a Slingshot pseudotime built on the WNN embedding of the oligodendrocyte lineage, the most dynamically opening loci gain H3K27ac with a slight delay, ATAC plateaus earlier, and H3K27me3 changes little at these sites. The effect is weaker when starting from loci selected for H3K27ac gain.
- **Two H3K27me3 waves.** An early wave represses genes expressed mainly in neurons. A second wave represses neuronal genes and OPC genes (*Sox5*, *Sox6*, *Ptprz1*; GO terms gliogenesis, glial cell differentiation, oligodendrocyte differentiation). The authors argue these two repressive states could not be separated with transcriptomic data.
- **ATAC/H3K27ac chromatin velocity.** ATAC and H3K27ac gene-by-cell matrices were passed to scVelo (v0.2.4, defaults) as the unspliced and spliced layers. The velocity field pointed from OPCs to mature oligodendrocytes, supported by phase plots for *Mal* and *Mog*. Velocity driver genes were mostly variable in oligodendrocyte scRNA-seq but relatively lowly expressed, with GO terms such as nervous system development and neurogenesis, which the authors call non-canonical oligodendrocyte differentiation genes. H3K27ac/H3K27me3, an anti-correlated pair, **did not** predict the correct trajectory.

## Methods / evidence

Nanobody sequences come from Pleiner et al. 2018, fused to hyperactive Tn5, expressed in *E. coli* BL21 (DE3) Star and purified by IMAC and gel filtration. Plasmids are on Addgene (#183637, #183638). Each nano-Tn5 is loaded with a pool of barcoded MeA (P5) adapters. Antibodies: mouse anti-H3K27me3 (Abcam Ab6002) and rabbit anti-H3K27ac (Abcam Ab177178), with Cell Signaling 9733T for the unimodal run. Primary antibodies and both nano-Tn5s are incubated together overnight, then tagmentation runs 1 h at 37 °C in 300 mM NaCl. ATAC, when used, is Omni-ATAC with barcoded P5-only Tn5 before antibody incubation. 16,000 nuclei were loaded per chip. After GEM barcoding and linear amplification, a MeB (P7) Tn5 tagmentation and 11–15 PCR cycles complete the library. Libraries were sequenced on NovaSeq with custom primers (36-8-48-36). Modalities were demultiplexed by barcode (1 mismatch) and processed with Cell Ranger, MACS2 broad peaks (`--keep-dup=1`), cell calling by Gaussian mixture on reads per cell and FrIP, then Seurat v4.0.5 and Signac v1.4.0 (LSI, UMAP, CCA label transfer to the Zeisel 2018 mouse brain atlas), Slingshot v2.2.0 and scVelo v0.2.4. Two biological replicates for the two-mark design; the three-modality run was done on the same biological sample as a technical replicate. Data: GEO GSE198467; code: github.com/mardzix/bcd_nano_CUTnTag.

Weight: a strong methods paper with clear, quantified gains in fragments per cell over scCUT&Tag and multi-CUT&Tag, honest reporting of the FrIP penalty, and sensible specificity checks (Hox loci, metagenes, cross-talk scatter plots). The biology rests on a single tissue at a single age, one pair of marks, and few replicates, and the velocity and two-wave results are pseudotime analyses without perturbation or orthogonal validation. (synthesis)

## Limitations

**Authors' own:**
- Orphan-tagmentation capture raises fragments per cell but lowers specificity, giving higher background and lower FrIP than scCUT&Tag.
- Adding ATAC increases nuclei loss and clumping, so the three-modality version needs ~200,000 input cells, and more modalities modestly increase assay noise.
- H3K27ac signal is slightly contaminated by ATAC signal in highly accessible regions.
- The ATAC/H3K27ac difference in timing is subtle. Chromatin modalities do not follow the unspliced/spliced RNA relationship, so scVelo's assumptions do not strictly apply, and anti-correlated pairs (H3K27ac/H3K27me3) need different models.
- Multiplexing is limited to two marks by the mouse/rabbit host-species split; going further needs nanobodies against other species or primary nanobodies.

**Reviewer notes:**
- The 1,093 H3K27ac/H3K27me3 overlapping peaks appear only in nano-CT and are not resolved as true bivalency versus cross-barcode or background tagmentation, which matters given the higher background of orphan-insertion libraries. (synthesis)
- The comparisons with scCUT&Tag use the authors' own 2021 data and pipeline; the multi-CUT&Tag comparison mixes a cell-line mixture with brain tissue, so fragment ratios are not like-for-like. (synthesis)
- The paper reports linear-amplification duplicates (0.11–0.14%) but gives no PCR-duplicate rate in the text, so library complexity per cell cannot be fully judged from the main text. (synthesis)

## Surprising or load-bearing bits

- **Most of the gain is library chemistry, not the nanobody.** Capturing single insertions by linear amplification before the second adapter is added is what breaks the two-insertion requirement of CUT&Tag; the nanobody mainly enables multiplexing and a shorter protocol. (synthesis)
- **Histone marks beat ATAC for cell identity** in this dataset at matched depth: 28 and 24 clusters against 15, with pericytes and vascular smooth muscle cells visible only in H3K27ac.
- **Velocity only works for a "precursor → product" pair.** ATAC → H3K27ac gave the right direction; the anti-correlated H3K27ac/H3K27me3 pair did not, a useful negative result for anyone applying RNA-velocity tooling to chromatin.
- **Repression has stages.** The two H3K27me3 waves (neuronal genes first, then OPC genes) are a claim about the epigenetic state that expression data alone cannot show.
- **Low-expressed velocity drivers.** Chromatin velocity picked up genes that are lowly expressed and not canonical markers, suggesting chromatin dynamics can flag regulators missed by scRNA-seq.

## Concepts touched

- [[30-Concepts/cut-and-tag]] — nanobody-Tn5 removes the secondary antibody step; P5-only tagmentation plus linear amplification captures orphan insertions.
- [[30-Concepts/tn5-tagmentation]] — two distinct barcoded nano-Tn5s plus barcoded unfused Tn5 in one nucleus; two-step P5/P7 tagmentation.
- [[30-Concepts/chromatin-accessibility]] — ATAC as an optional first modality, unaffected by subsequent CUT&Tag steps.
- [[40-Topics/histone-modifications]] — joint H3K27ac/H3K27me3 per cell; two waves of H3K27me3 in oligodendrocyte differentiation.
- [[30-Concepts/chromatin-velocity]] — ATAC/H3K27ac as unspliced/spliced layers in scVelo; H3K27ac/H3K27me3 fails.
- [[30-Concepts/multimodal-integration-methods]] — WNN across three chromatin modalities; CCA label transfer from scRNA-seq.
- [[30-Concepts/trajectory-inference]] — Slingshot pseudotime on the WNN embedding.
- [[30-Concepts/latent-semantic-indexing]] — LSI for each modality; overlapping LSI-loading regions across modalities.
- [[30-Concepts/enhancer-states]] — opening precedes H3K27ac at activating loci.

## Connections to other sources

- Direct predecessor: [[10-Summaries/bartosovic-2021-sccut-tag]] — same lab, platform and tissue; the 15.8-fold fragment gain and the clustering comparisons are measured against it.
- Bulk ancestor: [[10-Summaries/kaya-okur-2019-cut-and-tag]].
- Multimodal comparator: [[10-Summaries/gopalan-2022-multi-cut-and-tag]] — nano-CT reports roughly 10–100× more reads per cell.
- Other CUT&Tag-family single-cell methods: [[10-Summaries/wu-2021-sccut-tag]], [[10-Summaries/zhang-2022-sccut-tag-pro]] (whose integration suggested H3K27me3 states are more heterogeneous than expression shows; nano-CT measures this directly), [[10-Summaries/janssens-2023-scicut-tag]].
- Chromatin-velocity lineage: builds on chromatin potential from [[10-Summaries/ma-2020-share-seq]]; contrasts with the two-mark deconvolution approach of [[10-Summaries/yeung-2023-scchix-seq]].
- Integration tools used: [[10-Summaries/hao-2021-seurat-wnn]] (WNN), [[10-Summaries/stuart-2021-natmethods]] (Signac), [[10-Summaries/butler-2018-seurat-cca]] (CCA).
- Downstream use: [[10-Summaries/hu-2026-patty]] corrects nano-CT data; [[10-Summaries/schwager-2026-onecell-cut-tag]] uses the Nano-Tn5 reagent; [[10-Summaries/raimundo-2023-schptm-benchmark]] cites it as a route to higher coverage; [[10-Summaries/wu-2026-sccut-tag-review]] catalogues it.
- Bivalency context for the H3K27ac/H3K27me3 overlap: [[10-Summaries/bernstein-2006-bivalent-chromatin]]; enhancer mark context: [[10-Summaries/creyghton-2010-h3k27ac-enhancers]]. (synthesis)
- Other multimodal epigenome assays in the wiki: [[10-Summaries/geisenberger-2025-scepi2-seq]] (methylation + histone mark).

## Open questions

- Are the 4.4%/11.5% H3K27ac–H3K27me3 overlapping peaks real bivalent loci or background tagmentation? (synthesis)
- Would a velocity model built for chromatin (rather than scVelo's splicing kinetics) give stronger or different driver genes? The authors call for such methods.
- How far can multiplexing go with primary nanobodies or nanobodies against other host species, and how fast does noise grow per added modality?
- The wiki's scCUT&Tag review page reports 30–50% duplicated fragments in nano-CT libraries, while this paper reports only 0.11–0.14% linear-amplification duplicates; the two numbers measure different things, and the PCR-duplicate rate is not in the main text. (synthesis)

## Related

- [[30-Concepts/cut-and-tag]] · [[40-Topics/histone-modifications]] · [[30-Concepts/chromatin-accessibility]] · [[30-Concepts/chromatin-velocity]] · [[30-Concepts/tn5-tagmentation]]
- [[10-Summaries/bartosovic-2021-sccut-tag]] · [[10-Summaries/gopalan-2022-multi-cut-and-tag]] · [[10-Summaries/janssens-2023-scicut-tag]] · [[10-Summaries/geisenberger-2025-scepi2-seq]] · [[10-Summaries/ma-2020-share-seq]]
- [[40-Topics/single-cell-multiomics]] · [[40-Topics/chromatin-architecture]]
