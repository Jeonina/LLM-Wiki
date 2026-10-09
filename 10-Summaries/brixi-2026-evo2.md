---
type: summary
title: "Brixi et al. 2026 — Genome modelling and design across all domains of life with Evo 2"
source: "[[00-Sources/papers/Genome modelling and design across all domains of life with Evo 2]]"
source_quality: full
source_sha256: "f92e45c40214e5516a88e31f85123a7eb8079e52f7a98d373aa7eb00203036cd"
source_kind: paper
author: "Garyk Brixi, Matthew G. Durrant, Jerome Ku, Mohsen Naghipourfar, Michael Poli, Gwanggyu Sun, … , Patrick D. Hsu, Brian L. Hie (corresponding authorship not marked in the clipped text)"
published: 2026-03-04
ingested: 2026-10-08
doi: "10.1038/s41586-026-10176-5"
journal: "Nature"
tags: [Evo-2, DNA-language-model, genomic-foundation-model, StripedHyena-2, autoregressive, long-context, single-nucleotide-resolution, OpenGenome2, zero-shot, variant-effect-prediction, ClinVar, BRCA1, splicing, sparse-autoencoder, mechanistic-interpretability, sequence-generation, inference-time-guidance, chromatin-accessibility, open-model]
entities: []
concepts: ["[[dna-language-model]]", "[[variant-effect-prediction]]", "[[genomic-tokenization]]", "[[sequence-to-function-model]]", "[[chromatin-accessibility]]", "[[transcription-factor-motif]]", "[[atac-seq]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Brixi et al. (2026) — *Genome modelling and design across all domains of life with Evo 2* — *Nature*. [DOI](https://doi.org/10.1038/s41586-026-10176-5)

# Brixi 2026 — Evo 2

> Evo 2 is an autoregressive DNA language model that reads single nucleotides and carries a 1 million-token context window. It was trained on OpenGenome2, a curated non-redundant atlas of more than 8.8 trillion nucleotides from bacteria, archaea, eukarya and bacteriophage, in two sizes: 7B parameters on 2.4 trillion tokens and 40B on 9.3 trillion tokens. The architecture is StripedHyena 2, a hybrid of three input-dependent convolution operators plus attention. What the model outputs is a **sequence likelihood**, not an epigenomic track: variant effects are scored **zero-shot as the change in log-likelihood when a mutation is introduced**, with likelihood-lowering changes predicted to be deleterious, and the same embeddings can be fed to small supervised classifiers. The paper evaluates this on mutational effects across domains of life, on human clinical variants (ClinVar, SpliceVarDB, *BRCA1*/*BRCA2*), on sparse-autoencoder features that align with annotated genomic elements, and on long-sequence generation. For the chromatin-accessibility design task Evo 2 supplies only the sequence proposal; Enformer and Borzoi supply the accessibility predictions that score it. Sequences from viruses infecting eukaryotic hosts were excluded from training, and the authors document that the model performs poorly in that domain as intended.

## Key claims

- **Training is staged, and long context is learned late.** Pretraining uses 8,192-token contexts with data weighting towards genic windows; a multi-stage midtraining phase then extends context to 1 million tokens. Loss improves with both model scale and longer context. In a needle-in-a-haystack check, the model retrieves a 100 bp needle hidden in 1 Mb of otherwise random DNA. StripedHyena 2 gives up to a 3× throughput speedup over optimised Transformer baselines at 40B parameters and 1M context, and better loss scaling on DNA than Transformers or StripedHyena 1.
- **Likelihoods track known biological constraint.** Single-nucleotide substitutions at start codons produce large likelihood changes, followed by three-base periodicity with the smallest effects at wobble positions, across 20 prokaryotic and 16 eukaryotic species. Upstream patterns match Shine–Dalgarno (prokaryotes) and Kozak (eukaryotes) positions. Non-synonymous, premature-stop and frameshift changes move likelihood far more than synonymous ones; deletions in tRNAs and rRNAs matter more than deletions in intergenic loci. The model distinguishes the standard genetic code from the mycoplasma (code 4) and ciliate (code 6) codes, and when ciliate genomes are artificially recoded it switches to calling the standard stop codons essential — so the code is inferred from sequence context, not memorised per species.
- **Deep mutational scanning: competitive, not best.** Likelihoods correlate with fitness across nine prokaryotic protein, six eukaryotic protein, and seven rRNA/tRNA/ribozyme datasets. Evo 2 is competitive with ProGen models on protein DMS and with RNA language models on ncRNA DMS, but **underperforms state-of-the-art protein DMS models**, and performance saturates or decreases at the largest model scale.
- **Human variant effect prediction is the headline result, with a clear shape.** On ClinVar coding SNVs, Evo 2 7B/40B lead other zero-shot methods but trail ESM-1b, GPN-MSA and some PhyloP variants. On **coding non-SNVs (insertions, deletions, duplications) they beat every method tested** — and such variants cannot be scored at all by AlphaMissense or GPN-MSA. On noncoding SNVs, Evo 2 40B is first among unsupervised models and behind supervised ones; on noncoding non-SNVs it is first overall. On SpliceVarDB, Evo 2 ranks first among unsupervised models for both exonic and intronic variants; on intronic variants it slightly trails SpliceAI and CADD but beats Pangolin.
- **BRCA1/BRCA2.** Zero-shot Evo 2 outperforms all other models on *BRCA1* noncoding SNVs and is strong on coding SNVs; on *BRCA2* coding and noncoding variants together it beats GPN-MSA and comes second to CADD. A ridge regression on Evo 2 40B embeddings trained only on *BRCA1* variants separates loss-of-function variants with AUROC 0.95 and AUPRC 0.88 on the test set, beating the model's own zero-shot score.
- **It is not an accessibility predictor, and the paper says so with numbers.** On DART-eval zero-shot tasks, Evo 2 40B reaches caQTL AUROC 0.58 and dsQTL AUROC 0.66, ahead of Nucleotide Transformer (0.52 and 0.61) but well behind ChromBPNet, a model trained on accessibility data (0.77 and 0.89). The authors conclude that task-specific sequence-to-function training still wins for distal regulatory variants. Evo 2 is also **not trained on any human genetic variation or functional genomics data**.
- **Embeddings support annotation.** Lightweight classifiers on Evo 2 7B base embeddings label exons at single-nucleotide resolution with AUROC 0.91–0.99 on eight held-out species, beating classifiers on Nucleotide Transformer and Evo 1 embeddings, conservation metrics (local GC, PhyloP), ab initio AUGUSTUS, and SegmentNT outside its training set.
- **Gene essentiality.** Zero-shot scoring of premature stop insertions predicts prokaryotic, archaeal and phage gene essentiality on par with Evo 1 and better than other zero-shot methods. On human gene essentiality (DepMap) Evo 2 40B reaches AUROC 0.66 / AUPRC 0.15, better than other genomic language models (AUROC 0.50–0.59) but within the range of PhyloP conservation scores (0.65–0.71) — the authors call the performance modest.
- **Sparse autoencoders find interpretable features.** A Batch-TopK SAE trained on layer-26 representations from 1 billion tokens yields features matching prophage regions (f/19746, which also fires on CRISPR spacers and on scrambled spacers, so it generalises rather than memorises), ORFs, intergenic regions, tRNAs, rRNAs, α-helices and β-sheets, a frameshift/premature-stop-sensitive feature (f/24278), coding regions (f/15680), introns (f/28339), and the first and last bases of exons at splice junctions (f/1050, f/25666). Across sampled human promoters, SAE features hit 70% of promoter-enriched HOCOMOCO v12 CORE motifs (q < 0.01, TOMTOM), against 35% recall for HOMER. Features found on the human genome transfer to a woolly mammoth genic region.
- **Generation scales to organelle, bacterial and chromosome length.** Prompted with human mitochondrial DNA, the model produced over 250 unique 16-kb sequences with the expected counts of CDSs, tRNA and rRNA genes (MitoZ annotation), correct synteny and matching codon usage. A 10.5-kb *M. genitalium* prompt yielded ten 580-kb sequences in which nearly 70% of called genes had significant Pfam hits, against 18% for Evo 1 131k. A 10.5-kb *S. cerevisiae* chromosome III prompt yielded 20 sequences of 330 kb containing tRNAs, promoters and genes with introns, though tRNA and gene density fell below the native yeast genome.
- **Chromatin design works by pairing a generator with external oracles.** An ensemble of Enformer and Borzoi DNase predictions scores candidate sequences; a beam search re-evaluates after every 128 bp and extends only the best partial sequences. Sampling 30 or more chunks and keeping the top two per step reached design AUROC above 0.9, and design quality improved log-linearly with beam width. Morse-code accessibility patterns ("LO", "ARC", "EVO2") integrated into mouse embryonic stem cells gave measured ATAC-seq AUROCs of 0.92–0.95. In HEK293T and K562, 33 of 36 designs (92%) reached AUROC > 0.8 for varying accessibility within a sequence, but only 4 of 24 (17%) achieved more than twofold differential accessibility between the two cell types and 1 of 24 (4%) more than threefold.

## Methods / evidence

Two models (7B, 40B) plus an experimental 1B short-context model the authors say to avoid. Single-nucleotide tokens; StripedHyena 2 hybrid architecture; two-phase training with context extension to 1M tokens. Zero-shot scoring is the difference in model log-likelihood between reference and mutant sequence, applied uniformly to SNVs and to insertions, deletions and duplications — which is what lets the model score variant classes that alignment-based and missense-specific predictors cannot. Supervised use is a ridge regression over embeddings pooled around the variant site, with the block and pooling window chosen by five-fold cross-validation. Interpretability uses a Batch-TopK SAE on layer 26 plus a "contrastive feature search" that looks for features enriched in annotated segments; ablation of high-F1 features raises cross-entropy, which the authors read as evidence the features are causally used. Generation is evaluated in silico with MitoZ, Prodigal, GeneMark-ES, Pfam, ESMFold/AlphaFold 3, TM-score and tetranucleotide usage deviation. The design task is the only part with wet-lab validation: synthesised DNA, site-specific integration, ATAC-seq in mESC, HEK293T and K562. Model weights, training and inference code, and the OpenGenome2 dataset are released openly.

Weight: the benchmark coverage is wide and the comparators are the right ones (PhyloP, ESM-1b/ESM-2, GPN-MSA, AlphaMissense, CADD, SpliceAI, Pangolin, Nucleotide Transformer, ChromBPNet, AUGUSTUS, SegmentNT). Most headline numbers live in figures rather than in the clipped body text, so several comparisons here are reported as the text describes them rather than as exact values. (synthesis)

## Limitations

**Authors' own:**
- In silico generation metrics "do not guarantee functional or replication-competent genomes", and the genome-scale generations lack important elements including some essential genes; testing designs experimentally would need large-scale iterative effort.
- Evo 2 underperforms state-of-the-art models on protein deep mutational scanning, and fitness-prediction performance saturates or decreases at the largest scale.
- It falls behind supervised sequence-to-function models for distal regulatory variants, where task-specific training on accessibility data still wins.
- Human gene essentiality prediction is "modest" and within the range of conservation baselines.
- Inference-time guidance can require computationally intensive sampling.
- SAE-based annotation has not been systematically benchmarked against established annotation tools.
- Sequences from viruses that infect eukaryotes were excluded from training for biosafety; the authors verify this weakened language modelling, mutational effect prediction and generation in that domain, and note that task-specific post-training could undo the mitigation and "should be approached with caution".

**Reviewer notes:**
- The cross-cell-type design result is much weaker than the headline design result: 92% success at shaping accessibility within one cell type against 17% at achieving twofold differential accessibility between two, which is the property most regulatory-design applications actually need. (synthesis)
- The chromatin result is a property of the Evo 2 + Enformer/Borzoi + beam-search pipeline, not of Evo 2 alone; the oracles define the objective and the paper's own DART-eval numbers show Evo 2 scoring accessibility poorly by itself. (synthesis)
- Several comparisons that matter most — whether 40B is worth 40B over 7B, and which baselines win per variant stratum — are reported only inside figures, so the clipped text does not permit checking effect sizes. (synthesis)

## Surprising or load-bearing bits

- **The non-SNV result is the real advance.** Insertions, deletions and duplications are unscoreable by the leading human variant predictors because those are built on protein-level or alignment-column assumptions. A nucleotide-level autoregressive likelihood scores them for free, and that is where Evo 2 beats everything else tested rather than merely leading the unsupervised pack.
- **Genetic code is inferred, not memorised.** Recoding ciliate genomes to the standard code flips which stop codons the model treats as essential, which is strong evidence the model uses context rather than species identity.
- **A generic language model out-recalls a dedicated motif finder.** SAE features hit 70% of promoter-enriched HOCOMOCO motifs against HOMER's 35%, without any motif supervision.
- **Evo 2 generations behave like natural DNA without being asked to.** Prompting with native genomic context yielded natural dinucleotide frequencies and high Enformer/Borzoi ensemble agreement, while uniform and bigram proposals did not — the authors suspect simpler proposals produce adversarial inputs to the oracles. Ensemble agreement turned out retrospectively to predict experimental success.
- **The ceiling on likelihood-based fitness prediction.** Performance saturating or falling at the largest scale is a real scaling caveat for DNA language models, matching what has been seen for protein language models. (synthesis)

## Concepts touched

- [[dna-language-model]] — the current scale reference point for the autoregressive, single-nucleotide, multi-domain branch: 9.3 trillion training tokens, 40B parameters, 1 Mb context, fully open weights and data.
- [[variant-effect-prediction]] — defines the zero-shot scoring rule (Δ log-likelihood on mutation) and shows where it wins (non-SNVs, noncoding, splicing among unsupervised methods) and where it loses (coding SNVs against alignment-based models; distal regulatory variants against supervised accessibility models).
- [[genomic-tokenization]] — single-nucleotide tokens, in contrast to k-mer and BPE schemes; the paper's non-SNV advantage follows directly from nucleotide-level scoring.
- [[sequence-to-function-model]] — explicitly positioned as the complement, not the replacement: Enformer and Borzoi provide the accessibility objective Evo 2 cannot score itself.
- [[chromatin-accessibility]] / [[atac-seq]] — designed accessibility patterns validated by ATAC-seq in mESC, HEK293T and K562.
- [[transcription-factor-motif]] — SAE features recover promoter motifs; designed peak regions are enriched for motifs of transcription factors expressed in the target cell type.

## Connections to other sources

- Distilled by [[fang-2025-evo2hic]], which turns Evo 2 representations into a 3D-contact predictor — a downstream use of exactly the embeddings this paper releases.
- Architecture lineage: [[nguyen-2023-hyenadna]] introduced the Hyena-style long-context DNA model; StripedHyena 2 here is the convolutional multi-hybrid successor.
- Baseline and comparator in this paper: [[dallatorre-2025-nucleotide-transformer]] (beaten on exon classification and DART-eval), [[benegas-2025-gpn-msa]] (ahead on coding SNVs, but cannot score non-SNVs).
- External oracles for the design task: [[avsec-2021-enformer]] and [[linder-2025-borzoi]], both of which the paper notes are not generative and are trained only on natural genomes.
- Contrast with the supervised multi-task branch: [[avsec-2026-alphagenome]] predicts regulatory tracks directly, where Evo 2 only predicts sequence likelihood. (synthesis)
- Other DNA language models in this ingest batch for architecture and tokenisation comparison: [[zhou-2023-dnabert-2]], [[schiff-2024-caduceus]], [[boshar-2025-ntv3]], [[salman-2026-mendel]].
- Foundation-model framing on the single-cell side: [[fan-2026-gfetm]] fine-tunes a genome foundation model inside a cell model; Evo 2 instead keeps the model frozen and uses likelihoods and embeddings directly. (synthesis)

## Open questions

- Does the 40B model justify its cost over 7B outside generation? The paper states 40B is best overall but calls 7B competitive, and on DMS the larger model is sometimes worse.
- Would adding population-scale variation or sequence-to-function data — which the authors name as future work — close the gap to supervised predictors on distal regulatory variants, or does likelihood-only training have a ceiling there? (synthesis)
- Cross-cell-type regulatory design succeeded at only 17% for twofold differential accessibility; it is unclear whether this is a limit of the beam search, of the Enformer/Borzoi oracles, or of the generative proposal. (synthesis)
- The SAE analysis targeted features with known annotations. Whether the remaining features encode anything biologically new is untested.
- None of the genome-scale generated sequences were tested in cells, so coherent in silico annotation has not been connected to function. (synthesis)

## Related

- [[dna-language-model]] · [[variant-effect-prediction]] · [[genomic-tokenization]] · [[sequence-to-function-model]] · [[fang-2025-evo2hic]] · [[nguyen-2023-hyenadna]] · [[40-Topics/sequence-models-and-foundation-models]]
