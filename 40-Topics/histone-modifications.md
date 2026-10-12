---
type: topic
title: Histone modifications
explainer: histone-modifications
aliases: [chromatin marks, post-translational modifications, PTMs, single-cell chromatin, histone marks]
tags: [chromatin, epigenetics, H3K27me3, H3K4me3, CUT&Tag, ChIC, MNase, enhancers, promoters]
created: 2026-05-12
updated: 2026-10-12
paper_section: ["3.4"]
---

# Histone modifications

> Post-translational modifications of histone tails — methylation, acetylation, ubiquitylation, phosphorylation — that demarcate functional chromatin states ([[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]).

> [!abstract] 한눈에
> 히스톤 꼬리의 변형은 promoter, enhancer, heterochromatin 같은 chromatin 상태를 표시하며, 이를 single cell에서 읽는 기술은 2015년 Drop-ChIP을 거쳐 2019년 scChIC-seq와 CUT&Tag로 실용화되었고, 지금은 한 세포에서 여러 mark와 5mC를 함께 읽는 단계까지 왔다 ([[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]; [[10-Summaries/rotem-2015-drop-chip|Rotem 2015]]; [[10-Summaries/ku-2019-scchic-seq|Ku 2019]]; [[10-Summaries/geisenberger-2025-scepi2-seq|scEpi²-seq]]). 그래도 세포당 감도는 여전히 낮고, 지금의 foundation model은 bulk 데이터로만 학습되어 single-cell histone 데이터를 입력으로 쓰지 않는다 ([[10-Summaries/bartosovic-2021-sccut-tag|Bartosovic 2021]]; [[10-Summaries/yu-2026-chrombert|ChromBERT]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 히스톤 변형](../60-Explainers/histone-modifications.html)
<!-- /explainer-links -->

## Key points

- **Each mark reports a chromatin state.** H3K4me3 marks active promoters, H3K27ac separates active from poised enhancers, and H3K27me3 and H3K9me3 mark facultative and constitutive heterochromatin ([[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]; [[10-Summaries/creyghton-2010-h3k27ac-enhancers|Creyghton 2010]]).
- **Single-cell profiling moved from one mark to several marks and modalities per cell.** It began with Drop-ChIP in 2015 ([[10-Summaries/rotem-2015-drop-chip|Rotem 2015]]), became practical in 2019 with scChIC-seq and scCUT&Tag, reached droplet-scale tissue profiling in 2021, and now reads two marks, marks plus 5mC, or marks plus RNA and surface protein in the same cell ([[10-Summaries/ku-2019-scchic-seq|Ku 2019]]; [[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]; [[10-Summaries/bartosovic-2021-sccut-tag|Bartosovic 2021]]; [[10-Summaries/yeung-2023-scchix-seq|scChIX-seq]]; [[10-Summaries/geisenberger-2025-scepi2-seq|scEpi²-seq]]; [[10-Summaries/schwager-2026-onecell-cut-tag|OneCell CUT&Tag]]).
- **Per-cell sensitivity is the recurring constraint.** Single-cell histone profiling has lagged scRNA-seq and scATAC-seq in sensitivity and throughput ([[10-Summaries/bartosovic-2021-sccut-tag|Bartosovic 2021]]), and even bulk CUT&Tag recovers only ~54% of ENCODE ChIP-seq peaks ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]).
- **Analysis choices matter more than method novelty.** In scHPTM pipelines bin size dominates, TF-IDF/LSI wins and feature selection hurts ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]); no tested imputer improves both signal and clustering ([[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025]]).
- **Sequence and foundation models are trained on bulk histone data only.** CANDI and ChromBERT take no single-cell histone input ([[10-Summaries/foroozandeh-2025-candi|CANDI]]; [[10-Summaries/yu-2026-chrombert|ChromBERT]]), and no scHPTM-specific or pretrained model was available to benchmark ([[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/chip-seq|ChIP-seq]] — The bulk ancestor of histone-mark profiling.
> - `concept` [[30-Concepts/cut-and-run|CUT&RUN]] — Antibody-tethered MNase with in situ release (Skene/Henikoff).
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — Antibody-tethered Tn5 (Kaya-Okur/Henikoff).
> - `concept` [[30-Concepts/chic-seq|ChIC-seq]] — The original chromatin immunocleavage (Schmid), ancestor of the MNase branch.
> - `concept` [[30-Concepts/scchix-seq|scChIX-seq]] — Two marks per cell with computational deconvolution.
> - `note` [[50-Notes/regulatory-layers-overview|Regulatory layers overview]] — Histone marks as one of the four molecular regulatory layers.

## Marks and the chromatin states they report

Modifications occur predominantly on histone H3 and H4 lysines and arginines ([[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]). They are the substrate for cell-type-specific gene regulation: profile them and you know which regions are active, primed, repressed or silenced ([[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]).

| Mark | State | Note |
|---|---|---|
| H3K4me3 | Active promoters ([[10-Summaries/klemm-2019-chromatin-accessibility-review\|Klemm 2019]]) | Tracks CpG density in ES cells (r_phi = 0.73) ([[10-Summaries/bernstein-2006-bivalent-chromatin\|Bernstein 2006]]) |
| H3K4me1 | Enhancers: alone = primed; + H3K27ac = active; + H3K27me3 = poised ([[10-Summaries/klemm-2019-chromatin-accessibility-review\|Klemm 2019]]) | Foundational partition established by [[10-Summaries/creyghton-2010-h3k27ac-enhancers\|Creyghton 2010]] |
| H3K27ac | Active promoters and enhancers ([[10-Summaries/klemm-2019-chromatin-accessibility-review\|Klemm 2019]]) | The discriminating mark separating active from inactive enhancers; eRNA production is specific to H3K27ac⁺ regions ([[10-Summaries/creyghton-2010-h3k27ac-enhancers\|Creyghton 2010]]) |
| H3K36me3 | Actively transcribed gene bodies ([[10-Summaries/klemm-2019-chromatin-accessibility-review\|Klemm 2019]]) | — |
| H3K27me3 | Facultative heterochromatin, Polycomb-repressed ([[10-Summaries/klemm-2019-chromatin-accessibility-review\|Klemm 2019]]) | Enriched at LAD borders in some cell types ([[10-Summaries/van-steensel-2017-lads-review\|van Steensel 2017]]); tracks conserved transposon-exclusion zones in ES cells (r_phi = 0.69) ([[10-Summaries/bernstein-2006-bivalent-chromatin\|Bernstein 2006]]) |
| H3K9me3 | Constitutive heterochromatin ([[10-Summaries/klemm-2019-chromatin-accessibility-review\|Klemm 2019]]) | The cLAD anchoring mark ([[10-Summaries/van-steensel-2017-lads-review\|van Steensel 2017]]) |

Beyond the one-mark-one-state picture:

- **Bivalency.** Bivalent domains were established in ES cells across 61 tiled regions, replicated in an independent line with a non-crosslinked MNase protocol (94/95 domains recovered) and confirmed on the same chromatin by sequential ChIP ([[10-Summaries/bernstein-2006-bivalent-chromatin|Bernstein 2006]]); bivalency was later refined to adjacent histones within one nucleosome ([[10-Summaries/rothbart-2014-histone-dna-language|Rothbart 2014]]).
- **Sequence predicts the ES-cell ground state.** The H3K4me3–CpG and H3K27me3–transposon-exclusion correlations weaken in differentiated cells ([[10-Summaries/bernstein-2006-bivalent-chromatin|Bernstein 2006]]).
- **The histone code is more complex than one mark per domain.** PTMs at the histone–DNA interface act physically on nucleosome stability; more than 200 distinct modified H3.2 and H4 N-terminal forms exist; readers engage multivalently in *cis* and *trans*; and acyl-CoA-derived marks couple chromatin state to metabolic flux ([[10-Summaries/rothbart-2014-histone-dna-language|Rothbart 2014]]).
- **Population reference.** Roadmap profiled 127 epigenomes on five core marks with a shared 15-state model; enhancer-associated marks carry essentially all the GWAS tissue signal, while H3K27me3 and H3K9me3 carry none ([[10-Summaries/roadmap-2015-111-epigenomes|Roadmap 2015]]).
- **Enhancer priming.** Collaborative binding of lineage-determining TFs primes enhancers, and HOMER was built to find it ([[10-Summaries/heinz-2010-homer|Heinz 2010]]).
- **Regulation by histone modifications** is reviewed in [[10-Summaries/andrew-2011-cellresearch|Bannister & Kouzarides 2011]].

## Overlap with other regulatory layers

Histone marks are not independent of other regulatory axes:

- **H3K9me2/3 anchors LADs to the nuclear lamina** via G9a and SUV39H1/2 acting redundantly ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]).
- **H3K27me3 is enriched at LAD boundaries** in some cell types ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]).
- **H3K27ac and other active marks** co-localize with accessible chromatin and compartment A regions ([[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]).
- **DNA methylation is partially redundant with H3K9me3** at heterochromatic regions, but *not* at LADs, where CpG methylation is not enriched ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]).

