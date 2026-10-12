---
type: concept
title: cis-regulatory element
aliases: [cRE, regulatory element, enhancer, promoter]
tags: [regulation, enhancer, promoter, chromatin]
created: 2026-05-12
updated: 2026-10-12
---

# cis-regulatory element (cRE)

> A non-coding DNA region — enhancer, promoter, silencer, insulator — that controls the expression of nearby (or distant via 3D contact) genes through transcription factor binding (synthesis).

> [!abstract] 한눈에
> cis-regulatory element는 enhancer, promoter, silencer, insulator처럼 TF 결합을 통해 가까운 유전자나 3차원 접촉으로 이어진 먼 유전자의 발현을 조절하는 비암호화 DNA 구간이다. 최근 sequence model은 서열만으로 이런 요소를 찾고 enhancer–gene 연결을 ABC score 수준으로 맞히지만, 거리가 멀어질수록 enhancer 효과를 과소평가하는 한계가 남아 있다 ([[10-Summaries/avsec-2021-enformer|Enformer]]; [[10-Summaries/lal-2026-decima|Decima]]).

## Definition

cREs include enhancers, promoters, silencers and insulators; they act on nearby genes, or on distant ones through 3D contact, by binding transcription factors (synthesis). Single-cell chromatin accessibility maps (scATAC-seq, scCUT&Tag) identify cREs across cell types and developmental stages (synthesis).

## Why it matters

- cREs encode tissue-specific and developmental gene-expression programs (synthesis).
- They are the primary substrate of disease GWAS variants, about 90% of which fall outside coding regions (synthesis).
- Enhancer and promoter sequence classes explain most UK Biobank heritability for 47 traits, with 83 class–trait associations surviving conditioning on baseline annotations ([[10-Summaries/chen-2022-sei|Sei]]).

## Approaches

### Finding and annotating elements from sequence

| Model | What it does | Key result | Source |
|---|---|---|---|
| Basenji | Saliency maps from sequence | Distinguishes promoters, enhancers and CTCF sites from background in GM12878; found two PIM1 enhancers (POU2F and PU.1 motifs) supported by TF knockdown data | ([[10-Summaries/kelley-2018-basenji\|Basenji]]) |
| AIDO.DNA (7B masked DNA language model) | Unsupervised nucleotide-dependency map | Recovers promoters, TF binding sites and a putative minisatellite enhancer at KIF26B in O(L) inferences, without labels | ([[10-Summaries/ellington-2024-aido-dna\|AIDO.DNA]]) |
| SegmentNT | Base-resolution segmentation of ENCODE cCRE promoters and enhancers | Remains hard: enhancer MCC 0.27 (tissue-specific) and 0.19 (tissue-invariant), with mispredictions enriched inside whole regions rather than at their edges | ([[10-Summaries/dealmeida-2025-segmentnt\|SegmentNT]]) |
| Atacformer | Contextualised region embeddings from scATAC | Separated ENCODE pELS from dELS without TSS labels; distal regions embedded near the promoter centroid (icTSSs) showed about 6-fold enrichment for cell-matched H3K4me3 | ([[10-Summaries/leroy-2025-atacformer\|Atacformer]]) |
| Decima | Attributions from an expression model | Highest at promoters; scores intronic and distal ENCODE CREs above background | ([[10-Summaries/lal-2026-decima\|Decima]]) |

### Linking enhancers to genes

| Method | Input | Key result | Source |
|---|---|---|---|
| SnapHiC-G on sn-m3C-seq brain data | Cell-type-specific enhancer–promoter interactions from single-cell contacts | Assigned noncoding GWAS variants to about one target gene each, versus 25–83 genes within ±1 Mb | ([[10-Summaries/liu-2024-snaphic-g\|SnapHiC-G]]) |
| Enformer | DNA sequence alone (contribution scores) | Ranked CRISPRi-validated K562 enhancer–gene pairs about as well as the ABC score, which uses measured H3K27ac and Hi-C | ([[10-Summaries/avsec-2021-enformer\|Enformer]]) |
| GET | Jacobian scores | Called enhancer–gene links at fetal haemoglobin loci more accurately than Enformer, HyenaDNA, DeepSEA or ABC, especially for long-range pairs, including regions more than 1 Mb away | ([[10-Summaries/fu-2025-get\|GET]]) |
| EPInformer | Final-layer promoter-to-enhancer attention | Linked CRISPRi-validated K562 enhancers to genes better than ABC with identical inputs (AUPRC 0.732 vs 0.698 with Hi-C), especially at 60–100 kb (0.510 vs 0.429) | ([[10-Summaries/lin-2026-epinformer\|EPInformer]]) |
| Decima | CRISPRi comparison | Learned enhancer effects decay with distance just as in earlier sequence models | ([[10-Summaries/lal-2026-decima\|Decima]]) |

### Variant effects in regulatory elements

- ExPecto's in-silico scan of >140 million promoter-proximal mutations placed expression-decreasing mutations mainly near −50 bp, the core-promoter position, and stronger-effect bases were more conserved ([[10-Summaries/zhou-2018-expecto|ExPecto]]).
- GPN-MSA, an alignment-based DNA language model, ranks curated Mendelian promoter and enhancer variants (OMIM) above gnomAD common variants better than CADD, phyloP or Nucleotide Transformer ([[10-Summaries/benegas-2025-gpn-msa|GPN-MSA]]).
- In-silico restoration of single enhancers on a shuffled HBE1 background recovers the measured HS2 > HS1 > HS4 > HS3 > HS5 hierarchy (Spearman rho = 0.900, p = 0.037) from sequence alone ([[10-Summaries/boshar-2025-ntv3|NTv3]]).

