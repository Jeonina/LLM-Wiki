---
type: concept
title: Methylation clones and epimutation lineage tracing
aliases: [epimutation lineage tracing, methylation clones, epi-clone]
tags: [methylation, lineage-tracing, epimutation, single-cell]
created: 2026-05-19
updated: 2026-10-12
---

# Methylation clones and epimutation lineage tracing

> Heritable, mitotically propagated changes in DNA methylation state at individual CpGs ("epimutations") serve as endogenous lineage markers in human cells where engineered barcoding is not feasible, and methods such as Epi-CLONE and MethylTree reconstruct clonal genealogies from methylation patterns at clock-like CpGs ([[10-Summaries/chen-2025-methyltree|MethylTree]]; [[10-Summaries/xiao-2025-epitrace|EpiTrace]]).

> [!abstract] 한눈에
> CpG 메틸화 상태의 변화(epimutation)는 세포 분열을 거쳐 물려지므로, 유전자 조작 없이 사람 조직에서 클론 계보를 추적하는 자연 barcode로 쓸 수 있다 ([[10-Summaries/chen-2025-methyltree|MethylTree]]). 메틸화는 noise가 크지만 다른 modality보다 클론 신호가 강하며, 이 clock이 얼마나 먼 과거까지 읽히는지는 아직 정해지지 않았다 ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]; [[10-Summaries/li-2023-darlin|Li 2023]]).

## Definition

Methylation is maintained by DNMT1 with PCNA and UHRF1 at the replication fork, and passive demethylation occurs when DNMT1 fails during replication; methylation thus acts as both a memory and a clock ([[10-Summaries/kim-2017-methylation-memory-review|Kim 2017]]). A lineage clock built on it needs three properties, first established in plants: epimutations accumulate **neutrally** genome-wide, they originate **mainly during somatic development** rather than in the germline — which is what makes them mark *cell lineages within an individual* — and they can **age-date trees** ([[10-Summaries/shahryary-2020-alphabeta|AlphaBeta]]). Gains and losses are separate stochastic processes, with forward and backward rates α and β ([[10-Summaries/shahryary-2020-alphabeta|AlphaBeta]]).

## Why it matters

Methylation-based lineage tracing works in human tissue without genetic engineering ([[10-Summaries/chen-2025-methyltree|MethylTree]]). It complements somatic-mutation-based [[30-Concepts/lineage-tracing]]: methylation is denser but noisier, mutations are sparser but more confident (synthesis).

## Methods

| Method | Year | Input | What it does | Source |
|---|---|---|---|---|
| [[10-Summaries/chen-2025-methyltree\|MethylTree]] | 2025 | scBS-seq | Phylogenetic inference from single-cell methylation patterns | ([[10-Summaries/chen-2025-methyltree\|MethylTree]]) |
| Epi-CLONE | 2025 | scTAM-seq | Methylation lineage tracing in human stem cells; CLL precedent in Gaiti 2019 | ([[10-Summaries/scherer-2025-nature\|EPI-Clone]]; [[10-Summaries/gaiti-2019-cll-epigenetic\|Gaiti 2019]]) |
| [[10-Summaries/xiao-2025-epitrace\|EpiTrace]] | 2025 | Chromatin accessibility | Epigenetic age estimation from clock-like accessibility loci, parallel to methylation clones | ([[10-Summaries/xiao-2025-epitrace\|EpiTrace]]) |
| [[10-Summaries/shahryary-2020-alphabeta\|AlphaBeta]] | 2020 | Pedigree-structured methylation data (plants) | Estimates forward and backward epimutation rates (α, β) | ([[10-Summaries/shahryary-2020-alphabeta\|AlphaBeta]]) |
| [[10-Summaries/gabbutt-2025-evoflux\|EVOFLUx]] | 2025 | Bulk methylation array | Reads fluctuating CpGs (fCpGs), sites whose methylation stochastically flips on a timescale of years, as a natural barcode; trades per-cell resolution for cohort scale | ([[10-Summaries/gabbutt-2025-evoflux\|EVOFLUx]]) |
| Camellia-seq | 2023 | Lineage barcodes + RNA + CpG methylation + GpC accessibility per cell | Engineered-barcode ground truth for methylation as a clonal mark | ([[10-Summaries/li-2023-darlin\|Li 2023]]) |

