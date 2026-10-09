---
type: summary
title: "LeRoy et al. 2025 — Atacformer: A transformer-based foundation model for analysis and interpretation of ATAC-seq data"
source: "[[00-Sources/papers/Atacformer- A transformer-based foundation model for analysis and interpretation of ATAC-seq data.pdf]]"
source_quality: full
source_sha256: "6232554e878b8d789f297c73e4daade83ea382fe6d7bfef48118f07147f1b24a"
source_kind: paper
author: "Nathan J. LeRoy, Guangtao Zheng, Oleksandr Khoroshevskyi, Donald R. Campbell Jr, Aidong Zhang, Nathan C. Sheffield (corresponding)"
published: 2025-11-04
ingested: 2026-10-08
doi: "10.1101/2025.11.03.685753"
journal: "bioRxiv preprint"
tags: [Atacformer, CRAFT, scATAC-seq, foundation-model, transformer, ELECTRA, region-tokenization, genomic-intervals, BEDbase, Geneformer, contrastive-learning, fragment-files, cryptic-promoters, preprint-text]
entities: []
concepts: ["[[single-cell-foundation-model]]", "[[genomic-tokenization]]", "[[scatac-seq]]", "[[cis-regulatory-element]]", "[[multimodal-integration-methods]]", "[[batch-effect]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/single-cell-atac-seq]]"]
---

