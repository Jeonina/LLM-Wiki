---
type: summary
title: "Gillman et al. 2026 — Detecting somatic mutations in rare clones using single-cell multiomics"
source: "[[00-Sources/papers/Detecting somatic mutations in rare clones using single-cell multiomics.pdf]]"
source_quality: full
source_sha256: "b1d30a124f70475a6df6d539c83ce8a561d29b7e71ced73ad062be28a16eb50d"
source_kind: paper
author: "Rhys Gillman, Sonam Dudka, Jerome Samir, Raymond Louie, Chris Goodnow, Fabio Luciani, Mandeep Singh, Matt A. Field (corresponding)"
published: 2026-08-13
ingested: 2026-10-12
doi: "10.1101/gr.281609.125"
journal: "Genome Research (accepted manuscript, published online ahead of print)"
aliases: ["Gillman 2026", "SCARCE", "Single-Cell Analysis of Rare Clonal Events"]
tags: [SCARCE, somatic-variant-prioritisation, rare-clones, Tapestri, ADT, surface-markers, odds-ratio, Wald-test, variant-clustering, refractory-coeliac-disease, autoimmunity, PDAC, KG-1, R-package, Field-lab]
entities: []
concepts: ["[[30-Concepts/single-cell-variant-calling]]", "[[30-Concepts/cite-seq]]", "[[30-Concepts/variant-effect-prediction]]", "[[30-Concepts/structural-variants]]", "[[30-Concepts/gt-seq]]", "[[30-Concepts/resolveome]]"]
topics: ["[[40-Topics/mosaic-variant-calling]]", "[[40-Topics/somatic-mosaicism]]", "[[40-Topics/single-cell-multiomics]]", "[[40-Topics/scdna-seq]]"]
---