The epimutation clock was quantified in **plants** first, and the mammalian literature arrived at the same premise independently five years later (synthesis). EVOFLUx is the human clinical realisation: single-cell phylogenetics had been restricted to small cohorts by cost, so it reads fCpGs from bulk arrays instead ([[10-Summaries/gabbutt-2025-evoflux|EVOFLUx]]).

## Evidence and examples

**Methylation versus other modalities as a clonal mark**

- A head-to-head of methylation, ATAC-seq and RNA against ground-truth barcodes points to the **superiority of the methylome for inferring clonal relationships**: methylation patterns are noisy but carry the strongest clonal signal once cell-type and cell-state variation are regressed out ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).
- Camellia-seq showed DNA methylation retains clonal memory in HSCs across five mice and labelling windows from 36 h to 10 weeks, consistently more than expression or accessibility ([[10-Summaries/li-2023-darlin|Li 2023]]).
- The discovery of slow-fluctuating "static" CpGs widens epimutation tracing from cancer to normal-tissue clonal dynamics ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).

**Cancer evolution at clinical scale (EVOFLUx, 1,976 lymphoid cancer samples)**

- Growth rate, malignancy age and epimutation rate vary by **orders of magnitude** across disease types ([[10-Summaries/gabbutt-2025-evoflux|EVOFLUx]]).
- **Subclonal selection is infrequent** within bulk samples ([[10-Summaries/gabbutt-2025-evoflux|EVOFLUx]]).
- Evolutionary history is a strong independent prognostic factor in two CLL series ([[10-Summaries/gabbutt-2025-evoflux|EVOFLUx]]).
- The seed of a Richter-transformed clone **existed decades before presentation** ([[10-Summaries/gabbutt-2025-evoflux|EVOFLUx]]).

## Contested points

- **Neutrality is assumed, not tested, in humans.** Human epimutation-clock methods generally *assume* neutrality; AlphaBeta *tested* it ([[10-Summaries/shahryary-2020-alphabeta|AlphaBeta]]), but in plants, which differ substantially from mammals in methylation maintenance and germline segregation, so the framework transfers but the rate estimates do not (synthesis).
- **The clock saturates.** Gain/loss equilibrium bounds how far back the clock can read, and neither AlphaBeta nor EVOFLUx quantifies it (synthesis).
- **Biology or resolution limit?** Whether infrequent subclonal selection is biology or the resolution limit of bulk fCpG data is the most consequential open question in EVOFLUx (synthesis).
- **Clock versus fingerprint.** [[50-Notes/methylation-cancer-origin-classifiers|Cancer-of-origin classifiers]] use methylation statically, while EVOFLUx uses its *dynamics*: the same measurement carries entirely different information (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/lineage-tracing|Lineage tracing]] — Reconstructing cell ancestry from natural or synthetic marks.
> - `concept` [[30-Concepts/epigenetic-memory|Epigenetic memory]] — The mitotically heritable record of past cell states in methylation and chromatin.
> - `concept` [[30-Concepts/epigenetic-aging|Epigenetic aging]] — Predicting age from methylation at specific CpGs.
> - `concept` [[30-Concepts/phylogenetic-inference|Phylogenetic inference]] — Reconstructing a cell-division tree from heritable markers.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC at CpG dinucleotides and how it is measured.
> - `hub` [[40-Topics/single-cell-lineage-tracing|Single-cell lineage tracing]] — Methods and algorithms that reconstruct the ancestry of individual cells.
> - `note` [[50-Notes/methylation-cancer-origin-classifiers|Methylation cancer-of-origin classifiers]] — Methylation used statically, as a fingerprint of cell type.

## All sources on this page

> [!info]- 9 summaries cited here
> - [[10-Summaries/chen-2025-methyltree|Chen 2025]]
> - [[10-Summaries/gabbutt-2025-evoflux|Gabbutt 2025]]
> - [[10-Summaries/gaiti-2019-cll-epigenetic|Gaiti 2019]]
> - [[10-Summaries/kim-2017-methylation-memory-review|Kim & Costello 2017]]
> - [[10-Summaries/li-2023-darlin|Li 2023]]
> - [[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]
> - [[10-Summaries/scherer-2025-nature|Scherer 2025]]
> - [[10-Summaries/shahryary-2020-alphabeta|Shahryary 2020]]
> - [[10-Summaries/xiao-2025-epitrace|Xiao 2025]]
