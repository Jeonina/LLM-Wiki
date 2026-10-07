---
type: summary
title: "Sollier et al. 2023 — COMPASS: joint copy number and mutation phylogeny reconstruction from amplicon single-cell sequencing data"
source: "[[00-Sources/papers/COMPASS_ joint copy number and mutation phylogeny reconstruction from amplicon single-cell sequencing data]]"
source_kind: paper
author: "Etienne Sollier, Jack Kuipers, Koichi Takahashi, Niko Beerenwinkel, Katharina Jahn (corresponding)"
published: 2023-08-15
ingested: 2026-10-07
doi: "10.1038/s41467-023-40378-8"
journal: "Nature Communications 14:4921"
tags: [COMPASS, tumour-phylogeny, SNV, CNA, CNLOH, Tapestri, amplicon-sequencing, targeted-scDNA-seq, AML, MPN, doublets, convergent-evolution, BiTSC2, SCITE]
entities: []
concepts: ["[[phylogenetic-inference]]", "[[copy-number-variation]]", "[[allele-dropout]]", "[[doublet-detection]]", "[[intratumor-heterogeneity]]", "[[jak2-v617f]]", "[[myeloproliferative-neoplasm]]"]
topics: ["[[cancer-clonal-evolution]]", "[[hematopoietic-malignancies]]", "[[scdna-cancer-applications]]", "[[computational-methods]]"]
---

