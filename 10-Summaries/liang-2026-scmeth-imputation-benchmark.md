---
type: summary
title: "Liang et al. 2026 — A systematic benchmarking framework and dual-view optimization strategy for single-cell DNA methylation imputation"
source: "[[00-Sources/papers/A systematic benchmarking framework and dual-view optimization strategy for single-cell DNA methylation imputation]]"
source_quality: full
source_sha256: "ddc3a8994b12c8a890d18450f264a96e17c96f93f8853ea2268fc02348748f9d"
source_kind: paper
author: "Haitian Liang, Heyang Hua, Siyu Li, Shengquan Chen (corresponding)"
published: 2026-08-12
ingested: 2026-10-07
doi: "10.1093/bib/bbag434"
journal: "Briefings in Bioinformatics 27(4):bbag434"
tags: [benchmark, imputation, single-cell-methylation, CaMelia, DeepCpG, CpG-Transformer, GraphCpG, MambaCpG, BridgeCpG, ensemble-learning, LightGBM, divide-and-conquer, Shannon-entropy, data-leakage, chromosome-holdout, transfer-learning]
entities: []
concepts: ["[[imputation]]", "[[bisulfite-sequencing]]", "[[scbs-seq]]", "[[clustering-algorithms]]", "[[convolutional-neural-network]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[dna-methylation]]", "[[computational-methods]]"]
---

