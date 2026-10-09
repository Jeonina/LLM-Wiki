---
type: summary
title: "Liu et al. 2025 — CLM-access: A Specialized Foundation Model for High-dimensional Single-cell ATAC-seq analysis"
source: "[[00-Sources/papers/CLM-access- A Specialized Foundation Model for High-dimensional Single-cell ATAC-seq analysis.pdf]]"
source_quality: full
source_sha256: "442fe0fff2b233945fb4d6ca9cb4e859f9e298108f51e1cf2b285b4f6023ee79"
source_kind: paper
author: "Ziqiang Liu, Bowen Li, Zhenyu Xu, Yantao Li, Junwei Zhang, Chulin Sha (corresponding), Xiaolin Li (corresponding)"
published: 2025-08-12
ingested: 2026-10-08
doi: "10.1101/2025.08.10.669570"
journal: "bioRxiv preprint"
tags: [CLM-access, scATAC-seq, foundation-model, cell-language-model, transformer, BERT, patch-tokenization, masked-peak-reconstruction, batch-correction, cell-type-annotation, RNA-prediction, multimodal-integration, preprint-text]
entities: []
concepts: ["[[single-cell-foundation-model]]", "[[genomic-tokenization]]", "[[scatac-seq]]", "[[cell-type-annotation]]", "[[batch-effect]]", "[[multimodal-integration-methods]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/single-cell-atac-seq]]"]
---

