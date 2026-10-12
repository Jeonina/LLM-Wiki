---
type: topic
title: Chromatin architecture
aliases: [chromatin biology, chromatin organization]
tags: [chromatin, regulation, single-molecule]
created: 2026-05-07
updated: 2026-10-12
paper_section: ["3.5"]
---

# Chromatin architecture

> How DNA is packaged with proteins (nucleosomes, TFs, cohesin/CTCF, polycomb, …) along chromosomes, and how that packaging varies across fibers, haplotypes and cells. The single-molecule branch is moving fast: Fiber-seq → DAF-seq closes the gap from bulk to single-cell, single-molecule resolution ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).

> [!abstract] 한눈에
> scDAF-seq로 한 세포의 염색체 전장을 단일 분자 수준에서 읽어 보니, 같은 세포 안 두 haplotype 사이의 regulatory element actuation 차이(~61%)가 세포 간 차이(~63%)와 거의 같았다 ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]). 핵 구조 쪽에서는 LAD가 켜고 끄는 이분법이 아니라 위치마다 lamina 접촉 확률을 갖는 상태로 보이고, TAD 경계는 heterochromatin 확산이 멈출 자리를 미리 표시한다 ([[10-Summaries/peric-hupkes-2010-lad-differentiation|Peric-Hupkes 2010]]; [[10-Summaries/dixon-2012-tads|Dixon 2012]]).

## Key points

- **Regulatory-element actuation varies about as much within a cell as between cells.** Two haplotypes in one cell differ in ~61% of actuation states, two cells in ~63% ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- **Same-fiber co-actuation forms ~100 kb domains that mirror cohesin loops**, though causality is not directly tested ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- **Lamina contact is a probability, not a binary state.** LAD relocation during differentiation is often confined to one transcription unit, and genes that detach become more likely to activate one step later ([[10-Summaries/peric-hupkes-2010-lad-differentiation|Peric-Hupkes 2010]]).
- **Topological domain boundaries pre-mark where heterochromatin spreading will stop**, and domains are related to but independent of LADs and replication-timing zones ([[10-Summaries/dixon-2012-tads|Dixon 2012]]).
- **Protein-anchored interaction mapping has no single-cell member**, so it serves as reference truth for single-cell loop callers, whereas CUT&Tag brought histone profiling to single cells ([[10-Summaries/li-2014-chia-pet|Li 2014]]; [[10-Summaries/yu-2021-snaphic|SnapHiC]]; [[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]). (synthesis)

## Start here

> [!cards]
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — Whether DNA is "open" for binding; measured by ATAC-seq, DNase-seq or single-molecule footprinting.
> - `concept` [[30-Concepts/chromatin-actuation|Chromatin actuation]] — Single-molecule refinement: the per-fiber binary state of "open + bound".
> - `concept` [[30-Concepts/single-molecule-footprinting|Single-molecule footprinting]] — The method class behind Fiber-seq, DAF-seq and FOODIE.
> - `concept` [[30-Concepts/fiber-seq|Fiber-seq]] — Bulk single-molecule chromatin profiling by m6A methyltransferase stenciling.
> - `concept` [[30-Concepts/daf-seq|DAF-seq]] — Single-cell single-molecule chromatin profiling by cytidine deaminase footprinting.
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Single-cell Tn5 tagmentation of accessible chromatin.

## Concepts and assays

- [[30-Concepts/atac-seq]] — Tn5 transposase tagmentation of accessible chromatin; the workhorse assay.
- [[30-Concepts/dnase-seq]] — original ENCODE accessibility assay; largely superseded by ATAC-seq.
- [[40-Topics/histone-modifications]] — covalent chromatin marks.
- [[30-Concepts/replication-timing]] — temporal axis of chromatin state.
- [[30-Concepts/enhancer-states]] — active, primed and poised functional categories.
- [[30-Concepts/cis-regulatory-element]] — enhancers, promoters, insulators.
- [[30-Concepts/cut-and-tag]], [[30-Concepts/cut-and-run]], [[30-Concepts/chic-seq]] — antibody-tethered nuclease methods.
- [[30-Concepts/lamina-associated-domains]] and [[30-Concepts/topologically-associating-domain]] — the two nuclear-structure units this page keeps returning to.

Key people: [[20-Entities/andrew-b-stergachis]] (UW Genome Sciences; developer of Fiber-seq and senior author of DAF-seq), [[20-Entities/elliott-g-swanson]] (co-first author of DAF-seq) and [[20-Entities/william-greenleaf]] (Stanford; co-developer of ATAC-seq; senior author of the canonical accessibility review) ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]; [[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]).

