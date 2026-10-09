---
type: summary
title: "Wang et al. 2026 — A generalizable Hi-C foundation model for chromatin architecture, single-cell and multiomics analysis across species"
source: "[[00-Sources/papers/A generalizable Hi-C foundation model for chromatin architecture, single-cell and multiomics analysis across species]]"
source_quality: full
source_sha256: "69032beefb021eae77e85d675ee9cdb74854fce43bc292585246e8e628ae04da"
source_kind: paper
author: "Xiao Wang, Yuanyuan Zhang, Suhita Ray, Anupama Jha, Tangqi Fang, Shengqi Hang, … William S. Noble, Sheng Wang (9 authors)"
published: 2026-06-15
ingested: 2026-10-08
doi: "10.1038/s41592-026-03097-8"
journal: "Nature Methods"
tags: [HiCFoundation, Hi-C, foundation-model, masked-autoencoder, ViT, contrastive-loss, reproducibility, loop-calling, resolution-enhancement, scHi-C, epigenome-prediction, cross-species, DNA-Zoo, 4DN, ENCODE, HSPC, neutrophil, lamin-B1, Noble-lab]
entities: []
concepts: ["[[single-cell-foundation-model]]", "[[single-cell-hi-c]]", "[[chromatin-loop]]", "[[topologically-associating-domain]]", "[[chromatin-compartments]]", "[[hi-c-normalization]]", "[[imputation]]", "[[chip-seq]]", "[[chromatin-accessibility]]", "[[nuclear-lamina]]", "[[hematopoietic-differentiation]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/3d-genome]]", "[[40-Topics/chromatin-architecture]]"]
---

**Citation:** Wang et al. (2026) — *A generalizable Hi-C foundation model for chromatin architecture, single-cell and multiomics analysis across species* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-026-03097-8)

# Wang 2026 — HiCFoundation

> HiCFoundation treats Hi-C contact maps as images and pretrains a **masked autoencoder** on them. Inputs are 224 × 224 submatrices at 5-kb resolution (196 patches of 16 × 16), drawn from both *cis* and *trans* chromosome pairs, with 75% of patches masked. The encoder is a ViT-Large (304 M parameters), the decoder small (26 M). The loss is a **patchwise contrastive term** (InfoNCE-style: each reconstructed patch should match its own target and differ from all other patches in the submatrix) plus an SSIM term, because plain MSE collapsed to all-zero outputs on sparse maps. Pretraining used Hi-C from 81 training human biosamples (with 20 for validation) from ENCODE and 4DN, about two weeks on eight A100s. For each task the encoder is frozen and only a task decoder is fine-tuned (under ten hours): replicate-reproducibility scoring, loop calling at high and low coverage, resolution enhancement, prediction of six 1-D epigenomic tracks from Hi-C, and single-cell Hi-C enhancement. It is not a sequence model: there is no DNA input, and the authors list adding sequence as future work.

## Key claims

- **Loop calling.** Against consensus HiCCUPS loops from two deep replicates, mean loop F1 was 81.6% (high coverage) and 75.1% (1/16 downsampled), beating HiCCUPS, Chromosight and Mustache (sign test P < 0.001 vs the second best). 90.4% (high) and 81.8% (low) of called loops had CTCF ChIP-seq peaks at both anchors. Results held against CTCF ChIA-PET loops.
- **Reproducibility.** Embedding similarity separated biological replicates from non-replicates better than HiCRep, GenomeDISCO and HiC-Spector, with more than 10× speed-up, and stayed robust with up to 50% injected noise.
- **Resolution enhancement.** On raw counts (not normalised maps, because the authors found a systematic problem with the normalisation used by earlier methods), mean rank across six metrics was 1.08 (human) and 1.05 (mouse), vs 2.38 for HiCARN1, with HiCNN and HiCSR also retrained on the same splits. Enhanced maps kept biosample-specific differences.
- **Pretraining matters.** The same architecture without pretraining was worse on every task and about 10× slower to train. On DNA Zoo Hi-C from more than 300 species (fine-tuned on human only), HiCFoundation beat competitors, and its gain over "no pretrain" was larger in non-mammals. Genome-wide embeddings tracked divergence time from humans.
- **HSPC to neutrophil.** Enhancing low-coverage Hi-C from control and lamin B1-knockdown (LB1^LO, about 25% of normal) CD34⁺ HSPCs and neutrophils found >7-fold more short-range loops (the Methods say >8-fold). Loop strength (P2LL) fell in neutrophils vs HSPCs and with lamin B1 loss in both (P < 0.001), while 806 loops were gained in neutrophils, with enhancer–promoter rewiring at *CEBPA* and *CEBPE* and secretion-gene enrichment among strengthened loops. More than 70% of previously published loops were recovered.
- **Epigenome from Hi-C.** HiCFoundation-epi predicts ATAC, DNase, CTCF, H3K4me3, H3K27ac and H3K27me3 at 1 kb from Hi-C alone (trained on GM12878 and H1, tested on K562 and held-out chromosomes) and beat Hi-C PCA and a no-pretrain model. Accuracy was higher in TSS windows than genome-wide. Zeroing the Hi-C around 392 convergent-CTCF loops lowered predicted CTCF at the anchor in 383 (97.8%), by 41.8% on average.
- **Single-cell Hi-C.** Fine-tuned on HiRES mouse embryo scHi-C (1-Mb bins, 1/4 downsampled input, rank-weighted MSE), it beat Higashi, scHiCluster and scVI-3D. In the cross-species test on human WTC11 cells, applied without retraining while the others were retrained, it improved Pearson by 35.9%, SSIM by 20.0% and PSNR by 30.2% over scHiCluster. On K562 GAGE-seq (also not retrained), pseudobulk of enhanced cells matched bulk Hi-C best (mean rank 1.167) and gave A/B compartments consistent with ATAC and expression.

