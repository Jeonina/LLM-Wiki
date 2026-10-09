---
type: concept
title: Variant effect prediction
aliases: [VEP, variant effect scoring, in silico mutagenesis, noncoding variant interpretation, zero-shot variant scoring]
tags: [variant-effect, deep-learning, eQTL, ClinVar, noncoding]
created: 2026-10-08
updated: 2026-10-09
---

# Variant effect prediction

> Estimating the functional consequence of a DNA variant by comparing a model's outputs for the reference and alternative alleles — predicted tracks for a [[sequence-to-function-model]], likelihoods or embeddings for a [[dna-language-model]] ([[10-Summaries/zhou-2015-deepsea]]; [[10-Summaries/benegas-2025-gpn-msa]]).

## Definition

Four scoring modes appear in this wiki (synthesis):
1. **Track difference.** Predict functional tracks for both alleles and take the difference, as in DeepSEA, Basenji's SED, Enformer, Borzoi and AlphaGenome ([[10-Summaries/zhou-2015-deepsea]]; [[10-Summaries/kelley-2018-basenji]]; [[10-Summaries/avsec-2021-enformer]]; [[10-Summaries/linder-2025-borzoi]]; [[10-Summaries/avsec-2026-alphagenome]]).
2. **Likelihood ratio.** Score the change in the language model's log-likelihood, zero-shot ([[10-Summaries/benegas-2025-gpn-msa]]; [[10-Summaries/brixi-2026-evo2]]; [[10-Summaries/li-2026-generator]]).
3. **Embedding distance.** Measure how far the alternative embedding moves from the reference ([[10-Summaries/dallatorre-2025-nucleotide-transformer]]; [[10-Summaries/ellington-2024-aido-dna]]).
4. **Supervised classifier.** Fine-tune on labelled variants such as ClinVar ([[10-Summaries/vishniakov-2025-gene42]]; [[10-Summaries/ayanian-2025-strand]]).

## Why it matters

- It is the main practical use of both model families and the bridge from a GWAS or eQTL hit to a mechanism ([[10-Summaries/zhou-2018-expecto]]; [[10-Summaries/chen-2022-sei]]).
- **Somatic variants are barely tested.** Nearly every benchmark here is germline (eQTL, caQTL, ClinVar, gnomAD); the exceptions are GPN-MSA on COSMIC somatic missense, EpiZoo on TCGA noncoding variants and AlphaGenome's case study of oncogenic TAL1 neo-enhancer insertions in T-ALL ([[10-Summaries/benegas-2025-gpn-msa]]; [[10-Summaries/li-2026-epizoo]]; [[10-Summaries/avsec-2026-alphagenome]]). Applying these scores to mosaic variants from single-cell DNA remains untested (synthesis).

## Variants and refinements

**Models in this wiki** (38, by year):