**Citation:** LeRoy et al. (2025) — *Atacformer: A transformer-based foundation model for analysis and interpretation of ATAC-seq data* — *bioRxiv preprint*. [DOI](https://doi.org/10.1101/2025.11.03.685753)

# LeRoy 2025 — Atacformer

> Atacformer is a transformer encoder **pretrained on single-cell ATAC-seq** that treats each cell as an unordered "bag" of accessible regions. Each region is a token drawn from a fixed vocabulary of 890,704 consensus regions. There is no DNA sequence input and **no positional encoding**. Pretraining uses ELECTRA-style replaced-token detection: 45% of tokens are swapped for random vocabulary regions, and the model predicts which were swapped. Context is 8,192 tokens. Because inputs are just intervals, the model can tokenise raw fragment files directly, skipping peak calling and the count matrix, and it can also read bulk BED files. Cell embeddings are mean-pooled region embeddings. The authors add a triplet-loss cell-type fine-tune (atacformer-ctft), a CLIP-style RNA–ATAC model with Geneformer (CRAFT), and a bulk BED fine-tune (atacformer-bb). Results are competitive clustering at high speed, cell-line prediction for bulk BED files, and the use of contextualised region embeddings to flag unannotated promoter-like regions ("icTSSs") that carry H3K4me3.

## Key claims

- **Pretraining corpus.** Described as 1.2 million cells and 10 billion tokens from 30 tissues, processed uniformly (CellRanger ATAC → SnapATAC2). 359 Leiden clusters were pseudo-bulked, peaks were called with MACS3, and the peak sets were merged into a consensus vocabulary.
- **Why ELECTRA, not masked-LM.** Masked-LM over about 890k tokens needs a softmax over the full vocabulary. Also, a cell's regions have no order, so masked-LM penalises right answers predicted "out of order". Replaced-token detection is a per-token binary task and avoids both problems.
- **Zero-shot clustering.** Tested on three datasets kept out of training (a pre-annotated Alzheimer's brain multiome set, a PBMC set simulated from ENCODE bulk ATAC, and 10x PBMC5k), against PCA, SnapATAC2, SCALE, EpiAgent and scEmbed. The base model underperformed on PBMC. Triplet fine-tuning on Luecken2021 PBMC raised ARI by about 15% on the PBMC sets. The base model did best on brain, which the authors attribute to the blood-only fine-tune. CRAFT performed well on all three. On PBMC5k, CRAFT had both the best clustering and the highest throughput (cells/s) of all methods.
- **Speed.** Atacformer was second fastest after scEmbed (the authors' earlier Word2Vec method). EpiAgent (1.5B parameters) and SCALE were slowest. Going from fragments to embeddings on a new 3,000-cell 10x brain dataset was faster than SnapATAC2 or ArchR, with Leiden clusters "comparable to or better resolved" (visual). From count matrices, Atacformer's tokenisation and embedding steps were about 2.5× faster than EpiAgent's. The abstract states an 80% end-to-end speed-up.
- **Robust to truncation.** With random sampling of tokens, clustering stayed stable down to small context windows and degraded sharply only below about 512 tokens (Fig. S5).
- **CRAFT.** Atacformer and Geneformer encoders were trained contrastively for 15 epochs on about 106,000 multiome cells. Nearest RNA neighbours of ATAC embeddings had the same cell type. A one-hidden-layer decoder predicted RNA from ATAC embeddings on unseen PBMC5k, with marker genes (*LYZ*, *MS4A1*, *CD3E*, *GNLY*) raised in the expected lineages. No quantitative accuracy is given.
- **Bulk BED files.** Continued pretraining on more than 35,000 hg38 BED files from BEDbase (10 epochs; atacformer-bb) produced file embeddings that clustered by assay and cell line. An XGBoost classifier on these embeddings recovered missing cell-line labels with accuracy 86% and F1 0.85 across more than 275 cell lines.
- **Region embeddings know promoters from enhancers without TSS labels.** Contextualised region embeddings separated ENCODE pELS from dELS. Distance to the pELS centroid correlated with distance to the nearest TSS (positive "TSS distribution scores", against shuffled controls centred at zero).
- **icTSSs.** In 10,000 Luecken2021 CD14+ monocytes and naive CD20+ B cells, regions far from any annotated TSS but embedded near the pELS centroid were called inferred cryptic TSSs. They were enriched 6.33-fold (monocytes) and 6-fold (B cells) for cell-matched H3K4me3 over 500 random region sets (empirical p < 0.001). The overall TSS-distance vs centroid-distance correlation was modest (Spearman ρ 0.30 and 0.29).

## Methods / evidence

Tokenisation: interval overlap of each cell's fragments or peaks with the 890,704-region vocabulary, using Rust implementations (AIList, BITS) in the authors' gtars package with a Hugging Face–compatible API. Model: shared embedding matrix, L transformer encoder layers with no positional encodings, and a linear head for replaced-token detection. The text does not state layer count, width or parameter count. Fine-tunes: triplet margin loss (margin 1.0, L2) on Luecken2021 labels; CRAFT initialised from Geneformer gf-12L-30M-i2048 and atacformer-base-hg38, learning rate up to 5e-5. Clustering: K-means with k equal to the number of true cell types, scored by ARI, AMI and homogeneity. PBMC ground truth comes from KNN label transfer with scEmbed, the authors' own tool. Code and tokenisers are public (databio GitHub, Hugging Face).

Weight: clustering evidence is three datasets with figure-only scores. Ground truth for two of them comes from the authors' own scEmbed-based transfer. RNA imputation, batch correction and fragment-level clustering quality are shown only as UMAPs or marker plots. ChromFound was left out of the benchmark because its code is not public. (synthesis)

## Limitations

**Authors' own:**
- No positional encoding is a deliberate choice, but it may hurt tasks that need spatial resolution, such as linking enhancers to promoters over long distances.
- Tokenisation depends on the fixed vocabulary and its resolution, which could limit transfer across genome builds or to non-human species.
- Evaluations, especially multimodal alignment, used well-annotated datasets. Low-quality or noisy settings remain untested.

**Reviewer notes:**
- The pretraining corpus in Table S1 adds up to about 976,000 cells from 8 datasets, not the 1.2 million cells from 30 tissues stated in the text. Luecken2021 is in both the pretraining corpus and the fine-tuning and icTSS sets, and Kidney22k is in both pretraining and CRAFT training. Supplementary Fig. S2 labels the replacement rate "MLM 45%". (synthesis)
- Region identity is a vocabulary index with no DNA sequence. Like peak-ID models, Atacformer cannot score regions outside its vocabulary, and anything that falls outside the universe is dropped. This is the reverse trade-off from sequence-aware models such as scBasset or EpiZoo. (synthesis)
- The icTSS analysis compares H3K4me3 at selected regions against random vocabulary regions. A stronger control would be distal accessible regions matched for accessibility, since accessible sites in general carry more H3K4me3 than random sites. (synthesis)

## Surprising or load-bearing bits

- **A cell as a set, not a sequence.** Dropping positional encodings and switching to ELECTRA follows from treating co-accessible regions as unordered. This is a clean answer to "what is a token in scATAC?" (synthesis)
- **Fragments in, embeddings out.** Removing peak calling and the count matrix is a practical speed gain, because I/O and matrix building dominate runtime in standard pipelines.
- **The same model reads bulk and single-cell data.** A BED file of any assay is valid input, which makes the model a metadata-imputation tool for repositories such as BEDbase.
- **Base model vs fine-tune trade-off.** The blood-tuned model got worse on brain. Task-specific fine-tuning can reduce generality.

## Concepts touched

- [[single-cell-foundation-model]] — a lightweight scATAC foundation model, positioned against EpiAgent (>1B parameters) and ChromFound.
- [[genomic-tokenization]] — vocabulary of consensus genomic intervals as tokens, with no sequence and no position.
- [[scatac-seq]] — clustering, batch integration and fragment-level analysis.
- [[cis-regulatory-element]] — region embeddings separate ENCODE pELS from dELS; icTSSs are candidate unannotated promoters.
- [[multimodal-integration-methods]] — CRAFT RNA–ATAC contrastive alignment and RNA prediction.
- [[batch-effect]] — preliminary zero-shot integration across PBMC datasets (visual).

## Connections to other sources

- Pipelines compared: [[zhang-2024-snapatac2]], [[granja-2021-archr]], [[xiong-2019-scale]]. Sequence-based CNN reference: [[yuan-2022-scbasset]].
- Other scATAC foundation models in this ingest: [[liu-2025-clm-access]], [[wu-2025-epifoundation]] and [[li-2026-epizoo]]. EpiZoo is sequence-aware. Atacformer (individual region IDs) and CLM-access (patches of position-ordered cCREs) use coordinate-based tokens with no DNA sequence. (synthesis)
- Transcriptomic encoder reused in CRAFT: Geneformer. Single-cell foundation-model template: [[cui-2024-natmethods]] (scGPT).
- Benchmark context for scATAC embeddings: [[luo-2024-scatac-benchmark]].

## Open questions

- How does Atacformer compare with EpiAgent, ChromFound or EpiFoundation on a shared, independently labelled benchmark with reported numbers? (synthesis)
- Do icTSSs drive transcripts? H3K4me3 enrichment suggests promoter activity, but no RNA (e.g. CAGE) or nascent-transcription evidence is shown.
- What happens when a new dataset's peaks fall largely outside the 890k-region vocabulary, as with a different tissue, species or genome build?

## Related

- [[liu-2025-clm-access]] · [[wu-2025-epifoundation]] · [[li-2026-epizoo]] · [[yuan-2022-scbasset]] · [[scatac-seq]] · [[single-cell-foundation-model]] · [[40-Topics/single-cell-atac-seq]] · [[40-Topics/sequence-models-and-foundation-models]]
