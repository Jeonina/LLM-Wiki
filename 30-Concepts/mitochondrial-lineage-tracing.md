---
type: concept
title: Mitochondrial lineage tracing
aliases: [mtDNA lineage tracing, mtscATAC]
tags: [lineage-tracing, mtDNA, mosaicism]
created: 2026-05-12
updated: 2026-05-12
---

# Mitochondrial lineage tracing

> Using somatic mtDNA mutations — which accumulate at higher rates than nuclear DNA mutations and are present at hundreds-to-thousands of copies per cell — as natural barcodes for retrospective cell-lineage reconstruction in humans.

## Definition

mtDNA's high mutation rate and high copy number make it easier to detect somatic mutations from limited sequencing per cell. Methods include **mtscATAC-seq** (single-cell ATAC-seq with mtDNA recovery) and **EMBLEM** (epigenome and mitochondrial barcode of lineage from endogenous mutations).

## Why it matters

Provides a non-invasive, retrospective lineage system for human tissues where germline barcoding (CRISPR scarring) is unavailable. Particularly useful for hematopoietic clonal tracing where mtDNA mutations track cell lineages over decades.

## Examples

- Walker et al. 2020 NEJM used mtDNA mutations to track T-cell purifying selection.
- mtscATAC-seq used in clonal hematopoiesis studies; implemented in [[10-Summaries/ludwig-2020-mtscatac-seq]] and MAESTER ([[10-Summaries/miller-2022-maester]]); variant calling refined by scMitoMut ([[10-Summaries/sun-2025-scmitomut]]).

## Caveats

mtDNA's high copy number and random segregation between daughter cells mean only high-heteroplasmy variants persist robustly as labels, and some mutations may be under selection rather than neutral; hybridization capture recovers more variants but risks artifacts ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]). Despite few reliable variants per cell, mtDNA tracing succeeds when tissues undergo clonal expansion ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).

## Related

- [[30-Concepts/lineage-tracing]] · [[30-Concepts/mitochondrial-heteroplasmy]] · [[40-Topics/somatic-mosaicism]] · [[30-Concepts/phylogenetic-inference]]
- [[40-Topics/somatic-mosaicism]] · [[40-Topics/single-cell-lineage-tracing]]

## Added 2026-08-17

mtDNA is the **cheap** endogenous barcode: high copy number, mutation rate >10× the nuclear genome, and variants come along free with any scRNA-seq, scATAC-seq or scDNA-seq experiment — no deep whole-genome sequencing required, which is why mtDNA tracing scaled where nuclear-SNV tracing did not ([[10-Summaries/kwok-2022-mquad]]). (synthesis)

**The bottleneck is variant selection, not variant detection.** Most mtDNA variants are noise or non-clonal. [[10-Summaries/kwok-2022-mquad|MQuad]] fits each variant to a binomial with one shared allele frequency (H₀) versus a two-component mixture (H₁) and ranks by **ΔBIC**, with the cutoff set automatically at the knee of the cumulative ΔBIC curve ([[10-Summaries/kwok-2022-mquad]]).

**Nuclear callers fail structurally**: [[monovar|Monovar]] and Conbase assume a **diploid context** that the mitochondrial genome violates, so the binomial parameter must range freely from 0 to 1 to accommodate any heteroplasmy level ([[10-Summaries/kwok-2022-mquad]]). Benchmark on simulated Smart-seq2 data: AUPRC 0.976 (MQuad) vs 0.800 (mgatk) vs 0.147 (Monovar) — and the authors note AUROC is uninformative under 150-vs-16,000 class imbalance ([[10-Summaries/kwok-2022-mquad]]).

**Two hard limits.** Below **~1% allele frequency all tools fail**, because average technical noise sits at 0.44% — the boundary is set by chemistry, not statistics ([[10-Summaries/kwok-2022-mquad]]). And **linear evolution is the hardest topology**: when clones nest rather than branch, most variants are shared and carry little discriminative signal ([[10-Summaries/kwok-2022-mquad]]) — a point that generalises to every clonal-inference method. (synthesis)

Positioned as **complementary** to nuclear SNVs and CNVs rather than a replacement, giving finer clonal resolution in combination ([[10-Summaries/kwok-2022-mquad]]). Pipeline: cellSNP-lite → MQuad → vireoSNP.
