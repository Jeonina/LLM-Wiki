---
type: summary
title: "Lin et al. 2026 — EPInformer: scalable and integrative prediction of gene expression from promoter-enhancer sequences with multimodal epigenomic profiles"
source: "[[00-Sources/papers/EPInformer_ scalable and integrative prediction of gene expression from promoter-enhancer sequences with multimodal epigenomic profiles]]"
source_quality: full
source_sha256: "c4176fd685c69d429418f57806987c0e76149b258913b207a6e658fb68982fac"
source_kind: paper
author: "Jiecong Lin, Zhijian Li, Yajie Zhao, Ruibang Luo, Luca Pinello"
published: 2026-03-14
ingested: 2026-10-08
doi: "10.1038/s41467-026-70535-8"
journal: "Nature Communications"
tags: [EPInformer, gene-expression-prediction, promoter-enhancer, transformer, attention, ABC-score, H3K27ac, DNase-seq, ATAC-seq, Hi-C, CAGE, RNA-seq, enhancer-gene-linking, CRISPRi, eQTL, TF-MoDISco, lightweight-model, Pinello-lab]
entities: []
concepts: ["[[sequence-to-function-model]]", "[[cis-regulatory-element]]", "[[transcription-factor-motif]]", "[[de-novo-motif-discovery]]", "[[convolutional-neural-network]]", "[[dnase-seq]]", "[[chip-seq]]", "[[atac-seq]]", "[[chromatin-loop]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[histone-modifications]]", "[[3d-genome]]", "[[computational-methods]]"]
---

**Citation:** Lin et al. (2026) — *EPInformer: scalable and integrative prediction of gene expression from promoter-enhancer sequences with multimodal epigenomic profiles* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-026-70535-8)

# Lin 2026 — EPInformer

> EPInformer is a small (447,149 parameters) model that predicts a gene's expression in one cell type from its **promoter plus up to 60 candidate enhancers**, rather than from a long contiguous DNA window. A CNN encodes each 2-kb element; a fusion layer adds measured enhancer activity (DNase, H3K27ac or ATAC), distance and optionally Hi-C contact; a masked transformer lets only the promoter attend to enhancers; a small MLP predicts CAGE or RNA-seq. It is a hybrid of a [[sequence-to-function-model]] and an ABC-style activity × contact model. With measured epigenomic inputs it beats sequence-only Enformer and Borzoi on held-out CAGE, and its final-layer attention scores link CRISPRi-validated enhancers to genes better than the ABC score.

## Key claims

- **RNA-seq (12-fold cross-chromosome, six cell lines).** Sequence + distance only (EPInformer-PE): mean Pearson 0.78 vs Xpresso 0.67. Adding DNase and H3K27ac (PE-Activity): 0.83 (range 0.79–0.86) vs CREaTor 0.78. Adding Hi-C (PE-Activity-HiC): 0.84. For cross-cell-line variation, median Pearson was 0.69 (HiC model), 0.65 (Activity) and 0.51 (CREaTor).
- **CAGE.** On Enformer's and Borzoi's own held-out splits, PE-Activity-HiC beat both in K562 and GM12878; even without Hi-C, PE-Activity beat Borzoi (K562 r = 0.841 vs 0.792; GM12878 0.847 vs 0.800). Under 12-fold CV, PE-Activity-HiC averaged r = 0.883, against Seq-GraphReg 0.744 and CREaTor 0.810. Against MENTR on 92,473 transcripts: 0.792 vs 0.675.
- **Isoforms and ATAC.** Isoform-level K562 CAGE over 46,616 TSSs reached r = 0.814. ATAC-only activity gave 0.843 (K562) and 0.854 (GM12878), close to DNase + H3K27ac (0.867 and 0.874).
- **Enhancer–gene linking.** On 1,575 K562 CRISPR-tested pairs within 100 kb (370 positives), attention with Hi-C reached AUPRC 0.732 vs ABC-HiC 0.698; without Hi-C, 0.600 vs ABC-distance 0.579. The largest gain was for 60–100 kb enhancers (0.510 vs 0.429). Attention-HiC matched or beat ABC-HiC per-gene F1 for 212 of 244 genes (89%). For 166 GM12878 fine-mapped eQTLs (PIP > 0.7), attention-HiC gave higher enrichment than ABC-HiC at recall < 10% and similar at ≥ 10%.
- **Motifs.** The pretrained EPInformer-seq enhancer-activity encoder (256 bp, mean Pearson 0.727 across six lines) yielded shared motifs (JUN, ELF1, ELK1, BACH1, NFYA) and cell-specific ones (GATA1, GATA2, GATA1::TAL1 in K562; SPI1, FOSL1 in GM12878). At a distal *KLF1* enhancer, ISM found GATA1, SP4 and ETV6 motifs.
- **Cheap to train.** About one hour on one A100 for 18,377 protein-coding genes; the authors contrast 0.4 M parameters with Enformer's 250 M and Borzoi's 186 M.

## Methods / evidence

