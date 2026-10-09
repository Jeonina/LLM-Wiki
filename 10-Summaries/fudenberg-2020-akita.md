---
type: summary
title: "Fudenberg et al. 2020 — Predicting 3D genome folding from DNA sequence with Akita"
source: "[[00-Sources/papers/Predicting 3D genome folding from DNA sequence with Akita]]"
source_quality: full
source_sha256: "87b53a06574019458e20079d6b8c3dfe45d9d2f00e3a30b724f44c4a6240b318"
source_kind: paper
author: "Geoff Fudenberg (corresponding), David R. Kelley (corresponding), Katherine S. Pollard (corresponding)"
published: 2020-10-12
ingested: 2026-10-08
doi: "10.1038/s41592-020-0958-x"
journal: "Nature Methods"
tags: [Akita, sequence-to-function, convolutional-neural-network, Hi-C, Micro-C, contact-map-prediction, CTCF, loop-extrusion, in-silico-mutagenesis, structural-variants, B2-SINE, eQTL, Basenji, Calico]
entities: []
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[convolutional-neural-network]]", "[[topologically-associating-domain]]", "[[chromatin-loop]]", "[[micro-c]]", "[[structural-variants]]", "[[transposable-elements]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[3d-genome]]", "[[chromatin-architecture]]"]
---

**Citation:** Fudenberg et al. (2020) — *Predicting 3D genome folding from DNA sequence with Akita* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-020-0958-x)

# Fudenberg 2020 — Akita

> Akita is a CNN that takes ~1 Mb (2²⁰ bp) of DNA and predicts the log(observed/expected) Hi-C or Micro-C contact map for all pairs of 2,048 bp bins in that window. A Basenji-style 1D trunk (convolutions, then dilated residual convolutions) produces 512 bin vectors; a 2D head averages each bin pair, adds a distance encoding, and runs symmetrised dilated residual 2D convolutions. Trained jointly on five high-quality human datasets with only 746,149 parameters, it reaches Pearson R 0.61 on held-out regions, close to the read-splitting replicate limit. Because predictions take seconds, the authors use in-silico mutagenesis to show that CTCF dominates folding in an orientation-dependent way, that nucleotides beyond the core motif matter, that fine-mapped eQTLs disrupt predicted folding more, that an engineered Lmo2 deletion and an Epha4 inversion are reproduced, and that B2 SINE CTCF sites in mouse are buffered. Akita predicts little cell-type specificity.

## Key claims

- **Folding is predictable from sequence.** On the held-out test set: MSE 0.14, Pearson R 0.61, Spearman R 0.56, approaching the limit from splitting reads into two pseudo-replicates (which was itself a stricter bar than biological replicates for HFF). Low-correlation maps were often correct predictions of featureless experimental maps. Predictions align with called TAD boundaries and dots.
- **Multitask helps.** Joint training on five datasets beat single-dataset models for all but the best dataset (H1-hESC).
- **CTCF and orientation.** Mutating all CTCF motifs in a region weakens locus-specific patterns, resembling acute CTCF degradation; some patterns persist at DHSs without strong CTCF binding. Inverting all CTCF motifs redistributes rather than removes contacts. Across all JASPAR motifs, CTCF has the largest effect, CTCFL second; other motifs either do little or their effect tracks overlap with CTCF motifs. NR3C2 motifs cover a similar number of bases as CTCF but barely matter; YY1 shows little genome-wide impact.
- **Beyond the core motif.** Saturation mutagenesis of 500 bp around 500 strong CTCF motifs shows large effects in the motif and elevated effects in flanks, decaying with distance; disruption correlates moderately with phyloP inside and next to motifs and varies widely for a given FIMO motif-score change. Among 100,000 uniformly spaced random mutations in the 241 Mb test set, CTCF motifs and flanks, promoters and enhancers score highest, but 19.9% of high-impact mutations fall outside these annotations. Mutating cohesin (Rad21) peaks with CTCF motifs masked still disrupts maps.
- **eQTLs.** For SuSiE-fine-mapped GTEx v8 whole-blood eQTLs (1,906 with PP > 0.9; 29,112 total), predicted folding disruption is larger for higher causal PP, both inside and outside CTCF motifs. One non-CTCF variant alters an uncharacterised motif 70 bp from a CTCF site and is predicted to strengthen a boundary (~2% contact change).
- **Engineered variants.** An in-silico ~25 kb deletion of the three-CTCF-site Lmo2 boundary in HEK293T merges the flanking domains as in 5C data; deleting any single site barely changes predictions, implying a redundant boundary. A mouse-trained model reproduces the flipped "flare" after a ~622 kb inversion at the Epha4 locus seen by Capture-C (using the mESC output, as limb-bud data were not available for training).
- **Cross-species.** The human-trained model on mouse sequence gives median Spearman R 0.50 against mESC Hi-C; errors increase with B2 SINE count, and masking B2 SINEs raises it to 0.55. A mouse-trained model reaches 0.63 and is not helped by masking (0.62), meaning it learned that CTCF sites inside B2 SINEs have little effect, consistent with ChAHP blocking CTCF binding there.
- **Limited cell-type specificity.** Predictions for different cell types correlate more strongly with each other than the experiments do; predicted cell-type differences correlate only weakly with observed ones. The model mostly tunes overall dynamic range rather than gaining or losing specific features.

