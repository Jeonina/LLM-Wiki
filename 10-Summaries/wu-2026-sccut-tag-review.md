---
type: summary
title: "Wu et al. 2026 — Advances in scCUT&Tag and computational analysis for single-cell gene regulatory element mapping"
source: "[[00-Sources/papers/Advances in scCUT&Tag and computational analysis for single-cell gene regulatory element mapping]]"
source_quality: full
source_sha256: "768ff3ce1be1e9a7b74a21e3cc3a44db38a45ce5343cc4d00188fc2438cca3d9"
source_kind: paper
author: "Jun Wu, Md Wahiduzzaman, Pengfei Yin, Puxuan Sun, Haoping Chen, Yongwen Ding, Jiankang Wang (supervising author)"
published: 2026-01-29
ingested: 2026-10-07
doi: "10.1093/bib/bbag015"
journal: "Briefings in Bioinformatics 27(1):bbag015"
tags: [review, scCUT-and-Tag, histone-modifications, transcription-factors, Signac, ArchR, SnapATAC2, LSI, TF-IDF, ChromHMM, WNN, duplicate-removal, TSS-enrichment, G-quadruplex, spatial-CUT-and-Tag]
entities: []
concepts: ["[[cut-and-tag]]", "[[scicut-tag]]", "[[cut-and-run]]", "[[chip-seq]]", "[[tn5-tagmentation]]", "[[peak-calling]]", "[[pseudo-bulk]]", "[[quality-control-metrics]]", "[[duplicate-marking]]", "[[dimensionality-reduction]]", "[[clustering-algorithms]]", "[[multimodal-integration-methods]]", "[[cell-type-annotation]]", "[[chromvar]]", "[[transcription-factor-motif]]", "[[trajectory-inference]]", "[[enhancer-states]]", "[[spatial-multiomics]]", "[[batch-effect]]", "[[scatac-seq]]"]
topics: ["[[histone-modifications]]", "[[single-cell-atac-seq]]", "[[computational-methods]]", "[[single-cell-multiomics]]"]
---

