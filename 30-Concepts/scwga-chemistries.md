---
type: concept
title: scWGA chemistries
aliases: [single-cell whole-genome amplification, scWGA chemistry, WGA methods]
tags: [scWGA, MDA, MALBAC, PTA, DOP-PCR, LIANTI, amplification]
created: 2026-05-19
updated: 2026-10-12
---

# scWGA chemistries

> The family of chemistries that amplify femtogram quantities of single-cell DNA into nanogram-scale sequencing input, each trading off coverage uniformity, allelic dropout and error rate ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

> [!abstract] 한눈에
> scWGA chemistry는 단일 세포의 극미량 DNA를 sequencing이 가능한 양으로 불리는 방법들이고, coverage 균일성, allelic dropout, error rate를 한꺼번에 모두 잡는 방법은 없다 ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]). 그래서 최선의 WGA는 따로 없고 variant 종류마다 맞는 방법이 다르다는 것이 2015년 두 benchmark의 공통 결론이다 ([[10-Summaries/hou-2015-wga-comparison|Hou 2015]]; [[10-Summaries/huang-2015-scwga-review|Huang 2015]]).

## Definition

scWGA chemistries amplify femtogram quantities of single-cell DNA into nanogram-scale sequencing input ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]). The shared artifact list — locus and allelic dropout, uneven amplification, chimeric molecules and base-copy errors — is catalogued in [[10-Summaries/lim-2024-single-cell-omics-review|Lim 2024]]. See also [[30-Concepts/scwga]].

## Why it matters

- Coverage uniformity ↑, allelic dropout ↓ and error rate ↓ cannot all be had at once — no chemistry wins on all three ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- The standard statement of the trade-off: PCR-based WGA gives more uniform coverage and suits CNV calling but uses error-prone thermostable polymerases, whereas MDA with Φ29 has lower error rates and suits SNV calling but shows stronger allelic bias ([[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]).
- Two 2015 benchmarks, published three weeks apart by independent groups, converge on the same ordering and on the same conclusion: **there is no best WGA method, only a best method per variant class** ([[10-Summaries/hou-2015-wga-comparison|Hou 2015]]; [[10-Summaries/huang-2015-scwga-review|Huang 2015]]).

## The major chemistries

| Chemistry | Mechanism | Trade-off | Source |
|---|---|---|---|
| DOP-PCR | First general-purpose WGA (1992): one partially degenerate primer, low-stringency priming then high-stringency tag-driven amplification | High amplification bias; best uniformity among WGA chemistries and most CNA-amenable, but unsuitable for SNVs | ([[10-Summaries/telenius-1992-dop-pcr\|Telenius 1992]]; [[10-Summaries/gawad-2016-scgenome-review\|Gawad 2016]]; [[10-Summaries/zahn-2017-dlp\|Zahn 2017]]) |
| MDA (Multiple Displacement Amplification) | phi29 polymerase + random hexamers; long products (>10 kb, 10–12 kb) | First practical scWGA chemistry; lower error rate, stronger allelic bias | ([[10-Summaries/dean-2002-mda\|Dean 2002]]; [[10-Summaries/hard-2023-long-read-scwgs\|Hård 2023]]; [[10-Summaries/lahnemann-2020-grand-challenges\|Lähnemann 2020]]) |
| MALBAC | Quasi-linear preamplification by amplicon looping, then exponential PCR | Lower bias than MDA, higher error rate; framed for CNV rather than SNV work | ([[10-Summaries/gawad-2016-scgenome-review\|Gawad 2016]]; [[10-Summaries/zong-2017-malbac-protocol\|Zong 2017]]; [[10-Summaries/chenghang-2012-science\|Zong 2012]]) |
| PicoPLEX / NEB-WGA | Proprietary hybrid chemistries | — | — |
| LIANTI (Linear Amplification via Transposon Insertion) | Tn5-based linear amplification | Lower error rate | ([[10-Summaries/chen-2017-lianti\|LIANTI]]) |
| PTA (Primary Template-Directed Amplification) | phi29 + exonuclease-resistant terminator nucleotides | Most uniform coverage to date | ([[10-Summaries/gonzalez-pena-2021-pnas\|Gonzalez-Pena 2021]]) |
| META-CS / Tn5-duplex | Tn5-based, strand-aware scWGA built on META; single-cell-compatible duplex sequencing variant | Strand filter removes single-strand false positives | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]; [[10-Summaries/xing-2021-meta-cs\|META-CS]]) |
| Amplification-free (DLP+) | Direct tagmentation, no WGA | A separate branch, not a successor: trades per-cell coverage for integer copy number, clean allele ratios and readable replication state | ([[10-Summaries/laks-2019-dlp-plus\|Laks 2019]]) |

Strand-aware alternatives to standard WGA (META-CS, SISSOR) are catalogued in [[10-Summaries/lim-2024-single-cell-omics-review|Lim 2024]]. For the amplification-free branch see [[30-Concepts/dlp-plus]]; for PTA see [[30-Concepts/pta]].

### Chronology anchors

- **DOP-PCR (1992).** The founding paper was a flow-sorted-chromosome and cytogenetics method, judged more even than Alu-PCR by FISH ([[10-Summaries/telenius-1992-dop-pcr|Telenius 1992]]); its 4–6 orders of magnitude locus-to-locus bias, the baseline later chemistries are measured against, was measured later ([[10-Summaries/dean-2002-mda|Dean 2002]]).
- **MALBAC.** Five looping pre-amplification cycles give a power spectrum close to unamplified bulk, against MDA's megabase-scale over- and under-amplification ([[10-Summaries/zong-2017-malbac-protocol|Zong 2017]]; [[10-Summaries/chenghang-2012-science|Zong 2012]]).
- **Amplification-free.** DLP+ opts out of WGA entirely via direct tagmentation across 51,926 cells ([[10-Summaries/laks-2019-dlp-plus|Laks 2019]]).