- **DeepSEA** (2015) — DeepSEA scores variants by predicting reference and alternative alleles; though never trained on variants, its DHS predictors picked the more accessible allele with >95% accuracy for 6,726 confidently predicted allelically imbalanced SNPs ([[10-Summaries/zhou-2015-deepsea]])
- **Basset** (2016) — Basset's SNP accessibility difference (SAD) scores were higher for 235 high-PICS than for 3,004 low-PICS autoimmune GWAS SNPs (P < 1.3e-7), and predicted a CTCF-site gain at rs4409785 confirmed by allele-specific CTCF ChIP-seq ([[10-Summaries/kelley-2016-basset]])
- **Basenji** (2018) — Basenji SNP expression difference scores, projected through LD, correlated with GTEx eQTL χ² in all 19 matched tissues and gave 3.2–5.8× eQTL enrichment in the top quantile; combined with DeepSEA they reached AUROC 0.706 on GWAS Catalog SNPs ([[10-Summaries/kelley-2018-basenji]])
- **ExPecto** (2018) — ExPecto, never trained on variants, predicted the direction of 92% of the top 500 GTEx eQTLs and prioritised three GWAS LD SNPs (IRGM, CCR1, HLA-DOA) that changed luciferase activity while the seven lead SNPs did not ([[10-Summaries/zhou-2018-expecto]])
- **Akita** (2020) — Akita disruption scores were larger for GTEx whole-blood eQTLs with higher fine-mapping posterior, both inside and outside CTCF motifs, and in-silico deletions and inversions reproduced engineered Lmo2 and Epha4 rearrangements ([[10-Summaries/fudenberg-2020-akita]])
- **DNABERT** (2021) — DNABERT scores variants by re-predicting high-attention regions with the alternative allele; 24.7–31.4% of the dbSNP Common variants it flagged in promoter data appear in ClinVar, GRASP or the GWAS Catalog ([[10-Summaries/ji-2021-dnabert]])
- **Enformer** (2021) — On fine-mapped GTEx eQTLs, random forests built on Enformer's 5,313 reference-minus-alternative features beat Basenji2 in 47 of 48 tissues (mean auROC 0.729→0.747), and Enformer features gave the best CAGI5 MPRA correlation ([[10-Summaries/avsec-2021-enformer]])
- **Orca** (2022) — Orca predicted 3D effects of structural variants from 2 kb boundary insertions (cosine 0.89 vs Hi-C over 14 sites) to a 40.5 Mb AML inversion, and its predictions agreed with chromatin conformation experiments across all six studies tested ([[10-Summaries/zhou-2022-orca]])
- **Sei** (2022) — Sei sequence-class scores make variant effects directional; among 138 strong-effect HGMD regulatory mutations ~80% decrease and ~20% increase class activity, with 44.9% hitting enhancer, 38.4% promoter and 15.9% CTCF–cohesin classes ([[10-Summaries/chen-2022-sei]])
- **AIDO.DNA** (2024) — Scoring ClinVar vs gnomAD variants by max-normalised L2 distance between mean-pooled reference and alternate embeddings gives AUROC 0.807 for AIDO.DNA-300M and 0.785 for the 7B model, against 0.720 for NT 2.5B — the smaller model wins ([[10-Summaries/ellington-2024-aido-dna]]).
- **Caduceus** (2024) — On an Enformer-derived eQTL task, SVMs on frozen Caduceus-PS embeddings beat the 500M-parameter NT-v2 increasingly with distance to the TSS and beat Enformer for SNPs more than 100 kb away ([[10-Summaries/schiff-2024-caduceus]])
- **ChromBPNet** (2024) — On Yoruba LCL dsQTLs, ChromBPNet's integrative score reached AP 0.54 (572 M-read ATAC) vs gkm-SVM 0.19 and Enformer's published scores 0.33, though Enformer rescored over a local 2-kb window reached 0.53 and beat depth-matched ChromBPNet ([[10-Summaries/pampari-2024-chrombpnet]])
- **EpiGePT** (2024) — Random forests built on EpiGePT log-ratio scores beat Enformer at separating causal from non-causal GTEx eQTLs (lung auPRC 0.922 vs 0.873), and adding EpiGePT features to CADD raised ClinVar auROC from 0.772 to 0.806 ([[10-Summaries/gao-2024-epigept]]).
- **BMFM-DNA** (2025) — On a new SNP-to-disease association task built from GWAS Catalog and ClinVar, SNP-aware pretraining gave no gain over reference pretraining (AUC 90 vs 90) ([[10-Summaries/li-2025-bmfm-dna]]).
- **BioFM** (2025) — On an 8-task Variant Benchmark with linear probes, BioFM averages AUROC 0.780 vs 0.727 for NT-500M-v2 and 0.726 for Evo2-7B, but no GFM, BioFM included, beats CADD, AlphaMissense or GPN-MSA on pathogenicity ([[10-Summaries/medvedev-2025-biofm]]).
- **Borzoi** (2025) — Statistics from Borzoi's predicted coverage separate fine-mapped eQTLs (AUROC 0.794 vs Enformer 0.747), 3′ paQTLs (better than APARENT2) and sQTLs (about even with Pangolin), but tissue-specific alternative splicing is mostly not captured ([[10-Summaries/linder-2025-borzoi]])
- **GENA-LM** (2025) — A GENA-LM promoter classifier separated pathogenic from benign ClinVar promoter SNVs with AUC 0.66, and pathogenic variants were enriched about 2.5-fold in the top-1% most important tokens by Integrated Gradients ([[10-Summaries/fishman-2025-gena-lm]]).
- **GPN-MSA** (2025) — GPN-MSA scores variants zero-shot as alt/ref log-likelihood ratios and gives the best AUPRC on OMIM regulatory and COSMIC somatic missense variants and the highest rare-vs-common gnomAD enrichment, but its scores are uncalibrated (synonymous variants centre near −3) ([[10-Summaries/benegas-2025-gpn-msa]]).
- **Gene42** (2025) — A supervised Gene42 ClinVar classifier reached AUC-ROC 0.931 on 8.8k held-out variants, while its zero-shot score was at chance (AUC 0.513) ([[10-Summaries/vishniakov-2025-gene42]]).
- **JanusDNA** (2025) — On DNALongBench causal-eQTL classification, a 7.7M-activated-parameter JanusDNA beat size-matched Caduceus and the 252M Enformer in 8 of 9 GTEx tissues, e.g. 0.914 vs 0.842 and 0.683 AUROC in tibial nerve ([[10-Summaries/duan-2025-janusdna]]).
- **MutBERT** (2025) — On the Enformer/NT eQTL causal-variant task MutBERT embeddings plus an SVM reach average AUROC 0.615, marginally above NTv2-500M (0.613) and DNABERT-2 (0.590) ([[10-Summaries/long-2025-mutbert]]).
- **NTv3** (2025) — Across 3,792 GTEx whole-blood eQTLs, NTv3's gradient-attribution differences are significantly larger for pathogenic than benign variants (Wilcoxon p < 0.001) and resolve them into motif ablation, motif creation and distributed rewiring ([[10-Summaries/boshar-2025-ntv3]]).
- **Nucleotide Transformer** (2025) — Zero-shot embedding-distance scores from Nucleotide Transformer reached AUC 0.7–0.8 for eQTL, meQTL, ClinVar and HGMD variants (0.80 for ClinVar with Multispecies 2.5B), and fine-tuned NT slightly beat or matched CADD, GERP, phyloP and DeepSEA ([[10-Summaries/dallatorre-2025-nucleotide-transformer]])
- **OmniReg-GPT** (2025) — OmniReg-GPT reached AUROC 0.724 on fine-mapped eQTL classification at 2 kb and 0.679 separating pathogenic ClinVar SNPs from common gnomAD variants, ahead of GENA-BigBird, NT-v2, DNABERT-2 and HyenaDNA ([[10-Summaries/wang-2025-omnireg-gpt]]).
- **STRAND** (2025) — Fine-tuned STRAND reports the best MCC on four of five new ClinVar-derived tasks (e.g. cardiovascular phenotype 77.4 vs 38.3 for NT-2.5B) and on RA and IBD variant tasks, though benchmark construction is only in an unavailable supplement ([[10-Summaries/ayanian-2025-strand]]).
- **scooby** (2025) — A scooby model trained on OneK1K came close to Borzoi on GTEx whole-blood eQTLs (Spearman 0.45 vs 0.47), beat it on cell-type sc-eQTLs, and was better than Borzoi, ATAC-peak and eGene-expression baselines at picking the cell type an eQTL acts in ([[10-Summaries/hingerl-2025-scooby]]).
- **AlphaGenome** (2026) — AlphaGenome matched or beat the best external model on 25 of 26 variant-effect benchmarks, raising eQTL effect-size Spearman ρ from 0.39 (Borzoi) to 0.49 and sign auROC from 0.75 to 0.80 ([[10-Summaries/avsec-2026-alphagenome]])
- **DNAChunker** (2026) — On BEND zero-shot scoring, DNAChunker leads on expression variants (AUROC 0.59) but is near chance on disease variants (0.55 vs 0.84 for PatchDNA) ([[10-Summaries/kim-2026-dnachunker]]).
- **DNT** (2026) — Reading the same trained model through DNT's diploid input instead of haploid input raises zygosity-aware ClinVar SNV AUROC in 10 of 11 arms by a mean of 0.106, while phase-blind models stay at chance on a synthetic cis/trans compound-heterozygous benchmark ([[10-Summaries/leib-2026-dnt]]).
- **Decima** (2026) — On fine-mapped OneK1K sc-eQTLs, Decima beat Borzoi in 19 of 21 cell types, its predictions correlated with eQTL beta at 0.42 (0.58 with 87% correct sign when it predicted any effect), and it placed higher effects in the matching cell type (P = 1.1e-7) ([[10-Summaries/lal-2026-decima]]).
- **EpiZoo** (2026) — EpiZoo-Cancer scores 5,959 TCGA noncoding variants by the decoded accessibility change after adding the alt−ref SEAM sequence embedding to cancer-type-conditioned cell embeddings; top-2.5% variants were enriched near COSMIC Tier 1 driver genes ([[10-Summaries/li-2026-epizoo]]).
- **Evo 2** (2026) — Zero-shot scoring as the change in model log-likelihood on mutation lets a nucleotide-level model score insertions, deletions and duplications that AlphaMissense and GPN-MSA cannot — Evo 2 40B beats all tested methods on ClinVar coding and noncoding non-SNVs, leads unsupervised models on noncoding SNVs and SpliceVarDB, but trails ESM-1b, GPN-MSA and some PhyloP variants on coding SNVs and trails ChromBPNet on caQTL/dsQTL (AUROC 0.58/0.66 vs 0.77/0.89) ([[10-Summaries/brixi-2026-evo2]])
- **GENERator** (2026) — Marginalising 6-mer token probabilities to per-nucleotide log-likelihood ratios gave zero-shot ClinVar AUROC 0.921 for GENERator-3B, matching Evo2-7B but still below alignment-based GPN-MSA (0.970) and CADD (0.966) ([[10-Summaries/li-2026-generator]]).
- **GenART** (2026) — GenART's authors report near-random zero-shot VEP because a point mutation shifts dynamic chunk boundaries and misaligns reference and alternate embeddings ([[10-Summaries/chen-2026-genart]]).
- **Genos** (2026) — Genos-10B reached AUC 0.9326 on the 8-kb LRB pathogenic-ClinVar task, above Evo2-40B (0.9167) and GENERator-3B (0.7206), but trailed on causal eQTL (0.6773 vs Evo2-40B 0.7054) ([[10-Summaries/lin-2025-genos]]).
- **Mendel** (2026) — Variants that Mendel predicts poorly across held-out donors are enriched for fine-mapped cis-eQTLs (mean hard miscall 0.22 vs 0.12 in MAF/TSS-matched controls), giving AUROC 0.731 for eQTL prioritisation ([[10-Summaries/salman-2026-mendel]]).
- **OmniNA** (2026) — Fine-tuned per gene on ClinVar/1000 Genomes SNVs in 1 kb windows, OmniNA-1.7B reaches mean F1 0.90 against 0.81 for EVE across 48 shared genes (p = 0.011), and its log-likelihood effect scores track pathogenic/benign odds ratios at PAS and TIS loci (r = 0.92) ([[10-Summaries/shen-2026-omnina]]).
- **UKBioBERT** (2026) — In-silico mutagenesis with UKBioFormer predicts the sign of more GTEx blood eQTLs than Performer (P = 0.02) or AlphaGenome (P = 0.06); for JUP, 71% of top-30 eQTLs are correctly signed vs 53% for Enformer ([[10-Summaries/liu-2026-ukbiobert]]).

