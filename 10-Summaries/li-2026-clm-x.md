---
type: summary
title: "Li et al. 2026 — CLM-X: A multimodal single-cell foundation model with flexible multi-way Transformer for unified scRNA-seq and scATAC-seq analysis"
source: "[[00-Sources/papers/CLM-X- A multimodal single-cell foundation model with flexible multi-way Transformer for unified scRNA-seq and scATAC-seq analysis.pdf]]"
source_quality: full
source_sha256: "22c8d67ad5c4ba460322cb7e81eb51ae6bd327d1cbd24d3e968981be170e8062"
source_kind: paper
author: "Bowen Li, Ziqiang Liu, Zhen Wang, Zhenyu Xu, Yantao Li, Chulin Sha (corresponding), Xiaolin Li (corresponding)"
published: 2026-02-18
ingested: 2026-10-08
doi: "10.64898/2026.02.17.704943"
journal: "bioRxiv preprint"
tags: [CLM-X, single-cell-foundation-model, multiway-transformer, BEiT-3, mixture-of-modality-experts, scRNA-seq, scATAC-seq, multiome, pseudo-paired, scCLIP, masked-modeling, cross-modal-translation, batch-correction, perturbation-prediction, CLM-Access, preprint]
entities: []
concepts: ["[[single-cell-foundation-model]]", "[[multimodal-integration-methods]]", "[[joint-single-cell-multi-omics]]", "[[scatac-seq]]", "[[scrna-seq]]", "[[batch-effect]]", "[[cell-type-annotation]]", "[[cis-regulatory-element]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/single-cell-multiomics]]", "[[40-Topics/single-cell-atac-seq]]"]
---

