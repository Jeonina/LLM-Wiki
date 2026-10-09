---
type: summary
title: "Pampari et al. 2024 — ChromBPNet: bias factorized, base-resolution deep learning models of chromatin accessibility reveal cis-regulatory sequence syntax, transcription factor footprints and regulatory variants"
source: "[[00-Sources/papers/ChromBPNet- bias factorized, base-resolution deep learning models of chromatin accessibility reveal cis-regulatory sequence syntax, transcription factor footprints and regulatory variants.pdf]]"
source_quality: full
source_sha256: "1c790097400b5103d450828217e52775b3c5bd30fea3c2c31c493dbd903b9cd5"
source_kind: paper
author: "Anusri Pampari, Anna Shcherbina, Evgeny Z. Kvon, Michael Kosicki, Surag Nair, Soumya Kundu, … , William James Greenleaf, Len A. Pennacchio, Anshul Kundaje (lead contact)"
published: 2024-12-25
ingested: 2026-10-08
doi: "10.1101/2024.12.25.630221"
journal: "bioRxiv preprint (clipped text = version posted 2026-09-23)"
tags: [ChromBPNet, BPNet, sequence-to-function, ATAC-seq, DNase-seq, Tn5-bias, DNase-I-bias, bias-correction, base-resolution, TF-footprints, TF-MoDISco, DeepLIFT, caQTL, dsQTL, bQTL, MPRA, GWAS, pseudobulk-scATAC, variant-effect-prediction, Kundaje-lab]
entities: ["[[william-greenleaf]]"]
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[convolutional-neural-network]]", "[[chromatin-accessibility]]", "[[atac-seq]]", "[[dnase-seq]]", "[[tn5-tagmentation]]", "[[transcription-factor-motif]]", "[[de-novo-motif-discovery]]", "[[cis-regulatory-element]]", "[[scatac-seq]]", "[[pseudo-bulk]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[single-cell-atac-seq]]", "[[computational-methods]]"]
---

