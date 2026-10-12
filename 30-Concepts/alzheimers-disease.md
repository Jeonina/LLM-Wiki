---
type: concept
title: Alzheimer's disease
aliases: [AD, dementia of Alzheimer type]
tags: [neurodegeneration, somatic-mosaicism, aging, ROSMAP]
created: 2026-05-12
updated: 2026-10-12
---

# Alzheimer's disease

> A progressive neurodegenerative disorder characterized by amyloid-β plaques, neurofibrillary tau tangles, and cognitive decline. Strong genetic risk from rare familial mutations (APP, PSEN1/2) and common variants (APOE, CLU, PICALM, BIN1), but most sporadic cases lack a clear single genetic cause.

> [!abstract] 한눈에
> 알츠하이머병은 amyloid-β plaque와 tau tangle을 특징으로 하는 진행성 신경퇴행 질환이며, 유전 변이만으로는 위험의 일부만 설명된다. 그래서 세포 유형별 somatic mosaicism과 microglia enhancer 같은 세포 유형 특이적 조절 영역이 추가 설명으로 연구되고 있다 ([[10-Summaries/kousi-2022-ad-mosaicism|Kousi 2022]]; [[10-Summaries/liu-2024-snaphic-g|SnapHiC-G]]).

## Definition

AD is the most common form of dementia. ~5% of cases are early-onset familial; the rest are late-onset and multifactorial.

## Why it matters

- Inherited variants explain only a fraction of AD risk. Cell-type-specific somatic mosaicism is an emerging hypothesis for additional risk ([[10-Summaries/kousi-2022-ad-mosaicism|Kousi 2022]]).
- ROSMAP cohort provides multi-omic AD brain data (RNA, DNA, ATAC, methylation) at single-cell resolution.

## Evidence and examples

**Somatic mutation**

- Kousi et al. 2022 reports cell-type-specific somatic mutational burden in Alzheimer's dementia ([[10-Summaries/kousi-2022-ad-mosaicism|Kousi 2022]]).
- Cumulative somatic SNV burden in neurons increases with age and correlates with neurodegeneration (Lodato et al. 2018; reviewed in [[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto 2022]]).

**Regulatory architecture**

- AD SNP heritability is most strongly enriched in microglia-specific enhancer–promoter target regions called by SnapHiC-G from sn-m3C-seq (S-LDSC P = 1.07 × 10⁻⁶) ([[10-Summaries/liu-2024-snaphic-g|SnapHiC-G]]).
- An AD variant (rs1880949) is linked to the microglia-expressed gene ARPC1B ([[10-Summaries/liu-2024-snaphic-g|SnapHiC-G]]).

## Open questions

- The Kousi et al. 2022 source is a preprint and only its reference list is clipped, so its AD-vs-control specifics are unverified ([[10-Summaries/kousi-2022-ad-mosaicism|Kousi 2022]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/post-zygotic-variation|Post-zygotic variation]] — Genetic changes acquired after fertilization.
> - `entity` [[20-Entities/manolis-kellis|Manolis Kellis]] — Computational biologist behind ROSMAP-scale aging and neurodegeneration genomics.
> - `entity` [[20-Entities/li-huei-tsai|Li-Huei Tsai]] — Picower Institute director working on Alzheimer's disease and neurodegeneration.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one body.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto & Walsh 2022]]
> - [[10-Summaries/kousi-2022-ad-mosaicism|Kousi 2022]]
> - [[10-Summaries/liu-2024-snaphic-g|Liu 2024]]
