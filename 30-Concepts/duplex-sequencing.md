---
type: concept
title: Duplex sequencing
aliases: [duplex consensus sequencing, single-molecule duplex sequencing]
tags: [single-molecule, error-correction, low-VAF, method]
created: 2026-05-11
updated: 2026-05-19
---

# Duplex sequencing

> Single-molecule sequencing strategy that independently sequences both the Watson and Crick strands of each DNA fragment and requires consensus between them to call a variant ([[10-Summaries/schmitt-2012-pnas]]). Drops the false-positive error rate to ≤10⁻⁸ — orders of magnitude below standard sequencing ([[10-Summaries/schmitt-2012-pnas]]; [[10-Summaries/kennedy-2014-duplex-protocol]]) — by exploiting the fact that polymerase and sequencing errors are present on only one strand, while true mutations are present on both.

## Definition

Standard sequencing reads one strand of a DNA fragment; sequencing/polymerase errors and ssDNA damage are indistinguishable from true variants ([[10-Summaries/schmitt-2012-pnas]]). Duplex sequencing tags both strands of each original DNA molecule so that the strand identity is preserved through library preparation and sequencing. Only variants observed in **both Watson and Crick strands** of the same molecule are called as true ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]; [[10-Summaries/schmitt-2012-pnas]]).

Single-strand errors are filtered ([[10-Summaries/kennedy-2014-duplex-protocol]]). Single-strand DNA damage — of which a typical cell experiences ~70,000 lesions per day — is filtered ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). The error floor approaches the probability of the polymerase making the *exact same* error on both strands of the same molecule (≤10⁻⁸) ([[10-Summaries/schmitt-2012-pnas]]).

## Variants and refinements

Four implementation strategies ([[10-Summaries/shao-2025-scDNA-mosaicism-review]] Fig 3a):

- **Y-adaptor based** — BotSeqS, NanoSeq ([[10-Summaries/abascal-2021-nanoseq]]). Asymmetric Y-shaped adapter with distinct strand barcodes; bottleneck dilution required.
- **Tn5-based** — [[meta-cs]] is the only single-cell-compatible variant; Tn5 inserts adapters with orientation distinguishing the two strands ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- **Quadruplex adaptor** — CODEC ([[10-Summaries/bae-2023-codec]]). Adapter physically concatenates both strands so they appear in the same read.
- **Circularized sequencing** — HiDEF-seq (PacBio HiFi, error rate ~7 × 10⁻¹⁶) ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]), SMM-seq (Illumina rolling-circle) ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Why it matters

Duplex sequencing redefines the **fidelity** floor of variant detection ([[10-Summaries/evrony-2021-scDNA-applications-review]]). Without it, the false-positive rate at low VAFs is dominated by ssDNA damage; with it, true variants at <1% VAF become detectable ([[10-Summaries/kennedy-2014-duplex-protocol]]; [[10-Summaries/schmitt-2012-pnas]]).

Most duplex methods sequence **bulk DNA** at single-molecule resolution — they capture the full mutational landscape but cannot assign variants to specific cells ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). [[meta-cs]] is the exception and the bridge to per-cell duplex resolution ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). **Duplex-Multiome** further integrates duplex consensus into the 10x Multiome platform, achieving per-nucleus point-mutation + scATAC + scRNA ([[10-Summaries/kriz-2025-duplex-multiome]]).

[[10-Summaries/swanson-2025-daf-seq]] (DAF-seq) achieves an analogous fidelity gain by a different route — using deamination patterns as per-molecule UMIs that allow consensus-read assembly.

## Contested points

- Trade-off: duplex sequencing requires twice the read depth per molecule and complex library prep — cost per variant detected is high ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- Whether single-molecule long-read direct sequencing (PacBio HiFi without amplification, ONT) will displace duplex sequencing as long-read accuracy improves ([[10-Summaries/liu-2025-long-read-epigenome-review]]).
- Benchmarking heterogeneity: different duplex protocols disagree on mutation spectra at extreme low VAF ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]).

## Examples

- NanoSeq detection of somatic SNVs across normal human tissues at error rate <5 × 10⁻⁹ ([[10-Summaries/abascal-2021-nanoseq]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- HiDEF-seq on PacBio reaching ~7 × 10⁻¹⁶ error rate from concatenated Watson-Crick reads ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- CODEC: ligated-quadruplex single-read duplex resolution ([[10-Summaries/bae-2023-codec]]).
- [[meta-cs]] applied to single cells — bridging duplex and scDNA-seq ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- Duplex-Multiome: 51,400 nuclei from postmortem human brain with point mutations + chromatin + RNA per cell ([[10-Summaries/kriz-2025-duplex-multiome]]).
- Cardiovascular-tissue duplex toolbox catalog (TwinStrand, NanoSeq, BotSeqS, CODEC, Pro-Seq, META-CS) per [[10-Summaries/hilal-2026-cardiac-somatic-review]].

## Related

- [[30-Concepts/scdna-seq]]
- [[meta-cs]] — single-cell-compatible duplex method.
- [[scdna-capabilities-framework]] — fidelity capability.
- [[codec]] · [[nanoseq]]
- [[40-Topics/duplex-sequencing]]
- [[40-Topics/scdna-seq]]
