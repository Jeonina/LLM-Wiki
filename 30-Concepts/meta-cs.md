---
type: concept
title: META-CS (Multiplexed End-Tagging Amplification of Complementary Strands)
aliases: [METACS]
tags: [scWGA, Tn5, duplex, single-cell, method]
created: 2026-05-11
updated: 2026-10-07
---

# META-CS (Multiplexed End-Tagging Amplification of Complementary Strands)

> The only [[40-Topics/duplex-sequencing]] method that can be applied to **single cells** rather than bulk DNA. Tags fragments with Tn5 carrying 2 of 16 transposon sequences, then melts them and runs two sequential primer-extension rounds that label the two complementary strands ([[10-Summaries/xing-2021-meta-cs]]) — combining the per-cell resolution of scWGA with the per-base accuracy of duplex sequencing.

## Definition

META-CS performs Tn5-based tagmentation of single-cell DNA (or single nuclei), followed by melting and two sequential primer-extension rounds that **label the two complementary strands** (the earlier review description in terms of insertion orientation is superseded by the primary paper, [[10-Summaries/xing-2021-meta-cs]]) ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). After amplification and sequencing, reads from each strand can be separated by adapter orientation, and variant calls require consensus between strands.

Because Tn5 inserts adapters directly without an end-repair / A-tailing step, META-CS avoids a class of errors that arise from those processes in Y-adaptor duplex methods. The false-positive rate has an upper bound of 2.4 × 10⁻⁸ (70 SNVs / 2.9 Gb in kindred eHAP cells); the authors say the true rate is likely much lower ([[10-Summaries/xing-2021-meta-cs]]).

## Why it matters

META-CS bridges the long-standing gap between [[scwga]]-based scDNA-seq (per-cell, but high false-positive rate) and bulk [[40-Topics/duplex-sequencing]] (low false-positive rate, but no per-cell assignment). It is the only method that gives single-cell genotypes at near-duplex error rates.

In the [[evrony-2021-scDNA-applications-review|Evrony capabilities framework]], META-CS would combine **fidelity** (duplex error correction) and **co-presence** (per-cell assignment) at genome-wide scale (synthesis; the Evrony review does not discuss META-CS).

## Variants and refinements

- Family-related: LIANTI and DLP+ are also Tn5-based scWGA but without strand-pairing duplex correction.
- Currently the only single-cell duplex method; new short-read platforms (Ultima Genomics) may add native duplex capability without specialized chemistry.

## Contested points

- Cost: general duplex methods need roughly twice the read depth per molecule (synthesis), but the META-CS paper reports *lower* sequencing cost, calling SNVs from ≥4 reads with most cells at 3–8× rather than the usual 30–60× ([[10-Summaries/xing-2021-meta-cs]]).
- Tn5 tagmentation biases limit coverage compared to MDA/PTA.

## Examples

- Tn5-based single-cell duplex SNV detection (the only duplex method applicable to single cells) ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Added 2026-10-07

**Reuse beyond SNV calling.** scDeChIC-seq builds its single-cell libraries on META-CS transposons, lysis buffer and strand-tagging with a U-tolerant polymerase to read deaminase-written C→U edits from one cell ([[10-Summaries/shi-2026-dechic-seq]]).

Primary source: META-CS tags fragments with 2 of 16 Tn5 transposon sequences. After melting, two sequential primer-extension rounds label the forward and reverse strands, all in one tube, and the strands are told apart by how they map to the reference. Strand labeling had a conversion rate of 2.3 × 10⁻⁵ ([[10-Summaries/xing-2021-meta-cs]]). The 2.4 × 10⁻⁸ figure is an upper bound on the false-positive rate (70 SNVs / 2.9 Gb in day-5 eHAP kindred cells), not a measured error rate ([[10-Summaries/xing-2021-meta-cs]]). Most cells were sequenced at 3–8×, compared with 30–60× typical for single-cell SNV calling, and about 90% of cells amplified successfully. Genome coverage was 50.9 ± 12.2% and strand-specific detection efficiency 15.9 ± 6.1% in eHAP cells ([[10-Summaries/xing-2021-meta-cs]]).


## Related

- [[scwga]]
- [[40-Topics/duplex-sequencing]]
- [[40-Topics/scdna-seq]]
- [[dlp-plus]] — Tn5-based sibling without duplex correction.
- [[scdna-capabilities-framework]]
