---
type: summary
title: "Fan et al. 2026 — GFETM: Genome foundation-based embedded topic model for scATAC-seq modeling"
source: "[[00-Sources/papers/GFETM_ Genome foundation-based embedded topic model for scATAC-seq modeling]]"
source_quality: full
source_sha256: "77ab573d4b1ca0396be3c1e09116e9449014100ea2d11d23562ebc5f5dd60fca"
source_kind: paper
author: "Yimin Fan, Adrien Osakwe, Shi Han, Yu Li, Jun Ding, Yue Li (lead contact)"
published: 2026-05
ingested: 2026-10-07
updated: 2026-10-07
doi: "10.1016/j.cels.2026.101563"
preprint_doi: "10.1101/2023.11.09.566403"
journal: "Cell Systems 17(5):101563 (clipped text = bioRxiv v3, July 2024)"
tags: [GFETM, scATAC-seq, genome-foundation-model, embedded-topic-model, ETM, VAE, DNABERT, Nucleotide-Transformer, HyenaDNA, sequence-informed, transfer-learning, zero-shot, peak-imputation, denoising, preprint-text]
entities: []
concepts: ["[[scatac-seq]]", "[[latent-dirichlet-allocation]]", "[[cistopic]]", "[[convolutional-neural-network]]", "[[dimensionality-reduction]]", "[[scatac-imputation]]", "[[transcription-factor-motif]]", "[[batch-effect]]", "[[hematopoietic-differentiation]]", "[[clustering-algorithms]]"]
topics: ["[[single-cell-atac-seq]]", "[[computational-methods]]"]
---

