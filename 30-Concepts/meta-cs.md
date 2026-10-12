---
type: concept
title: META-CS (Multiplexed End-Tagging Amplification of Complementary Strands)
aliases: [METACS]
tags: [scWGA, Tn5, duplex, single-cell, method]
created: 2026-05-11
updated: 2026-10-12
---

# META-CS (Multiplexed End-Tagging Amplification of Complementary Strands)

> The only [[40-Topics/duplex-sequencing]] method that can be applied to **single cells** rather than bulk DNA. It tags fragments with Tn5 carrying 2 of 16 transposon sequences, then melts them and runs two sequential primer-extension rounds that label the two complementary strands — combining the per-cell resolution of scWGA with the per-base accuracy of duplex sequencing ([[10-Summaries/xing-2021-meta-cs|Xing 2021]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

> [!abstract] 한눈에
> META-CS는 Tn5로 단일 세포 DNA를 tagmentation한 뒤 두 상보 가닥을 따로 표지해, 두 가닥이 일치하는 변이만 부르는 single-cell duplex 방법이다 ([[10-Summaries/xing-2021-meta-cs|Xing 2021]]). 위양성률 상한은 2.4 × 10⁻⁸이고 대부분의 세포를 3–8×만 시퀀싱해도 SNV를 부를 수 있다 ([[10-Summaries/xing-2021-meta-cs|Xing 2021]]).

## Definition

META-CS performs Tn5-based tagmentation of single-cell DNA (or single nuclei), followed by melting and two sequential primer-extension rounds that **label the two complementary strands** ([[10-Summaries/xing-2021-meta-cs|Xing 2021]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). The earlier review description in terms of insertion orientation is superseded by the primary paper ([[10-Summaries/xing-2021-meta-cs|Xing 2021]]). After amplification and sequencing, reads from each strand can be separated by adapter orientation, and variant calls require consensus between strands.

Because Tn5 inserts adapters directly without an end-repair / A-tailing step, META-CS avoids a class of errors that arise from those processes in Y-adaptor duplex methods.

## Why it matters

- **It bridges per-cell and per-base accuracy.** META-CS bridges the long-standing gap between [[scwga]]-based scDNA-seq (per-cell, but high false-positive rate) and bulk [[40-Topics/duplex-sequencing]] (low false-positive rate, but no per-cell assignment); it is the only method that gives single-cell genotypes at near-duplex error rates ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **It fits two capabilities at once.** In the [[evrony-2021-scDNA-applications-review|Evrony capabilities framework]], META-CS would combine **fidelity** (duplex error correction) and **co-presence** (per-cell assignment) at genome-wide scale (synthesis; the Evrony review does not discuss META-CS).

## Protocol and performance

| Attribute | Value | Source |
|---|---|---|
| Transposons | 2 of 16 Tn5 transposon sequences per fragment | ([[10-Summaries/xing-2021-meta-cs\|Xing 2021]]) |
| Strand labelling | Two sequential primer-extension rounds after melting label the forward and reverse strands, all in one tube; strands are told apart by how they map to the reference | ([[10-Summaries/xing-2021-meta-cs\|Xing 2021]]) |
| Strand-labelling conversion rate | 2.3 × 10⁻⁵ | ([[10-Summaries/xing-2021-meta-cs\|Xing 2021]]) |
| False-positive rate | Upper bound 2.4 × 10⁻⁸ (70 SNVs / 2.9 Gb in day-5 eHAP kindred cells), not a measured error rate; the authors say the true rate is likely much lower | ([[10-Summaries/xing-2021-meta-cs\|Xing 2021]]) |
| Sequencing depth | Most cells at 3–8×, compared with 30–60× typical for single-cell SNV calling; SNVs called from ≥4 reads | ([[10-Summaries/xing-2021-meta-cs\|Xing 2021]]) |
| Amplification success | About 90% of cells | ([[10-Summaries/xing-2021-meta-cs\|Xing 2021]]) |
| Genome coverage (eHAP) | 50.9 ± 12.2% | ([[10-Summaries/xing-2021-meta-cs\|Xing 2021]]) |
| Strand-specific detection efficiency (eHAP) | 15.9 ± 6.1% | ([[10-Summaries/xing-2021-meta-cs\|Xing 2021]]) |

## Variants and relatives

- **Tn5-based relatives without duplex correction** — LIANTI and DLP+ are also Tn5-based scWGA but without strand-pairing duplex correction (see [[dlp-plus]]).
- **Currently the only single-cell duplex method** ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]); new short-read platforms (Ultima Genomics) may add native duplex capability without specialized chemistry.

## Evidence and examples

- Tn5-based single-cell duplex SNV detection, the only duplex method applicable to single cells ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Reuse beyond SNV calling.** scDeChIC-seq builds its single-cell libraries on META-CS transposons, lysis buffer and strand-tagging with a U-tolerant polymerase to read deaminase-written C→U edits from one cell ([[10-Summaries/shi-2026-dechic-seq|Shi 2026]]).

## Contested points

- **Cost.** General duplex methods need roughly twice the read depth per molecule (synthesis), but the META-CS paper reports *lower* sequencing cost, calling SNVs from ≥4 reads with most cells at 3–8× rather than the usual 30–60× ([[10-Summaries/xing-2021-meta-cs|Xing 2021]]).
- **Coverage.** Tn5 tagmentation biases limit coverage compared to MDA/PTA.
- **How strands are separated.** This page's definition says strands are separated by adapter orientation, while the primary paper says they are told apart by how they map to the reference ([[10-Summaries/xing-2021-meta-cs|Xing 2021]]); the adapter-orientation wording may be a holdover from the review description (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/scwga|scWGA]] — Biochemical methods that amplify the DNA of one cell for whole-genome sequencing.
> - `concept` [[30-Concepts/dlp-plus|DLP+]] — Tn5-based sibling without duplex correction, built for cell throughput.
> - `concept` [[30-Concepts/scdna-capabilities-framework|scDNA capabilities framework]] — Fidelity, co-presence and phenotypic association as the organizing capabilities.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Tagging and sequencing both strands of each molecule to cancel errors.
> - `hub` [[40-Topics/scdna-seq|scDNA-seq]] — Technologies that interrogate the DNA of single cells.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/shi-2026-dechic-seq|Shi 2026]]
> - [[10-Summaries/xing-2021-meta-cs|Xing 2021]]
