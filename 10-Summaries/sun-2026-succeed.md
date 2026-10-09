---
type: summary
title: "Sun et al. 2026 — Large-scale data-driven pre-trained DNA models enhance performance across diverse genomics tasks"
source: "[[00-Sources/papers/Large-scale data-driven pre-trained DNA models enhance performance across diverse genomics tasks]]"
source_quality: full
source_sha256: "f1b6f73857be530cce9c790ac52d20aed8416594c155c363a97794652168ce3f"
source_kind: paper
author: "Canzhuang Sun, Zhijie He, Shifei Zhang, Kang Xu, Yu Sun, Yuyang Wang, … , Hao Li, Hebing Chen"
published: 2026-05-14
ingested: 2026-10-08
doi: "10.1038/s41467-026-73129-6"
journal: "Nature Communications"
tags: [SUCCEED, sequence-to-function, supervised-pretraining, DNA-foundation-model, transformer, RoPE, RMSNorm, SwiGLU, ENCODE, transfer-learning, EPCOT, AtacWorks, C.Origami, ATAC-denoising, scATAC, Hi-C-prediction, cross-species, zero-shot]
entities: []
concepts: ["[[sequence-to-function-model]]", "[[dna-language-model]]", "[[scatac-imputation]]", "[[scatac-seq]]", "[[pseudo-bulk]]", "[[single-cell-hi-c]]", "[[topologically-associating-domain]]", "[[chip-seq]]", "[[atac-seq]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[single-cell-atac-seq]]", "[[3d-genome]]", "[[computational-methods]]"]
---

**Citation:** Sun et al. (2026) — *Large-scale data-driven pre-trained DNA models enhance performance across diverse genomics tasks* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-026-73129-6)

# Sun 2026 — SUCCEED

> SUCCEED (Sequence-Functional Genome Foundation Model) is a lighter Enformer-style CNN + transformer, pretrained in a **supervised** multi-task way on 6,389 human ENCODE tracks (DNase, ATAC, TF and histone ChIP-seq), and then used as a frozen or fine-tuned sequence encoder for downstream tasks. The authors present it as a "foundation model" built from functional labels rather than self-supervised masked-token training. Paired with a small encoder for a cell type's own ATAC-seq signal, it predicts cell-type-specific histone and TF tracks (beating EPCOT), denoises sparse bulk and single-cell ATAC (beating AtacWorks), and predicts Hi-C contact maps without CTCF input (beating C.Origami). In shared-encoder comparisons it and Sei, both supervised, beat self-supervised DNA language models.

## Key claims

- **Enformer-level accuracy with a smaller model.** Retrained on Enformer's Basenji2 data, SUCCEED reached test PCC 0.76 for CAGE (Enformer 0.703), 0.556 for TF ChIP (0.572), 0.698 for histone ChIP (0.692) and 0.813 for DNase/ATAC (0.847).
- **Short-sequence benchmarks.** On six GenBench promoter tasks plus human splice sites, fine-tuned SUCCEED had mean accuracy 0.906 vs 0.891 trained from scratch, and was comparable to or better than larger self-supervised models (DNABERT, DNABERT-2, Nucleotide Transformer, HyenaDNA) on most tasks. Baseline numbers were taken from the GenBench paper, not rerun.
- **Cross-scale transfer.** A model pretrained at 131,072 bp / 128 bp transfers to 524 kb, 1 Mb and 2 Mb inputs; fine-tuning only the head did well, and fine-tuning transformer + head beat training from scratch at lower cost.
- **scATAC transfer.** On CATlas human brain pseudobulk scATAC (45 cell types in Results; Methods mention 128 pseudobulk cell types), fine-tuning and training from scratch performed about the same, with fine-tuning cheaper.
- **Cell-type-specific epigenomes.** With a frozen 1 Mb backbone plus an ATAC encoder, SUCCEED beat EPCOT across most histone marks and TFs in cross-chromosome tests (trained on K562, GM12878, HepG2, MCF-7) and on held-out IMR-90 and A549, except MAFK, CEBPB and (in A549) MYC. Removing pretraining made it worse on all metrics. Zero-shot on mouse tissues it did well for CTCF and H3K27ac.
- **ATAC denoising.** Against AtacWorks it had higher PCC and peak-calling AUPRC at all depths down to 0.2 M reads. On held-out erythroid cells at 0.2 M reads, peak-calling AUPRC was 0.38 with the SUCCEED encoder vs 0.17 without it. For scATAC, it reconstructed profiles from single-cell input comparable to conventional methods at ~300 cells, and recovered regulatory activity from 50 effector CD4+ T cells.
- **3D genome.** Replacing C.Origami's sequence encoder with SUCCEED gave closer insulation-score agreement on IMR-90, worked without CTCF ChIP-seq, generalised to GM12878, and predicted K562 Hi-C from pseudobulk scATAC of ≤200 cells with modest loss. Sei was comparable (slightly better with scATAC input); Enformer and self-supervised DNA LMs were worse. Zero-shot on mouse, insulation agreed well but observed/expected correlation was lower than in human.

## Methods / evidence

