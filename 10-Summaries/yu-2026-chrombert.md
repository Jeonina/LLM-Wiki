---
type: summary
title: "Yu et al. 2026 — ChromBERT: A foundation model for learning interpretable representations for context-specific transcriptional regulatory networks"
source: "[[00-Sources/papers/ChromBERT- A foundation model for learning interpretable representations for context-specific transcriptional regulatory networks.pdf]]"
source_quality: full
source_sha256: "d646f32101276ee6f722c9319c374a6384a18026eaee7de909eabf1c245dc8dd"
source_kind: paper
author: "Zhaowei Yu, Dongxu Yang, Qianqian Chen, Yuxuan Zhang, Zhanhao Li, Yucheng Wang, … , Yong Zhang (lead contact, corresponding)"
published: 2026-04-08
ingested: 2026-10-12
updated: 2026-10-12
doi: "10.1016/j.xgen.2025.101130"
journal: "Cell Genomics 6, 101130"
tags: [ChromBERT, foundation-model, ChIP-seq, cistrome, Cistrome-DB, transcription-regulators, histone-modifications, DNase-seq, ATAC-seq, masked-pretraining, BERT, transformer, cistrome-imputation, gene-regulatory-network, eQTL, STARR-seq, scGPT, prompt-fine-tuning, bulk-pretraining, histone-gap]
entities: ["[[rui-jiang]]"]
concepts: ["[[single-cell-foundation-model]]", "[[chip-seq]]", "[[gene-regulatory-network]]", "[[chromatin-accessibility]]", "[[transcription-factor-motif]]", "[[cis-regulatory-element]]", "[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[topologically-associating-domain]]", "[[micro-c]]", "[[scatac-seq]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/histone-modifications]]"]
---

