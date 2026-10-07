---
type: summary
title: "Chen et al. 2025 — EpiAgent: foundation model for single-cell epigenomics"
source: "[[00-Sources/papers/EpiAgent_ foundation model for single-cell epigenomics]]"
source_kind: paper
author: "Xiaoyang Chen, Keyi Li, Xuejian Cui, Zian Wang, Qun Jiang, Jiacheng Lin, Zhen Li, Zijing Gao, Hairong Lv, Rui Jiang"
published: 2025-09-25
ingested: 2026-10-07
doi: "10.1038/s41592-025-02822-z"
journal: "Nature Methods 22(11):2316–2327"
tags: [EpiAgent, foundation-model, transformer, scATAC-seq, cell-sentence, cCRE, Human-scATAC-Corpus, perturbation-prediction, in-silico-knockout, cell-type-annotation, imputation, batch-correction, zero-shot]
entities: ["[[rui-jiang]]"]
concepts: ["[[scatac-seq]]", "[[chromatin-accessibility]]", "[[cis-regulatory-element]]", "[[cell-type-annotation]]", "[[scatac-imputation]]", "[[batch-effect]]", "[[reference-atlas-mapping]]", "[[dimensionality-reduction]]", "[[cistopic]]", "[[scale]]"]
topics: ["[[single-cell-atac-seq]]", "[[computational-methods]]"]
---

