---
type: summary
title: "Park et al. 2026 — MINTsC learns multi-way chromatin interactions from single cell high throughput chromatin conformation data"
source: "[[00-Sources/papers/MINTsC learns multi-way chromatin interactions from single cell high throughput chromatin conformation data]]"
source_kind: paper
author: "Kwangmoon Park, Tianchuan Gao, Jingwen Yan, Sündüz Keleş (corresponding)"
published: 2026-06-02
ingested: 2026-08-13
doi: "10.1038/s41467-026-73773-y"
journal: "Nature Communications 17 (2026)"
tags: [MINTsC, multi-way-interaction, clique-detection, dirichlet-multinomial, spline, epistasis, eQTL, prefrontal-cortex, SPRITE, scNanoHi-C]
entities: ["[[sunduz-keles]]"]
concepts: ["[[single-cell-hi-c]]", "[[multi-way-chromatin-interaction]]", "[[chromatin-loop]]", "[[cis-regulatory-element]]", "[[gene-regulatory-network]]", "[[dip-c]]", "[[sc-sprite]]"]
topics: ["[[3d-genome]]", "[[computational-methods]]", "[[brain-somatic-mosaicism]]"]
---

**Citation:** Park, Gao, Yan & Keleş (2026) — *MINTsC learns multi-way chromatin interactions from single cell high throughput chromatin conformation data* — *Nature Communications* 17. [DOI](https://doi.org/10.1038/s41467-026-73773-y)

# Park 2026 — MINTsC

> A reframing more than a tool: **scHi-C is a multilayer network** — each cell is a layer, loci are nodes, contacts are edges — so a **multi-way chromatin interaction is a clique**. Bulk Hi-C cannot express this question at all, because aggregation destroys the within-nucleus co-occurrence that makes three loci "simultaneously" in contact. The payoff is practical: multi-way interactions collapse the multiple-testing burden for **epistatic SNP effects** in eQTL analysis from all-pairs to a candidate list.

## Key claims

- **The clique formulation is the contribution.** Under the multilayer-network view, scHi-C already contains abundant cliques of order 3–6, even at its sparsity — enough to infer lower-order multi-way interactions, though very high-order events remain out of reach.
- **The statistical machinery has three parts.** (1) A Dirichlet-multinomial model of per-cell contact counts with a natural cubic **spline** over genomic distance "bands" (off-diagonals), giving bias-adjusted pairwise test statistics; (2) a clique-level statistic ("clique p-score") built from **order statistics of the pairwise p-values** across cells of one context, with an analytic Beta null; (3) Benjamini–Hochberg FDR control. Because the statistic is built from distance-adjusted pairwise tests, it is stable to the distribution of intra-clique genomic distances.
- **Two filters guard against the obvious failure mode** — a spurious clique assembled from pairwise contacts that never co-occurred in any single cell. A **pre-filter** admits only cliques fully observed in at least *c* cells; an optional **post-filter** applies a co-occurrence test on clique edges.
- **Same-cell co-localisation is verified three ways.** (i) Train/test split on GM12878 scMicro-C: 904 of 43,469 candidate 3-way cliques called at FDR 0.1 on 48 training cells; in the 48 test cells, called cliques had significantly smaller maximum pairwise 3D distance (via [[tan-2018-science|Dip-C]] reconstruction), nearly all below the 3.5-particle-radius (~240 nm) cutoff scMicro-C itself uses. Empirical FDR 8%. (ii) Cross-technology against mouse-brain DNA seqFISH+: in the top 20% of cells by clique count, MINTsC cliques had significantly smaller within-clique distances (P < 0.01); per-cell false-positive rate ≤3% against a 150-nm imaging gold standard. (iii) Simulation with deliberately planted spurious cliques (two pairs in one cell group, the third pair in another) held empirical FDR at 5%.
- **External multi-way assays corroborate.** MINTsC cliques have significantly higher [[sc-sprite|SPRITE]] enrichment scores in both GM12878 and mESCs, higher GAM triplet scores in mESCs, and higher scNanoHi-C concatemer counts across clique sizes. Stratification shows cliques with maximum within-clique distance under 200 kb are best supported — an empirical distance constraint for post-processing.
- **A methylation-based validation with no equivalent elsewhere.** In human PFC [[lee-2019-natmethods|sn-m3C-seq]] data, MINTsC clique *z*-scores correlate with **partial correlations of DNA methylation** among clique loci — conditional dependence in co-methylation as independent evidence of a multi-way regulatory relationship. This uses the joint nature of sn-m3C-seq to validate its own contact channel with its methylation channel.
- **Beats the natural baselines.** Against cliques assembled from [[yu-2021-snaphic|SnapHiC]] loop calls (which yielded no cliques above order 3) and from strong pseudobulk O/E ≥ 2 pairs, MINTsC captured more PsychENCODE gene–enhancer–enhancer "v-structures" across cell types; on synthetic data, comparable TPR at significantly lower FPR (<0.05).
- **Haplotype-aware analysis works.** On haplotype-resolved Dip-C mouse brain, p-values are well calibrated per haplotype; most cliques are concordant between haplotypes; aggregating over haplotypes loses some power for haplotype-specific interactions but does not inflate false positives.
- **Genes in multi-way interactions are more highly expressed** across most PFC cell types (Wilcoxon P ≤ 0.003), agreeing with long-read scHi-C findings in GM12878.
- **Epistatic eQTLs in Alzheimer's data.** Testing 321 (gene, SNP₁, SNP₂) tuples from 39 genes in ROS/MAP cortex expression data, SNP–SNP interaction F-test p-values were significantly stronger than permuted. The showcase: ***DKK3*** (amyloid-β pathology, synapse restoration), where rs7480026 and rs16910272 in introns 3 and 5 each have weak individual effects but a significant interaction on expression; a similar effect for *CPLX2* (cognitive resilience, synaptic plasticity).

## Methods / evidence

Six datasets across resolutions: GM12878 scMicro-C (10 kb), GM12878 scHi-C (500 kb), mESC serum/LIF (1 Mb) and 2i/LIF (10 kb), mouse cortex/hippocampus Dip-C (25 kb), human PFC sn-m3C-seq (10 kb, eight neuronal subtypes). Orthogonal validation from imaging (DNA seqFISH+, Dip-C 3D reconstruction), multi-way assays (SPRITE, GAM, scNanoHi-C), regulatory annotation (ABC scores, PsychENCODE, snATAC/scRNA cCRE links), and an independent eQTL cohort.

Weight: the validation stack is unusually broad — three imaging/3D routes plus three orthogonal multi-way assays. The eQTL epistasis result is the most exciting and the least replicated: 39 genes, one cohort.

## Surprising or load-bearing bits

- **Multiple-testing reduction is the real application.** Genome-wide SNP–SNP epistasis testing is hopeless because of the combinatorial burden; MINTsC converts "test all pairs" into "test the pairs that share a nucleus with the promoter." That is a structural-biology prior applied to a statistical genetics problem, and it is the paper's most transferable idea.
- **Using methylation partial correlations to validate contacts** is an argument only possible in joint assays, and it is the sharpest demonstration in the corpus of why [[lee-2019-natmethods|sn-m3C-seq]]-style co-measurement pays off analytically, not just descriptively.
- **SnapHiC-derived cliques never exceeded order 3.** Loop-caller output is too sparse and too conservative to reconstruct higher-order structure — multi-way calling genuinely needs its own statistic rather than post-processing of pairwise calls.
- **The homogeneity assumption is explicit and load-bearing.** MINTsC requires a relatively homogeneous cell group; each cell is treated as an independent sample of one context's true contact matrix. The authors note uncertainty in cluster assignment could be folded into the GLM, but it is not done here.
- **Dedicated multi-way assays exist (GAM, ChIA-drop, SPRITE, Tri-C, multi-contact 4C, COLA, Pore-C) but are mostly cell-line demonstrations**, while scHi-C from complex tissue is abundant — notably the NIH BRAIN Initiative's brain datasets. MINTsC is a bet on reanalysing existing data rather than generating new assay data.
- The two-stage band-level/locus-pair-level modelling is offered as a **general template** for any sparse high-dimensional single-cell modality where an exponential-family generative model applies.

## Entities mentioned

- [[sunduz-keles]] — corresponding author; statistical genomics.

## Concepts touched

- [[multi-way-chromatin-interaction]] — this is the founding computational source for the concept.
- [[single-cell-hi-c]] — the multilayer-network/clique formulation.
- [[gene-regulatory-network]] — multi-enhancer cooperativity as the biological target.

## Connections to other sources

- Explicit baseline and closest sibling: [[yu-2021-snaphic]].
- Input data and cell labels: [[lee-2019-natmethods]], [[tan-2018-science]], [[nagano-2013-nature]], [[luo-2017-snmc-seq]].
- Related scHi-C feature callers: [[zhou-2019-schicluster]], [[zhang-2022-higashi]], [[xiong-2024-scghost]].
- Multi-way assay context: [[sc-sprite]]; long-read multi-contact via [[oxford-nanopore]]-style concatemers.
- Regulatory-link references used for validation: ABC scores, PsychENCODE, and cCRE links analogous to [[pliner-2018-cicero]] and [[bravo-2023-scenicplus]].
- Alzheimer's context: [[miller-2022-nature]], [[kousi-2022-ad-mosaicism]], [[david-bennett]] (ROS/MAP).
- Differential-compartment counterpart at bulk/pseudobulk scale: [[chakraborty-2022-dchic]].

## Open questions

- **Cliques above order ~6 remain undetectable** — the ligation and sparsity ceiling, not a statistical one.
- The homogeneity assumption is untested within methylation-defined clusters; soft cluster assignments are proposed but not implemented.
- The 200-kb within-clique distance constraint is empirical, derived from scNanoHi-C support, and may be assay-specific.
- The epistasis result covers 39 genes in one cohort; whether the multi-way prior generally enriches for real epistasis needs replication.
- Multi-way interactions are called per cell type, so their **cell-to-cell variability** — the thing the single-cell formulation ought to enable — is not reported.

## Related

- [[yu-2021-snaphic]] · [[multi-way-chromatin-interaction]] · [[lee-2019-natmethods]] · [[40-Topics/3d-genome]]