**Citation:** Liang et al. (2026) — *A systematic benchmarking framework and dual-view optimization strategy for single-cell DNA methylation imputation* — *Briefings in Bioinformatics* 27(4):bbag434. [DOI](https://doi.org/10.1093/bib/bbag434)

# Liang 2026 — scDNAm imputation benchmark (BridgeCpG, divide-and-conquer)

> Single-cell CpG-level imputation methods have only ever been evaluated in their own papers, on favourable data. Benchmarking five of them (CaMelia, DeepCpG, CpG Transformer, GraphCpG, MambaCpG) across 13 public scDNAm datasets on seven dimensions shows **no universal winner**: performance is set mainly by the data — **sparsity and methylome heterogeneity (Shannon entropy)** matter more than cell number or coverage — and every method fails to finish on whole-genome datasets above ~500 cells within 72 h. The authors respond on two fronts: **BridgeCpG**, a LightGBM stacking ensemble over three deep models, and an **adaptive divide-and-conquer (D&C)** scheme that clusters cells (Ward linkage) into homogeneous 10–100-cell subsets and imputes each separately.

## Key claims

- **Ranking**: CaMelia and CpG Transformer had the highest aggregate scores across 10 metrics; CpG Transformer had consistently high medians with minimal variance; GraphCpG and MambaCpG were volatile; DeepCpG ran only in small, low-sparsity settings (e.g. ran on 20-cell hCLP, failed on 71-cell hMK). Aggregate rankings are not fully comparable because methods completed different dataset subsets.
- **Hard scale ceiling**: on whole-genome datasets >500 cells (e.g. hFC, 2313 cells), no method completed within 72 h at standard settings.
- **Entropy drives difficulty**: low-entropy datasets (e.g. mOocyte, hCMP; entropy <1.00) gave ACC generally >0.90; accuracy fell by >15% (relative) from low- to high-entropy groups (>1.5, e.g. hPGC, mESC_2i). ACC rose with lower sparsity and MCC with higher per-cell CpG coverage; regression/correlation analysis ranked sparsity and entropy above coverage or cell count as determinants.
- **Accuracy is misleading under heterogeneity**: high-entropy datasets showed TPR/TNR imbalance (e.g. mESC_2i TNR ≫ TPR) — models predict the majority class to inflate ACC; hPGC kept high ACC with poor MCC.
- **Sample size thresholds**: CaMelia cannot run on N = 1, peaks at 3–5 cells, and commonly failed above 20 cells (memory limit at ~50 million unique loci, ≈ 20 scBS-seq cells); deep models run at N = 1 but stabilise only above 5 cells (small datasets) and needed ≥50 cells on hPGC. GraphCpG was the only method to process the full 461-cell hPGC.
- **Random splits leak**: random 9:1 CpG splits gave significantly higher MCC/F1 than chromosome hold-out (train chr1–9, 11–19/22; test chr10; 20% of observed sites masked), because neighbouring CpGs are correlated. CpG Transformer and MambaCpG — reliant on neighbouring-CpG correlations — dropped most; CaMelia and GraphCpG were most split-robust.
- **Transfer depends on the source's entropy more than the method**: models trained on low-entropy mOocyte transferred to mESC_2i could beat self-trained models (DeepCpG MCC ~0.77 vs ~0.35). Pooling datasets (mouse, human, or cross-species) did not help and often hurt (negative transfer). Fine-tuning helped GraphCpG most; for sequence models it helped high→low entropy transfers and could hurt low→high; it cut CpG Transformer convergence from ~30 to 7–9 epochs.
- **Compute**: on an RTX A6000 (48 GB), MambaCpG exceeded 16,000 min at 200 hEmbryo cells; DeepCpG and MambaCpG reached nearly 900 min at 12 mESC_2i cells; GraphCpG scaled most linearly. Most models changed little after ~20 epochs; GraphCpG training fluctuated throughout.
- **BridgeCpG** (CpG Transformer + GraphCpG + MambaCpG probabilities → LightGBM meta-learner trained on chr11, tested on chr10) beat each base model and a naive average ensemble on five difficult datasets (mESC_2i, mESC_Ser, hMK, hPGC, hCellLine) and in 1–12-cell settings; gain-based importance ranked GraphCpG predictions highest, then local relative-position features. Its cost is bounded by the slowest base model.
- **D&C**: on hEmbryo (285 cells), Ward clustering produced 11 sub-clusters, all of which beat a stratified-sampling global model on F1 and MCC; D&C also improved CpG Transformer and GraphCpG on larger datasets and beat random/stratified baselines on mESC_2i and mESC_Ser. On hFC and mBrain_Atlas (103,982 cells), only the partitioning step is shown (t-SNE of separable groups), not full imputation accuracy.
- **Decision guide**: ≤20 cells with bulk reference → CaMelia; hundreds of cells → MambaCpG for heterogeneous populations, GraphCpG for class imbalance, CpG Transformer as default, BridgeCpG when compute allows; >500 cells → D&C first.

## Methods / evidence

13 benchmark datasets (12–461 cells; scBS-seq, scRRBS, scNOMe-seq, scCOOL-seq) from mouse ESC/oocyte, human haematopoietic progenitors, HCC, cell lines, embryos and PGCs, plus two snmC-seq/snmC-seq2 datasets (hFC, mBrain_Atlas) for D&C. All tools at default hyperparameters, 30 epochs for deep models, shared mask positions. Ten metrics (ACC, AUC, MCC, TPR, TNR, F1 + four composites) and five data descriptors (sparsity, mean methylation, coverage complexity, methylation variance, Shannon entropy). Datasets tiered as simple/intermediate/challenging by observed accuracy and between-method variance.

Weight: the leakage and entropy findings are well designed and broadly useful. Caveats the paper itself flags: CaMelia uses a bulk methylation profile other methods do not get; no ground truth beyond masked observed sites; no downstream (clustering/DMR) evaluation; all tools at defaults. The difficulty tiers are partly defined from the very performance they are used to explain, and BridgeCpG/D&C are evaluated by their developers on the datasets chosen because baselines did poorly there (synthesis).

## Surprising or load-bearing bits

- **More data made models worse** when the added data were high-entropy — a direct argument for curating training sets over pooling them.
- **Chromosome hold-out vs random split** is a general lesson for any CpG-level predictor: architectures that look best under random splits are exactly those exploiting neighbour correlation (synthesis).
- The scale asymmetry is stark: imputing 500 methylomes is framed as computationally equivalent to ~70,000 transcriptomes, because the human methylome has >28 million CpGs and coverage loss often exceeds 95%.
- The hard ceiling (>500 cells unfinished) means none of these site-level imputers is currently usable on sciMET/snmC atlas-scale data without partitioning — which is why atlas tools aggregate over windows instead (synthesis).

## Concepts touched

- [[imputation]] — adds the methylation-specific case: binary, ultra-high-dimensional, entropy-limited; random-split evaluation inflates scores.
- [[scbs-seq]] / [[bisulfite-sequencing]] — most benchmark data are scBS-seq; per-cell coverage and sparsity are the limiting inputs.
- [[clustering-algorithms]] — Ward hierarchical clustering repurposed to partition cells before imputation.
- [[convolutional-neural-network]] — DeepCpG's CNN+GRU is the oldest architecture tested and the least scalable.

## Connections to other sources

- Methods benchmarked: [[angermueller-2017-genomebiol]] (DeepCpG); CaMelia, CpG Transformer, GraphCpG and MambaCpG have no wiki summaries yet.
- Benchmark data sources in the wiki: [[smallwood-2014-natmethods]] (scBS-seq mESC/oocyte, GSE56879), [[hou-2016-sctrio-seq]] (HCC), [[luo-2017-snmc-seq]] (hFC), [[luo-2018-snmc-seq2]].
- Alternative, window-level ways around sparsity rather than site imputation: [[kapourani-2019-melissa]], [[kapourani-2021-scmet]], [[kremer-2024-methscan]], [[rylaarsdam-2025-amethyst]] (no imputation; missing set to 0).
- Parallel sparsity/imputation debates in other modalities: [[zhou-2019-schicluster]], [[zhang-2022-higashi]], [[zhang-2022-fast-higashi]] (scHi-C).

## Open questions

- Does better masked-site imputation translate into better clustering, DMRs or lineage inference? Not tested.
- How would entropy-aware or class-balanced losses (focal or class-balanced loss, suggested by the authors) change the TPR/TNR imbalance?
- D&C imputes within clusters defined from the same sparse data — circularity risk: within-cluster imputation may sharpen the clusters it was conditioned on (synthesis).

## Related

- [[imputation]] · [[angermueller-2017-genomebiol]] · [[40-Topics/dna-methylation]] · [[40-Topics/computational-methods]]
