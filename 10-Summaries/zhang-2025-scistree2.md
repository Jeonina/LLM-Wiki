---
type: summary
title: "Zhang et al. 2025 — ScisTree2 enables large-scale inference of cell lineage trees and genotype calling using efficient local search"
source: "[[00-Sources/papers/ScisTree2 enables large-scale inference of cell lineage trees and genotype calling using efficient local search]]"
source_kind: paper
author: "Haotian Zhang, Yiming Zhang, Teng Gao, Yufeng Wu"
published: 2025-12
ingested: 2026-10-07
doi: "10.1101/gr.280542.125"
journal: "Genome Research 35(12):2781–2791"
tags: [ScisTree2, ScisTree, cell-lineage-tree, infinite-sites, SPR-local-search, branch-and-bound, genotype-calling, allele-dropout, CellPhy, HUNTRESS, SiFit, SCITE, CellCoal, HGSOC, DLP+]
entities: []
concepts: ["[[phylogenetic-inference]]", "[[allele-dropout]]", "[[single-cell-variant-calling]]", "[[lineage-tracing]]", "[[dlp-plus]]", "[[intratumor-heterogeneity]]"]
topics: ["[[single-cell-lineage-tracing]]", "[[cancer-clonal-evolution]]", "[[computational-methods]]"]
---