### Evaluation axes

- **The eight-axis evaluation vocabulary** — coverage, uniformity, reproducibility, unmappable rate, chimera rate, allele dropout rate, SNV false-positive rate, CNV-calling ability — comes from [[10-Summaries/huang-2015-scwga-review|Huang 2015]] and is still how the field argues about WGA (synthesis).
- "Reproducibility" is a distinct axis from "uniformity": consistent bias is workable for CNV calling with matched controls, random bias is not (synthesis).
- For long-read scWGS, fragment length matters as much as uniformity: most WGA methods give fragments too short for long reads, whereas MDA yields 10–12 kb products, and droplet MDA keeps that length and reduces bias ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).
- **Input copy number** is a fourth lever that is not a chemistry at all: sorting G2/M nuclei gives MDA four copies of each locus instead of one ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]).

## Evidence and examples

**Head-to-head benchmark (Hou 2015)**

| Axis | DOP-PCR | MDA | MALBAC | Source |
|---|---|---|---|---|
| Genome recovery (consensus-genotype detection efficiency) | ~6% | ~84% | ~52% | ([[10-Summaries/hou-2015-wga-comparison\|Hou 2015]]) |
| Read evenness / CNV accuracy | best | variable by kit | good | ([[10-Summaries/hou-2015-wga-comparison\|Hou 2015]]) |
| Mapping ratio | 89.31% | 98.36% | 97.68% | ([[10-Summaries/hou-2015-wga-comparison\|Hou 2015]]) |
| Concordance where detected | 82.05% | 97.10% | 96.74% | ([[10-Summaries/hou-2015-wga-comparison\|Hou 2015]]) |

- **Kit identity matters as much as chemistry identity.** Three MDA kits diverged more on some metrics than the chemistries did: REPLI-g Single Cell gave the best coverage (8.84%), REPLI-g Mini and GenomiPhi V2 had higher read-distribution bias than the other kits tested, and GenomiPhi V2 showed strong GC dependence ([[10-Summaries/hou-2015-wga-comparison|Hou 2015]]). "We used MDA" is therefore an insufficient methods description (synthesis).
- DOP-PCR is specifically depleted in Alu and L1 repeat regions, a direct consequence of degenerate-primer annealing ([[10-Summaries/hou-2015-wga-comparison|Hou 2015]]).
- DOP-PCR's coverage breadth **saturates** with deeper sequencing, so extra reads buy nothing ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).

**Other findings**

- Sorting G2/M nuclei for MDA cut allele dropout to 9.73% and lifted breadth to 91% ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]).
- In kindred haploid cells, META-CS's strand-filtered calls had a C>A-dominated spectrum (Ti/Tv 0.27) ([[10-Summaries/xing-2021-meta-cs|META-CS]]).
- The same cells without the strand filter gave a transition-dominated spectrum (Ti/Tv 1.73) and roughly 100× more calls at the a4 threshold; the authors cite C>T deamination artifacts in MDA as the kind of single-strand false positive the filter removes ([[10-Summaries/xing-2021-meta-cs|META-CS]]).

## Contested points

- **Is amplification itself the problem?** The founding DLP paper argues that WGA copies each template as long molecules that are fragmented *afterwards*, so one region yields multiple inserts with non-overlapping coordinates that **cannot be filtered as duplicates**; fragmenting first makes every PCR copy an exact duplicate and therefore removable ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]). See [[30-Concepts/duplicate-marking]].
- This single fact accounts for most of WGA's coverage pathology, and it generalises: any protocol amplifying before fragmenting forfeits the distinction between duplicates and independent molecules (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/scwga|scWGA]] — Single-cell whole-genome amplification as a step in scDNA-seq.
> - `concept` [[30-Concepts/pta|PTA]] — Primary template-directed amplification with terminator nucleotides.
> - `concept` [[30-Concepts/dlp-plus|DLP+]] — Amplification-free direct-tagmentation single-cell library preparation.
> - `concept` [[30-Concepts/duplicate-marking|Duplicate marking]] — Why fragment-then-amplify makes PCR copies removable.
> - `hub` [[40-Topics/whole-genome-amplification|Whole-genome amplification]] — The scWGA methods and their artifacts.
> - `hub` [[40-Topics/scdna-seq|Single-cell DNA sequencing]] — Platforms and analysis for scDNA-seq.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Strand-aware error correction, including single-cell variants.

## All sources on this page

> [!info]- 17 summaries cited here
> - [[10-Summaries/chen-2017-lianti|Chen 2017]]
> - [[10-Summaries/chenghang-2012-science|Zong 2012]]
> - [[10-Summaries/dean-2002-mda|Dean 2002]]
> - [[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]
> - [[10-Summaries/gonzalez-pena-2021-pnas|Gonzalez-Pena 2021]]
> - [[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]
> - [[10-Summaries/hou-2015-wga-comparison|Hou 2015]]
> - [[10-Summaries/huang-2015-scwga-review|Huang & Xie 2015]]
> - [[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]
> - [[10-Summaries/laks-2019-dlp-plus|Laks 2019]]
> - [[10-Summaries/lim-2024-single-cell-omics-review|Lim 2024]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/telenius-1992-dop-pcr|Telenius 1992]]
> - [[10-Summaries/wang-2014-nuc-seq|Wang 2014]]
> - [[10-Summaries/xing-2021-meta-cs|Xing 2021]]
> - [[10-Summaries/zahn-2017-dlp|Zahn 2017]]
> - [[10-Summaries/zong-2017-malbac-protocol|Zong 2017]]
