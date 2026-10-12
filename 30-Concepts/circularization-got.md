---
type: concept
title: Circularization GoT
aliases: [circ-GoT]
tags: [single-cell, scRNA-seq, genotyping, method]
created: 2026-05-07
updated: 2026-10-12
---

# Circularization GoT

> Extension of [[got]] for genotyping mutations located far (≥ 1.5 kb) from a transcript end, using sequential rounds of intramolecular ligation and inverse PCR to shrink the amplicon to a length compatible with short-read Illumina sequencing while preserving the cell barcode ([[10-Summaries/nam-2019-got|Nam 2019]]).

> [!abstract] 한눈에
> Circularization GoT는 전사체 끝에서 멀리 떨어진 돌연변이를 GoT로 genotyping하기 위해 분자 내 ligation과 inverse PCR을 반복해 amplicon을 짧게 줄이는 방법이고, JAK2 V617F를 이렇게 읽었다 ([[10-Summaries/nam-2019-got|Nam 2019]]). 다만 우회책에 가까워서, gDNA에서 locus를 직접 잡는 GoT-ChA가 나온 뒤로는 필요가 없어졌다 ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Definition

Standard GoT amplifies from a gene-specific primer at the mutation locus to the 3′ end of the 10x library fragment, retaining the cell barcode and UMI ([[10-Summaries/nam-2019-got|Nam 2019]]). For mutations far from transcript ends the resulting amplicon is too long to cluster efficiently on Illumina flow cells ([[10-Summaries/nam-2019-got|Nam 2019]]). The method was introduced by [[20-Entities/anna-s-nam]] and colleagues in the [[20-Entities/landau-lab]] ([[10-Summaries/nam-2019-got|Nam 2019]]).

## Why it matters

Circularization GoT genotyped JAK2 V617F at ~2.3 kb from the closer transcript end, a target unreachable with linear GoT ([[10-Summaries/nam-2019-got|Nam 2019]]). It is, however, a workaround: each circularization step adds wet-lab complexity and reduces yield (synthesis). The cleaner architectural fix — capture the locus from genomic DNA instead of cDNA — arrives with [[got-cha]], which obviates circularization entirely ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Protocol

Circularization GoT performs ([[10-Summaries/nam-2019-got|Nam 2019]]):

1. Hemi-nested gene-specific PCR to define cloning-compatible ends around the region of interest.
2. **Intramolecular ligation + inverse PCR** to remove the intervening sequence between the cell barcode and the mutation site.
3. A second round of circularization + inverse PCR.
4. Final library indexing and short-read sequencing.

## Evidence and examples

- JAK2 V617F (~2.3 kb from the transcript 3′ end) was genotyped via circularization GoT ([[10-Summaries/nam-2019-got|Nam 2019]]).
- The method was validated against Oxford Nanopore long-read sequencing (GridION X5) of un-circularized GoT amplicons, confirming low intra- and inter-transcript PCR recombination ([[10-Summaries/nam-2019-got|Nam 2019]]).
- It was used both for a common driver (JAK2 V617F) and in a mixing study with TF-1 / HEL cell lines ([[10-Summaries/nam-2019-got|Nam 2019]]).

## Contested points

- The yield improvement is real but limited compared with gDNA-based approaches; circularization GoT is now largely of historical methodological interest (synthesis), since GoT-ChA removes the transcript-distance limitation that motivated it ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/got|GoT]] — Base method: genotyping of transcriptomes in single cells.
> - `concept` [[30-Concepts/got-cha|GoT-ChA]] — gDNA-based successor that removes the need for circularization.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