Architecture: convolutional stem (kernel 19, max pool stride 8), multi-stage convolutional tower (kernel 5, max pool stride 2), adaptive average pooling to 1,024 bins, transformer encoder with RoPE, RMSNorm, grouped-query attention and SwiGLU, cropping 64 bins per side, and 6,389 softplus heads. Pretraining: Poisson NLL, 131,072 bp input at 128 bp, 8:1:1 split following Basenji2, reverse complement and 1–3 bp shift augmentation, AdamW (lr 1e-4), gradient clip 0.2. ENCODE signal p-value bigWigs (read-depth-normalised signal for DNase), replicates merged, values clipped to 0–32. Downstream: frozen or fine-tuned backbone plus a task-specific signal encoder; for comparisons with other foundation models, only the sequence encoder is swapped. Code: github.com/bioczsun/SUCCEED. Parameter counts are not given in the clipped text.

Weight: a broad set of transfer tasks, each against one task-specific baseline (EPCOT, AtacWorks, C.Origami) plus a shared-encoder comparison against Sei, Enformer and self-supervised models. Many numbers live in figures and supplementary data not in the clipping. There are small inconsistencies: Results give chromosomes 10 and 21 for cross-chromosome testing, Methods give 10 and 21 in one place and 10 and 20 in another; Results name 45 brain cell types, Methods 128; Methods list H1 as a cross-cell-type test line that Results do not report. (synthesis)

## Limitations

**Authors' own:**
- Pretrained only on human ENCODE data, which does not cover the diversity of in vivo tissues, cell types and states; Roadmap, FANTOM and single-cell epigenomic data are proposed additions.
- Compute grows steeply with input length; the purely convolutional Sei is competitive at lower cost.
- Limited ability to integrate information across scales from 128 bp to 2 Mb.
- Transfer to rare or uncharacterised cell types could improve with few-shot or meta-learning.
- Some baselines have input-length or design constraints that may disadvantage them under the unified evaluation; Enformer's poor showing on the 1 Mb task may reflect its 196 kb / 128 bp configuration.

**Reviewer notes:**
- Cell-type specificity comes mainly from the measured ATAC input, not from sequence; the pretrained encoder supplies a prior. This is closer to EPCOT/C.Origami-style imputation than to a pure sequence model. (synthesis)
- Self-supervised baselines were run by chunking 1–2 Mb inputs into 1 kb or 8 kb pieces processed independently, which removes their long-range context; their weaker results partly reflect this setup. (synthesis)
- No variant-effect benchmark is reported, so its standing against Enformer/Borzoi/AlphaGenome on the main use of sequence-to-function models is unknown. (synthesis)

## Surprising or load-bearing bits

- The paper reframes a supervised sequence-to-function model as a "DNA foundation model" and argues, with Sei, that functional-label pretraining beats masked-token pretraining for regulatory tasks — a direct counterpoint to DNA language model claims.
- Fine-tuning versus training from scratch on brain scATAC made little difference in accuracy; the gain was mostly compute.
- Hi-C maps predicted from ATAC of ≤200 cells give a route to cell-type 3D structure without single-cell Hi-C, though the paper evaluates only against bulk Hi-C. (synthesis)

## Concepts touched

- [[sequence-to-function-model]] — supervised multi-task pretraining as a reusable encoder.
- [[dna-language-model]] — outperforms DNABERT, DNABERT-2, Nucleotide Transformer and HyenaDNA as encoders on regulatory tasks.
- [[scatac-imputation]] / [[scatac-seq]] / [[pseudo-bulk]] / [[sequencing-depth-and-coverage]] — denoising down to 0.2 M reads and single-cell input.
- [[single-cell-hi-c]] / [[topologically-associating-domain]] / [[3d-genome]] — ATAC-plus-sequence prediction of Hi-C, scored by insulation.
- [[chip-seq]] / [[atac-seq]] — pretraining targets and the cell-type input.

## Connections to other sources

- Architecture and data pipeline follow [[avsec-2021-enformer]] and [[kelley-2018-basenji]]; cites [[linder-2025-borzoi]] and [[avsec-2026-alphagenome]] as inspiration.
- Closest supervised peer: [[chen-2022-sei]] (comparable, purely convolutional).
- Self-supervised comparators: [[ji-2021-dnabert]], [[zhou-2023-dnabert-2]], [[dallatorre-2025-nucleotide-transformer]], [[nguyen-2023-hyenadna]].
- Uses SnapATAC2 ([[zhang-2024-snapatac2]]) for scATAC processing; CATlas brain pseudobulk as in [[linder-2025-borzoi]].
- Related ATAC-to-epigenome models in this ingest: [[gao-2024-epigept]], [[fu-2025-get]]. Hi-C prediction peers: [[fudenberg-2020-akita]], [[zhou-2022-orca]], [[wang-2026-hicfoundation]]. (synthesis)

## Open questions

- Would the supervised-beats-self-supervised result hold if DNA language models were given full long-range context rather than chunked inputs? (synthesis)
- How does SUCCEED score noncoding variants compared with Enformer and AlphaGenome? Not tested.
- Can Hi-C predicted from pseudobulk scATAC be validated against single-cell Hi-C of the same cell types? (synthesis)

## Related

- [[sequence-to-function-model]] · [[dna-language-model]] · [[chen-2022-sei]] · [[avsec-2021-enformer]] · [[scatac-imputation]] · [[40-Topics/sequence-models-and-foundation-models]]
