---
type: summary
title: "Geisenberger 2025 — scEpi²-seq: single-cell joint DNA methylation + histone modifications"
aliases: ["Geisenberger 2025 scEpi2-seq", "scEpi²-seq"]
tags: [scEpi2-seq, TAPS, sortChIC, histone-modification, DNA-methylation, FUCCI, cell-cycle, van-Oudenaarden-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Single-cell multi-omic detection of DNA methylation and histone modifications reconstructs the dynamics of epigenomic maintenance.md"]
---

Geisenberger, van den Berg, van Batenburg et al. (van Oudenaarden lab; Hubrecht) developed **scEpi²-seq** — joint single-cell histone modification (via pA-MNase tethered antibody, sortChIC-style) and DNA methylation (via TAPS bisulfite-free conversion). Single cells sorted into 384-well plates; MNase digestion + adapter ligation + TAPS conversion + library prep. Applied to K562, RPE-1 hTERT with FUCCI cell-cycle reporter, and mouse intestine. Revealed cell-cycle-dependent methylation dynamics driven by DNA replication: H3K9me3 chromatin shows slower re-methylation extending into G1, consistent with UHRF1-H3K9me3 maintenance pathway. In mouse intestine H3K27me3 + 5mC profiling: DMRs show methylation-independent cell-type regulation in addition to H3K27me3 regulation.

## Why this matters

The first robust single-cell joint histone + methylation method. Major §3.4 advance. Anchors any §6 future-perspective discussion of 4+ layer single-cell omics. Cell-cycle integration via FUCCI demonstrates dynamic methylation maintenance — directly relevant to mosaicism in dividing cells.

---
**Source:** [Open paper](https://www.nature.com/articles/s41592-025-02847-4)
## Related

- [[10-Summaries/tavares-2026-6base-cuttag]]
- [[10-Summaries/yeung-2023-scchix-seq]]
- [[10-Summaries/bai-2024-simple-seq]]
- [[10-Summaries/clark-2018-scnmt]]
