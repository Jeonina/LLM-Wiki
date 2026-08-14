---
type: concept
title: scWGA chemistries
aliases: [single-cell whole-genome amplification, scWGA chemistry, WGA methods]
tags: [scWGA, MDA, MALBAC, PTA, DOP-PCR, LIANTI, amplification]
created: 2026-05-19
updated: 2026-08-10
---

# scWGA chemistries

> The family of chemistries used to amplify femtogram quantities of single-cell DNA into nanogram-scale sequencing input. Different chemistries trade off coverage uniformity, allelic dropout, and error rate.

## The major chemistries

- **DOP-PCR** — first generation; degenerate oligonucleotide-primed PCR; high amplification bias ([[10-Summaries/gawad-2016-scgenome-review]]).
- **MDA (Multiple Displacement Amplification)** — phi29 polymerase + random hexamers; long products (>10 kb); first practical scWGA chemistry ([[10-Summaries/dean-2002-mda]]).
- **MALBAC** — quasi-linear preamplification + PCR exponential phase; lower bias than MDA, higher error rate ([[10-Summaries/gawad-2016-scgenome-review]]).
- **PicoPLEX / NEB-WGA** — proprietary hybrid chemistries.
- **LIANTI (Linear Amplification via Transposon Insertion)** — Tn5-based linear amplification; lower error rate ([[10-Summaries/chen-2017-lianti]]).
- **PTA (Primary Template-Directed Amplification)** — phi29 + exonuclease-resistant terminator nucleotides; most uniform coverage to date ([[10-Summaries/gonzalez-pena-2021-pnas]]).
- **META-CS / Tn5-duplex** — single-cell-compatible duplex sequencing variant ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Tradeoff space

Coverage uniformity ↑, allelic dropout ↓, error rate ↓ — but no chemistry wins on all three ([[10-Summaries/gawad-2016-scgenome-review]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Chronology anchors

- **DOP-PCR (1992)** — first general-purpose WGA; one partially degenerate primer, low-stringency priming then high-stringency tag-driven amplification. Its 4–6 orders of magnitude locus-to-locus bias is the baseline every later chemistry is measured against ([[10-Summaries/telenius-1992-dop-pcr]]; contrast in [[10-Summaries/dean-2002-mda]]).
- **MALBAC** — quasi-linear amplification by amplicon looping, framed for CNV rather than SNV work; early-cycle polymerase errors imprint on all downstream copies ([[10-Summaries/zong-2017-malbac-protocol]]).
- **Amplification-free is a separate branch, not a successor.** DLP+ opts out of WGA entirely via direct tagmentation, trading per-cell coverage for integer copy number, clean allele ratios and readable replication state across 51,926 cells ([[10-Summaries/laks-2019-dlp-plus]]).
- **The mechanistic argument against WGA, from the founding DLP paper.** WGA copies each template as long molecules that are fragmented *afterwards*, so one region yields multiple inserts with non-overlapping coordinates that **cannot be filtered as duplicates**; fragmenting first makes every PCR copy an exact duplicate and therefore removable ([[10-Summaries/zahn-2017-dlp]]). This single fact accounts for most of WGA's coverage pathology, and it generalizes: any protocol amplifying before fragmenting forfeits the distinction between duplicates and independent molecules (synthesis). Among the WGA chemistries, DOP-PCR gives the best uniformity and is the most CNA-amenable, but its coverage breadth **saturates** with deeper sequencing, so extra reads buy nothing and it remains unsuitable for SNVs ([[10-Summaries/zahn-2017-dlp]]). See [[30-Concepts/duplicate-marking]].
- The shared WGA artifact list — locus and allelic dropout, uneven amplification, chimeric molecules, base-copy errors — plus strand-aware alternatives (META-CS, SISSOR) is catalogued in [[10-Summaries/lim-2024-single-cell-omics-review]].

## Related

- [[30-Concepts/scwga]] · [[30-Concepts/pta]] · [[40-Topics/duplex-sequencing]]
- [[40-Topics/whole-genome-amplification]] · [[40-Topics/scdna-seq]]
- [[10-Summaries/telenius-1992-dop-pcr]] · [[10-Summaries/zong-2017-malbac-protocol]] · [[10-Summaries/laks-2019-dlp-plus]] · [[30-Concepts/dlp-plus]]

## Added 2026-08-13

Two 2015 benchmarks, published three weeks apart from independent groups, converge on the same ordering — and on the same conclusion that **there is no best WGA method, only a best method per variant class** ([[10-Summaries/hou-2015-wga-comparison]]; [[10-Summaries/huang-2015-scwga-review]]).

| Axis | DOP-PCR | MDA | MALBAC |
|---|---|---|---|
| Genome recovery (consensus-genotype detection efficiency) | ~6% | ~84% | ~52% ([[10-Summaries/hou-2015-wga-comparison]]) |
| Read evenness / CNV accuracy | best | variable by kit | good ([[10-Summaries/hou-2015-wga-comparison]]) |
| Mapping ratio | 89.31% | 98.36% | 97.68% ([[10-Summaries/hou-2015-wga-comparison]]) |
| Concordance where detected | 82.05% | 97.10% | 96.74% ([[10-Summaries/hou-2015-wga-comparison]]) |

**Kit identity matters as much as chemistry identity.** Three MDA kits diverged more on some metrics than the chemistries did: REPLI-g Single Cell gave the best coverage (8.84%), REPLI-g Mini had the *highest* read-distribution bias of all seven kits tested, and GenomiPhi V2 showed strong GC dependence ([[10-Summaries/hou-2015-wga-comparison]]). "We used MDA" is insufficient methods description. (synthesis)

DOP-PCR is specifically depleted in Alu and L1 repeat regions, a direct consequence of degenerate-primer annealing ([[10-Summaries/hou-2015-wga-comparison]]).

**The eight-axis evaluation vocabulary** — coverage, uniformity, reproducibility, unmappable rate, chimera rate, allele dropout rate, SNV false-positive rate, CNV-calling ability — comes from [[10-Summaries/huang-2015-scwga-review]] and is still how the field argues about WGA. Note that "reproducibility" is a distinct axis from "uniformity": consistent bias is workable for CNV calling with matched controls; random bias is not. (synthesis)

A fourth lever exists that is not a chemistry at all: **input copy number**. Sorting G2/M nuclei gives MDA four copies of each locus instead of one, cutting allele dropout to 9.73% and lifting breadth to 91% ([[10-Summaries/wang-2014-nuc-seq]]).
