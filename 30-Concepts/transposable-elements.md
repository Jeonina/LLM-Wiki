---
type: concept
title: Transposable elements
aliases: [TEs, retrotransposons, LINE-1, SINE Alu, ERVs]
tags: [genome, repeats, retrotransposition, methylation]
created: 2026-05-12
updated: 2026-10-07
---

# Transposable elements (TEs)

> DNA sequences that can replicate and insert themselves at new genomic locations. Comprise ~50% of the human genome. Most are inactive relics; some — particularly LINE-1, SINE Alu, and a few ERVs — remain "hot" and can still mobilize.

## Definition

Major families:
- **LINE-1 (L1)**: ~17% of human genome; full-length L1Hs elements can autonomously retrotranspose.
- **SINE Alu**: ~11% of human genome; uses LINE-1 machinery for retrotransposition.
- **ERVs** (endogenous retroviruses): ~8% of genome; mostly inactive but some encode functional Env proteins.

## Why it matters

- TEs are kept silenced by DNA methylation (especially at internal promoters) and H3K9me3 heterochromatin.
- Loss of TE silencing in cancer triggers [[30-Concepts/viral-mimicry]] innate immune responses.
- L1 retrotransposition in neurons contributes to somatic genomic mosaicism (synthesis).
- TE methylation serves as a surrogate for global methylation status (basis of [[30-Concepts/sctem-seq]]).

## Added 2026-10-07

Long-read scATAC resolves accessibility of individual repeat copies: 157 of 16,882 full-length LINE1s are activated from zygote to morula, 4.3-fold enriched in the A compartment, and LINE1 or MERVL copies with >98% identity can differ in accessibility, which short reads cannot resolve ([[10-Summaries/li-2025-scnanoatac-seq2]]).

Long-read single-cell CUT&Tag resolves histone marks on individual transposable-element copies: 96.5% mappability/discernibility for 320 full-length L1Hs elements with >99% pairwise identity, and K562 cells treated with 5-azacytidine gained H3K27ac on 201 individual repeats, all of the 102 checked having lost DNA methylation ([[10-Summaries/li-2024-scnanoseq-cut-tag]]). H3K4me3-marked L1Md elements peaked at the Sperm1 stage of mouse spermatogenesis ([[10-Summaries/li-2024-scnanoseq-cut-tag]]).


## Related

- [[40-Topics/dna-methylation]] · [[30-Concepts/sctem-seq]] · [[30-Concepts/viral-mimicry]] · [[40-Topics/somatic-mosaicism]]
