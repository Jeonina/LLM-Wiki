---
type: concept
title: scTrio-seq
aliases: [scTrio-seq, single-cell triple omics sequencing]
tags: [joint-assay, triple-omics, single-cell-multiomics, scDNA, scRRBS, CNV, dna-methylation, foundational, method]
created: 2026-05-12
updated: 2026-10-12
---

# scTrio-seq

> First single-cell **triple-omics** assay: simultaneously yields copy-number variation (from RRBS read distribution), DNA methylome, and transcriptome from the same cell ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]). Methodological landmark for **DNA + epigenome + transcriptome co-measurement at single-cell resolution** — the conceptual ancestor of the somatic-mosaicism × epigenome synthesis ([[40-Topics/somatic-mosaicism]]) (synthesis).

> [!abstract] 한눈에
> scTrio-seq는 한 세포에서 RRBS read 분포로 얻은 CNV, DNA methylome, transcriptome을 함께 읽은 첫 single-cell triple-omics assay다 ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]). CNV는 발현량을 바꾸지만 해당 구간의 methylation은 바꾸지 않는다는 결과가 대표적이며, DNA 쪽은 10 Mb 해상도의 CNV에 머문다 ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]).

## Definition

Hou et al. 2016 ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]):

- Mild lysis breaks only the cytoplasm; centrifugation separates the mRNA-bearing supernatant from the intact nucleus ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]).
- Supernatant → Tang-lab scRNA-seq; nuclear pellet → scRRBS ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]).
- The RRBS read distribution doubles as the CNV signal (after normalization against a normal-liver-RRBS reference and HMM fitting) at 10-Mb resolution ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]).

## Why it matters

- **First demonstration that all three layers can be jointly read per cell** at acceptable depth: ~1.5M CpGs, ~6,179 genes, CNV at 10-Mb resolution ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]).
- Its CNV × methylation × expression result requires all three layers in the same cell — the wiki's anchor result for "mutation × epigenome × transcriptome at single-cell" reasoning ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]).
- For the planned review's §4.6, scTrio-seq is the **triple-omics anchor** alongside scNMT-seq; the contrast — CNV (scTrio-seq) vs accessibility (scNMT-seq) — is the key axis to articulate when comparing DNA-anchored vs chromatin-anchored joint assays (synthesis).

## Variants and refinements

| Assay | Layers | Relation | Source |
|---|---|---|---|
| **scTrio-seq** | CNV + methylation + RNA | Original triple-omics assay | ([[10-Summaries/hou-2016-sctrio-seq\|Hou 2016]]) |
| [[scnmt-seq]] | Accessibility + methylation + RNA | Companion / contemporaneous; accessibility instead of CNV | (synthesis) |
| [[gt-seq\|G&T-seq]] | DNA + RNA | Lineage cousin; no methylation | (synthesis) |

## Evidence and examples

- **CNVs drive expression dosage (r ≈ 0.68–0.73) but do NOT alter DNA methylation in the affected regions (r ≈ 0.05)** at single-cell resolution ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]).
- Promoter methylation negatively correlates with expression; gene-body methylation positively correlates with expression, and the correlation increases toward the 3′ end — the first global demonstration of this distinction in single cells ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]).
- **Applied to 25 HCC tumor cells**, scTrio-seq identifies two subpopulations that cluster identically by CNV, methylation, *and* expression ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]).
- The minor subpopulation (subpop I) downregulates complement / innate-immunity pathways (likely immune-evasive) ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]).

## Contested points

- CNV resolution is capped at ~10 Mb, limited by the RRBS read distribution ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]).
- Tumor-only demonstration; not yet applied to neuronal or developmental mosaicism (synthesis).
- Does not capture point mutations directly — CNV-only on the DNA side. This is the gap the wiki's mosaicism + epigenome synthesis flags (see "Mosaicism × epigenome — an open gap" on [[40-Topics/somatic-mosaicism]]) (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/scnmt-seq|scNMT-seq]] — Triple-omics with accessibility instead of CNV.
> - `concept` [[30-Concepts/gt-seq|G&T-seq]] — Physical separation of genome and transcriptome from one cell.
> - `concept` [[30-Concepts/dr-seq|DR-seq]] — Joint genome and transcriptome sequencing from one cell.
> - `concept` [[30-Concepts/scbs-seq|scBS-seq]] — Single-cell bisulfite sequencing of the methylome.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Post-zygotic variation between cells of one body.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — Methylation chemistry, assays and analysis.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Joint measurement of several layers in one cell.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]
