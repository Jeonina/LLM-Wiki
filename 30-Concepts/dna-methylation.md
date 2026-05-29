---
type: concept
title: DNA methylation
aliases: [5mC, cytosine methylation, methylation]
tags: [epigenetics, methylation, regulation]
created: 2026-05-11
updated: 2026-05-19
---

# DNA methylation

> Covalent modification of the fifth carbon of cytosine to produce 5-methylcytosine (5mC), primarily at symmetric CpG dinucleotides in mammals ([[10-Summaries/smith-2013-methylation-development]]). The most stable and best-studied epigenetic mark, maintained through mitosis by DNMT1 ([[10-Summaries/kim-2017-methylation-memory-review]]) and globally reset during two developmental windows: pre-implantation and primordial germ cell specification ([[10-Summaries/smith-2013-methylation-development]]).

## Definition

In mammals, ~60–80% of the ~28 million CpG dinucleotides in the human genome are methylated ([[10-Summaries/smith-2013-methylation-development]]). Less than 10% of CpGs are in **CpG islands** — short (~200–2000 bp) regions of high CpG density at promoters of housekeeping and developmental genes, which are constitutively unmethylated ([[10-Summaries/smith-2013-methylation-development]]).

Other modification forms ([[10-Summaries/fu-2025-longread-methylation]]):
- **5-hydroxymethylcytosine (5hmC)** — TET-catalyzed oxidation intermediate; functional readout in some contexts ([[10-Summaries/fu-2025-longread-methylation]]; see also [[10-Summaries/bai-2024-simple-seq]] for joint 5mC/5hmC measurement).
- **N6-methyladenine (6mA)** — common in prokaryotes; rare in mammals ([[10-Summaries/fu-2025-longread-methylation]]).
- **N4-methylcytosine (4mC)** — prokaryotic ([[10-Summaries/fu-2025-longread-methylation]]).
- Non-CpG 5mC (mCpH) — found in brain and pluripotent cells ([[10-Summaries/fu-2025-longread-methylation]]).

## Why it matters

- **Stable propagation of cell identity** — methylation marks established during differentiation are maintained through mitosis, contributing to epigenetic memory ([[10-Summaries/kim-2017-methylation-memory-review]]; [[10-Summaries/kim-2017-methylation-memory-review]]).
- **Genomic imprinting and X-inactivation** — methylation establishes parent-of-origin and chromosome-of-origin gene-expression patterns ([[10-Summaries/smith-2013-methylation-development]]; imprinted loci established in primordial germ cells per [[10-Summaries/smith-2013-methylation-development]]).
- **Transposon silencing** — most repetitive elements are heavily methylated ([[10-Summaries/smith-2013-methylation-development]]); loss of methylation can derepress LINE-1, SINE, and ERV elements, triggering "viral mimicry" interferon responses ([[10-Summaries/hunt-2022-sctem-seq]]).
- **Disease biomarker** — cancer-associated promoter hypermethylation silences tumor suppressors; global hypomethylation enables oncogene activation and chromosome instability ([[10-Summaries/smith-2013-methylation-development]]).
- **Therapeutic target** — DNMT inhibitors (hypomethylating agents) are approved for MDS / AML ([[10-Summaries/hunt-2022-sctem-seq]]; [[10-Summaries/shen-2026-splicool-seq]] shows decitabine vs azacitidine produce divergent demethylation patterns).
- **Predicts and is predicted by chromatin accessibility** — methylation–accessibility coupling strengthens along differentiation ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018 scNMT-seq]]).
- **Largely independent of CNVs** — CNVs drive expression but do not propagate to local methylation state ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016 scTrio-seq]]).

## Variants and refinements

- **Measurement chemistries** ([[10-Summaries/fu-2025-longread-methylation]]):
  - **Bisulfite sequencing** — C→U→T conversion of unmethylated C; standard short-read assay. Suffers from three-base alignment problem ([[10-Summaries/fu-2025-longread-methylation]]).
  - **EM-seq / TAPS-seq** — enzymatic alternatives to bisulfite, less DNA damage ([[10-Summaries/fu-2025-longread-methylation]]).
  - **Long-read direct detection** — PacBio (kinetic features), Oxford Nanopore (current changes through nanopore). No base conversion; full alignment quality preserved in repeats and structural variants ([[10-Summaries/fu-2025-longread-methylation]]; [[10-Summaries/fu-2025-longread-methylation]]).
  - **Microarrays** — limited to pre-selected ~935,000 CpGs (synthesis; standard EPIC array specification).
- **Single-cell methylation** — scBS-seq, scRRBS, snmC-seq2, sciMETv2 are sparse but compatible with multi-omic combinations ([[10-Summaries/iqbal-2023-methylome-review]]).

## Contested points

- **5hmC function** — intermediate vs functional mark — partly unresolved ([[10-Summaries/fu-2025-longread-methylation]]; [[10-Summaries/bai-2024-simple-seq]]).
- **Methylation-calling accuracy across long-read platforms** — no community-standard benchmark ([[10-Summaries/fu-2025-longread-methylation]]).
- **Are HMAs (azacitidine, decitabine) interchangeable in the clinic?** Single-cell data argues no — they produce divergent demethylation patterns ([[10-Summaries/shen-2026-splicool-seq]]) and viral-mimicry response is decoupled from raw methylation loss ([[10-Summaries/hunt-2022-sctem-seq]]).

## Examples

- Cancer-associated hypermethylation of CDKN2A, MLH1, BRCA1 promoters ([[10-Summaries/smith-2013-methylation-development]]).
- X-inactivation: random monoallelic silencing maintained via methylation of XIST and downstream genes ([[10-Summaries/smith-2013-methylation-development]]).
- DNMT3A R882 mutations in clonal hematopoiesis perturb early progenitor states through selective hypomethylation ([[10-Summaries/nam-2022-natgenet]]).

## Related

- [[cpg-island]]
- [[dnmt]]
- [[tet-enzymes]]
- [[bisulfite-sequencing]]
- [[long-read-sequencing]]
- [[5hmc]]
- [[decitabine]]
- [[epigenetic-memory]]
- [[40-Topics/dna-methylation]]
- [[50-Notes/regulatory-layers-overview]] — methylation as one of the four molecular regulatory layers
