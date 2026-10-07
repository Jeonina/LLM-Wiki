---
type: summary
title: "Duan et al. 2026 — mist: a hierarchical Bayesian framework for detecting differential DNA methylation dynamics in single-cell data"
source: "[[00-Sources/papers/mist_ a hierarchical Bayesian framework for detecting differential DNA methylation dynamics in single-cell data]]"
source_kind: paper
author: "Daoyu Duan, Wenjing Ma, Wen Tang, Hao Wu, Liangliang Zhang, Hao Feng"
published: 2026-03-12
ingested: 2026-10-07
doi: "10.1038/s41467-026-70523-y"
journal: "Nature Communications 17:3835"
tags: [mist, single-cell-methylation, pseudotime, differential-methylation, hierarchical-Bayesian, horseshoe-prior, Gibbs-sampling, logit-normal, scNMT-seq, snm3C-seq, Bioconductor]
entities: []
concepts: ["[[trajectory-inference]]", "[[scbs-seq]]", "[[scnmt-seq]]", "[[bisulfite-sequencing]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[dna-methylation]]", "[[computational-methods]]"]
---

**Citation:** Duan et al. (2026) — *mist: a hierarchical Bayesian framework for detecting differential DNA methylation dynamics in single-cell data* — *Nature Communications* 17:3835. [DOI](https://doi.org/10.1038/s41467-026-70523-y)

# Duan 2026 — mist

> mist (methylation inference for single-cell along trajectory) fills a gap the authors state no prior method covered: **differential methylation along pseudotime** in single-cell DNA methylation (scDNAm) data. Per gene (or region), methylation level is modelled as **logit-normal** with a mean that is a **degree-4 polynomial in pseudotime** (horseshoe-shrunk coefficients) and a variance that differs across **four pseudotime stages**; parameters are fit by Gibbs sampling. Genes are ranked by the **minimised squared area between fitted trajectories** (vs a flat line for one group, or between two groups after an optimal vertical shift), so ranking reflects *shape of change*, not baseline level. In simulations mist beats GAM and polynomial regression; on scNMT-seq mouse gastrulation and snm3C-seq developing human brain it recovers plausible developmental regulators.

## Key claims

- **No prior method models scDNAm along pseudotime**, per the authors; RNA tools (tradeSeq, PseudotimeDE) assume dense negative-binomial counts, whereas scDNAm is sparse and proportional.
- **Stage-specific dispersion is a first-class output.** Simulated bias for σ² is mostly within ±10%; mist gives lower squared error than GAM (constant-variance Gaussian) and fixed polynomial regression for both variance and coefficient parameters.
- **Better DM ranking in simulation.** In one-group simulations, mist's ROC dominates especially at 1 − specificity < 0.2; its true discovery rate (TDR) among top-ranked genes stays above 0.75 at various cutoffs while GAM and polynomial regression struggle to exceed 0.5; mist's TDR rises with cell number, a trend less evident for the others. Two-group simulations show the same ordering.
- **scMET does not capture trajectories.** In simulations with 10,000 genes and 4,000 cells per group, scMET's differential-variability test showed limited ability to detect differential trajectories — expected, since it ignores cell ordering.
- **Mouse gastrulation (GSE121708, E4.5–E7.5 multi-omics; one-group design).** With Monocle3 pseudotime from methylation, estimated dispersion is higher in early stages and lower later, matching the expectation of stabilising methylation with fate commitment. mist uniquely identified **3,927 DM genes** not shared with GAM/polynomial; examples *Apela*, *L1td1* (methylation changes mirroring loss of pluripotency) and *Cd3g*.
- **Developing human brain (snm3C-seq; frontal cortex vs hippocampus, mid-gestation to adult, >53,000 nuclei; two-group design).** Top 50 DM genes show region-specific landscapes; *CAMK2A* loses methylation in hippocampus with development and *FGFR3* gains methylation in frontal cortex.

## Methods / evidence

CpGs aggregated to gene (or promoter/region) features: methylated and total read counts per cell → methylation proportion. Pseudotime is a required external input (Monocle3, Slingshot, STREAM, etc.), rescaled to [0, 1] and cut into four default stages ([0, 0.25), …, [0.75, 1]). Priors: horseshoe on polynomial coefficients (half-Cauchy local/global scales, slice-sampled), N(0, 3²) intercept, 1/σ² on stage variances. Simulations: 10,000 genes with 5/10/15% DM, 20 iterations, parameters drawn from fits to the gastrulation data. Comparators: GAM with cubic regression splines (knots at 0.25/0.5/0.75; likelihood-ratio test) and degree-4 polynomial regression (ANOVA). Released as an R/Bioconductor package.

Weight: simulations are generated from mist's own logit-normal model with parameters fitted by mist, which favours mist against GAM/polynomial baselines; the comparators are generic regressions rather than specialised pseudotime DE tools. Real-data results are illustrative (known genes "align with" transitions), not validated against an orthogonal ground truth. The authors flag pseudotime double-dipping when ordering is inferred from the same methylation data, and report a re-analysis with STREAM pseudotime from RNA (supplementary).

## Surprising or load-bearing bits

- **Coverage floor:** performance is sensitive at 10–20 reads per feature, with stable estimation generally at ≥50 reads — which restricts mist to gene/region aggregates in sparse scBS-type data rather than CpG-level analysis.
- **Shift-invariant DM metric**: by optimising the vertical offset C, mist deliberately ignores absolute methylation differences between groups and scores only differences in dynamics — a design choice users must keep in mind when two groups differ mainly in level. (synthesis)
- **Variance as biology**: early-stage high and late-stage low dispersion is presented as validating the stage-specific variance assumption; it also echoes the general idea of methylation heterogeneity collapsing with commitment. (synthesis)
- Computational cost scales with number of features under Gibbs sampling; moving to smaller regions would increase burden substantially.

## Concepts touched

- [[trajectory-inference]] — pseudotime-conditioned differential testing extended from RNA to methylation; the paper lists pseudotime's single-scalar limitation for branching processes.
- [[scbs-seq]] / [[scnmt-seq]] — sparse proportion data as the modelling target; the gastrulation dataset is scNMT-seq.
- [[sequencing-depth-and-coverage]] — explicit per-feature read thresholds (≥50 reads for stable estimates).

## Connections to other sources

- Benchmarked against [[kapourani-2021-scmet]] (cell-to-cell variability without ordering).
- Real data from [[argelaguet-2019-nature]] (mouse gastrulation scNMT-seq); assay context [[clark-2018-scnmt-seq]].
- Other single-cell methylation analysis tools: [[kapourani-2019-melissa]] (clustering/imputation), [[kremer-2024-methscan]] (VMR-based analysis), [[desouza-2020-epiclomal]] (clustering), [[angermueller-2017-genomebiol]] (DeepCpG imputation); review context [[iqbal-2023-methylome-review]].
- Brain methylation + 3D context: [[liu-2023-mouse-brain-methylome-3d]], [[lee-2019-natmethods]] (sn-m3C-seq).
- Trajectory tooling borrowed from RNA: [[cao-2019-moca]] (Monocle 3).

## Open questions

- Fixed four stages and degree-4 polynomials are defaults, not learned; how sensitive are rankings to these choices on branching trajectories?
- No uncertainty-calibrated significance (FDR) is described for the area statistic in the clipping — genes are ranked, not thresholded.
- Extension to CpG-level dynamics and joint modelling with accessibility/RNA is proposed but not done.

## Related

- [[kapourani-2021-scmet]] · [[argelaguet-2019-nature]] · [[trajectory-inference]] · [[40-Topics/dna-methylation]]
