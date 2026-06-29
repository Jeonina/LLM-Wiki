---
type: concept
title: scTrio-seq
aliases: [scTrio-seq, single-cell triple omics sequencing]
tags: [joint-assay, triple-omics, single-cell-multiomics, scDNA, scRRBS, CNV, dna-methylation, foundational, method]
created: 2026-05-12
updated: 2026-05-12
---

# scTrio-seq

> First single-cell **triple-omics** assay: simultaneously yields copy-number variation (from RRBS read distribution), DNA methylome, and transcriptome from the same cell. Methodological landmark for **DNA + epigenome + transcriptome co-measurement at single-cell resolution** — the conceptual ancestor of the somatic-mosaicism × epigenome synthesis ([[40-Topics/somatic-mosaicism]]).

## Definition

Hou et al. 2016 ([[10-Summaries/hou-2016-sctrio-seq]]). Mild lysis breaks only the cytoplasm; centrifugation separates mRNA-bearing supernatant from the intact nucleus. Supernatant → Tang-lab scRNA-seq. Nuclear pellet → scRRBS. The RRBS read distribution doubles as the CNV signal (after normalization against normal-liver-RRBS reference and HMM fitting) at 10-Mb resolution.

## Why it matters

- **First demonstration that all three layers can be jointly read per cell** at acceptable depth: ~1.5M CpGs, ~6,179 genes, CNV at 10-Mb resolution.
- **CNVs drive expression dosage (r ≈ 0.68–0.73) but do NOT alter DNA methylation in the affected regions (r ≈ 0.05)** at single-cell resolution. This biological finding requires all three layers in the same cell — the wiki's anchor result for "mutation × epigenome × transcriptome at single-cell" reasoning.
- Promoter-methylation negatively correlates with expression; gene-body methylation positively correlates with expression (and the correlation increases toward the 3′ end) — first global demonstration of this distinction in single cells.
- **Applied to 25 HCC tumor cells**: identifies two subpopulations that cluster identically by CNV, methylation, *and* expression — and shows the minor subpopulation (subpop I) downregulates complement / innate-immunity pathways (likely immune-evasive).
- For the planned review's §4.6: scTrio-seq is the **triple-omics anchor** alongside scNMT-seq. The contrast — CNV (scTrio-seq) vs accessibility (scNMT-seq) — is the key axis to articulate when comparing DNA-anchored vs chromatin-anchored joint assays.

## Variants and refinements

- **scTrio-seq** ([[10-Summaries/hou-2016-sctrio-seq]]).
- Companion / contemporaneous: [[scnmt-seq]] (accessibility instead of CNV).
- Lineage cousin: [[gt-seq|G&T-seq]] (DNA + RNA only, no methylation).

## Contested points

- CNV resolution capped at ~10 Mb (limited by RRBS read distribution).
- Tumor-only demonstration; not yet applied to neuronal or developmental mosaicism.
- Does not capture point mutations directly — CNV-only on the DNA side. This is the gap the wiki's mosaicism + epigenome synthesis flags (somatic mosaicism#Mosaicism × epigenome — an open synthesis gap (synthesis)).

## Related

- [[scbs-seq]]
- [[40-Topics/dna-methylation]]
- [[40-Topics/single-cell-multiomics]]
- [[scnmt-seq]]
- [[gt-seq]]
- [[dr-seq]]
- [[40-Topics/somatic-mosaicism]]
- [[40-Topics/single-cell-multiomics]]
- [[40-Topics/dna-methylation]]
