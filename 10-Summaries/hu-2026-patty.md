---
type: summary
title: "Hu et al. 2026 — PATTY corrects open-chromatin bias for improved bulk and single-cell CUT&Tag profiling"
source: "[[00-Sources/papers/PATTY corrects open-chromatin bias for improved bulk and single-cell CUT&Tag profiling]]"
source_kind: paper
author: "Shengen Shawn Hu, Zhangli Su, Lin Liu, Qingying Chen, Megan C. Grieco, Mengxue Tian, Anindya Dutta, Chongzhi Zang"
published: 2026-05-22
ingested: 2026-10-07
doi: "10.1038/s41467-026-73599-8"
journal: "Nature Communications 17:6710"
tags: [PATTY, CUT&Tag, Tn5-bias, open-chromatin-bias, bias-correction, logistic-regression, H3K27me3, H3K27ac, H3K9me3, single-cell-CUT&Tag, ATAC-seq-control, bivalent-chromatin]
entities: []
concepts: ["[[30-Concepts/cut-and-tag]]", "[[30-Concepts/tn5-tagmentation]]", "[[30-Concepts/atac-seq]]", "[[30-Concepts/peak-calling]]", "[[30-Concepts/chromatin-accessibility]]", "[[30-Concepts/clustering-algorithms]]", "[[30-Concepts/chip-seq]]"]
topics: ["[[40-Topics/histone-modifications]]", "[[40-Topics/computational-methods]]", "[[40-Topics/single-cell-multiomics]]"]
---