## Methods / evidence

Targets: five human Hi-C/Micro-C datasets (from Krietenstein et al. and Rao et al.; including HFF and H1-hESC Micro-C) reprocessed with distiller to hg38 at 2,048 bp, ICE-balanced with cooler, then adaptively coarse-grained, distance-normalised, natural-log, clipped to (−2, 2), missing bins linearly interpolated (critical; zero-filling did much worse) and Gaussian-smoothed. Genome split into 10 Mb virtual contigs assigned 80/10/10; 7,008 training, 419 validation and 413 test sequences. Trunk: 96 filters of width 11, a pooling tower to 512 × 2,048 bp bins, dilated residual tower, 64-filter bottleneck. Head: pairwise averaging (slightly better than dot, geometric mean, max or concatenation), |i − j| encoding, 2D dilated residual blocks resymmetrised each iteration, linear output for five targets. MSE on the upper triangle; SGD with momentum, batch size 2, ~60 epochs; ±11 bp shifts and reverse-complement with map flipping; Dragonfly Bayesian hyperparameter search. Disruption score = L2 norm of the reference-minus-alternative predicted map, averaged across outputs. Deletions are made by extending the window symmetrically to keep 1 Mb. Code: github.com/calico/basenji/tree/master/manuscripts/akita.

Weight: a careful, well-controlled methods paper with several in-silico perturbation designs and two engineered-variant validations. The Lmo2 and Epha4 cases are single loci, and the eQTL result is an enrichment, not a mechanism.

## Limitations

**Authors' own:**
- Predictions cover ~1 Mb windows and ignore information beyond them; distal contacts and A/B compartments are out of scope.
- Akita must be trained on Hi-C or Micro-C for any cell type where perturbation predictions are wanted.
- Cell-type specificity is limited, likely constrained by the number of loci with strong cell-type differences in current data.
- Even the best datasets limit accuracy through sequencing depth.
- The best architectures to reflect loop extrusion remain open; deepC, a similar contemporaneous CNN, differs in head, preprocessing and training.

**Reviewer notes:**
- Random contig assignment (not by chromosome) and an 80/10/10 split leave room for paralogous or repeat sequence shared across sets. (synthesis)
- Targets are heavily processed (clipped, interpolated, smoothed), so the model predicts a denoised locus-specific pattern, not raw contact frequencies; disruption magnitudes are relative. (synthesis)
- Training uses bulk Hi-C/Micro-C; nothing here tests whether sequence predicts the cell-to-cell variability seen in single-cell Hi-C. (synthesis)

## Surprising or load-bearing bits

- One-fifth of high-impact single-nucleotide changes fall outside CTCF, promoter and enhancer annotations, pointing to uncharacterised folding sequences.
- The B2 SINE experiment shows a sequence model failing for a biologically interpretable reason (no B2 SINEs in human training data) and then succeeding when trained on mouse.
- The small parameter count (746,149) contrasts with the much larger long-context models that followed. (synthesis)

## Concepts touched

- [[sequence-to-function-model]] — extends 1D track prediction to 2D contact maps.
- [[variant-effect-prediction]] — disruption scores for SNVs, eQTLs, deletions and inversions.
- [[topologically-associating-domain]] / [[chromatin-loop]] — predicted boundaries and dots; redundant CTCF boundary at Lmo2.
- [[micro-c]] — HFF and H1-hESC Micro-C among the five targets; mESC Micro-C for the mouse model.
- [[structural-variants]] — in-silico deletions and inversions recapitulate engineered rearrangements.
- [[transposable-elements]] — B2 SINE CTCF sites buffered in mouse.
- [[convolutional-neural-network]] — Basenji trunk plus a 2D dilated-residual head.

## Connections to other sources

- Built on [[kelley-2018-basenji]] (trunk architecture, same software).
- Kilobase-to-chromosome successor that compares against Akita: [[zhou-2022-orca]].
- Training data lineage: [[hsieh-2015-micro-c]], [[rao-2014-in-situ-hic]]; processing with [[abdennur-2020-cooler]]; visualisation help from the HiGlass authors ([[kerpedjiev-2018-higlass]]).
- TAD-boundary disruption by deletion and inversion parallels [[lupianez-2015-tad-disruption]] and the SV–3D genome review [[spielmann-2018-sv-3d-genome]].
- Later sequence-to-contact work in this ingest: [[fang-2025-evo2hic]], [[wang-2026-hicfoundation]]. (synthesis)
- For the single-cell side of 3D genome analysis see [[single-cell-hi-c]] and [[zhang-2022-higashi]]. (synthesis)

## Open questions

- What are the uncharacterised sequences behind the 19.9% of high-impact mutations outside known annotations?
- Can more cell types and better architectures produce real cell-type-specific folding predictions?
- Would an architecture that mirrors loop extrusion generalise better than dilated convolutions?

## Related

- [[sequence-to-function-model]] · [[topologically-associating-domain]] · [[kelley-2018-basenji]] · [[zhou-2022-orca]] · [[40-Topics/3d-genome]] · [[40-Topics/sequence-models-and-foundation-models]]
