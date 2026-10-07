---
type: summary
title: "Farlik et al. 2015 — Single-Cell DNA Methylome Sequencing and Bioinformatic Inference of Epigenomic Cell-State Dynamics"
source: "[[00-Sources/papers/Single-Cell DNA Methylome Sequencing and Bioinformatic Inference of Epigenomic Cell-State Dynamics]]"
source_quality: full
source_sha256: "190d28eb5e87755f00c475dd83d8823ed9bf5f51f46171bf439788754f6e3b56"
source_kind: paper
author: "Matthias Farlik, Nathan C. Sheffield, Angelo Nuzzo, Paul Datlinger, Andreas Schönegger, Johanna Klughammer, Christoph Bock (corresponding)"
published: 2015-03
ingested: 2026-10-07
doi: "10.1016/j.celrep.2015.02.001"
journal: "Cell Reports 10(8):1386–1397"
tags: [scWGBS, muWGBS, post-bisulfite-adaptor-tagging, EpiGnome, region-set-analysis, lineage-plot, composite-methylome, azacytidine, K562, HL60, mESC, 2i, imprinting, Bismark, RnBeads]
entities: []
concepts: ["[[bisulfite-sequencing]]", "[[scbs-seq]]", "[[cpg-island]]", "[[pseudo-bulk]]", "[[trajectory-inference]]", "[[enhancer-states]]", "[[dnmt]]", "[[decitabine]]"]
topics: ["[[dna-methylation]]", "[[computational-methods]]"]
---