**Citation:** Wu et al. (2026) — *Advances in scCUT&Tag and computational analysis for single-cell gene regulatory element mapping* — *Briefings in Bioinformatics* 27(1):bbag015. [DOI](https://doi.org/10.1093/bib/bbag015)

# Wu 2026 — scCUT&Tag computational review

> This is a bioinformatics-focused review of scCUT&Tag and its variants. Its core argument: scCUT&Tag data are analysed almost entirely with scATAC-seq tooling (Signac, ArchR, SnapATAC), and that inheritance breaks down in specific, nameable places. The places it names are bins versus peaks, mark-specific QC thresholds, TSS enrichment for repressive marks, duplicate handling, cell-type annotation and multi-mark integration. The review catalogues **21 public datasets (Table 1)** found by a PRISMA 2020 search covering January 2019–December 2025. It lays out a seven-step workflow, demonstrates it on the scCUT&Tag-pro PBMC dataset (GSE195725, six marks), and ends with a list of integration gaps.

## Key claims

- **Dataset landscape.** The 21 studies cover active marks (H3K4me1/2/3, H3K27ac, H3K36me3), repressive marks (H3K9me3, H3K27me3), H2A.Z, CTCF/RAD21, Pol II, TFs (NR2F1, OLIG2), m6A (sn-m6A-CT) and G-quadruplexes (scG4, snG4-CUT&Tag). Captured cells range from ~2000 to >100,000. Fragments per cell range from 500 to 20,000. FRiP ranges from 0.1 to 0.81. Analysis bin sizes range from 200 bp to 50 kb.
- **Coverage is the main gap with scATAC-seq.** scCUT&Tag typically yields <10³ fragments per cell (10²–10⁴ in the comparison section), against >10⁴ commonly seen in scATAC-seq.
- **Three partitioning strategies:**
  - nano-well (ICELL8), used in the original Kaya-Okur 2019 study and in sciCUT&Tag;
  - droplet (10x Genomics), now the most widely used;
  - split-pool, as in uCoTarget, which profiled multiple HMs plus transcriptome in nearly 20,000 cells.
- **Transposase variants:** pA-, pAG-, pG-, nano- and nanobody-Tn5. pAG-Tn5 is noted for broader IgG compatibility.
- **Bins vs peaks:**
  - scCUT&Tag-pro, CoTACIT, NTT-seq, sciCUT&Tag and scNanoSeq-CUT&Tag used cell-by-bin matrices, typically 5 kb.
  - nano-CT, scG4, uCoTarget and sn-m6A-CT used cell-by-peak matrices.
  - The review's rule: low coverage favours bins, especially large ones (e.g. 50 kb). Peaks are better when coverage is sufficient.
  - It warns that "peaks" in scCUT&Tag papers are often actually fixed bins.
- **QC thresholds have to be set per mark.** scATAC uses cut-offs such as FRiP < 0.2 or TSS enrichment < 6–8× to flag background. In scCUT&Tag these vary by target: RAD21 gives concentrated, high-FRiP signal, H3K4me3 has high TSS enrichment, and H3K9me3 has minimal TSS enrichment.
- **TSS enrichment reverses for repressive marks.** For H3K27me3, Wu et al. 2021 defined a chromatin silencing score (CSS) at TSSs, where *low* CSS marks active genes. ChIP-seq strand cross-correlation metrics (NSC/RSC) have not been adopted, because depth is too low.
- **PCR duplicates.** nano-CT libraries contain 30–50% duplicated fragments. The original scCUT&Tag study did not explicitly report deduplication, but later pipelines (Picard, SAMtools, Cell Ranger ATAC, MACS2 `--keep-dup=1`) remove duplicates as standard. The review notes that in bulk CUT&Tag, duplicates may partly reflect real repeated tagmentation.
- **LSI dimensions 2–30 are typical.** The first component is dropped because it correlates with depth.
- **Footprints look different from scATAC.** In scATAC-seq, TF footprints are broad, shallow dips that need deep coverage and bias correction (HINT-ATAC, TOBIAS). In scCUT&Tag, TF events appear as narrow, high-amplitude peaks at the binding site, because the pA-Tn5 is tethered there, so only local background normalization is needed.
- **Capabilities scATAC lacks:**
  - chromatin-state inference from multiple marks (ChromHMM, scChromHMM);
  - in the review's demo on the PBMC data, four states recovered (promoter, enhancer, repressive, heterochromatin), with monocytes showing broader repressive-domain coverage;
  - peak-to-gene linkage with Cicero (e.g. distal Sox10 enhancers, Bartosovic 2021);
  - HM-centric trajectories: broadening of H3K4me3 at mature-oligodendrocyte promoters, and progressive H3K27me3 silencing of TF motifs in glioblastoma.
- **Integration gaps:**
  - batch effects across platforms and bin sizes;
  - expert-driven integration with scRNA-seq via WNN, which can obscure native chromatin variation;
  - ChromHMM/scChromHMM described as the only promising approaches for combining multiple marks within one dataset;
  - no scCUT&Tag-specific method for matching cells across modalities (pseudobulk or metacells are the current workarounds).
- **Outlook:**
  - translational: AutoCUT&Tag (leukemia drug sensitivity), scCPA-Tag (HCC subtypes linked to prognosis);
  - spatial: spatial CUT&Tag and spatial CTRP-seq;
  - foundation models pretrained mostly on scATAC (EpiAgent, EpiFoundation, Atacformer, EpiBERT), with the caveat that adapting them needs larger, standardised scCUT&Tag datasets.

## Methods / evidence

This is a narrative review with a PRISMA-guided literature search (Fig. S1). The original analysis consists of a single demo on GSE195725 (Zhang 2022 scCUT&Tag-pro, six HMs in human PBMC) using Signac. It covers:

- QC (median FRiP >0.7 for all six marks);
- global correlations (H3K27ac positive with H3K4me1/2/3 and negative with H3K27me3);
- PCA versus LSI;
- WNN with RNA;
- the CD8A locus;
- top-50 differential H3K27ac peaks per cluster;
- ChromHMM;
- motif enrichment (E2F1/3/4 shared; HOXC8 in T/NK and IRF6 in monocytes);
- CD5 peak-to-gene linkage.

Supplementary tables S1–S4 catalogue tools and algorithms; they are not in the clipping.

Weight: useful as a map of datasets and as a checklist of how scCUT&Tag differs from scATAC. There is no new benchmarking. Some claims about other papers are loosely paraphrased; see Open questions for one case.

## Surprising or load-bearing bits

- **Repressive-mark logic inverts familiar QC.** A metric that flags good cells in scATAC (high TSS enrichment) would flag bad cells, or mean nothing, for H3K9me3 or H3K27me3. Pipelines that copy ATAC thresholds will quietly discard valid heterochromatin cells. (synthesis)
- **The bins-vs-peaks choice shapes what the analysis can see, beyond being a preprocessing detail.** The review's catalogue shows the field split roughly in half on this, so cross-study comparisons are confounded from the start. (synthesis)
- **The scCUT&Tag footprint argument.** Tethered cleavage puts signal at the binding site, while ATAC records steric hindrance in a sea of insertions. This makes TF scCUT&Tag a cleaner direct readout than ATAC footprinting, provided coverage allows. (synthesis based on the review's comparison)
- **Multi-mark integration within one dataset is described as almost entirely unsolved.** Only ChromHMM and scChromHMM are named.

## Concepts touched

- [[cut-and-tag]] / [[scicut-tag]] / [[tn5-tagmentation]] — variants, transposase fusions and partitioning platforms.
- [[cut-and-run]] / [[chip-seq]] — positioned as bulk predecessors (MNase release unsuited to single cells; ChIP has high background and needs many cells).
- [[peak-calling]] / [[pseudo-bulk]] — pseudobulk MACS2 (broad mode for H3K27me3), or cluster-level calling.
- [[quality-control-metrics]] / [[duplicate-marking]] — mark-specific FRiP/TSS thresholds; 30–50% duplicates.
- [[dimensionality-reduction]] / [[clustering-algorithms]] — TF-IDF + SVD (LSI), dropping LSI component 1, Louvain/Leiden, UMAP.
- [[multimodal-integration-methods]] / [[cell-type-annotation]] — WNN with matched scRNA-seq versus marker-based annotation (CSS for H3K27me3).
- [[chromvar]] / [[transcription-factor-motif]] — the chromVAR variant modified in scCUT&Tag-pro; HOMER, MEME/JASPAR, ArchR deviations.
- [[trajectory-inference]] — HM-centric pseudotime.
- [[enhancer-states]] — ChromHMM chromatin states from multi-mark pseudobulk.
- [[spatial-multiomics]] — spatial CUT&Tag and spatial CTRP-seq.
- [[batch-effect]] — cross-platform harmonisation of scCUT&Tag data.

## Connections to other sources

- **Primary studies catalogued:** [[kaya-okur-2019-cut-and-tag]], [[bartosovic-2021-sccut-tag]], [[zhang-2022-sccut-tag-pro]] (demo dataset), [[bartosovic-2022-nano-cut-tag]] (nano-CT), [[janssens-2023-scicut-tag]], [[wu-2021-sccut-tag]] (glioblastoma H3K27me3, CSS).
- **Benchmark it summarises (its ref. 32):** [[raimundo-2023-schptm-benchmark]]. The recommended recipe matches (large fixed bins, no feature selection, TF-IDF, then SVD/NMF), but other details differ; see Open questions.
- **Tooling inherited from scATAC:** [[stuart-2021-natmethods]] (Signac), [[granja-2021-archr]], [[fang-2021-snapatac]], [[zhang-2024-snapatac2]] (more efficient and scalable than the R frameworks), [[pliner-2018-cicero]], [[schep-2017-chromvar]], [[hao-2021-seurat-wnn]], [[bravo-2019-cistopic]].
- **scChIP-seq lineage:** [[rotem-2015-drop-chip]].
- **Independent scATAC benchmark for contrast:** [[luo-2024-scatac-benchmark]].

## Open questions

- **Paraphrase of the benchmark does not match Raimundo 2023.** The review says ref. 32 used "simulated and public datasets", benchmarked "Signac, ArchR, cisTopic and SnapATAC", and found that cell-by-peak matrices "perform better at high sequencing depth". [[raimundo-2023-schptm-benchmark]] instead:
  - used three public datasets with in-silico downsampling;
  - did not include ArchR (it tested ChromSCape_LSI/PCA, Signac, cisTopic, SnapATAC, PeakVI, SCALE, NMF and TFIDF-NMF);
  - found pseudobulk peak sets generally not competitive with fixed bins, with no stated depth-dependent reversal.

  The review's own bins-vs-peaks rule may therefore rest on scATAC analogy rather than scHPTM evidence. (synthesis)
- **A sentence is garbled.** The text says active marks "are not informative ... from scRNA-seq data, yet their repressive chromatin landscape exhibits clear patterns of cell-type specificity". What the authors meant is unclear.
- There is no consensus on how to set mark-specific QC thresholds; the review says they must be decided case by case.
- It is open whether scATAC-pretrained foundation models transfer to scCUT&Tag, given the differences between marks and antibodies.

## Related

- [[raimundo-2023-schptm-benchmark]] · [[zhang-2022-sccut-tag-pro]] · [[cut-and-tag]] · [[40-Topics/histone-modifications]]
