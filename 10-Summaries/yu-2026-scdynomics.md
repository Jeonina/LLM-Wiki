---
type: summary
title: "Yu et al. 2026 — scDynOmics: An Optimized Transformer Model for Representation Learning from Single-Cell Multiomics"
source: "[[00-Sources/papers/scDynOmics- An Optimized Transformer Model for Representation Learning from Single-Cell Multiomics.pdf]]"
source_quality: full
source_sha256: "1b2eab155d430b83bb3cc3d4420d785732decccc1b863828b08a45775e09bbb7"
source_kind: paper
author: "Gang Yu, Timothy J.S. Ramnarine, Johanna Klughammer (corresponding), Simon W. Mages (corresponding)"
published: 2026-05-24
ingested: 2026-10-08
doi: "10.64898/2026.02.28.708160"
journal: "bioRxiv preprint (version posted 24 May 2026)"
tags: [scDynOmics, single-cell-foundation-model, Linformer, linear-attention, transcription-factor, gene-regulatory-network, LoRA, adapter, PEFT, integrated-gradients, multiome, pan-promoter-ATAC, RNA-velocity, Slide-seq, mouse, LMU, preprint]
entities: []
concepts: ["[[single-cell-foundation-model]]", "[[multimodal-integration-methods]]", "[[joint-single-cell-multi-omics]]", "[[gene-regulatory-network]]", "[[scrna-seq]]", "[[scatac-seq]]", "[[cell-type-annotation]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/single-cell-multiomics]]"]
---

