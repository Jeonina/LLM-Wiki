---
type: summary
title: "Izzo 2024 — GoT-ChA: mapping genotypes to chromatin accessibility in single cells"
aliases: ["Izzo 2024 GoT-ChA", "GoT-ChA", "Genotyping of Targeted loci with single-cell Chromatin Accessibility"]
tags: [GoT-ChA, genotyping, scATAC-seq, JAK2-V617F, CH, MPN, Landau-lab, NYGC, multimodal]
created: 2026-05-13
updated: 2026-05-13
sources: ["Franco_2024_Nature.pdf"]
---

Izzo, Myers, Ganesan, Mekerishvili et al. (Landau lab; NYGC + Weill Cornell) developed **GoT-ChA** (Genotyping of Targeted loci with single-cell Chromatin Accessibility), extending the GoT family to scATAC-seq. The platform adds custom GoT-ChA primers to the 10x Multiome droplet barcoding step, amplifying the targeted locus from genomic DNA (not from transcript, which avoids dependency on gene-expression level). Applied to CD34+ cells from patients with JAK2-V617F-mutated MPNs (PV, ET, MF), GoT-ChA revealed both **cell-intrinsic pro-inflammatory chromatin signatures** in mutant HSCs and a **distinct profibrotic inflammatory landscape** in mutant megakaryocytic progenitors. Integration with mitochondrial-genome profiling and cell-surface proteins extends the multimodal capture to DOGMA-seq + genotyping + chromatin + RNA + protein.

## Why this matters

Direct progression of GoT (Nam 2019) into the chromatin domain — solves the low expression problem (JAK2 is poorly expressed in some progenitor states, making GoT unreliable) by reading genomic DNA. Important §3.1/§5 anchor for CH/MPN applications. Demonstrates the practical multimodal stacking: genotype → chromatin → RNA → protein from the same single cell. Existing `izzo2024` bibkey present. Anchors the multimodal-genotyping arc: Nam GoT (2019) → Izzo GoT-ChA (2024) → future GoT-Multiome.

## Related

- [[10-Summaries/nam-2019-got]]
- [[10-Summaries/kriz-2025-duplex-multiome]]
- [[10-Summaries/miller-2022-maester]]
- [[20-Entities/dan-landau]]
- [[40-Topics/clonal-hematopoiesis]]
