---
type: concept
title: scWGA chemistries
aliases: [single-cell whole-genome amplification, scWGA chemistry, WGA methods]
tags: [scWGA, MDA, MALBAC, PTA, DOP-PCR, LIANTI, amplification]
created: 2026-05-19
updated: 2026-10-07
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

- **DOP-PCR (1992)** — first general-purpose WGA; one partially degenerate primer, low-stringency priming then high-stringency tag-driven amplification. The founding paper was a flow-sorted-chromosome and cytogenetics method, judged more even than Alu-PCR by FISH ([[10-Summaries/telenius-1992-dop-pcr]]); its 4–6 orders of magnitude locus-to-locus bias, the baseline later chemistries are measured against, was measured later ([[10-Summaries/dean-2002-mda]]).
- **MALBAC** — quasi-linear amplification by amplicon looping, framed for CNV rather than SNV work: five looping pre-amplification cycles give a power spectrum close to unamplified bulk, against MDA's megabase-scale over- and under-amplification ([[10-Summaries/zong-2017-malbac-protocol]]; [[10-Summaries/chenghang-2012-science]]).
- **Amplification-free is a separate branch, not a successor.** DLP+ opts out of WGA entirely via direct tagmentation, trading per-cell coverage for integer copy number, clean allele ratios and readable replication state across 51,926 cells ([[10-Summaries/laks-2019-dlp-plus]]).
- **The mechanistic argument against WGA, from the founding DLP paper.** WGA copies each template as long molecules that are fragmented *afterwards*, so one region yields multiple inserts with non-overlapping coordinates that **cannot be filtered as duplicates**; fragmenting first makes every PCR copy an exact duplicate and therefore removable ([[10-Summaries/zahn-2017-dlp]]). This single fact accounts for most of WGA's coverage pathology, and it generalizes: any protocol amplifying before fragmenting forfeits the distinction between duplicates and independent molecules (synthesis). Among the WGA chemistries, DOP-PCR gives the best uniformity and is the most CNA-amenable, but its coverage breadth **saturates** with deeper sequencing, so extra reads buy nothing and it remains unsuitable for SNVs ([[10-Summaries/zahn-2017-dlp]]). See [[30-Concepts/duplicate-marking]].
- The shared WGA artifact list — locus and allelic dropout, uneven amplification, chimeric molecules, base-copy errors — plus strand-aware alternatives (META-CS, SISSOR) is catalogued in [[10-Summaries/lim-2024-single-cell-omics-review]].

## Added 2026-10-07

The standard trade-off is stated as: PCR-based WGA gives more uniform coverage and suits CNV calling but uses error-prone thermostable polymerases, whereas MDA with Φ29 has lower error rates and suits SNV calling but shows stronger allelic bias ([[10-Summaries/lahnemann-2020-grand-challenges]]).

For long-read scWGS, fragment length matters as much as uniformity. Most WGA methods give fragments too short for long reads, whereas MDA yields 10–12 kb products; droplet MDA keeps that length and reduces bias ([[10-Summaries/hard-2023-long-read-scwgs]]).

META-CS is a Tn5-based, strand-aware scWGA built on META. In kindred haploid cells its strand-filtered calls had a C>A-dominated spectrum (Ti/Tv 0.27). The same cells without the strand filter gave a transition-dominated spectrum (Ti/Tv 1.73) and roughly 100× more calls at the a4 threshold. The authors cite C>T deamination artifacts in MDA as the kind of single-strand false positive the filter removes ([[10-Summaries/xing-2021-meta-cs]]).


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

**Kit identity matters as much as chemistry identity.** Three MDA kits diverged more on some metrics than the chemistries did: REPLI-g Single Cell gave the best coverage (8.84%), REPLI-g Mini and GenomiPhi V2 had higher read-distribution bias than the other kits tested, and GenomiPhi V2 showed strong GC dependence ([[10-Summaries/hou-2015-wga-comparison]]). "We used MDA" is insufficient methods description. (synthesis)

DOP-PCR is specifically depleted in Alu and L1 repeat regions, a direct consequence of degenerate-primer annealing ([[10-Summaries/hou-2015-wga-comparison]]).

**The eight-axis evaluation vocabulary** — coverage, uniformity, reproducibility, unmappable rate, chimera rate, allele dropout rate, SNV false-positive rate, CNV-calling ability — comes from [[10-Summaries/huang-2015-scwga-review]] and is still how the field argues about WGA. Note that "reproducibility" is a distinct axis from "uniformity": consistent bias is workable for CNV calling with matched controls; random bias is not. (synthesis)

A fourth lever exists that is not a chemistry at all: **input copy number**. Sorting G2/M nuclei gives MDA four copies of each locus instead of one, cutting allele dropout to 9.73% and lifting breadth to 91% ([[10-Summaries/wang-2014-nuc-seq]]).
