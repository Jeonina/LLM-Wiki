---
type: concept
title: "DeChIC-seq (DNA Deaminase-based Chromatin Immuno-Conversion sequencing)"
aliases: [DeChIC-seq, scDeChIC-seq, DeChIC]
tags: []
created: 2026-10-07
updated: 2026-10-07
sources: ["[[10-Summaries/shi-2026-dechic-seq]]"]
---

# DeChIC-seq (DNA Deaminase-based Chromatin Immuno-Conversion sequencing)

> An antibody-tethered chromatin profiling method in which a protein A–DddA_tox fusion (pA-DddA) writes C→U edits (read as C→T) near antibody-bound histone marks or chromatin-associated proteins, so binding is recorded as a per-site conversion rate in a whole-genome library rather than by immunoprecipitation or fragment release ([[10-Summaries/shi-2026-dechic-seq]]).

## Definition

- Deaminase activity is repressed at pH 8.0 (Tris-HCl) during binding and reactivated at pH 6.4 (MES) for a 30-min conversion pulse ([[10-Summaries/shi-2026-dechic-seq]]).
- Signal is the fraction of converted reads at TC sites; peaks are differentially converted regions versus IgG or a simulated pseudo-IgG, called with Metilene ([[10-Summaries/shi-2026-dechic-seq]]).
- scDeChIC-seq couples the reaction to single-cell WGA built on META-CS transposons in an all-in-one-tube workflow ([[10-Summaries/shi-2026-dechic-seq]]).

## Why it matters

- Retains genome-wide background, giving near-proportional signal in cell-mixing series (R² 0.89/0.94 vs 0.70/0.84 for ChIP-seq) ([[10-Summaries/shi-2026-dechic-seq]]).
- Profiles TFs (CTCF, RAD21, NR5A2, TFAP2C, KLF5) from individual mouse blastomeres, with ~10,000 H3K4me3 peaks per cell ([[10-Summaries/shi-2026-dechic-seq]]).
- Limitations: TC-density dependence, weak contrast for H3K27me3/H3K9me3, one-cell-per-tube throughput ([[10-Summaries/shi-2026-dechic-seq]]).

## Related

- [[dd-seq]] · [[cut-and-run]] · [[cut-and-tag]] · [[meta-cs]] · [[damid]] · [[40-Topics/histone-modifications]]
