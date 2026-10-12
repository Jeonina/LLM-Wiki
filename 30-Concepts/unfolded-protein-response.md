---
type: concept
title: Unfolded protein response (UPR)
aliases: [UPR, ER stress response]
tags: [cell-biology, ER-stress, stress-response]
created: 2026-05-07
updated: 2026-10-12
---

# Unfolded protein response (UPR)

> A homeostatic ER stress response, signaled through three transmembrane sensors — PERK, IRE1, and ATF6 — that re-balances protein folding capacity, halts general translation, and (depending on the branch) promotes either survival or apoptosis.

> [!abstract] 한눈에
> UPR은 ER에 잘못 접힌 단백질이 쌓일 때 PERK, IRE1, ATF6 세 센서를 통해 켜지는 스트레스 반응이며, 어느 가지가 켜지느냐에 따라 세포는 살아남거나 apoptosis로 간다. CALR 돌연변이 세포는 progenitor 종류에 따라 다른 가지를 쓰고, MkP에서는 생존 쪽인 IRE1-XBP1과 ATF6가 우세하다 ([[10-Summaries/nam-2019-got|Nam 2019]]).

## Definition

When unfolded/misfolded proteins accumulate in the ER lumen, BiP (HSPA5) releases the three sensors, which signal through:

- **PERK** — phosphorylates eIF2α, halting general translation and selectively translating ATF4. Pro-apoptotic when sustained; protective for the HSC pool under generic ER stress.
- **IRE1** — endoribonuclease that performs unconventional splicing of XBP1u → XBP1s (the active TF). Pro-survival, especially in committed progenitors; its targets are characterized by XBP1 splicing assays.
- **ATF6** — Golgi-cleaved to release a TF that drives chaperone gene expression (HSPA5/BiP, HSP90B1, HSPD1, HSP90AA1).

## Why it matters

- In hematopoiesis, the UPR's three branches are differentially deployed: PERK dominates in HSPCs (eliminating ER-stressed cells from the stem pool), IRE1-XBP1 dominates in committed progenitors (promoting survival under stress).
- **CALR mutation — which breaks the chaperone activity of CALR — induces UPR in mutant cells, but the branch deployed depends on the progenitor type** ([[10-Summaries/nam-2019-got|Nam 2019]]).
- The cell-identity dependence of UPR branching is the load-bearing observation. It explains why CALR-mutant cells survive and proliferate rather than apoptose: they activate the survival arm (IRE1/ATF6), not the apoptotic arm (PERK) ([[10-Summaries/nam-2019-got|Nam 2019]]).

## Branch use by cell type

| Cell state | Branch deployed | Note | Source |
|---|---|---|---|
| HSPCs, generic ER stress | PERK | Eliminates ER-stressed cells from the stem pool | — |
| Committed progenitors, generic ER stress | IRE1-XBP1 | Promotes survival under stress | — |
| CALR-mutant MkPs | Strong IRE1-XBP1 splicing and ATF6 chaperone induction; PERK *not* enhanced | The IRE1/ATF6 dominance is the survival/proliferative arm | ([[10-Summaries/nam-2019-got\|Nam 2019]]) |
| CALR-mutant HSPCs | XBP1 itself is upregulated; IRE1 splicing is also active | Less PERK-biased than expected for HSPCs under generic ER stress | ([[10-Summaries/nam-2019-got\|Nam 2019]]) |
| CALR-mutated MF MkPs | IRE1-mediated UPR | Persists into myelofibrosis | ([[10-Summaries/nam-2019-got\|Nam 2019]]) |

## Evidence and examples

- CALR-mutant MkPs in ET show ATF6-mediated chaperone induction (HSPA5, HSP90B1, HSPD1) and IRE1-XBP1 splicing without PERK enhancement ([[10-Summaries/nam-2019-got|Nam 2019]]).
- IRE1-mediated UPR persists into CALR-mutated MF MkPs ([[10-Summaries/nam-2019-got|Nam 2019]]).
- GoT was further extended to genotype the **XBP1 splice site itself** in single cells, validating IRE1 activity in mutant MkPs and HSPCs in vivo ([[10-Summaries/nam-2019-got|Nam 2019]]).

## Contested points

- IRE1-XBP1 is proposed as a therapeutic target for eradicating mutant HSPCs ([[10-Summaries/nam-2019-got|Nam 2019]]). Therapeutic validation in patients is not yet in the wiki.
- Whether IRE1/ATF6 dominance (rather than PERK) is causal for clonal expansion or merely correlative is not directly tested.

## Related

> [!cards]
> - `concept` [[30-Concepts/calr-mutation|CALR mutation]] — MPN driver in calreticulin whose UPR output depends on progenitor identity.
> - `concept` [[30-Concepts/got|GoT]] — Links somatic genotype to the single-cell transcriptome from 10x cDNA.
> - `concept` [[30-Concepts/hematopoietic-differentiation|Hematopoietic differentiation]] — The HSC-to-mature-cell hierarchy used as the reference scaffold.
> - `hub` [[40-Topics/hematopoietic-malignancies|Hematopoietic malignancies]] — Cancers and pre-cancerous clonal expansions from hematopoietic stem and progenitor cells.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/nam-2019-got|Nam 2019]]
