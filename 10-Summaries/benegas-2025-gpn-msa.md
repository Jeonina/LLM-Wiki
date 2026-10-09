---
type: summary
title: "Benegas et al. 2025 — A DNA language model based on multispecies alignment predicts the effects of genome-wide variants"
source: "[[00-Sources/papers/A DNA language model based on multispecies alignment predicts the effects of genome-wide variants]]"
source_quality: full
source_sha256: "e09c51466d081d68db2c1d3bff1f8d191f648d04b96b778eaa6a66309f9e3465"
source_kind: paper
author: "Gonzalo Benegas, Carlos Albors, Alan J. Aw, Chengzhong Ye, Yun S. Song"
published: 2025-01-02
ingested: 2026-10-08
doi: "10.1038/s41587-024-02511-w"
journal: "Nature Biotechnology"
tags: [GPN-MSA, GPN, DNA-language-model, variant-effect-prediction, multiple-sequence-alignment, conservation, masked-language-model, RoFormer, ClinVar, COSMIC, OMIM, gnomAD, DepMap, CADD, phyloP, noncoding-variants, zero-shot]
entities: []
concepts: ["[[dna-language-model]]", "[[variant-effect-prediction]]", "[[cis-regulatory-element]]", "[[transposable-elements]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]"]
---

**Citation:** Benegas et al. (2025) — *A DNA language model based on multispecies alignment predicts the effects of genome-wide variants* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-024-02511-w)

# Benegas 2025 — GPN-MSA

> GPN-MSA is a small masked DNA language model (~86 M parameters, RoFormer) whose input is not a single human sequence but a 128-bp window of the **100-vertebrate multiz whole-genome alignment**, with the ten primates closest to human removed. It predicts masked human-reference nucleotides from both neighbouring columns and aligned species, is trained mostly on the 5% most conserved windows, and scores a variant zero-shot as the log-likelihood ratio of alternate to reference allele. Trained in about 3.5 h on four A100 GPUs, it beats much larger single-sequence DNA language models (Nucleotide Transformer 2.5B, HyenaDNA 1 Mb) and standard predictors (CADD, phyloP, Enformer, SpliceAI) on most clinical, population and functional benchmarks, with the largest relative advantage on noncoding variants. The authors frame it as retrieval augmentation: explicit evolutionary context replaces scale.

## Key claims

- **Alignment beats scale.** Prior human DNA language models, including Nucleotide Transformer trained for 28 days on 128 GPUs, did worse than simple conservation scores for unsupervised variant effect prediction (VEP). GPN-MSA, trained in ~3.5 h, outperforms Nucleotide Transformer and HyenaDNA on ClinVar pathogenic vs gnomAD common missense variants.
- **ClinVar (missense).** With gnomAD common variants as controls, GPN-MSA beats CADD, phyloP and the protein language model ESM-1b. With ClinVar benign variants as controls, AUROC drops for every method and GPN-MSA is marginally behind CADD and ESM-1b; the three are very close either way.
- **COSMIC (somatic missense).** For frequent COSMIC somatic missense variants vs gnomAD common missense, GPN-MSA has the highest AUPRC "with substantial margins". The bimodal score distribution of frequent COSMIC variants suggests many are passenger mutations.
- **Deep mutational scanning.** On 31 human proteins (ProteinGym), GPN-MSA and CADD are comparable and both beat phyloP and phastCons, but ESM-1b is best overall. GPN-MSA beats ESM-1b on some proteins (TADBP AUROC 0.83 vs 0.75).
- **Regulatory variants (OMIM).** On curated Mendelian regulatory variants vs gnomAD common variants, GPN-MSA has the best AUPRC overall and per category; Nucleotide Transformer is poor, and CADD's precision starts near zero for several categories. Examples: rs606231231 in the ZRS enhancer of *SHH* (~1 Mb away, polydactyly) and rs1367115848 disrupting HNF4 binding at the *F7* promoter.
- **gnomAD rare vs common.** GPN-MSA has the highest enrichment of singletons over common (MAF > 5%) variants in the extreme score tail, overall and in most consequence classes, beating SpliceAI on intronic variants. CADD is better only for splice-region variants. On low-frequency vs common nonexonic variants GPN-MSA beats Enformer substantially.
- **Gene essentiality (DepMap).** Gene-level summaries of GPN-MSA scores classify essential vs nonessential genes better than other VEP tools and better than pLI, heterozygous selection and GeneBayes.
- **Ablation.** Removing the MSA had by far the largest effect. Including the closest primates or training on less conserved regions also hurt substantially. Subsetting to 51 mammals or 51 vertebrates, removing conservation upweighting, or removing nonconserved-site replacement had minor effects. Window size shows diminishing returns from 4 to 128 bp; a 256-bp model was less stable.
- **Precomputed scores.** Scores for all ~9 billion possible human SNVs are released; a cutoff around −7 is suggested if a hard threshold is needed, but scores should be used only as relative ranks, not calibrated fitness.

## Methods / evidence

Input: 128-bp MSA window; one-hot nucleotides of all species concatenated per column; a 12-layer, 12-head RoFormer over columns; output four nucleotide probabilities at masked human positions. 15% masking during training, only human rows masked; at VEP time only the variant position is masked, and both strands are averaged. Loss is weighted cross-entropy: repeats down-weighted tenfold, conserved sites up-weighted by phyloP and a 7-nt max-smoothed phastCons. In nonconserved positions (phastCons_M < 0.1) the reference is randomly replaced with probability 0.5 to push scores toward neutral. Training windows: top 5% by 75th-percentile phastCons plus 0.1% of the rest; chr21 for early stopping, chr22 for perplexity. Max 30,000 steps (~14 epochs). Scoring throughput ~25 million variants per hour on four A100s.

