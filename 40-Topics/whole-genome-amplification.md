---
type: topic
title: Whole-genome amplification (scWGA)
aliases: [scWGA topic, WGA topic, whole-genome amplification methods]
tags: [scWGA, methods, amplification]
created: 2026-05-11
updated: 2026-10-12
paper_section: ["3.1"]
explainer: wga-simulator
---

# Whole-genome amplification (scWGA)

> The set of biochemical methods that bridge the ~6 pg of DNA in a single diploid cell ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]) to the input requirement of any sequencing platform. It is the defining technical challenge of [[40-Topics/scdna-seq]]: amplifying 10⁵- to 10⁶-fold without losing coverage uniformity, allelic balance or per-base accuracy (synthesis).

> [!abstract] 한눈에
> 단일 세포 DNA를 시퀀싱하려면 증폭이 필요하고, 증폭 방식(PCR, Φ29 등온, Tn5)마다 coverage, 균일도, 대립유전자 균형, 오류율을 서로 다르게 맞바꾼다 ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). 여러 벤치마크는 최선의 방법이 하나로 정해지지 않고 찾으려는 변이 종류에 따라 달라진다고 결론짓는다 ([[10-Summaries/hou-2015-wga-comparison|Hou 2015]]; [[10-Summaries/huang-2015-scwga-review|Huang 2015]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 WGA 시뮬레이터](../60-Explainers/wga-simulator.html)
<!-- /explainer-links -->

## Key points

- **Three chemistry families with different tradeoffs.** PCR-based, isothermal Φ29 and Tn5-based methods differ in coverage, uniformity, allelic balance and throughput; PTA reaches ~95% coverage, DLP+ more than 10,000 cells at very low per-cell coverage ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **There is no best method, only a best method per variant class.** Two independent 2015 benchmarks reached this conclusion ([[10-Summaries/hou-2015-wga-comparison|Hou 2015]]; [[10-Summaries/huang-2015-scwga-review|Huang 2015]]).
- **False positives are the dominant scWGA problem.** Overamplified errors and single-strand dropout overwhelm the true signal ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Input copy number is a lever separate from chemistry.** Starting MDA from G2/M nuclei with four copies gave 91% breadth and 9.73% ADO ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]).
- **WGA's problems were first treated as computational in genome assembly.** Single-cell assemblers handled MDA's uneven coverage years before variant callers faced the same statistics ([[10-Summaries/chitsaz-2011-velvet-sc|Velvet-SC]]; [[10-Summaries/peng-2012-idba-ud|IDBA-UD]]; [[10-Summaries/bankevich-2012-spades|SPAdes]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/scwga|scWGA]] — Umbrella concept: amplifying ~6 pg of single-cell DNA for sequencing; three chemistry categories.
> - `concept` [[30-Concepts/scwga-chemistries|scWGA chemistries]] — How chemistries trade coverage uniformity, allelic dropout and error rate.
> - `concept` [[30-Concepts/pta|PTA]] — Φ29 with chain terminators; ~95% coverage with high allelic balance.
> - `concept` [[30-Concepts/mda|MDA]] — Isothermal Φ29 strand-displacement amplification; the first method above 70% coverage.
> - `concept` [[30-Concepts/sequencing-depth-and-coverage|Sequencing depth and coverage]] — Allocating a fixed budget between depth per cell and number of cells.
> - `concept` [[30-Concepts/single-cell-genome-assembly|Single-cell genome assembly]] — De novo assembly from one amplified cell, where MDA's coverage pathology was first confronted.

## Method categories

The umbrella concept is [[30-Concepts/scwga]], with three chemistry categories ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]); see [[30-Concepts/scwga-chemistries]] for the comparison table.

| Category | Method | Coverage | Note |
|---|---|---|---|
| PCR-based | [[30-Concepts/dop-pcr\|DOP-PCR]] | 20–25% | High uniformity, low cost ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| PCR-based | PicoPLEX | 35–45% | Looped products ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| PCR-based (hybrid) | [[30-Concepts/malbac\|MALBAC]] | 55–60% | Looped products ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| Isothermal (Φ29) | [[30-Concepts/mda\|MDA]] | 70–75% | Low allelic balance ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| Isothermal (Φ29) | [[30-Concepts/pta\|PTA]] | ~95% | Chain terminators give short amplicons primed from the native template; high allelic balance ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| Tn5 transposon | LIANTI | 80–85% | Not commercially available, complex protocol ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| Tn5 transposon | [[30-Concepts/dlp-plus\|DLP+]] | Very low per cell | >10,000 cells per run ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| Tn5 transposon | [[30-Concepts/meta-cs\|META-CS]] | — | Strand-labeling WGA; FPR upper bound ~2.4×10⁻⁸ validated on kindred eHAP cells and sperm ([[10-Summaries/xing-2021-meta-cs\|META-CS]]) |
| Isothermal (Φ29), droplet | Droplet MDA (Xdrop) | — | Better coverage uniformity than tube MDA; keeps long fragments for long-read sequencing ([[10-Summaries/hard-2023-long-read-scwgs\|Hård 2023]]) |

## Errors introduced by scWGA

| Error | Effect | Source |
|---|---|---|
| Allelic dropout / locus dropout | False negatives | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]; [[10-Summaries/gawad-2016-scgenome-review\|Gawad 2016]]) |
| Allelic imbalance | — | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]; [[10-Summaries/gawad-2016-scgenome-review\|Gawad 2016]]) |
| Single-strand dropout (SSD) | False positives that overwhelm true signal | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| Polymerase error | Taq much higher than Φ29 | Polymerase errors listed by ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]); Taq vs Φ29 comparison (synthesis) |
| Chimera formation (strand displacement) | Makes structural variants hard to observe in single cells | ([[10-Summaries/huang-2015-scwga-review\|Huang 2015]]; [[10-Summaries/gawad-2016-scgenome-review\|Gawad 2016]]) |