## Bulk profiling methods

| Method | Year | Enzyme | Note |
|---|---|---|---|
| [[30-Concepts/chip-seq\|ChIP-seq]] ([[10-Summaries/barski-2007-histone-methylation-chip-seq\|Barski 2007]]) | 2007 | — | Bulk ancestor; founding ChIP-Seq atlas of 20 histone methylations in human CD4⁺ T cells ([[10-Summaries/barski-2007-histone-methylation-chip-seq\|Barski 2007]]) |
| [[30-Concepts/chic-seq\|ChIC]] | — | MNase | Original chromatin immunocleavage (Schmid) |
| [[30-Concepts/cut-and-run\|CUT&RUN]] ([[10-Summaries/skene-2017-cut-and-run\|Skene 2017]]) | 2017 | pA-MNase | Antibody-tethered MNase with in situ release and spike-in ([[10-Summaries/skene-2017-cut-and-run\|Skene 2017]]) |
| [[30-Concepts/cut-and-tag\|CUT&Tag]] ([[10-Summaries/kaya-okur-2019-cut-and-tag\|Kaya-Okur 2019]]) | 2019 | pA-Tn5 | Antibody-tethered Tn5; the founding paper also introduced iCell8 scCUT&Tag ([[10-Summaries/kaya-okur-2019-cut-and-tag\|Kaya-Okur 2019]]) |

