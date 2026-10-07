---
type: summary
title: "Raimundo et al. 2023 — A benchmark of computational pipelines for single-cell histone modification data"
source: "[[00-Sources/papers/A benchmark of computational pipelines for single-cell histone modification data]]"
source_kind: paper
author: "Félix Raimundo, Pacôme Prompsy, Jean-Philippe Vert, Céline Vallot"
published: 2023-06-20
ingested: 2026-10-07
doi: "10.1186/s13059-023-02981-2"
journal: "Genome Biology 24:143"
tags: [benchmark, scHPTM, scCUT-and-Tag, scChIP-seq, dimensionality-reduction, TF-IDF, LSI, bin-size, feature-selection, neighbor-score, ChromSCape, Signac, cisTopic, SnapATAC, PeakVI, SCALE, NMF]
entities: []
concepts: ["[[cut-and-tag]]", "[[chip-seq]]", "[[dimensionality-reduction]]", "[[cistopic]]", "[[snapatac]]", "[[scale]]", "[[latent-dirichlet-allocation]]", "[[jaccard-similarity]]", "[[peak-calling]]", "[[pseudo-bulk]]", "[[quality-control-metrics]]", "[[cite-seq]]", "[[scanpy]]", "[[scopen]]"]
topics: ["[[histone-modifications]]", "[[computational-methods]]", "[[single-cell-atac-seq]]"]
---

