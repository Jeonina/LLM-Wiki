---
type: concept
title: CODEC
aliases: [Concatenating Original Duplex for Error Correction]
tags: [duplex-sequencing, library-prep, low-input]
created: 2026-05-12
updated: 2026-05-12
---

# CODEC

> Concatenating Original Duplex for Error Correction — a duplex-sequencing chemistry developed at the Broad Institute (V. Adalsteinsson) that concatenates both strands of a DNA molecule into one read, allowing per-molecule error correction in standard short-read sequencing.

## Definition

CODEC fuses the two strands of a duplex into a contiguous sequenced fragment, enabling strand-consensus calling from a single read pair. One of the methods evaluated by the SMaHT duplex benchmark.

## Why it matters

Lower-cost duplex chemistry; benchmark-comparable accuracy to NanoSeq and HiDEF-seq.

## Examples

- One of six methods compared in [[10-Summaries/zhang-2025-smaht-duplex-benchmark]].

## Related

- [[30-Concepts/duplex-sequencing]] · [[30-Concepts/nanoseq]] · [[30-Concepts/hidef-seq]] · [[40-Topics/duplex-sequencing]]