## Benchmarks and reviews

Two independent 2015 comparisons converge: there is no best method, only a best method per variant class — see [[30-Concepts/scwga-chemistries]] for the table ([[10-Summaries/hou-2015-wga-comparison|Hou 2015]]; [[10-Summaries/huang-2015-scwga-review|Huang 2015]]).

| Study | Year | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/debourcy-2014-plosone\|de Bourcy 2014]] | 2014 | Quantitative comparison of single-cell WGA methods | First systematic head-to-head benchmark of MDA, MALBAC and other chemistries ([[10-Summaries/debourcy-2014-plosone\|de Bourcy 2014]]) |
| [[10-Summaries/hou-2015-wga-comparison\|Hou 2015]] | 2015 | Seven commercial kits, 29 cells, with a 0.1× downsampling step so uniformity comparisons are not confounded by sequencing effort | No best method, only a best method per variant class ([[10-Summaries/hou-2015-wga-comparison\|Hou 2015]]) |
| [[10-Summaries/huang-2015-scwga-review\|Huang 2015]] | 2015 | Review; five kits deep-sequenced | The eight-axis evaluation vocabulary ([[10-Summaries/huang-2015-scwga-review\|Huang 2015]]) |
| [[10-Summaries/gawad-2016-scgenome-review\|Gawad 2016]] | 2016 | Review | Pre-PTA three-category comparison ([[10-Summaries/gawad-2016-scgenome-review\|Gawad 2016]]) |
| [[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]] | 2025 | Review | Current method comparison (Table 1) ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |

## Input copy number as a fourth lever

[[10-Summaries/wang-2014-nuc-seq|Wang 2014]] sorts G2/M nuclei so MDA starts from four copies rather than one — 91% breadth, 9.73% ADO, FPR 1.24 × 10⁻⁶ — without changing the chemistry at all ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]).

## Assembly as the first computational response

[[10-Summaries/chitsaz-2011-velvet-sc|Velvet-SC]], [[10-Summaries/peng-2012-idba-ud|IDBA-UD]] and [[10-Summaries/bankevich-2012-spades|SPAdes]] solved MDA's coverage catastrophe for de novo assembly years before the variant-calling field faced the same statistics; see [[30-Concepts/single-cell-genome-assembly]]. This is also the earliest place in the corpus where WGA's problems are declared computational rather than experimental ([[10-Summaries/chitsaz-2011-velvet-sc|Velvet-SC]]). Related downstream handling of amplification copies: [[30-Concepts/duplicate-marking]].

## Multi-omic methods built on specific amplification chemistries

| Method | Amplification | Source |
|---|---|---|
| GoT | 10x cDNA amplification — not classical scWGA but related | ([[10-Summaries/nam-2019-got\|Nam 2019]]) |
| GoT–ChA | gDNA locus amplification in droplets | ([[10-Summaries/izzo-2024-got-cha\|Izzo 2024]]) |
| scDAF-seq | PTA for genome-wide amplification | ([[10-Summaries/swanson-2025-daf-seq\|Swanson 2025]]) |
| G&T-seq family | MDA / PCR / DA-PCR | ([[10-Summaries/vandereyken-2023-scmultiomics-review\|Vandereyken 2023]]) |

## Alternatives that skip scWGA

- **Duplex sequencing.** Bulk-DNA single-molecule methods: [[40-Topics/duplex-sequencing]].
- **DNTR-seq.** Direct nuclear DNA tagmentation, skipping WGA ([[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]).

## Key people

- [[20-Entities/diane-d-shao]] — keystone 2025 review ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- [[20-Entities/charles-gawad]] — foundational 2016 review ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]).
- [[20-Entities/christopher-walsh]] — early PTA adopter for neuron mosaicism.

No synthesized note exists yet; a natural target is "Choosing a scWGA method: tradeoffs and applications."

## Open questions

- Whether MDA retains a niche given PTA's cost approaching MDA's. (synthesis)
- When to use scWGA-free approaches (DNTR-seq, duplex sequencing) — application-dependent, no consensus heuristic ([[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]).
- Standardization of QC metrics and definitions (especially ADO) across methods — flagged by [[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]], still partly unresolved.
- Coverage vs cell-throughput operating points — DLP+ scales to >10⁴ cells at very low coverage; PTA reaches ~95% coverage at much lower cell throughput; how to choose for a given biology ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

## Related

> [!cards]
> - `hub` [[40-Topics/scdna-seq|scDNA-seq]] — Technologies that interrogate the DNA of single cells, by amplification or by single-molecule reads.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Strand-paired single-molecule sequencing that avoids amplification error.

## All sources on this page

> [!info]- 15 summaries cited here
> - [[10-Summaries/bankevich-2012-spades|Bankevich 2012]]
> - [[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]
> - [[10-Summaries/debourcy-2014-plosone|de Bourcy 2014]]
> - [[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]
> - [[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]
> - [[10-Summaries/hou-2015-wga-comparison|Hou 2015]]
> - [[10-Summaries/huang-2015-scwga-review|Huang & Xie 2015]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
> - [[10-Summaries/peng-2012-idba-ud|Peng 2012]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
> - [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]
> - [[10-Summaries/wang-2014-nuc-seq|Wang 2014]]
> - [[10-Summaries/xing-2021-meta-cs|Xing 2021]]
