---
type: summary
title: "Rylaarsdam et al. 2025 — Single-cell DNA methylation analysis tool Amethyst resolves distinct non-CG methylation patterns in human astrocytes and oligodendrocytes"
source: "[[00-Sources/papers/Single-cell DNA methylation analysis tool Amethyst resolves distinct non-CG methylation patterns in human astrocytes and oligodendrocytes]]"
source_quality: full
source_sha256: "32da68014586f62f1b4f7807caba6ee7d9809842a973506fc63b44dc9b3dc2a1"
source_kind: paper
author: "Lauren E. Rylaarsdam, Benjamin W. Skubi, Ruth V. Nichols, Brendan L. O'Connell, Jack Henry Kotnik, Stephen D. Coleman, Galip Gürkan Yardımcı, Andrew C. Adey (corresponding)"
published: 2025-10-14
ingested: 2026-10-07
doi: "10.1038/s42003-025-08859-2"
journal: "Communications Biology 8:1468"
tags: [Amethyst, Facet, single-cell-methylation, sciMET, sciMETv3, mCH, non-CG-methylation, DMR-calling, glia, astrocytes, oligodendrocytes, X-inactivation, ALLCools, MethSCAn, R-package, hdf5]
entities: ["[[20-Entities/andrew-adey]]"]
concepts: ["[[bisulfite-sequencing]]", "[[combinatorial-indexing]]", "[[dimensionality-reduction]]", "[[clustering-algorithms]]", "[[cell-type-annotation]]", "[[reference-atlas-mapping]]", "[[batch-effect]]"]
topics: ["[[dna-methylation]]", "[[computational-methods]]"]
---

