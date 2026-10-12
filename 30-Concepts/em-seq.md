---
type: concept
title: "EM-seq (enzymatic methyl-seq)"
aliases: []
tags: []
created: 2026-10-07
updated: 2026-10-12
sources: ["[[10-Summaries/nichols-2025-scimetv3]]", "[[10-Summaries/spix-2025-scdeep-mc]]", "[[10-Summaries/vaisvila-2021-em-seq]]"]
---

# EM-seq (enzymatic methyl-seq)

> Bisulfite-free methylation sequencing in which TET2 oxidises 5mC and T4-BGT glucosylates 5hmC, protecting both, while APOBEC3A deaminates unmodified cytosines; the C/T readout matches bisulfite data ([[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]).

> [!abstract] 한눈에
> EM-seq는 bisulfite 대신 TET2·T4-BGT로 5mC와 5hmC를 보호하고 APOBEC3A로 나머지 cytosine을 탈아미노화하는 효소 기반 methylation sequencing으로, 결과는 bisulfite 데이터와 같은 C/T readout이다 ([[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]). 5mC와 5hmC를 따로 구분하지는 못한다 ([[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]).

## Key points

- Higher library complexity, fewer duplicates and even GC coverage than adaptor-first WGBS; ~54 M of 56 M CpGs covered at 1× from 10–200 ng NA12878 DNA ([[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]).
- Works from 100 pg input and from cfDNA and FFPE DNA ([[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]).
- Does not separate 5mC from 5hmC without an auxiliary reaction; cannot read 5fC/5caC ([[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]).
- Offered as an alternative conversion in combinatorial-indexing single-cell methylation (sciMETv3) ([[10-Summaries/nichols-2025-scimetv3|sciMETv3]]).
- In single-cell reprocessing, an enzymatic-conversion scWGBS method (Cabernet) showed incomplete CpY conversion in 43–49% of reads ([[10-Summaries/spix-2025-scdeep-mc|scDEEP-mC]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/bisulfite-sequencing|Bisulfite sequencing]] — The standard chemistry EM-seq replaces: unmethylated C reads as T.
> - `concept` [[30-Concepts/taps|TAPS]] — Bisulfite-free chemistry that converts 5mC itself rather than unmodified C.
> - `concept` [[30-Concepts/5hmc|5hmC]] — The oxidative intermediate EM-seq protects but does not separate from 5mC.
> - `concept` [[30-Concepts/tet-enzymes|TET enzymes]] — Dioxygenases that oxidize 5mC; TET2 is EM-seq's protection step.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5-methylcytosine, predominantly at CpG, and how it is measured.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/nichols-2025-scimetv3|Nichols 2025]]
> - [[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]
> - [[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]