Candidate enhancers come from the ABC pipeline: MACS2 DNase peaks (top 150,000, 500-bp extended, merged), within 100 kb of the TSS, up to 60 per gene (said to cover 95% of elements within a 200-kb window), giving an average of 338,909 promoter–enhancer pairs per cell line. Enhancer activity = geometric mean of DNase and H3K27ac RPM; Hi-C contacts from 4DN maps at 5 kb via FANC and the ABC pipeline. Architecture: sequence encoder (5 residual + 4 dilated conv layers + linear, 64-d embedding per element); fusion by concatenation and 1×1 conv; 3 transformer layers with 4 heads, attention masked to promoter–enhancer pairs only, with final-layer attention weighted by activity × contact (or 1/distance); predictor of three dense layers with mRNA half-life features (from Xpresso) and promoter activity. Smooth L1 loss on log10 expression, AdamW (lr 5e-4), early stopping. Six cell lines: K562, GM12878, HepG2, H1, NHEK, HUVEC. Code: github.com/pinellolab/EPInformer (MIT).

Weight: careful cross-chromosome validation and an enhancer-linking benchmark against the right baseline (ABC with identical inputs). The comparisons with Enformer and Borzoi are not like-for-like: EPInformer receives measured DNase, H3K27ac and Hi-C from the test cell type, while Enformer and Borzoi see only sequence and predict thousands of tracks. Seq-GraphReg numbers are taken from its paper. Most figures are images in the clipping.

## Limitations

**Authors' own:**
- Predicts gene-level expression from the canonical TSS, not isoform-specific expression (although an isoform-level K562 test is reported in Results).
- Uses only activating marks (H3K27ac, DNase); repressive marks such as H3K9me3 and H3K27me3 are not explicitly modelled.
- Trains one model per cell type; multi-cell-type training is future work.
- CTCF, relative positional encoding, reverse-complement handling and pretrained DNA foundation-model embeddings are named as future additions.
- Motif findings (e.g. at *KLF1*) are predictive and need CRISPR or base/prime-editing validation.

**Reviewer notes:**
- Because cell-type information enters through measured epigenomic inputs, EPInformer cannot score a sequence variant's effect on expression unless the variant changes the encoder's view of an element; it is not a variant-effect model in the Enformer sense. (synthesis)
- Reported CAGE correlations differ between Results (12-fold mean 0.883) and Discussion (0.875 K562, 0.891 GM12878), and the window is described as 100 kb in Methods but as 200 kb in the Xpresso comparison. (synthesis)
- Restricting candidates to 100 kb rules out the very distal enhancers where long-context models also struggle, so its distal-enhancer gains are bounded to that range. (synthesis)

## Surprising or load-bearing bits

- A 0.4 M-parameter model with the right inputs beat 186–250 M-parameter sequence-only models on held-out CAGE. Measured chromatin state carries much of what long-context models try to infer from sequence. (synthesis)
- Attention restricted to promoter–enhancer pairs gives a directly readable enhancer–gene score that beats ABC with the same inputs.
- ATAC-only input loses little against DNase + H3K27ac, which makes the approach usable for cell types with only (pseudobulk) ATAC data. (synthesis)

## Concepts touched

- [[sequence-to-function-model]] — a sequence + measured-epigenome hybrid, contrasted with sequence-only Enformer/Borzoi.
- [[cis-regulatory-element]] — enhancer–gene linking against CRISPRi and eQTL benchmarks; ABC as baseline.
- [[transcription-factor-motif]] / [[de-novo-motif-discovery]] — TF-MoDISco-lite and Tangermeme ISM on the enhancer encoder.
- [[convolutional-neural-network]] — residual + dilated sequence encoder.
- [[dnase-seq]] / [[chip-seq]] / [[atac-seq]] / [[histone-modifications]] — enhancer activity inputs (H3K27ac).
- [[chromatin-loop]] / [[3d-genome]] — Hi-C contact as an optional input weighting attention.

## Connections to other sources

- Benchmarks against [[avsec-2021-enformer]] and [[linder-2025-borzoi]] on their own CAGE splits; cites their weakness for enhancers > 10 kb.
- H3K27ac as an active-enhancer mark: [[creyghton-2010-h3k27ac-enhancers]].
- Contrast with sequence-only enhancer–gene linking in Enformer, Borzoi and [[avsec-2026-alphagenome]] (which compares to ENCODE-rE2G). (synthesis)
- Another model that combines sequence with measured accessibility: [[sun-2026-succeed]]; see also [[fu-2025-get]]. (synthesis)

## Open questions

- Would pseudobulk scATAC (plus imputed contacts) as input let EPInformer predict expression for rare cell types? (synthesis)
- Does attention-based linking hold beyond 100 kb if the candidate window is widened, given that performance fell at 500 kb?
- Would plugging in a pretrained DNA language model or Borzoi-style encoder, as the authors propose, help or just add cost?

## Related

- [[sequence-to-function-model]] · [[cis-regulatory-element]] · [[avsec-2021-enformer]] · [[linder-2025-borzoi]] · [[creyghton-2010-h3k27ac-enhancers]] · [[40-Topics/sequence-models-and-foundation-models]]