**Citation:** Fan et al. (2026) — *GFETM: Genome foundation-based embedded topic model for scATAC-seq modeling* — *Cell Systems* 17(5):101563. [DOI](https://doi.org/10.1016/j.cels.2026.101563). Preprint: bioRxiv [10.1101/2023.11.09.566403](https://doi.org/10.1101/2023.11.09.566403) (v3).

# Fan 2026 — GFETM

> **Version note (re-clipped 2026-10-07):** the source is now the **full bioRxiv v3 text** (posted July 2024), with Results, Methods, supplementary text and figure captions. It replaces the earlier ScienceDirect clipping, which had no Results. The published *Cell Systems* version (2026) adds an author (Shi Han) and may differ in numbers, figures and baselines. Everything below is from the preprint. Figure values and supplementary tables are images or links in the clipping, so most comparisons are reported here as the text describes them, not as numbers.
>
> GFETM puts a pretrained **genome foundation model (GFM)** inside an **embedded topic model (ETM)**. The ETM is a VAE: a two-layer MLP encoder maps each cell's TF-IDF-normalised peak vector to a topic mixture θ, and a **linear decoder** reconstructs peaks from θ · α · ρ, where α is a learned topic embedding and ρ is the peak embedding. GFETM computes ρ by running each peak's DNA through the GFM (DNABERT 6-mer by default, 768-d) and **fine-tunes the GFM's last two transformer layers jointly with the ETM**. Because cells pass through an amortised encoder and peaks pass through a sequence model, the trained model can embed **unseen cells** and score **unseen peaks**, which the authors present as the main advance over scBasset.

## Key claims

- **Frozen GFM embeddings are not enough; joint fine-tuning is the gain.** Across 13 GFMs (DNABERT, DNABERT-2, Nucleotide Transformer, HyenaDNA variants), initialising ρ from GFM embeddings and freezing it beat random ρ on ARI, and larger embedding sizes did better. But frozen GFM embeddings did not significantly beat an ETM that learns random ρ. End-to-end fine-tuning gave "drastic improvements". DNABERT was chosen for its light weight, not because it was best: NT-2.5b-multi-species performed best, and NT-500M-human-ref beat NT-500M-1000g, which the authors attribute to matching the hg38 reference.
- **Clustering benchmark.** On Buenrostro 2018 human HSC differentiation (2,034 cells, 6 batches), 10x PBMC (2,714 cells) and 10x E18 mouse brain (4,878 cells), the sequence-informed deep models (**GFETM and scBasset**) beat all other baselines "by a large margin". GFETM is **competitive with scBasset, not uniformly better**. An ETM+CNN baseline did worse than GFETM, though the authors note they did not explore CNN designs thoroughly.
- **Scaling.** On 20k–80k Cusanovich-mouse cells with 1k–70k highly variable peaks, GFETM beat scBasset and PeakVI throughout, and most clearly with many peaks and a modest number of cells (>30k peaks at 20k–40k cells). It is slower: about 4 h against about 1.5 h for scBasset at 20k cells × 20k peaks, with 88 M against 5 M parameters. GFETM runtime grows linearly with cells, scBasset's with peaks.
- **Batch.** On Buenrostro 2018, GFETM without a batch term had the highest ARI and second-highest kBET. Adding the batch term λ (GFETM-bc) gave the best kBET at a slightly lower ARI. The authors dropped λ for later analyses.
- **Unseen cells.** scBasset stores cell embeddings as parameters, so it must be partly or fully fine-tuned on new cells. GFETM and PeakVI apply their encoders directly. Trained on 1k–30k cells and tested on 10k held-out cells, GFETM generalised best and beat scBasset even when scBasset was fine-tuned on the test set.
- **Unseen peaks (leave-one-chromosome-out).** On Buenrostro 2018 with the top 500 variable peaks per autosome, GFETM's top-K precision beat scBasset by about 10% at K = 5, 6% at K = 10 and 3% at K = 20, varying by chromosome. CellSpace, SIMBA and PeakVI cannot do this task. Imputation uses a three-stage procedure: train, freeze the encoder and retrain the decoder and GFM with a Bernoulli cross-entropy loss, then score new peaks as θ · α · ρ′.
- **Denoising shifts marker peaks distal.** For HSCs, GFETM-denoised signal increased enrichment of differential peaks near known marker genes over raw counts. scBasset was better within 1 kb of the TSS, and GFETM was better beyond 1 kb, especially >10 kb. The authors read this as CNN receptive fields favouring promoter-proximal motifs and attention reaching distal enhancers.
- **Transfer across tissues, species and omics (zero-shot unless stated).** Cross-tissue transfer (12 mouse and 21 human tissues, 2,000 cells each) beat PeakVI, and worked better between functionally similar tissues; cell-type Jaccard similarity correlated with transfer ARI (Kendall τ, Spearman ρ). Transfer followed by training on the target tissue usually beat training on the target alone. Human-to-mouse transfer (heart, lung, intestine; mm9 peaks lifted over to hg19, overlap-matched) separated major cell types where PeakVI did not. Cross-omic transfer (RNA and ATAC on a shared gene basis, ±256 bp around each TSS as the "peak" sequence) gave reasonable clusters. On myocardial data, ATAC-trained models clustered scRNA-seq better than RNA-trained ones, and reduced donor effects within age groups. The authors call this analysis "illustrative" rather than systematic.
- **Interpretable topics.** In a diabetic-kidney dataset, topic 9 marked fibroblasts (top peaks near *CRISPLD2*, *ADAMTS2*, *FBLN5*) and was also disease-associated. Topic 10 marked podocytes (*PTPRO*, *LMX1B*, *FGF1*). Topics 0, 29, 38 and 55 were up in diabetes, with topic 38 near *PRKCQ*, *FYB1* and *ITK*. In HSC differentiation, top-100 peaks per topic run through MEME-SEA with HOCOMOCO v11 linked IRF1/IRF2 to MEP-enriched topics, CTCF to topics enriched in CLP, MEP and monocytes, and ETV2/5/6 to a monocyte topic.

## Methods / evidence

Generative model: θ_c ~ logistic-normal; peak tokens drawn from Cat(θ_c β), with β ∝ softmax(αρ); an optional batch term λ; ELBO with a β-VAE KL weight of 1e-6. Encoder: two-layer MLP, hidden size 128, ReLU and batch norm. Adam, learning rate 0.005. Peaks are mean-pooled GFM token embeddings from the last layer. Joint training samples 384 peaks per minibatch to bound GFM cost. Topic differential analysis uses 100,000 label permutations with Bonferroni correction (q < 0.1). Marker enrichment is a Wilcoxon test for marker peaks, then a hypergeometric test against CellMarker 2.0 genes. Data: all public (Buenrostro 2018, 10x PBMC and E18 brain, Catlas-human 1.3 M cells, Cusanovich-mouse, CELLxGENE kidney, myocardial and ovary). Code: github.com/fym0503/GFETM.

Weight: a thorough methods paper with several baselines (scBasset, PeakVI, CellSpace, SIMBA, cisTopic-class methods) and many tasks. The headline is **parity with scBasset on clustering**, with clear gains only on generalisation, imputation, distal denoising and transfer. Most transfer comparisons are only against PeakVI, and the cross-omic result is illustrative. The preprint has small inconsistencies: the unseen-cell test is said to use Cusanovich-mouse in the text but Human HSC in the Fig. 3e caption; Methods 4.3 announces "three strategies" and describes two plus joint training; and the Results give "FDR > 0.1" where Methods say < 0.1. (synthesis)

## Surprising or load-bearing bits

- **Pretraining helps only when adapted.** Frozen embeddings from even a 2.5-billion-parameter GFM did not significantly beat learning ρ from scratch. The value appears only after task-specific fine-tuning, which complicates the "foundation model features transfer for free" story. (synthesis)
- **Peak sequence vs. peak identity.** scBasset embeds cells as parameters but peaks through sequence. GFETM amortises both, which is why it is the one that handles unseen cells *and* unseen peaks.
- **Transfer still needs coordinate overlap.** Cross-species transfer lifts over mm9 to hg19 and keeps only overlapping peaks, so the shared feature space is still coordinate-based. The sequence model adapts the embeddings, but the features do not come from sequence alone. (synthesis)
- **Distal vs. proximal.** The <1 kb vs >10 kb split between scBasset and GFETM is a testable claim about CNN vs attention receptive fields, though both models see only the peak sequence itself. (synthesis)
- **scATAC as a cleaner signal than scRNA for clustering** in the myocardial example, where RNA showed strong age-group batch effects that ATAC did not.

## Concepts touched

- [[scatac-seq]] — sequence-informed, transferable representation model.
- [[latent-dirichlet-allocation]] / [[cistopic]] — ETM keeps the topic decomposition with a linear decoder; cisTopic sits in the sequence-free family.
- [[convolutional-neural-network]] — scBasset and the ETM+CNN ablation as the short-range comparator.
- [[scatac-imputation]] — leave-one-chromosome-out peak imputation and denoising.
- [[batch-effect]] — kBET/ARI trade-off with and without λ.
- [[transcription-factor-motif]] — topic top-peaks scanned with MEME-SEA/HOCOMOCO.
- [[hematopoietic-differentiation]] — Buenrostro 2018 benchmark and motif-topic analysis.
- [[dimensionality-reduction]] / [[clustering-algorithms]] — θ as the cell embedding, Louvain clustering scored by ARI/AMI/ASW.

## Connections to other sources

- Main comparator: [[yuan-2022-scbasset]] — competitive on clustering; GFETM better on unseen cells, unseen-peak imputation and distal denoising, scBasset better at promoter-proximal (<1 kb) marker enrichment.
- Transfer baseline: [[ashuach-2022-peakvi]].
- Critiques [[tayyebi-2024-cellspace]] for inferring only on training cells and for short-range k-mer features.
- Sequence-free family: [[bravo-2019-cistopic]], [[xiong-2019-scale]], [[pliner-2018-cicero]]. Sequence-informed predecessors: [[schep-2017-chromvar]], [[de-boer-2018-brockman]].
- Foundation-model framing parallels [[cui-2024-natmethods]] (scGPT) on the transcriptome side. (synthesis)
- Benchmark context for scATAC embeddings: [[luo-2024-scatac-benchmark]]. Combinatorial-indexing data lineage: [[cusanovich-2015-sciatac]].

## Open questions

- Do the published *Cell Systems* numbers match the preprint? The 2026 version added an author and may have changed baselines or figures. (synthesis)
- Would a stronger GFM (NT-2.5b, which did best frozen) fine-tuned with parameter-efficient methods beat DNABERT? The authors list efficient fine-tuning as future work.
- Is the clustering parity with scBasset enough to justify ~3× runtime and ~18× parameters, outside transfer use cases? (synthesis)
- Cross-species transfer was tested only human → mouse on three tissues with lifted-over peaks; distant species and non-overlapping peaks remain untested. (synthesis)

## Related

- [[scatac-seq]] · [[cistopic]] · [[scatac-imputation]] · [[yuan-2022-scbasset]] · [[tayyebi-2024-cellspace]] · [[40-Topics/single-cell-atac-seq]]
