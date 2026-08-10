---
type: concept
title: Duplicate Marking
aliases: [PCR duplicate removal, deduplication]
tags: [alignment, amplification, QC, library-complexity]
created: 2026-08-10
updated: 2026-08-10
---

# Duplicate Marking

> Identifying reads that are PCR copies of the same original template rather than independent observations. The standard implementation is coordinate-based — reads sharing start and end positions are duplicates — and is available as a first-class utility in the SAM toolkit ([[li-2009-samtools]]).

## Why the definition depends on chemistry

Coordinate-based deduplication is **only valid when fragmentation precedes amplification**. Under whole-genome amplification, long amplicons are copied first and fragmented afterwards, so a single original region yields multiple inserts with non-overlapping coordinates that cannot be filtered as duplicates ([[zahn-2017-dlp]]). This is the mechanistic core of the argument for amplification-free single-cell library preparation, and it explains most of WGA's coverage pathology ([[zahn-2017-dlp]]).

Consequences observed in practice:

- C-DOP-L libraries carry high duplicate rates and need roughly twice the total reads for equivalent usable yield ([[zahn-2017-dlp]]).
- DOP-PCR coverage breadth **saturates** with deeper sequencing, making it unsuitable for SNV calling ([[zahn-2017-dlp]]).
- Peak callers remove redundant tags beyond what sequencing depth warrants (binomial *p* < 10⁻⁵) as an amplification-artefact control ([[zhang-2008-macs]]).
- **UMIs** provide the alternative solution — molecular identity carried in sequence rather than inferred from coordinates ([[chen-2018-fastp]]); see [[umi-molecular-barcoding]].

## Related

- [[scwga-chemistries]] · [[umi-molecular-barcoding]] · [[read-alignment]] · [[dlp-plus]]