## Methods / evidence

Data: 678 Hi-C experiments from ENCODE and 4DN (in situ, dilution, intact Hi-C, Micro-C, DNase Hi-C; human, mouse, chicken, zebrafish, fly; at least 10 M non-diagonal read pairs), plus 337 DNA Zoo experiments. Splits are by human biosample (81/20/18) and by chromosome (chr4, 5, 11, 14 held out). Low coverage is simulated by 1/16 downsampling. scHi-C datasets: WTC11 (185 cells), Tan2021 mouse cortex (1,943), HiRES (7,576), GAGE-seq K562 (593), each filtered to cells with more than 100,000 *cis* contacts. Ablations covered loss variants, masking ratio (75% best; 90% worse) and decoder-to-encoder size (0.09 best). Code and models are public (Apache 2.0).

Weight: a broad, carefully split benchmark from the Noble lab. Most per-method numbers sit in figures and supplementary tables that are images or downloads in the clipping; this page reports the numbers given in text. Several counts differ between sections: 81 vs 101 human biosamples for pretraining, 118 vs about 116 million submatrices, and >7-fold vs >8-fold more loops in HSPCs. (synthesis)

## Limitations

**Authors' own:**
- No DNA sequence input; adding sequence tokens is proposed.
- Hi-C → epigenome is one-way; a bidirectional model (e.g., with Epiphany) is suggested.
- Reliable ground truth is hard to obtain for loop calling and enhancement; validation relies on orthogonal CTCF ChIP-seq and ChIA-PET.

**Reviewer notes:**
- Enhancement is trained on downsampled deep maps, so "low coverage" means thinned high-quality libraries. Real low-input libraries (HSPCs, single cells) have other biases, and the extra loops found there are validated only indirectly (CTCF enrichment, recovery of known loops). (synthesis)
- scHi-C enhancement uses 1-Mb bins and the original sparse map as target. It recovers coarse structure, not loops, in single cells. (synthesis)
- The epigenome predictions come from three cell lines and 1-kb bins. They show that Hi-C carries activity information, not that Hi-C can replace those assays. (synthesis)

## Surprising or load-bearing bits

- **Contrastive patches beat pixel losses.** MSE, SSIM and cosine pretraining all did worse; contrasting each patch against all others in the same submatrix was what made sparse Hi-C learnable.
- **Pretraining helps most where the data are most foreign** (non-mammals, single cells applied cross-dataset), which is the usual case for a foundation model being worth it.
- **In silico loop deletion** reduces predicted CTCF at the anchors in 97.8% of convergent-CTCF loops, so the model's 1-D predictions depend on the 3-D input the way biology suggests.
- **Neutrophils lose loops** globally but keep and rewire loops at neutrophil genes, and lamin B1 loss weakens loops in both HSPCs and neutrophils.

## Concepts touched

- [[single-cell-foundation-model]] — a 3D-genome foundation model pretrained on bulk Hi-C and adapted to scHi-C.
- [[single-cell-hi-c]] — enhancement of sparse single-cell maps by transfer from bulk pretraining.
- [[chromatin-loop]] / [[topologically-associating-domain]] / [[chromatin-compartments]] — loop calling, TAD F1 and A/B compartments as tasks and checks.
- [[hi-c-normalization]] — works on raw counts; argues earlier enhancement methods were hurt by normalisation.
- [[imputation]] — coverage enhancement as imputation of missing contacts.
- [[chip-seq]] / [[chromatin-accessibility]] — predicted from Hi-C.
- [[nuclear-lamina]] / [[hematopoietic-differentiation]] — lamin B1 knockdown and HSPC-to-neutrophil loop loss.

## Connections to other sources

- Single-cell Hi-C baselines: [[zhang-2022-higashi]], [[zhou-2019-schicluster]], [[zheng-2022-bandnorm-scvi-3d]].
- Hi-C foundations: [[lieberman-aiden-2009-hic]], [[rao-2014-in-situ-hic]] (HiCCUPS); Juicer tooling [[durand-2016-juicer]]; Micro-C data included ([[hsieh-2015-micro-c]]).
- Sequence-based 3D models that HiCFoundation does not use but cites as future direction: [[fudenberg-2020-akita]], [[zhou-2022-orca]]. A DNA-language-model route to Hi-C prediction is [[fang-2025-evo2hic]]. (synthesis)
- Using 3D contacts to guide epigenome prediction is the reverse of [[gao-2024-epigept]], which uses HiChIP loops to supervise a sequence model's attention. (synthesis)
- Review context for scHi-C methods: [[hong-2025-sc3d-genome-review]], [[dautle-2025-schic-review]].

## Open questions

- Would adding DNA sequence tokens (as proposed) let the model predict structure for samples with no Hi-C at all? (synthesis)
- Do the extra loops found in enhanced low-input HSPC maps validate with an orthogonal assay such as Micro-C or HiChIP?
- Can scHi-C enhancement work at loop-level resolution, or is 1 Mb the practical floor for current single-cell coverage? (synthesis)

## Related

- [[single-cell-foundation-model]] · [[single-cell-hi-c]] · [[chromatin-loop]] · [[zhang-2022-higashi]] · [[zhou-2019-schicluster]] · [[gao-2024-epigept]] · [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/3d-genome]]
