---
type: concept
title: Viral mimicry
aliases: [retrotransposon-induced viral mimicry, ERV mimicry]
tags: [methylation, retrotransposon, immune-response, HMA, cancer]
created: 2026-05-12
updated: 2026-10-12
---

# Viral mimicry

> A cellular state in which **endogenous retrotransposons** (LINE-1, SINE, ERVs) are transcribed in dsRNA-forming or chimeric configurations that trigger a type-I interferon innate immune response — as if the cell were infected by a virus. Induced by DNA methylation loss (hypomethylating agents, TET activity).

> [!abstract] 한눈에
> Viral mimicry는 methylation이 빠진 retrotransposon이 전사되어 dsRNA를 만들고, 세포가 바이러스에 감염된 것처럼 type-I interferon 반응을 일으키는 상태다. decitabine을 처리한 AML 세포 중 일부만 여러 TE family를 함께 올리며, 이 세포들은 global methylation만으로는 구별되지 않는다 ([[10-Summaries/hunt-2022-sctem-seq|Hunt 2022]]).

## Definition

When DNA methylation is lost at retrotransposon sequences, RNA polymerase II reads through them. The resulting transcripts form dsRNA, which is sensed by MDA5/RIG-I and triggers IFN-β/IFN-α signaling. The pathway is therapeutically exploited by hypomethylating agents (azacitidine, decitabine) in AML and MDS.

## Why it matters

- Mechanism of action of [[30-Concepts/decitabine]] and azacitidine in AML/MDS.
- Therapeutic axis for cold-tumor sensitization to immune checkpoint inhibitors.
- Cell-to-cell heterogeneity in viral mimicry response may predict clinical response to HMAs.

## Examples

- [[10-Summaries/hunt-2022-sctem-seq|Hunt 2022]] shows that a subgroup of decitabine-treated AML cells coordinately upregulates many TE families — and these cells are **indistinguishable by global methylation alone**, implying other factors (e.g., SETDB1, TF availability) gate the response.

## Related

> [!cards]
> - `concept` [[30-Concepts/transposable-elements|Transposable elements]] — Mobile DNA sequences, ~50% of the human genome, normally silenced by methylation.
> - `concept` [[30-Concepts/decitabine|Decitabine]] — Cytidine analog that traps DNMT1 and causes genome-wide methylation loss.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC at CpG dinucleotides, its maintenance, and how it is measured.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/hunt-2022-sctem-seq|Hunt 2022]]
