---
type: summary
title: "Lähnemann et al. 2020 — Eleven grand challenges in single-cell data science"
source: "[[00-Sources/papers/Eleven grand challenges in single-cell data science]]"
source_kind: paper
author: "David Lähnemann, Johannes Köster, Ewa Szczurek, Davis J. McCarthy, Stephanie C. Hicks, Mark D. Robinson, Catalina A. Vallejos, Kieran R. Campbell, Niko Beerenwinkel, Ahmed Mahfouz, Luca Pinello, Pavel Skums, Alexandros Stamatakis, ... Oliver Stegle, Fabian J. Theis, ... Alexander Schönhuth (last author)"
published: 2020-02-07
ingested: 2026-10-07
doi: "10.1186/s13059-020-1926-6"
journal: "Genome Biology 21:31"
tags: [review, perspective, single-cell-data-science, scDNA-seq, scRNA-seq, imputation, variant-calling, WGA, phylogenetics, population-genetics, data-integration, benchmarking, simulation]
entities: ["[[20-Entities/oliver-stegle]]", "[[20-Entities/fabian-theis]]"]
concepts: ["[[single-cell-variant-calling]]", "[[allele-dropout]]", "[[phylogenetic-inference]]", "[[copy-number-variation]]", "[[imputation]]", "[[multimodal-integration-methods]]", "[[reference-atlas-mapping]]", "[[trajectory-inference]]", "[[scwga-chemistries]]", "[[intratumor-heterogeneity]]", "[[spatial-multiomics]]"]
topics: ["[[computational-methods]]", "[[cancer-clonal-evolution]]", "[[scdna-seq]]", "[[single-cell-multiomics]]"]
---

