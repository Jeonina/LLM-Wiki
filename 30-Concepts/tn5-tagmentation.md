---
type: concept
title: Tn5 tagmentation
aliases: [Tn5 transposition, tagmentation]
tags: [transposase, library-prep, ATAC-seq]
created: 2026-05-12
updated: 2026-05-12
---

# Tn5 tagmentation

> The simultaneous fragmentation and adapter-ligation of DNA by Tn5 transposase. A hyperactive Tn5 variant loaded with sequencing adapter–containing oligos cuts dsDNA and inserts the adapters in a single enzymatic reaction.

## Definition

Tn5 is an Escherichia coli transposase. Each transposition introduces a 9-nt gap into the target DNA and inserts the loaded adapter at both ends of the resulting fragment. Library prep that takes hours of fragmentation + ligation in conventional workflows takes ~30 minutes with Tn5.

## Why it matters

- Foundation of ATAC-seq (preferentially cuts open chromatin) and many low-input methods.
- Single-cell adaptable: pA-Tn5 enables CUT&Tag; concentration tuning enables size control in SMRT-Tag.
- Limitation: invariant transposon mosaic-end sequence is incompatible with [[40-Topics/duplex-sequencing]] strand discrimination.

## Examples

- [[30-Concepts/atac-seq]], [[30-Concepts/cut-and-tag]], [[30-Concepts/smrt-tag]], [[30-Concepts/scicut-tag]], [[30-Concepts/micro-atac-seq]], [[30-Concepts/splicool-seq]].

## Related

- [[30-Concepts/atac-seq]] · [[30-Concepts/cut-and-tag]] · [[30-Concepts/smrt-tag]]