**Citation:** Raimundo et al. (2023) — *A benchmark of computational pipelines for single-cell histone modification data* — *Genome Biology* 24:143. [DOI](https://doi.org/10.1186/s13059-023-02981-2)

# Raimundo 2023 — scHPTM pipeline benchmark

> Single-cell histone PTM data (scCUT&Tag, scChIP-seq) look like scATAC-seq on disk but are far sparser and their signal domains are far wider, so scATAC habits do not transfer automatically. Running **11,970 pipeline combinations (11,080 successful)** over mark × embedding method × matrix construction × cell selection × feature selection × cell number × coverage, the authors find that **how reads are binned matters more than which embedding method is used**. Their recipe: large fixed-size bins (100–200 kbp), no feature selection, minimal cell filtering, TF-IDF, then SVD or NMF.

## Key claims

- **TF-IDF-based methods win.** On the mouse brain dataset the three best embeddings are consistently ChromSCape_LSI, TFIDF-NMF and Signac, all of which apply TF-IDF. They are followed by SnapATAC and PeakVI (except on H3K4me3), then cisTopic, NMF, SCALE and ChromSCape_PCA. CPM normalization followed by PCA (ChromSCape_PCA) is worst everywhere. The TF-IDF effect also shows up directly as the gap between NMF and TFIDF-NMF.
- **This ranking is specific to scHPTM.** In the earlier scATAC-seq benchmark the authors cite, CPM-based methods were competitive, and cisTopic was one of the best tools. Here cisTopic is not among the top methods, while LSI is strong in both modalities. The authors' conclusion is that scATAC practice should not be extrapolated to histone marks.
- **Signac drops off on the lower-coverage human PBMC data.** The authors attribute this to Signac's whitening step and its default 50 dimensions, which they say capture more noise at larger bin sizes (supplementary analysis).
- **Matrix construction has a large effect.** Performance first rises with bin size, then falls after a peak. The best/worst ratio across matrix constructions reaches 10.76 on PBMC (TFIDF-NMF, H3K4me1; mostly driven by a poor GeneTSS annotation). On mouse brain it averages 1.98 for H3K27me3 and reaches 2.8 for PeakVI. The Discussion puts it as "up to 80% better" with the best versus the worst bin size. An average method run with a well-chosen bin size can beat a top method run with a poor one.
- **Optimal bins are much larger than those used in practice.** Competitive ranges span roughly 50–1000 kbp for H3K27me3 and 10–200 kbp for H3K4me1. That is one to two orders of magnitude larger than the 1–5 kbp (and 50 kbp for H3K27me3) chosen in the original studies. Enhancing marks plateau at smaller bins than repressive marks.
- **Annotation-based features lose.** GeneTSS binning is usually not competitive, except for H3K4me3, which is TSS-enriched. MACS2 and SICER pseudobulk peak sets are also generally not competitive; the effect is weaker for H3K4me1 and H3K4me3, whose peaks are small and easier to call.
- **Feature selection is detrimental.** Both highly-variable (Seurat FindVariableFeatures) and top-coverage selection reduce performance, which keeps improving as more regions are retained. This holds at each bin size. It contradicts scRNA-seq and scATAC-seq (Signac) guidance.
- **Coverage filtering of cells helps only modestly.** The maximum gain is 15% (ChromSCape_LSI) and 13% (Signac) for H3K4me1, and the average for ChromSCape_LSI is 8%. Weak methods gain the most (ChromSCape_PCA 41%, SCALE 21%). Average coverage per cell, however, is strongly positively correlated with representation quality.
- **Cell number plateaus near ~6000 cells** for LSI and kernel-PCA methods, with only about 5% further gain going from 6000 to 10,000 cells. PeakVI had not plateaued (all datasets were under 12,000 cells), so VAE methods might overtake LSI at atlas scale. The authors state this is a conjecture.
- **Marks differ in how well they agree with RNA.** On mouse brain, H3K4me1 (0.291 ± 0.028) and H3K27ac (0.273 ± 0.026) have higher neighbor scores than H3K27me3 (0.169), H3K9me3 (0.148) and H3K4me3 (0.112). The authors read this as weaker coupling to expression, not lower information content.

## Methods / evidence

- **Datasets.** Three sets: mouse brain (Zhu et al., five marks, joint scRNA-seq), human PBMC scCUT&Tag-pro (five marks, joint CITE-seq protein), and MDA-MB468 breast cancer scChIP-seq (treated vs untreated, experimental labels).
- **Neighbor score.** The main metric is the overlap of kNN neighbourhoods between the scHPTM embedding and a scanpy PCA embedding of the co-assay. It is averaged over k = 0.1–10% of cells and runs from 0 to 1, with a random baseline of 0.05. ARI and AMI against author labels (k-means or hierarchical clustering) are reported as secondary metrics.
- **Fixed parameters.** Bin sizes range from 5 to 1000 kbp on a log scale. Nine embedding methods were run with default dimensions (Signac 50; SnapATAC, SCALE, NMF, TFIDF-NMF and ChromSCape 10; PeakVI and cisTopic choose their own).
- **What "experimental design" means here.** Cell number and coverage are varied by in-silico downsampling of existing data. No new data were generated.

Weight: very large and systematic, but the main metric assumes epigenomic neighbours should be transcriptomic neighbours. The authors note this holds for enhancer marks and may fail for repressive marks. Only three datasets are used, all under 12,000 cells, and the author labels used for ARI/AMI favour whatever method those authors used.

## Surprising or load-bearing bits

- **Bin size beats algorithm choice.** The step most pipelines treat as a default is the one with the largest effect. In practice, before comparing tools, sweep the bin size. (synthesis)
- **Enhancer marks can do well with 100–200 kbp bins** even though their peaks are a few kbp wide. The authors suggest two reasons: per-cell coverage is too low for small bins, and co-expressed genes cluster along the genome. If so, at this resolution the embedding may be tracking co-regulated gene neighbourhoods rather than individual enhancers, and the neighbor-score metric could reward that. (synthesis, building on the authors' own caveat)
- **The recommended workflow is two-stage.** Large bins are used to build the embedding and the clusters. Differential enrichment at finer resolution is then run on those clusters.
- **Coverage, not cell count, is the binding constraint.** Representation quality keeps improving with coverage and did not saturate on the data available. The authors point to higher-coverage protocols such as nano-CUT&Tag as the way forward.

## Concepts touched

- [[dimensionality-reduction]] — TF-IDF/LSI beats CPM-PCA, LDA (cisTopic) and VAEs (PeakVI, SCALE) at current scHPTM scale.
- [[cut-and-tag]] / [[chip-seq]] — benchmark spans Tn5-based scCUT&Tag and MNase-based scChIP-seq (for the scChIP data all methods except Signac do well on ARI).
- [[peak-calling]] / [[pseudo-bulk]] — pseudobulk MACS2/SICER peak sets underperform fixed bins as features for embedding.
- [[cistopic]], [[snapatac]], [[scale]], [[latent-dirichlet-allocation]], [[jaccard-similarity]], [[scopen]] (origin of TF-IDF + NMF) — all are compared head-to-head.
- [[quality-control-metrics]] — cell-coverage filtering matters little; the advice is to filter only non-cell barcodes.

## Connections to other sources

- **Contrasting scATAC result.** [[luo-2024-scatac-benchmark]] found SnapATAC/SnapATAC2 and feature aggregation outperform LSI for scATAC-seq. Here TF-IDF/LSI wins for scHPTM. Together these support the authors' point that best practice depends on the modality. (synthesis)
- **Datasets benchmarked:** [[zhang-2022-sccut-tag-pro]] (PBMC) and [[rotem-2015-drop-chip]] (the scChIP-seq lineage, as background).
- **Tools benchmarked:** [[stuart-2021-natmethods]] (Signac), [[bravo-2019-cistopic]], [[fang-2021-snapatac]], [[xiong-2019-scale]], [[li-2021-scopen]] (TF-IDF + NMF).
- **Assay context:** [[kaya-okur-2019-cut-and-tag]], [[bartosovic-2021-sccut-tag]], [[bartosovic-2022-nano-cut-tag]] (cited as a route to higher coverage), [[janssens-2023-scicut-tag]], [[wu-2021-sccut-tag]].
- **Review that summarises this benchmark:** [[wu-2026-sccut-tag-review]]. Its paraphrase differs in places; see Open questions there.

## Open questions

- Whether VAE methods (PeakVI, SCALE) overtake LSI above roughly 12,000 cells is untested.
- The neighbor score cannot separate "the embedding captures chromatin biology" from "the embedding mirrors RNA". This matters most for repressive marks, whose cell-state structure may legitimately differ from expression.
- At 100–200 kbp bins, cell states that differ only in a few local enhancers may be invisible. The benchmark cannot detect such losses, because its reference is the global RNA neighbourhood. (synthesis)

## Related

- [[wu-2026-sccut-tag-review]] · [[luo-2024-scatac-benchmark]] · [[zhang-2022-sccut-tag-pro]] · [[40-Topics/histone-modifications]]
