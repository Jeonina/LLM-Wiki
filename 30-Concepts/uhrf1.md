---
type: concept
title: UHRF1
aliases: [Np95, ICBP90]
tags: [methylation-maintenance, DNMT1-cofactor, replication-fork]
created: 2026-05-12
updated: 2026-10-12
---

# UHRF1

> An obligate cofactor for DNMT1-mediated maintenance methylation. UHRF1 reads hemimethylated CpG sites via its SRA domain (after replication, the newly synthesized strand is unmethylated) and recruits DNMT1 to restore symmetric methylation.

> [!abstract] 한눈에
> UHRF1은 복제 직후의 hemimethylated CpG를 읽고 DNMT1을 불러와 methylation을 되살리는 필수 보조인자다. single-cell scWGBS에서는 막 복제된 구간의 중간 methylation 상태가 S기와 G2기를 거치며 줄어드는 모습으로 이 유지 과정이 직접 보인다 ([[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]).

## Why it matters

- Loss of UHRF1 causes genome-wide hypomethylation.
- UHRF1 also binds H3K9me3 (via TTD domain), coupling DNA methylation to heterochromatin.
- H3K9me3-marked late-replicating regions take longest to remethylate after S phase, which scEpi2-seq attributes to late replication timing rather than the histone mark per se ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]); a UHRF1-mediated contribution is (synthesis).
- Single-cell, allele- and strand-resolved scWGBS shows the maintenance intermediate directly: newly replicated (4n) regions in early S-phase carry high intermediate methylation that declines through S and G2 but remains above G1 levels ([[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/dnmt|DNMT]] — The DNA methyltransferases; DNMT1 maintains methylation through S phase.
> - `concept` [[30-Concepts/replication-timing|Replication timing]] — The order in which genomic regions replicate during S phase.
> - `concept` [[30-Concepts/epigenetic-memory|Epigenetic memory]] — Mitotically heritable record of past cell states in methylation and chromatin.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC at CpG dinucleotides, its maintenance, and how it is measured.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]
> - [[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]
