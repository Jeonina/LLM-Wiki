---
type: summary
title: "Avsec et al. 2026 — Advancing regulatory variant effect prediction with AlphaGenome"
source: "[[00-Sources/papers/Advancing regulatory variant effect prediction with AlphaGenome]]"
source_quality: full
source_sha256: "3668c2320b5d9d7cca55d987a2d2632915f171fd3c8a255e01d985af07851914"
source_kind: paper
author: "Žiga Avsec, Natasha Latysheva, Jun Cheng, Guido Novati, Kyle R. Taylor, Tom Ward, … , Demis Hassabis, Pushmeet Kohli"
published: 2026-01-28
ingested: 2026-10-08
doi: "10.1038/s41586-025-10014-0"
journal: "Nature"
tags: [AlphaGenome, sequence-to-function, U-net, transformer, base-resolution, 1Mb-context, multimodal, splicing, splice-junctions, contact-maps, eQTL, caQTL, sQTL, paQTL, distillation, variant-effect-prediction, TAL1, Google-DeepMind]
entities: []
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[chromatin-accessibility]]", "[[micro-c]]", "[[cis-regulatory-element]]", "[[transcription-factor-motif]]", "[[chip-seq]]", "[[atac-seq]]", "[[dnase-seq]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]", "[[histone-modifications]]", "[[3d-genome]]"]
---

