---
type: summary
title: "Ji et al. 2017 — Single-cell regulome data analysis by SCRAT"
source: "[[00-Sources/papers/Single-cell regulome data analysis by SCRAT]]"
source_quality: full
source_sha256: "76e50e175ad93cb4fc71937f43dd4af377f5b6d2470ba5fdd19b0b2e07b7f208"
source_kind: paper
author: "Zhicheng Ji, Weiqiang Zhou, Hongkai Ji (corresponding)"
published: 2017-09-15
ingested: 2026-10-07
doi: "10.1093/bioinformatics/btx315"
journal: "Bioinformatics 33(18):2930-2932"
tags: [SCRAT, scATAC-seq, scDNase-seq, scChIP-seq, feature-aggregation, motif, gene-sets, ENCODE, clustering, cell-type-annotation, GUI, R-package, application-note]
entities: []
concepts: ["[[scatac-seq]]", "[[chromatin-accessibility]]", "[[transcription-factor-motif]]", "[[clustering-algorithms]]", "[[cell-type-annotation]]", "[[dnase-seq]]", "[[dimensionality-reduction]]"]
topics: ["[[single-cell-atac-seq]]", "[[computational-methods]]"]
---

**Citation:** Ji et al. (2017) — *Single-cell regulome data analysis by SCRAT* — *Bioinformatics* 33:2930–2932. [DOI](https://doi.org/10.1093/bioinformatics/btx315)

# Ji 2017 — SCRAT

> Single-cell regulome data (scATAC-seq, scDNase-seq, scChIP-seq) are so sparse that each locus is nearly binary, so per-peak analysis fails. **SCRAT** (Single-Cell Regulome Analysis Toolbox) is an early, GUI-driven R package/web app that **aggregates reads over biologically grouped features** — all sites of a TF motif, co-regulated ENCODE DHS clusters, gene regions, MSigDB gene sets, or custom BED sets — then clusters cells on those aggregates, compares them to an ENCODE DNase reference panel to infer identity, and tests features differing between subpopulations.

## Key claims

- **Peak-level clustering fails where aggregation works**: on a scATAC-seq mix of GM12878 and HEK293T cells, bulk peak calling plus clustering on peak signals did not separate the two cell types; SCRAT's aggregated features did, and recovered differential features matching cell identity.
- **Feature types** (pre-defined for human and mouse): *Motif*, *ENCODE Cluster* (co-regulated DHSs), *Gene*, *Gene Set* (MSigDB), plus *Custom Feature*; signals are library-size normalised after aggregation.
- **Workflow**: BAM input with optional ENCODE-blacklist exclusion and low-count cell filtering → feature summarisation → clustering (multiple methods, optional dimension reduction, automatic cluster number) → identity inference by similarity to ENCODE DNase-seq profiles (heatmap; projection of reference samples into the single-cell PC space) → differential feature tests (t/ANOVA or Wilcoxon/Kruskal–Wallis/permutation with FDR cutoff).
- **Example biology**: in human and mouse ESC scATAC-seq, cell-cycle genes were a consistent driver of heterogeneity.

## Methods / evidence

Two-page application note; demonstrations rely on public scATAC-seq data, with comparisons to other tools in supplementary tables (not in the clipping). No quantitative benchmark against alternatives in the main text.

Weight: low as evidence, useful as history — it codifies the feature-aggregation strategy already used in the founding scATAC/scChIP papers into a point-and-click tool.

## Surprising or load-bearing bits

- **Aggregation over prior-knowledge feature sets is the same idea chromVAR formalised for motifs** (deviations with GC/accessibility-matched backgrounds); SCRAT's distinctive pieces are the GUI and the reference-panel identity inference. (synthesis)
- Using bulk ENCODE DNase profiles as a reference to label single cells anticipates later reference-mapping approaches, though here only by correlation. (synthesis)
- A 2024 benchmark still tests a feature-aggregation approach alongside LSI- and spectral-embedding methods ([[luo-2024-scatac-benchmark]]) — aggregation remains a live baseline. (synthesis)

## Concepts touched

- [[scatac-seq]] / [[chromatin-accessibility]] — sparsity motivates aggregation over feature sets.
- [[transcription-factor-motif]] — motif-site aggregation as a feature type.
- [[clustering-algorithms]] / [[dimensionality-reduction]] — clustering on aggregated features.
- [[cell-type-annotation]] — identity inference against ENCODE DNase references.
- [[dnase-seq]] — ENCODE DHS clusters and scDNase-seq input.

## Connections to other sources

- Data types and founding papers cited: [[buenrostro-2015-nature]], [[cusanovich-2015-sciatac]] (scATAC-seq), [[rotem-2015-drop-chip]] (scChIP-seq), [[jin-2015-nature]] (scDNase-seq).
- Contemporaneous/later scATAC analysis tools: [[schep-2017-chromvar]], [[zamanighomi-2018-scabc]], [[bravo-2019-cistopic]], [[fang-2021-snapatac]], [[granja-2021-archr]], [[stuart-2021-natmethods]].
- Benchmark context: [[luo-2024-scatac-benchmark]].

## Open questions

- How much information is lost by collapsing loci into pre-defined features, versus data-driven embeddings (LSI, topic models) that can find novel regulatory programs?
- Reference-based identity depends on ENCODE coverage of the relevant cell types.

## Related

- [[scatac-seq]] · [[40-Topics/single-cell-atac-seq]] · [[schep-2017-chromvar]]
