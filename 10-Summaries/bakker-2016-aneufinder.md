---
type: summary
title: "Bakker et al. 2016 — Single-cell sequencing reveals karyotype heterogeneity in murine and human malignancies (AneuFinder)"
source: "[[00-Sources/papers/Single-cell sequencing reveals karyotype heterogeneity in murine and human malignancies]]"
source_kind: paper
author: "Bjorn Bakker, Aaron Taudt, Mirjam E. Belderbos, David Porubsky, Diana C. J. Spierings, ... Peter M. Lansdorp, Maria Colomé-Tatché, Floris Foijer (corresponding)"
published: 2016-05-31
ingested: 2026-08-10
doi: "10.1186/s13059-016-0971-7"
journal: "Genome Biology"
tags: [AneuFinder, CNV-calling, HMM, aneuploidy, chromosomal-instability, T-ALL, B-ALL, karyotype-heterogeneity, Mps1]
entities: []
concepts: ["[[copy-number-variation]]", "[[chromosomal-instability]]", "[[chromosomal-instability]]", "[[intratumor-heterogeneity]]", "[[scwga]]", "[[mappability]]", "[[quality-control-metrics]]"]
topics: ["[[cancer-clonal-evolution]]", "[[scdna-cancer-applications]]", "[[computational-methods]]"]
---

