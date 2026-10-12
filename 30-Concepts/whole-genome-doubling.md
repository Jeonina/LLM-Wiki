---
type: concept
title: "Whole-Genome Doubling"
aliases: []
tags: []
created: 2026-10-07
updated: 2026-10-12
sources: ["[[10-Summaries/kaufmann-2022-medicc2]]", "[[10-Summaries/mcpherson-2025-ongoing-wgd]]"]
---

# Whole-Genome Doubling

> Whole-genome doubling (WGD) is the duplication of an entire chromosome complement in a cell lineage, found in more than 30% of solid cancers and linked to metastasis, drug resistance and poor outcomes ([[10-Summaries/mcpherson-2025-ongoing-wgd]]).

## Definition

In single-cell WGS, WGD can be called per cell from allele-specific copy number: a cell with more than half its genome at two or more copies of the major allele (FM2 > 0.5) has undergone at least one WGD, and FM3 > 0.5 marks at least two ([[10-Summaries/mcpherson-2025-ongoing-wgd]]).

## Why it matters

- WGD is an ongoing process rather than a single event: 40 of 41 high-grade serous ovarian cancer patients carried coexisting WGD multiplicities ([[10-Summaries/mcpherson-2025-ongoing-wgd]]).
- WGD cells show higher ploidy-adjusted rates of chromosome and arm losses and gains, and WGD-high tumours have a 3.3-fold higher rate of cGAS-positive ruptured micronuclei ([[10-Summaries/mcpherson-2025-ongoing-wgd]]).
- Despite more chromosomal instability, WGD-high tumours show STING1 repression and reduced interferon signalling ([[10-Summaries/mcpherson-2025-ongoing-wgd]]).
- Pseudo-triploid HGSOC karyotypes are inferred to arise from WGD plus pre- and post-WGD losses rather than incremental gains ([[10-Summaries/mcpherson-2025-ongoing-wgd]]).

## Modes

Truncal, parallel, subclonal and unexpanded WGD histories were distinguished by SNV-based timing (doubleTime) in 39 patients ([[10-Summaries/mcpherson-2025-ongoing-wgd]]). WGD-aware copy-number phylogenies model doubling explicitly ([[10-Summaries/kaufmann-2022-medicc2]]).

Read-depth-ratio callers cannot detect WGD, because a doubled cell has the same depth ratios between regions as an undoubled one ([[10-Summaries/wesley-2026-songbird]]). Songbird estimates absolute ploidy from fragment geometry in amplification-free Tn5 libraries: fragments that overlap a reference fragment can come only from the other n − 1 copies, so the ratio of overlap density to upstream density approaches (n − 1)/n ([[10-Summaries/wesley-2026-songbird]]). Within each breakpoint-defined subclone, cells near a 1:2 ploidy ratio to the rest are flagged as WGD ([[10-Summaries/wesley-2026-songbird]]). Median ploidy was accurate up to 6 on a DLP+ hTERT/HEK293T ladder, and only Songbird and ASCENT called the 2× hTERT wells correctly ([[10-Summaries/wesley-2026-songbird]]).

B-allele-frequency methods such as CHISEL cannot detect a recent WGD with no later copy-number change, because they need mutations to accumulate on different alleles. scAbsolute instead detects such WGD from read density alone in DLP/ACT-type data ([[10-Summaries/schneider-2024-scabsolute]]).

Balanced doublings carry no allelic imbalance, so BAF-based callers can miss them ([[10-Summaries/kolbeinsdottir-2025-ascent]]). In direct-tagmentation scWGS, the rate of fragment overlap rises with copy number, and ASCENT used it to flag S-phase, G2M and multiplet HCT116 cells at P < 1%, while scAbsolute missed 89% of G2M cells ([[10-Summaries/kolbeinsdottir-2025-ascent]]).

Callers can disagree on whether WGD happened at all. On DLP+ ovarian cancer OV2295, Alleloscope called no WGD while CNRein, SIGNALS and CHISEL called WGD in many cells ([[10-Summaries/ivanovic-2025-cnrein]]). Truncal-SNV VAFs peaked at 1/3 and 2/3 in {2,1} regions for the WGD-calling methods but near 1/2 for Alleloscope, which supports WGD ([[10-Summaries/ivanovic-2025-cnrein]]). CNRein models WGD as one of its CNA actions, doubling all copy numbers ([[10-Summaries/ivanovic-2025-cnrein]]).

## Open questions

- Whether STING1 repression precedes WGD is untested ([[10-Summaries/mcpherson-2025-ongoing-wgd]]).
- Perfectly doubled cells are hard to distinguish from their non-doubled counterparts in single-cell copy-number data, so 2×WGD frequency may be underestimated (synthesis).
- Fragment-overlap ploidy estimation needs no SNPs or copy-number variation, so it can in principle call perfectly doubled cells. Songbird recovered doubled diploid genomes (2× hTERT wells), but its WGD module has not yet been tested in tumours with mixed WGD multiplicities ([[10-Summaries/wesley-2026-songbird]]; (synthesis)).
- scAbsolute addresses this for amplification-free, paired-end data. Overlapping unique reads are capped by the number of physical DNA copies, so read density at a given read depth separates G1 cells from G2, WGD or multiplet cells that look the same in copy-number profiles: 97% G1 vs 6N–12N accuracy in PEO1 multiplets ([[10-Summaries/schneider-2024-scabsolute]]). It still cannot tell G2 from WGD cells without extra information such as Geminin staining ([[10-Summaries/schneider-2024-scabsolute]]).
- **Disagreement over scAbsolute's G2/WGD detection.** Its authors report 97% accuracy separating G1 cells from 6N–12N multiplets in PEO1 ([[10-Summaries/schneider-2024-scabsolute]]). The ASCENT authors report that scAbsolute missed 89% of G2M cells in sorted HCT116 ([[10-Summaries/kolbeinsdottir-2025-ascent]]), and the Songbird ploidy ladder found it tended to call 2× and 3× hTERT wells diploid ([[10-Summaries/wesley-2026-songbird]]). The competing benchmarks ran scAbsolute outside its original setup (e.g. GRCh38 at 1 Mb in the ASCENT run), so whether this is a method limit or a regime mismatch is unresolved (synthesis).

## Related

- [[chromosomal-instability]] · [[copy-number-variation]] · [[dlp-plus]] · [[40-Topics/cancer-clonal-evolution]]
