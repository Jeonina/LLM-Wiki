---
type: concept
title: Unfolded protein response (UPR)
aliases: [UPR, ER stress response]
tags: [cell-biology, ER-stress, stress-response]
created: 2026-05-07
updated: 2026-05-07
---

# Unfolded protein response (UPR)

> A homeostatic ER stress response, signaled through three transmembrane sensors — PERK, IRE1, and ATF6 — that re-balances protein folding capacity, halts general translation, and (depending on the branch) promotes either survival or apoptosis.

## Definition

When unfolded/misfolded proteins accumulate in the ER lumen, BiP (HSPA5) releases the three sensors, which signal through:

- **PERK** — phosphorylates eIF2α, halting general translation and selectively translating ATF4. Pro-apoptotic when sustained.
- **IRE1** — endoribonuclease that performs unconventional splicing of XBP1u → XBP1s (the active TF). Pro-survival, especially in committed progenitors.
- **ATF6** — Golgi-cleaved to release a TF that drives chaperone gene expression (HSPA5, HSP90B1, etc.).

## Why it matters

In hematopoiesis, the UPR's three branches are differentially deployed: PERK dominates in HSPCs (eliminating ER-stressed cells from the stem pool), IRE1-XBP1 dominates in committed progenitors (promoting survival under stress).

[[10-Summaries/anna-2019-nature]] shows that **CALR mutation — which breaks the chaperone activity of CALR — induces UPR in mutant cells, but the branch deployed depends on the progenitor type**:

- **MkPs**: strong IRE1-XBP1 splicing and ATF6 chaperone induction; PERK *not* enhanced. The IRE1/ATF6 dominance is the survival/proliferative arm.
- **HSPCs**: XBP1 itself is upregulated; IRE1 splicing is also active; the response is less PERK-biased than expected for HSPCs under generic ER stress.

The cell-identity dependence of UPR branching is the load-bearing observation. It explains why CALR-mutant cells survive and proliferate rather than apoptose: they activate the survival arm (IRE1/ATF6), not the apoptotic arm (PERK).

## Variants and refinements

- **PERK arm** — pro-apoptotic; protective for the HSC pool under generic ER stress.
- **IRE1-XBP1 arm** — pro-survival; targets characterized by XBP1 splicing assays.
- **ATF6 arm** — chaperone induction (HSPA5/BiP, HSP90B1, HSPD1, HSP90AA1).

[[10-Summaries/anna-2019-nature]] further extended GoT to genotype the **XBP1 splice site itself** in single cells, validating IRE1 activity in mutant MkPs and HSPCs in vivo.

## Contested points

- IRE1-XBP1 is proposed as a therapeutic target for eradicating mutant HSPCs ([[10-Summaries/anna-2019-nature]]). Therapeutic validation in patients is not yet in the wiki.
- Whether IRE1/ATF6 dominance (rather than PERK) is causal for clonal expansion or merely correlative is not directly tested.

## Examples

- CALR-mutant MkPs in ET show ATF6-mediated chaperone induction (HSPA5, HSP90B1, HSPD1) and IRE1-XBP1 splicing without PERK enhancement ([[10-Summaries/anna-2019-nature]]).
- IRE1-mediated UPR persists into CALR-mutated MF MkPs ([[10-Summaries/anna-2019-nature]]).

## Related

- [[calr-mutation]]
- [[hematopoietic-differentiation]]
- [[got]]
- [[40-Topics/hematopoietic-malignancies]]
