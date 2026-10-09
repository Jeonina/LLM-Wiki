---
type: summary
title: "Liang et al. 2025 — scDNAm-GPT Captures Genome-wide CpG Dependencies in Single-cell DNA methylomes to Revolutionize Epigenetic Analysis"
source: "[[00-Sources/papers/scDNAm-GPT Captures Genome-wide CpG Dependencies in Single-cell DNA methylomes to Revolutionize Epigenetic Analysis.pdf]]"
source_quality: full
source_sha256: "3b61d86db3e0c2d3afaf86998e82831ed066c64313e14be0e4d4e6b82aa434d5"
source_kind: paper
author: "Chaoqi Liang, Peng Ye, Hongliang Yan, Peng Zheng, Jianle Sun, Yanni Wang, … Wangmeng Zuo, Lei Bai, Wanli Ouyang, Jia Li (corresponding)"
published: 2025-02 (clipped text = bioRxiv version posted 2025-11-28)
ingested: 2026-10-08
doi: "10.1101/2025.02.19.638959"
journal: "bioRxiv preprint"
tags: [scDNAm-GPT, single-cell-methylation, scWGBS, foundation-model, Mamba, state-space-model, CpG-tokenization, cross-attention, cell-type-annotation, trajectory-inference, deconvolution, cfDNA, gene-expression-prediction, preprint-text]
entities: []
concepts: ["[[single-cell-foundation-model]]", "[[genomic-tokenization]]", "[[cell-type-annotation]]", "[[trajectory-inference]]", "[[scbs-seq]]", "[[cis-regulatory-element]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/dna-methylation]]"]
---

