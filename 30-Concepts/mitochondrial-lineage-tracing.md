---
type: concept
title: Mitochondrial lineage tracing
aliases: [mtDNA lineage tracing, mtscATAC]
tags: [lineage-tracing, mtDNA, mosaicism]
created: 2026-05-12
updated: 2026-10-12
---

# Mitochondrial lineage tracing

> Using somatic mtDNA mutations — which accumulate at higher rates than nuclear DNA mutations and are present at hundreds-to-thousands of copies per cell — as natural barcodes for retrospective cell-lineage reconstruction in humans ([[10-Summaries/kwok-2022-mquad|MQuad]]; [[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).

> [!abstract] 한눈에
> 체세포 mtDNA 변이는 세포당 copy 수가 많고 변이율이 높아서, 사람 조직에서 계통을 거꾸로 추적하는 값싼 내재 barcode로 쓰인다 ([[10-Summaries/kwok-2022-mquad|MQuad]]). 다만 병목은 변이 검출이 아니라 정보가 있는 변이를 고르는 일이고, allele frequency 약 1% 아래에서는 모든 도구가 실패한다 ([[10-Summaries/kwok-2022-mquad|MQuad]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 계통 추적](../60-Explainers/single-cell-lineage-tracing.html)
<!-- /explainer-links -->

## Definition

mtDNA's high mutation rate and high copy number make it easier to detect somatic mutations from limited sequencing per cell ([[10-Summaries/kwok-2022-mquad|MQuad]]). Methods include **mtscATAC-seq** (single-cell ATAC-seq with mtDNA recovery) and **EMBLEM** (epigenome and mitochondrial barcode of lineage from endogenous mutations).

## Why it matters

- **A retrospective system for humans.** It provides a non-invasive, retrospective lineage system for human tissues where germline barcoding (CRISPR scarring) is unavailable. It is particularly useful for hematopoietic clonal tracing, where mtDNA mutations track cell lineages over decades.
- **The cheap endogenous barcode.** High copy number, a mutation rate >10× the nuclear genome, and variants that come along free with any scRNA-seq, scATAC-seq or scDNA-seq experiment mean no deep whole-genome sequencing is required ([[10-Summaries/kwok-2022-mquad|MQuad]]). This is why mtDNA tracing scaled where nuclear-SNV tracing did not (synthesis).
- **Complementary to nuclear markers.** It is positioned as complementary to nuclear SNVs and CNVs rather than a replacement, giving finer clonal resolution in combination ([[10-Summaries/kwok-2022-mquad|MQuad]]).

## Methods and callers

| Method | Readout | What it adds | Source |
|---|---|---|---|
| mtscATAC-seq with mgatk | Droplet-scale scATAC-seq with mtDNA recovery | mtDNA genotypes and chromatin from the same cells | ([[10-Summaries/ludwig-2020-mtscatac-seq\|mtscATAC-seq]]) |
| MAESTER | scRNA-seq | Mitochondrial variant enrichment from high-throughput scRNA-seq | ([[10-Summaries/miller-2022-maester\|MAESTER]]) |
| scMitoMut | Single-cell mtDNA variant calls | Refined variant calling | ([[10-Summaries/sun-2025-scmitomut\|scMitoMut]]) |
| MQuad | Per-cell variant counts | Variant selection: each variant is fit to a binomial with one shared allele frequency (H₀) versus a two-component mixture (H₁), ranked by ΔBIC, with the cutoff set automatically at the knee of the cumulative ΔBIC curve; pipeline cellSNP-lite → MQuad → vireoSNP | ([[10-Summaries/kwok-2022-mquad\|MQuad]]) |
| EMBLEM | Epigenome plus mtDNA | Epigenome and mitochondrial barcode of lineage from endogenous mutations | — |

## Evidence and examples

**Applications**

- Walker et al. 2020 NEJM used mtDNA mutations to track T-cell purifying selection.
- mtDNA lineage tracing has been used in clonal hematopoiesis studies ([[10-Summaries/ludwig-2020-mtscatac-seq|mtscATAC-seq]]; [[10-Summaries/miller-2022-maester|MAESTER]]).
- Despite few reliable variants per cell, mtDNA tracing succeeds when tissues undergo clonal expansion ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).

**Cross-contamination in droplets**

- Without formaldehyde fixation ~8.7% of droplet barcodes carried another cell's mtDNA variants; fixation cut cross-contamination ~3×, to 0.19% after doublet removal ([[10-Summaries/ludwig-2020-mtscatac-seq|mtscATAC-seq]]).

**Why nuclear callers fail**

- [[monovar|Monovar]] and Conbase assume a **diploid context** that the mitochondrial genome violates, so the binomial parameter must range freely from 0 to 1 to accommodate any heteroplasmy level ([[10-Summaries/kwok-2022-mquad|MQuad]]).
- Monovar also failed on mtscATAC data for a computational reason: a factorial of the maximum depth that overflows at mtDNA coverage ([[10-Summaries/ludwig-2020-mtscatac-seq|mtscATAC-seq]]).
- On simulated Smart-seq2 data, AUPRC was 0.976 for MQuad vs 0.800 for mgatk vs 0.147 for Monovar; the authors note AUROC is uninformative under 150-vs-16,000 class imbalance ([[10-Summaries/kwok-2022-mquad|MQuad]]).

## Contested points

- **Variant selection, not detection, is the bottleneck.** Most mtDNA variants are noise or non-clonal ([[10-Summaries/kwok-2022-mquad|MQuad]]).
- **Only some variants make durable labels.** mtDNA's high copy number and random segregation between daughter cells mean only high-heteroplasmy variants persist robustly as labels, and some mutations may be under selection rather than neutral ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).
- **Capture trades yield for artifacts.** Hybridization capture recovers more variants but risks artifacts ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).
- **A chemistry floor.** Below ~1% allele frequency all tools fail, because average technical noise sits at 0.44% — the boundary is set by chemistry, not statistics ([[10-Summaries/kwok-2022-mquad|MQuad]]).
- **Linear evolution is the hardest topology.** When clones nest rather than branch, most variants are shared and carry little discriminative signal ([[10-Summaries/kwok-2022-mquad|MQuad]]) — a point that generalises to every clonal-inference method (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/lineage-tracing|Lineage tracing]] — Reconstructing the developmental ancestry of cells in a tissue.
> - `concept` [[30-Concepts/mitochondrial-heteroplasmy|Mitochondrial heteroplasmy]] — Mixed mtDNA populations within one cell; the source of the barcodes.
> - `concept` [[30-Concepts/phylogenetic-inference|Phylogenetic inference]] — Reconstructing a cell-division tree from heritable markers.
> - `concept` [[30-Concepts/monovar|Monovar]] — Nuclear single-cell SNV caller whose diploid model fails on mtDNA.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct lineages within one organism.
> - `hub` [[40-Topics/single-cell-lineage-tracing|Single-cell lineage tracing]] — Methods that reconstruct the ancestry of individual cells.

## All sources on this page

> [!info]- 5 summaries cited here
> - [[10-Summaries/kwok-2022-mquad|Kwok 2022]]
> - [[10-Summaries/ludwig-2020-mtscatac-seq|Lareau & Ludwig 2021]]
> - [[10-Summaries/miller-2022-maester|Miller 2022]]
> - [[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]
> - [[10-Summaries/sun-2025-scmitomut|Sun 2025]]
