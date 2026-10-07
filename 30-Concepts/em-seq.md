---
type: concept
title: "EM-seq (enzymatic methyl-seq)"
aliases: []
tags: []
created: 2026-10-07
updated: 2026-10-07
sources: ["[[10-Summaries/nichols-2025-scimetv3]]", "[[10-Summaries/spix-2025-scdeep-mc]]", "[[10-Summaries/vaisvila-2021-em-seq]]"]
---

# EM-seq (enzymatic methyl-seq)

> Bisulfite-free methylation sequencing in which TET2 oxidises 5mC and T4-BGT glucosylates 5hmC, protecting both, while APOBEC3A deaminates unmodified cytosines; the C/T readout matches bisulfite data ([[10-Summaries/vaisvila-2021-em-seq]]).

## Key points

- Higher library complexity, fewer duplicates and even GC coverage than adaptor-first WGBS; ~54 M of 56 M CpGs covered at 1× from 10–200 ng NA12878 DNA ([[10-Summaries/vaisvila-2021-em-seq]]).
- Works from 100 pg input and from cfDNA and FFPE DNA ([[10-Summaries/vaisvila-2021-em-seq]]).
- Does not separate 5mC from 5hmC without an auxiliary reaction; cannot read 5fC/5caC ([[10-Summaries/vaisvila-2021-em-seq]]).
- Offered as an alternative conversion in combinatorial-indexing single-cell methylation (sciMETv3) ([[10-Summaries/nichols-2025-scimetv3]]).
- In single-cell reprocessing, an enzymatic-conversion scWGBS method (Cabernet) showed incomplete CpY conversion in 43–49% of reads ([[10-Summaries/spix-2025-scdeep-mc]]).

## Related

- [[bisulfite-sequencing]] · [[taps]] · [[5hmc]] · [[tet-enzymes]] · [[40-Topics/dna-methylation]]
