---
type: summary
title: "Kelley et al. 2016 — Basset: learning the regulatory code of the accessible genome with deep convolutional neural networks"
source: "[[00-Sources/papers/Basset_ learning the regulatory code of the accessible genome with deep convolutional neural networks]]"
source_quality: full
source_sha256: "6c1d2578569b20c9f4847b088655fd99c888fc90fe4da89f13ebf8620bbfd634"
source_kind: paper
author: "David R. Kelley (corresponding), Jasper Snoek, John L. Rinn"
published: 2016-07-01
ingested: 2026-10-08
doi: "10.1101/gr.200535.115"
journal: "Genome Research 26(7):990"
tags: [Basset, sequence-to-function, convolutional-neural-network, DNase-seq, chromatin-accessibility, in-silico-mutagenesis, SAD-score, GWAS, PICS, CTCF, AP-1, transfer-learning, gkm-SVM]
entities: []
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[convolutional-neural-network]]", "[[chromatin-accessibility]]", "[[dnase-seq]]", "[[transcription-factor-motif]]", "[[de-novo-motif-discovery]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Kelley et al. (2016) — *Basset: learning the regulatory code of the accessible genome with deep convolutional neural networks* — *Genome Research* 26(7):990. [DOI](https://doi.org/10.1101/gr.200535.115)

# Kelley 2016 — Basset

> Basset is an open-source Torch7 package that trains a deep CNN to predict, from 600 bp of hg19 sequence, whether a site is a DNase I hypersensitive site in each of 164 cell types (125 ENCODE, 39 Roadmap). On held-out sites it reaches mean AUC 0.895 against 0.780 for gkm-SVM. The paper uses the trained model three ways: first-layer filters as learned motifs (45% match CIS-BP), in-silico saturation mutagenesis as per-nucleotide "loss" and "gain" scores that correlate with PhyloP conservation, and SNP accessibility difference (SAD) scores that are higher for likely causal autoimmune GWAS SNPs. It also shows that a model pretrained on public data can be adapted to a new cell type's DNase-seq in one training pass. This is the accessibility-only, cell-type-multitask design that scBasset later carried to single cells.

## Key claims

- **Accuracy over gkm-SVM.** Mean AUC 0.895 vs 0.780 for gkm-SVM; better for every cell type. Mean AUPRC 0.561 vs 0.322. At 10% false-positive rate Basset recovers 55–80% of true DHSs; at 20% FDR it recalls only 20–35%, so the authors say no tool is yet accurate enough to annotate genomes de novo.
- **Cell-specific sites are harder.** AUC drops to 0.858 on sites active in fewer than half the cells. AUC is similar across promoters (0.900), intragenic (0.884) and intergenic (0.891) sites.
- **Filters are motifs.** Of 300 first-layer filters, 45% align to CIS-BP motifs (TomTom, q < 0.1). CTCF is the most influential factor across cell types and gets 12 filters tiling its 19 bp site; AP-1 gets four. Other filters capture GC content, CpGs and poly-AT stretches. Clustering filter-influence profiles groups TP63, GRHL1 and KLF filters with epithelial cells.
- **Context beyond the motif.** Sequences with a central AP-1 motif are classified at AUC 0.86, whereas a motif-only classifier would score 0.5. In mammary fibroblasts the full consensus scores 0.49, with a 5′ T 0.25, and with a 5′ T and 3′ A 0.10. Flanking poly-AT lowers predictions; an overlapping ETS-like GGAART motif raises them.
- **Mutagenesis tracks conservation.** Genome-wide, loss scores correlate with PhyloP (Pearson 0.188, P = 4.4 × 10⁻¹⁰²); loss plus gain raises this to 0.221 (P = 3.0 × 10⁻¹⁴¹).
- **GWAS fine-mapping support.** Among 7,252 noncoding autoimmune GWAS SNPs with PICS probabilities, 235 high-PICS (≥0.5) SNPs had greater SAD means than 3,004 low-PICS (≤0.05) SNPs (Mann-Whitney P < 1.3 × 10⁻⁷), and more than seven times more high-PICS SNPs passed a mean SAD > 0.1. 31% of index SNPs had at least one LD partner with a >10% predicted change in some cell type.
- **rs4409785 example.** The C allele of this vitiligo/RA/MS SNP (PICS 85.3% for vitiligo) in a 559 kb gene desert is predicted to create a CTCF site, raising predicted accessibility in H1-hESCs from 0.8% to 73.24%. In 88 ENCODE CTCF ChIP-seq sets, all 11 cell types with significant peaks at the site sequenced the C allele.
- **Pretrain then adapt.** A model pretrained on 149 cell types (AUC 0.892) and fine-tuned for one pass on each of 15 held-out sets matched the full 164-cell model for all but one (HRCEpiC renal epithelial cells). Training took 6.5 h on a MacBook CPU or 18 min on a Tesla K20m.

## Methods / evidence

Data: ENCODE and Roadmap HotSpot DNase-seq peaks (1% FDR), extended to 600 bp and greedily merged into 2,071,886 sites; 4.1–19.0% (median 8.2%) active per cell type. Split: 1,930,000 train, 70,000 validation, 71,886 test, sampled randomly (not by chromosome). Model: three convolution layers, two fully connected layers, 164 sigmoid outputs; batch normalisation after every layer; RMSprop; early stopping after 12 epochs without improvement; architecture chosen by Bayesian optimisation (Spearmint). gkm-SVM v1.3 was trained on a 100,000-site subsample with down-sampled negatives because of its Gram matrix; on default options it took 16 days for 50 cell types. Motif PWMs are built from sequences that activate a filter above half its maximum. The PhyloP comparison uses ridge regression on 328 scores per nucleotide, restricted to nonrepetitive sequence in the central 100 bp of DHSs.

Weight: a strong, well-documented methods paper. The GWAS evaluation uses PICS fine-mapping probabilities as a proxy truth because confirmed causal noncoding variants are scarce. Figures are images in the clipping; values quoted here are from the text.

## Limitations

**Authors' own:**
- At 20% FDR Basset recalls only 20–35% of accessible sites; no tool is accurate enough to annotate large genomes de novo.
- Motifs with variable spacing between two halves were not prominently recognised by the filters.
- Many high-information filters remain unannotated; their binding proteins need future work.
- No training data to weight cell types for GWAS, so SAD means across all cell types were compared with PICS.
- The improvement seen with seeded single-cell-type training suggests the full model may need more capacity or less regularisation.

**Reviewer notes:**
- Train/test sites were split randomly rather than by chromosome, so overlapping or nearby sequence may inflate test AUC compared with DeepSEA-style chromosome hold-outs. (synthesis)
- Only peak sites enter training, so the model ranks which DHSs are open in which cell type; it is not trained on the closed genome at large. (synthesis)
- Binary peak calls in 600 bp windows ignore signal strength and distal context. (synthesis)

## Surprising or load-bearing bits

- The "gain score" idea: mutations that would create accessibility mark latent regulatory potential, and adding them improves the conservation correlation. Gain-of-function variants are invisible to annotation-overlap methods because the sequenced genome carried the inactive allele.
- Pretrain-on-public, fine-tune-on-your-cell-type is presented here in 2016, well before the "foundation model" vocabulary. (synthesis)
- CTCF dominates accessibility prediction, which ties sequence models to 3D genome architecture work; the authors cite TAD-boundary disruption studies.

## Concepts touched

- [[sequence-to-function-model]] — multitask CNN for cell-type accessibility.
- [[variant-effect-prediction]] — SAD scores validated against PICS fine-mapping.
- [[convolutional-neural-network]] — first-layer filters as PWMs, filter nullification for influence.
- [[chromatin-accessibility]] / [[dnase-seq]] — 164 cell types of DHS calls as labels.
- [[transcription-factor-motif]] / [[de-novo-motif-discovery]] — 45% of filters match CIS-BP; CTCF and AP-1 most influential.
- [[topologically-associating-domain]] — CTCF gain at rs4409785 discussed via boundary-disruption studies such as [[lupianez-2015-tad-disruption]].

## Connections to other sources

- Builds on [[zhou-2015-deepsea]] (cited as a parallel CNN success); Basset focuses on accessibility only and uses a random rather than chromosome split.
- Direct successor from the same author: [[kelley-2018-basenji]] (quantitative, 131 kb context).
- Single-cell extension of the Basset architecture: [[yuan-2022-scbasset]], which in turn is the comparator in [[fan-2026-gfetm]].
- Reviewed as a landmark model in [[angermueller-2017-genomebiol]].
- Labels come partly from [[roadmap-2015-111-epigenomes]].

## Open questions

- How much does the random site split inflate accuracy relative to chromosome hold-out? (synthesis)
- Which proteins bind the high-information unannotated filters?
- Does the one-pass fine-tuning recipe hold for sparse single-cell data, or does it need the per-cell embeddings that scBasset adds? (synthesis)

## Related

- [[sequence-to-function-model]] · [[variant-effect-prediction]] · [[chromatin-accessibility]] · [[zhou-2015-deepsea]] · [[kelley-2018-basenji]] · [[yuan-2022-scbasset]] · [[40-Topics/sequence-models-and-foundation-models]]