## Single-molecule footprinting

| Method | Year | Readout | Note |
|---|---|---|---|
| [[10-Summaries/swanson-2025-daf-seq\|DAF-seq / scDAF-seq]] | 2025 | Cytidine deamination of accessible DNA, long reads | Chromosome-length single-cell, single-molecule chromatin maps ([[10-Summaries/swanson-2025-daf-seq\|Swanson 2025]]) |
| [[10-Summaries/he-2024-foodie\|FOODIE]] | 2024 | Deaminase (DddB) on Tn5-open chromatin, short reads | TF footprinting with single-molecule binding fractions and pairwise cooperativity ([[10-Summaries/he-2024-foodie\|FOODIE]]) |

## Single-cell accessibility and its tooling

The canonical review of accessibility and the regulatory epigenome is [[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]. Droplet-scale accessibility can be tied to genotype: GoT–ChA links chromatin accessibility to *JAK2* V617F in single cells ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).

| Tool | Year | Input | Model | Note |
|---|---|---|---|---|
| [[10-Summaries/schep-2017-chromvar\|chromVAR]] | 2017 | scATAC | TF motif accessibility | Built for sparse single-cell data ([[10-Summaries/schep-2017-chromvar\|chromVAR]]) |
| [[10-Summaries/zamanighomi-2018-scabc\|scABC]] | 2018 | scATAC | Weighted *k*-medoids | Unsupervised clustering ([[10-Summaries/zamanighomi-2018-scabc\|scABC]]) |
| [[10-Summaries/mezger-2018-microfluidic-atac\|µATAC-seq]] | 2018 | — | Assay (nano-wells) | 5,184 nano-wells, ~1,800 cells per chip ([[10-Summaries/mezger-2018-microfluidic-atac\|Mezger 2018]]) |
| [[10-Summaries/pliner-2018-cicero\|Cicero]] | 2018 | scATAC | Co-accessibility | Links regulatory elements to genes from co-accessibility rather than conformation ([[10-Summaries/pliner-2018-cicero\|Cicero]]) |
| [[10-Summaries/bravo-2019-cistopic\|cisTopic]] | 2019 | scATAC | LDA topic model | ([[10-Summaries/bravo-2019-cistopic\|cisTopic]]) |
| [[10-Summaries/fang-2021-snapatac\|SnapATAC]] | 2021 | scATAC | Peak-free | Scales to 1 M cells ([[10-Summaries/fang-2021-snapatac\|SnapATAC]]) |
| [[10-Summaries/danese-2021-episcanpy\|EpiScanpy]] | 2021 | scATAC, scBS | scanpy framework | Unified accessibility and methylation analysis ([[10-Summaries/danese-2021-episcanpy\|EpiScanpy]]) |
| [[10-Summaries/gur-2025-scatac-vs-bulk\|Gur 2025]] | 2025 | scATAC pseudobulk vs bulk ATAC | Comparison | Same signal, better data quality ([[10-Summaries/gur-2025-scatac-vs-bulk\|Gur 2025]]) |

## Histone marks and protein binding in single cells

| Method | Year | Note |
|---|---|---|
| [[10-Summaries/kaya-okur-2019-cut-and-tag\|CUT&Tag]] | 2019 | Low-input chemistry that replaced ChIP and reached single cells ([[10-Summaries/kaya-okur-2019-cut-and-tag\|Kaya-Okur 2019]]) |
| [[10-Summaries/ku-2019-scchic-seq\|scChIC-seq]] | 2019 | Antibody–MNase fusion for single-cell histone marks ([[10-Summaries/ku-2019-scchic-seq\|scChIC-seq]]) |
| [[10-Summaries/yeung-2023-scchix-seq\|scChIX-seq]] | 2023 | Computational deconvolution of two histone marks per cell ([[10-Summaries/yeung-2023-scchix-seq\|scChIX-seq]]) |
| [[10-Summaries/janssens-2023-scicut-tag\|sciCUT&Tag]] | 2023 | Combinatorial indexing, 40,000 cells per chip ([[10-Summaries/janssens-2023-scicut-tag\|sciCUT&Tag]]) |
| [[10-Summaries/geisenberger-2025-scepi2-seq\|scEpi²-seq]] | 2025 | Histone marks and 5mC in the same cell ([[10-Summaries/geisenberger-2025-scepi2-seq\|scEpi²-seq]]) |
| [[10-Summaries/tavares-2026-6-base-cut-tag\|6-base-CUT&Tag]] | 2026 | 5mC + 5hmC at targeted histone marks ([[10-Summaries/tavares-2026-6-base-cut-tag\|6-base-CUT&Tag]]) |
| [[10-Summaries/shi-2026-dechic-seq\|DeChIC-seq]] | 2026 | Single-cell CTCF/RAD21 binding dynamics in preimplantation embryos ([[10-Summaries/shi-2026-dechic-seq\|DeChIC-seq]]) |