### Designing elements

| Model | Design setting | Key result | Source |
|---|---|---|---|
| HybriDNA | Prompt-conditioned 200-bp human enhancers | Predicted top-100 mean activity (5.4/6.2/4.7 in HepG2/K562/SK-N-SH) exceeded both HyenaDNA's designs and held-out natural sequences under the regLM oracle, with comparable diversity | ([[10-Summaries/ma-2025-hybridna\|HybriDNA]]) |
| ATGC-Gen | FANTOM-derived promoter benchmark, conditioned on a per-base transcription-initiation profile | Conditioning only works when the signal stays aligned per token; pooling it into a prefix worsens MSE from 0.0192 to 0.0289 | ([[10-Summaries/su-2025-atgc-gen\|ATGC-Gen]]) |
| GENERator | Prompt tokens (<high>/<mid>/<low>) plus a fine-tuned activity predictor for Drosophila CREs, tested on 12,026 oligos by UMI-STARR-seq | Best housekeeping design exceeded the strongest natural sequence by 35%; the weakest designs were over 100-fold below the weakest natural sequences | ([[10-Summaries/li-2026-generator\|GENERator]]) |

## Evidence and examples

- Cell-type-specific enhancer–promoter interactions from sn-m3C-seq brain data recovered 29 fine-mapped AD variants in microglia and 9 fine-mapped SCZ variants in L2/3 neurons ([[10-Summaries/liu-2024-snaphic-g|SnapHiC-G]]).
- Somatic mutations in human neurons are enriched in neuron-specific regulatory elements: TSS-distal enhancers showed ~1.3 (SNV) and ~1.8 (indel) observed:expected, strongest for brain, and indels (not SNVs) were enriched at promoters ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]).
- TAL1 downstream enhancer I, mutated in 6% of TAL1 T-ALLs, already holds MYB, GATA3, RUNX1 and TAL1 motifs in the reference genome, so somatic indels (6 of 8 creating de novo MYB sites) and ITDs (79 bp to 10.5 kb) reactivate it rather than creating a neo-enhancer ([[10-Summaries/terekhanova-2026-tal1-enhancer|Terekhanova 2026]]).

## Contested points

- **Distance.** GET and EPInformer report their largest gains over ABC on long-range pairs ([[10-Summaries/fu-2025-get|GET]]; [[10-Summaries/lin-2026-epinformer|EPInformer]]), while Decima's learned enhancer effects still decay with distance as in earlier sequence models ([[10-Summaries/lal-2026-decima|Decima]]); whether sequence models capture distal regulation is not settled (synthesis).
- **Sequence vs measured chromatin.** Enformer's sequence-only scores match the ABC score, which needs measured H3K27ac and Hi-C ([[10-Summaries/avsec-2021-enformer|Enformer]]), yet base-resolution enhancer segmentation remains poor ([[10-Summaries/dealmeida-2025-segmentnt|SegmentNT]]); ranking known enhancer–gene pairs and delimiting elements are different tasks (synthesis).
- **Design claims rest on oracles.** HybriDNA's enhancer activity is predicted under the regLM oracle ([[10-Summaries/ma-2025-hybridna|HybriDNA]]), whereas GENERator's designs were tested by UMI-STARR-seq ([[10-Summaries/li-2026-generator|GENERator]]) (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — Open vs closed DNA, the main way cREs are mapped.
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Genome-wide accessibility in individual cells.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone marks that demarcate functional chromatin states, including active enhancers.
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — How DNA is packaged along chromosomes and how that varies across fibers, haplotypes and cells.

## All sources on this page

> [!info]- 18 summaries cited here
> - [[10-Summaries/avsec-2021-enformer|Enformer 2021]]
> - [[10-Summaries/benegas-2025-gpn-msa|GPN-MSA 2025]]
> - [[10-Summaries/boshar-2025-ntv3|NTv3 2025]]
> - [[10-Summaries/chen-2022-sei|Sei 2022]]
> - [[10-Summaries/dealmeida-2025-segmentnt|SegmentNT 2025]]
> - [[10-Summaries/ellington-2024-aido-dna|AIDO.DNA 2024]]
> - [[10-Summaries/fu-2025-get|GET 2025]]
> - [[10-Summaries/kelley-2018-basenji|Basenji 2018]]
> - [[10-Summaries/lal-2026-decima|Decima 2026]]
> - [[10-Summaries/leroy-2025-atacformer|Atacformer 2025]]
> - [[10-Summaries/li-2026-generator|GENERator 2026]]
> - [[10-Summaries/lin-2026-epinformer|EPInformer 2026]]
> - [[10-Summaries/liu-2024-snaphic-g|Liu 2024]]
> - [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]
> - [[10-Summaries/ma-2025-hybridna|HybriDNA 2025]]
> - [[10-Summaries/su-2025-atgc-gen|ATGC-Gen 2025]]
> - [[10-Summaries/terekhanova-2026-tal1-enhancer|Terekhanova 2026]]
> - [[10-Summaries/zhou-2018-expecto|ExPecto 2018]]
