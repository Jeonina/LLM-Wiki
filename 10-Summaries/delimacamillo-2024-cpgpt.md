---
type: summary
title: "de Lima Camillo et al. 2024 — CpGPT: a Foundation Model for DNA Methylation"
source: "[[00-Sources/papers/CpGPT- a Foundation Model for DNA Methylation.pdf]]"
source_quality: full
source_sha256: "323f2f1590b40128cc7c503b5b2b30cc9247b537c23d8a1d1906cd90fe844a01"
source_kind: paper
author: "Lucas Paulo de Lima Camillo (main author; corresponding), Raghav Sehgal (corresponding), Jenel Armstrong, Max Melnikas, Henry E. Miller, Jun Ding, … Albert T. Higgins-Chen, Steve Horvath, Bo Wang"
published: 2024-10 (clipped text = bioRxiv version posted 2026-08-12)
ingested: 2026-10-08
doi: "10.1101/2024.10.24.619766"
journal: "bioRxiv preprint"
tags: [CpGPT, DNA-methylation, foundation-model, transformer, bulk-methylation, Illumina-array, CpGCorpus, epigenetic-clock, imputation, array-conversion, mortality, GrimAge, Nucleotide-Transformer, sciMETv3, DeepCpG, zero-shot, preprint-text]
entities: ["[[20-Entities/andrew-adey]]"]
concepts: ["[[single-cell-foundation-model]]", "[[dna-language-model]]", "[[epigenetic-aging]]", "[[imputation]]", "[[cpg-island]]", "[[bisulfite-sequencing]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/dna-methylation]]"]
---