**Citation:** Rylaarsdam et al. (2025) — *Single-cell DNA methylation analysis tool Amethyst resolves distinct non-CG methylation patterns in human astrocytes and oligodendrocytes* — *Communications Biology* 8:1468. [DOI](https://doi.org/10.1038/s42003-025-08859-2)

# Rylaarsdam 2025 — Amethyst

> Single-cell methylation has a tooling gap rather than a data gap: sciMET-class assays now yield up to a million methylomes, but most analysis packages either cannot hold the data, ignore mCH, or cover one step. **Amethyst** is an R package (Adey lab) that runs base-level calls → feature matrices → IRLBA reduction → clustering → annotation → DMR calling → methylation-specific visualisation, with calls stored in **hdf5** and heavy aggregation optionally offloaded to a Python helper, **Facet**. It is shown on PBMC and cortex sciMET data and scaled to 145,219 cells; the biological payoff is that **astrocytes and oligodendrocytes carry gene-specific hyper-mCH** with neuron-like properties — anticorrelated with expression, CAC-dominated, and elevated over X-inactivation escapees in females.

## Key claims

- **Most existing packages could not run on a 1346-cell test set.** Of 16 packages surveyed, MELISSA and BPRMeth required in-memory storage of single-cytosine calls (1.8 billion CG and 38.4 billion CH sites for this dataset) and could not be built; scMET took 481 minutes and found 9 variable features with defaults; Epiclomal took days and found 13. Only Amethyst, MethSCAn and ALLCools handled sciMETv3-scale throughput.
- **Clustering was fastest in Amethyst** (IRLBA truncated SVD); for DMR testing between excitatory and inhibitory neurons, all three viable tools performed similarly when Facet was used, with MethSCAn's DMR step fastest at the cost of an expensive preparation stage.
- **Feature choice matters by tissue.** mCG over 100 kb windows resolves PBMC and brain populations; MethSCAn VMRs resolved an extra PBMC group; in brain, combining mCG + mCH separated clusters better than either alone (silhouette 0.67 vs 0.57 / 0.50).
- **DMRs land on regulatory DNA.** 91.2% of PBMC DMRs and 83.1% of brain DMRs fell in GeneHancer enhancers/promoters (~12% of the genome); top DMRs hit canonical markers (e.g. hypomethylated *NCR1* in NK cells; *TLE4* in Exc L6 TLE4 neurons; *SATB2* hyper-mCH in MGE/CGE inhibitory but not excitatory neurons).
- **Three-tool DMR comparison** (313 excitatory vs 184 inhibitory neurons): >5 million differentially methylated CG sites in total, 412,202 shared by all three methods. ALLCools' site-based calling gives much smaller regions and needs very high coverage; MethSCAn is more lenient at default; Amethyst's high-confidence defaults gave fewer DMRs that overlapped regulatory elements more often.
- **Glial hyper-mCH**: 99.9% of hyper-mCH regions and 99.0% of hyper-mCH genes were neuronal, but astrocyte and oligodendrocyte hits exist; 14 genes were glia-hypermethylated in both region and gene-body tests, usually driven by one glial type (*PCDHGC3–5* oligodendrocyte-only; *CTTNBP2*, *POU4F1*, *BMI1* in astrocytes; *BROX* in oligodendrocytes). Glial hyper-mCH is often not gene-body-bounded and is decoupled from mCG.
- **Repressive, as in neurons**: using paired RNA from the reference atlas (40/53 astrocyte and 2/5 oligodendrocyte hyper-mCH genes captured), hyper-mCH genes were lowly expressed in the glial class carrying them.
- **Atlas scale**: 145,219 cells from BA46 of four individuals across two sequencing platforms (sciMETv3) separated without platform/sample bias; processing time scaled linearly with cell number. *BROX* (oligodendrocytes) and *CTTNBP2* (astrocytes) replicated.
- **Trinucleotide context**: across all 12 CHH contexts, CAH (especially CAC) dominated in hyper-mCH genes regardless of cell type; non-hyper-mCH glial genes converged toward an even distribution.
- **Sex and X-inactivation**: 453 inter-individual DMGs, 91% on chrX; top hit *USP9X* hyper-mCH in all female neural populations (not at mCG), with escapees such as *USP9X* and *KDM6A* among top hits; absent in mesoderm-derived microglia.

## Methods / evidence

Data: sciMETv2 PBMC (3138 cells, sciMET-cap with the Twist methylome panel, one individual) and middle frontal gyrus (1346 cells); sciMETv3 BA46 from four donors (F38, M48, F27, M40). Preprocessing via Premethyst (unidex demultiplexing, BSBolt alignment, per-cell dedup, calls → .h5). Score metric = normalised deviation of feature mCG from the cell's global mCG; `regressCovBias` regresses each dimension on log cytosines covered; missing values set to 0 (no imputation). DMR test: Fisher's exact test variant (from methylKit) on aggregated, smoothed windows per group, multiple-testing correction, collapse of adjacent windows. Annotation by marker-gene mCG/mCH plots or correlation of gene-body %mCH to a reference brain atlas (two built-in references: brain, PBMC). Benchmarks tracked with `/usr/bin/time -v` against ALLCools, MethSCAn, scMET, MOFA+, Epiclomal, BPRMeth/MELISSA.

Weight: the benchmark is authored by the tool's developers on their own (high-coverage) data, with competitors run largely at defaults — the authors themselves acknowledge scMET and Epiclomal would do better with tuned features. The DMR "higher confidence" claim rests on regulatory-element overlap, not ground truth. The glial mCH biology is the more durable contribution, replicated in an independent four-donor dataset, though with only four individuals.

## Surprising or load-bearing bits

- **mCH is not a neuron-only mark**: glia carry targeted hyper-mCH at ~fivefold lower global levels, with the same context preference (CAC) that matches MeCP2 binding — the authors use this to support glial involvement in Rett syndrome.
- **mCH over X-escape genes in females** across neurons, astrocytes and oligodendrocytes but not microglia — an ectoderm-shared principle visible only at single-cell resolution.
- **Promoter hypo-mCG is an unreliable marker readout**: some validated markers show no variable methylation, some have universal promoter hypomethylation, and some (e.g. *C1QA*) appear to use a promoter shifted from the annotated site — hence gene-body visualisation tools (`heatMap`, `histograM`).
- The design choice to compute on a cluster then interact locally in RStudio is the practical contribution: it brings methylation into the Seurat/Signac/ArchR ecosystem that ALLCools (Python) sits outside (synthesis).

## Entities mentioned

- [[20-Entities/andrew-adey]] — corresponding author; the sciMET assay family (v2, v3, sciMET-cap) supplies all datasets.

## Concepts touched

- [[bisulfite-sequencing]] — downstream analysis layer for combinatorial-indexing scWGBS; reinforces mCH as a typing modality beyond neurons.
- [[combinatorial-indexing]] — sciMETv3's third barcoding round is what creates the atlas-scale analysis problem.
- [[dimensionality-reduction]] — IRLBA on windowed score matrices with coverage-bias regression.
- [[cell-type-annotation]] / [[reference-atlas-mapping]] — annotation by marker methylation or correlation to a reference methylation atlas.
- [[batch-effect]] — Harmony available; atlas data integrated across two sequencing platforms without visible platform bias.

## Connections to other sources

- Assay lineage: [[mulqueen-2018-sci-met]] → [[nichols-2022-scimet-v2]] (source of the 1346-cell brain test set); the PBMC data come from sciMET-cap ([[acharya-2024-scimet-cap]]); the 145,219-cell BA46 atlas from sciMETv3 ([[nichols-2025-scimetv3]]); throughput comparison with [[zhang-2023-drop-bs]].
- Competing analysis tools it benchmarks: [[kremer-2024-methscan]] (MethSCAn), [[kapourani-2021-scmet]] (scMET), [[kapourani-2019-melissa]] (MELISSA), [[desouza-2020-epiclomal]] (Epiclomal), [[argelaguet-2020-mofa-plus]] (MOFA+); surveyed but not benchmarked: [[danese-2021-episcanpy]].
- mCH as a cell-typing signal, established on neurons: [[luo-2017-snmc-seq]], [[luo-2018-snmc-seq2]]; brain methylome atlases: [[liu-2023-mouse-brain-methylome-3d]].
- Imputation-free sparsity handling contrasts with the imputation route benchmarked in [[liang-2026-scmeth-imputation-benchmark]].

## Open questions

- No ground-truth DMR benchmark; agreement among tools (412,202 shared sites out of >5 million) shows the tools disagree substantially, and which DMR set is "right" is left open.
- Only four donors for inter-individual analysis — sex dominates the signal; autosomal individual variation in mCH is underpowered, as the authors note.
- Whether glial hyper-mCH is deposited by DNMT3A in a postnatal window as in neurons, or reflects lineage history, is not addressed (synthesis).

## Related

- [[nichols-2022-scimet-v2]] · [[kremer-2024-methscan]] · [[40-Topics/dna-methylation]] · [[20-Entities/andrew-adey]]
