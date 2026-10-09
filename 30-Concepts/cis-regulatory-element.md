---
type: concept
title: cis-regulatory element
aliases: [cRE, regulatory element, enhancer, promoter]
tags: [regulation, enhancer, promoter, chromatin]
created: 2026-05-12
updated: 2026-10-09
---

# cis-regulatory element (cRE)

> A non-coding DNA region — enhancer, promoter, silencer, insulator — that controls the expression of nearby (or distant via 3D contact) genes through transcription factor binding.

## Why it matters

cREs encode tissue-specific and developmental gene-expression programs. They are the primary substrate of disease GWAS variants (~90% of which fall outside coding regions). Single-cell chromatin accessibility maps (scATAC-seq, scCUT&Tag) identify cREs across cell types and developmental stages.

## Added 2026-10-07

Cell-type-specific enhancer–promoter interactions called from sn-m3C-seq brain data assigned noncoding GWAS variants to about one target gene each, versus 25–83 genes within ±1 Mb, and recovered 29 fine-mapped AD variants in microglia and 9 fine-mapped SCZ variants in L2/3 neurons ([[10-Summaries/liu-2024-snaphic-g]]).

Somatic mutations in human neurons are enriched in neuron-specific regulatory elements: TSS-distal enhancers showed ~1.3 (SNV) and ~1.8 (indel) observed:expected, strongest for brain, and indels (not SNVs) were enriched at promoters [[10-Summaries/luquette-2022-neuron-scan2-indels]].


## Added 2026-10-08 — sequence models & foundation models

- Basenji saliency maps distinguish promoters, enhancers and CTCF sites from background in GM12878 and found two PIM1 enhancers (POU2F and PU.1 motifs) supported by TF knockdown data ([[10-Summaries/kelley-2018-basenji]])
- ExPecto's in-silico scan of >140 million promoter-proximal mutations placed expression-decreasing mutations mainly near −50 bp, the core-promoter position, and stronger-effect bases were more conserved ([[10-Summaries/zhou-2018-expecto]])
- Enformer contribution scores computed from DNA sequence alone ranked CRISPRi-validated K562 enhancer–gene pairs about as well as the ABC score, which uses measured H3K27ac and Hi-C ([[10-Summaries/avsec-2021-enformer]])
- Partitioning UK Biobank heritability over Sei's non-overlapping sequence classes shows enhancer and promoter classes explain most heritability for 47 traits, with 83 class–trait associations surviving conditioning on baseline annotations ([[10-Summaries/chen-2022-sei]])
- An unsupervised nucleotide-dependency map from a 7B masked DNA language model recovers promoters, TF binding sites and a putative minisatellite enhancer at KIF26B in O(L) inferences, without labels ([[10-Summaries/ellington-2024-aido-dna]]).
- GPN-MSA, an alignment-based DNA language model, ranks curated Mendelian promoter and enhancer variants (OMIM) above gnomAD common variants better than CADD, phyloP or Nucleotide Transformer ([[10-Summaries/benegas-2025-gpn-msa]]).
- In-silico restoration of single enhancers on a shuffled HBE1 background recovers the measured HS2 > HS1 > HS4 > HS3 > HS5 hierarchy (Spearman rho = 0.900, p = 0.037) from sequence alone ([[10-Summaries/boshar-2025-ntv3]]).
- Segmenting ENCODE cCRE promoters and enhancers at base resolution remains hard — enhancer MCC is 0.27 (tissue-specific) and 0.19 (tissue-invariant), with mispredictions enriched inside whole regions rather than at their edges ([[10-Summaries/dealmeida-2025-segmentnt]]).
- Using GET Jacobian scores, enhancer–gene links at fetal haemoglobin loci were called more accurately than with Enformer, HyenaDNA, DeepSEA or ABC, especially for long-range pairs, including regions more than 1 Mb away ([[10-Summaries/fu-2025-get]]).
- Atacformer's contextualised region embeddings separated ENCODE pELS from dELS without TSS labels; distal regions embedded near the promoter centroid (icTSSs) showed about 6-fold enrichment for cell-matched H3K4me3 ([[10-Summaries/leroy-2025-atacformer]]).
- Prompt-conditioned HybriDNA generated 200-bp human enhancers whose predicted top-100 mean activity (5.4/6.2/4.7 in HepG2/K562/SK-N-SH) exceeded both HyenaDNA's designs and held-out natural sequences under the regLM oracle, with comparable diversity ([[10-Summaries/ma-2025-hybridna]]).
- On the FANTOM-derived promoter benchmark, conditioning on a per-base transcription-initiation profile only works when the signal stays aligned per token; pooling it into a prefix drops MSE from 0.0192 to 0.0289 ([[10-Summaries/su-2025-atgc-gen]]).
- Decima's attributions are highest at promoters and score intronic and distal ENCODE CREs above background, but in a CRISPRi comparison its learned enhancer effects decay with distance just as in earlier sequence models ([[10-Summaries/lal-2026-decima]]).
- Prompt tokens (<high>/<mid>/<low>) plus a fine-tuned activity predictor produced Drosophila CREs tested on 12,026 oligos by UMI-STARR-seq, where the best housekeeping design exceeded the strongest natural sequence by 35% and the weakest designs were over 100-fold below the weakest natural sequences ([[10-Summaries/li-2026-generator]]).
- EPInformer's final-layer promoter-to-enhancer attention linked CRISPRi-validated K562 enhancers to genes better than the ABC score with identical inputs (AUPRC 0.732 vs 0.698 with Hi-C), especially at 60–100 kb (0.510 vs 0.429) ([[10-Summaries/lin-2026-epinformer]])

## Added 2026-10-09 — foundation-model gap evidence

- TAL1 downstream enhancer I, mutated in 6% of TAL1 T-ALLs, already holds MYB, GATA3, RUNX1 and TAL1 motifs in the reference genome, so somatic indels (6 of 8 creating de novo MYB sites) and ITDs (79 bp to 10.5 kb) reactivate it rather than creating a neo-enhancer ([[10-Summaries/terekhanova-2026-tal1-enhancer]])

## Related

- [[30-Concepts/chromatin-accessibility]] · [[30-Concepts/scatac-seq]] · [[40-Topics/histone-modifications]] · [[40-Topics/chromatin-architecture]]
