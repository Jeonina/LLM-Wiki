---
type: summary
title: "Chen et al. 2022 — A sequence-based global map of regulatory activity for deciphering human genetics"
source: "[[00-Sources/papers/A sequence-based global map of regulatory activity for deciphering human genetics]]"
source_quality: full
source_sha256: "4c6a2264ebbc556b389d4812b678294b1411cb22d61168290cb4b04c29b64ea4"
source_kind: paper
author: "Kathleen M. Chen, Aaron K. Wong, Olga G. Troyanskaya (corresponding), Jian Zhou (corresponding)"
published: 2022-07-11
ingested: 2026-10-08
doi: "10.1038/s41588-022-01102-2"
journal: "Nature Genetics"
tags: [Sei, sequence-classes, sequence-to-function, convolutional-neural-network, Cistrome, chromatin-profile-prediction, variant-effect-prediction, enhancer, Polycomb, LD-score-regression, UK-Biobank, GTEx, HGMD, gain-of-function, Louvain]
entities: []
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[convolutional-neural-network]]", "[[enhancer-states]]", "[[cis-regulatory-element]]", "[[chip-seq]]", "[[chromatin-accessibility]]", "[[clustering-algorithms]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[histone-modifications]]", "[[computational-methods]]"]
---

**Citation:** Chen et al. (2022) — *A sequence-based global map of regulatory activity for deciphering human genetics* — *Nature Genetics*. [DOI](https://doi.org/10.1038/s41588-022-01102-2)

# Chen 2022 — Sei

> Sei has two parts. The Sei model is a CNN that reads 4 kb of hg38 sequence and predicts 21,907 binary chromatin-profile peaks at the centre position (9,471 TF, 10,064 histone mark and 2,372 accessibility profiles; ~1,000 DNA-binding proteins, 77 histone marks, >1,300 cell lines and tissues, mostly from Cistrome). The "sequence classes" are then built by running the model over 30 million 4 kb windows tiling the genome, reducing the predictions by PCA and Louvain-clustering them into 40 classes that cover >97.4% of the genome: promoter (P), 12 enhancer classes (E1–E12, many cell-type-specific), CTCF, TF, Polycomb (PC), heterochromatin (HET), transcription (TN) and low-signal (L). Any sequence or variant can be scored against these classes by projection, giving a directional, interpretable variant effect such as "decreases liver/intestine enhancer activity". The paper uses the classes to explain tissue-specific expression and eQTL direction, show bidirectional selection on enhancer effects, partition UK Biobank heritability into non-overlapping categories, and propose mechanisms for 853 HGMD regulatory mutations, about 20% of which are predicted gain-of-function.

## Key claims

- **Broadest chromatin model.** Average AUROC 0.972 and AUPRC 0.409 over 21,907 profiles on held-out chr8 and chr9; predictions reproduce the profiles' correlation structure. On the 2,002 profiles shared with DeepSEA Beluga, Sei improves AUROC/(1 − AUROC) by 19% on average.
- **A map of regulatory activity.** Embedding the 30 million windows places low-activity sequence at the centre with specific activities radiating outward; tissue-specific enhancers group by tissue, Polycomb sits next to H3K9me3 heterochromatin, and promoter and CTCF–cohesin sequences form separate clusters. Classes are robust to clustering parameters and concordant with classes built from measured profiles.
- **Enhancer classes are cell-type-specific.** E7 monocyte/macrophage (PU.1/SPI1), E9 liver/intestine, E1 embryonic stem cell/iPSC (SOX2/NANOG/POU5F1), E10 and E3 brain, E12 erythroblast-like, E5 B-cell-like, E11 T cell; E2, E4 and E8 are multi-tissue. E-class coverage within 10 kb of a TSS correlates with differential expression in the matching tissue.
- **Directional eQTL effects.** For GTEx v8 eQTLs within 5 kb of TSSs, variants predicted to increase E-class activity correlate with higher expression; those increasing PC-class activity correlate with lower expression. Correlations are higher for fine-mapped eQTLs (PIP > 0.95).
- **Selection.** Variants in E, P and CTCF classes are less often common, and variants with stronger predicted effects on these classes are less often common still. E4, E2 and E10 show the strongest association. Enhancer and promoter effects are constrained in both directions; for CTCF only decreasing effects are strongly constrained. HET, PC, TF and L classes show weak signatures.
- **Non-overlapping heritability partition.** Across 47 UK Biobank traits, E and P classes explain most heritability. Blood traits map to matching blood enhancer classes (E7 for monocyte count; E5, E11, E7 for autoimmune traits; E12 for red cell traits); cognitive and behavioural traits map to E10, E3 and E1; height, waist–hip ratio, balding, lung FVC and heel T-score map to multi-tissue E4, E2 and E8; high cholesterol maps to E9. P explains a sizable share in nearly all traits. Conditioning on baseline annotations leaves 83 significant class–trait associations, covering 33 of 47 traits and 9 of 13 E and P classes.
- **Disease mutations.** Mean maximum absolute effect for 853 HGMD regulatory mutations is 0.903, 4.2× that of de novo mutations in healthy individuals (0.217) and 6.5× that of common variants (0.139). Of the 138 strongest (>1.1), ~80% decrease and ~20% increase class activity; 44.9% hit E classes, 38.4% P and 15.9% CTCF–cohesin. Strong E-class mutations almost always hit the class matching the disease tissue (e.g., protein C deficiency and haemophilia B decrease E9; an SHH limb enhancer mutation decreases E1).
- **Gain-of-function examples.** The largest increase is a CTCF-class gain near XIST that skews X-inactivation (validated CTCF binding increase); an α-thalassaemia variant near HBM that creates a GATA1 site increases E12; a familial melanoma TERT promoter variant increases P; a hereditary persistence of fetal haemoglobin variant near HBG1, which creates a POU-family octamer, is predicted to increase E12.

## Methods / evidence

Training data: 21,907 peak-format profiles (19,905 from Cistrome, excluding those with <1,000 peaks; the rest ENCODE and Roadmap), hg38. Architecture: convolution blocks with dual linear and nonlinear paths joined by residual connections, residual dilated convolutions, then a B-spline spatial basis (256 spatial bins → 16 basis dimensions) instead of a large fully connected layer, a fully connected layer and 21,907 outputs. Training with on-the-fly sampling in Selene (PyTorch); chr8 and chr9 test, chr10 validation; ENCODE blacklist excluded. Sequence classes: 30 million predictions → incremental PCA (top 180 PCs) → k = 14 nearest-neighbour graph → Louvain gave 61 clusters, the largest 40 kept (the other 21 are <2.6% of the genome, mostly L/HET-like). Class score = projection onto the unit vector of the class's mean prediction; variant effect = alt minus ref score, with histone predictions renormalised by total histone signal as a nucleosome-occupancy proxy. Heritability: stratified LD score regression with only class annotations plus an all-ones baseline; conservative estimate = proportion minus one SE, floored at zero. Code: github.com/FunctionLab/sei-framework; web server hb.flatironinstitute.org/sei.

Weight: large, carefully held-out model plus an interpretation layer that is genuinely useful for genetics. Most class-level claims are enrichments and correlations; individual mutation mechanisms are hypotheses except where prior experiments exist. The figure panels (class activity heatmaps, selection plots, heritability matrix) are images in the clipping, so per-class numbers beyond the text are not reported here.

## Limitations

**Authors' own:**
- The high share of P-class mutations among strong HGMD effects likely reflects both biology and the historical focus on promoter-proximal mutations.
- L sequence classes lack an intuitive biological interpretation and are excluded from variant-effect analyses; L and HET are excluded from the eQTL analysis.
- The 21 smallest Louvain clusters are dropped because of size.
- Weak selection signatures for PC, TF and HET classes do not mean these activities are inessential; PC and TF regulation likely act through E and P classes.
- Predicted mechanisms for individual mutations remain to be tested experimentally.

**Reviewer notes:**
- The model predicts binary peak presence at one centre position, so "activity" is a probability of being in a peak, not a quantitative signal. (synthesis)
- Sequence classes are defined by clustering the model's own predictions; downstream associations inherit any systematic model biases, though the authors report concordance with classes built from measured profiles. (synthesis)
- Class labels depend on which cell types are well profiled in Cistrome; under-profiled tissues may be folded into broad multi-tissue classes. (synthesis)

## Surprising or load-bearing bits

- Asymmetric selection on CTCF: losing CTCF activity is constrained, gaining it is tolerated, unlike enhancers and promoters where both directions are constrained.
- One in five strong-effect pathogenic regulatory mutations is predicted gain-of-function, a class that annotation-overlap methods cannot see.
- The histone-mark nucleosome-occupancy correction shows a practical pitfall: a promoter loss-of-function can raise predicted H3K4me3 by raising nucleosome occupancy.
- Non-overlapping classes let heritability be partitioned cleanly, which overlapping annotations in standard LDSC cannot do.

## Concepts touched

- [[sequence-to-function-model]] — 21,907-output CNN plus an interpretable class layer on top.
- [[variant-effect-prediction]] — directional class-level scores; GoF vs LoF; HGMD, eQTL, heritability.
- [[enhancer-states]] — 12 enhancer classes with cell-type activity and Polycomb repression in inactive cell types.
- [[cis-regulatory-element]] — promoter, enhancer, CTCF classes cover nearly all GWAS heritability.
- [[chip-seq]] / [[chromatin-accessibility]] — Cistrome-scale TF, histone and accessibility labels.
- [[clustering-algorithms]] — Louvain on a kNN graph of model predictions defines the vocabulary.
- [[convolutional-neural-network]] — dual linear/nonlinear residual blocks and B-spline spatial basis.

## Connections to other sources

- Same lab lineage: [[zhou-2015-deepsea]] (919 profiles) → [[zhou-2018-expecto]] (2,002 profiles; DeepSEA Beluga appears to be this 2,002-profile model (synthesis)) → Sei (21,907 profiles).
- Sei's encoder design is reused in [[zhou-2022-orca]].
- Sequence classes parallel chromatin-state segmentation in [[roadmap-2015-111-epigenomes]] but are defined from sequence, so they apply to variants. (synthesis)
- Gain-of-function scoring echoes the "gain score" idea in [[kelley-2016-basset]]. (synthesis)
- The UMAP visualisation uses [[mcinnes-2018-umap]].

## Open questions

- Do predicted cell-type-specific enhancer disruptions for HGMD mutations hold up in reporter or editing assays in the matching cell type?
- How stable are the 40 classes when the profile compendium grows or shifts toward single-cell data? (synthesis)
- Would quantitative (signal) training targets change class boundaries or variant-effect magnitudes? (synthesis)

## Related

- [[sequence-to-function-model]] · [[variant-effect-prediction]] · [[enhancer-states]] · [[zhou-2015-deepsea]] · [[zhou-2018-expecto]] · [[zhou-2022-orca]] · [[40-Topics/sequence-models-and-foundation-models]]