**Citation:** Gillman et al. (2026) — *Detecting somatic mutations in rare clones using single-cell multiomics* — *Genome Research* (accepted manuscript, published online 2026-08-13). [DOI](https://doi.org/10.1101/gr.281609.125)

# Gillman 2026 — SCARCE: enrichment-based prioritisation of rare-clone somatic variants

> **Source note:** full text of the accepted (not copy-edited) manuscript, including Methods. Figures are described only by their legends; Supplementary Figures S1–S5 and Supplementary Materials are not in the source.
>
> SCARCE (Single-Cell Analysis of Rare Clonal Events) is an R package that ranks somatic variants in scDNA-seq data by how strongly they are enriched in one cell subpopulation versus all other cells. Subpopulations come from ADT surface-marker clustering (Tapestri), user annotations, or clustering on the variants themselves. Each variant gets a 2×2 table (mutant vs reference cells, inside vs outside the group), an odds ratio, and a Wald test (Fisher's exact test when any count is < 5), with Benjamini–Yekutieli FDR control. The argument is that a statistical ranking lets you filter lightly, so true rare-clone variants are not thrown away by the stringent filtering that Mission Bio's Optima and Mosaic need to shrink ~100,000 calls to ~20–50. In a PBMC sample with a KG-1 spike-in, SCARCE isolated a 10-cell cluster out of 16,316 cells (0.06%) and ranked a known KG-1 *TP53* variant first. In a refractory coeliac disease sample, it recovered all four known drivers that survived filtering and two additional *STAT3* candidates.

> [!abstract] 한눈에
> SCARCE는 scDNA-seq의 somatic variant를 특정 세포 subpopulation에 얼마나 enrichment되어 있는지로 순위를 매기는 R package다. Tapestri 데이터에서 0.06% 수준의 희귀 KG-1 clone을 분리했는데, Optima와 Mosaic은 이 clone을 찾지 못했다.

## Key claims

- **Rare-clone isolation at 0.06%.** Tapestri Myeloid panel data from Mission Bio's public repository: 16,316 cells, 114,788 raw variant calls, two PBMC samples mixed with KG-1 AML cells. Variant-based clustering in SCARCE gave two large clusters (likely the two PBMC donors) and a 10-cell cluster. Optima and Mosaic, which cluster on far fewer variants, did not appear to isolate a KG-1 cluster.
- **Validation by a known cell-line variant.** Only one DepMap KG-1 variant overlapped the targeted panel: a *TP53* splice-donor variant (hg19 chr17:7578176C>T). SCARCE ranked it the most enriched variant: present in 10/10 cluster-0 cells and 30/15,734 (0.2%) other cells. Six variants were significantly enriched (p < 0.05) in cluster 0, and **none of the six passed the filters of Optima or Mosaic**. Genotype quality for these variants was high inside cluster 0 and lower outside it, which the authors read as false-positive calls outside the cluster.
- **Robust down to ~10 cells in real tumour data.** PDAC patient PR02-4 (Tapestri data from an earlier study): two populations of 3,400 and 209 cells. Of three previously reported variants, *KRAS* G12D and *TP53* C242Y were significantly enriched; *KRAS* G12V was present but not enriched. Subsampling the 209-cell population to 100, 50, 25 and 10 cells (10 iterations each) kept both variants significant and the mutant population identified in every run except one (iteration 8 at 10 cells).
- **Known drivers recovered in refractory coeliac disease (RCD).** 4,858 lymphocytes with five previously established drivers (*DDX3X* M187R, *DDX3X* R528C, *SOCS3* V84I, *STAT5B* N642H, *STAT3* E552K). All three tools dropped *SOCS3* V84I in filtering (low depth, poor alignment). In Optima and Mosaic heatmaps only the two *DDX3X* variants showed obvious enrichment; SCARCE ranked all four remaining drivers as highly significant.
- **New candidate variants.** SCARCE also flagged *STAT3* S614R (OR = 47.5, p = 1.05 × 10⁻²²) and *STAT3* T389S (OR = 34.3, p = 2.53 × 10⁻¹³) in cluster 2, called "probably damaging" and "possibly damaging" by PolyPhen. The authors call them likely true variants; no orthogonal validation is reported.
- **Cell-type context from ADT.** ADT-based clustering of the same RCD sample put both *DDX3X* drivers in CD4−CD8− T cells and *STAT5B* N642H and *STAT3* E552K in CD8+ T cells, matching the earlier publication.
- **Works beyond Tapestri, but power drops.** Any multi-sample VCF with one column per cell or clone is accepted. On clonally amplified WGS from a cryoglobulinaemic vasculitis patient (34 cells: blue branch 16, orange branch 16, control 2; chromosome 3 only), no variant reached significance after multiple-testing correction. Ranking by OR / Wald Z instead placed the known blue-branch *KLHL6* L90P among the top variants, along with other previously unreported variants.
- **Memory.** Peak memory was far lower than Optima on large datasets (chunked loading) but much higher than Mosaic. Datasets under ~5,000 cells can run on a local machine.

## Methods / evidence

- **Inputs.** Tapestri HDF5 (variants + ADT) or a multi-sample VCF with one column per cell. Variants are normalised for Ensembl VEP and multi-allelic sites split to biallelic.
- **Three-level filtering.** Per call (depth < 10 or GQ < 30 → genotype set to missing, NGT = 3); per variant across all cells (e.g. alt allele count < 30, alt proportion > 0.7, < 100 cells or < 25% of cells with data, mean mutant AF < 0.1); per cell type (lenient defaults of 1 or 0). A PRIORITY flag marks protein-altering variants with population max AF < 0.02.
- **ADT annotation.** Seurat v5, CLR normalisation, top-75% markers, PCA/UMAP, clustering at several resolutions. SCINA (up to 100 iterations, CellMarker 2.0 markers by default) gives per-cell labels; cells below 0.5 probability are "unknown". The user makes the final per-cluster call.
- **Variant-based clustering.** 100 features: 90% chosen by Bernoulli variance p(1 − p) of the population alt frequency (among variants genotyped in > 80% of cells), 10% from rare variants (< 2%) with mean GQ > 30 ranked by an evidence score (ln alt count × ln mean depth × mean GQ/30). Cosine distance on per-cell AF vectors over shared variants (set to 1 when fewer than 10 overlap), UMAP embedding, then DBSCAN.
- **Enrichment test.** 1-vs-all per group. 2×2 counts a, b, c, d (mutant/reference cells inside/outside), Haldane–Anscombe +0.5 when any count is 0, OR = ad/bc, Wald Z on log OR, Fisher's exact test when min count < 5, Benjamini–Yekutieli adjustment over passing variants. QQ plots on presumed-null variants are said to show super-uniform p-values (supplement, not in source).
- **Evidence weight.** Three to four datasets, each a case study. Truth is a single DepMap variant for KG-1, prior publications by the same group for RCD and vasculitis, and a prior PDAC paper. There is no simulation, no sensitivity/precision curve, and no comparison with any variant caller outside the Tapestri vendor tools.

## Limitations

**Authors' own:**
- No structural variants or copy-number alterations are considered in prioritisation.
- Cell-type annotation is not fully automated; users must decide cluster labels from the plots.
- Optimised for targeted panels; WGS input can need more memory and runtime than expected.
- Variant-based and ADT-based clustering are separate; no combined clustering, no transcriptome-based clustering (for G&T-seq or ResolveOME data), and no immune-repertoire-based annotation yet.
- With large WGS variant sets and small cell numbers, multiple-testing correction removes all significance; users must fall back on effect size.

**Reviewer notes:**
- Benchmarking is narrow: only against Mission Bio's own filtering/visualisation tools, which the authors themselves say are not built for statistical enrichment. No comparison with single-cell callers or with bulk somatic callers run per cell, and no ground-truth simulation. (synthesis)
- The 1-vs-all test treats cells as independent counts, while allelic dropout, doublets and clone-specific copy number all shape per-cell genotypes; none of these is modelled, so the p-values rest on the assumption that called genotypes are correct. (synthesis)
- Several internal inconsistencies: the KG-1 spike-in is 0.06% in the abstract and Results but "0.05%" in the Figure 2 legend; author names are spelled differently on the journal cover page ("Dukda", "Sadir") and the manuscript ("Dudka", "Samir"); the Mosaic package is cited to the PDAC application paper (Zhang et al. 2023); and the Discussion describes MDA as "a precursor to NANOSeq, used by BioSkryb's ResolveOME" before saying ResolveOME uses PTA. (synthesis)

## Surprising or load-bearing bits

- **Filter lightly, then rank.** The main design point is that statistical enrichment replaces aggressive filtering. All six significant KG-1 variants were removed by the vendor tools' filters, so in this example the vendor workflow would have missed the clone entirely.
- **Variant-based clustering beat ADT clustering at isolating "rogue" populations** in the authors' comparison, while ADT clustering gave the biological label (which T-cell subset carries the driver). They propose combining the two.
- **Autoimmune disease as the motivating use case**, not cancer: the drivers are somatic lymphoma-type mutations in expanded T-cell clones of refractory coeliac disease, from the same group's earlier work.

## Entities mentioned

- No entity pages exist for Mission Bio (Tapestri, Optima, Mosaic), BioSkryb, the Field lab or the Garvan Institute.

## Concepts touched

- [[30-Concepts/single-cell-variant-calling]] — SCARCE is a post-calling prioritisation layer: it takes per-cell genotypes and ranks group-enriched variants, rather than calling variants from reads.
- [[30-Concepts/cite-seq]] — ADT surface-marker data (Tapestri's protein assay) used to annotate cell types for enrichment tests.
- [[30-Concepts/variant-effect-prediction]] — VEP consequences, SIFT and PolyPhen used to flag PRIORITY variants and to support the new *STAT3* candidates.
- [[30-Concepts/structural-variants]] — explicitly out of scope (stated limitation).
- [[30-Concepts/gt-seq]] / [[30-Concepts/resolveome]] — other plate-based genome(+transcriptome) platforms the authors say SCARCE accepts via VCF.

## Connections to other sources

- Built for data from [[10-Summaries/pellegrino-2018-tapestri]] (droplet targeted scDNA-seq); [[10-Summaries/sollier-2023-compass]] is another Tapestri-downstream method, but for trees with CNAs, which SCARCE does not model. (synthesis)
- Its critique that bulk somatic callers expect tumour/normal pairs applies to [[10-Summaries/cibulskis-2013-mutect]] and [[10-Summaries/koboldt-2009-varscan]], which the paper names.
- UMI and duplex error-correction approaches it cites as earlier routes to rare variants: [[10-Summaries/schmitt-2012-pnas]].
- Uses Seurat v5 for ADT processing: [[10-Summaries/hao-2024-seurat-v5]].
- Accepts G&T-seq and ResolveOME output: [[10-Summaries/macaulay-2015-gt-seq]], [[10-Summaries/marks-2023-resolveome]].
- Cites the RNA variant-detection problems in [[10-Summaries/lahnemann-2020-grand-challenges]] as a reason to use DNA.

## Open questions

- How well calibrated are the Wald/Fisher p-values when allelic dropout and doublets are present, and what is the false-positive rate on a sample with no rare clone?
- How does SCARCE compare with read-level single-cell callers or tree-based methods on the same Tapestri data?
- The *STAT3* S614R and T389S candidates remain unvalidated.

## Related

- [[40-Topics/mosaic-variant-calling]] · [[40-Topics/somatic-mosaicism]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/scdna-seq]]
- [[pellegrino-2018-tapestri]] · [[sollier-2023-compass]] · [[single-cell-variant-calling]] · [[cite-seq]]