**Citation:** Liu et al. (2025) — *CLM-access: A Specialized Foundation Model for High-dimensional Single-cell ATAC-seq analysis* — *bioRxiv preprint*. [DOI](https://doi.org/10.1101/2025.08.10.669570)

# Liu 2025 — CLM-access

> CLM-access is a BERT-style "cell language model" **pretrained on single-cell ATAC-seq**: about 2.8 million human cells mapped onto one reference of about 1.15 million cCREs. Using every cCRE as a token would be too large, so cCREs are sorted by genomic position and split into 2,000 fixed patches. Each patch is one token. Its embedding is the sum of a patch-ID embedding and a linear projection of the patch's binarised peak values. An 8-block transformer (256-d, 8 heads, about 12M parameters; about 20M in total) is trained to reconstruct masked peak values with peak-level binary cross-entropy. The model sees no DNA sequence. The paper's main contribution is a set of ablations on what makes scATAC pretraining work: binarisation, per-peak loss, and masking values only. Fine-tuned, the model beats a few baselines on cell-type annotation, RNA prediction and integration. The paper is short (NeurIPS-style), and dataset details, fine-tuning settings and the integration figures are in a supplement that is not part of the clipped text.

## Key claims

- **Naive scRNA-style training fails.** Using only accessible peaks as tokens, or only highly variable peaks, could not train the model.
- **Binarisation is essential.** With patch-level summed signal, ARI stayed at 0.0001–0.0033 for every patch count. Binarised input reached ARI 0.0113 (1k patches) to 0.1688 (5k patches) and 0.2397 with TAD-defined patches (about 14k). These are pretraining-stage scores on a 370,000-cell scCLIP-processed set.
- **Peak-level loss beats patch-level loss.** Binarising each peak and applying BCE per peak gave the best scores at 2,000 patches (ARI 0.2511, NMI 0.5813), better than patch-level MSE or BCE. A 2,000-token input was chosen as the trade-off between accuracy and cost.
- **Mask values only, not tokens.** Masking both patch tokens and peak values collapsed performance (ARI ≤ 0.0048). Masking only peak values gave the scores above.
- **Scale.** Pretraining on CATlas (1.3M cells) gave NMI 0.5881 and ARI 0.2628, against 0.5813 and 0.2510 on the scCLIP set (0.33M). The medium model was best (NMI 0.6618, ARI 0.3024). The large model was slightly worse, which the authors read as overfitting given the data size.
- **Batch correction.** On 4 PBMC scATAC datasets, zero-shot embeddings beat PCA and Harmony, and fine-tuning with batch labels improved them further. Results are figure-only.
- **Cell-type annotation.** On GSE219281 (~70k cells), accuracy was 0.7635 and macro-F1 0.5437, against scATAnno (0.7283, 0.3610) and Cellcano (0.7064, 0.3434). On GSE181346 (~70k cells), accuracy was 0.7470 and macro-F1 0.6742, against 0.6834/0.5473 and 0.6286/0.3955.
- **RNA prediction.** On a paired RNA/ATAC dataset, Pearson was 0.9175 and RMSE 1.4185, against BABEL (0.9101, 1.5316) and MultiVI (0.8845, 3.5755).
- **Multimodal integration.** Combining predicted and measured RNA gave better cell-type identification than SnapATAC2 on ATAC alone (figure-only).

## Methods / evidence

Input: cell × cCRE matrix over about 1.15M cCREs, binarised. cCREs are ordered by chromosome position and cut into 2,000 patches, each padded to a fixed length L. Embedding: patch-token embedding (1,998 cCRE-patch markers plus 4 special tokens) plus a linear peak-value embedding, 256-d, with a [CLS] token. No positional encoding is described. Encoder: 8 transformer blocks with FlashAttention v2. Decoder: one fully connected layer maps embeddings to masked peak values, trained with BCE. Pretraining: 15 epochs, batch size 8. Code: github.com/HIM-AIM/CLM-access.

Weight: the pretraining ablations are informative and fully tabulated, but they are scored on the authors' own split of a single dataset. Downstream benchmarks use few baselines (no scATAC foundation model, scBasset or SCALE), give dataset identities only as GEO accessions, and do not describe how fine-tuning data were split. (synthesis)

## Limitations

**Authors' own:**
- Only human data were used. Cross-species cCRE unification is future work.
- The model uses only chromatin accessibility, and attention works between patches, not individual cCREs. Extending attention to the cCRE level is planned.
- Adding other modalities such as RNA-seq to build multi-omic "cell sentences" is future work.

**Reviewer notes:**
- Table 4 looks mislabelled. The "all data (2.8M)" row gives NMI 0.2785 and ARI 0.6236, the reverse order of every other row and the same numbers as the "small model" row. So the claimed roughly linear gain from data size is not cleanly supported. The text also calls the annotation metric "micro-averaged F1" while the table reports macro-F1, and refers to a "ranking embedding" layer that the method does not use. (synthesis)
- Patches are fixed blocks of consecutive cCREs, not biological units. Attention therefore links arbitrary genomic chunks, and any cCRE outside the 1.15M reference is lost. TAD-based patches scored best at pretraining but were not used in the final model. (synthesis)
- Pretraining ARIs of about 0.25–0.30 are low in absolute terms. The downstream gains depend on supervised fine-tuning. (synthesis)

## Surprising or load-bearing bits

- **Binarise, then predict each peak.** The jump from ARI ≈ 0.003 (summed, patch-level) to ≈ 0.25 (binarised, peak-level) is the clearest practical lesson for anyone building an scATAC foundation model. (synthesis)
- **Masking tokens kills training.** Hiding patch identity along with values leaves the model nothing to anchor on, which differs from standard BERT practice.
- **Medium beats large** at 2.8M cells. Data, not parameters, was the limit at this scale.

## Concepts touched

- [[single-cell-foundation-model]] — a BERT-style scATAC cell language model with patch tokens.
- [[genomic-tokenization]] — fixed patches of position-ordered cCREs as tokens; ablations on patch size and TAD patches.
- [[scatac-seq]] — the data type; uses a 1.15M-cCRE reference rather than filtered variable peaks.
- [[cell-type-annotation]] — beats scATAnno and Cellcano on two ~70k-cell datasets.
- [[batch-effect]] — zero-shot and fine-tuned integration across four PBMC datasets.
- [[multimodal-integration-methods]] — RNA prediction compared with BABEL and MultiVI, and integration using predicted RNA.

## Connections to other sources

- Other scATAC foundation models in this ingest: [[leroy-2025-atacformer]] (region-ID tokens, ELECTRA objective), [[wu-2025-epifoundation]] (peak-to-gene alignment) and [[li-2026-epizoo]] (sequence-aware). None of them is benchmarked against CLM-access here. (synthesis)
- Extended to multi-omics by [[li-2026-clm-x]], which reuses the same patch tokenisation and Human-scATAC corpus.
- Baselines and related tools: [[ashuach-2023-multivi]] (MultiVI), [[zhang-2024-snapatac2]], [[yuan-2022-scbasset]] and [[xiong-2019-scale]] (cited, not benchmarked).
- Pretraining atlas lineage: CATlas, from the human single-cell chromatin atlas. scRNA foundation-model template: [[cui-2024-natmethods]].

## Open questions

- Do the TAD-based patches (best pretraining scores) also do better downstream, and why were they not used in the final model?
- How does CLM-access compare with Atacformer, EpiFoundation or EpiAgent on a shared benchmark? (synthesis)
- What is the corrected Table 4, and does performance in fact rise with pretraining data size?

## Related

- [[leroy-2025-atacformer]] · [[wu-2025-epifoundation]] · [[li-2026-epizoo]] · [[li-2026-clm-x]] · [[scatac-seq]] · [[single-cell-foundation-model]] · [[40-Topics/single-cell-atac-seq]] · [[40-Topics/sequence-models-and-foundation-models]]
