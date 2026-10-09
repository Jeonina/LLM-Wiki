---
type: summary
title: "Liu et al. 2025 — SCARF: Single Cell ATAC-seq and RNA-seq Foundation model"
source: "[[00-Sources/papers/SCARF_ Single Cell ATAC-seq and RNA-seq Foundation model]]"
source_quality: full
source_sha256: "a6f4a484a10c47b29ee82b58611365be1a3a57674e72cb173f770c156d269f1d"
source_kind: paper
author: "Guole Liu, Yongbing Zhao, Yingying Zhao, Tianyu Wang, Quanyou Cai, Xiaotao Wang, … (Jiekai Chen, Ge Yang, Yongbing Zhao and Lihui Lin supervised)"
published: 2025-04-13
ingested: 2026-10-08
doi: "10.1101/2025.04.07.647689"
journal: "bioRxiv preprint"
tags: [SCARF, X-Omics, single-cell-foundation-model, multiome, 10x-multiome, scRNA-seq, scATAC-seq, Mamba, contrastive-learning, CLIP, masked-modeling, cell-matching, cross-omics-translation, cell-type-annotation, preprint]
entities: []
concepts: ["[[single-cell-foundation-model]]", "[[multimodal-integration-methods]]", "[[joint-single-cell-multi-omics]]", "[[scatac-seq]]", "[[scrna-seq]]", "[[cell-type-annotation]]", "[[batch-effect]]", "[[clustering-algorithms]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/single-cell-multiomics]]", "[[40-Topics/single-cell-atac-seq]]"]
---

