---
type: summary
title: "Kang et al. 2022 — SIEVE: joint inference of single-nucleotide variants and cell phylogeny from single-cell DNA sequencing data"
source: "[[00-Sources/papers/SIEVE_ joint inference of single-nucleotide variants and cell phylogeny from single-cell DNA sequencing data]]"
source_kind: paper
author: "Senbai Kang, Nico Borgsmüller, Monica Valecha, Jack Kuipers, Joao M. Alves, Sonia Prado-López, Débora Chantada, Niko Beerenwinkel, David Posada, Ewa Szczurek"
published: 2022-11-30
ingested: 2026-10-07
doi: "10.1186/s13059-022-02813-9"
journal: "Genome Biology 23:248"
tags: [SIEVE, phylogenetics, finite-sites-assumption, acquisition-bias, branch-lengths, allelic-dropout, BEAST2, Dirichlet-multinomial, single-cell-SNV-calling, colorectal-cancer, TNBC]
entities: []
concepts: ["[[30-Concepts/phylogenetic-inference]]", "[[30-Concepts/single-cell-variant-calling]]", "[[30-Concepts/allele-dropout]]", "[[30-Concepts/monovar]]", "[[30-Concepts/intratumor-heterogeneity]]", "[[30-Concepts/copy-number-variation]]"]
topics: ["[[40-Topics/cancer-clonal-evolution]]", "[[40-Topics/single-cell-lineage-tracing]]", "[[40-Topics/mosaic-variant-calling]]", "[[40-Topics/computational-methods]]"]
---

