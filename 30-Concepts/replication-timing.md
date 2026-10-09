---
type: concept
title: Replication timing
aliases: [DNA replication timing, RT]
tags: [replication, S-phase, chromatin, scEdU-seq]
created: 2026-05-12
updated: 2026-10-08
---

# Replication timing

> The order in which different genomic regions are replicated during S phase. Active, gene-rich A compartments replicate early; repressive, gene-poor B compartments replicate late. Tightly correlated with chromatin state.

## Why it matters

- Late-replicating regions are enriched for heterochromatin marks (H3K9me3, H3K27me3) and lower CpG methylation.
- DNA methylation maintenance kinetics depend on replication timing: late-replicating, H3K9me3-marked regions take longest to recover methylation after replication ([[10-Summaries/geisenberger-2025-scepi2-seq]]).

## Added 2026-10-07

Late-replicating regions show more hemi-methylation in early-passage fibroblasts and substantial methylation loss after extended passage, consistent with incomplete maintenance remethylation ([[10-Summaries/spix-2025-scdeep-mc]]). S-phase cells can be identified without BrdU/EdU from read-count skew toward early-replicating regions plus allele-resolved methylation discordance ([[10-Summaries/spix-2025-scdeep-mc]]).

Somatic SNVs in single postmitotic PFC neurons were depleted from late-replicating domains and enriched in transcribed regions. Single PBMCs showed the opposite pattern (late-replication enrichment, transcribed-region depletion), which points to HSPC origin for blood-cell mutations and transcription-associated damage for neuronal ones ([[10-Summaries/xing-2021-meta-cs]]).


## Added 2026-10-08 — sequence models & foundation models

- GROVER's window embeddings, trained only on hg19 sequence, assign distinct territories to K562 replication timing and recover the anticorrelation between LINE orientation and replication direction ([[10-Summaries/sanabria-2024-grover]])

## Related

- [[30-Concepts/chromatin-compartments]] · [[30-Concepts/uhrf1]] · [[40-Topics/dna-methylation]] · [[40-Topics/chromatin-architecture]]
