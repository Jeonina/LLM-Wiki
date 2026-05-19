---
type: concept
title: PacBio
aliases: [Pacific Biosciences, SMRT sequencing]
tags: [long-read, sequencing, HiFi, methylation]
created: 2026-05-12
updated: 2026-05-12
---

# PacBio (Pacific Biosciences) SMRT sequencing

> A long-read sequencing platform based on **single-molecule real-time (SMRT)** observation of DNA polymerase incorporating fluorescent nucleotides into a single template held in a zero-mode waveguide (ZMW). Circular consensus sequencing (CCS) reads multiple passes of the same circularized molecule and consensus-calls for high accuracy.

## Definition

PacBio Sequel II/IIe/Revio instruments. **HiFi reads**: ≥5 CCS passes yields >99% per-read accuracy. Read length 5–20 kb. Cost has dropped from $2,000 to $35 per Gb. Kinetic signatures (interpulse distance, pulse width) detect 5mC and 6mA without separate library prep.

## Why it matters

- Direct methylation detection via kinetic analysis (Primrose for 5mC, Fibertools for 6mA).
- PCR-free workflows preserve native modifications.
- High accuracy plus long reads make PacBio HiFi the de facto standard for clinical-grade variant calling and genome assembly.

## Examples

- [[10-Summaries/elliott-2025-naturebiotechnology]] (DAF-seq / scDAF-seq).
- [[10-Summaries/abdulhay-2020-samosa]] (SMRT-Tag / SAMOSA-Tag).
- [[10-Summaries/profiling-the-epigenome-using-long-read-sequencing]] reviews PacBio epigenomics.

## Related

- [[30-Concepts/long-read-sequencing]] · [[30-Concepts/oxford-nanopore]] · [[30-Concepts/single-molecule-footprinting]] · [[40-Topics/long-read-sequencing]]
