---
type: summary
title: "Mo 2023 — STAM-seq: single-molecule targeted accessibility + methylation in Arabidopsis"
aliases: ["Mo 2023 STAM-seq", "STAM-seq"]
tags: [STAM-seq, single-molecule, nanopore, EcoGII, adaptive-sampling, centromere, telomere, rDNA, Zhai-lab, Arabidopsis]
created: 2026-05-13
updated: 2026-05-13
sources: ["Single-molecule targeted accessibility and methylation sequencing of centromeres, telomeres and rDNAs in Arabidopsis.md"]
---

Mo, Shu, Liu et al. (Zhai lab) developed **STAM-seq** in Arabidopsis: nuclei isolation → EcoGII m6A methylation of accessible regions → nanopore long-read sequencing with **adaptive sampling** (real-time rejection of non-target sequences) → joint readout of 6mA (accessibility) and 5mC (endogenous methylation) on the same long read. Resolves highly repetitive regions (centromeres, telomeres, rDNAs) unmappable by short reads. 4.8× HRR enrichment via adaptive sampling. Revealed strand-asymmetric accessibility and methylation at CEN180 satellite repeats; negative accessibility-methylation correlation in rDNA units.

## Why this matters

A 2023 plant extension of the methyltransferase-footprinting family (SMAC/Fiber/SAMOSA/nanoNOMe). Important for showing the toolkit generalizes across kingdoms and for the **adaptive sampling** trick — targeted long-read sequencing without prior enrichment. Anchors §3.3 (SMF — adaptive sampling future direction).

---
**Source:** [Open paper](https://www.nature.com/articles/s41477-023-01498-7)
## Related

- [[10-Summaries/shipony-2020-smac]]
- [[10-Summaries/lee-2020-nanonome]]
- [[10-Summaries/wang-2019-mesmlr]]
- [[10-Summaries/bohaczuk-2024-targeted-fiberseq]]
