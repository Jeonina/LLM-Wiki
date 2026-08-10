---
type: summary
title: "Ludwig et al. 2019 — Lineage tracing in humans enabled by mitochondrial mutations and single-cell genomics"
source: "[[00-Sources/papers/Lineage Tracing in Humans Enabled by Mitochondrial Mutations and Single-Cell Genomics]]"
source_kind: paper
author: "Leif S. Ludwig, Caleb A. Lareau, Jacob C. Ulirsch, ... Aviv Regev, Vijay G. Sankaran (corresponding)"
published: 2019-03-07
ingested: 2026-08-10
doi: "10.1016/j.cell.2019.01.022"
journal: "Cell"
tags: [mtDNA, lineage-tracing, heteroplasmy, natural-barcode, scATAC-seq, clonal-architecture, mtscATAC]
entities: ["[[aviv-regev]]"]
concepts: ["[[lineage-tracing]]", "[[mitochondrial-heteroplasmy]]", "[[scatac-seq]]", "[[clonal-hematopoiesis]]", "[[copy-number-variation]]", "[[multimodal-integration-methods]]"]
topics: ["[[single-cell-lineage-tracing]]", "[[single-cell-multiomics]]", "[[somatic-mosaicism]]"]
---

**Citation:** Ludwig et al. (2019) — *Lineage tracing in humans enabled by mitochondrial mutations and single-cell genomics* — *Cell* 176, 1325–1339.e22. [DOI](https://doi.org/10.1016/j.cell.2019.01.022)

# Ludwig 2019 — mtDNA as a natural barcode

> Engineered lineage barcodes cannot be introduced into a living human. This paper's move is to notice that one already exists: somatic **mtDNA mutations**, which every scATAC-seq and scRNA-seq run already captures as a by-product and routinely discards. Heteroplasmic mtDNA variants are shown to be reliably detectable, stably heritable, and sufficient to reconstruct clonal relationships — while the same read set reports cell state.

## Key claims

- **Why mtDNA works as a barcode**, argued from first principles: the genome is 16.6 kb (cheap to cover deeply), the mutation rate is **10–100× higher than nuclear DNA**, copy number is 100–1,000s per cell, and vegetative segregation with genetic drift and relaxed replication drives variants to **high heteroplasmy** — so a mutation reaches detectable allele fractions rather than staying at 1/N.
- The by-product argument is quantitative: ATAC-seq covered the mitochondrial genome at **3,380-fold per million mapped reads** with no mtDNA enrichment step.
- **Ground truth by construction.** 65 sub-clonal TF1 populations were derived over **8 generations** of iterative single-cell bottlenecks (~3 weeks each) to build an experimental lineage tree, then profiled by ATAC-seq. Clone- and sub-clone-specific mutations were stably propagated; new mutations arising mid-experiment were also stably transmitted. Hierarchical clustering recovered the most recent common ancestor at **96% accuracy between first-generation clones and 79% within sub-clones**.
- Most mutations were **C>T transitions**, consistent across the cell-line, tissue and GTEx analyses.
- **Detection works across assays.** Full-length scRNA-seq covers mtDNA better than 3′-end protocols; heteroplasmy estimates from scRNA-seq agree with whole-genome sequencing of the same cell; scATAC-seq and a purpose-built rolling-circle scMito-seq give the deepest and most uniform coverage. Across all methods, the known clonal allele was detected in **95.4% (210/220) of cells**.
- **Benchmarked against an exogenous gold standard.** Lentiviral 30-bp barcodes assigned 158 cells to 11 non-overlapping groups; 20 quality-filtered mtDNA variants recovered that structure with **AUROC 0.96 / AUPRC 0.84**, and a trio analysis was 95% accurate. Critically, mtDNA outperformed **CNVs inferred from scRNA-seq** as a clonality measure.
- **Lineage plus state, from one assay.** Pairing mtDNA-inferred clonal relatedness with chromatin accessibility, a random-effects variance decomposition found **8,570 of 91,607 ATAC peaks with >90% of variance explained by clone** — i.e. heritable chromatin features.
- **Population-scale diversity**: 8,820 GTEx bulk RNA-seq samples across 49 tissues yielded **2,762 donor-specific, tissue-specific mutations at ≥3% heteroplasmy**, establishing that the required variation exists broadly in humans.

## Methods / evidence

The validation stack is unusually complete: a constructed ground-truth tree, an orthogonal exogenous barcode benchmark, cross-assay concordance (bulk/single-cell × ATAC/RNA/mito-seq), per-base per-allele base-quality-aware variant calling, and reproducibility across sequencing runs. Applications extend to native hematopoiesis, T lymphocytes, chronic myeloid leukemia and colon cancer.

Stated artefact controls: scRNA-derived variants were filtered against bulk ATAC allele frequencies (>0.5%) and base-quality scores, because several highly heteroplasmic RNA-only variants reflect **RNA editing** (one previously validated at 2,619 A>G) or transcription/technical error.

## Surprising or load-bearing bits

- **The data was always there.** Mitochondrial reads are treated as contamination in essentially every single-cell protocol; this paper reframes the same reads as the lineage channel. That makes retrospective lineage tracing possible on **already-published datasets** — no new experiment, no genetic manipulation, and therefore applicable to humans where all engineered approaches are unavailable.
- **mtDNA beats inferred CNV for clonality.** This is a direct comparison against the method most commonly used to infer clonal structure from single-cell transcriptomes ([[tickle-2019-infercnv|inferCNV]], [[gao-2021-copykat|CopyKAT]]) and it favours mtDNA — a result that should inform tool choice whenever mtDNA coverage is adequate.
- **8,570 clonally heritable chromatin peaks** is the strongest claim in the paper and the least expected: chromatin state is transmitted along lineage strongly enough to be measured as heritability, in a cell line, over eight generations. It makes clone a legitimate covariate in any accessibility analysis.
- The **heteroplasmy mechanism is the enabling condition, not a detail.** Nuclear somatic mutations sit at one or two copies per cell and are lost to dropout; an mtDNA variant drifting to 20–80% heteroplasmy across hundreds of genome copies is robustly detectable at shallow depth. This is why mtDNA lineage tracing works where nuclear single-cell SNV calling struggles ([[xu-2012-single-cell-exome-kidney]]).
- The RNA-only variant problem is the flip side: **RNA editing and transcription error masquerade as heteroplasmy** in scRNA-seq, so DNA-based (ATAC or mito-seq) confirmation is not optional for scRNA-derived calls.
- Because mutation accumulation is stochastic and drift-driven, resolution is uneven across a tree — deep relationships resolved at 96% but sub-clonal ones at 79% in the best-case cell-line setting.

## Entities mentioned

- [[aviv-regev]] — co-corresponding; connects this to the broader single-cell atlas program.

## Concepts touched

- [[lineage-tracing]] — this is the founding source for endogenous mtDNA barcoding in humans.
- [[mitochondrial-heteroplasmy]] — heteroplasmy, drift and relaxed replication as the properties that make the barcode work.
- [[scatac-seq]] — the assay that both carries the barcode and reports the state.

## Connections to other sources

- Contrasts with engineered barcoding and CRISPR-scar tracing ([[jones-2020-cassiopeia]] on the reconstruction algorithms; [[lineage-tracing]] for the taxonomy).
- Outperforms transcriptome-inferred CNV clonality: [[tickle-2019-infercnv]], [[gao-2021-copykat]].
- Nuclear-SNV alternative and its limits: [[xu-2012-single-cell-exome-kidney]], [[gonzalez-pena-2021-pnas]].
- Multimodal framing: [[zhu-2020-multimodal-power-of-many]], [[argelaguet-2021-integration-principles]].

## Open questions

- **Resolution depends on mutation availability per lineage** — a clone with no private mtDNA variant is invisible, and the paper's own accuracy figures (79% within sub-clones) show where this bites. There is no way to know in advance whether a given tissue has enough variation.
- Whether mtDNA mutations are strictly neutral markers, or whether some are under selection (particularly in tissues with high oxidative demand), is not settled here — a selected variant would distort tree topology.
- Whether the clonal heritability of chromatin peaks seen in a cell line holds in primary tissue over longer timescales is untested.

## Related

- [[lineage-tracing]] · [[mitochondrial-heteroplasmy]] · [[single-cell-lineage-tracing]] · [[jones-2020-cassiopeia]]