**Citation:** Liu et al. (2025) — *SCARF: Single Cell ATAC-seq and RNA-seq Foundation model* — bioRxiv preprint (v1, posted 13 April 2025). [DOI](https://doi.org/10.1101/2025.04.07.647689)

# Liu 2025 — SCARF

> SCARF is a foundation model pretrained only on **paired** 10x Multiome (RNA + ATAC from the same nucleus) data. The authors built **X-Omics**: 2.7 million human cells from 454 public 10x Multiome profiles in GEO, 21 tissue types, all reprocessed from raw reads with Cell Ranger ARC on GRCh38 against a shared reference set of 1,743,872 peaks. Each modality has its own encoder trained with masked-token reconstruction. The two cell-level [CLS] embeddings are then aligned with a CLIP-style contrastive loss, using a queue of negatives. The backbone is described as a "modified Mamba". The paper evaluates zero-shot clustering, RNA–ATAC cell matching, a reference-lookup form of cross-omics translation, and few-shot cell-type annotation, almost entirely on 10x PBMC, human brain and BMMC multiome sets. The paper is short, and most results are shown as figures without numbers in the text.

## Key claims

- **Pretraining corpus is paired-only.** X-Omics holds 2.7 M cells from 454 10x Multiome profiles across 21 tissues, with a GEO cutoff of 23 February 2024. The authors call it "the largest curated collection of uniformly processed single-cell Multiome data". Every pretraining cell has both RNA and ATAC, so the contrastive step depends on true pairs.
- **Concatenated RNA + ATAC embeddings cluster best.** On hBMMC, hPBMC and hBrain, the concatenated SCARF embedding had the highest NMI, ARI, AMI, ASW and homogeneity, and the best AvgBio score. Baselines were single-modality models (scGPT and scFoundation for RNA, scBasset for ATAC) and RNA or ATAC PCA. The comparison pits a two-modality embedding against one-modality baselines.
- **Cell matching.** On 10x PBMC multiome (12,073 cells, 15 cell types), with Sinkhorn optimal-transport refinement of the embeddings, SCARF had the highest matching-probability score and the lowest FOSCTTM against scGLUE, Seurat, Harmony, LIGER, uniPort and scVI. On cell-type matching accuracy it scored 0.854, second to Harmony. It scored above 0.8 for 9 of 15 cell types.
- **Cross-omics translation.** The Results describe predicting RNA from ATAC. Marker genes (FCGR3A, "CSP3R", CD247) had Pearson r = 0.70–0.87 between predicted and measured expression, and predicted-RNA clustering approached real-RNA clustering on ARI, NMI and HOM. The Methods describe a k-nearest-neighbour lookup (k = 10, cosine distance, softmax weights) into a paired reference. The query is embedded in one modality, and the other modality is the weighted average of its reference neighbours. No decoder generates the missing modality.
- **Few-shot annotation.** A logistic-regression classifier on SCARF embeddings, trained on 10% of BMMC cells and tested on the other 90%, gave accuracy, macro F1, recall and precision above 0.75. This beat scFoundation, the only baseline.

## Methods / evidence

Data processing: Cell Ranger ARC v2.0.2. Sample-level filters were median RNA UMIs > 80 and median ATAC high-quality fragments > 250. Cell-level filters: for RNA, Scrublet doublets, ≥ 200 genes, ≥ 1,000 UMIs and mitochondrial fraction ≤ 0.2; for ATAC, ArchR doublets, ≥ 1,000 fragments and TSS enrichment ≥ 4. The reference peak set (1,743,872 peaks) was merged from 254 ATAC datasets. The peak matrix was binarised and TF-IDF transformed with corpus-wide IDF. RNA features are 19,365 protein-coding genes with GeneCompass-style ranked tokenisation: normalise to 10,000 counts, log1p, then divide by each gene's non-zero median computed from 100,000 sampled cells. Training: AdamW (weight decay 0.001), cosine schedule with 1,000 warm-up steps, peak learning rate 5 × 10⁻⁴, batch size 32, four epochs on 8 GPUs with mixed precision. The loss is a weighted sum of masked reconstruction, CLIP contrastive loss and a clipping-based regulariser. Code: github.com/JiekaiLab/scarf.

Weight: the text gives very few numbers, so most comparisons can only be read from figures. Parameter count, layer count, ATAC tokenisation and the λ loss weights are not reported. The "Mamba" backbone is described alongside "self-attention" in the RNA encoder and in the discussion of Mamba itself, so the architecture is unclear. Benchmarks use three 10x datasets, two from 10x demos. The paper does not say whether these demo datasets were excluded from X-Omics (GEO-sourced), so overlap between pretraining and test data cannot be ruled out. (synthesis)

## Limitations

**Authors' own:**
- The Discussion names future work rather than limitations: adding proteomic or spatial layers, testing more advanced fusion strategies, scaling to larger datasets and real-time analysis. It states no explicit limitations.

**Reviewer notes:** (at most three, each marked `(synthesis)`)
- The clustering benchmark compares a two-modality SCARF embedding against single-modality baselines. Multimodal baselines (MultiVI, GLUE, Seurat WNN) were used only for matching, not for joint-embedding clustering, so the "state-of-the-art" claim for cell representation is not tested against like-for-like methods. (synthesis)
- The translation method is a nearest-neighbour average over a paired reference. It cannot produce profiles absent from the reference, and the Results (ATAC → RNA) and Methods (RNA → ATAC) describe opposite directions. (synthesis)
- The abstract says X-Omics spans "multiple tissues and species", but the Results and Methods describe human data aligned to GRCh38 only. (synthesis)

## Surprising or load-bearing bits

- **Paired data at scale is the design premise.** SCARF needs true Multiome pairs for its contrastive step, which caps the corpus at what 10x Multiome has produced. 2.7 M paired cells is large for multiome but about ten times smaller than RNA-only corpora such as scGPT's ~33 M cells. (synthesis)
- **Uniform reprocessing is the most reusable part.** Re-aligning all 454 profiles from raw reads to one reference peak set gives a common ATAC feature space across studies, which most multiome atlases lack. (synthesis)
- **Harmony beat SCARF on cell-type matching accuracy (0.854 for SCARF, second place)**, even though SCARF was best on the pairwise metrics. A classical integration method is still competitive at the cell-type level.

## Concepts touched

- [[single-cell-foundation-model]] — a paired RNA + ATAC foundation model with CLIP-style alignment.
- [[multimodal-integration-methods]] / [[joint-single-cell-multi-omics]] — compared with scGLUE, Seurat, Harmony, LIGER, uniPort and scVI on RNA–ATAC matching.
- [[scatac-seq]] / [[scrna-seq]] — modality-specific masked reconstruction with a shared peak reference.
- [[cell-type-annotation]] — few-shot logistic-regression probe on frozen embeddings.
- [[clustering-algorithms]] — Leiden clustering scored by ARI/AMI/NMI/HOM and AvgBio.

## Connections to other sources

- Matching baselines: [[cao-2022-glue]] (scGLUE), [[korsunsky-2019-harmony]], [[welch-2019-liger]], and Seurat ([[hao-2024-seurat-v5]] is the cited Seurat paper).
- RNA-side foundation-model comparator: [[cui-2024-natmethods]] (scGPT). ATAC-side comparator: [[yuan-2022-scbasset]].
- Other RNA + ATAC foundation models in this ingest take different positions on pairing. [[liu-2025-scmomer]] trains its fusion stage on pseudo-paired data and distils ATAC knowledge into an RNA-only path. [[li-2026-clm-x]] and [[yu-2026-scdynomics]] are the other multimodal entries. (synthesis)
- Classical multimodal integration for context: [[ashuach-2023-multivi]], [[gong-2021-cobolt]], [[argelaguet-2020-mofa-plus]], [[stuart-2021-natmethods]]. Benchmark context: [[xiao-2024-multiomics-benchmark]].

## Open questions

- How much does the contrastive step add over concatenating two independently pretrained encoders? The paper has no ablation of the loss components. (synthesis)
- Were the 10x demo and BMMC test datasets excluded from X-Omics? (synthesis)
- Can the model embed RNA-only or ATAC-only datasets without a paired reference, as the "missing modality" framing in the translation section implies? (synthesis)

## Related

- [[single-cell-foundation-model]] · [[multimodal-integration-methods]] · [[joint-single-cell-multi-omics]] · [[cao-2022-glue]] · [[cui-2024-natmethods]] · [[yuan-2022-scbasset]] · [[liu-2025-scmomer]] · [[li-2026-clm-x]] · [[yu-2026-scdynomics]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/sequence-models-and-foundation-models]]
