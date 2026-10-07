---
type: summary
title: "Dautle & Chen 2025 — Single-Cell Hi-C Technologies and Computational Data Analysis"
source: "[[00-Sources/papers/Single‐Cell Hi‐C Technologies and Computational Data Analysis]]"
source_kind: paper
author: "Madison A. Dautle, Yong Chen (corresponding)"
published: 2025-01-30
ingested: 2026-10-07
doi: "10.1002/advs.202412232"
journal: "Advanced Science 12(9):2412232"
tags: [scHi-C, review, protocol-comparison, cis-trans-ratio, quality-control, imputation, normalization, BandNorm, Higashi, SnapHiC2, scHiCDiff, bin-size, saturation]
entities: []
concepts: ["[[single-cell-hi-c]]", "[[hi-c-normalization]]", "[[imputation]]", "[[chromatin-compartments]]", "[[topologically-associating-domain]]", "[[chromatin-loop]]", "[[dip-c]]", "[[sc-sprite]]", "[[combinatorial-indexing]]", "[[quality-control-metrics]]", "[[joint-single-cell-multi-omics]]", "[[latent-dirichlet-allocation]]", "[[trajectory-inference]]", "[[batch-effect]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]", "[[computational-methods]]", "[[single-cell-multiomics]]"]
---