**Citation:** Kang et al. (2022) — *SIEVE: joint inference of single-nucleotide variants and cell phylogeny from single-cell DNA sequencing data* — *Genome Biology* 23:248. [DOI](https://doi.org/10.1186/s13059-022-02813-9)

# Kang 2022 — SIEVE

> SIEVE (SIngle-cell EVolution Explorer) puts scDNA-seq tumour phylogenetics inside a proper **statistical phylogenetic model** (rate matrix + topology + branch lengths, BEAST 2 / MCMC) and makes **variant calling a by-product of the tree**. It reads raw counts of all four nucleotides at candidate sites, works under the **finite-sites assumption** with four genotypes (0/0, 0/1, 1/1, 1/1′), and — the authors' claimed first — **corrects branch lengths for acquisition bias** using the count of invariant background sites. Branch lengths come out in expected somatic mutations per site, and ADO is called explicitly through a coverage model.

## Key claims

- **Joint inference beats pipelines.** Methods that first call variants with Monovar and then build trees (CellPhy, SiFit) inherit calling errors; methods that do both but under the ISA without branch lengths (SCIPhI) break when ISA is violated. SIEVE outperformed CellPhy and SiFit on branch-score distance in every simulated scenario, and was the most robust on normalised RF distance across cell number, mutation rate and coverage quality.
- **Acquisition bias is real.** Using only variant sites overestimates branch lengths; SIEVE's BS distance had a negative nonlinear association with the number of background sites, "proving the necessity" of enough background sites for accurate branch lengths.
- **FSA models also handle ISA data.** At mutation rate 10⁻⁶ (<0.1% double mutants, ≤1% parallel-mutation sites) all methods reached median normalised RF ≈ 0.15–0.3. At 8 × 10⁻⁶ and 3 × 10⁻⁵ (2–8% and 10–27% sites with parallel mutations), SCIPhI was reasonable at 40 cells but dropped dramatically at 100 cells.
- **Variant calling**: single-mutant recall higher than SCIPhI by 0.16–18.55% and Monovar by 28.89–71.74%, with precision comparable to Monovar. SCIPhI miscalled 0/0 as 0/1 under high mutation rates while overestimating ADO; SIEVE avoids this by modelling coverage overdispersion. Double-mutant calls: higher recall than Monovar, precision almost 1, FPR almost 0 (SCIPhI cannot call double mutants).
- **ADO calling only works with good coverage**: mean F1 0.86 (medium) and 0.93 (high coverage quality) but **0.10 for low quality — "typical for current scDNA-seq data"**, so ADO calls were not reported for real data.
- **Robust to CNAs despite a diploid model**: simulated CNAs (copy number 0–10 at ⅓ or ⅔ of sites) barely changed BS distance; topology worsened for all methods, and with many CNAs, *including* CNA sites helped. Monovar's F1 dropped with CNAs; SIEVE's and SCIPhI's did not.
- **Real data**: CRC28 (new; 28 tumour cells, three biopsies, Ampli1 WGA, ~6× scWGS): 8,470 candidate sites, 1,163,335,103 background sites, three biopsy-matched clades, only single mutations on branches (no ISA violation detected); clonal trunk includes *APC*. TNBC16 (scWES, [[wang-2014-nuc-seq|Wang 2014]]): 44 homozygous coincident double mutations, 9 homozygous single-mutation additions, 2 parallel single mutations, 7 single back mutations. CRC48 (scWES, Wu 2017): normal cells inside tumour biopsies identified; parallel mutations in *CHD3* and *PLD2* across polyp and tumour; *MLH3* on the tumour-subclone branch. **Double mutants rare in CRC, frequent in TNBC.**
- **Speed**: not competitive single-threaded, but in default multi-thread mode faster than other Bayesian methods and similar to CellPhy (ML + bootstrap); SiFit required "tremendous amounts of memory".

## Methods / evidence

Model: continuous-time Markov chain on 4 genotypes (back-mutation rate ⅓ of forward), Gamma rate heterogeneity, Kingman coalescent prior with exponential growth, a **trunk** (root fixed at 0/0 with a single child = MRCA, so no outgroup is needed). Read model: negative binomial coverage scaled by number of sequenced alleles (1 if ADO) and per-cell size factors; Dirichlet-multinomial nucleotide counts with effective error rate *f* and genotype-dependent overdispersion. Background likelihood approximated (all 0/0, no tree) to estimate *f* and wildtype overdispersion cheaply. Two-stage MCMC (acquisition-bias correction off, then on). Variants, ADO and branch mapping by max-sum on the MCC tree. Candidate sites from **DataFilter** (beta-binomial LRT, SCIPhI-like, modified to admit double mutants; normal cells remove germline). Benchmark: modified CellCoal simulator, 18 scenarios × 20 repeats, 40 or 100 cells; low-quality scenario mimics CRC28. Comparators: CellPhy and SiFit (on Monovar calls), SCIPhI, Monovar — SiFit and Monovar given true error rates as priors.

Weight: the simulator shares SIEVE's own coverage model (Eqs. 3–6), which favours SIEVE. Real-data validation is concordance with biopsy geography and other methods, not ground truth. Diploid assumption and at most one ADO per site per cell are stated limitations.

## Surprising or load-bearing bits

- **Branch lengths need the sites that did *not* mutate.** Every scDNA tree method that ignores background sites systematically inflates evolutionary distance; this is a cheap fix (a count of invariant sites) with large effect. Targeted panels can supply a user-specified background count.
- **ADO is identifiable only through coverage**, and at present-day coverage quality the identification fails (F1 0.10). The model is ahead of the data — the honest limit is chemistry, not statistics. (synthesis)
- **ISA violations are tumour-type dependent**: none detected in CRC28, many kinds in TNBC16. Whether to use an FSA model is therefore an empirical, per-dataset question — and FSA costs nothing when ISA holds.
- **Hierarchical clustering is not phylogeny.** The authors note the original TNBC study built its SNV tree by clustering, which assumes ultrametricity and gives no node support.

## Concepts touched

- [[phylogenetic-inference]] — statistical (rate-matrix, branch-length) phylogenetics for scDNA under FSA, with acquisition-bias correction.
- [[single-cell-variant-calling]] — genotypes called through the tree, distinguishing single from double mutants.
- [[allele-dropout]] — modelled as a hidden number-of-sequenced-alleles variable, separable from homozygosity only via coverage.
- [[monovar]] — the phylogeny-free baseline; noisier calls, more missing entries, more (likely false) double mutants.
- [[copy-number-variation]] — tolerated rather than modelled; the authors list CNAs and indels as future extensions.

## Connections to other sources

- Direct comparators: [[singer-2018-sciphi]] (joint, ISA), [[zafar-2017-sifit]] (FSA, on called variants), [[kozlov-2022-cellphy]] (ML FSA on called variants), [[zafar-2016-monovar]].
- ISA-based tree inference it generalises: [[jahn-2016-scite]], [[malikic-2019-phiscs]], [[el-kebir-2018-sphyr]], [[ross-2016-onconem]].
- Dataset source: [[wang-2014-nuc-seq]] (TNBC16). Co-author Valecha's review of the same calling problem: [[valecha-2022-scsnv-review]].
- Later work in the same Bayesian-phylogenetic line: [[seidel-2026-sciphy]], [[seidel-2022-tidetree]] (synthesis — not cited by the source).
- CNA-based phylogenetics that SIEVE does not cover: [[kaufmann-2022-medicc2]], [[lu-2024-cnaphylogeny-review]].

## Open questions

- How far does the simulator–model match (shared coverage model) inflate the benchmark margin?
- Extension to CNAs and indels while separating evolutionary deletions from ADO — flagged by the authors, unresolved.
- Is the high double-mutant rate in TNBC16 biology (LOH, hypermutable motifs, retained mutability) or a scWES/MDA artefact? The authors offer biological explanations but cannot discriminate.
- Molecular-clock compatibility could time divergences, but only if the mutation rate is known — not demonstrated.

## Related

- [[phylogenetic-inference]] · [[singer-2018-sciphi]] · [[kozlov-2022-cellphy]] · [[40-Topics/cancer-clonal-evolution]]
