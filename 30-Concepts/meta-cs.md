---
type: concept
title: META-CS (Multiplexed End-Tagging Amplification of Complementary Strands)
aliases: [METACS]
tags: [scWGA, Tn5, duplex, single-cell, method]
created: 2026-05-11
updated: 2026-05-11
---

# META-CS (Multiplexed End-Tagging Amplification of Complementary Strands)

> The only [[duplex-sequencing]] method that can be applied to **single cells** rather than bulk DNA. Uses Tn5 transposase to insert sequencing adapters into DNA in a way that the adapter orientation distinguishes the two complementary strands — combining the per-cell resolution of scWGA with the per-base accuracy of duplex sequencing.

## Definition

META-CS performs Tn5-based tagmentation of single-cell DNA (or single nuclei), with adapters configured so that the **orientation of insertion** differentiates the two complementary DNA strands ([[10-Summaries/diane-2025-naturereviewsgenetics]]). After amplification and sequencing, reads from each strand can be separated by adapter orientation, and variant calls require consensus between strands.

Because Tn5 inserts adapters directly without an end-repair / A-tailing step, META-CS avoids a class of errors that arise from those processes in Y-adaptor duplex methods. Estimated error rate: <2.4 × 10⁻⁸.

## Why it matters

META-CS bridges the long-standing gap between [[scwga]]-based scDNA-seq (per-cell, but high false-positive rate) and bulk [[duplex-sequencing]] (low false-positive rate, but no per-cell assignment). It is the only method that gives single-cell genotypes at near-duplex error rates.

In the [[gilad-2021-annualreviewofgenomicsandhumangenetics|Evrony capabilities framework]], META-CS uniquely combines **fidelity** (duplex error correction) and **co-presence** (per-cell assignment) at genome-wide scale.

## Variants and refinements

- Family-related: LIANTI and DLP+ are also Tn5-based scWGA but without strand-pairing duplex correction.
- Currently the only single-cell duplex method; new short-read platforms (Ultima Genomics) may add native duplex capability without specialized chemistry.

## Contested points

- Higher cost per cell than non-duplex scWGA — duplex sequencing requires twice the read depth per molecule plus complex library prep.
- Tn5 tagmentation biases limit coverage compared to MDA/PTA.

## Examples

- Single-cell SNV detection with error rate <2.4 × 10⁻⁸, applied across normal tissues ([[10-Summaries/diane-2025-naturereviewsgenetics]]).

## Related

- [[scwga]]
- [[duplex-sequencing]]
- [[scdna-seq]]
- [[dlp-plus]] — Tn5-based sibling without duplex correction.
- [[scdna-capabilities-framework]]