**Citation:** Lähnemann et al. (2020) — *Eleven grand challenges in single-cell data science* — *Genome Biology* 21:31. [DOI](https://doi.org/10.1186/s13059-020-1926-6)

# Lähnemann 2020 — Eleven grand challenges

> A community perspective by about fifty authors. It argues that single-cell sequencing has become a data-science field ("SCDS") and lists eleven open problems, each with motivation, status and open problems. Three recurring themes run through all of them: **choosing the right level of resolution**, **quantifying and propagating measurement uncertainty**, and **scaling to more cells and more features**. The challenges fall into transcriptomics (I–V), genomics (VI), phylogenomics (VII–IX) and two overarching ones (X integration, XI benchmarking). For this wiki, the scDNA half is the load-bearing part. It frames scDNA analysis as variant calling under WGA artefacts (VI), followed by phylogenetic (VII–VIII) and population-genetic (IX) inference that is constrained by the fact that **somatic evolution is asexual**.

## Key claims

**Transcriptomics (I–V)**
- **I Sparsity.** The authors recommend *against* "dropout" as a catch-all for observed zeros, because it conflates technical and biological zeros. They define three imputation families: (A) model-based, (B) data-smoothing, (C) data-reconstruction (matrix factorisation, autoencoders), plus (T) imputation using external references. The core risk is **circularity**: imputation from internal information can inflate correlations and create false positives downstream.
- **II Differential patterns.** Differential tests usually ignore the uncertainty in cluster assignment and the "double use" of the same data for clustering and testing. Single-cell-specific DE methods do not uniformly beat bulk methods.
- **III Reference atlases**, **IV trajectories beyond transcriptomics** and **V spatial patterns**. For epigenomic trajectories, features are ill-defined, and inputs as small as two copies of each chromosome make the data sparser than scRNA-seq.

**Genomics (VI)**
- **WGA trade-off.** PCR-based WGA gives more uniform coverage (best for CNV) but uses error-prone thermostable polymerases. MDA with Φ29 has lower error rates (best for SNV) but stronger allelic bias.
- **Three failure modes.** Imbalanced allele proportions, allele dropout (the extreme case), and site dropout (neither allele amplified).
- **Asexuality as a modelling asset.** There is no recombination in mitosis, so cells share one lineage tree, which can constrain variant calling.
- **Status of callers.** Monovar pools across cells; SCcaller and SCAN-SNV model local allelic imbalance from nearby germline hets. "Single-cell genotyper", "SciCloneFit" and SCIΦ jointly call mutations and infer trees. For CNVs: AneuFinder (HMM), Ginkgo (CBS, web-only), and HoneyBADGER and inferCNV from scRNA-seq.
- **Gaps (as of 2020).** "We are not aware of any scDNA-seq variant callers" for indels. There was no systematic comparison of SNV or CNV callers beyond the tools' own papers. FDR control via direct modelling of amplification is an open goal.

**Phylogenomics (VII–IX)**
- **VII Scale.** Phylogenetic inference is NP-hard under most scoring criteria, and exhaustive search is infeasible beyond ~20 cells. Excluding invariant sites (ascertainment bias) has been shown, in closely related populations, to change branch lengths but not topology.
- **VIII Variant types.** OncoNEM and SCITE use binary presence/absence, with false negatives orders of magnitude more likely than false positives. SiFit allows infinite-sites violations; Dollo-k allows k losses. RAxML-NG has been extended with a **10-state unphased diploid genotype model** plus an ADO/error model. It beat a ternary model only slightly, and only at very high error rates (10–50%), although a preliminary analysis suggests gains grow with more cells and SNVs. CNV phylogenies are hard because events overlap (breakage-fusion-bridge, missegregation) and realistic transition probabilities are needed; several profile-distance problems are NP-hard.
- **IX Population genetics.** Open questions on early vs late and single- vs multi-cell metastatic seeding. Needed parameters are fitness, birth, death and mutation rates per subclone. SCIFIL fits fitness landscapes on scDNA-based trees. dN/dS is relatively insensitive within a species. Laser capture microdissection has isolated hundreds of cells from sections for CNV analysis.

**Overarching (X–XI)**
- **X Integration.** Six setups: 1S, +S, +X+S, +M1C (multiple modalities in the same cell), +M+C (different modalities in different cells), +all. "**Measurement linkage**" (e.g., copy number raising expression) is unaddressed for same-cell modalities. clonealign, cardelino and MATCHER are examples of +M+C linking.
- **XI Benchmarking.** Ground-truth datasets are scarce. scRNA simulators with validation exist (Splatter, powsimR, SymSim; countsimQC for checking simulations), but "no such tool is available for scDNA-seq data". The authors call for community challenges along the lines of CASP, CAMI and DREAM.

## Methods / evidence

A narrative review and research agenda. No new data. Tables of WGA improvements, imputation methods, cell atlases and integration approaches are referenced but not reproduced in the clipping.

Weight: authoritative as a map of problems circa early 2020, with authors spanning the tools it discusses (e.g., Beerenwinkel, Jahn and Kozlov on SCITE/SCIΦ/RAxML-NG lines). Its "status" sections are a dated snapshot, and several gaps have since been partly filled (see Open questions). (synthesis)

## Surprising or load-bearing bits

- **Lineage tree as a variant-calling prior.** Cells are related by an unknown tree, so calling and tree inference should be done jointly. This is the conceptual root of the joint caller/phylogeny tools in this wiki. (synthesis)
- **"Dropout" is an overloaded word.** Allele dropout in scDNA and zero counts in scRNA are different phenomena; the paper's terminology split is worth adopting. (synthesis)
- **A richer genotype model buys little at realistic error rates.** The 10-state vs ternary result suggests that, under current data quality, model complexity is not the bottleneck.
- **Integration without same-cell data (+M+C) depends on clone identity.** Linking expression to genotype in tumours requires knowing the clonal structure, which "only performing scDNA-seq experiments can definitively reveal".

## Concepts touched

- [[single-cell-variant-calling]] / [[allele-dropout]] — taxonomy of WGA failure modes and caller strategies.
- [[scwga-chemistries]] — PCR vs MDA error/uniformity trade-off.
- [[phylogenetic-inference]] — NP-hardness, infinite-sites violations, genotype models, CNV phylogeny.
- [[copy-number-variation]] — CNV calling and CNV phylogeny as open problems.
- [[imputation]] — the A/B/C/T taxonomy and the circularity critique.
- [[multimodal-integration-methods]] — the six-setup integration taxonomy and measurement linkage.
- [[reference-atlas-mapping]], [[trajectory-inference]], [[spatial-multiomics]] — challenges III–V.

## Connections to other sources

- Tools it discusses that the wiki covers: [[zafar-2016-monovar]], [[dong-2017-sccaller]], [[luquette-2019-natcomm]] (SCAN-SNV), [[zafar-2019-siclonefit]], [[singer-2018-sciphi]], [[jahn-2016-scite]], [[ross-2016-onconem]], [[zafar-2017-sifit]], [[el-kebir-2018-sphyr]] (Dollo-k), [[bakker-2016-aneufinder]], [[tickle-2019-infercnv]], [[wolf-2019-paga]], [[haghverdi-2018-mnn]], [[zahn-2017-dlp]].
- The RAxML-NG single-cell extension it previews appears as [[kozlov-2022-cellphy]], whose simulations use CellCoal ([[kozlov-2022-cellphy]]).
- The indel gap is later addressed for PTA data by [[luquette-2021-scan2]]; ProSolo ([[lahnemann-2021-natcomm]], same first author) addresses FDR-controlled calling with bulk pairing.
- Later reviews of the same terrain: [[valecha-2022-scsnv-review]], [[lu-2024-cnaphylogeny-review]], [[heumos-2023-best-practices]].

## Open questions

- Several 2020 "gaps" need re-checking against the later corpus: scDNA indel calling (cf. [[luquette-2021-scan2]]), scDNA simulators (CellCoal is used in [[kozlov-2022-cellphy]]), and systematic caller benchmarks. (synthesis)
- Measurement linkage in same-cell multi-omics (e.g., DNA + RNA) remains a modelling challenge the review flags but does not solve.
- Whether heterotachy-aware and population-genetic models can be fitted at single-cell scale is still open.

## Related

- [[computational-methods]] · [[phylogenetic-inference]] · [[single-cell-variant-calling]] · [[40-Topics/cancer-clonal-evolution]]
