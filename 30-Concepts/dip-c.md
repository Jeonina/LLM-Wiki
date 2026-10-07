---
type: concept
title: Dip-C
aliases: [diploid Hi-C]
tags: [3D-genome, single-cell, Hi-C, haplotype-phasing]
created: 2026-05-12
updated: 2026-10-07
---

# Dip-C

> A single-cell Hi-C variant that reconstructs **diploid** 3D structures by leveraging heterozygous SNVs to distinguish paternal from maternal contacts within the same cell.

## Definition

Standard sc-Hi-C protocol combined with phased SNV calling. Each contact is assigned to one of the two parental chromosomes when it spans a phased SNV.

## Why it matters

Reveals allele-specific 3D architecture — important for genomic imprinting, X-inactivation in females, and allele-specific expression mechanisms.

## Added 2026-10-07

Long reads raise single-cell phasing: scNanoHi-C monomers average 610 bp (short-read scHi-C ≤150 bp), and 25% of monomers are directly phasable versus 9% in Dip-C. scNanoHi-C reuses Dip-C/hickit to build haplotype-resolved 20-kb models that capture X inactivation ([[10-Summaries/li-2023-scnanohi-c]]).

BandNorm-normalized Dip-C data from postnatal mouse forebrain (Tan2021, 100 kb) separated cell types in agreement with matched MALBAC-DT transcriptomes. Single-cell gene-associating-domain (scGAD) scores computed on these maps recovered transcriptome-defined marker genes ([[10-Summaries/zheng-2022-bandnorm-scvi-3d]]).


## Related

- [[30-Concepts/single-cell-hi-c]] · [[40-Topics/3d-genome]]
