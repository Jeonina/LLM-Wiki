---
type: summary
title: "de Boer & Regev 2018 — BROCKMAN: deciphering variance in epigenomic regulators by k-mer factorization"
source: "[[00-Sources/papers/BROCKMAN_ deciphering variance in epigenomic regulators by k-mer factorization]]"
source_kind: paper
author: "Carl G. de Boer, Aviv Regev"
published: 2018-07-03
ingested: 2026-10-07
doi: "10.1186/s12859-018-2255-6"
journal: "BMC Bioinformatics 19:253"
tags: [BROCKMAN, scATAC-seq, k-mer, gapped-k-mers, PCA, TF-activity, peak-free, AP-1, TF-cooperativity, K562]
entities: ["[[aviv-regev]]"]
concepts: ["[[scatac-seq]]", "[[chromatin-accessibility]]", "[[transcription-factor-motif]]", "[[de-novo-motif-discovery]]", "[[chromvar]]", "[[dimensionality-reduction]]", "[[batch-effect]]", "[[peak-calling]]", "[[replication-timing]]", "[[tn5-tagmentation]]"]
topics: ["[[single-cell-atac-seq]]", "[[computational-methods]]"]
---

**Citation:** de Boer & Regev (2018) — *BROCKMAN: deciphering variance in epigenomic regulators by k-mer factorization* — *BMC Bioinformatics* 19:253. [DOI](https://doi.org/10.1186/s12859-018-2255-6)

# de Boer 2018 — BROCKMAN

> BROCKMAN (Brockman Representation Of Chromatin by *K*-mers in Mark-Associated Nucleotides) sidesteps both peak calling and prior motif knowledge: each cell becomes a vector of **gapped *k*-mer frequencies (k = 1–8) in the DNA around its Tn5 insertion sites**, and PCA on that k-mer × cell matrix exposes axes of variation that map onto (sets of) transcription factors. The rationale is mechanistic: if a TF that can open chromatin becomes more active, more of its cognate k-mers end up in accessible DNA. Applied to 1,440 scATAC-seq cells (C1 platform, GEO GSE65360), the representation separates cell types, drug treatments, replicate batches, a chip-position artifact and cycling cells; individual PCs correspond to co-varying TFs that are enriched for known physical interactions, and a simple occupancy model argues that cooperative binding is intrinsically more variable than non-cooperative binding.

## Key claims

- **A peak-free, motif-free representation separates biology and artifacts.** On 1,440 human cells (K562 ± drug treatments, GM12878, H1ESC, BJ, TF-1, HL-60), t-SNE of the **131 significant PCs** partitions cell types and K562 treatments, and also exposes a K562-replicate-3 outlier cluster whose cells have **consecutive C1-chip indices** — interpreted as an experimental artifact.
- **A "mixed" cluster is cycling cells.** It contains every cell type except BJ fibroblasts; scoring each cell's ratio of ATAC reads in (G2+S) vs G1 replication-timing domains (from K562 Repli-seq) shows high-ratio cells fall into this cluster or into a sub-region of their own cell-type cluster.
- **Reads outside peaks carry more grouping information than reads inside peaks.** With peaks called by HOMER on pooled K562 scATAC (46,145 peaks, ±250 bp), out-of-peak reads grouped cells by sample better, particularly in the local (20-nearest-neighbour) measure. The result held using 360,648 ENCODE K562 DNase hypersensitive sites as the peak set, where out-of-peak reads were on average **55% of reads**. Out-of-peak reads also yielded more significant PCs (47 vs 31), which the authors use to argue the effect is not simple G+C bias.
- **Including repeat-element reads improves grouping** both locally and globally (K562-only analysis, so not polymorphism-driven).
- **Gapped k-mers help only globally** (ROC), not locally, but compress the signal into fewer significant PCs (57 vs 88 with ungapped only).
- **PCs map to TFs.** k-mer loadings are tested for enrichment of each TF's cognate k-mers (CIS-BP PBM 8-mer Z-scores and PWMs; 412 K562-expressed TFs) by a minimum-hypergeometric test. In the K562 treated/untreated analysis (53 significant PCs), PC3 and PC5 best separate treated cells, with 107 and 37 motifs enriched/depleted respectively; JUNB is enriched on PC3 and JUND on PC5 despite near-identical PWMs — PBM Z-scores distinguish them.
- **Within untreated K562**, 13 of 27 significant PCs distinguished replicates (excluded as batch); of the remaining 14 cell-variable PCs, **40.5% (167/412)** of expressed TFs with known motifs associated with at least one PC — a number the authors caution may be inflated by motif similarity.
- **Variable-activity TFs are lowly expressed, not more variably expressed** (scRNA-seq of K562: mean expression lower, Wilcoxon P = 0.08; mean-corrected CV similar, P = 0.54).
- **Co-varying TFs physically interact.** There are **2.5×** more high-confidence protein–protein interactions among TFs co-enriched on a PC than expected (hypergeometric P = 0.03). AP-1 family motifs were associated with five of the 13 cell-variable PCs.
- **Cooperativity predicts variability.** An equilibrium occupancy model shows that cooperative binding (Kd_xy < Kd_x) gives a steeper occupancy curve, so cell-to-cell variation in TF concentration around the critical point produces larger occupancy/accessibility variation than non-cooperative binding.

## Methods / evidence

Re-analysis of public scATAC-seq (GSE65360): Bowtie2 to hg19; regions = ±50 bp around each Tn5 insertion (5′ read end), merged; sequences scanned for all gapped k-mers k = 1–8 on both strands (AMUSED). Cells with <3,162 (10^3.5) distinct insertion loci removed. k-mer frequencies z-scaled, PCA (`prcomp`), significant PCs by jackstraw permutation; t-SNE for display. Grouping quality measured by same-sample fraction among 20 nearest neighbours and by ROC with bootstrap P-values. TF assignment via CIS-BP (638 PBM-derived 8-mer motifs, 1,882 PWMs, 870 TFs → 412 expressed in K562). The authors note PC1 is often dominated by G+C content and must be interpreted carefully. Factorization by ICA and sparse minibatch PCA reportedly gave similar results (data not shown).

Weight: a single, small (C1, 1,440-cell) dataset, mostly cell lines; the outside-peak result is striking but measured as ability to separate *samples/replicates*, which could partly reflect technical batch differences — the authors acknowledge this. Several robustness claims are "data not shown". No quantitative benchmark against chromVAR or other scATAC tools is performed; the chromVAR comparison in the Discussion is argued, not measured.

## Surprising or load-bearing bits

- **Out-of-peak reads beat in-peak reads for grouping cells** — an early empirical case for peak-free featurization, later the design premise of bin-based tools such as [[fang-2021-snapatac]]. (synthesis)
- **Biology can hide in the "noise" fraction**: the authors propose that dynamic enhancers are both harder to call as peaks and more informative of cell state, or that pioneer TFs transiently open non-functional motif-bearing loci ("hit and run").
- **Knowledge deficit moves from analysis to interpretation**: k-mer space can separate cells differing by an as-yet-undescribed TF, which motif-based scoring cannot.
- **Chip-position artifacts are visible in sequence-feature space** — consecutive C1 indices formed their own cluster, a reminder that unsupervised structure is not automatically biology.
- The cooperativity argument offers a mechanistic reason why AP-1 (bZIP heterodimer-forming, proposed pioneer) motifs dominate variable accessibility axes.

## Concepts touched

- [[transcription-factor-motif]] / [[de-novo-motif-discovery]] — k-mer loadings as an assumption-light alternative to predefined motif sets.
- [[chromvar]] — the closest contemporary; BROCKMAN argues chromVAR's reliance on predefined peaks and ungapped 7-mers may reduce sensitivity and interpretability.
- [[peak-calling]] — evidence that restricting to peak reads discards cell-discriminating signal.
- [[batch-effect]] — replicate-specific PCs explicitly identified and excluded.
- [[replication-timing]] — read ratio in Repli-seq domains as a cell-cycle score for scATAC.
- [[dimensionality-reduction]] — PCA + jackstraw on k-mer features.

## Connections to other sources

- Re-analyses the data of [[buenrostro-2015-nature]] (the C1 scATAC study, GSE65360).
- Positioned against [[schep-2017-chromvar]]; complements later sequence-aware scATAC models [[yuan-2022-scbasset]] (CNN on sequence) and peak-free [[fang-2021-snapatac]] / [[zhang-2024-snapatac2]]. (synthesis)
- Alternative scATAC latent representations: [[bravo-2019-cistopic]] (LDA), [[xiong-2019-scale]] (VAE), [[ashuach-2022-peakvi]] (VAE on peaks).
- Motif-enrichment tooling context: [[heinz-2010-homer]] (HOMER used for its peak calls).
- Benchmark context for scATAC featurization: [[luo-2024-scatac-benchmark]].

## Open questions

- Is the outside-peak advantage biological (dynamic enhancers, transient pioneer sampling) or technical (batch-specific tagmentation)? Not resolved with this dataset.
- How does the approach scale to droplet/combinatorial-indexing data with far fewer fragments per cell, where 8-mer counts would be sparser? (synthesis)
- Disentangling causal TFs within motif families (AP-1) remains unsolved by any motif-based method, as the authors note.

## Related

- [[schep-2017-chromvar]] · [[buenrostro-2015-nature]] · [[transcription-factor-motif]] · [[40-Topics/single-cell-atac-seq]]
