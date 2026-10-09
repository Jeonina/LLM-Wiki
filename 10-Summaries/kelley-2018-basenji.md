---
type: summary
title: "Kelley et al. 2018 — Sequential regulatory activity prediction across chromosomes with convolutional neural networks"
source: "[[00-Sources/papers/Sequential regulatory activity prediction across chromosomes with convolutional neural networks]]"
source_quality: full
source_sha256: "ac17e67a0edd0762f16071184c2b395b0a6753c87d6779a025be854b32075905"
source_kind: paper
author: "David R. Kelley (corresponding), Yakir A. Reshef, Maxwell Bileschi, David Belanger, Cory Y. McLean, Jasper Snoek"
published: 2018-05-01
ingested: 2026-10-08
doi: "10.1101/gr.227819.117"
journal: "Genome Research 28(5):739"
tags: [Basenji, sequence-to-function, convolutional-neural-network, dilated-convolution, CAGE, gene-expression-prediction, DNase-seq, ChIP-seq, multimapping-reads, eQTL, GTEx, SED-score, saliency, Calico]
entities: []
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[convolutional-neural-network]]", "[[chromatin-accessibility]]", "[[cis-regulatory-element]]", "[[enhancer-states]]", "[[transcription-factor-motif]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[histone-modifications]]", "[[computational-methods]]"]
---

