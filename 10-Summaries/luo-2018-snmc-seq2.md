---
type: summary
title: "Luo 2018 — snmC-seq2: robust single-cell DNA methylome profiling"
aliases: ["Luo 2018 snmC-seq2", "snmC-seq2"]
tags: [snmC-seq2, single-cell-methylome, bisulfite, post-bisulfite-adapter-tagging, Ecker-lab, methodology]
created: 2026-05-13
updated: 2026-05-13
sources: ["Chongyuan_2018_NatureCommunications.pdf"]
---

Luo, Rivkin, Zhou et al. (Ecker lab, Salk) reported **snmC-seq2**, an improved version of snmC-seq for single-cell DNA methylome profiling. Key changes: (i) shrimp alkaline phosphatase (SAP) treatment after random-primed DNA synthesis removes carryover dNTPs that contaminate Adaptase 3'-tagging; (ii) optimized random-primer concentration. These reduce adapter-dimer artefacts and improve reverse-read base composition. Net result: substantially higher mapping rates, lower artefactual reads, increased library complexity, and better coverage uniformity than snmC-seq. The method underpins the snmC-seq3 and snm3C-seq atlases of mouse brain methylome (Liu 2023, Mukamel 2025).

## Why this matters

Operational backbone of the Ecker-lab single-cell methylome program. Cited when describing methylome assay options alongside scBS-seq (Smallwood 2014), scRRBS (Guo 2013), scNMT-seq (Clark 2018), and sci-MET. Anchors §3.3 (methylome assays) and prerequisite for §5 brain-methylome work. The 2018 → snmC-seq3 (2023) → snm3C-seq (Liu 2023) → Mukamel 2025 lineage is the dominant brain-methylome production line.

## Related

- [[10-Summaries/clark-2018-scnmt]]
- [[10-Summaries/liu-2023-mouse-brain-methylome-3d]]
- [[10-Summaries/mukamel-2025-aneuploidy-brain]]
- [[20-Entities/joseph-ecker]]
- [[30-Concepts/scwgbs-methods]]