**Citation:** de Lima Camillo et al. (2024) — *CpGPT: a Foundation Model for DNA Methylation* — *bioRxiv preprint*. [DOI](https://doi.org/10.1101/2024.10.24.619766)

# de Lima Camillo 2024 — CpGPT

> **Version note:** the clipped text is the bioRxiv version posted 12 August 2026, not the October 2024 v1. It includes ablations, clustering metrics, a DeepCpG comparison and the CpGPTGrimAge3 cohort analyses that may not be in earlier versions.
>
> CpGPT is a transformer trained on **bulk human methylation array data**: CpGCorpus, 155,151 samples from 2,042 GEO studies on Illumina 27k, 450k, EPIC, EPIC+ and EPICv2 arrays (over 101 billion CpG-sample tokens). Each input is a variable subset of 5,000–10,000 CpG sites. A token is one CpG in one sample, built from three parts: a Nucleotide Transformer v2 (500M) embedding of the 2,001 bp around the CpG, a genomic position encoding, and an embedding of the beta value. Half the sites are hidden and the model reconstructs them from a CLS sample embedding. Because a locus is described by its sequence rather than by a fixed probe ID, the model can query CpGs it never saw in training. The authors use this for zero-shot imputation, array conversion and reference mapping. Fine-tuned, a 2.5M-parameter version predicts age, plasma proteins, cancer and mortality. Single-cell methylation (sciMETv3) is only a fine-tuning and evaluation target, not pretraining data.

## Key claims

- **Two model sizes, two roles.** CpGPT-100M (101M parameters, 32 layers) is used for unsupervised tasks (embeddings, imputation). CpGPT-2M (2.5M parameters, 8 layers) is used for all supervised fine-tuning. The standard model trained for about 10 days on one H100.
- **Ablations.** With CpGPT-2M at 100k steps, NTv2-500M with 2,001 bp context gave the lowest test beta MAE (0.0704), against 0.0794 for the largest HyenaDNA. Longer context helped all backbones, with diminishing returns from 1,001 to 2,001 bp. Removing the transformer blocks raised MAE to 0.0802 (+14%). Random CpG order instead of chromosome sorting gave 0.0709, so the ordering matters little. MAE fell from 0.0931 at 20k steps to 0.0613 at 1M steps, roughly as a power law.
- **Locus embeddings carry chromatin state.** On about 100,000 EPICv2 CpGs, CpGPT locus embeddings separated ChromHMM states better than raw NTv2 embeddings. Average rank over six annotation sets: CpGPT-2M 1.22, CpGPT-100M 2.28, NTv2 2.50. For ChromHMM, CpGPT-2M had ARI 0.083 and NMI 0.237 against 0.054 and 0.166 for NTv2. These ARIs are low in absolute terms.
- **Sample embeddings cluster by tissue and species.** On the AltumAge multi-tissue set, CpGPT-100M embeddings gave ARI 0.234 and NMI 0.509 against 0.031 and 0.083 for raw betas. On a 55-species mammalian array set, species was the main axis (ARI 0.606). After fine-tuning, tissue became the main axis (tissue ARI 0.322) and species ARI fell to 0.397.
- **Zero-shot reference mapping.** With k = 5 nearest neighbours in embedding space, 653 of 656 Hannum blood samples mapped to a blood category. In an independent Parkinson's set, 20 of 20 blood and 17 of 20 brain samples mapped correctly (92.5%). In an OSKM reprogramming time course, day 15 was the last time point that mapped to fibroblast entries in GEO, and day 28 mapped to iPSC entries.
- **Imputation of CpGs never seen in training.** 1% of probes (11,864) were held out of pretraining. In the hardest "unseen input, unseen target" case, CpGPT-100M reached MAE 0.0811 against about 0.333 for the sample mean. With seen sites on both sides it reached 0.0386. Error was lowest in blood and immune samples (0.068, 0.069) and highest in fibroblast/skin (0.122).
- **Array conversion.** Keeping only the 113,585 probes shared by 450k and the new MSA array, CpGPT-100M rebuilt the remaining 450k probes at MAE 0.0314 zero-shot and 0.0244 after fine-tuning, against 0.3661 for the sample mean. The intrinclock's correlation with age rose from 0.920 (mean imputation) to 0.984 with imputed probes. EPIC → mammalian array conversion reached MAE 0.0419, against 0.2164 for the rule-based mLiftOver. Clock values from the reconstructed mammalian or EPIC data were less faithful.
- **Unseen species.** Trained only on human arrays and then fine-tuned on 43 mammalian species, the model imputed half-masked chimpanzee data (an unseen test species) at MAE 0.0814 against 0.3257 for the sample mean. Accuracy was better for species closer to humans.
- **Single-cell methylation is a narrow result.** On sciMETv3 brain cells, zero-shot CpGPT-100M had AUPRC 0.882, the fine-tuned model 0.909 and a PyTorch reimplementation of DeepCpG 0.897. On AUROC, **DeepCpG was best**. Statistical baselines were near random.
- **Iterative refinement helps a little.** Feeding back the most confident predictions lowered MSA → 450k MAE from 0.0554 to 0.0534 over 10 steps of 500 CpGs. Gains reversed after more steps.
- **Fine-tuned prediction.** Chronological age on AltumAge: MAE 3.29 years and Pearson r 0.9847, against 11.37 years for ElasticNet and 5.51 for an MLP. Median Spearman over 322 plasma proteins: 0.204 against 0.177 for ElasticNet. Cancer vs adjacent normal: AUROC 0.9544, about the same as the MLP (0.9519). Predictions stayed stable across 10 random 10,000-CpG input subsets (ICC above 0.99 for most heads, lowest 0.919).
- **Mortality.** CpGPTGrimAge3 combines 7 GrimAge2 proxies and 23 CpGPT protein proxies in a Cox model trained on Framingham (N = 3,853). In three held-out cohorts its hazard ratio per SD was the largest of nine clocks: about 3.7 (MGB, N = 4,387), 2.1 (WHI, N = 2,101) and 4.6 (BLSA, N = 768). Across 34 mortality and disease comparisons it ranked in the top two 30 times and first 18 times. PCGrimAge was its closest competitor.

## Methods / evidence

Architecture: sequence embedding through an MLP adapter, plus a sinusoidal absolute position encoding scaled to chromosome length, plus rotary embeddings; added to a beta-value embedding (scaled by 1/√2). A Transformer++ stack (SwiGLU, RMSNorm, no biases) with a CLS token. Decoders take the inner product of a projected locus embedding with the CLS state to predict M values and their uncertainty. Losses: MAE on M values, MAE on the uncertainty, a Wasserstein distance between predicted and true distributions, a KL term on sample embeddings, and the scGPT-style contrastive loss. Masking ratio is 50%, chosen to match the half-missing case of converting between arrays. Chromosome order is shuffled each batch so the model cannot tie input position to a fixed locus.

Data: CpGCorpus was processed with SeSAMe where IDAT files existed, and otherwise from the authors' processed beta matrices. Splits were made by study (training 150,719 samples from 1,986 studies; test 4,258 from 46). Downstream sets include AltumAge, Hannum, a human RRBS atlas, GSE223748 mammalian arrays, sciMETv3 single-cell data, Biomarkers of Aging proteomics and four mortality cohorts (FHS, MGB, WHI, BLSA). Code, weights and the CpGCorpus are public.

Weight: a broad, carefully baselined paper for bulk array tasks. Most imputation baselines are simple means, so the large MAE gains show the model beats trivial imputation, not that it beats other learned imputers. The single-cell test has one learned comparator. Several authors report consulting fees from methylation-clock companies, and S.H. holds patents on epigenetic biomarkers and the mammalian array. (synthesis)

## Limitations

**Authors' own:**
- Pretraining data are dominated by human bulk array methylation. Performance varied across tissues, platforms and species.
- Specialised methods stayed competitive in some areas, especially single-cell methylation. Foundation models complement task-specific tools rather than replace them.
- Future work should expand CpGCorpus beyond arrays and add more non-human and longitudinal data.
- Clock values from reconstructed EPIC ↔ mammalian data were less faithful than the low MAE suggests.
- Iterative refinement stops helping once the added predictions reach about the size of the original input.

**Reviewer notes:**
- The model has never been pretrained on sequencing-based or single-cell methylomes. Its "single-cell" result is one fine-tuned dataset filtered to cells with at least 1,000 CpGs that fall on array probes, so it says little about genome-wide scBS-seq beyond array loci. (synthesis)
- Array probes cover a biased subset of CpGs (about 1.17M of ~28M in the genome). "Unseen loci" means unseen array probes, not arbitrary genomic CpGs. (synthesis)
- Transformer++ is cited to the Mamba paper, which looks like a referencing slip. (synthesis)

## Surprising or load-bearing bits

- **Sequence as the locus identifier.** Using DNA-LM embeddings instead of probe IDs is what lets the model query new CpGs and move between array designs. This is the general trick that separates CpGPT from fixed-vocabulary clocks. (synthesis)
- **Attention adds only about 14%.** Removing all transformer blocks raised error from 0.0704 to 0.0802. Much of the signal comes from the sequence and position embeddings alone.
- **Fine-tuning swaps the main axis of the embedding.** On mammals, pretraining organised samples by species and fine-tuning reorganised them by tissue. What a methylation embedding "means" depends on the training target. (synthesis)
- **DeepCpG is still competitive** on single-cell imputation (best AUROC), which is a useful calibration point for single-cell methylation foundation models.

## Entities mentioned

- [[20-Entities/andrew-adey]] — senior author of sciMETv3, the single-cell methylation dataset CpGPT is fine-tuned and tested on (cited, not an author here).

## Concepts touched

- [[single-cell-foundation-model]] — a bulk-trained methylation foundation model that is adapted to single-cell data only by fine-tuning.
- [[dna-language-model]] — uses frozen NTv2-500M embeddings as locus descriptors; NTv2 beat HyenaDNA in the ablation.
- [[epigenetic-aging]] — age, mortality and morbidity clocks, including CpGPTGrimAge3.
- [[imputation]] — zero-shot imputation of held-out probes and array conversion.
- [[cpg-island]] — CGI is one of the six annotation sets used to score locus embeddings.
- [[bisulfite-sequencing]] — RRBS atlas and sciMETv3 are the sequencing-based test sets.

## Connections to other sources

- Concurrent bulk methylation foundation model: [[ying-2024-methylgpt]]. The two differ in tokens: MethylGPT uses a fixed 49,156-CpG vocabulary, CpGPT uses sequence embeddings and so can query new CpGs. (synthesis)
- Single-cell methylation counterpart pretrained on single cells: [[liang-2025-scdnam-gpt]].
- Single-cell imputation baseline: [[angermueller-2017-genomebiol]] (DeepCpG). Wider benchmark context for single-cell methylation imputation: [[liang-2026-scmeth-imputation-benchmark]].
- Single-cell test data come from sciMETv3: [[nichols-2025-scimetv3]].
- Sequence encoders compared: [[dallatorre-2025-nucleotide-transformer]] (chosen) and [[nguyen-2023-hyenadna]].
- Contrastive loss borrowed from scGPT: [[cui-2024-natmethods]].

## Open questions

- How would CpGPT do if pretrained on whole-genome bisulfite or single-cell data instead of arrays? The authors list this as future work.
- Does the single-cell result hold for cells with fewer than 1,000 array-overlapping CpGs, which is common in sparse scBS-seq? (synthesis)
- The gap between low imputation MAE and weaker clock fidelity after EPIC ↔ mammalian conversion suggests errors concentrate on clock CpGs. This is not analysed. (synthesis)

## Related

- [[ying-2024-methylgpt]] · [[liang-2025-scdnam-gpt]] · [[angermueller-2017-genomebiol]] · [[epigenetic-aging]] · [[single-cell-foundation-model]] · [[40-Topics/dna-methylation]] · [[40-Topics/sequence-models-and-foundation-models]]