**Citation:** Zhang et al. (2025) — *ScisTree2 enables large-scale inference of cell lineage trees and genotype calling using efficient local search* — *Genome Research* 35(12):2781–2791. [DOI](https://doi.org/10.1101/gr.280542.125)

# Zhang 2025 — ScisTree2

> ScisTree2 scales model-based single-cell SNV phylogenetics to **tens of thousands of cells** by keeping the model deliberately simple — binary genotypes under the **infinite-sites (IS)** assumption, input as a per-cell, per-site posterior probability of wild type — and spending the algorithmic effort on search. Given a tree, the best placement of each mutation (and hence the genotype matrix) is found in O(nm) by dynamic programming; ScisTree2's contribution is an **SPR local search that evaluates the whole O(n²) SPR neighbourhood in O(n²m) rather than the naive O(n³m)**, plus a branch-and-bound pruning that makes ≥10,000-cell trees practical. The authors claim it is the first model-based lineage-tree and genotype-calling method able to handle data of that size.

## Key claims

- **ScisTree (2020) stalls above ~1,000 cells**; its NNI search is O(Kn²m) and easily trapped in local optima. ScisTree2 switches to SPR (whose neighbourhood contains NNI's) and achieves the same O(Kn²m) per-iteration order — one order of magnitude faster than naive SPR, with a proven bound (contrasted with heuristic SPR speedups lacking guarantees).
- **Accuracy (CellCoal simulations, diploid IS model; defaults 200 cells, 5× sites, ADO 0.2, error 0.01, 10× coverage; 50 replicates):** ScisTree2 and CellPhy had the highest tree accuracy, but CellPhy was weaker on genotype accuracy; ScisTree2 remained best at higher ADO (0.1–0.4) and lower coverage (2×–20×).
- **Speed (30 threads where supported):** ScisTree2 most efficient overall, especially with many cells; CellPhy scales with sites but not cells; HUNTRESS scales with cells but not sites. SiFit, SCITE and original ScisTree are single-threaded and dropped out at larger sizes (>1 day).
- **Ultra-low coverage:** by thinning 1× simulations, ScisTree2 called genotypes with **>85% accuracy at 0.1× coverage** and led on AD/DL F-scores — but **no method achieved high tree accuracy** at <1×.
- **Targeted-sequencing regime (1,000 / 2,000 / 50,000 cells, 500 SNVs):** ScisTree2 beat HUNTRESS and CellPhy on genotype accuracy and AD/DL F-scores; tree topology accuracy was very low for all methods when sites are few.
- **Robust to moderate IS violations:** with increasing fractions of finite-sites (FS) sites (0–0.75; 100 cells, 500 sites), all methods declined but ScisTree2 still outperformed SiFit and CellPhy, which are designed for FS.
- **Real data (HGSOC; 891 cells from three clonally related cell lines of one patient, described as low-coverage (~0.15×) targeted sequencing, 14,068 SNVs; data from Laks et al. 2019):** only ScisTree2 was run on the full set. Called genotypes: 2,337 (16%) ancestral, 1,891 (14%) clonal, 9,840 (70%) clade mutations; ANNOVAR gave 48 exonic ancestral genes, all within the 49 ancestral genes extracted from the original clonal tree (only XXYLT1 missed). The ordering of the six highlighted genes (TP53, FOXP2, SUGCT ancestral; HTR1D, INSL4, ZHX1 clade) matched the published clonal tree exactly, with TP53 first. Each cell line formed its own clade; within-line topology agreed for OV2295 and OV2295(R2) but differed substantially for TOV2295(R).
- **Reduced HGSOC (789 SNVs after removing sites with >650 missing values):** ScisTree2 outperformed HUNTRESS, CellPhy and neighbour joining on AD/DL F-scores in most parameter settings; robust to the assumed ADO rate; allele-frequency-based genotype priors recommended as default.

## Methods / evidence

Input: n × m matrix M of posterior wild-type probabilities (e.g., from GATK genotype likelihoods via Bayes' rule). Posterior of a tree = product over sites of the best single-branch placement, using Q_s(v) = ∏(1−M)/M over the leaves below v, computed bottom-up. SPR neighbourhood evaluation uses precomputed subtree maxima (M1), path maxima (M2) and "subtree-minus-path" maxima (M3) so each candidate SPR costs O(1) per site. Initial tree by neighbour joining (modified from ScisTree). Metrics: genotype accuracy, tree accuracy (1 − normalised Robinson–Foulds), ancestor–descendant and different-lineage F-scores; for FS-model tools (CellPhy, SiFit) mutations were placed on their trees with ScisTree2's caller. Benchmarked: CellPhy, HUNTRESS, SiFit, ScisTree, and SCITE (small data only). C++ with a Python interface.

Weight: mostly simulation under the same IS generative assumptions ScisTree2 uses (CellCoal), which flatters IS methods; the FS-violation experiment partially addresses this. Real-data "ground truth" is the published CNV-based clonal tree, i.e. a consistency check rather than truth. The 50,000-cell claim is from the 500-SNV targeted simulation; the real dataset has 891 cells.

## Surprising or load-bearing bits

- **Simplicity buys scale**: the authors argue that simpler-but-adequate probabilistic models may be the key to speeding up lineage inference — an explicit trade-off against richer models allowing recurrence/loss (e.g., Kuipers et al. 2022). (synthesis on emphasis)
- **Genotype calling is a by-product of the tree**: once the tree is fixed, genotypes follow by trace-back — tree inference doubles as a denoising genotype caller for ADO-heavy data (ADO stated as 50% or higher in current single-cell data).
- **Low coverage separates genotype accuracy from topology accuracy**: >85% genotype accuracy at 0.1× with poor trees means "accurate calls" do not imply "reliable phylogeny". (synthesis)
- **Clustering-free lineage reconstruction**: the authors pitch direct whole-population trees as an alternative to cluster-then-tree workflows, noting CNVs (used for clustering) are rare in normal tissue, so SNV-only methods matter for development and aging.

## Concepts touched

- [[phylogenetic-inference]] — IS-model maximum-posterior tree search with provable SPR speedup.
- [[allele-dropout]] — modelled implicitly via uncertain genotype probabilities; ADO-rate robustness tested.
- [[single-cell-variant-calling]] — tree-informed genotype calling.
- [[dlp-plus]] — the HGSOC DLP+ dataset used as the real-data test.

## Connections to other sources

- Benchmarked predecessors summarised in the wiki: [[jahn-2016-scite]] (MCMC, IS), [[zafar-2017-sifit]] (FS model).
- Other single-cell SNV phylogeny tools: [[singer-2018-sciphi]], [[el-kebir-2018-sphyr]], [[malikic-2019-phiscs]], [[satas-2020-scarlet]], [[foroughmand-2022-scelestial]], [[ross-2016-onconem]].
- Real data from [[laks-2019-dlp-plus]] (HGSOC OV2295 lines); the same HGSOC/DLP+ lineage of work underlies [[mcpherson-2025-ongoing-wgd]], which builds SNV clone trees from pseudobulked clones (SBMClone/doubleTime) and CNA cell trees with MEDICC2 rather than per-cell SNV trees. (synthesis)
- CNA-based alternatives: [[kaufmann-2022-medicc2]], [[wang-2021-medalt]]; review [[lu-2024-cnaphylogeny-review]].
- Large-scale lineage context motivating scale: [[coorens-2021-nature]]; mtDNA-based trees [[ludwig-2019-mtdna-lineage-tracing]]; review [[rodriguez-fraticelli-2026-lineage-tracing-review]].

## Open questions

- Extension beyond binary SNVs (ternary genotypes, CNA-altered allele states) is left open; the speed depends on binary simplicity.
- ScisTree2 does not itself define clonal populations; downstream tools are needed to turn large trees into clones or population dynamics.
- How accurate are topologies on real low-coverage scDNA (DLP+-like) data without CNV pre-clustering? The TOV2295(R) discordance is unexplained.

## Related

- [[jahn-2016-scite]] · [[laks-2019-dlp-plus]] · [[phylogenetic-inference]] · [[40-Topics/single-cell-lineage-tracing]]
