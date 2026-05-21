---
type: concept
title: Circularization GoT
aliases: [circ-GoT]
tags: [single-cell, scRNA-seq, genotyping, method]
created: 2026-05-07
updated: 2026-05-07
---

# Circularization GoT

> Extension of [[got]] for genotyping mutations located far (≥ 1.5 kb) from a transcript end, using sequential rounds of intramolecular ligation and inverse PCR to shrink the amplicon to a length compatible with short-read Illumina sequencing while preserving the cell barcode.

## Definition

Standard GoT amplifies from a gene-specific primer at the mutation locus to the 3′ end of the 10x library fragment, retaining the cell barcode + UMI. For mutations far from transcript ends, the resulting amplicon is too long to cluster efficiently on Illumina flow cells. Circularization GoT instead performs ([[10-Summaries/nam-2019-got]]):

1. Hemi-nested gene-specific PCR to define cloning-compatible ends around the region of interest.
2. **Intramolecular ligation + inverse PCR** to remove the intervening sequence between the cell barcode and the mutation site.
3. A second round of circularization + inverse PCR.
4. Final library indexing and short-read sequencing.

## Why it matters

In [[10-Summaries/nam-2019-got]] the technique increased SF3B1 genotyping yield from 750 to 2,004 cells (9% → 24%) and successfully genotyped JAK2 V617F at ~2.3 kb from the closer transcript end — a target unreachable with linear GoT.

It is, however, a **workaround**: each circularization step adds wet-lab complexity and reduces yield. The cleaner architectural fix — capture the locus from genomic DNA instead of from cDNA — arrives with [[got-cha]] in [[10-Summaries/izzo-2024-got-cha]], which obviates circularization entirely.

## Variants and refinements

- Validated against Oxford Nanopore long-read sequencing (GridION X5) of un-circularized GoT amplicons to confirm low intra- and inter-transcript PCR recombination.
- Used for both common drivers (JAK2 V617F) and a mixing study with TF-1 / HEL cell lines.

## Contested points

- The yield improvement is real but limited compared to gDNA-based approaches; circularization GoT is now largely of historical methodological interest.

## Examples

- JAK2V617F essential thrombocythemia: 7.3% of CD34+ cells genotyped via circularization GoT, sufficient to recover the clinical phenotype-associated MkP-priming pattern ([[10-Summaries/nam-2019-got]]).

## Related

- [[got]] — base method.
- [[got-cha]] — gDNA-based successor that supersedes the need for circularization.
- [[20-Entities/anna-s-nam]]
- [[20-Entities/landau-lab]]