**Citation:** Li et al. (2026) — *CLM-X: A multimodal single-cell foundation model with flexible multi-way Transformer for unified scRNA-seq and scATAC-seq analysis* — bioRxiv preprint (posted 18 February 2026). [DOI](https://doi.org/10.64898/2026.02.17.704943)

# Li 2026 — CLM-X

> CLM-X extends the same group's scATAC model CLM-Access into an RNA + ATAC foundation model. It uses a BEiT-3-style **multiway Transformer**: one shared self-attention module per block, with three modality-routed feed-forward experts (R-FFN, A-FFN, RA-FFN). Each modality becomes a fixed 2,000-token sequence. RNA is gene tokens plus within-cell rank bins (B = 50). ATAC is 1,998 genome-ordered patches of about 575 binarised cCREs each, from a 1,154,464-cCRE reference. Paired cells concatenate both into one 4,000-token context. Pretraining runs in stages: masked RNA reconstruction on **~36 M CELLxGENE scRNA-seq cells**, then masked ATAC reconstruction on **~2.8 M scATAC-seq cells** (CATlas + Descartes fetal atlas), then paired conditional reconstruction on **377,134 pseudo-paired fetal cells from scCLIP**. In the paired stage, ATAC is masked first and predicted from RNA, then the reverse. The pseudo-pairs are RNA and ATAC cells matched at random within the same annotated cell type, so **no truly paired multiome data are used in pretraining**. All five benchmarks fine-tune on 10 public datasets.

## Key claims

- **Design argument against contrastive multimodal FMs.** The authors argue that scCLIP and SCARF depend on contrastive pair discrimination, which is tied to paired data and to one specific modality pair. CLM-X instead uses unimodal branches to exploit abundant single-modality data, and learns the cross-modal link by conditional masked completion.
- **Batch correction.** The benchmarks were PBMC datasets 1–4 (4 batches), BMMC dataset 5 (13 batches) and PBMC datasets 6–7 (2 batches). Fine-tuned CLM-X had the highest mean NMI, bASW and overall score on each benchmark against MultiVI, Multigrate, MIRA and scMoMaT. Its overall score was 5.9–35.0% higher than these baselines and on average 11.6% higher than scGPT. On PBMC 1–4: NMI 0.759 / bASW 0.972 (Multigrate 0.734 / 0.927). On BMMC: 0.768 / 0.973. Zero-shot embeddings from the frozen Stage-RA checkpoint are described as "meaningful", but the text does not separate their scores.
- **Multimodal integration (datasets 1–7).** Overall fusion score 0.730, the best of all methods. ARI 0.658 against 0.622 for MultiVI and NMI 0.716 against 0.693. On cell-type neighbourhood metrics it roughly tied MultiVI (cLISI 0.977 vs 0.978; cASW 0.569 vs 0.577). The gain over baselines was 1.8–16.4%. On BMMC, the fused embedding (ARI 0.718, NMI 0.785) beat CLM-X RNA-only (0.505 / 0.661) and ATAC-only (0.415 / 0.624), and was only slightly above Multigrate (0.696 / 0.782).
- **Cross-modal translation is the largest gain.** Each dataset was split 80/20, stratified by cell type. For RNA → ATAC over the full peak set, CLM-X had the lowest RMSE on all seven datasets and the highest mean PCC, while its AUROC was similar to MultiVI (0.959 vs 0.968). For ATAC → RNA over all genes, it had the highest PCC on 6/7 datasets and the lowest RMSE on 7/7. CMAE was second on mean PCC (0.787 ± 0.074) but had unstable RMSE (3.333 ± 3.394). Example per-gene RMSE: CD8A 0.529 (BABEL 0.567, MultiVI 0.677); CD79A 0.368 (BABEL 0.411).
- **Multimodal cell-type annotation (datasets 1–4, 80/20 split).** The fused model with a learned per-cell RNA/ATAC gate reached macro F1 88.24 ± 2.35% and accuracy 91.88 ± 1.19%. This beat RNA-only (86.86%) and ATAC-only (67.45%), Seurat WNN (85.44 ± 6.67%), a multimodal scGPT variant (74.94%) and scJoint (58.14%). Recall on rare IL1B+ monocytes was 82.35% against 70.59% for scBridge; scGPT, scJoint and Seurat had 0% recall.
- **Perturbation (RNA-only fine-tuning).** On held-out perturbations in Adamson, Replogle K562-essential and Replogle RPE1-essential, CLM-X had the highest DE20 Pearson, beating the best baseline by +0.0029, +0.0196 and +0.1293. On genome-wide Δ Pearson it was near-tied with GEARS on Adamson (0.7423 vs 0.7467).

## Methods / evidence

Backbone: 12 pre-norm blocks, 8 heads, d = 512. Masking is 15% in the unimodal stages and 50% per modality in the paired stage. The RNA loss is MSE on bins and the ATAC loss is peak-wise BCE through a patch-to-600-peak decoder. The gene vocabulary has about 60k entries. Cells with more than 2,000 non-zero genes are deterministically subsampled. The RNA corpus is the CELLxGENE Census (schema 2.1.0), deduplicated from 65.6 M to about 36 M human cells. The ATAC corpus combines CATlas (hg38) with Descartes fragments lifted over from hg19 and re-quantified with snapATAC2. Downstream ATAC data are mapped onto the reference cCREs by any-overlap. Fine-tuning ran on 2 × A100 80 GB with batch size 20, for 30 epochs (batch correction and integration) or 100 epochs (translation, annotation and perturbation). Baselines and metrics follow the Hu et al. 2024 *Nature Methods* multi-omics benchmark. The paper does not give a code URL.

Weight: the benchmark is broad (10 datasets, 12 baseline algorithms, five tasks) and follows an external protocol, which is a strength. But almost every task fine-tunes on the evaluation datasets. For batch correction and integration, the fine-tuning target is HVG expression regression from the [CLS] embedding. The integration margins over MultiVI and Multigrate are small. The perturbation task bypasses the pretraining tokenisation entirely (5,000-gene dense vectors, no binning), so what transfers from pretraining is unclear there. (synthesis)

## Limitations

**Authors' own:**
- Fixed-length packing (2,000 tokens per modality, 4,000 paired) compresses information and may under-represent rare features.
- Genome-ordered ATAC patching scales but may miss higher-order regulatory organisation and long-range interactions.
- Imbalanced pretraining corpora and technology-specific artefacts can bias representations, and long-context pretraining is computationally expensive.

**Reviewer notes:** (at most three, each marked `(synthesis)`)
- The paired pretraining stage uses scCLIP pseudo-pairs: random RNA–ATAC matches within shared cell-type labels. Cross-modal dependencies learned there can only reflect cell-type-level co-variation, not within-type cell-to-cell coupling. The fine-tuning on real multiome data likely does the rest of the work, and the paper has no ablation that removes Stage-RA. (synthesis)
- Each benchmark task fine-tunes on train/test splits of the same datasets. There is no cross-dataset generalisation test (train on one multiome set, test on another) and no zero-shot numbers for the integration tasks. (synthesis)
- Patches of about 575 cCREs in genome order give the ATAC branch no explicit DNA-sequence or motif information, unlike sequence-aware ATAC models such as scBasset. (synthesis)

## Surprising or load-bearing bits

- **Pseudo-paired data is the common bottleneck.** CLM-X and [[liu-2025-scmomer]] both use the same scCLIP fetal pseudo-paired atlas (377,134 cells, 36,601 genes, 1,154,464 peaks) as their only "paired" pretraining data. SCARF instead uses 2.7 M true 10x Multiome cells. (synthesis)
- **Shared attention, separate FFNs.** The mixture-of-modality-experts design lets RNA-only, ATAC-only and paired inputs run through one encoder, so unpaired corpora can be used without any alignment loss.
- **Translation gains are in magnitude, not on/off.** AUROC for accessibility was roughly tied with MultiVI, but PCC and RMSE improved. The model's advantage is reconstructing graded signal rather than binary peak calls.

## Concepts touched

- [[single-cell-foundation-model]] — a multiway (mixture-of-modality-experts) RNA + ATAC foundation model pretrained on unpaired corpora plus pseudo-pairs.
- [[multimodal-integration-methods]] / [[joint-single-cell-multi-omics]] — benchmarked against MultiVI, Multigrate, MIRA, scMoMaT, SCOIT, BABEL, CMAE, Seurat WNN, scJoint and scBridge.
- [[scatac-seq]] — genome-ordered patch tokenisation of about 1.15 M binarised cCREs.
- [[cis-regulatory-element]] — CATlas cCREs as the shared ATAC feature space.
- [[batch-effect]] — NMI/bASW trade-off across 2-, 4- and 13-batch benchmarks.
- [[cell-type-annotation]] — gated RNA/ATAC fusion classifier.

## Connections to other sources

- Builds on the authors' scATAC foundation model [[liu-2025-clm-access]] (same patch tokenisation and Human-scATAC corpus).
- Positions itself against the contrastive designs of [[liu-2025-scarf]] and scCLIP. Shares its pseudo-paired data with [[liu-2025-scmomer]]. The other RNA + ATAC entry in this ingest is [[yu-2026-scdynomics]]. (synthesis)
- Other ATAC foundation models it cites: [[fu-2025-get]] (GET) and [[chen-2025-epiagent]] (EpiAgent).
- Main integration baseline: [[ashuach-2023-multivi]]. Annotation baseline Seurat WNN: [[hao-2021-seurat-wnn]]. RNA foundation-model baseline: [[cui-2024-natmethods]] (scGPT).
- Broader integration context: [[cao-2022-glue]], [[gong-2021-cobolt]], [[argelaguet-2020-mofa-plus]], [[stuart-2021-natmethods]], [[xiao-2024-multiomics-benchmark]].

## Open questions

- How much of the downstream gain comes from Stage-RA pseudo-pair pretraining versus fine-tuning on real multiome pairs? (synthesis)
- Does the model transfer to a multiome dataset from a tissue absent from CELLxGENE, CATlas and the fetal atlas without fine-tuning? (synthesis)
- The authors propose extending to more modalities. Does the multiway design actually scale to a third modality (for example protein or methylation) with only unpaired data? (synthesis)

## Related

- [[single-cell-foundation-model]] · [[multimodal-integration-methods]] · [[liu-2025-clm-access]] · [[liu-2025-scarf]] · [[liu-2025-scmomer]] · [[yu-2026-scdynomics]] · [[ashuach-2023-multivi]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/sequence-models-and-foundation-models]]