**Citation:** Pampari et al. (2024) — *ChromBPNet: bias factorized, base-resolution deep learning models of chromatin accessibility reveal cis-regulatory sequence syntax, transcription factor footprints and regulatory variants* — *bioRxiv preprint*. [DOI](https://doi.org/10.1101/2024.12.25.630221)

# Pampari 2024 — ChromBPNet

> **Version note:** the source is the extracted text of a later bioRxiv version (posted 2026-09-23) of the December 2024 preprint. It already cites and compares against AlphaGenome. Figure panels are images in the PDF and were only partly readable as extracted text; numbers below come from the main text and Methods.
>
> ChromBPNet is a compact (~6 M parameter) [[sequence-to-function-model]] that predicts base-resolution ATAC-seq or DNase-seq cleavage profiles over 1 kb from 2,114 bp of sequence. Its key idea is **bias factorisation**: a small frozen CNN trained on non-peak background learns the enzyme's own sequence preference (Tn5 or DNase-I), and a larger BPNet-style CNN is trained on what is left. Removing the bias head yields bias-corrected profiles, footprints and contribution scores. With these, the model recovers compact TF motif lexicons, cooperative composite motifs and footprints, works on shallow and pseudobulk scATAC data, and predicts variant effects on accessibility about as well as much larger multi-task models such as Enformer — but below AlphaGenome.

## Key claims

- **Enzyme bias distorts profile shape, not total counts.** Naive BPNet models of K562 ATAC-seq learned Tn5 preference motifs in profile contribution scores but not in count contribution scores. A bias model trained on background predicted Tn5 profile shapes in peaks well (median JSD 0.48) but not total counts (r = −0.16). DNase-I bias is weaker; marginal Tn5 bias footprints were orders of magnitude stronger than DNase-I ones.
- **Bias factorisation removes the bias.** In GM12878, bias correction eliminated Tn5 motifs from profile-derived TF-MoDISco motifs and revealed latent footprints, e.g. tight footprints bookending CTCF. GATA1 motifs (a negative control; GATA not expressed in GM12878) produced footprints only in uncorrected profiles.
- **Chromatin-background bias models beat alternatives.** Naked-DNA bias models (including seq2PRINT's) left GC bias and Tn5 motifs behind; TOBIAS and HINT-ATAC pre-correction gave only partial correction. Naked-DNA vs chromatin-background Tn5 profiles over 1,000 BAC regions correlated with mean Pearson r = 0.56 (range −0.011 to 0.93). Chromatin-background bias models transferred between cell lines.
- **ATAC and DNase converge after correction.** Profile JSD between K562 ATAC and DNase was 0.81 for measured data, 0.58 for uncorrected predictions and 0.26 for bias-corrected predictions. DNase footprints were narrower (25–35 vs 35–40 bp) and deeper, but footprint depths correlated across TF motifs at r = 0.98.
- **Accuracy.** K562 held-out peaks: total-count Pearson r = 0.70 (ATAC) and 0.71 (DNase); peak vs background auROC 0.98. Other cell lines: median count r = 0.69, median profile JSD 0.62.
- **Low depth.** Subsampling a 572 M-read GM12878 ATAC dataset, measured-profile median JSD rose from 0.3 (250 M) to 0.9 (5 M), while model-imputed profiles stayed at 0.147–0.190. Motif recall was stable down to 25 M reads, then rare motifs dropped. Pseudobulk scATAC from 11,000 down to ~100 cells (250 M to 2 M reads) showed the same trends.
- **Compact lexicons.** After merging, each ENCODE Tier-1 cell line had 41–60 non-redundant predictive motifs (GM12878 51, HepG2 60, IMR90 47, H1 41, K562 47). The FOS–TEAD composite in IMR90 gave a super-additive footprint that disappeared when spacing or orientation changed. ChromBPNet motif contribution scores tracked TF occupancy from BPNet ChIP-seq models (CTCF r > 0.89), far better than peak accessibility (r = −0.1) or TOBIAS footprint scores (r = 0.2).
- **Variant effects.** New scores: logFC, JSD (profile shape change), AAQ (active allele quantile), IES and IPS. On Yoruba LCL dsQTLs, IPS reached AP 0.54 (572 M ATAC) and 0.43 (68 M DNase), against gkm-SVM 0.19 and Enformer's published scores 0.33. After the authors recomputed Enformer scores over a local 2 kb window, Enformer reached AP 0.53, beating depth-matched ChromBPNet (0.43–0.46) but not the 572 M ATAC model. Effect-size r: 0.76 (ATAC 572 M), 0.73 (DNase), Enformer revised 0.73.
- **Generalisation.** Allelic-imbalance correlation r = 0.68 in African caQTLs; variant scores correlated r = 0.96–0.97 between models from six African ancestry subgroups and 0.93–0.95 with European models. Pseudobulk scATAC models gave r = 0.6 (microglia) and 0.7 (smooth muscle) with caQTL effect sizes.
- **Beyond accessibility.** SPI1 bQTLs: AP 0.33 (DNase) vs Enformer published 0.14 and revised 0.34; ATAC models 0.37. CAGI5 MPRA: within ±0.05 of Enformer at 9 loci, substantially better at 5 of 14. Red blood cell GWAS: up to 70-fold enrichment of high-scoring variants among fine-mapped variants (PIP ≥ 0.4). A rare-disease de novo variant (chr6:14501369 A>G) predicted to cut accessibility by 40% by creating an NR2F1 repressor site abolished forebrain enhancer activity in E11.5 transgenic mice; a nearby predicted-neutral variant had no effect.

## Methods / evidence

Architecture: expanded BPNet with 512 filters and 8 dilated residual layers (receptive field 1,041 bp), input 2,114 bp, output 1,000 bp profile plus total count. Bias model: 128 filters, 4 dilated layers, 81-bp receptive field, trained on GC-matched non-peak regions below a tunable signal threshold. Two-stage training: fit and scale the frozen bias model, then train the main model on the residual. Loss: multinomial NLL on profile plus λ × MSE on log total counts (BPNet loss). Tn5 shift +4/−4 and DNase-I shift 0/+1 chosen by aligning strand-specific bias PWMs. Data: ATAC and DNase from five ENCODE Tier-1 lines (K562, HepG2, GM12878, IMR90, H1-hESC), 5-fold chromosome cross-validation, peaks plus non-peaks at a 1:10 non-peak:peak ratio, ±500 bp jitter, Adam (lr 0.001), early stopping. Interpretation: DeepLIFT/DeepSHAP, TF-MoDISco (modisco-lite), marginal footprinting. Code: github.com/kundajelab/chrombpnet; models on ENCODE and Synapse.

Weight: a thorough methods paper with careful negative controls (GATA1 in GM12878, bias-model motif audits) and many independent QTL benchmarks. The fairest comparison to Enformer required the authors to recompute Enformer's scores, after which Enformer won on classification at matched depth. Benchmarks are restricted to local, in-peak SNVs.

## Limitations

**Authors' own:**
- Total-accessibility predictions lag pseudo-replicate concordance and long-context models; local context predicts profile shape well, but distal context matters for total accessibility. Predictions are less reliable outside peaks.
- Sensitivity to rare motifs and variant classification fall notably below 25 M reads, though effect-size prediction stays robust.
- One model per cell state or biosample; no joint cis/trans modelling yet.
- Cannot reveal "settler" TFs that bind open chromatin without changing accessibility.
- Benchmarks cover only local in-peak QTLs and SNVs; distal chromatin QTLs, eQTLs, indels and STRs were not tested; control variants were restricted to peaks.
- Consistently underperforms AlphaGenome; multi-task models across contexts can learn causally inconsistent features, which the authors flag as a caution for that route.

**Reviewer notes:**
- The bias model must be checked per experiment; the authors provide diagnostics, but misuse with a contaminated bias model would quietly leak TF motifs into "bias". (synthesis)
- The 572 M-read GM12878 ATAC set is far deeper than most datasets, so the best headline numbers are not typical of what users will get. (synthesis)
- Pseudobulk scATAC at ~100 cells is shown to work for imputation, but variant classification at that depth (comparable to 2–5 M reads) is clearly weaker. (synthesis)

## Surprising or load-bearing bits

- A ~6 M-parameter, 2-kb-context single-task CNN is competitive with a ~250 M-parameter multi-task transformer (Enformer) on local accessibility QTLs.
- The authors found that Enformer's published variant scores, summed over ~100 kb, diluted local effects; a local 2 kb score fixed much of the gap. Scoring choices can swing benchmarks as much as architecture.
- Bias correction makes ATAC and DNase footprints agree, which means footprint depth can be read as a TF property (deep CTCF, NRF1, BACH; shallow NFYB, STAT5) rather than an assay property.
- For scATAC users, pseudobulk ChromBPNet models of rare cell types give bias-corrected footprints and motif maps that raw sparse data cannot. (synthesis)
- The authors state ChromBPNet outperforms large DNA language models at predicting accessibility QTLs, citing a separate benchmark.

## Entities mentioned

- [[william-greenleaf]] — co-author (Stanford; ATAC-seq developer lab).

## Concepts touched

- [[sequence-to-function-model]] — local, base-resolution, single-task design; bias factorisation as a modular add-on.
- [[variant-effect-prediction]] — dsQTL, caQTL, bQTL, MPRA, GWAS and de novo variant benchmarks; new JSD/AAQ/IPS scores.
- [[tn5-tagmentation]] — Tn5 sequence preference modelled and removed; +4/−4 shift recommended.
- [[atac-seq]] / [[dnase-seq]] / [[chromatin-accessibility]] — both assays modelled; footprint differences linked to enzyme size.
- [[transcription-factor-motif]] / [[de-novo-motif-discovery]] — TF-MoDISco lexicons, composite elements, marginal footprints.
- [[convolutional-neural-network]] — dilated-residual CNN; authors argue further architecture changes add little.
- [[scatac-seq]] / [[pseudo-bulk]] / [[sequencing-depth-and-coverage]] — training on pseudobulk down to ~100 cells.
- [[cis-regulatory-element]] — motif syntax of accessible cREs.

## Connections to other sources

- Benchmarks against [[avsec-2021-enformer]] and is in turn outperformed by [[avsec-2026-alphagenome]], which uses ChromBPNet's QTL benchmarks.
- Shares the BPNet count/profile loss decomposition used by [[linder-2025-borzoi]].
- Peak-level CNN predecessors: [[kelley-2016-basset]], [[zhou-2015-deepsea]]. scATAC sequence model in the same space: [[yuan-2022-scbasset]].
- Motif-deviation alternative for scATAC: [[schep-2017-chromvar]]. ATAC origin context: [[buenrostro-2015-nature]].
- Cell-type-resolved scATAC sequence models in this ingest: [[kempynck-2026-crested]].

## Open questions

- Can stage-wise training grow long-context models from pretrained local ChromBPNet models, as the authors propose?
- How do bias-corrected footprints behave on very sparse single-cell data where only a handful of reads cover each peak per cell type? (synthesis)
- Would a single model across cell states that takes regulator expression as input (a cis+trans "foundation" model, as the authors suggest) keep the causal consistency that single-task models have?

## Related

- [[sequence-to-function-model]] · [[variant-effect-prediction]] · [[tn5-tagmentation]] · [[atac-seq]] · [[avsec-2026-alphagenome]] · [[yuan-2022-scbasset]] · [[40-Topics/sequence-models-and-foundation-models]]
