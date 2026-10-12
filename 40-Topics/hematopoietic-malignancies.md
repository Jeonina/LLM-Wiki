---
type: topic
title: Hematopoietic malignancies
explainer: hematopoietic-malignancies
aliases: [blood cancers, myeloid malignancies]
tags: [hematology, cancer, clonal-evolution]
created: 2026-05-07
updated: 2026-10-12
paper_section: ["5.1"]
---

# Hematopoietic malignancies

> Cancers and pre-cancerous clonal expansions arising from hematopoietic stem and progenitor cells. The wiki's main focus is [[30-Concepts/myeloproliferative-neoplasm|myeloproliferative neoplasms]] (MPN), a tractable model for how single somatic mutations corrupt normal hematopoiesis ([[10-Summaries/nam-2019-got|Nam 2019]]; [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]), with leukaemia and lymphoma sources on clonal architecture alongside.

> [!abstract] 한눈에
> 혈액암은 같은 표면 marker를 공유하는 변이 세포와 정상 세포를 한 환자 안에서 구분해야 하는 문제이며, GoT 계열 방법은 MPN에서 genotype과 전사체·chromatin 상태를 한 세포에서 함께 읽어 이를 해결한다 ([[10-Summaries/nam-2019-got|Nam 2019]]; [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]). 백혈병에서는 single-cell genotyping이 bulk VAF로 추정한 founder 클론을 뒤집거나 bulk가 놓친 소수 subclone을 찾아낸다 ([[10-Summaries/pellegrino-2018-tapestri|Pellegrino 2018]]; [[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [혈액암 교재](../60-Explainers/hematopoietic-malignancies.html)
<!-- /explainer-links -->

## Key points

- **Mutant and wild-type cells share surface markers, so they must be split by genotype in the same cell.** Both GoT papers use MPN as their proving ground for this reason: recurrent, well-characterised drivers in clinically obtainable CD34⁺ samples ([[10-Summaries/nam-2019-got|Nam 2019]]; [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- **CALR-mutant output depends on cell identity.** In CALR-mutated ET and MF, UPR and NF-κB outputs differ by progenitor type ([[10-Summaries/nam-2019-got|Nam 2019]]).
- **JAK2V617F primes chromatin cell-intrinsically.** GoT–ChA finds a pro-inflammatory chromatin program in mutant cells, which ruxolitinib reverses at the TF-motif level without removing the clone ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- **Single-cell genotyping can overturn bulk founder inference.** In one AML patient, bulk VAFs predicted a 23.6% DNMT3A single-mutant founder population, but single cells found 1.7% and pointed to TP53 as the founder ([[10-Summaries/pellegrino-2018-tapestri|Pellegrino 2018]]).
- **Childhood ALL often holds several codominant clones.** Five of six patients had codominant clones, with structural variants acquired before point mutations ([[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/myeloproliferative-neoplasm|Myeloproliferative neoplasm]] — The disease class (ET, PV, MF) and its driver landscape.
> - `concept` [[30-Concepts/calr-mutation|CALR mutation]] — Driver in ~25–30% of MPN; chaperone disruption leads to UPR; cell-identity-dependent transcriptional output.
> - `concept` [[30-Concepts/jak2-v617f|JAK2 V617F]] — Most common MPN driver; constitutive JAK-STAT activation; chromatin priming visible at clonal hematopoiesis.
> - `concept` [[30-Concepts/unfolded-protein-response|Unfolded protein response]] — Load-bearing output of CALR mutation, with branch use depending on cell type.
> - `concept` [[30-Concepts/hematopoietic-differentiation|Hematopoietic differentiation]] — The native scaffold against which mutated clones are mapped.
> - `concept` [[30-Concepts/intratumor-heterogeneity|Intratumor heterogeneity]] — Variation between cells within one tumour, and how cell number shapes its measured size.

## Genotype-to-phenotype in MPN

Bulk and uncoupled single-cell assays cannot separate mutated from wild-type cells in the same patient because they share surface markers; the Landau-lab GoT methods genotype each cell alongside its phenotype ([[10-Summaries/nam-2019-got|Nam 2019]]; [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

| Study | System | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/nam-2019-got\|Nam 2019]] | CALR-mutated ET and MF | GoT: genotyping of transcriptomes | UPR and NF-κB outputs depend on cell identity ([[10-Summaries/nam-2019-got\|Nam 2019]]) |
| [[10-Summaries/izzo-2024-got-cha\|Izzo 2024]] | JAK2V617F MF, PV→MF, clonal hematopoiesis | GoT–ChA: genotyping with chromatin accessibility | Cell-intrinsic pro-inflammatory chromatin priming ([[10-Summaries/izzo-2024-got-cha\|Izzo 2024]]) |

## Clonal architecture in leukaemia

| Study | System | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/gawad-2014-all-clonal-origins\|Gawad 2014]] | Childhood ALL, 6 patients | Microfluidic MDA + targeted resequencing, 1,479 single cells | Codominant clones in five of six; structural variants before point mutations; APOBEC-like TC-motif cytosine bias; subclonal, late *KRAS*; clones arrested at different B-cell stages in the same patient ([[10-Summaries/gawad-2014-all-clonal-origins\|Gawad 2014]]) |
| [[10-Summaries/pellegrino-2018-tapestri\|Pellegrino 2018]] | AML | Tapestri droplet scDNA-seq | Bulk VAF founder (DNMT3A, 23.6%) vs single-cell founder (TP53; DNMT3A single mutants 1.7%) ([[10-Summaries/pellegrino-2018-tapestri\|Pellegrino 2018]]) |
| [[10-Summaries/sollier-2023-compass\|COMPASS]] | AML/MPN | Tapestri re-analysis, joint SNV + CNA/CNLOH trees | FLT3 CNLOH, EZH2 deletion, subclonal TP53 loss and JAK2 CNLOH ([[10-Summaries/sollier-2023-compass\|COMPASS]]) |
| [[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]] | Diagnostic paediatric B-ALL | DNTR-seq + ASCENT, 324 cells | Four subclones, including a 3% minor clone with breakpoints not seen in bulk WGS, and a small chr12 copy-neutral LOH confirmed by bulk WGS ([[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]]) |
| [[10-Summaries/pancikova-2025-splongget\|SPLONGGET]] | High-hyperdiploid paediatric B-ALL, diagnosis + three relapses | Long-read multiome (preprint) | CD19-negative relapse after CAR-T explained by an 8 Mb chr16 deletion plus four phased splice-site SNVs ([[10-Summaries/pancikova-2025-splongget\|SPLONGGET]]) |

Tools validated on blood data:

- **SCIΦ** validates on a panel ALL dataset ([[10-Summaries/singer-2018-sciphi|SCIΦ]]).
- **MQuad** supplies the mtDNA-variant selection step used for clonal substructure discovery in blood ([[10-Summaries/kwok-2022-mquad|MQuad]]).

See also [[30-Concepts/chromosomal-instability]].

## Lymphoid cancers and CLL

- **Methylation barcodes.** EVOFLUx applies fluctuating-CpG methylation barcodes to 1,976 lymphoid cancer samples: growth rate, malignancy age and epimutation rate vary by orders of magnitude across disease types; evolutionary history is a strong independent prognostic factor in two separate CLL series; the seed of a Richter-transformed CLL clone existed decades before presentation ([[10-Summaries/gabbutt-2025-evoflux|EVOFLUx]]).
- **Multi-omics factors.** MOFA on 200 CLL patients (mutations, RNA, methylation, ex vivo drug response) finds factors for IGHV status and trisomy 12, an oxidative-stress axis, and factors predicting time to next treatment ([[10-Summaries/argelaguet-2018-mofa|MOFA]]).
- **Archival tissue.** scFFPE-ATAC profiles paired primary/relapsed follicular lymphoma and FL→DLBCL transformation from archival FFPE ([[10-Summaries/yadav-2025-scffpe-atac|scFFPE-ATAC]]).

## Regulatory variants and sequence models

- **AlphaGenome on TAL1.** It predicted that oncogenic TAL1 neo-enhancer insertions in T-ALL create a MYB motif and raise H3K27ac, accessibility and TAL1 expression, using CD34⁺ CMP tracks as the closest available proxy for the T-ALL cell of origin ([[10-Summaries/avsec-2026-alphagenome|AlphaGenome]]).
- **A miss on a held-out enhancer.** In pediatric T-ALL, somatic indels and internal tandem duplications in TAL1 downstream enhancer I (25 of 391 TAL1 cases) drive mono-allelic expression of the short TAL1 isoform from an exon-4 promoter by reactivating a progenitor enhancer, and AlphaGenome did not predict this effect ([[10-Summaries/terekhanova-2026-tal1-enhancer|Terekhanova 2026]]).

## Key people

- [[20-Entities/anna-s-nam]] — first author of the GoT paper; pathologist-scientist at Weill Cornell.
- [[20-Entities/franco-izzo]] — first author of GoT–ChA; postdoc-to-PI trajectory in the Landau lab.
- [[20-Entities/dan-a-landau]] — senior author of both GoT and GoT–ChA; clonal-evolution methods PI.
- [[20-Entities/landau-lab]] — group hub for the GoT family of methods applied to hematopoietic malignancies.

## Open questions

- Why is CALR-mutant fitness advantage differentiation-dependent in ET but already strong in HSPCs in MF? GoT observes the difference but does not explain the switch ([[10-Summaries/nam-2019-got|Nam 2019]]).
- Is the cell-intrinsic NF-κB chromatin program in JAK2V617F HSCs causal for clonal expansion, or downstream of it ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]])?
- Does the IRE1-XBP1 therapeutic hypothesis ([[10-Summaries/nam-2019-got|Nam 2019]]) hold up in MPN clinical trials? The wiki has no source on this yet.
- Ruxolitinib reverses the chromatin TF-motif phenotype but not the clone ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]). Does combination therapy targeting the cell-intrinsic chromatin program (e.g. NF-κB or BET inhibitors) eliminate the clone in vivo?
- ~~Other hematopoietic malignancies (AML, CLL, MDS) are not yet represented in the vault~~ — AML and CLL now appear through the clonal-architecture, EVOFLUx and MOFA sources above, but MDS still has no source (synthesis). The [[20-Entities/landau-lab]] history references CLL clonal-evolution work that would extend this topic substantially.
- AlphaGenome reproduces the TAL1 neo-enhancer effect but not the enhancer-I indel/ITD effect, so sequence-model predictions for blood-cancer regulatory variants remain unreliable ([[10-Summaries/avsec-2026-alphagenome|AlphaGenome]]; [[10-Summaries/terekhanova-2026-tal1-enhancer|Terekhanova 2026]]). (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/clonal-hematopoiesis|Clonal hematopoiesis]] — Mosaic HSC clonal expansions; the precursor state to MPN, MDS and AML.
> - `hub` [[40-Topics/cancer-clonal-evolution|Cancer clonal evolution]] — Somatic mutation and clonal selection behind tumour heterogeneity, treatment response and metastasis.

## All sources on this page

> [!info]- 14 summaries cited here
> - [[10-Summaries/argelaguet-2018-mofa|Argelaguet 2018]]
> - [[10-Summaries/avsec-2026-alphagenome|AlphaGenome 2026]]
> - [[10-Summaries/gabbutt-2025-evoflux|Gabbutt 2025]]
> - [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/kolbeinsdottir-2025-ascent|Kolbeinsdottir 2025]]
> - [[10-Summaries/kwok-2022-mquad|Kwok 2022]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
> - [[10-Summaries/pancikova-2025-splongget|Pančíková 2025 (bioRxiv preprint)]]
> - [[10-Summaries/pellegrino-2018-tapestri|Pellegrino 2018]]
> - [[10-Summaries/singer-2018-sciphi|Singer 2018]]
> - [[10-Summaries/sollier-2023-compass|Sollier 2023]]
> - [[10-Summaries/terekhanova-2026-tal1-enhancer|Terekhanova 2026]]
> - [[10-Summaries/yadav-2025-scffpe-atac|Yadav 2025]]
