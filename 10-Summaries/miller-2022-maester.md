---
type: summary
title: "Miller 2022 — Mitochondrial variant enrichment from high-throughput single-cell RNA sequencing resolves clonal populations (MAESTER)"
aliases: ["Miller 2022 MAESTER", "MAESTER", "maegatk"]
tags: [MAESTER, mtDNA, lineage-tracing, scRNA-seq, clonal-hematopoiesis, vanGalen-lab, Sankaran-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Tyler_2022_NatureBiotechnology.pdf"]
---

Miller, Lareau, Verga, DePasquale, Liu, Szabo, Sandor, Yin, Ludwig, El Farran, Morgan, Satpathy, Griffin, Lane, Love, Bernstein, Sankaran and van Galen (Mass General, Broad, Dana-Farber) developed **MAESTER** (Mitochondrial Alteration Enrichment from Single-cell Transcriptomes to Establish Relatedness). The method targets mtDNA-derived transcripts using primer panels covering all 15 mtDNA-encoded mRNAs in standard 3′ scRNA-seq libraries (10x Genomics, Seq-Well), increasing mitochondrial coverage by 50–217-fold compared to unenriched scRNA-seq.

Computational toolkit: **maegatk** uses UMIs to build consensus per starting mtRNA molecule and calls heteroplasmic variants at single-cell resolution. Applied to a chronic myelogenous leukemia (K562) + brain-tumor (BT142) mixing experiment, MAESTER recovered six homoplasmic distinguishing variants with 100% concordance to mRNA-based identity. Applied to clonal hematopoiesis from a patient bone marrow with BPDCN, MAESTER resolved 23 clones from 26 informative mtDNA variants, with paired TCR-seq (TREK-seq) validating clonality (ARI = 0.74 with mtDNA clones).

## Why this matters

The high-throughput cousin of mtscATAC-seq (Lareau 2021): brings mtDNA-based lineage tracing into mainstream 3′ scRNA-seq workflows, which dominate cohort-scale studies. Anchors §3.1 (mtDNA as native molecular barcode) and §5 (clonal hematopoiesis applications). Important methodological point for the review: lineage tracing now coexists at scale with transcriptomic state readout in the same single cells — but achieving the same with *nuclear* somatic SNVs at scale remains unsolved.

## Related

- [[10-Summaries/lareau-2021-natbiotech]]
- [[10-Summaries/ludwig-2019-cell]]
- [[30-Concepts/mtDNA-lineage-tracing]]
