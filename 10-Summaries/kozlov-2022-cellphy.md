---
type: summary
title: "Kozlov et al. 2022 — CellPhy: accurate and fast probabilistic inference of single-cell phylogenies from scDNA-seq data"
source: "[[00-Sources/papers/CellPhy_ accurate and fast probabilistic inference of single-cell phylogenies from scDNA-seq data]]"
source_kind: paper
author: "Alexey Kozlov, Joao M. Alves, Alexandros Stamatakis, David Posada (corresponding)"
published: 2022-01-26
ingested: 2026-10-07
doi: "10.1186/s13059-021-02583-w"
journal: "Genome Biology 23:37"
tags: [CellPhy, RAxML-NG, GT16, maximum-likelihood, finite-site-model, allelic-dropout, genotype-likelihoods, bootstrap, tumor-phylogeny, CellCoal, colorectal-cancer]
entities: []
concepts: ["[[phylogenetic-inference]]", "[[allele-dropout]]", "[[single-cell-variant-calling]]", "[[doublet-detection]]", "[[mutational-signatures]]", "[[scwga]]"]
topics: ["[[single-cell-lineage-tracing]]", "[[cancer-clonal-evolution]]", "[[computational-methods]]"]
---

**Citation:** Kozlov et al. (2022) — *CellPhy: accurate and fast probabilistic inference of single-cell phylogenies from scDNA-seq data* — *Genome Biology* 23:37. [DOI](https://doi.org/10.1186/s13059-021-02583-w)

# Kozlov 2022 — CellPhy

> Instead of building yet another single-cell tree method from scratch, CellPhy **ports organismal statistical phylogenetics to somatic cells**: it extends the 4-state GTR nucleotide model to a **16-state diploid-genotype model (GT16)**, adds a two-parameter scWGA error model (**ADO rate δ** and **amplification/sequencing error ε**), and plugs it into **RAxML-NG**. The payoff is a finite-site maximum-likelihood method that inherits RAxML-NG's tree search, multithreading, **bootstrap branch support**, and ancestral-state reconstruction — and that can take **genotype likelihoods** (VCF PL field) instead of hard calls, which is what makes it win at low (5×) depth.

## Key claims

- **Genotype-level, not presence/absence, model.** Prior SNV tree methods (OncoNEM, SCITE, SiFit) use at most a ternary state space (0/1/2 mutant alleles); GT16 models all 16 phased genotypes, and handles unphased data (10 states) by treating the phase of heterozygotes as ambiguous. A cheaper unphased **GT10** model is ~2× faster and gave very similar accuracy despite a theoretically incorrect reversibility assumption.
- **No infinite-sites assumption and no root genotype assumption.** CellPhy is finite-site; the tree is unrooted and rooted a posteriori with an outgroup (e.g., healthy cells), whereas SiFit assumes a reference-homozygous root.
- **Error model distinguishes ADO from amplification/sequencing error** and permits both in one genotype (e.g., an error turning a homozygous mutant into a heterozygote); at most one ERR per genotype is allowed since ε is ~10⁻³–10⁻⁵.
- **Most accurate across six simulation scenarios** (40–1000 cells, 250–50,000 SNVs/sites; ISM, finite-site, COSMIC signatures 1 and 5, NGS read counts, doublets), especially when ADO and genotype errors are high. Benchmarked against TNT, OncoNEM, SASC, SPhyR, infSCITE, SiFit, SCIPhI and ScisTree; OncoNEM, SASC and SPhyR were dropped after a preliminary round for poor accuracy (OncoNEM trees were 50–90% polytomies), long runtimes, or (SPhyR) memory-corruption crashes.
- **Genotype likelihoods matter at low depth.** At 5× simulated NGS depth, CellPhy-GL was much better than competitors; at 30× and 100× the differences shrank. SCIPhI and ScisTree degraded at higher depth in the presence of single-cell noise.
- **Scale.** With up to 1000 cells and 50,000 SNVs, infSCITE jobs were still running after 1 month, and SCIPhI/ScisTree gave no result for the largest datasets after >100 h per replicate. SCIPhI held a constant ~0.4 accuracy with many unresolved nodes.
- **Speed.** Parsimony-based TNT was fastest by ≥2 orders of magnitude but lost accuracy under scDNA-seq errors; CellPhy (ML and GL) and ScisTree were next, ~1–2 orders of magnitude faster than SiFit, SCIPhI or infSCITE. Single-threaded CellPhy with 100 bootstraps is still faster than infSCITE.
- **Error-rate estimation**: genotyping error estimated with MSE 0.00003–0.002; ADO estimates more variable and tending to underestimate (MSE 0.002–0.02).
- **Empirical re-analysis of metastatic CRC (L86, 86 cells from Leung et al. patient CRC2, 598 SNVs via SC-Caller):** all metastatic cells formed one well-supported clade — **monoclonal seeding of the liver metastasis**, siding with SCARLET's conclusion against the polyclonal seeding inferred by the original SCITE analysis and by SiCloneFit. SCIPhI and ScisTree also recovered a single metastatic clade; infSCITE and TNT did not group tumor cells as a clade.
- **Sanity check on clonal (non-WGA) data:** on 140 single-cell-derived HSPC colonies (LS140, 127,884 SNVs), CellPhy's ML estimates of both error and ADO were **zero**, as expected without amplification, with very high bootstrap values.

## Methods / evidence

Simulations with **CellCoal** (coalescent genealogies from an exponentially growing population, rate variation across lineages, ADO/amplification/sequencing errors and doublets applied either to genotypes or to read counts); 100 replicates per parameter combination, 19,400 cell samples in total (only 20 replicates in the largest scenario). Accuracy = 1 − normalized Robinson–Foulds distance. Multi-allelic sites were recoded for ternary-input tools with "keep", "remove" or "missing" strategies; "missing" was best and used thereafter. Empirical data: an in-house CRC dataset (CRC24, 24 Ampli1-amplified cells from two tumor regions, ~6× WGS, 17,851 SNVs), L86, 15 neurons (E15, 242 SNVs), and LS140. Calling with SC-Caller; its non-standard PL field must be converted before CellPhy-GL can use it.

Weight: strong and broad simulation design with an explicit growing-population model, but the simulator (CellCoal) and the method come from the same group (Posada lab), so scenarios may favour CellPhy's assumptions (synthesis). Empirical datasets have no ground truth; the tree comparisons (nRF 0.50–0.86 between CellPhy and other tools on CRC24) show disagreement, not correctness.

## Surprising or load-bearing bits

- **Bootstrap support is the practical differentiator.** For E15 neurons, most branches had <50% support — CellPhy says "not enough SNVs" where other tools return a confident-looking tree with no support measure. The paper states that infSCITE, SiFit, SCIPhI and ScisTree do not assess branch support.
- **Demographic growth makes trees hard**: short internal branches and long terminal branches need hundreds to tens of thousands of SNVs depending on cell number — a limitation the authors say applies to all methods.
- **On CRC24, tumor-interior non-stem cells had longer branches than stem cells**, suggesting a possible evolutionary-rate difference between cell types.
- The ternary-coding step that every other tool requires is itself a source of accuracy loss on multi-allelic finite-site data — CellPhy sidesteps it by modelling nucleotides directly (synthesis).
- **Doublets hurt all methods**; the authors recommend scDNA-seq doublet removal upstream rather than modelling it.

## Concepts touched

- [[phylogenetic-inference]] — finite-site ML with RAxML-NG search and bootstrap support for somatic SNV trees.
- [[allele-dropout]] — explicit ADO parameter δ, estimable from data.
- [[single-cell-variant-calling]] — consumes genotype likelihoods; flags caller-specific PL semantics (SC-Caller).
- [[doublet-detection]] — doublets degrade tree accuracy; filtering recommended.
- [[mutational-signatures]] — COSMIC signatures 1 and 5 used to simulate realistic substitution spectra.
- [[scwga]] — the error model targets WGA-specific ADO and amplification error.

## Connections to other sources

- Benchmarked competitors with wiki summaries: [[jahn-2016-scite]] (infSCITE extends SCITE), [[zafar-2017-sifit]], [[singer-2018-sciphi]], [[ross-2016-onconem]], [[el-kebir-2018-sphyr]].
- **Sides with** [[satas-2020-scarlet]] (monoclonal liver-metastasis seeding in CRC2) against SiCloneFit's polyclonal reading.
- Uses [[dong-2017-sccaller]] for SNV calling and notes [[zafar-2016-monovar]] produces standard PL fields usable by CellPhy-GL.
- Re-analyses [[lee-six-2018-hsc-dynamics]] colonies (LS140) and 15 neurons from Evrony et al. 2015 (E15; no wiki summary); motivated by developmental phylogenies such as [[coorens-2021-nature]].
- Same lab's review of the upstream calling problem: [[valecha-2022-scsnv-review]].
- Listed among natural-variant SNV tree methods in [[wang-2026-multimodal-lineage-computational]].

## Open questions

- The authors flag joint SNV+CNV Markov modelling as unsolved: overlapping CNVs break the site-independence assumption CellPhy relies on.
- Classical phylogenetic assumptions (reversibility, stationarity, context independence) may be poor fits at somatic time scales; dropping them is noted as future work.
- With 242 SNVs across 15 neurons nothing is well supported — how many somatic SNVs per cell (and how accurate) are needed for a trustworthy normal-tissue tree is left open (synthesis).

## Related

- [[phylogenetic-inference]] · [[jahn-2016-scite]] · [[zafar-2017-sifit]] · [[40-Topics/single-cell-lineage-tracing]] · [[40-Topics/cancer-clonal-evolution]]