**Citation:** Yu et al. (2026) — *ChromBERT: A foundation model for learning interpretable representations for context-specific transcriptional regulatory networks* — *Cell Genomics* 6, 101130 (published April 8, 2026). [DOI](https://doi.org/10.1016/j.xgen.2025.101130)

# Yu 2026 — ChromBERT

> ChromBERT treats co-binding across ChIP-seq tracks as a language. Each 1-kb genomic bin is a "sentence", and each word is the binding status of one Cistrome profile in that bin. The model is a BERT-style encoder pretrained to recover masked binding statuses from the other profiles in the same bin. The corpus is **Cistrome-Human-6K: 6,391 bulk profiles (ChIP-seq, DNase-seq, ATAC-seq) covering 991 transcription regulators, 76 histone modifications and chromatin accessibility**, pooled across cell types from over 100 tissues. The model takes **no DNA sequence**. The pretrained embeddings are cell-type-agnostic. Cell-type context enters only at fine-tuning, through prompts (DNase-seq embeddings, scGPT transcriptome embeddings, DNABERT-2 variant embeddings) or task labels (eQTLs, STARR-seq, expression or accessibility changes). The authors then rank regulators by how much their fine-tuned embeddings shift between two groups of regions with different outcomes. ChromBERT is the closest thing in this wiki to a foundation model pretrained with histone-mark channels. But histone marks are a small labelled subset of a corpus built around transcription regulators, all of it is bulk, and the histone cistromes are removed or ignored in several downstream analyses.

## Key claims

- **Pretraining corpus.** The authors collected all human ChIP-seq, DNase-seq and ATAC-seq data from the Cistrome Data Browser and filtered them by QC metrics (at least 4 of 5), peak counts, genome coverage and one dataset per regulator per cell type. This left 6,391 cistromes "for 991 transcription regulators, 76 histone modifications, and chromatin accessibility". The data come from over 100 tissues and three sources: cell lines, primary cancer cells and naturally occurring primary cells. Most cell types have cistromes for fewer than 10 regulators, and most regulators have cistromes in fewer than 4 cell types (Figure S1C). The pooled data cover M = 1,073 "regulators".
- **Input and objective.** The signal (RPM) of every cistrome is averaged over consecutive 1-kb hg38 bins. ENCODE blacklist regions are removed, and only bins with a peak in more than two cistromes are kept, giving 2,137,894 bins. Each cistrome's signal is cut into five binding-status tokens: three "binding" levels above the 10th percentile of peak-bin signal and two "non-binding" levels. A position embedding encodes cistrome identity and a token embedding encodes status. 15% of statuses are masked with BERT's 80/10/10 rule and reconstructed by a two-layer MLP under focal loss (γ = 2).
- **Pretrained embeddings carry regulatory structure.** TRN embeddings cluster by ChromHMM state on chromosome 1 and separate promoter-proximal from distal accessible regions. Similarity is higher within the same TAD and between bins in Micro-C contact. A CNN that combines embedding similarity with low-resolution Hi-C imputed hESC Micro-C and transferred to HFF cells. Regulator-embedding similarity tracks BioPlex 3.0 protein–protein interaction and MSigDB co-membership. RNF2 sits near PCGF2 in repressive regions and near EP300/MYC in active regions. Shuffling the input co-binding patterns abolishes these associations.
- **Cistrome imputation in unseen cell types.** Prompt-enhanced fine-tuning concatenates a regulator embedding with a cell-type prompt. The DNase prompt is ChromBERT's own pretrained embedding of that cell type's DNase-seq cistrome. The RNA prompt is a 512-d scGPT cell embedding. ChromBERT-D, fine-tuned on 104 cistromes of 29 regulators in 22 cell types, reached a mean AUPRC of 0.554 on 241 held-out cistromes. The baseline, regulator-specific candidate peaks weighted by DNase signal, reached 0.271. ChromBERT-D scored 0.659 against Avocado's 0.514 on 57 cistromes, beating it on 93.0% of them. It also classified cell-type-specific binding sites with matched accessibility (186 cell-type pairs, 24 regulators). ChromBERT-R (RNA prompts) was less accurate overall but helped for EZH2 and REST. Concatenating both prompts did not beat DNase alone.
- **Single-cell imputation.** The authors swapped bulk RNA prompts for scGPT embeddings of single cells from a 10x PBMC multiome dataset (9,493 of 11,898 cells kept). ChromBERT-R beat a motif plus imputed-scATAC (scOpen) baseline for eight regulators in B cells, scored against GM12878 ChIP-seq. It also showed cell-specific predictions, scored against scATAC-inferred motif accessibility. T-cell clusters were dropped because scGPT embeddings could not separate them.
- **eQTL fine-mapping.** With a DNABERT-2 sequence prompt for each variant's 1-kb window, fine-tuned ChromBERT classified causal (PIP > 0.9) versus non-causal eQTLs with a mean AUROC of 0.828 across 49 tissues. Enformer scored 0.770, DNABERT-2 alone 0.788 and ChromBERT without pretraining 0.804. The DNase-seq cistrome showed the largest embedding shift between causal and non-causal variants. A case study links rs17079281 to a gained YY1 motif that represses *DCBLD1* in lung.
- **Enhancer activity and cofactor dependence.** On HCT116 STARR-seq, ChromBERT beat Enformer, DNABERT-2 and the non-pretrained model, with histone and accessibility cistromes excluded. Embedding shifts after EP300/CREBBP depletion flagged FOSL1 and JUND as EP300-dependent. BRD4 showed little shift, and the BRD4-depletion STARR-seq data confirmed its weak dependence on EP300.
- **EZH2 dual roles.** Classifying hESC EZH2 peaks as classical (with H3K27me3) or non-classical (without) gave a repressive module and an activator module that includes E2F1 and STAT3. H3K27me3 cistromes were omitted from the input for this analysis because they dominated the signal.
- **Drivers of cell-state change.** The model was fine-tuned on pairwise pseudobulk expression and accessibility changes among five PBMC cell types, then regulators were ranked by embedding shift. 37 of 84 identified key regulators had been reported for the matching cell type, for example BACH2, PAX5, BCL6 and IRF4 in B cells and CEBPA, CEBPB and SPI1 in monocytes. Many of these were missed by differential expression, motif enrichment and SCENIC+. Across five transdifferentiation paradigms the method recovered nearly all known drivers. MEF2C was missed, and FOXA3 has no cistrome in the corpus. On an ATAC-seq perturbation dataset it identified the perturbed regulator in 3 of 5 cases.

## Methods / evidence

Architecture: input embedding, 8 transformer blocks (768-d, 8 heads, FlashAttention-2, sequence length P = 6,391) and task-specific decoders. Pretraining: 100 epochs, AdamW, peak learning rate 1e-4 with 10% warm-up, batch 32 with 8-step gradient accumulation, about 23 days on four A800 80 GB GPUs. Cistrome-level embeddings are averaged per regulator into regulator embeddings, so each bin is an M × 768 matrix. Fine-tuning freezes the early encoder layers and trains the last N blocks plus a decoder. Interpretation uses 1 − cosine similarity of regulator embeddings averaged over two region sets, not attention weights. The authors argue attention maps are too layer- and head-dependent to compare. Released: human models at 200 bp, 1, 2 and 4 kb, a mouse 1-kb model, the Cistrome-Human-6K dataset on Hugging Face, and code on GitHub and Zenodo.

Weight: the paper benchmarks against Avocado, a DNase-plus-candidate-peak baseline, Enformer, DNABERT-2, SCENIC+ and a non-pretrained ChromBERT, and the gains over the non-pretrained model are moderate (e.g. AUROC 0.828 vs 0.804 for eQTLs). Most key-regulator results are checked against known drivers from the literature, which favours well-studied factors. The source PDF includes the supplementary figure legends, but Tables S1–S4 are not in it, so the exact split of the 6,391 cistromes into regulator, histone and accessibility profiles cannot be read from the source. (synthesis)

## Limitations

**Authors' own:**
- The pretraining corpus covers cistromes for only about one thousand transcription regulators. Many regulators lack public ChIP-seq data and are not represented.
- Cell-type-specific cistromes are scarce, so tracks are pooled across cell types. This widens coverage but "blurs cell-type specificity". Larger ChIP-seq datasets with explicit cell-type metadata would allow cell-type-specific pretraining.
- Because of this pooling, the encoder "exhibits a limited capacity to generate variable TRN embeddings in response to specific inputs". Prompt-enhanced fine-tuning is the workaround.
- Aligning ChromBERT with other foundation models (DNA sequence, 3D chromatin, single-cell transcriptomics) is hard because each sits in its own latent space. The long-term aim is a multimodal model pretrained from scratch.
- Hyperparameters such as the number of transformer blocks and hidden size were not systematically optimised.
- Representation frequency of cell types and regulators varies. Performance was largely insensitive to it except for a few massively over-represented regulators.

**Reviewer notes:**
- The model is not single-cell. Pretraining uses bulk cistromes only. Single-cell data enter only as scGPT prompts, as pseudobulk fine-tuning targets or as evaluation ground truth, and single-cell imputation was tested on one PBMC dataset, with T cells excluded. (synthesis)
- Bins with peaks in two or fewer cistromes are dropped from pretraining, and the Hi-C task treats them as all-zero. The model therefore never sees most of the genome, including broad heterochromatin domains where repressive histone marks dominate. (synthesis)
- The interpretation method ranks regulators by embedding shift, and validation leans on recovering literature-known drivers. That supports plausibility but does not show causality for new candidates beyond the 3-of-5 perturbation check. (synthesis)

## Surprising or load-bearing bits

- **A ChIP-seq "language" with no DNA.** ChromBERT's vocabulary is cistrome identity × binding level. Sequence enters only as an optional DNABERT-2 prompt. That makes it orthogonal to sequence-to-function models: it learns which regulators co-occupy a bin, not why the sequence recruits them. (synthesis)
- **Accessibility is the strongest single signal.** In eQTL fine-mapping the DNase cistrome shifted most, and DNase prompts beat scGPT prompts for imputation. Even a model built around regulators leans hardest on accessibility.
- **Fine-tuning, not pretraining, does the interpretive work.** Known PBMC and transdifferentiation drivers ranked higher in the fine-tuned model than in the pretrained one.

**What this means for the histone gap.** The paper itself confirms that histone-modification ChIP-seq is in the pretraining corpus: Cistrome-Human-6K covers "991 transcription regulators, 76 histone modifications, and chromatin accessibility". So "no foundation model has histone data in pretraining" is false if bulk models count. But the paper never says how many of the 6,391 profiles are histone marks; that split is in Table S1, which is not in the source. The model is built and evaluated around transcription regulators. Histone and accessibility cistromes are excluded from the STARR-seq task. H3K27me3 is omitted from the EZH2 task. The PBMC and transdifferentiation driver rankings cover only the 991 transcription factors ("Epigenetic modifications were not considered in this analysis"). Every pretraining profile is bulk, and only bins with peaks in more than two cistromes are used. No single-cell histone data (scCUT&Tag, scChIP, sortChIC) appear anywhere in the paper. ChromBERT therefore narrows the claim to this: no foundation model is pretrained on **single-cell** histone-modification data, and no model treats histone marks as its main modality. (synthesis)

## Entities mentioned

- [[rui-jiang]] — thanked in the acknowledgements for comments on the research design.

## Concepts touched

- [[single-cell-foundation-model]] — a bulk-pretrained regulatory foundation model that reaches single cells only through scGPT prompts and pseudobulk fine-tuning.
- [[chip-seq]] — the pretraining corpus is about 6,000 Cistrome ChIP-seq (plus DNase/ATAC) profiles, discretised into five binding levels per 1-kb bin.
- [[gene-regulatory-network]] — "TRN embeddings" per bin, and regulator rankings by embedding shift; the authors propose explicit TRN reconstruction as future work.
- [[chromatin-accessibility]] — DNase/ATAC cistromes are both pretraining channels and the best cell-type prompt.
- [[transcription-factor-motif]] — ChromBERT is pitched against motif-centric methods; top-shift regulators have more motif presence and larger motif-affinity changes at causal eQTLs.
- [[cis-regulatory-element]] — embeddings cluster by ChromHMM state and predict STARR-seq enhancer activity.
- [[variant-effect-prediction]] — causal-eQTL classification across 49 tissues with a DNABERT-2 prompt.
- [[sequence-to-function-model]] — Enformer and DNABERT-2 are the sequence-based comparators.
- [[topologically-associating-domain]] / [[micro-c]] — embedding similarity is higher within TADs and at Micro-C contacts, and drives Micro-C imputation.
- [[scatac-seq]] — PBMC scATAC is used for pseudobulk accessibility targets and as motif-accessibility ground truth.

## Connections to other sources

- Histone-gap context: [[foroozandeh-2025-candi]] imputes bulk histone and accessibility tracks with a self-supervised transformer. ChromBERT is the other bulk model with histone channels, but its tokens are binary-like binding levels per cistrome, not continuous tracks, and histone marks are a minority. [[morenogonzalez-2025-schistone-imputation]] found no pretrained model to test on single-cell histone data, and ChromBERT does not change that. (synthesis)
- [[gao-2024-epigept]] predicts histone tracks from sequence plus TF expression, while ChromBERT takes histone tracks as input channels and no sequence. The two run in opposite directions. (synthesis)
- [[fu-2025-get]] pretrains on pseudobulk scATAC with motif features. ChromBERT pretrains on bulk ChIP-seq co-binding and uses scATAC only downstream. (synthesis)
- Sequence-based comparators and neighbours: [[avsec-2021-enformer]], [[zhou-2023-dnabert-2]], [[avsec-2026-alphagenome]], [[chen-2022-sei]].
- RNA prompt source: [[cui-2024-natmethods]] (scGPT).
- Key-regulator baseline that ChromBERT outperformed on PBMC drivers: [[bravo-2023-scenicplus]].

## Open questions

- How many of the 6,391 cistromes are histone-mark profiles, and which marks? The text gives 76 histone modifications but not their profile count. Table S1 or the Hugging Face dataset would settle it. (synthesis)
- The text gives 991 transcription regulators but M = 1,073 "regulators". The gap (82) presumably covers the histone-modification and accessibility entries (76 + a few accessibility types), but the paper does not spell this out. (synthesis)
- Would a ChromBERT-style model pretrained on single-cell CUT&Tag co-profiles (multi-mark per cell) work, given that per-cell, per-bin binding statuses would be far sparser? (synthesis)
- Do histone channels help or hurt? The authors drop them in several tasks. No ablation reports pretraining with versus without the 76 histone modifications. (synthesis)

## Related

- [[single-cell-foundation-model]] · [[chip-seq]] · [[gene-regulatory-network]] · [[foroozandeh-2025-candi]] · [[morenogonzalez-2025-schistone-imputation]] · [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/histone-modifications]]