**Citation:** Sollier et al. (2023) — *COMPASS: joint copy number and mutation phylogeny reconstruction from amplicon single-cell sequencing data* — *Nature Communications* 14:4921. [DOI](https://doi.org/10.1038/s41467-023-40378-8)

# Sollier 2023 — COMPASS

> High-throughput **targeted (amplicon) scDNA-seq** such as Mission Bio Tapestri genotypes thousands of cells over a small gene panel with PCR rather than MDA, so in principle both SNVs and copy-number changes can be read from the same cells. COMPASS is a likelihood model and simulated-annealing search for a **joint tree of SNVs and CNAs (gains, losses and copy-neutral LOH)** that explicitly models the **uneven per-amplicon coverage** that breaks the only previous joint method (BiTSC²). On 123 AML patients it recovers known AML copy-number events, validates clonal ones against bulk data, finds subclonal ones bulk cannot see, and exposes **convergent evolution** missed by SNV-only trees.

## Key claims

- **Model.** Events: SNVs (acquired once, lossable multiple times — Dollo) and CNAs per region (gene = grouped amplicons), at most once per lineage. Input: per-cell ref/alt read counts at variants and total reads per region. Region depth is negative binomial with a per-region weight ρₖ (primer efficiency); allelic counts are beta-binomial with per-variant dropout rates; doublets optionally modelled as in ∞SCITE. Cell-to-node attachments are marginalised (as in SCITE) but with **learned node weights** rather than a uniform prior; node weights and dropout rates are fit by EM inside each step. Germline SNPs can be included to sharpen CNA calls and are placed at the root.
- **Two-stage search reduces false CNAs.** First infer a tree without gains/losses; root-attached cells estimate ρₖ and candidate CNA regions are those whose coverage differs from the root; then search again allowing CNAs only there. Consequence: CNAs in subclones **not supported by an SNV or LOH** are mostly missed, but the false-positive rate is very low.
- **Simulations (Tapestri-like, 3000 cells, 30 regions, 6-node trees).** COMPASS was best in all settings by MP3 similarity. BiTSC² was close with uniform coverage but dropped sharply with non-uniform coverage and had a very high CNA false-positive rate; it also performed worse with many cells and was very slow (subsampled to 200 cells). SCITE degraded when CNAs were present and when clone sizes were unequal — even without CNAs COMPASS slightly outperformed it because of the non-uniform attachment prior. All methods were robust to doublets except at very high doublet rates.
- **Unexplained amplicon-coverage correlations** in Tapestri data (not previously reported) could mimic clones; simulated correlations did not affect COMPASS.
- **AML cohort (123 patients; 67 samples on a 50-amplicon/19-gene panel and 53 on a 279-amplicon/37-gene panel).** CNAs in 42 samples: 31 CNLOH, 26 deletions, 12 gains. Most common: CNLOH of *FLT3* (12 samples, 9.8%) and *EZH2* deletion (8, 6.5%). All *JAK2* V617F samples also had CNLOH, often in a very small subclone. *TP53* mutation associated with gains/losses (5 of 9; one-sided Fisher p = 0.009, OR 6.96).
- **Orthogonal validation.** Among 8 samples with gains/losses and bulk data (SNP array or 297-gene targeted panel), all majority-clone CNAs were confirmed except one *ASXL1* gain; in 85 bulk-sequenced samples only one bulk CNA in panel regions was missed (trisomy 8). CNLOH vs ASCAT on 32 SNP arrays: 6 concordant, 1 COMPASS-only, 4 ASCAT-only (in untargeted regions or without SNVs).
- **What single-cell adds.** A subclonal *TP53* loss in ~5% of cells (AML-59-001) invisible in bulk; subclonal *JAK2* CNLOH (bulk VAF cannot tell 5% homozygous from 10% heterozygous); ordering, e.g. trisomy 8 after *DNMT3A*/*IDH2* but before *FLT3*/*NRAS*.
- **Convergent evolution.** AML-101-001: two independent chromosome-17 deletions plus parallel *KRAS* and *PTPN11* clones, interpreted as convergence on RAS activation via *NF1* loss; MPN1: an *EZH2* deletion and an *EZH2* p.N693K mutation in different subclones. Applied also to 4 *TP53*-mutated AML patients before/after venetoclax (EZH2 loss in all four; TP53-wt fraction fell 46% → 18% in seven days in one) and 8 *TP53*-mutated MPNs (JAK2 CNLOH in three; more compact trees without recurrences, attributed to the doublet model).

## Methods / evidence

Simulation benchmark against BiTSC² (the only other joint SNV+CNA method) and SCITE (SNV-only), scored by MP3 tree similarity, CNA FP/FN rates and cell-assignment accuracy; re-analysis of three published Tapestri cohorts (no new data); bulk CNVkit and SNP-array ASCAT for orthogonal validation. Implemented in C++ (GPL3).

Weight: credible for amplicon data — the uneven-coverage model is the decisive feature and is well motivated by the data. Limits acknowledged: CNA-only subclones are largely undetectable; detection depends on panel content (no chromosome-8 amplicon on the small panel; one low-coverage 5q amplicon); evaluated only on myeloid neoplasms; penalty parameters set empirically.

## Surprising or load-bearing bits

- **The design trades sensitivity for specificity on purpose**, mirroring CHISEL in the opposite direction: COMPASS sees CNAs only in SNV-marked subclones; CHISEL (shallow WGS) sees SNVs only in CNA-marked subclones. Each data type's blind spot is the other's strength.
- **SCITE's uniform attachment prior is a real bias**, not just a simplification: with unequal clone sizes it misplaces a minority mutation below a majority one (the two *RUNX1* mutations case).
- **Convergence is more common than SNV-only trees suggest** — a claim with clinical weight if parallel routes to the same pathway predict resistance. (synthesis)
- Minor inconsistency: the cohort is described as 123 patients while the two panel counts given sum to 120 samples. (synthesis — the clipping does not reconcile this)

## Concepts touched

- [[phylogenetic-inference]] — joint SNV+CNA Dollo-style tree with learned node weights for amplicon data.
- [[copy-number-variation]] — CNA and CNLOH calling from targeted read depth plus allelic imbalance.
- [[allele-dropout]] — per-variant dropout rates inferred by EM.
- [[doublet-detection]] — doublet model explains apparent mutation recurrences.
- [[jak2-v617f]] / [[myeloproliferative-neoplasm]] — subclonal JAK2 CNLOH resolved only at single-cell level.
- [[intratumor-heterogeneity]] — convergent evolution on RAS and EZH2.

## Connections to other sources

- SNV-only tree methods it builds on and compares with: [[jahn-2016-scite]], [[singer-2018-sciphi]] (read-count input, like COMPASS), [[zafar-2017-sifit]], [[malikic-2019-phiscs]].
- Joint/related CNA–SNV approaches: [[satas-2020-scarlet]] (CNA-constrained LOH), [[zaccaria-2021-chisel]] (SNVs in CNA-defined clones), [[kaufmann-2022-medicc2]] and [[wang-2021-medalt]] (CNA-only phylogenies).
- Platform and data: [[pellegrino-2018-tapestri]] (targeted droplet scDNA-seq). Related Beerenwinkel-group methods: [[kang-2022-sieve]], [[kuipers-2025-scicone]].
- Reviews: [[lu-2024-cnaphylogeny-review]], [[mallory-2020-cna-review]].

## Open questions

- Can CNA-only subclones be recovered from amplicon data at all, or does this require wider panels? The authors expect larger targeted regions to help.
- What causes the strong cross-amplicon coverage correlations in Tapestri data?
- Whole-genome doubling and solid tumours are untested; the authors sketch adding a doubling event.

## Related

- [[phylogenetic-inference]] · [[40-Topics/cancer-clonal-evolution]] · [[pellegrino-2018-tapestri]] · [[jahn-2016-scite]]