Benchmarks: ClinVar (release 20230730), COSMIC v98, OMIM regulatory variants (Smedley et al.), gnomAD v3.1.2 (allele number ≥ 25,000; common MAF > 5%, rare = singletons), ProteinGym v0.1, DepMap 23Q4. Nucleotide Transformer and HyenaDNA were scored only on ClinVar (and part of OMIM for NT) because of compute cost. A FAVOR enrichment analysis of 10 M simulated chr22 variants found the most deleterious 1% enriched for active histone marks, RNA-seq and DNase-seq signal and depleted for nucleotide diversity, recombination rate, B statistic, H3K9me3 and H3K27me3. Hyperparameters were not tuned systematically. Code and scores are public (github.com/songlab-cal/gpn; Hugging Face). Figures 1–2 and Extended Data Table 1 are images in the clipping; values above are those stated in text.

## Limitations

**Authors' own:**
- Training mostly on conserved regions may miss functional sites in primate- or human-specific, fast-evolving or hard-to-align regions.
- The masked-LM objective becomes too easy when near-identical genomes are in the MSA, so most primates were excluded; phylogeny-aware objectives are under exploration.
- Uses a single reference genome; integrating population variation is future work.
- Likelihood ratios are systematically lower than fitness differences imply: synonymous variants centre around −3 instead of 0, and nonconserved-site replacement shifts the score distribution (peak near log(0.125/0.625) ≈ −1.6). Scores are relative, not calibrated.
- Whether it separates deleterious from benign *rare* variants genome-wide is open; that needs more labelled data. Hyperparameters were not tuned. Less interpretable than functional-genomics models such as SpliceAI and Enformer.

**Reviewer notes:**
- Several baselines are scored on narrower variant sets (Nucleotide Transformer and HyenaDNA only on ClinVar; Enformer only on low-frequency variants), so the "beats large DNA LMs" claim rests mainly on one missense benchmark. (synthesis)
- The gnomAD rare-vs-common metric partly rewards models that track mutation-rate and conservation structure, which GPN-MSA uses directly in its loss weights; the evaluation and the training signal are not fully independent. (synthesis)
- The model is human-reference-only and alignment-bound: variants in regions without a vertebrate alignment (repeats, segmental duplications, many structural-variant breakpoints) cannot be scored the same way. (synthesis)

## Surprising or load-bearing bits

- **Retrieval, not scale.** An 86 M-parameter model trained for hours beats a 2.5 B-parameter model trained for weeks, because evolution is given explicitly. This is the main counterweight in this ingest to the "scale up single-sequence DNA LMs" line. (synthesis)
- **Context beyond one column.** At perfectly conserved positions GPN-MSA still ranks loss-of-function and missense variants as more deleterious than synonymous ones, which a single-column conservation score cannot do.
- **Older phyloP-100v often beats newer phyloP-241m** (Zoonomia mammals) as a deleteriousness score in these benchmarks.
- **ClinVar is an easy benchmark.** Even MSA column frequency does well on ClinVar but not on OMIM or gnomAD, likely because conservation scores were used in ClinVar labelling guidelines.
- **Somatic signal.** COSMIC somatic missense variants are the one cancer-somatic benchmark here; GPN-MSA scores them as germline-trained, constraint-based deleteriousness. Using such scores to prioritise somatic mosaic variants found by single-cell sequencing is plausible but untested. (synthesis)

## Concepts touched

- [[dna-language-model]] — alignment-conditioned masked LM; argues explicit multispecies context beats parameter count for VEP.
- [[variant-effect-prediction]] — zero-shot LLR scores for all ~9 B human SNVs; benchmarks across ClinVar, COSMIC, OMIM, gnomAD, DMS and DepMap.
- [[cis-regulatory-element]] — strongest gains on noncoding/regulatory variants (OMIM promoter and enhancer, ZRS example).
- [[transposable-elements]] — repeats are down-weighted tenfold in the loss as likely nonfunctional.

## Connections to other sources

- Main single-sequence DNA LM comparators: [[dallatorre-2025-nucleotide-transformer]] and [[nguyen-2023-hyenadna]] — both outperformed on ClinVar despite far more compute.
- Functional-genomics comparator: [[avsec-2021-enformer]] — worse than GPN-MSA (and phyloP) at deleteriousness ranking of nonexonic gnomAD variants, though not designed for it.
- Mentioned as a long-context DNA LM family: [[fishman-2025-gena-lm]].
- The authors' stated next step, integrating population variation instead of one reference, is what [[long-2025-mutbert]], [[li-2025-bmfm-dna]], [[salman-2026-mendel]], [[liu-2026-ukbiobert]] and [[leib-2026-dnt]] attempt. (synthesis)

## Open questions

- Can a phylogeny-aware objective fix the calibration problem (synonymous variants centred at −3) without losing ranking power?
- How does GPN-MSA rank variants in human-specific or unalignable regions that matter for structural and repeat-mediated variation? (synthesis)
- Would GPN-MSA scores help prioritise low-VAF somatic variants in single-cell or duplex data from [[somatic-mosaicism]] studies, where population allele frequency is uninformative? (synthesis)

## Related

- [[dna-language-model]] · [[variant-effect-prediction]] · [[40-Topics/sequence-models-and-foundation-models]] · [[dallatorre-2025-nucleotide-transformer]] · [[avsec-2021-enformer]] · [[salman-2026-mendel]]