**Citation:** Liang et al. (2025) — *scDNAm-GPT Captures Genome-wide CpG Dependencies in Single-cell DNA methylomes to Revolutionize Epigenetic Analysis* — *bioRxiv preprint*. [DOI](https://doi.org/10.1101/2025.02.19.638959)

# Liang 2025 — scDNAm-GPT

> **Version note:** the clipped text is the bioRxiv version posted 28 November 2025.
>
> scDNAm-GPT is a foundation model **pretrained on single-cell whole-genome bisulfite data**: about 1 million cells (≈400,000 mouse brain, ≈600,000 human cells from various tissues), about 1.2 trillion CpG tokens, about 1.2–1.3 million covered CpGs per cell on average. Each covered CpG becomes a CpG-centred 6-mer "XXC(M)GXX" token. Methylated and unmethylated versions are mixed by the CpG's methylation rate (a "fuzzy" embedding), so bulk data can be fed in too. A stack of 8 Mamba (selective state-space) blocks reads the whole cell's CpGs as one sequence, up to about 20 million tokens. Pretraining is causal "next fuzzy token" prediction. For downstream tasks, a cross-attention head lets the final [SEP] state attend to every CpG. The authors report cell-type classification on four unseen datasets (average accuracy 83.7%), prediction of gene expression from methylation in colorectal cancer, pseudotime in early embryos, and deconvolution of simulated bulk and cfDNA samples. Many evaluations are small, and several key comparisons are only against weak or ablated baselines.

## Key claims

- **Pretraining data.** Mouse brain atlases (Liu et al. 2021, 2023), human brain (Tian et al. 2023) and a human-body single-cell 3D genome / methylation atlas (Zhou et al. 2025 preprint), described as 35 tissues and cell types across human and mouse.
- **Tokenisation choice.** CpG-centred 6-mers gave the most flanking DNA per MB of memory. Memory per token rose sharply above 6-mer as the vocabulary grew (Fig. S1).
- **Mamba beats a transformer backbone, and cross-attention adds more.** All backbones were pretrained on the same 1M cells. On adult human brain classification, Mamba exceeded 70% accuracy, F1 and recall, about 15% above a transformer. Adding the cross-attention head reached over 80%, about another 15%. Mamba inference was under 2 seconds per cell for more than 10 million CpGs and scaled linearly. Transformer latency rose steeply with length. At equal compute, Mamba reached lower perplexity.
- **Cell-type classification.** Accuracy was 96.8% on adult human brain (15 types, 116,643 training cells; this dataset was in the pretraining corpus). On unseen datasets: 87.1% human early embryo (10 stages, 195 training cells), 81.9% mouse early embryo (14 types, 168 cells), 80.5% colorectal cancer (5 lesion classes, 895 cells), 85.2% developing human brain (9 types, 4,096 cells).
- **Pretraining and depth both matter.** Average accuracy on the four unseen datasets was 83.66% with pretraining and 60.69% without it. On developing brain, the gap was 85.15% vs 26.31%. The 4-layer model reached 77.86%.
- **Expression from methylation.** On about 600 colorectal-cancer cells with paired scDNAm and scRNA-seq (7:3 split), the fine-tuned model predicted lesion-level expression of the top 1,000 variable genes with PCC 0.95. Per-cell PCC for *MALAT1* was 0.77. Genes that varied more across lesions were predicted better.
- **In-silico CpG effects.** For each CpG within 0.17 Mb of *MALAT1*, the model was given methylated and unmethylated versions and the predicted change in expression was recorded. The resulting effect profile tracked H3K27ac signal from colorectal cancer, and high-effect sites overlapped HiChIP/Hi-C contacts. These comparisons are visual (IGV tracks).
- **Pseudotime.** On human (280 cells) and mouse (240 cells) oocyte-to-blastocyst data, diffusion pseudotime on layer-aggregated embeddings matched stage order better than methylation ratios did (Kendall τ, Spearman ρ). The model had been fine-tuned on cell-type labels, not on time.
- **Layer-wise attention.** Top-1% attention CpGs overlapped little between classes in layers 1–4 (Jaccard < 0.05) and more in layers 5–8. Early layers favoured TSSs; later layers also covered enhancers and repeats. In embryos, layer-8 top regions were enriched for stage-matched TF motifs (GATA2/4/6 in ICM; OTX2 and PITX1 at 8-cell; CTCF and TFAP2C in hESC). High-attention, low-methylation (<0.2) regions were enriched for H3K4me3. High-attention, high-methylation (>0.8) regions were depleted of it.
- **Reference-free deconvolution of simulated bulk.** Mixtures were built from 0–10 cells of each of five human brain neuronal or glial types, keeping per-cell depth variation. Predicted proportions correlated with truth at R 0.84–0.93 for the three types shown, average 0.88 in the text. RefFreeCellMix, EDec and MeDeCom were near zero (|r| < 0.05).
- **cfDNA tumour signal, zero-shot.** A model fine-tuned on scWGBS of normal vs primary colorectal tumour cells was applied directly to plasma cfDNA. It separated healthy from colorectal-cancer plasma across stages, and also lung-cancer plasma. The reference-based MethylBERT failed to separate several stage I and III cases. This evidence is UMAPs and boxplots, with no AUC.

## Methods / evidence

Token embedding t_i = α_i·emb(methylated token) + (1−α_i)·emb(unmethylated token), with α the methylation rate (0 or 1 for a single read in a single cell). Loss: cross-entropy for the next CpG token, split between methylated and unmethylated labels by α. Backbone: 8 Mamba blocks (depthwise conv, selective SSM, gating, LayerNorm). Methods describe this as "approximately 1M parameters". Fine-tuning: the [SEP] hidden state queries all CpG states through cross-attention. Training: 30,000 steps, learning rate 3e-5, batch size 16, fp16/fp8 on H200 GPUs. Maximum sequence length is 21M tokens in fp16 and 35M in fp8. Evaluation uses accuracy, F1, recall, perplexity, Kendall τ, Spearman ρ and PCC. Code and weights: github.com/ChaoqiLiang/scDNAm-GPT (MIT).

Weight: the main architecture claims compare scDNAm-GPT only with its own ablations (transformer, plain Mamba, no pretraining, 4 layers). There is no external single-cell methylation baseline for classification, such as bin-based PCA/clustering pipelines, scDMV-type tools or MethylGPT/CpGPT. The unseen datasets are small (72–1,759 test cells). Expression prediction uses about 180 test cells. The cfDNA result is qualitative. (synthesis)

## Limitations

**Authors' own:**
- Pretraining data are heavily weighted toward brain, which may limit how well the model captures other organs and diseases.
- No other omics (scRNA-seq, scHi-C, scCUT&Tag) are integrated.
- No patient metadata or clinical variables are used.
- Learning causal relations needs time-series and perturbation data.

**Reviewer notes:**
- The paper calls the deconvolution "reference-free", but the model is fine-tuned on labelled single cells of the same types it then deconvolves. The labelled cells act as a reference, so the comparison with truly unsupervised methods (RefFreeCellMix, EDec, MeDeCom) is not like-for-like. (synthesis)
- Numbers drift within the text: 1.2 vs 1.24 trillion tokens, 1.2 vs 1.3 million CpGs per cell, average deconvolution r 0.88 (text) vs 0.84 (Fig. S4 caption). A model that handles 20M-token inputs is described as having "approximately 1M parameters" in the backbone. (synthesis)
- "Attention" here is the single cross-attention head of the [SEP] query, plus per-layer analyses whose exact definition for Mamba layers is not given in Methods. Interpretability claims rest on enrichment of the top 1% of sites. (synthesis)

## Surprising or load-bearing bits

- **No binning.** Every covered CpG in a cell is a token, so the model avoids the 100-kb or 5-kb bins that standard single-cell methylation pipelines use. This is the main design difference from bin-based scBS-seq analysis. (synthesis)
- **State-space models make whole-cell inputs feasible.** Inputs of 10–35 million tokens per cell are far beyond transformer context lengths. The authors frame this as the key enabler.
- **Pretraining matters most where labels are few.** On the developing-brain set, accuracy without pretraining was 26%, against 85% with it.
- **Single-cell fine-tuning, cfDNA inference.** A classifier trained on tumour vs normal single cells transfers zero-shot to plasma cfDNA. If confirmed with proper metrics, this is a route from single-cell atlases to liquid biopsy. (synthesis)

## Concepts touched

- [[single-cell-foundation-model]] — the first foundation model in this wiki pretrained directly on single-cell methylomes.
- [[genomic-tokenization]] — CpG-centred 6-mer tokens with methylation state, mixed by methylation rate ("fuzzy" tokens).
- [[cell-type-annotation]] — fine-tuned classification on five scWGBS datasets.
- [[trajectory-inference]] — diffusion pseudotime on embeddings of early embryos.
- [[scbs-seq]] — the input data type (scWGBS / snmC-seq-style data).
- [[cis-regulatory-element]] — high-attention CpGs enrich at TSSs and enhancers and match H3K4me3 and H3K27ac.

## Connections to other sources

- Bulk methylation foundation models it positions against: [[delimacamillo-2024-cpgpt]] and [[ying-2024-methylgpt]]. Neither is used as a baseline. (synthesis)
- Earlier deep single-cell methylation model: [[angermueller-2017-genomebiol]] (DeepCpG). Imputation benchmark context: [[liang-2026-scmeth-imputation-benchmark]].
- Pretraining data include the mouse brain methylome and 3D atlas: [[liu-2023-mouse-brain-methylome-3d]]. The scWGBS lineage is cited through [[farlik-2015-scwgbs]] and [[mulqueen-2018-sci-met]].
- The paper cites [[nguyen-2023-hyenadna]] as prior long-sequence genomic modelling. Its Mamba backbone also parallels the Mamba-based DNA language model [[schiff-2024-caduceus]], which it does not cite. (synthesis)
- Single-cell transcriptomic foundation-model template: [[cui-2024-natmethods]] (scGPT).

## Open questions

- How does scDNAm-GPT compare with bin-based pipelines and with CpGPT fine-tuned on the same scWGBS datasets? (synthesis)
- Do the cfDNA results hold up as AUCs on held-out patient cohorts, and against reference-based tools beyond MethylBERT? (synthesis)
- The pretraining corpus is brain-heavy. How well does the model do on non-brain, non-embryo tissues, such as immune or tumour cells outside colorectal cancer? (synthesis)

## Related

- [[delimacamillo-2024-cpgpt]] · [[ying-2024-methylgpt]] · [[angermueller-2017-genomebiol]] · [[liu-2023-mouse-brain-methylome-3d]] · [[scbs-seq]] · [[single-cell-foundation-model]] · [[40-Topics/dna-methylation]] · [[40-Topics/sequence-models-and-foundation-models]]