Computational prediction: DeepHistone predicts histone marks from DNA sequence plus DNase ([[10-Summaries/yin-2019-deephistone|DeepHistone]]).

## 3D genome: domains, loops and hubs

- **Loops.** The founding kilobase-resolution loop catalogue, with HiCCUPS/Arrowhead/APA and the convergent-CTCF rule ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).
- **Domains.** Topological domain boundaries pre-mark where heterochromatin spreading will stop rather than following from it; domains are related to but independent of LADs and replication-timing zones ([[10-Summaries/dixon-2012-tads|Dixon 2012]]). See [[30-Concepts/topologically-associating-domain]].
- **Single-cell hubs.** scSPRITE resolves nucleolar, speckle and chromocenter hubs in single cells and finds mutually exclusive TAD and enhancer-contact states ([[10-Summaries/arrastia-2022-scsprite|scSPRITE]]).
- **Single-cell resources.** A review of single-cell 3D genome methods ([[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]) and a unified sc3DG-seq pipeline and atlas ([[10-Summaries/jiang-2026-stark-scnucleome|STARK + scNucleome]]).
- **Protein-anchored interactions.** [[30-Concepts/chia-pet|ChIA-PET]] is the source of the ">40% of enhancers do not regulate their nearest promoter" statistic and of the "chromatin communities" scale-free network framing ([[10-Summaries/li-2014-chia-pet|Li 2014]]).

Immunoprecipitation cannot be done on one cell, so the protein-anchored branch has no single-cell member and instead serves as reference truth for protein-agnostic single-cell loop callers ([[10-Summaries/yu-2021-snaphic|SnapHiC]]). The single-cell 3D field traded the functional handle for per-cell resolution — unlike the histone field, where [[30-Concepts/cut-and-tag|CUT&Tag]] replaced ChIP with a low-input chemistry that *did* reach single cells ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]). (synthesis)

## Nuclear lamina and the DamID lineage

| Study | System | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/peric-hupkes-2010-lad-differentiation\|Peric-Hupkes 2010]] | Isogenic ESC → NPC → astrocyte | Lamin B1 DamID | ~1,100–1,400 LADs per cell type covering ~40% of the genome; relocation often confined to one transcription unit; silent genes that detach become more likely to activate one step later ("unlocking"); binary LAD/inter-LAD calls oversimplify a per-locus contact probability ([[10-Summaries/peric-hupkes-2010-lad-differentiation\|Peric-Hupkes 2010]]) |
| [[10-Summaries/van-steensel-2017-lads-review\|van Steensel 2017]] | Review (*Cell*) | — | cLAD/fLAD distinction, multivalent and redundant anchoring, three-compartment competition (lamina, nucleoli, pericentromeric) ([[10-Summaries/van-steensel-2017-lads-review\|van Steensel 2017]]) |
| [[10-Summaries/rooijers-2019-scdamt-seq\|scDam&T-seq]] | Single cells | Joint protein–DNA contacts + transcriptome | First single-cell coupling of lamina contact to transcription ([[10-Summaries/rooijers-2019-scdamt-seq\|Rooijers 2019]]) |
| [[10-Summaries/de-luca-2021-scdamid-protocol\|de Luca 2021]] | Mammalian cells | Bench protocol, Dam-LMNB1 | scDamID for nuclear-lamina contacts ([[10-Summaries/de-luca-2021-scdamid-protocol\|de Luca 2021]]) |
| [[10-Summaries/mali-2025-conformational-heterogeneity\|Mali 2025]] | Polymer model | Lamina-DamID restraints | The conformational-heterogeneity metric exposes structural noise from lamin depletion ([[10-Summaries/mali-2025-conformational-heterogeneity\|Mali 2025]]) |

See [[30-Concepts/lamina-associated-domains]] for the consolidated concept.

## Biophysical state: phase separation and mechanics

The youngest sub-axis of structural-physical locus state, covering LLPS condensates, viscoelasticity, and the coupling between mechanics and 3D-genome organization.

