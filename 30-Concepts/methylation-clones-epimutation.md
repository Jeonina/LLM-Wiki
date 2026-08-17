---
type: concept
title: Methylation clones and epimutation lineage tracing
aliases: [epimutation lineage tracing, methylation clones, epi-clone]
tags: [methylation, lineage-tracing, epimutation, single-cell]
created: 2026-05-19
updated: 2026-05-19
---

# Methylation clones and epimutation lineage tracing

> Heritable, mitotically-propagated changes in DNA methylation state at individual CpGs ("epimutations") serve as endogenous lineage markers in human cells where engineered barcoding is not feasible. Methods like Epi-CLONE and MethylTree reconstruct clonal genealogies from methylation patterns at clock-like CpGs ([[10-Summaries/chen-2025-methyltree]]; [[10-Summaries/xiao-2025-epitrace]]).

## Underlying biology

Epimutations accumulate at predictable rates at clock-like CpGs (e.g., ELOVL2, scaffold ICRs). Maintenance errors of DNMT1 during replication produce these — they are heritable but not deterministic ([[10-Summaries/kim-2017-methylation-memory-review]]).

## Methods

- **MethylTree** — phylogenetic inference from scBS-seq methylation patterns ([[10-Summaries/chen-2025-methyltree]]).
- **EpiTrace** — chromatin-accessibility-based epigenetic age estimation, parallel to methylation clones ([[10-Summaries/xiao-2025-epitrace]]).
- **Epi-CLONE** — methylation lineage tracing in human stem cells ([[10-Summaries/gaiti-2019-cll-epigenetic]] precedent in CLL).

## Why it matters

Methylation-based lineage tracing works in human tissue without genetic engineering. It complements somatic-mutation-based lineage tracing ([[30-Concepts/lineage-tracing]]) — methylation is denser but noisier; mutations are sparser but more confident.

## Cross-modal comparison

A head-to-head of methylation, ATAC-seq, and RNA against ground-truth barcodes points to the **superiority of the methylome for inferring clonal relationships** — methylation patterns are noisy but carry the strongest clonal signal once cell-type and cell-state variation are regressed out ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]). The discovery of slow-fluctuating "static" CpGs widens epimutation tracing from cancer to normal-tissue clonal dynamics ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).

## Related

- [[30-Concepts/lineage-tracing]] · [[30-Concepts/epigenetic-memory]] · [[30-Concepts/epigenetic-aging]] · [[30-Concepts/phylogenetic-inference]]
- [[40-Topics/dna-methylation]] · [[40-Topics/single-cell-lineage-tracing]]

## Added 2026-08-17

The epimutation clock was quantified in **plants** first, and the mammalian literature arrived at the same premise independently five years later. (synthesis)

**[[10-Summaries/shahryary-2020-alphabeta|AlphaBeta]] (2020)** estimates **forward and backward** epimutation rates (α and β — gains and losses are separate stochastic processes) from **pedigree-structured** methylation data, and establishes the three properties a lineage clock requires: epimutations accumulate **neutrally** genome-wide; they originate **mainly during somatic development** rather than in the germline — which is what makes them mark *cell lineages within an individual*; and they can **age-date trees** ([[10-Summaries/shahryary-2020-alphabeta]]).

Human epimutation-clock methods generally *assume* neutrality; AlphaBeta *tested* it, in a system where plants differ substantially from mammals in methylation maintenance and germline segregation — so the framework transfers but the rate estimates do not. (synthesis)

**[[10-Summaries/gabbutt-2025-evoflux|EVOFLUx]] (2025)** is the human clinical realisation. **Fluctuating CpGs (fCpGs)** — sites whose methylation stochastically flips on a timescale of years — act as a natural barcode readable from a **bulk methylation array**, deliberately trading per-cell resolution for cohort scale: 1,976 lymphoid cancer samples, where single-cell phylogenetics had been restricted to small cohorts by cost ([[10-Summaries/gabbutt-2025-evoflux]]).

Findings: growth rate, malignancy age and epimutation rate vary by **orders of magnitude** across disease types; **subclonal selection is infrequent** within bulk samples; evolutionary history is a strong independent prognostic factor in two CLL series; and the seed of a Richter-transformed clone **existed decades before presentation** ([[10-Summaries/gabbutt-2025-evoflux]]).

**Two open issues shared by both.** Gain/loss equilibrium means the clock **saturates**, bounding how far back it can read — unquantified in both papers. And whether infrequent subclonal selection is biology or the resolution limit of bulk fCpG data is the most consequential open question in EVOFLUx. (synthesis)

**Methylation as clock versus methylation as fingerprint**: [[50-Notes/methylation-cancer-origin-classifiers|cancer-of-origin classifiers]] use methylation statically; EVOFLUx uses its *dynamics*. Same measurement, entirely different information. (synthesis)
