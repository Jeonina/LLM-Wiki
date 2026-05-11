---
type: concept
title: DNA methylation
aliases: [5mC, cytosine methylation, methylation]
tags: [epigenetics, methylation, regulation]
created: 2026-05-11
updated: 2026-05-11
---

# DNA methylation

> Covalent modification of the fifth carbon of cytosine to produce 5-methylcytosine (5mC), primarily at symmetric CpG dinucleotides in mammals. The most stable and best-studied epigenetic mark, maintained through mitosis by DNMT1 and globally reset during two developmental windows (pre-implantation and primordial germ cell specification).

## Definition

In mammals, ~60–80% of the ~28 million CpG dinucleotides in the human genome are methylated ([[10-Summaries/zachary-2013-naturereviewsgenetics]]). Less than 10% of CpGs are in **CpG islands** — short (~200–2000 bp) regions of high CpG density at promoters of housekeeping and developmental genes, which are constitutively unmethylated.

Other modification forms ([[10-Summaries/yilei-2025-naturereviewsgenetics]]):
- **5-hydroxymethylcytosine (5hmC)** — TET-catalyzed oxidation intermediate; functional readout in some contexts.
- **N6-methyladenine (6mA)** — common in prokaryotes; rare in mammals.
- **N4-methylcytosine (4mC)** — prokaryotic.
- Non-CpG 5mC (mCpH) — found in brain and pluripotent cells.

## Why it matters

- **Stable propagation of cell identity** — methylation marks established during differentiation are maintained through mitosis, contributing to epigenetic memory.
- **Genomic imprinting and X-inactivation** — methylation establishes parent-of-origin and chromosome-of-origin gene-expression patterns.
- **Transposon silencing** — most repetitive elements are heavily methylated.
- **Disease biomarker** — cancer-associated promoter hypermethylation (tumor suppressors) and global hypomethylation (oncogene activation, chromosome instability).
- **Therapeutic target** — DNMT inhibitors are approved for MDS / AML.

## Variants and refinements

- **Measurement chemistries** ([[10-Summaries/yilei-2025-naturereviewsgenetics]]):
  - **Bisulfite sequencing** — C→U→T conversion of unmethylated C; standard short-read assay. Suffers from three-base alignment problem.
  - **EM-seq / TAPS-seq** — enzymatic alternatives to bisulfite, less DNA damage.
  - **Long-read direct detection** — PacBio (kinetic features), Oxford Nanopore (current changes through nanopore). No base conversion; full alignment quality preserved in repeats and structural variants.
  - **Microarrays** — limited to pre-selected ~935,000 CpGs.
- **Single-cell methylation** — snmC-seq, methylC-seq; sparse but compatible with multi-omic combinations.

## Contested points

- 5hmC function — intermediate vs functional mark — partly unresolved.
- Methylation-calling accuracy across long-read platforms — no community-standard benchmark.

## Examples

- Cancer-associated hypermethylation of CDKN2A, MLH1, BRCA1 promoters ([[10-Summaries/zachary-2013-naturereviewsgenetics]]).
- X-inactivation: random monoallelic silencing maintained via methylation of XIST and downstream genes.

## Related

- [[cpg-island]]
- [[dnmt]]
- [[tet-enzymes]]
- [[bisulfite-sequencing]]
- [[long-read-sequencing]]
- [[40-Topics/dna-methylation]]