**Citation:** Chen et al. (2025) — *EpiAgent: foundation model for single-cell epigenomics* — *Nature Methods* 22(11):2316–2327. [DOI](https://doi.org/10.1038/s41592-025-02822-z)

# Chen 2025 — EpiAgent

> EpiAgent is a ~1.4-billion-parameter transformer pretrained on a curated **Human-scATAC-Corpus (~5 million cells, 31 tissues, 28 public datasets, >35 billion accessible-cCRE tokens)**. Its central representational move is the **"cell sentence"**: each cell is encoded only by the indices of its *accessible* cCREs (from a merged set of 1,355,445 cCREs), ordered by TF-IDF value, capped at 8,190 tokens. Because cCREs have no natural order, it is pretrained not by masked language modelling but by a new **cell–cCRE alignment** task (classify whether a cCRE is accessible given the cell embedding) plus **signal reconstruction** of all cCREs, with replaced-token detection as warm-up. Fine-tuned, it leads benchmarks on clustering, annotation and imputation; with added condition tokens it predicts responses to stimulation and unseen CRISPR perturbations, integrates batches, and supports in silico cCRE knockout.

## Key claims

- **Architecture.** Embedding module ~698M parameters (cCRE + rank embeddings, dim 512), transformer ~57M (18 bidirectional encoder layers, 8 heads, Flash Attention v2), signal decoder ~695M (single linear layer to all cCREs). The [CLS] output is the cell embedding; conditional embeddings (perturbation, batch) are added to the input [CLS].
- **Unsupervised feature extraction** (Buenrostro2018 hematopoiesis, Kanemaru2023 heart, Li2023b brain, Ameen2022 in-vitro stem cells): fine-tuned EpiAgent beats cisTopic, SCALE, PeakVI, SCALEX, scBasset and CASTLE on NMI and ARI (Leiden, cluster number matched), and on silhouette, cLISI and MAP; zero-shot EpiAgent is competitive on corpus-like data, especially brain.
- **Developmental pseudotime**: on Buenrostro2018 donor BM0828, PAGA trajectories on EpiAgent embeddings follow hematopoietic differentiation; combining EpiAgent embeddings with ClockDML loci (from the EpiTrace authors) gives pseudotime that, per the paper, avoids EpiTrace's mis-ordering of CLP and GMP cells.
- **Supervised annotation**: intra-dataset (2/3 reference, 1/3 query) EpiAgent beats PCA+SVM, MLP, EpiAnno, Cellcano and SANGO, by an average of 11.036% accuracy over the runner-up (Cellcano) and 21.549% macro-F1 over SANGO. Inter-dataset (brain: Li2023a / Lee2023 references → Li2023b query) it also leads; most other methods misannotate inhibitory neurons.
- **Imputation**: imputed data improve NMI by 11.123% and ARI by 18.605% on average over raw data, while scCASE and scOpen are unstable; median Pearson correlation of imputed signal with same-type cells >0.8.
- **Stimulation response (LPS-stimulated BMMCs, dsciATAC-seq; leave-one-cell-type-out)**: R² > 0.7 for mean accessibility change at the top 1,000 DA cCREs; >90% average direction accuracy on the top-100 up/down cCREs; lower Wasserstein distance than scGen, scPRAM and mean-shift baselines. Only resting cells were in the pretraining corpus.
- **Unseen genetic perturbation (CRISPR-sciATAC, Spear-ATAC; 25% of perturbations held out)**: Pearson correlation 24.177% higher than GEARS on Pierce2021; GEARS fails on Liscovitch-Brauer2021 and is barely above random on direction.
- **Integration and mapping**: batch tokens + optimal-transport-matched cross-batch targets remove batch structure in a three-dataset brain reference (best overall on NMI/ARI/kBET/iLISI); a 10x multiome brain query maps by 20-NN with labels consistent with marker gene expression, including rare endothelial cells.
- **In silico cCRE knockout**: removing the strongest promoter cCRE (within 5 kb upstream of TSS) from control cells moves them closer to real CRISPR-edited cells for most perturbations (one-sided t-test P < 0.05). In ccRCC, knocking out putative promoters of *EGLN3* (ccRCC-specific), *ABCC1* and *VEGFA* shifts synthetic 50%-cancer chimeric cells towards normal-like neighbours, *EGLN3* most strongly and the combination most of all — explicitly stated as cCRE-level, not causal.
- **Zero-shot annotators**: EpiAgent-B (brain; trained on Li2023a) accuracy >0.88 on Li2023b; EpiAgent-NT (non-brain; trained on Zhang2021) >0.95 on Kanemaru2023; balanced accuracy and macro F1 >0.8.

## Methods / evidence

Corpus: 27 published datasets + 30 integrated 10x PBMC samples; 18 with fragments, others peak matrices; cCRE set merged from three atlas cCRE sets (multi-tissue, brain, blood/bone marrow) rather than re-called peaks, to avoid bias toward abundant cell types; cCREs accessible in <100 cells and cells with <100 accessible cCREs removed. Pretraining 12 epochs, alignment negative ratio rising 1 → 2 → 5. Baselines run per their documentation; several (EpiAnno, Cellcano, scCASE, scOpen) required cell downsampling for memory; perturbation baselines limited to the top 50,000 cCREs.

Weight: broad and carefully leakage-aware in places (held-out cell types/perturbations; query brain dataset excluded from pretraining). But several evaluation datasets overlap with the pretraining corpus's tissue types, baselines were often run on reduced inputs because they could not scale, and ground truths for in silico knockout are proxies (embedding distances, synthetic chimeras). Most ablations live in supplementary notes not in the clipping.

## Surprising or load-bearing bits

- **Cell sentences avoid feature filtering**: by tokenising only accessible cCREs, EpiAgent sidesteps the usual pre-filtering of a sparse cell × peak matrix — the authors attribute part of the performance gap to baselines being "limited by extremely sparse signals and filtered cCREs".
- **Masked-LM does not fit ATAC**: accessibility is near-binary, the vocabulary is ~1.36M, and order is arbitrary — hence alignment-style binary classification objectives. A useful design lesson for any epigenomic foundation model. (synthesis on generalisation)
- **Parameters live in the vocabulary**: ~96% of the parameters (≈698M + ≈695M of ≈1.45B summed module sizes) are cCRE embeddings and the decoder; the transformer itself is only ~57M. "Billion-parameter" overstates model depth. (synthesis)
- **Perturbation prediction on chromatin** is new territory; even simple mean-shift baselines are included, which makes the gains interpretable.

## Concepts touched

- [[scatac-seq]] / [[cis-regulatory-element]] — cCRE-token representation and co-accessibility via attention.
- [[cell-type-annotation]] / [[reference-atlas-mapping]] — supervised, inter-dataset and zero-shot annotators.
- [[scatac-imputation]] — decoder-based reconstruction vs scOpen/scCASE.
- [[batch-effect]] — batch tokens with OT-matched cross-batch targets.

## Connections to other sources

- RNA foundation-model lineage it adapts: [[cui-2024-natmethods]] (scGPT).
- Benchmarked baselines in the wiki: [[bravo-2019-cistopic]], [[xiong-2019-scale]], [[ashuach-2022-peakvi]], [[yuan-2022-scbasset]], [[li-2021-scopen]].
- Pseudotime comparison with [[xiao-2025-epitrace]]; trajectory tool [[wolf-2019-paga]].
- scATAC tooling used: [[danese-2021-episcanpy]] (DA cCREs via `rank_features`), [[cao-2022-glue]] (MAP metric).
- Contrasting lightweight unsupervised approaches: [[de-boer-2018-brockman]] (k-mer PCA), [[fang-2021-snapatac]] / [[zhang-2024-snapatac2]]. (synthesis)

## Open questions

- No DNA sequence input: cCRE identities are arbitrary tokens, so the model cannot generalise to cCREs or species outside its vocabulary (multi-species sequence integration is listed as future work).
- How much of the gain survives against baselines given equal, unfiltered inputs and compute? (synthesis)
- In silico knockout validity beyond embedding proximity — no wet-lab validation of predicted state shifts.

## Related

- [[cui-2024-natmethods]] · [[ashuach-2022-peakvi]] · [[yuan-2022-scbasset]] · [[40-Topics/single-cell-atac-seq]]
