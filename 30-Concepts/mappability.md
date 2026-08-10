---
type: concept
title: Mappability
aliases: [multi-mapping, uniquely mappable regions, alignability]
tags: [alignment, repeats, bias, QC]
created: 2026-08-10
updated: 2026-08-10
---

# Mappability

> Whether a read originating from a given genomic position can be assigned back to that position uniquely. Low-mappability regions receive systematically depressed read counts regardless of their true copy number or signal.

## Definition

Exact repeats collapse onto a single path during BWT-based search, so a read matching many locations is cheap to detect and impossible to place ([[li-2009-bwa]]). Mappability is therefore a property of the reference and read length, not of the sample.

## Why it matters

- **Copy-number calling must correct for it.** Variable-size bins chosen so that each has comparable expected read count under mappability — averaging ~1 Mb — are what make an HMM emission model valid ([[bakker-2016-aneufinder]]).
- **Peak callers absorb it into local background.** A dynamic local λ estimated in 1/5/10 kb windows captures mappability bias along with copy number and chromatin structure ([[zhang-2008-macs]]).
- **Sparse-data callers must exclude it explicitly.** SEACR discards signal blocks overlapping a threshold-passing IgG block precisely to remove spurious peaks arising from multi-mapping at repeats ([[meers-2019-seacr]]).
- **Library chemistry can destroy it.** WGA4-amplified single cells suffer low mappability from adaptor contamination, wasting a large fraction of reads ([[zahn-2017-dlp]]).
- **Repeat-rich regions remain a structural blind spot** for short-read approaches generally ([[eichler-2007-completing-sv-map]]).

## Open questions

Highly repetitive and segmentally duplicated regions are the parts of the genome where somatic variation is least characterized, and no method in this corpus resolves them with short reads; see [[highly-repetitive-regions]].

## Related

- [[read-alignment]] · [[highly-repetitive-regions]] · [[copy-number-variation]] · [[computational-methods]]
