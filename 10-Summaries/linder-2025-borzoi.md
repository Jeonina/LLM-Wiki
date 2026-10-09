---
type: summary
title: "Linder et al. 2025 — Predicting RNA-seq coverage from DNA sequence as a unifying model of gene regulation"
source: "[[00-Sources/papers/Predicting RNA-seq coverage from DNA sequence as a unifying model of gene regulation]]"
source_quality: full
source_sha256: "2c93e0d2c187bdebcb94cd4d1f00ef828448fb35a942ced2974d7893a0ec397e"
source_kind: paper
author: "Johannes Linder, Divyanshi Srivastava, Han Yuan, Vikram Agarwal, David R. Kelley"
published: 2025-01-08
ingested: 2026-10-08
doi: "10.1038/s41588-024-02053-6"
journal: "Nature Genetics"
tags: [Borzoi, sequence-to-function, RNA-seq-coverage, Enformer, U-net, transformer, splicing, polyadenylation, APA, eQTL, sQTL, paQTL, enhancer-gene, TRIP, variant-effect-prediction, Calico]
entities: []
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[cis-regulatory-element]]", "[[transcription-factor-motif]]", "[[de-novo-motif-discovery]]", "[[pseudo-bulk]]", "[[scatac-seq]]", "[[damid]]", "[[joint-single-cell-multi-omics]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Linder et al. (2025) — *Predicting RNA-seq coverage from DNA sequence as a unifying model of gene regulation* — *Nature Genetics*. [DOI](https://doi.org/10.1038/s41588-024-02053-6)

# Linder 2025 — Borzoi

> Borzoi is an Enformer-derived [[sequence-to-function-model]] that predicts **RNA-seq coverage** itself, at 32-bp resolution across a 524-kb input window, together with the CAGE, DNase, ATAC and ChIP tracks Enformer used. Because RNA-seq coverage carries transcription, splicing and polyadenylation at once, statistics computed from the predicted coverage let one model score variant effects on expression, splicing and 3′ end choice. It beats Enformer on eQTL and enhancer–gene tasks, beats APARENT2 on polyadenylation QTLs, and is about even with Pangolin on splicing QTLs. Tissue-specific alternative splicing is the clear failure.

## Key claims

- **RNA-seq coverage can be predicted from sequence without gene annotation.** Test-set bin-level Pearson R was 0.74 per replicate and 0.75 for the four-model ensemble across human RNA-seq tracks. Gene-level R was 0.87 (0.86 per replicate). After quantile normalisation and mean-gene subtraction, R was 0.58, so the model explains part of the between-tissue variation.
- **Isoform features.** Tissue-specific expression fold changes across five GTEx tissues gave Spearman R 0.52–0.75. TSS usage ratios correlated with measurements at R = 0.85, tissue-specific TSS fold changes at 0.29–0.50. Distal-to-proximal polyadenylation ratios correlated at R = 0.81, tissue-specific APA fold changes at 0.23–0.41.
- **Tissue motifs from attribution.** TF-MoDISco on tissue-residual gradients recovered known regulators (SPI1/B and IRF4/8 in blood, HNF4A/G and HNF1A in liver, SOX9 and REST in brain, MYOD1 and MEF2D in muscle). Per-TF saliency differences between tissues correlated with TF TPM fold changes (Spearman R up to 0.77, blood vs muscle).
- **Enhancer–gene linking.** Borzoi scores sites up to 262 kb from the gene, about twice Enformer's reach, and uses exon rather than TSS annotation. On CRISPRi enhancer–gene datasets it had higher AUPRC and AUROC than Enformer and a TSS-distance baseline at all distances.
- **eQTLs.** With the L2 score, the Borzoi ensemble discriminated fine-mapped GTEx eQTLs better than Enformer (mean AUROC 0.794 vs 0.747; single model 0.788). Spearman R with fine-mapped eQTL effect sizes was 0.334 vs 0.227. Choosing the true eGene among nearby genes was at best marginally better than a TSS-distance baseline.
- **Post-transcriptional QTLs.** On 1,058 fine-mapped 3′ paQTLs, AUPRC was 0.64–0.74, rising closer to the PAS, and Borzoi beat APARENT2 throughout. Against an APARENT2+Saluki ensemble it led at long distances (dAUPRC > 0.050 at 2,000 bp) and was closer near the PAS. On 4,105 sQTLs, Pangolin had a slight overall edge (dAUPRC 0.01 within 10 kb), Borzoi was better within 200 bp of the junction, and averaging the two ranks beat both. On 567 intronic paQTLs, mean AUPRC was 0.725.
- **Rare vs common variants.** In ENCODE cCREs, Borzoi and CADD separated gnomAD singletons from matched common variants equally (AUROC 0.55); combined, 0.57.
- **Training on accessibility helps.** Ablations showed DNase and ATAC tracks, and mouse data, improved test accuracy, eQTL concordance and enhancer–gene linking compared with RNA-seq alone.

## Methods / evidence

Architecture: Enformer's convolution tower and self-attention at 128 bp, then a two-step U-net that upsamples to 64 and 32 bp using skip connections from the convolution tower. Simplifications to save memory: max pooling instead of attention pooling, one convolution per tower block, 8 instead of 11 attention blocks, and central-mask positional encodings only. Loss: Poisson on total coverage plus a multinomial shape term weighted 5× (a BPNet-style decomposition), computed on the central 196,608 bp. Targets: 866 human and 279 mouse ENCODE RNA-seq tracks (Methods give 867/278), 89 GTEx tracks via recount3, and Enformer's CAGE/DNase/ChIP tracks plus pseudo-bulk scATAC from CATlas — 7,611 human tracks in total. RNA-seq values are "squashed" (power 3/4, then square root above 384) to limit the weight of highly expressed genes. Data split: eight orthology-paired genome partitions, one for validation and one for test. Each model trained ~25 days on two A100 GPUs; four replicates form the ensemble. Ablation models were smaller (393 kb input, ~30 M parameters). Variant scores: SUM, L2, logSED for expression; a maximum PAS coverage-ratio change for polyadenylation; a maximum normalised coverage difference over the gene span for splicing. Code and weights are public (github.com/calico/borzoi, Apache 2.0).

Weight: a broad, carefully benchmarked paper with explicit comparisons to task-specific models (APARENT2, Saluki, Pangolin, CADD) and ablations. The authors state that comparisons to Enformer on shared tracks are imperfect because of different splits, bin sizes and stranded CAGE. Variant analyses use the ensemble on all of hg38, including training loci; the authors argue this is acceptable because the alleles and effects were never training targets. Many numbers are in figures that are images in the clipping; only text and caption values are used here.

## Limitations

**Authors' own:**
- Most tissue-specific alternative splicing is not captured; the model tends to predict the average RNA-seq shape.
- No mRNA half-life determinants were found in 3′ UTR attributions.
- Sequencing biases (3′ bias, GC bias) caused false positives when classifying alternatively used splice sites.
- Attribution method matters: window-shuffled ISM was needed for 3′ UTRs because of buffering effects.
- Only SNVs were scored; indels shift prediction boundaries and were left for future work.
- eGene prioritisation was at best marginally better than TSS distance.
- Borzoi predicts DNase less accurately than Enformer on shared tracks (and CAGE better).

**Reviewer notes:**
- The gnomAD singleton test (AUROC 0.55) shows sequence models, like CADD, carry only weak signal for rare regulatory variant constraint. (synthesis)
- Like Enformer, Borzoi predicts only for the bulk tissues and cell lines in its training set; it does not generalise to new cell states. (synthesis)
- The ~25 GPU-day training per replicate and 524-kb inputs put retraining out of reach for most labs; most users will depend on released weights. (synthesis)

## Surprising or load-bearing bits

- One coverage-predicting model gives separate variant scores for transcription, splicing and polyadenylation, and is competitive with specialised models on each.
- Adding accessibility data improved RNA predictions. The authors suggest single-cell multiome data (joint ATAC + RNA) would be valuable joint training data, which is the path scooby and Decima take.
- In the TRIP reporter test, DNase-derived predictions at insertion sites correlated with reporter expression (Spearman R = 0.58 for *ARHGEF9*) better than LMNB1 DamID, a strong position-effect baseline.
- Whether a variant falls in sequence seen during training only marginally changed prediction quality.

## Concepts touched

- [[sequence-to-function-model]] — extends the Enformer template to RNA-seq coverage at 32 bp via U-net upsampling.
- [[variant-effect-prediction]] — eQTL, sQTL, paQTL, intronic paQTL, MPRA and gnomAD benchmarks.
- [[cis-regulatory-element]] — CRISPRi enhancer–gene linking up to 262 kb.
- [[transcription-factor-motif]] / [[de-novo-motif-discovery]] — TF-MoDISco on tissue-residual gradients; splice and polyadenylation motifs.
- [[pseudo-bulk]] / [[scatac-seq]] — CATlas pseudo-bulk scATAC tracks used as training targets.
- [[damid]] — LMNB1 DamID as the TRIP position-effect baseline.
- [[joint-single-cell-multi-omics]] — multiome named as future training data.

## Connections to other sources

- Built on [[avsec-2021-enformer]] (architecture, tracks) and the Basenji line ([[kelley-2018-basenji]]). Same senior author (Kelley) as [[kelley-2016-basset]].
- Single-cell extensions built on Borzoi: [[hingerl-2025-scooby]] and [[lal-2026-decima]].
- Further extended by [[avsec-2026-alphagenome]] (1 Mb input, base-resolution RNA-seq and splice junctions), which benchmarks against Borzoi.
- BPNet-style loss decomposition shared with [[pampari-2024-chrombpnet]].
- Lamina position effects tie to [[van-steensel-2017-lads-review]]. (synthesis)

## Open questions

- Why does tissue-specific splicing fail while TSS and APA choice work? Bin size (32 bp), coverage biases and the small share of tissue-variable splicing are all candidates. (synthesis)
- Can matched individual genomes plus RNA-seq (as in GTEx) train the model to explain inter-individual variation? The authors propose it as future work.
- How would Borzoi-style scores behave for somatic variants found in single cells, where only one allele in one clone is affected? (synthesis)

## Related

- [[sequence-to-function-model]] · [[variant-effect-prediction]] · [[avsec-2021-enformer]] · [[avsec-2026-alphagenome]] · [[hingerl-2025-scooby]] · [[40-Topics/sequence-models-and-foundation-models]]
