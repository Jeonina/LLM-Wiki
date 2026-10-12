---
type: concept
title: Dip-C
aliases: [diploid Hi-C]
tags: [3D-genome, single-cell, Hi-C, haplotype-phasing]
created: 2026-05-12
updated: 2026-10-12
---

# Dip-C

> A single-cell Hi-C variant that reconstructs **diploid** 3D structures by leveraging heterozygous SNVs to distinguish paternal from maternal contacts within the same cell.

> [!abstract] 한눈에
> Dip-C는 heterozygous SNV로 부계와 모계 contact를 구분해 한 세포의 diploid 3D 구조를 재구성하는 single-cell Hi-C 변형이다. 짧은 read로는 직접 phasing되는 조각이 9%에 그쳐, long-read인 scNanoHi-C는 같은 Dip-C/hickit 도구로 25%까지 끌어올렸다 ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).

## Definition

Standard sc-Hi-C protocol combined with phased SNV calling. Each contact is assigned to one of the two parental chromosomes when it spans a phased SNV.

## Why it matters

Reveals allele-specific 3D architecture — important for genomic imprinting, X-inactivation in females, and allele-specific expression mechanisms.

## Evidence and examples

- Long reads raise single-cell phasing: scNanoHi-C monomers average 610 bp (short-read scHi-C ≤150 bp), and 25% of monomers are directly phasable versus 9% in Dip-C. scNanoHi-C reuses Dip-C/hickit to build haplotype-resolved 20-kb models that capture X inactivation ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).
- BandNorm-normalized Dip-C data from postnatal mouse forebrain (Tan2021, 100 kb) separated cell types in agreement with matched MALBAC-DT transcriptomes. Single-cell gene-associating-domain (scGAD) scores computed on these maps recovered transcriptome-defined marker genes ([[10-Summaries/zheng-2022-bandnorm-scvi-3d|BandNorm]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — The family of methods that profile genome-wide chromatin contacts in single cells.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromosome territories, compartments, TADs and loops inside the nucleus.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/li-2023-scnanohi-c|Li 2023]]
> - [[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]