| Study | System | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/gibson-2019-chromatin-llps\|Gibson 2019]] | Reconstituted chromatin | Foundational LLPS | Histone tails drive phase separation, H1 tunes it, acetylation dissolves it, BRD4 creates an immiscible new phase ([[10-Summaries/gibson-2019-chromatin-llps\|Gibson 2019]]) |
| [[10-Summaries/ahn-2021-llps-cancer-looping\|Ahn 2021]] | NUP98-HOXA9 leukaemia | IDR mutagenesis and FUS-IDR substitution | IDR-driven LLPS induces CTCF-independent loops at proto-oncogenes; IDR identity is interchangeable, LLPS competence is load-bearing ([[10-Summaries/ahn-2021-llps-cancer-looping\|Ahn 2021]]) |
| [[10-Summaries/daugird-2024-viscoelastic-chromatin\|Daugird 2024]] | Live cells | Lattice light-sheet single-molecule imaging | Chromatin viscoelasticity and interchromatin accessibility are *constant* across density regimes; transcription locally stabilizes nucleosomes ([[10-Summaries/daugird-2024-viscoelastic-chromatin\|Daugird 2024]]) |
| [[10-Summaries/qi-zhang-2021-nucleoli-coalescence\|Qi & Zhang 2021]] | Polymer model | Hi-C-parameterized simulation | A viscoelastic chromatin network arrests nucleolus coalescence through an entropic barrier, stabilizing the multi-droplet state of nuclear bodies ([[10-Summaries/qi-zhang-2021-nucleoli-coalescence\|Qi & Zhang 2021]]) |

## Open questions

- **Why is intra-cell haplotype divergence (~61%) almost equal to inter-cell divergence (~63%)?** The paper reports this but does not explain it; regulatory-element actuation may be closer to a stochastic per-fiber event than a programmed per-cell state ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- **Do cohesin loops cause co-actuation?** Co-actuation domains of ~100 kb mirror cohesin loops at single-fiber resolution, but causality is not directly tested ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- How well do single-molecule chromatin readouts ([[daf-seq|DAF-seq]]) reconcile with droplet-scale ([[got-cha|GoT–ChA]]) data — when scDAF-seq reports 63% inter-cell actuation divergence, what would scATAC-seq from the same cells say? (synthesis)
- Does scDAF-seq generalize beyond GM24385 lymphoblastoid cells to primary tissue and disease contexts ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]])?

## Related

> [!cards]
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromosome territories, compartments, TADs and loops inside the nucleus.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Post-translational histone marks that demarcate functional chromatin states.

## All sources on this page

> [!info]- 36 summaries cited here
> - [[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]
> - [[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]
> - [[10-Summaries/bravo-2019-cistopic|Bravo González-Blas 2019]]
> - [[10-Summaries/danese-2021-episcanpy|Danese 2021]]
> - [[10-Summaries/daugird-2024-viscoelastic-chromatin|Daugird 2024]]
> - [[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]
> - [[10-Summaries/dixon-2012-tads|Dixon 2012]]
> - [[10-Summaries/fang-2021-snapatac|Fang 2021]]
> - [[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]
> - [[10-Summaries/gibson-2019-chromatin-llps|Gibson 2019]]
> - [[10-Summaries/gur-2025-scatac-vs-bulk|Gur & Hughes 2025]]
> - [[10-Summaries/he-2024-foodie|He 2024]]
> - [[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]
> - [[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]
> - [[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]
> - [[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]
> - [[10-Summaries/ku-2019-scchic-seq|Ku 2019]]
> - [[10-Summaries/li-2014-chia-pet|Li & Ruan 2014]]
> - [[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]
> - [[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]
> - [[10-Summaries/peric-hupkes-2010-lad-differentiation|Peric-Hupkes 2010]]
> - [[10-Summaries/pliner-2018-cicero|Pliner 2018]]
> - [[10-Summaries/qi-zhang-2021-nucleoli-coalescence|Qi & Zhang 2021]]
> - [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]
> - [[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]
> - [[10-Summaries/schep-2017-chromvar|Schep 2017]]
> - [[10-Summaries/shi-2026-dechic-seq|Shi 2026]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
> - [[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]
> - [[10-Summaries/van-steensel-2017-lads-review|van Steensel & Belmont 2017]]
> - [[10-Summaries/yeung-2023-scchix-seq|Yeung 2023]]
> - [[10-Summaries/yin-2019-deephistone|Yin 2019]]
> - [[10-Summaries/yu-2021-snaphic|Yu 2021]]
> - [[10-Summaries/zamanighomi-2018-scabc|Zamanighomi 2018]]