**Citation:** Yu et al. (2026) — *scDynOmics: An Optimized Transformer Model for Representation Learning from Single-Cell Multiomics* — bioRxiv preprint (first posted February 2026; this version 24 May 2026). [DOI](https://doi.org/10.64898/2026.02.28.708160)

# Yu 2026 — scDynOmics

> scDynOmics is a compact (~78–80 M parameter) transformer that takes the **whole coding genome as input** (about 22k genes) using Linformer attention. Keys and values are projected to a latent dimension l = 500, which the authors relate to the number of active transcription factors. The encoder alternates **TF-Encoder** layers, whose K/V projections are restricted to documented TFs, with **Full-Encoder** layers that span all genes. Multiome data enter **per gene**. ATAC is not represented as peaks: reads are summed over a pan-promoter window (−1,500 to +500 bp of each TSS), and each modality adds a binned value embedding and a modality embedding to the shared gene token. The authors treat promoter accessibility as analogous to unspliced pre-mRNA and RNA as analogous to spliced mRNA, an "RNA velocity" view of multiome data. Pretraining is masked-input prediction (15% of genes masked across all modalities) on **752,155 mouse multiome cells** from public SHARE-seq, SNARE-seq, sci-CAR, Paired-seq, ISSAAC-seq and 10x Multiome datasets. A separate human model is trained on 48,067 immune multiome cells. Fine-tuning uses non-linear LoRA-style adapters, and interpretation uses Integrated Gradients with a "discriminative specificity" score.

## Key claims

- **Architecture choice.** No cell in the mouse corpus expressed more than 700 TFs, which capped the search for l. l = 500 gave the best trade-off between masked and full-input reconstruction. The hybrid TF/Full encoder (78 M parameters) matched an all-Full-Encoder variant (139 M) on masked reconstruction and did better on full-input reconstruction. The default model has 12 layers and 12 heads (L12H12), embedding dimension 96 and FFN dimension 768.
- **Cross-paradigm transfer (mouse gastrulation, 7,187 cells, 10-fold CV).** In fine-tuning, the multiome-pretrained model was fed **spliced/unspliced RNA** in place of RNA/ATAC. Its median accuracy was 0.82, against 0.78 without pretraining, 0.80 when fine-tuned on total RNA only, 0.75 for logistic regression, 0.79 for XGBoost and 0.82 for a tuned scANVI. Pretraining helps here, but the result ties scANVI rather than beating it.
- **Small, topic-specific pretraining (human immune, 48,067 cells → Zheng68k).** scDynOmics outperformed scBERT, Geneformer (v1 and v2-104M) and CellFM-80M, and matched or exceeded logistic regression, XGBoost and scANVI, with or without 2,000-HVG selection. The authors state that "the actual benefit of pretraining on this small corpus was limited": the non-pretrained model trailed only slightly. The text gives no accuracy numbers for this benchmark.
- **Interpretable drivers (mESC differentiation, 48 h vs 52 h, held out from pretraining).** Accuracy and F1 were about 0.96. Integrated-Gradients attribution ranked Pou5f1, Jdp2 and Mbd3 highly. Wilcoxon DE analysis and scANVI attribution did not prioritise these genes.
- **"Time-reversed" fate prediction (mouse embryo Slide-seq).** Models were trained on mature neural tube (2,288 beads) vs somites (616) and tested on tailbud progenitors (278 presomitic, 149 neuromesodermal). scDynOmics reached accuracy 0.78 and macro F1 0.75, against 0.73 and 0.72 for CoSpar. CellRank performed poorly. GO enrichment of top features matched lineage expectations.
- **Perturbation (Tbx6 KO Slide-seq).** After training on wild-type somite vs neural tube beads, the pretrained model placed predicted "ectopic neural tube" beads bilaterally, where somites would be. XGBoost, the non-pretrained model, scANVI and CoSpar gave sparse or spatially scattered predictions. The pretrained model uniquely prioritised Meis2 and Ddx3x.

## Methods / evidence

Corpus: 5,912,810 raw mouse multiome profiles were collected and 752,155 kept after QC (minimum detected genes lowered to 100). The paper says cells "passing quality control in at least one modality" were retained, so not every pretraining cell need have both modalities passing QC. RNA is TPM + log. ATAC promoter counts are divided by the number of TSSs per gene, then CPM + log. Values are binned to tokens. Pretraining: 8 × H100, AdamW, batch 240, cosine restarts from 5 × 10⁻⁵. The mouse model ran 10 epochs (~30k steps, ~24 h) and the human model 100 epochs (~20k steps, ~15 h). Fine-tuning freezes the encoder and adds adapters twice per layer (rank 4–8) plus an MLP head. One 10-fold Zheng68k fine-tune took 74 ± 5 min on a consumer RTX 5090. Code: github.com/KlughammerLab/scDynOmics (also on PyPI).

Weight: the evaluations are classification tasks plus attribution case studies. There is no clustering or integration benchmark, no cross-modal translation and no multimodal baseline such as MultiVI or GLUE. Several headline comparisons are ties (scANVI on gastrulation) or are shown only in figures (Zheng68k). The biology claims rest on attribution rankings checked against literature rather than on experiments. (synthesis)

## Limitations

**Authors' own:**
- Pretraining used only paired multiome data, which caps corpus size. They plan to add RNA-only atlases recast as spliced/unspliced "multiomics".
- Gene vocabularies are species-specific, which blocks cross-species transfer. An ortholog-aware tokenisation is proposed.
- Cells are modelled as independent, ignoring tissue context.
- The model still lacks hardware-level attention kernels (FlashAttention, SAGEAttention).

**Reviewer notes:** (at most three, each marked `(synthesis)`)
- Reducing ATAC to one promoter value per gene discards distal enhancers and most peaks. The "multiomics" signal is promoter accessibility only, so claims about chromatin regulation are limited to what promoters carry. (synthesis)
- The abstract claims scDynOmics "outperforms existing single-cell foundation models by a large margin". The main text gives no numbers for that comparison, and the foundation-model baselines were tested only on Zheng68k. (synthesis)
- The pretrained vs non-pretrained gaps are small (0.82 vs 0.78 on gastrulation; "only slightly" on Zheng68k). Most of the performance may come from the architecture rather than from multiome pretraining. (synthesis)

## Surprising or load-bearing bits

- **Promoter ATAC as "unspliced RNA".** Treating chromatin opening as an earlier time point of expression, and then swapping in spliced/unspliced counts at fine-tuning, is an unusual idea. It worked modestly: multimodal fine-tuning gave 0.82, against 0.80 for total RNA alone.
- **Small and cheap.** At about 80 M parameters with ~750k pretraining cells, this model is far smaller than CELLxGENE-scale foundation models. The paper's case rests on efficiency and interpretability more than on scale. (synthesis)
- **Mouse-only main model.** It is the only RNA + ATAC model in this batch pretrained on mouse, and the only one that collapses ATAC to gene-level features. (synthesis)

## Concepts touched

- [[single-cell-foundation-model]] — a whole-coding-genome Linformer foundation model with TF-guided attention and adapter fine-tuning.
- [[gene-regulatory-network]] — the low-rank latent space is motivated by the number of TF regulons; attribution yields STRING-reconstructed regulons.
- [[joint-single-cell-multi-omics]] / [[multimodal-integration-methods]] — pretrained on paired RNA + promoter-accessibility multiome from SHARE-seq, SNARE-seq, sci-CAR, Paired-seq, ISSAAC-seq and 10x Multiome.
- [[cell-type-annotation]] — Zheng68k and gastrulation benchmarks against scBERT, Geneformer, CellFM and scANVI.

## Connections to other sources

- Pretraining data include SHARE-seq ([[ma-2020-share-seq]]) and several other joint RNA + ATAC protocols.
- Cites [[liu-2025-scarf]] as a state-space (Mamba) alternative for long inputs. The other RNA + ATAC foundation models in this ingest, [[li-2026-clm-x]] and [[liu-2025-scmomer]], keep peak-level ATAC; scDynOmics collapses it to genes. (synthesis)
- RNA foundation-model context: [[cui-2024-natmethods]] (scGPT, cited for its attention-kernel optimisations).
- Integration context: [[ashuach-2023-multivi]], [[cao-2022-glue]], [[gong-2021-cobolt]], [[argelaguet-2020-mofa-plus]], [[stuart-2021-natmethods]], [[xiao-2024-multiomics-benchmark]].

## Open questions

- Would distal peak features, for example through a peak-to-gene linkage layer, improve the TF-encoder design, or does the gene-level input format rule them out? (synthesis)
- Does pretraining on RNA-only atlases recast as spliced/unspliced pairs, as the authors propose, match the benefit of real multiome pretraining? (synthesis)
- Are the Pou5f1/Jdp2/Mbd3 and Meis2/Ddx3x attributions stable across random seeds and fine-tuning folds? (synthesis)

## Related

- [[single-cell-foundation-model]] · [[multimodal-integration-methods]] · [[gene-regulatory-network]] · [[ma-2020-share-seq]] · [[liu-2025-scarf]] · [[li-2026-clm-x]] · [[liu-2025-scmomer]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/sequence-models-and-foundation-models]]