**Citation:** Hu et al. (2026) — *PATTY corrects open-chromatin bias for improved bulk and single-cell CUT&Tag profiling* — *Nature Communications* 17:6710. [DOI](https://doi.org/10.1038/s41467-026-73599-8)

# Hu 2026 — PATTY

> CUT&Tag inherits Tn5's preference for accessible chromatin, so even repressive-mark libraries pile reads onto **active promoters** — a false signal that ChIP-seq does not show. The authors document this across hundreds of public datasets (including high-salt protocols), then build **PATTY** (Propensity Analyzer for Tn5 Transposase Yielded bias): a **pre-trained, mark-specific logistic-regression model** that takes local CUT&Tag and ATAC-seq signal patterns and outputs a corrected per-200-bp score. ATAC-seq is used not as a background to subtract but as an empirical covariate for the open-chromatin component. Correction improves correlation with expression and with antagonistic marks in bulk, and improves cell-type clustering in single-cell CUT&Tag.

## Key claims

- **The bias is widespread.** In K562, on average 18% of H3K27me3 CUT&Tag peaks are absent from ChIP-seq, and these CUT&Tag-unique peaks are enriched at active promoters and ATAC-seq open regions. In **277 human H3K27me3 CUT&Tag datasets published since 2024** (most using high-salt washes), signal at TSS ± 300 bp of 1,000 ubiquitously expressed genes exceeded the 300 bp–3 kb flanks, unlike 30 ENCODE ChIP-seq datasets.
- **Ground truth from biology, not ChIP.** True H3K27me3 regions: reproducible CUT&Tag peaks near non-expressed genes with zero H3K27ac reads (recurring in ≥14 of 17 datasets); false: peaks near highly expressed genes overlapping H3K27ac peaks. Result: 1,428 true (285.6 kb) and 1,231 false (246.2 kb) 200-bp regions in K562. False regions have significantly higher ATAC signal.
- **Simple beats deep.** Among penalized LR, RF, GBM, CNN, MLP, RNN and GRU, deep models looked better in cross-validation, but **LR gave the strongest biologically expected genome-wide behaviour** (most negative correlation of corrected H3K27me3 with expression and with H3K27ac). The best feature set was **CUT&Tag + ATAC-seq only** — adding IgG or one-hot DNA sequence did not help; ATAC was essential.
- **Corrects active and repressive marks**: H3K27me3 and H3K27ac (K562 training), H3K9me3 (validated on the authors' own HCT116 CUT&Tag: false active-promoter enrichment removed; negative correlation with expression and H3K9ac appears only after correction). Residual bias was still corrected in **high-salt CUT&Tag and CUTAC** data.
- **Transfers across cell types**: K562-trained models improved H3K27me3 and H3K27ac analysis in H1 ESCs. Bivalent genes (H3K4me3 + H3K27me3 promoters) fell from 1,851 (uncorrected MACS2) to 990 (PATTY); the 1,013 genes lost were highly expressed — unlikely true bivalent genes.
- **Single cell**: meta-cell smoothing (each cell + 10 nearest neighbours in top-50 PC space) then PATTY with bulk/pseudo-bulk ATAC raised ARI against ground-truth labels for H3K27me3 and H3K27ac in nano-CT, scCUT&Tag-pro and Paired-Tag data, and improved WNN integration of the two marks in nano-CT.
- **Stated limits**: validated only for H3K27me3, H3K27ac and H3K9me3. Applying the H3K27ac model to H3K4me3/H3K4me1/H3K36me3 raised correlation with expression, but the authors "do not recommend this practice". CTCF results were inconclusive; not recommended for TFs.

## Methods / evidence

Public CUT&Tag/ChIP-seq/ATAC/IgG reprocessed uniformly (bowtie2, MAPQ ≥30, 146-bp read extension, RPM); SICER for training-set peaks, MACS2 for comparisons. Features: 10-bp-resolution signal across a 1-kb window around each 200-bp bin. Evaluation deliberately avoids ChIP-seq as gold standard: Pearson correlation of PATTY score with **exon-array** expression (orthogonal to the RNA-seq used for labelling) and with ChIP-seq of the reciprocal mark. Single-cell: ArchR processing, top 25k variable tiles, k-means with k = number of annotated cell types, ARI vs published labels (surface protein, multimodal or RNA-derived).

Weight: the problem documentation (277 datasets) is the most convincing part. The labelling rule (reciprocal marks are mutually exclusive; repressive marks absent from expressed genes) is close to the evaluation metric, so some circularity is unavoidable even with the exon-array swap. Requires a matched ATAC-seq profile; the single-cell version uses bulk ATAC and meta-cell smoothing, which can itself raise ARI.

## Surprising or load-bearing bits

- **High-salt washes do not fix it.** The field's experimental remedy for Tn5 accessibility bias (from [[kaya-okur-2019-cut-and-tag|the Henikoff lab]]'s protocol work) leaves measurable residual promoter signal in recent data.
- **"Bivalency" can be a Tn5 artefact.** Nearly half of CUT&Tag-defined bivalent genes in H1 were highly expressed — a direct warning for stem-cell chromatin papers built on uncorrected CUT&Tag. (synthesis)
- **Sparse single-cell data amplify the bias**, because most marks in a cell are represented by one fragment — so correction matters more, not less, at single-cell scale.
- **Two Tn5 biases are distinct**: sequence-level cleavage bias (the authors' earlier SELMA) vs chromatin-level open-chromatin bias (PATTY). Sequence features added nothing here, perhaps because ATAC already encodes them.

## Concepts touched

- [[cut-and-tag]] — systematic open-chromatin false positives, persisting under high-salt and CUTAC protocols.
- [[tn5-tagmentation]] — accessibility preference as a confounder in any Tn5-based assay (authors list LIANTI, HiChIP, HiCAR, epigenomic MERFISH as potentially affected).
- [[atac-seq]] — repurposed as a covariate describing Tn5 propensity, not as an input control.
- [[peak-calling]] — PATTY outperforms MACS2 (with or without IgG) on the biology-based metrics; SEACR and SICER are noted as not designed for Tn5 bias.
- [[clustering-algorithms]] — bias correction raises ARI of k-means clustering on single-cell CUT&Tag.

## Connections to other sources

- Assays whose data it corrects: [[kaya-okur-2019-cut-and-tag]] (K562 training data source), [[bartosovic-2022-nano-cut-tag]] (nano-CT), [[zhang-2022-sccut-tag-pro]], [[bartosovic-2021-sccut-tag]], [[wu-2021-sccut-tag]], [[gopalan-2022-multi-cut-and-tag]], [[janssens-2023-scicut-tag]].
- Peak callers it compares with or cites: [[zhang-2008-macs]], [[meers-2019-seacr]].
- Tools used: [[granja-2021-archr]], [[hao-2021-seurat-wnn]].
- Bivalency concept it stress-tests: [[bernstein-2006-bivalent-chromatin]].
- Assays that sidestep Tn5 entirely: [[skene-2017-cut-and-run]] (MNase; claims no accessibility/AT bias), [[shi-2026-dechic-seq]] (deaminase recording; reports low ATAC correlation).

## Open questions

- Marks without a clean antagonist (H3K4me1/3, H3K36me3) and TFs have no ground-truth recipe — the method's reach is three marks.
- In heterogeneous tissue, H3K27ac/H3K27me3 overlap can be genuine cell mixing; the training rule would then mislabel true signal. Authors acknowledge this; trained only on cell lines.
- Does single-cell improvement come from correction or from meta-cell smoothing? Smoothing was applied before PATTY but the uncorrected comparison is not described as smoothed. (synthesis)

## Related

- [[cut-and-tag]] · [[tn5-tagmentation]] · [[kaya-okur-2019-cut-and-tag]] · [[40-Topics/histone-modifications]]