**Citation:** Avsec et al. (2026) — *Advancing regulatory variant effect prediction with AlphaGenome* — *Nature*. [DOI](https://doi.org/10.1038/s41586-025-10014-0)

# Avsec 2026 — AlphaGenome

> **Source note:** the clipping holds the full main text, Discussion and Extended Data captions, but the Methods are in the Supplementary Information, which is not in the clipping. Architecture and training details below come from the main text and Extended Data Fig. 1 captions only; most quantitative results sit in figures (images) and only text-stated numbers are used.
>
> AlphaGenome is a supervised [[sequence-to-function-model]] from Google DeepMind that removes two trade-offs of earlier models: context length vs output resolution, and generalist vs specialist. It reads **1 Mb** of DNA and predicts 5,930 human or 1,128 mouse tracks across 11 modalities — RNA-seq, CAGE, PRO-cap, splice sites, splice-site usage, splice junctions, DNase, ATAC, histone marks, TF binding and contact maps — at up to **1-bp** resolution. A U-net (convolutional encoder, transformer tower at 128 bp with a 2D pair representation, convolutional decoder back to 1 bp) is pretrained with 4-fold cross-validation, then distilled into one student model that scores a variant across all modalities in under 1 s on an H100. It matches or beats the best external model on 22 of 24 track tasks and 25 of 26 variant-effect tasks.

## Key claims

- **Benchmark sweep.** Fold-specific models beat the strongest external model on 22/24 genome-track evaluations, and the distilled model matched or beat external models on 25/26 variant-effect evaluations. Examples: +14.7% relative on cell-type-specific gene-level expression log-fold change vs Borzoi; contact maps +6.3% Pearson r and +42.3% on cell-type-specific differences vs Orca; +15% total-count Pearson r vs ProCapNet; +1.6% (ATAC) and +9.5% (DNase profile JSD) vs ChromBPNet.
- **Splicing.** Predicting junctions as well as sites and usage gave the best result on 6 of 7 splicing benchmarks. ClinVar auPRC: deep intronic/synonymous 0.66 vs 0.64 (Pangolin), splice region 0.57 vs 0.55, missense 0.18 vs 0.16. Pangolin won on the MFASS minigene assay (0.54 vs 0.51). The junction scorer alone beat prior methods on all but two benchmarks.
- **eQTLs.** Tissue-weighted mean Spearman ρ with SuSiE effect sizes rose from 0.39 (Borzoi) to 0.49; sign auROC from 0.75 to 0.80. At a threshold giving 90% sign accuracy, it recovered 41% of GTEx eQTLs vs 19% for Borzoi. It also beat Borzoi on indel eQTLs. Zero-shot causality was comparable to Borzoi, but a random forest on multimodal scores raised causality auROC from 0.68 to 0.75 (Borzoi 0.71).
- **GWAS sign.** At a threshold calibrated to 80% eQTL sign accuracy, it assigned a confident direction to at least one variant in 49% of 18,537 GWAS credible sets (11% with PIP weighting), largely non-overlapping with COLOC, and resolved ~4× more credible sets than COLOC in the lowest MAF quintile.
- **Enhancer–gene linking.** Zero-shot, it beat Borzoi (especially beyond 10 kb) and came within 1% auPRC of the supervised ENCODE-rE2G extended model; adding AlphaGenome features to rE2G gave a new best.
- **Polyadenylation.** APA Spearman ρ 0.894 vs Borzoi 0.790. paQTL auPRC 0.629 vs 0.621 within 10 kb of a PAS, 0.762 vs 0.727 within 50 bp.
- **Chromatin QTLs.** On ChromBPNet's caQTL, dsQTL and bQTL benchmarks across ancestries, it beat ChromBPNet and Borzoi on causality and effect size (Pearson r = 0.74 for African-ancestry caQTLs, 0.55 for SPI1 bQTLs). Accessibility QTL sign prediction was +8.0% vs ChromBPNet averaged over five datasets. On CAGI5 MPRA, LASSO over multimodal features reached Pearson r = 0.65.
- **Multimodal locus screen.** For oncogenic *TAL1* neo-enhancer mutations in T-ALL, predictions in CD34+ CMP data showed gains in H3K27ac and H3K4me1 at the variant, loss of H3K9me3/H3K27me3 near the TSS, more H3K36me3 over the gene body and higher *TAL1* expression. ISM recovered the known MYB motif created by the insertion and a second ETS-like motif of unknown role.
- **Ablations.** 1-bp targets helped most for splicing and ATAC; histone and contact-map tracks were insensitive to resolution. Training on 1 Mb beat training on ≤32 kb even when both were run on 1 Mb. Distillation from many teachers matched or beat a four-model ensemble; dropping input mutation during distillation cost 0.06 eQTL-sign auROC. Multimodal training helped overall, especially eQTLs; accessibility QTLs needed only accessibility data.

## Methods / evidence

Architecture (from Extended Data Fig. 1): encoder of convolution blocks with max pooling from 1 bp to 128 bp; transformer tower at 128 bp that also builds 2D pair embeddings at 2,048 bp for contact maps; decoder with upsampling and skip connections back to 1 bp; linear heads per track, plus a separate donor–acceptor interaction head for junction counts. Training at 1 Mb with base-pair targets uses sequence parallelism over eight TPU v3 devices. Pretraining: 4-fold cross-validation for evaluation models and all-fold "teacher" models; distillation: one student trained on teacher-ensemble outputs from randomly mutated inputs. Data: public ENCODE, GTEx, FANTOM5, 4D Nucleome and others (Supplementary Table 2). Access: non-commercial API and SDK; source code and weights at github.com/google-deepmind/alphagenome_research.

Weight: a very broad benchmark against the strongest per-task baselines, with ablations on each design choice. Many gains over Borzoi on QTL tasks are small in absolute terms (paQTL auPRC 0.629 vs 0.621), and several comparisons required retraining AlphaGenome with matched heads or intervals. Detailed Methods were not available in the clipping, so data splits, loss functions and parameter counts cannot be checked here.

## Limitations

**Authors' own:**
- Capturing distal elements beyond ~100 kb remains hard; both AlphaGenome and Borzoi underestimate very distal enhancer effects.
- Tissue- and cell-type-specific patterns and condition-specific variant effects remain challenging; cell-type-specific expression deviations are hard to predict.
- Intermediate splicing efficiencies and tissue-specific splicing nuances need improvement.
- Training data and evaluations are concentrated on protein-coding genes; only human and mouse are covered.
- Not yet benchmarked on personal genome prediction, a known weakness of this model class.
- Predicts molecular consequences, not phenotypes; high-score thresholds enrich causal variants but with low recall, especially for GWAS variants.
- The authors list integration of single-cell data, DNA methylation, DNA language models and assay bias correction as future work.

**Reviewer notes:**
- Use is through a non-commercial API with released weights; how freely the full model can be fine-tuned by outside labs is not described in the main text. (synthesis)
- The *TAL1* analysis uses CMP tracks as the "closest available" proxy for T-ALL cells, which shows the bulk-reference limitation for cell states not in training. (synthesis)
- Gains over task-specialist models are often a few percent; the main practical advance is one model and one inference call for all modalities, not a large accuracy jump on any single task. (synthesis)

## Surprising or load-bearing bits

- A 1-Mb-trained model run on shorter windows performed about as well as models trained at those shorter lengths, so one model serves many context sizes.
- Distillation with input mutations produced a single student that rivals ensembles, cutting inference to one call per variant.
- Sign prediction, not causality, is where gains are clearest; AlphaGenome and COLOC give directions for largely different GWAS loci.
- The authors name "integration of single-cell data" as a next step — the gap that single-cell heads such as scooby and Decima address on the Borzoi backbone. (synthesis)

## Concepts touched

- [[sequence-to-function-model]] — first model combining 1-Mb context, 1-bp output and 11 modalities, including contact maps.
- [[variant-effect-prediction]] — 26 benchmarks: eQTL, sQTL, paQTL, caQTL, dsQTL, bQTL, ClinVar, MFASS, CAGI5, GWAS sign.
- [[chromatin-accessibility]] / [[atac-seq]] / [[dnase-seq]] — beats ChromBPNet on accessibility tracks and QTLs.
- [[micro-c]] / [[3d-genome]] — contact-map head trained on Hi-C/Micro-C, compared with Orca.
- [[histone-modifications]] / [[chip-seq]] — histone and TF ChIP tracks; *TAL1* neo-enhancer mark changes.
- [[cis-regulatory-element]] — ENCODE-rE2G enhancer–gene linking.
- [[transcription-factor-motif]] — ISM recovers MYB, SPI1, NF-κB, HNF1, GATA–TAL and CTCF motifs at disease variants.

## Connections to other sources

- Successor to [[avsec-2021-enformer]] (same first author) and [[linder-2025-borzoi]] (U-net idea, RNA-seq coverage, main baseline).
- Beats specialists [[pampari-2024-chrombpnet]] (accessibility; uses its QTL benchmarks) and [[zhou-2022-orca]] (contact maps). Lineage: [[zhou-2015-deepsea]], [[kelley-2018-basenji]], [[chen-2022-sei]].
- Single-cell outputs on Borzoi-class backbones: [[hingerl-2025-scooby]], [[lal-2026-decima]].
- Names DNA language models as a future input; see [[dallatorre-2025-nucleotide-transformer]] and [[boshar-2025-ntv3]] for that line. (synthesis)
- T-ALL *TAL1* context ties to [[hematopoietic-malignancies]]. (synthesis)

## Open questions

- Does the distilled model keep its accuracy on personal genomes, where earlier sequence models fail to explain inter-individual expression? Not tested.
- Could a single-cell head on this backbone reach rare or unprofiled cell states better than the CMP proxy used for T-ALL? (synthesis)
- For somatic variants found by single-cell DNA sequencing, can AlphaGenome scores rank driver vs passenger noncoding mutations? (synthesis)

## Related

- [[sequence-to-function-model]] · [[variant-effect-prediction]] · [[avsec-2021-enformer]] · [[linder-2025-borzoi]] · [[pampari-2024-chrombpnet]] · [[40-Topics/sequence-models-and-foundation-models]]
