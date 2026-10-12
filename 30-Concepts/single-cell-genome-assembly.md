---
type: concept
title: Single-cell genome assembly
aliases: [de novo single-cell assembly, SPAdes, Velvet-SC, IDBA-UD, E+V-SC]
tags: [assembly, de-Bruijn-graph, MDA, uneven-coverage, chimera, metagenomics, uncultivated-bacteria]
created: 2026-08-13
updated: 2026-10-12
---

# Single-cell genome assembly

> De novo reconstruction of a genome from the reads of one amplified cell, with no reference genome to lean on — which is why it was the first place [[mda|MDA]]'s coverage pathology had to be solved computationally ([[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]).

> [!abstract] 한눈에
> Single-cell genome assembly는 증폭된 세포 하나의 read만으로 reference 없이 유전체를 다시 짜 맞추는 작업이다. MDA가 만드는 극단적으로 고르지 않은 coverage와 chimera 때문에 기존 de Bruijn assembler가 통하지 않았고, Velvet-SC·IDBA-UD·SPAdes가 이를 알고리즘 차원에서 풀었다 ([[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]; [[10-Summaries/peng-2012-idba-ud|IDBA-UD]]; [[10-Summaries/bankevich-2012-spades|SPAdes]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [분석 도구 교재](../60-Explainers/computational-methods.html)
>
> [단일세포 WGA 시뮬레이터](../60-Explainers/wga-simulator.html)
<!-- /explainer-links -->

## Definition

Single-cell genome assembly is de novo reconstruction of a genome from the reads of one amplified cell ([[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]). Unlike every other analysis in this wiki, it has **no reference genome**, so the amplification artifacts of [[mda|MDA]] cannot be corrected against one and must be handled inside the assembler (synthesis).

## Why it matters

- The motivating application is uncultivated organisms: most microbes cannot be cultured ([[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]).
- Metagenomics is gene-centric and structurally cannot say which genes co-occur in one organism; single-cell assembly can ([[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]).
- It is the earliest place in the corpus where WGA's problems are named as **computational rather than experimental** ([[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]).

## Why it is a separate problem

**Uneven coverage.** Standard de Bruijn assemblers prune sequencing errors by discarding low-multiplicity *k*-mers, which assumes near-uniform coverage; single-cell MDA data violates that assumption catastrophically ([[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]).

| Data | Coverage profile | Source |
|---|---|---|
| Multicell *E. coli* | Most positions at 450–800×; only 0.1% below 450× | ([[10-Summaries/chitsaz-2011-velvet-sc\|Chitsaz 2011]]) |
| Single-cell *E. coli* | **5% of positions <10×, 11% <30×** — and ~30× is the usual minimum for gap-free assembly | ([[10-Summaries/chitsaz-2011-velvet-sc\|Chitsaz 2011]]) |

- The multiplicity ordering inverts: **incorrect *k*-mers in high-depth regions can outnumber correct *k*-mers in low-depth regions**, so no single global threshold works ([[10-Summaries/peng-2012-idba-ud|IDBA-UD]]).

**Chimeras.** A second MDA artifact compounds the first:

- Chimeras formed during φ29's branching amplification join non-contiguous sequences, producing both chimeric reads and chimeric read-pairs ([[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]).
- Chimeras are also why single-cell [[structural-variants|structural variants]] resist detection generally ([[10-Summaries/huang-2015-scwga-review|Huang 2015]]).

## Assemblers

Three solutions appeared in 2011–2012 ([[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]; [[10-Summaries/peng-2012-idba-ud|IDBA-UD]]; [[10-Summaries/bankevich-2012-spades|SPAdes]]).

| Tool | Core fix | Read pairs | Chimeras | Source |
|---|---|---|---|---|
| Velvet-SC / E+V-SC | Progressively increasing coverage cutoff, coupled to EULER-SR error correction | Discarded deliberately, to avoid misassembly from chimeric pairs | Quantified (2% of *E. coli*, 0.5% of *S. aureus* read pairs) but not removed | ([[10-Summaries/chitsaz-2011-velvet-sc\|Chitsaz 2011]]) |
| IDBA-UD | Multiple depth-relative thresholds; iterative *k* from k_min to k_max carrying contigs forward as reads; local assembly with paired-end info | Used for local assembly of low-depth short repeats | Not addressed | ([[10-Summaries/peng-2012-idba-ud\|IDBA-UD]]) |
| SPAdes | Paired de Bruijn graph + *k*-bimer adjustment; multisized de Bruijn graph; Hammer error correction | Used fully — the stated improvement over E+V-SC | Explicit detection and removal stage | ([[10-Summaries/bankevich-2012-spades\|SPAdes]]) |
| hifiasm on HiFi reads (human) | Self-BLAST chimera filter before assembly | — | Filtered before assembly | ([[10-Summaries/hard-2023-long-read-scwgs\|Hård 2023]]) |
| SALSA2 scaffolding with scNanoHi-C | Single-cell Hi-C contacts scaffold single-cell draft assemblies | — | — | ([[10-Summaries/li-2023-scnanohi-c\|scNanoHi-C]]) |

- Two SPAdes authors coauthored E+V-SC and stated the reason for rebuilding rather than patching: *"one needs to change algorithmic design (rather than just modify existing tools) to fully utilize the potential of SCS"* ([[10-Summaries/bankevich-2012-spades|SPAdes]]).
- SPAdes is the one of the three that remained in routine use (synthesis).

## Evidence and examples

- Single *E. coli* and *S. aureus* cells yield **>91% of genes within contigs**, against 95% from a multicell *E. coli* assembly ([[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]).
- A genome was assembled from a single cell of the marine SAR324 Deltaproteobacteria clade, with metabolic reconstruction indicating an aerobic, motile, chemotaxic organism ([[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]).
- On HG002, 20 scWGS cells plus 12 scNanoHi-C cells scaffolded with SALSA2 reached NG50 2.49 Mb, versus 1.34 Mb for 30 scWGS cells alone ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).
- Partial de novo assembly of human single-cell genomes from HiFi reads gave hifiasm primary assemblies of 598.3 Mb and 454.1 Mb (~19% and 15% of the reference), contig N50 of 35–42 kb, ~40 Mb of haplotype-alternative contigs, and 12.8% complete BUSCO genes in the best cell ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).

## Contested points

- **A generalisable lesson.** The claim that WGA's problems are computational rather than experimental ([[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]) recurs almost verbatim a decade later in the mosaic-variant-calling literature ([[10-Summaries/lahnemann-2021-natcomm|ProSolo]]; [[10-Summaries/ha-2023-natmethods|Ha 2023]]) (synthesis).
- **The same problem in another data type.** The abundance-inversion problem reappears as the allelic-imbalance problem that single-cell variant callers solve ([[10-Summaries/dong-2017-sccaller|SCcaller]]; [[10-Summaries/luquette-2019-natcomm|SCAN-SNV]]) (synthesis).
- **Why bacteria came first.** Bacterial single-cell genomics matured years before human single-cell variant calling because gene *presence* is far more robust to dropout than base-level genotype (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/mda|MDA]] — Isothermal φ29 amplification whose uneven coverage and chimeras created the assembly problem.
> - `concept` [[30-Concepts/scwga|scWGA]] — Amplifying the ~6 pg of a single cell's DNA for sequencing.
> - `concept` [[30-Concepts/scwga-chemistries|scWGA chemistries]] — How amplification chemistries trade uniformity, dropout and error.
> - `concept` [[30-Concepts/structural-variants|Structural variants]] — Large rearrangements that chimeras make hard to call in single cells.
> - `concept` [[30-Concepts/highly-repetitive-regions|Highly repetitive regions]] — Centromeres, telomeres and segmental duplications that short reads cannot resolve.
> - `hub` [[40-Topics/whole-genome-amplification|Whole-genome amplification]] — Methods that bridge single-cell DNA to sequencing input.

## All sources on this page

> [!info]- 10 summaries cited here
> - [[10-Summaries/bankevich-2012-spades|Bankevich 2012]]
> - [[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]
> - [[10-Summaries/dong-2017-sccaller|Dong 2017]]
> - [[10-Summaries/ha-2023-natmethods|Ha 2023]]
> - [[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]
> - [[10-Summaries/huang-2015-scwga-review|Huang & Xie 2015]]
> - [[10-Summaries/lahnemann-2021-natcomm|Lähnemann 2021]]
> - [[10-Summaries/li-2023-scnanohi-c|Li 2023]]
> - [[10-Summaries/luquette-2019-natcomm|Luquette 2019]]
> - [[10-Summaries/peng-2012-idba-ud|Peng 2012]]