**Citation:** Farlik et al. (2015) — *Single-Cell DNA Methylome Sequencing and Bioinformatic Inference of Epigenomic Cell-State Dynamics* — *Cell Reports* 10(8):1386–1397. [DOI](https://doi.org/10.1016/j.celrep.2015.02.001)

# Farlik 2015 — scWGBS and region-set lineage plots

> Two contributions in one Resource paper. **Wet lab**: a low-input whole-genome bisulfite protocol (μWGBS, scaled down to single cells as scWGBS) that bisulfite-treats lysed cells directly and does all post-bisulfite library steps in one tube, with **no pre-amplification**. **Dry lab**: since single-cell methylomes are sparse and binary, stop asking about individual CpGs and instead average methylation over **thousands of regions of one functional type** (2,768 region sets: DHS, histone marks, TF binding sites), regress out the trivial effects (starting methylation level, CpG content), and use the residuals to place cells on a two-axis "lineage plot". The bet is that the shallow-but-many design — many low-coverage one-cell / four-cell methylomes — is more informative than few deep ones.

## Key claims

- **Low input works**: an existing post-bisulfite-adaptor-ligation protocol optimized for 50 ng gave close to optimal data from **6 ng** (5.8% PCR duplicates vs 1.9% at 50 ng). Titrating 500, 50, 20, 10, 4 and 1 cell(s) with ≤18 PCR cycles, quality was "acceptable all the way down to single cells", with progressive loss of coverage; MDS grouped samples by cell type, not cell number, and one-cell samples clustered with 50-ng positive controls.
- **QC by design**: FACS validated by colony counting (78% of wells with exactly one mESC colony, none with more than one); one human + four mouse cells (or vice versa) sorted per well so read ratios across genomes flag lost cells; cell-line CNV signatures confirm no contaminating DNA; methylated/unmethylated oligo spike-ins track bisulfite conversion.
- **Scale**: >250 samples sequenced, >80% passed QC → **82 single-cell methylomes, 89 four-cell methylomes**, 53 optimization/QC samples. Human medians: 4.6 M reads → **1.4 M CpGs** (one-cell) and 13.7 M reads → 3.7 M CpGs (four-cell). The authors state these are the first single-cell methylomes of human cells.
- **Breadth over depth**: deeper sequencing of one library raised CpG coverage by 86% (mouse one-cell) and 62% (human four-cell) at high duplicate rates, whereas combining a few dozen low-coverage samples into a **composite methylome** covers >90% of CpGs in human and mouse — so sequencing many samples shallowly is more cost-effective.
- **K562 + azacytidine** (31 one-/four-cell samples, untreated / 48 h / 96 h): samples grouped by treatment and lost global methylation, except two treated one-cell samples that clustered with untreated — "possibly because these two cells had not divided". Regions demethylating **more slowly** than expected were repressive chromatin; regions demethylating **faster** were lineage-specific enhancers and TF binding sites; 48-h cells fell between untreated and 96-h on the lineage plot.
- **HL60 + vitamin D3** (38 samples, up to 14 days): no significant global methylation change and weaker MDS separation, yet a few region types deviated from the model — ESC enhancers gained methylation, blood-development-specific DHSs lost it — enough to build a lineage plot. Locus-specific change can be detected without global change.
- **Cell-to-cell variability rises then falls** after azacytidine or vitamin D3 (pairwise Euclidean distances within groups), consistent with cells responding individually before settling into a new state.
- **mESC (81 methylomes; 2i, LIF-withdrawal embryoid bodies, ATRA)**: 2i demethylated most cells; ATRA (day 14) lowered and EB formation raised global methylation. Under 2i, **imprinted regions were the most protected** set; repressive-chromatin sets demethylated slowly; enhancers of essentially any lineage fast, ESC-specific enhancers fastest. Patterns were anticorrelated in differentiation — regions fastest to lose methylation in 2i gained it fastest in EB/ATRA — and imprints were protected in either direction. A lineage plot built only from 120-h 2i vs serum placed ATRA and EB cells in the opposite direction.
- **Positioning vs other protocols**: scWGBS for many cells at low coverage; scRRBS for comparing CpG islands; scPBAT for deep sequencing of single cells. Relative to scPBAT, no pre-amplification gives lower cost, less hands-on time, reduced amplification bias, no strandedness confounding, correct paired-end assignment and accurate PCR-duplicate measurement, at the cost of somewhat lower library complexity.

## Methods / evidence

Library prep with the EpiGnome Methyl-Seq kit (random-hexamer post-bisulfite tagging), EZ DNA Methylation-Direct bisulfite conversion on lysed cells, HiSeq 2000/2500. Pipeline: Trimmomatic → Bismark → methylation calling → duplicate removal (identical start/end) → removal of reads with <3 converted non-CpG cytosines (excludes unconverted/contaminating fragments); RnBeads and EpiExplorer for initial analysis. Saturation plots compared against published scRRBS and scPBAT data, separately for CpG islands and non-island tiles. Region sets: ENCODE TFBS, Cistrome, tissue-clustered DHSs (human); a previously compiled mouse database; sets filtered to ≥100 and mean 200 CpG measurements. Per-sample linear model: Δmethylation ~ control methylation + CpG content; residuals t-tested treated vs control (p < 0.01, up to 20 top sets) → two scores (positive / negative residual sets) = lineage-plot axes. GEO GSE65196.

Weight: cell-line models with known perturbations, so trajectories have ground truth direction. The authors acknowledge the lineage plot is susceptible to overfitting at the two endpoints used to choose region sets, mitigated by placing held-out time points and treatments. Region-set inference depends entirely on the quality and cell-type relevance of external annotation catalogs.

## Surprising or load-bearing bits

- **Region-set aggregation is the conceptual ancestor of how sparse single-cell epigenomes are still analysed** — pooling over features of a type rather than imputing CpGs, the same move as chromVAR-style motif deviations in scATAC. (synthesis)
- **Regressing out baseline methylation is essential**: highly methylated regions lose more under any demethylating stimulus, so naive differences mostly rediscover starting levels. The residual is the biological signal.
- **Two non-dividing outliers** illustrate that hypomethylating drugs act through replication — a per-cell read-out of drug response heterogeneity bulk data cannot give. (synthesis)
- **Imprints withstand both naive conversion and differentiation** — the cleanest internal control in the paper.
- **"Composite methylomes" as reference epigenome corridors**: combining dozens of low-input methylomes gives coverage plus an inherent estimate of cell-to-cell variation — essentially pseudo-bulk with a variance term. (synthesis)

## Concepts touched

- [[bisulfite-sequencing]] — DNA loss from bisulfite damage between pre-ligated adapters motivates post-bisulfite tagging; no-pre-amplification variant.
- [[scbs-seq]] — scWGBS as a sibling of scBS-seq/scPBAT; explicit trade-off table.
- [[cpg-island]] — scRRBS's island focus vs scWGBS's relatively unbiased coverage; CpG content as a covariate.
- [[pseudo-bulk]] — composite methylomes from pooled low-coverage samples.
- [[trajectory-inference]] — lineage plot as an early supervised trajectory method for methylation.
- [[enhancer-states]] — enhancers and TF sites are the fastest-moving methylation compartments.
- [[dnmt]], [[decitabine]] — azacytidine depletes DNMTs; demethylation depends on cell division.

## Connections to other sources

- Protocols it positions itself against: scRRBS ([[guo-2013-scrrbs]]) and "scPBAT", a post-bisulfite-adaptor-tagging protocol with whole-genome pre-amplification (the clipping strips citation names; likely [[smallwood-2014-natmethods]] — unverified mapping). (synthesis)
- Later scaling of the scWGBS family: [[luo-2017-snmc-seq]], [[mulqueen-2018-sci-met]] (alignment-rate bottleneck of plate scWGBS), [[zhang-2023-drop-bs]], [[clark-2017-scbs-seq-protocol]].
- Later statistical models for sparse single-cell methylation that replace region-set averaging with probabilistic or learned models: [[kapourani-2019-melissa]], [[kapourani-2021-scmet]], [[angermueller-2017-genomebiol]] (DeepCpG).
- Analogous feature-set aggregation in scATAC: [[schep-2017-chromvar]]. (synthesis)

## Open questions

- Region-set averaging discards which CpGs and which cells co-vary within a set; it cannot detect heterogeneity *inside* a region type.
- The lineage plot is supervised by the chosen endpoints; how well it generalizes to unlabeled primary tissue (the authors' stated aim: heterogeneous organs, drug resistance) is not shown.
- The variability rise-and-fall rests on pairwise distances between sparse samples, where coverage differences could also inflate distances.

## Related

- [[scbs-seq]] · [[bisulfite-sequencing]] · [[40-Topics/dna-methylation]] · [[smallwood-2014-natmethods]] · [[guo-2013-scrrbs]]
