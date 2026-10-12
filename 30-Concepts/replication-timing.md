---
type: concept
title: Replication timing
aliases: [DNA replication timing, RT]
tags: [replication, S-phase, chromatin, scEdU-seq]
created: 2026-05-12
updated: 2026-10-12
---

# Replication timing

> The order in which different genomic regions are replicated during S phase. Active, gene-rich A compartments replicate early; repressive, gene-poor B compartments replicate late. Tightly correlated with chromatin state.

> [!abstract] 한눈에
> Replication timing은 S phase 동안 유전체 구간이 복제되는 순서이고, 늦게 복제되는 구간일수록 복제 후 methylation 회복이 느리다 ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]; [[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]). single-cell 데이터에서는 early-replicating 구간으로 쏠린 read 수만으로도 S-phase 세포를 가려낼 수 있다 ([[10-Summaries/schneider-2024-scabsolute|scAbsolute]]).

## Why it matters

- Late-replicating regions are enriched for heterochromatin marks (H3K9me3, H3K27me3) and lower CpG methylation.
- DNA methylation maintenance kinetics depend on replication timing: late-replicating, H3K9me3-marked regions take longest to recover methylation after replication ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).

## Reading replication state from single cells

- **Read-count skew plus methylation discordance.** S-phase cells can be identified without BrdU/EdU from read-count skew toward early-replicating regions plus allele-resolved methylation discordance ([[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]).
- **A 'cycling activity' statistic in shallow scWGS.** scAbsolute flags S-phase cells with the length-weighted median of per-segment partial Spearman trends of read counts against ENCODE Repli-chip replication time, controlling for GC and mappability ([[10-Summaries/schneider-2024-scabsolute|scAbsolute]]).
- **Sequence alone.** GROVER's window embeddings, trained only on hg19 sequence, assign distinct territories to K562 replication timing ([[10-Summaries/sanabria-2024-grover|GROVER]]).

## Evidence and examples

- Late-replicating regions show more hemi-methylation in early-passage fibroblasts and substantial methylation loss after extended passage, consistent with incomplete maintenance remethylation ([[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]).
- The unsupervised scAbsolute S-phase classifier reached 86% accuracy on DLP+ data and 89% on FUCCI-sorted PEO1 G1/S cells, against 71% for an early PERT release; a four-feature random forest reached 92% against 90% for the original Laks et al. classifier ([[10-Summaries/schneider-2024-scabsolute|scAbsolute]]).
- Somatic SNVs in single postmitotic PFC neurons were depleted from late-replicating domains and enriched in transcribed regions. Single PBMCs showed the opposite pattern (late-replication enrichment, transcribed-region depletion), which points to HSPC origin for blood-cell mutations and transcription-associated damage for neuronal ones ([[10-Summaries/xing-2021-meta-cs|Xing 2021]]).
- GROVER recovers the anticorrelation between LINE orientation and replication direction ([[10-Summaries/sanabria-2024-grover|GROVER]]).

## Open questions

- **Replication state as a hidden confounder.** S/G2 cells carry transient intermediate methylation from not-yet-maintained daughter strands, which at low coverage would look like epigenetic heterogeneity ([[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]) (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/chromatin-compartments|Chromatin compartments]] — A (early-replicating, active) and B (gene-poor) blocks that associate in 3D.
> - `concept` [[30-Concepts/uhrf1|UHRF1]] — DNMT1 cofactor that reads hemimethylated CpGs after replication.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC at CpG dinucleotides and how single cells measure it.
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — How DNA is packaged along chromosomes and across cells.

## All sources on this page

> [!info]- 5 summaries cited here
> - [[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]
> - [[10-Summaries/sanabria-2024-grover|GROVER 2024]]
> - [[10-Summaries/schneider-2024-scabsolute|Schneider 2024]]
> - [[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]
> - [[10-Summaries/xing-2021-meta-cs|Xing 2021]]
