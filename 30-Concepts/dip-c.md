---
type: concept
title: Dip-C
aliases: [diploid Hi-C]
tags: [3D-genome, single-cell, Hi-C, haplotype-phasing]
created: 2026-05-12
updated: 2026-05-12
---

# Dip-C

> A single-cell Hi-C variant that reconstructs **diploid** 3D structures by leveraging heterozygous SNVs to distinguish paternal from maternal contacts within the same cell.

## Definition

Standard sc-Hi-C protocol combined with phased SNV calling. Each contact is assigned to one of the two parental chromosomes when it spans a phased SNV.

## Why it matters

Reveals allele-specific 3D architecture — important for genomic imprinting, X-inactivation in females, and allele-specific expression mechanisms.

## Related

- [[30-Concepts/single-cell-hi-c]] · [[40-Topics/3d-genome]] · [[40-Topics/3d-genome]]