**Citation:** Dautle & Chen (2025) — *Single-Cell Hi-C Technologies and Computational Data Analysis* — *Advanced Science* 12(9):2412232. [DOI](https://doi.org/10.1002/advs.202412232)

# Dautle 2025 — scHi-C technologies and computational analysis (review)

> A review with a small empirical core. The authors re-download public datasets from **13 scHi-C protocols** (8 contact-only, 5 multi-omic) and score them on two simple metrics — total contacts per cell and *cis/trans* ratio — then catalogue the software for QC, normalization, imputation and seven downstream tasks (clustering, A/B compartments, TADs, loops, 3D reconstruction, differential interactions, simulation, plus pseudotime). Main verdicts: the Nagano 2017 protocol and scNanoHi-C lead among contact-only protocols; **multi-omic scHi-C protocols are not statistically worse** at capturing contacts; and **no single pipeline covers all tasks**, with many tasks served by exactly one tool. The forward-looking part argues for saturation modelling, data-driven bin-size selection, cell-type-aware imputation and parametric differential testing.

## Key claims

- **Protocol landscape.** Eight contact-only protocols (Nagano 2013/2017, Stevens 2017, Zhou 2019, snHi-C, sci-Hi-C, Dip-C, scSPRITE, scNanoHi-C) and five multi-omic ones (sn-m3C-seq and scMethyl Hi-C for methylation; HiRES and MUSIC for RNA, MUSIC also RNA–chromatin associations; s3-GCC for scDNA-seq). They differ mainly in step order, restriction enzyme (*MboI* sticky vs *AluI* blunt ends), barcoding and amplification (PCR, MDA, META). snHi-C is described as the only method that isolates nuclei before fixation.
- **Contact yield and cis/trans by protocol** (Table 3, means/medians per cell):
  - sci-Hi-C (Ramani 2017; Kim 2020) and scSPRITE have **low total contacts** (sci-Hi-C means ~5,500–19,000) with good *cis/trans*.
  - Stevens 2017 has the highest-quality *cis/trans* (mean 12.136, median 13.268) but recovers about a quarter of the contacts of the Nagano protocols.
  - snHi-C performs about average in mouse and fly but poorly in human cells (median *cis/trans* 0.428).
  - Dip-C datasets have average contact recovery but some of the lowest *cis/trans* ratios.
  - Nagano 2017 and scNanoHi-C (mouse mean ~800,000 contacts) have the best combination among contact-only protocols.
  - sn-m3C-seq in Luo et al. (4,238 human cells) recovered nearly twice the contacts per cell of the earlier Lee et al. application; scMethyl Hi-C about a tenth of sn-m3C-seq; HiRES similar to Nagano 2017; s3-GCC shows the most stable *cis/trans* across contact depths but has been used once.
- **Multi-omic ≠ worse.** Comparing contact-only and multi-omic datasets found no significant difference in total contacts or *cis/trans* (Wilcoxon–Mann–Whitney, P cutoff 0.05), so the authors recommend multi-omic scHi-C protocols.
- **QC is static and empirical.** Contact-count cutoffs in use range from 1,000 to 5,000 per cell, plus *cis/trans* >1, ≥95% uniquely mapped reads, short/long-range ratios and all-chromosome presence. GiniQC is presented as the only package whose filtering accounts for contact type and coverage (via clumping of *trans* contacts).
- **Normalization.** scHiCNorm normalizes *cis* only (local-bias features, distribution fitting); BandNorm removes genomic-distance bias, normalizes depth and applies band-dependent decay; Galaxy HiCExplorer 3 does coverage/row-sum scaling then Knight–Ruiz. Most other tools fold normalization into imputation.
- **Imputation families and their failure modes.** Random walk (scHiCluster, scHiCEmbed, Fast-Higashi, SnapHiC2's sliding window, HiCS, scHiCTools) is distribution-free but biased toward neighbouring observations and vulnerable to missing data; Gaussian convolution (scHiCDiff) may over-smooth high-frequency regions such as heterochromatin; Bayesian hierarchical (HiCImpute); deep learning (scVI-3D, scHiCEDRN, Higashi) avoids priors but is compute-heavy; LDA topics (scHiC Topics) is preprocessing-sensitive.
- **Tool coverage is thin and fragmented** (Table 5): ten clustering tools; scGHOST for (sub)compartments, designed to run after Higashi; four TAD callers (Higashi, scHiCEmbed, HiCS, DeDoc2); **SnapHiC2 as the only scHi-C loop caller** (up to 5 kb, no imputation required); four 3D-reconstruction tools (NucProcess+NucDynamics, scHiCEmbed, Si-C, DPDchrom); scHiCDiff as the only differential tool; scHiCPTR as the only pseudotime tool; scHi-CSim as the only simulator. BandNorm + scGAD is described as the only bridge from scHi-C to gene-level (gene-associating-domain) scores.
- **Saturation analysis.** New-discovery rate (proportion of newly detected bin-pair contacts per added cell) decays as a power law; 812 HAP1 cells saturate better than 471 GM12878 cells (Ramani 2017 data), and larger bins saturate with fewer cells. The authors recommend pre-sequencing a few cells to estimate maximum unique contacts, need for more depth, and cells needed per type.
- **Bin size is never optimized.** All tools rely on empirically chosen bins (e.g., 100 kb, 500 kb); matrices at 50 kb–1 Mb look different even within one cell type (shown for single 1-cell-stage blastomeres), and the optimum likely differs by task.
- **Differential testing lacks power.** scHiCDiff models NB/ZINB interaction strengths but tests by non-parametric KS or Cramér–von Mises, which are underpowered at small n and bin-based only; the authors propose adopting exact distributions of the difference of two NBs (DOTNB) and scale-aware (compartment/TAD/loop) tests.

## Methods / evidence

Narrative review plus a re-analysis: public GEO datasets (Table 3; ~20 studies, from 8 to 19,388 cells each) processed for contacts/cell and *cis/trans*, with scripts on GitHub (chenyongrowan/scHIC_Evaluation); a saturation analysis on Ramani 2017 HAP1/GM12878; tool tables of inputs, outputs and language.

Weight: the protocol comparison is **descriptive and confounded** — datasets differ in species, cell type, reference genome and, crucially, sequencing depth (the authors themselves attribute the Lee-vs-Luo sn-m3C-seq gap possibly to depth). Two metrics only; no assessment of noise, ligation artifacts or downstream analysis quality. The tool catalogue is functional (inputs, outputs, language), not a benchmark — no tool is run against another. "Only tool" claims reflect the authors' survey at writing time. The DeepBID proposal is the authors' own method (self-citation).

## Surprising or load-bearing bits

- **The cis/trans metric can be gamed by low depth and does not track contact yield** — sci-Hi-C has high *cis/trans* but few contacts, Dip-C the reverse. Using both together, as the authors do, is the minimum; neither alone ranks protocols. (synthesis)
- **Multi-omic scHi-C costs nothing in contacts** on these metrics — a practical argument that the default scHi-C experiment should co-measure methylation or RNA.
- **Single-tool bottlenecks everywhere downstream**: loops (SnapHiC2), differential contacts (scHiCDiff), pseudotime (scHiCPTR), simulation (scHi-CSim). Any review-level claim about scHi-C loop or differential biology rests on one method each. (synthesis)
- **Imputation trades structural zeros for false positives** — the authors explicitly warn neighbour-based imputation dilutes high-frequency contacts, and propose clustering first, then imputing within clusters, iteratively.
- The saturation curves give a concrete design rule: estimate the power-law decay of new contacts per added cell before deciding between more depth and more cells.
- Minor internal inconsistencies: the sn-m3C-seq application by Luo is cited as 2022 in text but 2019 in Table 3; the protocol name is written both "sn-3mC-seq" and "sn-m3C-seq"; BandNorm/scVI-3D are dated 03.2021 in the tables despite the Genome Biology reference.

## Concepts touched

- [[single-cell-hi-c]] — protocol taxonomy (13 protocols) and contact-yield / *cis/trans* comparison.
- [[hi-c-normalization]] — scHiCNorm, BandNorm and HiCExplorer approaches; *trans* contacts usually left unnormalized.
- [[imputation]] — five method families with explicit failure modes; proposal for cell-type-aware imputation.
- [[chromatin-compartments]] / [[topologically-associating-domain]] / [[chromatin-loop]] — the per-scale callers available for single-cell data.
- [[dip-c]] / [[sc-sprite]] / [[combinatorial-indexing]] — protocol-level trade-offs in throughput and cost.
- [[quality-control-metrics]] — contact-count thresholds (1,000–5,000), *cis/trans* >1, GiniQC.
- [[joint-single-cell-multi-omics]] — multi-omic scHi-C protocols do not lose contacts.
- [[latent-dirichlet-allocation]] — scHiC Topics' imputation.
- [[trajectory-inference]] — scHiCPTR as the lone scHi-C pseudotime method.
- [[batch-effect]] — integration of scHi-C with other modalities lacks automated batch correction.

## Connections to other sources

- Protocols reviewed that have their own summaries: [[nagano-2013-nature]], [[ramani-2017-scihi-c]], [[tan-2018-science]] (Dip-C), [[lee-2019-natmethods]] (sn-m3C-seq), [[liu-2023-mouse-brain-methylome-3d]].
- Tools catalogued that have their own summaries: [[zhou-2019-schicluster]], [[zhang-2022-higashi]], [[xiong-2024-scghost]], [[yu-2021-snaphic]].
- Bulk Hi-C foundations: [[lieberman-aiden-2009-hic]]; bulk pipelines [[servant-2015-hicpro]], [[durand-2016-juicer]], [[abdennur-2020-cooler]].
- Companion review covering the same field: [[hong-2025-sc3d-genome-review]].

## Open questions

- Would the protocol ranking survive depth-matched downsampling? The comparison does not control for sequencing depth. (synthesis)
- Can a stochastic-process saturation model, as the authors propose, predict per-protocol maximum unique contacts before full sequencing?
- What principled criterion should choose bin size per task and dataset?
- Whether the field's single-tool dependencies (loops, differential contacts, pseudotime) produce method-specific rather than biological conclusions remains untested. (synthesis)

## Related

- [[single-cell-hi-c]] · [[imputation]] · [[hong-2025-sc3d-genome-review]] · [[40-Topics/3d-genome]]