**Citation:** Kelley et al. (2018) — *Sequential regulatory activity prediction across chromosomes with convolutional neural networks* — *Genome Research* 28(5):739. [DOI](https://doi.org/10.1101/gr.227819.117)

# Kelley 2018 — Basenji

> Basenji changes the Basset recipe in two ways: it reads 131 kb of sequence instead of ~600 bp, and it predicts quantitative read coverage in 128 bp bins instead of a binary peak call. Standard convolution and pooling compress the sequence to 128 bp bins, seven densely connected dilated convolution layers spread information over a ~32 kb receptive field, and a width-one convolution predicts 4,229 coverage tracks (ENCODE and Roadmap DNase-seq and histone ChIP-seq, FANTOM5 CAGE) with a Poisson loss. The authors reprocessed all raw reads to keep multimapping reads and correct GC bias. Basenji predicts CAGE expression at held-out gene TSSs with mean Pearson r 0.85 (0.77 for nonzero genes), its predictions often correlate with experiments better than replicates do, and its SNP expression difference (SED) scores enrich for GTEx eQTLs 3.2–5.8× in the top quantile. It is the first of the long-context, coverage-predicting models that lead to Enformer and Borzoi.

## Key claims

- **Quantitative tracks are predictable from sequence, unevenly.** Variance explained is highest for DNase-seq and ChIP-seq of active marks and lowest for broad domains such as H3K79me2 and H3K9me3. Predictions are shrunk: overestimated at low coverage, underestimated at high.
- **Beats Basset on Basset's own task.** On 949 DNase-seq experiments converted to binary peaks in 1,024 bp windows, Basenji raised mean AUPRC from 0.435 to 0.577 (median 0.449 to 0.591) for every experiment. The authors note these numbers are not comparable to the Basset paper because sequences here are unbiased genome samples, not DHSs.
- **Predictions vs replicates.** Across 1,284 replicated experiments, mean and median prediction–experiment correlation exceeded replicate–replicate correlation (paired t-test P < 2 × 10⁻⁷⁸); cross-replicate predictions also exceeded it (P < 7 × 10⁻⁷). The explanation is implicit denoising. For the most consistent datasets, especially CAGE, predictions fall short of replicate agreement.
- **Receptive field matters.** Models with one to seven dilated layers improved monotonically for all data types.
- **Gene expression.** For held-out genes, log2 CAGE predictions at TSS bins correlate with experiment at mean r 0.85 (median 0.86); 0.77 (median 0.78) for nonzero genes. Accuracy rises with CAGE depth. For the most cell-type-variable quartile of genes, correlation falls from mean 0.3673 (third quartile) to 0.2708. Expression clusters across cell types agree weakly but significantly (ARI mean 0.107). For 201 genes with alternative TSSs >500 bp apart, predicted vs observed TSS-switch fold changes correlate at mean 0.295.
- **Distal elements.** Gradient-based saliency on 128 bp bins recovers ENCODE promoters, enhancers and CTCF sites in GM12878 (KS P = 9 × 10⁻⁶⁴, 2 × 10⁻¹⁸³, 4 × 10⁻⁶¹). At PIM1 it finds two annotated enhancers, one with POU2F motifs and one with two PU.1 motifs; POU2F1/POU2F2 siRNA knockdowns in GM19238 changed PIM1 expression (P = 0.026 and 0.066). Promoters show strong negative (repressive) saliency segments.
- **eQTL enrichment.** SED scores, projected through 1000 Genomes EUR LD as SED-LD, correlate with GTEx V6p eQTL χ² in all 19 CAGE-matched tissues (P < 1 × 10⁻⁵⁴ on LD-pruned chr1 variants) after controlling for LD score; the top quantile has 3.2–5.8× more significant eQTLs than the bottom three, robust to TSS distance.
- **GWAS.** On DeepSEA's 12,296 GWAS Catalog SNPs and matched negatives (same 10 folds), logistic regression on 128 PCs of Basenji features gave AUROC 0.666 vs 0.657 for DeepSEA with conservation (P < 0.10); combining both reached 0.706 (P < 1.6 × 10⁻⁵).
- **MS locus example.** Among 1,170 PICS-fine-mapped autoimmune and blood-trait loci, 67 contained a variant predicted to change CAGE >10%. rs78461372 (PICS 5%, linked to lead rs74796499 at 24%) is predicted to raise GPR65 transcription by strengthening an ETS motif next to a RUNX motif; GTEx confirms a larger effect for rs78461372 (beta 0.75, P = 1.8 × 10⁻⁹) than for the lead variant (beta 0.66, P = 4.9 × 10⁻⁷). The same motifs are predicted to repress in insular cortex.

## Methods / evidence

Data: FASTQ for 973 FANTOM5 CAGE, 593 ENCODE DNase-seq, 1,704 ENCODE histone ChIP-seq, 356 Roadmap DNase-seq and 603 Roadmap histone ChIP-seq experiments; Bowtie 2 with up to 10 multimapping alignments, apportioned by an EM algorithm assuming smooth coverage; GC bias removed with a third-degree polynomial on a Gaussian-weighted GC estimate. Genome cut into 14,533 non-overlapping 131 kb sequences (>35% unmappable discarded), split randomly 90/5/5. Architecture: four convolution layers pooling by 2, 4, 4, 4 to 128 bp; seven densely connected dilated layers; final width-one convolution; batch norm, ReLU, dropout; Poisson log-likelihood; Adam; hyperparameters by GPyOpt Bayesian optimisation; reverse-complement and ±3 nt shift augmentation, averaged at test. The 128 bp bin was chosen as the power of two nearest the 146 bp nucleosome spacing. Saliency = dot product of bin representation and gradient of summed prediction. Code: github.com/calico/basenji.

Weight: a careful paper with an honest comparison design (Basset retrained on the same genome-wide split). Validation of variant effects relies on population eQTL enrichment and one GWAS case study, not on direct perturbation.

## Limitations

**Authors' own:**
- Dataset quality varies; accuracy rises with sequencing depth and replicate consistency, and repressive marks (H3K9me3, H3K27me3) have low replicate consistency.
- Most samples are cell lines or heterogeneous tissues.
- The multitask scheme treats every experiment as independent; more structured sharing may help.
- Training assumes the reference genome underlies every experiment; sample-specific genomes are mostly unavailable.
- The ~32 kb receptive field captures many but not all distal elements.
- Basenji models transcription only, not post-transcriptional regulation.

**Reviewer notes:**
- The train/validation/test split is random over 131 kb blocks, not by chromosome, so homologous or paralogous sequence may leak across sets. (synthesis)
- The GWAS gain over DeepSEA (0.666 vs 0.657) is not significant at conventional thresholds (P < 0.10); the clearer result is that the two are complementary (0.706 combined). (synthesis)
- CAGE measures TSS activity; the expression benchmark is therefore a TSS-coverage task, not RNA abundance. (synthesis)

## Surprising or load-bearing bits

- Predictions out-correlating replicates is a recurring claim in later sequence-to-function papers; here it is explained as the model smoothing measurement noise, not as superhuman accuracy.
- Reprocessing raw reads to keep multimappers matters because consortium pipelines discard them, leaving roughly half the genome incompletely annotated, including repeats the authors consider regulatory.
- The same motif pair is predicted to activate GPR65 in immune cells and repress it in brain, a cell-type-dependent sign flip from sequence alone.

## Concepts touched

- [[sequence-to-function-model]] — move from binary peaks on short windows to quantitative coverage on 131 kb.
- [[variant-effect-prediction]] — SED and SED-LD scores tested against GTEx eQTLs and GWAS Catalog SNPs.
- [[convolutional-neural-network]] — dilated, densely connected convolutions for a ~32 kb receptive field.
- [[cis-regulatory-element]] / [[enhancer-states]] — saliency maps detect promoters, enhancers and CTCF sites and give a signed (activating vs repressive) score.
- [[transcription-factor-motif]] — POU2F, PU.1, ETS and RUNX motifs found by in-silico mutagenesis.
- [[chromatin-accessibility]] — 949 DNase-seq tracks predicted as coverage.

## Connections to other sources

- Extends [[kelley-2016-basset]] (same author) and is benchmarked against [[zhou-2015-deepsea]] on the DeepSEA GWAS set.
- Akita ([[fudenberg-2020-akita]]) reuses Basenji's dilated-residual trunk for contact maps.
- Long-context successors: [[avsec-2021-enformer]], [[linder-2025-borzoi]], [[avsec-2026-alphagenome]].
- Contemporary expression model from the DeepSEA group: [[zhou-2018-expecto]], which uses a different design (fixed 40 kb window, linear spatial features).
- Peak calling for the Basset comparison follows the MACS approach in [[zhang-2008-macs]].

## Open questions

- How much of the gain over Basset comes from quantitative targets vs longer context vs reprocessed data? The paper does not separate them. (synthesis)
- Does the eQTL enrichment hold for variants far beyond the 32 kb receptive field? The authors expect diminishing returns given GTEx effect-distance trends.
- Would sample-matched genomes for training improve accuracy as the authors suggest?

## Related

- [[sequence-to-function-model]] · [[variant-effect-prediction]] · [[kelley-2016-basset]] · [[avsec-2021-enformer]] · [[fudenberg-2020-akita]] · [[40-Topics/sequence-models-and-foundation-models]]