## Single-cell profiling methods

Single-cell profiling of histone marks began with droplet-based Drop-ChIP in 2015 ([[10-Summaries/rotem-2015-drop-chip|Rotem 2015]]), became practical in 2019 with scChIC-seq and iCell8 scCUT&Tag, was scaled to droplet-based tissue profiling in 2021, and has expanded into multi-mark and multimodal readouts ([[10-Summaries/ku-2019-scchic-seq|Ku 2019]]; [[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]; [[10-Summaries/bartosovic-2021-sccut-tag|Bartosovic 2021]]; [[10-Summaries/yeung-2023-scchix-seq|scChIX-seq]]; [[10-Summaries/geisenberger-2025-scepi2-seq|scEpi²-seq]]; [[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]; [[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]). Methods split into an MNase branch ([[30-Concepts/chic-seq|ChIC]], [[30-Concepts/sortchic|sortChIC]] — FACS-integrated single-cell ChIC) and a Tn5 branch ([[30-Concepts/cut-and-tag|CUT&Tag]]) (synthesis).

| Method | Year | Enzyme | Readout | Note |
|---|---|---|---|---|
| [[10-Summaries/rotem-2015-drop-chip\|Drop-ChIP]] | 2015 | MNase | One mark | Droplet barcoding of MNase-digested chromatin before ChIP; ~1,000 sites per cell ([[10-Summaries/rotem-2015-drop-chip\|Rotem 2015]]) |
| [[30-Concepts/scchic-seq\|scChIC-seq]] ([[10-Summaries/ku-2019-scchic-seq\|Ku 2019]]) | 2019 | MNase | One mark | First single-cell ChIC ([[10-Summaries/ku-2019-scchic-seq\|Ku 2019]]) |
| [[10-Summaries/wang-2019-cobatch\|CoBATCH]] | 2019 | PA-Tn5 | Histone marks, chromatin-binding proteins | In situ ChIP + combinatorial indexing; H3K27ac across endothelial cells from 10 embryonic organs ([[10-Summaries/wang-2019-cobatch\|CoBATCH]]) |
| [[10-Summaries/rooijers-2019-scdamt-seq\|scDam&T-seq]] | 2019 | — | Lamina contact, accessibility or Polycomb (RING1B) occupancy + transcriptome | Measured in single mESCs; allelic RING1B enrichment marks the inactive X ([[10-Summaries/rooijers-2019-scdamt-seq\|scDam&T-seq]]) |
| [[10-Summaries/bartosovic-2021-sccut-tag\|scCUT&Tag]] | 2021 | Tn5 | Marks + TFs in tissue | Active (H3K4me3, H3K27ac, H3K36me3) and repressive (H3K27me3) marks plus OLIG2 and RAD21 across tens of thousands of mouse CNS cells ([[10-Summaries/bartosovic-2021-sccut-tag\|Bartosovic 2021]]) |
| [[10-Summaries/wu-2021-sccut-tag\|Wu 2021]] scCUT&Tag | 2021 | Tn5 | Repressive marks | Cell typing in tissue and tumours ([[10-Summaries/wu-2021-sccut-tag\|Wu 2021]]) |
| [[10-Summaries/zhang-2022-sccut-tag-pro\|scCUT&Tag-pro]] | 2022 | Tn5 | Mark + surface protein | Multimodal chromatin-state inference ([[10-Summaries/zhang-2022-sccut-tag-pro\|scCUT&Tag-pro]]) |
| [[10-Summaries/gopalan-2022-multi-cut-and-tag\|Multi-CUT&Tag]] | 2022 | Tn5 | Several epitopes, barcoded | Multi-epitope co-localization (protocol) ([[10-Summaries/gopalan-2022-multi-cut-and-tag\|Gopalan 2022]]) |
| [[10-Summaries/bartosovic-2022-nano-cut-tag\|nano-CUT&Tag]] | 2022 | Nanobody-Tn5 | ATAC + H3K27ac + H3K27me3 per cell | 15.8-fold more H3K27me3 fragments than scCUT&Tag ([[10-Summaries/bartosovic-2022-nano-cut-tag\|Bartosovic 2022]]) |
| [[30-Concepts/scchix-seq\|scChIX-seq]] ([[10-Summaries/yeung-2023-scchix-seq\|Yeung 2023]]) | 2023 | MNase | Two marks per cell | Computational deconvolution of the two marks ([[10-Summaries/yeung-2023-scchix-seq\|Yeung 2023]]) |
| [[30-Concepts/scicut-tag\|sciCUT&Tag]] / [[30-Concepts/multi-tag\|MulTI-Tag]] ([[10-Summaries/janssens-2023-scicut-tag\|Janssens 2023]]) | 2023 | Tn5 | One or several epitopes | Combinatorial indexing at 40k cells/chip; MulTI-Tag for multi-epitope ([[10-Summaries/janssens-2023-scicut-tag\|Janssens 2023]]) |
| [[10-Summaries/li-2024-scnanoseq-cut-tag\|scNanoSeq-CUT&Tag]] | 2024 | Tn5 | Histone marks, TFs, long reads | Profiles repeats, blacklist regions and allele-specific peaks ([[10-Summaries/li-2024-scnanoseq-cut-tag\|Li 2024]]) |
| [[30-Concepts/scepi2-seq\|scEpi²-seq]] ([[10-Summaries/geisenberger-2025-scepi2-seq\|Geisenberger 2025]]) | 2025 | MNase | Mark + 5mC | sortChIC + TAPS ([[10-Summaries/geisenberger-2025-scepi2-seq\|Geisenberger 2025]]) |
| [[30-Concepts/6-base-cut-and-tag\|6-base-CUT&Tag]] ([[10-Summaries/tavares-2026-6-base-cut-tag\|Tavares 2026]]) | 2026 | Tn5 | 5mC + 5hmC + mark per fragment | Bulk so far; single-cell extension not yet demonstrated ([[10-Summaries/tavares-2026-6-base-cut-tag\|Tavares 2026]]) |
| [[10-Summaries/schwager-2026-onecell-cut-tag\|OneCell CUT&Tag]] | 2026 | Tn5 | Chromatin + RNA + surface markers | Plate-based, starts from single cells; benchmarked against sortChIC, scChIP-seq and 10x scCUT&Tag ([[10-Summaries/schwager-2026-onecell-cut-tag\|Schwager 2026]]) |
| [[10-Summaries/shi-2026-dechic-seq\|DeChIC-seq]] | 2026 | Deaminase | Histone marks + TF binding | Single-blastomere resolution ([[10-Summaries/shi-2026-dechic-seq\|Shi 2026]]) |

## Single-cell findings

- **Two waves of H3K27me3.** In P19 mouse oligodendrocyte differentiation, H3K27me3 is deposited first at neuronal genes, then at neuronal and OPC genes such as *Sox5*, *Sox6* and *Ptprz1* ([[10-Summaries/bartosovic-2022-nano-cut-tag|Bartosovic 2022]]).
- **Promoter breadth.** Single-cell H3K4me3 shows promoter breadth increasing along OPC → mature oligodendrocyte differentiation ([[10-Summaries/bartosovic-2021-sccut-tag|Bartosovic 2021]]).
- **Locus-level mark transitions.** scChIX-seq shows H3K27me3/H3K9me3 transitions at individual loci — cell-type-independent at *Bcl2*, cell-type-specific at *Crim1* ([[10-Summaries/yeung-2023-scchix-seq|Yeung 2023]]).
- **Oncogenic enhancer activation.** LLPS-competent IDR fusions (NUP98-HOXA9) induce H3K27ac at off-target proto-oncogenes ([[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]).

## Benchmarks, bias correction and reviews

| Study | Year | Data | Key finding |
|---|---|---|---|
| [[10-Summaries/abbasova-2025-cut-tag-encode-benchmark\|Abbasova 2025]] | 2025 | Bulk CUT&Tag vs ENCODE ChIP-seq | ~54% recall, mark-dependent signal-to-noise, peak-calling guidance ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark\|Abbasova 2025]]) |
| [[10-Summaries/raimundo-2023-schptm-benchmark\|Raimundo 2023]] | 2023 | scHPTM analysis pipelines | Bin size dominates, TF-IDF/LSI wins, feature selection hurts ([[10-Summaries/raimundo-2023-schptm-benchmark\|Raimundo 2023]]) |
| [[10-Summaries/morenogonzalez-2025-schistone-imputation\|SCIBED]] | 2025 | 10 scRNA/scATAC imputers on sortChIC and scCUT&Tag mouse data | No method improves both signal and clustering; no scHPTM-specific or pretrained model to test ([[10-Summaries/morenogonzalez-2025-schistone-imputation\|Moreno-González 2025]]) |
| [[10-Summaries/hu-2026-patty\|PATTY]] | 2026 | Bulk and single-cell CUT&Tag | Corrects Tn5 open-chromatin bias ([[10-Summaries/hu-2026-patty\|PATTY]]) |

Reviews:

- [[10-Summaries/ludwig-2019-sc-chromatin-modifications-review|Ludwig & Bintu 2019]] — single-cell histone and DNA-modification methods (scChIP, scCUT&Tag, scChIC, Co-ChIP, EpiTOF, live reporters).
- [[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]] — computational review of scCUT&Tag: 21 datasets, workflow, differences from scATAC, integration gaps.
- [[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]] — canonical histone-marks reference used for the mark → state mapping.
- [[10-Summaries/andrew-2011-cellresearch|Bannister & Kouzarides 2011]] — regulation of chromatin by histone modifications.

## Sequence and foundation models

| Tool | Year | Input | Model | Note |
|---|---|---|---|---|
| [[10-Summaries/yin-2019-deephistone\|DeepHistone]] | 2019 | DNA + DNase-seq | CNN | Predicts 7 marks ([[10-Summaries/yin-2019-deephistone\|DeepHistone]]) |
| [[10-Summaries/gao-2024-epigept\|EpiGePT]] | 2024 | Sequence + TF-expression context vector | Pretrained transformer | Predicts H3K27ac, H3K4me1, H3K4me3, H3K36me3, H3K27me3 and H3K9me3, including in cell types unseen in training ([[10-Summaries/gao-2024-epigept\|EpiGePT]]) |
| [[10-Summaries/foroozandeh-2025-candi\|CANDI]] | 2025 (preprint) | Bulk ENCODE histone ChIP-seq and accessibility | Self-supervised transformer | Imputes and denoises; trained and tested on bulk only, no single-cell input ([[10-Summaries/foroozandeh-2025-candi\|CANDI]]) |
| [[10-Summaries/yu-2026-chrombert\|ChromBERT]] | 2026 | Bulk: 76 histone modifications, 991 transcription regulators, DNase/ATAC | BERT-style | No single-cell histone input; excludes or ignores histone channels in several downstream tasks ([[10-Summaries/yu-2026-chrombert\|ChromBERT]]) |

## Key labs

- [[20-Entities/keji-zhao]] — Zhao lab; scChIC-seq.
- [[20-Entities/steven-henikoff]] — Henikoff lab; CUT&RUN, CUT&Tag, sciCUT&Tag, MulTI-Tag.
- [[20-Entities/alexander-van-oudenaarden]] — van Oudenaarden lab; sortChIC, scChIX-seq, scEpi²-seq.
- [[20-Entities/shankar-balasubramanian]] — Balasubramanian lab; 6-base-CUT&Tag.
- [[20-Entities/jake-yeung]] — Yeung; scChIX-seq.

## Open questions

- Per-cell sensitivity is the recurring constraint: single-cell histone-modification profiling has lagged scRNA-seq and scATAC-seq in sensitivity and throughput ([[10-Summaries/bartosovic-2021-sccut-tag|Bartosovic 2021]]). How much can linear amplification or library optimization improve this?
- Active vs repressive mark mutual exclusivity at the single-cell level: bulk data show clean separation, but scChIX-seq results show H3K27me3/H3K9me3 transitions at individual loci — cell-type-independent at *Bcl2*, cell-type-specific at *Crim1* — that bulk averages obscure ([[10-Summaries/yeung-2023-scchix-seq|Yeung 2023]]).
- How redundant are histone marks with LAD position? H3K9me2/3 anchors LADs ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]) — does any histone mark add information once you know LAD status?
- MNase-based (sortChIC family) vs Tn5-based (CUT&Tag family) single-cell chromatin profiling: what are the tradeoffs in nucleosome-positioning fidelity vs throughput? See [[50-Notes/mnase-vs-tn5-chromatin]]. (synthesis)
- Can a pretrained model use single-cell histone data? Current models are bulk-only ([[10-Summaries/foroozandeh-2025-candi|CANDI]]; [[10-Summaries/yu-2026-chrombert|ChromBERT]]), and imputers borrowed from scRNA/scATAC do not improve both signal and clustering ([[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025]]). (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — How DNA is packaged with proteins along chromosomes, and how that packaging varies across fibers, haplotypes and cells.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5-methylcytosine at CpG dinucleotides, the most stable and best-studied epigenetic mark.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Methods that measure two or more molecular modalities in the same single cell.

## All sources on this page

> [!info]- 38 summaries cited here
> - [[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]
> - [[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]
> - [[10-Summaries/andrew-2011-cellresearch|Bannister & Kouzarides 2011]]
> - [[10-Summaries/barski-2007-histone-methylation-chip-seq|Barski 2007]]
> - [[10-Summaries/bartosovic-2021-sccut-tag|Bartosovic 2021]]
> - [[10-Summaries/bartosovic-2022-nano-cut-tag|Bartosovic 2022]]
> - [[10-Summaries/bernstein-2006-bivalent-chromatin|Bernstein 2006]]
> - [[10-Summaries/creyghton-2010-h3k27ac-enhancers|Creyghton 2010]]
> - [[10-Summaries/foroozandeh-2025-candi|Foroozandeh 2025 CANDI]]
> - [[10-Summaries/gao-2024-epigept|EpiGePT 2024]]
> - [[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]
> - [[10-Summaries/gopalan-2022-multi-cut-and-tag|Gopalan 2022]]
> - [[10-Summaries/heinz-2010-homer|Heinz 2010]]
> - [[10-Summaries/hu-2026-patty|Hu 2026]]
> - [[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]
> - [[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]
> - [[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]
> - [[10-Summaries/ku-2019-scchic-seq|Ku 2019]]
> - [[10-Summaries/li-2024-scnanoseq-cut-tag|Li 2024]]
> - [[10-Summaries/ludwig-2019-sc-chromatin-modifications-review|Ludwig & Bintu 2019]]
> - [[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025 SCIBED]]
> - [[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]
> - [[10-Summaries/roadmap-2015-111-epigenomes|Roadmap Epigenomics 2015]]
> - [[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]
> - [[10-Summaries/rotem-2015-drop-chip|Rotem 2015]]
> - [[10-Summaries/rothbart-2014-histone-dna-language|Rothbart & Strahl 2014]]
> - [[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]
> - [[10-Summaries/shi-2026-dechic-seq|Shi 2026]]
> - [[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]
> - [[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]
> - [[10-Summaries/van-steensel-2017-lads-review|van Steensel & Belmont 2017]]
> - [[10-Summaries/wang-2019-cobatch|Wang 2019]]
> - [[10-Summaries/wu-2021-sccut-tag|Wu 2021]]
> - [[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]
> - [[10-Summaries/yeung-2023-scchix-seq|Yeung 2023]]
> - [[10-Summaries/yin-2019-deephistone|Yin 2019]]
> - [[10-Summaries/yu-2026-chrombert|Yu 2026 ChromBERT]]
> - [[10-Summaries/zhang-2022-sccut-tag-pro|Zhang 2022]]
