---
type: concept
title: Duplex sequencing
aliases: [duplex consensus sequencing, single-molecule duplex sequencing]
tags: [single-molecule, error-correction, low-VAF, method]
created: 2026-05-11
updated: 2026-05-11
---

# Duplex sequencing

> Single-molecule sequencing strategy that independently sequences both the Watson and Crick strands of each DNA fragment and requires consensus between them to call a variant. Drops the false-positive error rate to ≤10⁻⁸ — orders of magnitude below standard sequencing — by exploiting the fact that polymerase and sequencing errors are present on only one strand, while true mutations are present on both.

## Definition

Standard sequencing reads one strand of a DNA fragment; sequencing/polymerase errors and ssDNA damage are indistinguishable from true variants. Duplex sequencing tags both strands of each original DNA molecule so that the strand identity is preserved through library preparation and sequencing. Only variants observed in **both Watson and Crick strands** of the same molecule are called as true ([[10-Summaries/diane-2025-naturereviewsgenetics]]).

Single-strand errors are filtered. Single-strand DNA damage — of which a typical cell experiences ~70,000 lesions per day — is filtered. The error floor approaches the probability of the polymerase making the *exact same* error on both strands of the same molecule (≤10⁻⁸).

## Variants and refinements

Four implementation strategies ([[10-Summaries/diane-2025-naturereviewsgenetics]] Fig 3a):

- **Y-adaptor based** — BotSeqS, NanoSeq. Asymmetric Y-shaped adapter with distinct strand barcodes; bottleneck dilution required.
- **Tn5-based** — [[meta-cs]] is the only single-cell-compatible variant; Tn5 inserts adapters with orientation distinguishing the two strands.
- **Quadruplex adaptor** — CODEC. Adapter physically concatenates both strands so they appear in the same read.
- **Circularized sequencing** — HiDEF-seq (PacBio HiFi, error rate ~7 × 10⁻¹⁶), SMM-seq (Illumina rolling-circle).

## Why it matters

Duplex sequencing redefines the **fidelity** floor of variant detection ([[10-Summaries/gilad-2021-annualreviewofgenomicsandhumangenetics]]). Without it, the false-positive rate at low VAFs is dominated by ssDNA damage; with it, true variants at <1% VAF become detectable.

Most duplex methods sequence **bulk DNA** at single-molecule resolution — they capture the full mutational landscape but cannot assign variants to specific cells. [[meta-cs]] is the exception and the bridge to per-cell duplex resolution.

[[10-Summaries/elliott-2025-naturebiotechnology]] (DAF-seq) achieves an analogous fidelity gain by a different route — using deamination patterns as per-molecule UMIs that allow consensus-read assembly.

## Contested points

- Trade-off: duplex sequencing requires twice the read depth per molecule and complex library prep — cost per variant detected is high.
- Whether single-molecule long-read direct sequencing (PacBio HiFi without amplification, ONT) will displace duplex sequencing as long-read accuracy improves.

## Examples

- NanoSeq detection of somatic SNVs across normal human tissues at error rate <5 × 10⁻⁹ ([[10-Summaries/diane-2025-naturereviewsgenetics]]).
- HiDEF-seq on PacBio reaching ~7 × 10⁻¹⁶ error rate from concatenated Watson-Crick reads.
- [[meta-cs]] applied to single cells — bridging duplex and scDNA-seq.

## Related

- [[scdna-seq]]
- [[meta-cs]] — single-cell-compatible duplex method.
- [[scdna-capabilities-framework]] — fidelity capability.
- [[40-Topics/scdna-seq]]