**Citation:** Bakker et al. (2016) — *Single-cell sequencing reveals karyotype heterogeneity in murine and human malignancies* — *Genome Biology* 17, 115. [DOI](https://doi.org/10.1186/s13059-016-0971-7)

# Bakker 2016 — AneuFinder

> A biological puzzle resolved by a tool. Chromosomally unstable *Mps1*-truncated, *p53*-null mouse lymphomas showed **clonal-looking karyotypes by array CGH** despite mis-segregation in virtually every division. Either the tumours suppress instability, or selection outruns it. Single-cell whole-genome sequencing plus AneuFinder shows the second: **the population average is clonal; the individual cells are not**.

## Key claims

- **The setup.** Truncating the spindle-assembly-checkpoint kinase *Mps1* in T cells causes chromosomal instability but not malignancy; combined with *p53* loss it markedly accelerates lymphomagenesis. aCGH across a large cohort of the resulting T-ALLs showed **highly similar karyotypes** — recurrent gains of chromosomes 4, 9, 14 and 15 — implying clonal selection, which is hard to reconcile with per-division mis-segregation.
- **The resolution.** Sequencing 25 primary T-ALL cells from one such lymphoma, the **cumulative "artificial bulk" file exactly reproduced the aCGH profile**, while individual cells carried many additional alterations. Manual annotation found **56% of cells had a unique karyotype** — heterogeneity aCGH could not see.
- **AneuFinder's four design features**: no external reference required; automated CNV quantification by **Hidden Markov model**; stringent semi-automated per-library quality control; BED output for genome-browser inspection of small events.
- **The algorithm.** Reads counted in **variable-size bins chosen by mappability, averaging 1 Mb**, then GC-corrected. An HMM over states from **nullisomy to decasomy** — all modelled as negative binomial except nullisomy, modelled as a delta distribution — is fitted by Baum–Welch, and each bin takes the maximum-posterior state.
- **Quality control is a first-class step, not an afterthought.** Roughly 11% of libraries are poor quality. AneuFinder computes **spikiness** (bin-to-bin read-count variation), model log-likelihood, number of contiguous same-state segments, and the **Bhattacharyya distance** between the fitted negative binomials, then clusters libraries on these measures and keeps the best cluster — retaining ~89% of libraries.
- **Two derived scores**: an **aneuploidy score** (divergence from euploidy) and a **heterogeneity score** (number of cells with distinct copy-number profiles), making karyotype heterogeneity a quantity rather than an impression.
- **Comparison with Ginkgo**: copy-number calls were generally concordant; **AneuFinder is more sensitive to small CNVs, Ginkgo more robust to sequencing noise** — an explicit sensitivity/robustness trade rather than a claim of superiority.
- **Clinical extension**: human paediatric B-ALL samples showed **different grades of karyotype heterogeneity**, i.e. CIN rates differ between malignancies — the basis for the proposal that single-cell karyotyping could inform treatment stratification.
- Platform: nuclei flow-sorted, automated DNA fragmentation, barcoded library prep, **shallow multiplexed sequencing**. Released as the Bioconductor R package *AneuFinder*.

## Methods / evidence

The design is a controlled genetic model where instability is engineered and its magnitude known independently, so the discrepancy between bulk and single-cell views is interpretable rather than merely observed. Validation runs both directions: aCGH against pooled single cells (concordant), and interphase FISH confirming >70% of cells with three or more copies of chromosome 15. Mouse cohorts with the relevant genotypes and *Lck-Cre*-negative controls; extension to human B-ALL.

## Surprising or load-bearing bits

- **This is the cleanest bulk-versus-single-cell demonstration in the corpus**, because the same cells produce both answers: pool them and the karyotype is clonal, separate them and 56% are unique. The clonal appearance is not wrong — it is what selection produces on top of ongoing instability — but it is the wrong readout for asking whether instability is ongoing.
- **Ongoing CIN and clonal karyotype are compatible.** Selection drives cells toward favourable chromosome combinations while mis-segregation keeps generating variants around that attractor. Recurrent aneuploidy is therefore evidence about *selection*, not about *stability* — a distinction that matters for interpreting every recurrent-CNV report in bulk cancer genomics.
- **Mappability-variable bins** rather than fixed-width bins is a small choice with real consequences: read counts in poorly mappable regions are depressed regardless of copy number, so equalizing expected counts per bin is what makes an HMM emission model valid. The same reasoning underlies [[garvin-2015-natmethods|Ginkgo]] and [[wang-2020-scope|SCOPE]].
- **Spikiness as a QC metric generalizes.** Bin-to-bin variance separates a genuinely segmented genome from a noisy library, and is the same quantity as the MAD filter used in [[zahn-2017-dlp|DLP]] — independent arrivals at the same diagnostic.
- **The heterogeneity score turns CIN into a measurable per-tumour phenotype**, which is what makes the treatment-stratification proposal concrete rather than aspirational: different B-ALL patients have measurably different instability rates.
- Modelling nullisomy as a delta distribution is a detail worth noting — zero copies means zero reads, not a low count, so it cannot share the negative-binomial family with the other states.

## Concepts touched

- [[copy-number-variation]] — HMM over 0–10 copy states on mappability-variable bins is one of the standard single-cell CNV callers.
- [[chromosomal-instability]] — separated here, for the first time in this corpus, from aneuploidy as a static state.
- [[quality-control-metrics]] — spikiness, segment count, Bhattacharyya distance as library-level QC.

## Connections to other sources

- Compared directly against [[garvin-2015-natmethods]] (Ginkgo); related callers [[wang-2020-scope]], [[tickle-2019-infercnv]], [[gao-2021-copykat]].
- The amplification-free platform whose data it also serves: [[zahn-2017-dlp]], [[laks-2019-dlp-plus]].
- Founding single-cell CNV work: [[navin-2011-sns-tumor-evolution]]; phylogeny from CNV: [[lu-2024-cnaphylogeny-review]].
- Heterogeneity context: [[xu-2012-single-cell-exome-kidney]], [[kim-2018-tnbc-chemoresistance]].

## Open questions

- **Whether karyotype heterogeneity predicts treatment outcome is proposed, not shown.** The human B-ALL data establish that CIN rates differ between patients; no outcome data are presented.
- 25 cells for the primary T-ALL analysis is a small sample for a heterogeneity estimate; the 56%-unique figure is a lower bound that will rise with more cells, and the paper does not report its saturation.
- The sensitivity/robustness trade against Ginkgo means small-CNV calls depend on caller choice, with no external truth set to arbitrate.

## Related

- [[chromosomal-instability]] · [[garvin-2015-natmethods]] · [[zahn-2017-dlp]] · [[cancer-clonal-evolution]]
