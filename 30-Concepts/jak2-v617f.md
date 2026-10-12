---
type: concept
title: JAK2 V617F
aliases: [JAK2V617F, JAK2 V617]
tags: [hematology, MPN, driver-mutation, kinase]
created: 2026-05-07
updated: 2026-10-12
---

# JAK2 V617F

> Recurrent valine-to-phenylalanine point mutation at codon 617 of the Janus kinase 2 (JAK2) gene; the most common driver of [[myeloproliferative-neoplasm]] and a precursor lesion in clonal hematopoiesis, which constitutively activates JAK2 → STAT signaling in a cytokine-independent manner ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).

> [!abstract] 한눈에
> JAK2 V617F는 cytokine 없이도 JAK2–STAT 신호를 켜는 점돌연변이로, MPN의 가장 흔한 driver다 ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]). GoT–ChA는 돌연변이 HSC가 염증성 chromatin priming을 세포 내재적으로 갖는다는 것을 보였고, 이것이 clonal expansion의 원인인지 결과인지는 아직 열려 있다 ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [클론성 조혈 교재](../60-Explainers/clonal-hematopoiesis.html)
>
> [혈액암 교재](../60-Explainers/hematopoietic-malignancies.html)
<!-- /explainer-links -->

## Definition

JAK2 normally requires cytokine receptor engagement (EPO, TPO, G-CSF, etc.) to signal. The V617F mutation in the JH2 pseudokinase domain releases the kinase's auto-inhibition, producing constitutive activation and downstream phosphorylation of STAT3, STAT5, and STAT1 ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).

## Why it matters

JAK2V617F is found in:

- ~95% of polycythemia vera (PV) patients,
- ~50% of essential thrombocythemia (ET) and primary myelofibrosis (MF) patients,
- A substantial fraction of clonal-hematopoiesis-of-indeterminate-potential (CHIP) cases.

GoT–ChA reframes JAK2V617F's effect on HSCs from "downstream cytokine inflammation" to **cell-intrinsic chromatin priming** ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).

## Chromatin effects in mutant HSCs

Mutant HSCs in MF show these accessibility changes ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]):

| Program | Example genes or motifs | Direction | Source |
|---|---|---|---|
| NF-κB targets | TRAPPC9 | Increased | ([[10-Summaries/izzo-2024-got-cha\|GoT–ChA]]) |
| TGF-β superfamily | BMPR1B receptor, GDF10 ligand | Increased | ([[10-Summaries/izzo-2024-got-cha\|GoT–ChA]]) |
| Matrix remodeling | MMP15 | Increased | ([[10-Summaries/izzo-2024-got-cha\|GoT–ChA]]) |
| Stem/quiescence genes | FRY, HLF, PBX1 | Decreased | ([[10-Summaries/izzo-2024-got-cha\|GoT–ChA]]) |
| STAT motifs | STAT1/5 | Increased; reversed by ruxolitinib | ([[10-Summaries/izzo-2024-got-cha\|GoT–ChA]]) |

Only the canonical JAK2/STAT-target (STAT1/5) accessibility gain is already visible at the clonal-hematopoiesis stage, *before* overt MPN; the NF-κB/TGF-β program appears only in MF, not in the CH sample ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).

## Variants and refinements

- **Heterozygous JAK2V617F** — common; modest pro-inflammatory phenotype.
- **Homozygous JAK2V617F** — typically arises from copy-neutral loss of heterozygosity (UPD on chr 9p); more severe phenotype, NFKB1 and REL motifs specifically increased ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).
- In a 123-patient AML Tapestri cohort, all *JAK2* V617F samples also carried CNLOH of *JAK2*, often in a very small subclone — a distinction bulk VAF cannot make (5% homozygous vs 10% heterozygous cells) ([[10-Summaries/sollier-2023-compass|COMPASS]]).
- Pharmacologic targeting: ruxolitinib (JAK1/2 inhibitor) suppresses cytokine signaling and chromatin TF motif differences but **does not eliminate the mutated clone** ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).

## Evidence and examples

- 21 JAK2V617F MPN samples (150,643 cells) were profiled with [[got-cha]], at a 38.1% genotyping rate, and cell-intrinsic chromatin priming was visible at clonal hematopoiesis ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).
- Mutant cells preferentially distribute into erythroid–megakaryocytic and granulocyte–monocyte progenitors; lymphoid clusters remain ~92% wild-type.

## Contested points

- Whether the cell-intrinsic pro-inflammatory chromatin program is *causal* for clonal expansion or *consequential* is open: the longitudinal Pt-01 PV→MF data point to early causality ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]), but cohort-scale evidence is limited (synthesis).
- The mechanism connecting JAK2V617F kinase activity to chromatin remodeling at NF-κB and TGF-β loci is not nailed down (STAT-mediated? direct? pioneer factor recruitment?) ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/calr-mutation|CALR mutation]] — Sister MPN driver; converges on JAK-STAT activation.
> - `concept` [[30-Concepts/myeloproliferative-neoplasm|Myeloproliferative neoplasm]] — Disease context from CH through PV to MF.
> - `concept` [[30-Concepts/got-cha|GoT–ChA]] — Genotyping with single-cell chromatin accessibility, used to split mutant and wild-type cells.
> - `concept` [[30-Concepts/hematopoietic-differentiation|Hematopoietic differentiation]] — The progenitor hierarchy mutant cells skew toward myeloid fates.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — The readout that shows the mutant HSC priming.
> - `hub` [[40-Topics/hematopoietic-malignancies|Hematopoietic malignancies]] — Blood cancers and their clonal precursors.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/sollier-2023-compass|Sollier 2023]]