## Contested points

- **Zero-shot DNA LMs versus conservation.** GENERator-3B (ClinVar AUROC 0.921) matched Evo 2 but trailed GPN-MSA (0.970) and CADD (0.966) ([[10-Summaries/li-2026-generator]]); in BioFM's benchmark no genomic foundation model beat CADD, AlphaMissense or GPN-MSA on pathogenicity ([[10-Summaries/medvedev-2025-biofm]]).
- **Zero-shot can be at chance.** Gene42's zero-shot ClinVar score was AUC 0.513 against 0.931 supervised ([[10-Summaries/vishniakov-2025-gene42]]); DNAChunker was near chance on disease variants ([[10-Summaries/kim-2026-dnachunker]]).
- **Specialists versus generalists.** Evo 2 trails ChromBPNet on caQTL/dsQTL ([[10-Summaries/brixi-2026-evo2]]), while AlphaGenome beats ChromBPNet on the same benchmarks ([[10-Summaries/avsec-2026-alphagenome]]).
- **Phase.** Phase-blind models stay at chance on a cis/trans compound-heterozygote benchmark ([[10-Summaries/leib-2026-dnt]]); in single cells, allele dropout would add a further error mode (synthesis).

## Added 2026-10-09 — foundation-model gap evidence

- In a UK Biobank CH study, AlphaGenome was used only to predict cis-gene expression effects of age-associated somatic variants in hematopoietic progenitors (e.g. TERT up-regulation for a TERT promoter mutation), without accuracy checks. Coding burden tests used AlphaMissense > 0.3 and added no discoveries ([[10-Summaries/weinstock-2025-ch-noncoding-drivers]])
- GenomeBert's REF-minus-ALT [CLS] embedding, fed to XGBoost, separates somatic cancer driver from passenger point mutations with AUROC 83.25% in cross-validation and 84.64% on an independent 71-mutation xenograft set, ahead of CHASM, REVEL and CADD ([[10-Summaries/zeng-2025-somatic-driver-lm]])
- Somatic use case: AlphaGenome scores for real normal-tissue somatic SNVs and indels from colonic crypts were no larger than scores for random genomic positions, which is an unvalidated null result rather than a benchmark ([[10-Summaries/fischbach-2026-alphagenome-aging]])
- REF-vs-ALT Akita contact-map differences (MSE, 1−correlation) were used to score about 300,000 somatic SVs across 61 paediatric tumour types; scores rose with SV length and were not correlated with tumour purity (Spearman R = −0.082) ([[10-Summaries/gjoni-2026-pediatric-tumor-3d]])
- A linear probe on TESSERA's somatic SNV embeddings reached ClinVar ROC AUC 0.865–0.869 (0.828 on held-out genes), and the model's masked-allele reconstruction accuracy works as a per-variant confidence filter ([[10-Summaries/sidhom-2026-tessera]])
- On 24 T-ALL patients with somatic indels or ITDs in TAL1 downstream enhancer I, a region not used in the AlphaGenome paper, AlphaGenome's CD34+ CMP TAL1 expression scores were significantly lower than for other TAL1 enhancer variants while measured expression was similar, and identical recurrent variants received one score despite variable patient expression ([[10-Summaries/terekhanova-2026-tal1-enhancer]])

## Related

- [[sequence-to-function-model]] · [[dna-language-model]] · [[genomic-tokenization]] · [[cis-regulatory-element]] · [[structural-variants]]
- [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/mosaic-variant-calling]]
