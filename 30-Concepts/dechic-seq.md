---
type: concept
title: "DeChIC-seq (DNA Deaminase-based Chromatin Immuno-Conversion sequencing)"
aliases: [DeChIC-seq, scDeChIC-seq, DeChIC]
tags: []
created: 2026-10-07
updated: 2026-10-12
sources: ["[[10-Summaries/shi-2026-dechic-seq]]"]
---

# DeChIC-seq (DNA Deaminase-based Chromatin Immuno-Conversion sequencing)

> An antibody-tethered chromatin profiling method in which a protein A–DddA_tox fusion (pA-DddA) writes C→U edits (read as C→T) near antibody-bound histone marks or chromatin-associated proteins, so binding is recorded as a per-site conversion rate in a whole-genome library rather than by immunoprecipitation or fragment release ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]).

> [!abstract] 한눈에
> DeChIC-seq는 항체로 붙인 pA-DddA가 결합 부위 근처의 C를 T로 바꾸게 하고, 그 전환율을 whole-genome library에서 읽어 histone mark와 TF 결합을 기록한다 ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]). 생쥐 blastomere 하나에서도 TF를 프로파일링할 수 있지만, TC 밀도에 의존하고 한 tube에 한 세포만 처리한다 ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]).

## Definition

- Deaminase activity is repressed at pH 8.0 (Tris-HCl) during binding and reactivated at pH 6.4 (MES) for a 30-min conversion pulse ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]).
- Signal is the fraction of converted reads at TC sites; peaks are differentially converted regions versus IgG or a simulated pseudo-IgG, called with Metilene ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]).
- scDeChIC-seq couples the reaction to single-cell WGA built on META-CS transposons in an all-in-one-tube workflow ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]).

## Why it matters

- Retains genome-wide background, giving near-proportional signal in cell-mixing series (R² 0.89/0.94 vs 0.70/0.84 for ChIP-seq) ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]).
- Profiles TFs (CTCF, RAD21, NR5A2, TFAP2C, KLF5) from individual mouse blastomeres, with ~10,000 H3K4me3 peaks per cell ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]).
- Limitations: TC-density dependence, weak contrast for H3K27me3/H3K9me3, one-cell-per-tube throughput ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/dd-seq|D&D-seq]] — Sibling antibody-tethered DddA method using a split nanobody–DddA.
> - `concept` [[30-Concepts/cut-and-run|CUT&RUN]] — Antibody-tethered MNase that releases target fragments.
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — Antibody-tethered Tn5 profiling.
> - `concept` [[30-Concepts/meta-cs|META-CS]] — The transposon WGA used for single-cell DeChIC-seq.
> - `concept` [[30-Concepts/damid|DamID]] — Tethered-enzyme ancestor limited to GATC sites.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone marks and the methods that profile them in single cells.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/shi-2026-dechic-seq|Shi 2026]]
