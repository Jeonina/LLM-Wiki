---
type: topic
title: 3D genome
explainer: 3d-genome
aliases: [chromatin conformation, Hi-C, nuclear architecture, 3D chromatin organization]
tags: [Hi-C, TAD, compartments, loops, single-cell, chromatin-structure, chromatin]
created: 2026-05-12
updated: 2026-10-12
paper_section: ["3.5"]
---

# 3D genome

> The three-dimensional organization of DNA within the nucleus — chromosome territories, A/B compartments (active vs inactive) ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]), topologically associating domains (TADs) ([[10-Summaries/nagano-2013-nature|Nagano 2013]]), chromatin loops (e.g. enhancer–promoter, CTCF-anchored) ([[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]), and **spatial positioning relative to the nuclear lamina** ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]) — is a regulatory layer that shapes gene expression, replication timing, and cellular identity. Bulk Hi-C revealed the principles ([[10-Summaries/nagano-2013-nature|Nagano 2013]]); single-cell methods (scHi-C, sci-Hi-C, Dip-C, HiRES, Droplet Hi-C, scMicro-C) revealed the heterogeneity ([[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]), with TAD boundaries, compartments, loops, and lamina contacts varying substantially between cells in ways that bulk data cannot resolve ([[10-Summaries/tan-2018-science|Tan 2018]]; [[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).

> [!abstract] 한눈에
> 유전체는 염색체, compartment, TAD, loop로 이어지는 계층 구조로 접혀 있고, single-cell Hi-C로 보면 TAD 경계와 compartment가 세포마다 다르다 ([[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]; [[10-Summaries/nagano-2013-nature|Nagano 2013]]). TAD 경계가 깨지면 질환이 생기지만, TAD 호출 결과는 어떤 caller와 pipeline을 쓰느냐에 따라 달라진다 ([[10-Summaries/lupianez-2015-tad-disruption|Lupiáñez 2015]]; [[10-Summaries/kerpedjiev-2018-higlass|HiGlass]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [3D 유전체 교재](../60-Explainers/3d-genome.html)
<!-- /explainer-links -->

## Key points

- **The genome folds hierarchically.** Chromosomes → compartments (~5–10 Mb) → TADs (~100 kb–1 Mb) → loops (kb-scale) ([[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]; [[10-Summaries/nagano-2013-nature|Nagano 2013]]).
- **Single cells differ in their folds.** Compartments and TAD boundaries vary from cell to cell in ways that bulk Hi-C smears together ([[10-Summaries/nagano-2013-nature|Nagano 2013]]; [[10-Summaries/tan-2018-science|Tan 2018]]; [[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).
- **Boundary disruption is causal for disease.** Boundary-sparing controls of the same size are benign ([[10-Summaries/lupianez-2015-tad-disruption|Lupiáñez 2015]]); SVs fall into intra-TAD, TAD-fusion, neo-TAD and TAD-shuffling classes ([[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]).
- **Feature calls depend on the software.** Seven TAD callers give inconsistent domains on one matrix ([[10-Summaries/kerpedjiev-2018-higlass|HiGlass]]), and two pipelines correlate at only 0.83 on identical raw data ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]).
- **Single-cell callers report per cell type, not per cell.** SnapHiC, scGHOST, MINTsC and dcHiC all assume within-cluster homogeneity, so the single-cell formulation buys statistical power rather than per-cell feature variability ([[10-Summaries/yu-2021-snaphic|SnapHiC]]; [[10-Summaries/xiong-2024-scghost|scGHOST]]; [[10-Summaries/park-2026-mintsc|MINTsC]]; [[10-Summaries/chakraborty-2022-dchic|dcHiC]]) (synthesis).

## Start here

> [!cards]
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — The family of methods that profile genome-wide chromatin contacts in single cells.
> - `concept` [[30-Concepts/chromatin-compartments|Chromatin compartments]] — Large (~5–10 Mb) A (active) and B (inactive) blocks that associate in 3D.
> - `concept` [[30-Concepts/topologically-associating-domain|Topologically associating domain]] — Self-interacting ~100 kb–1 Mb neighbourhoods with sharp boundaries.
> - `concept` [[30-Concepts/chromatin-loop|Chromatin loop]] — A focal point-to-point contact enriched above its local background.
> - `concept` [[30-Concepts/lamina-associated-domains|Lamina-associated domains]] — Regions contacting the nuclear lamina; the cLAD/fLAD distinction.
> - `concept` [[30-Concepts/conformational-heterogeneity|Conformational heterogeneity]] — A single-number metric for cell-to-cell 3D variability.

## Hierarchy and why it matters

The 3D genome is mapped with 3C-family proximity-ligation methods — 3C, 4C, 5C, ChIA-PET, Hi-C, Capture Hi-C, Micro-C ([[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]). Single-cell variants — scHi-C, sci-Hi-C, Dip-C, HiRES, Droplet Hi-C, scMicro-C — extend these to per-cell 3D measurement ([[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]; [[10-Summaries/tan-2018-science|Tan 2018]]).

- **Regulatory layer.** Enhancer–promoter loops drive gene expression, while TAD boundaries constrain which regulatory interactions occur ([[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]).
- **Compartment switching** tracks cell-state changes during development and in cancer ([[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]).
- **LADs ≈ compartment B** at megabase scale — lamina-associated domains coincide with the inactive B compartment ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]).
- **LLPS-driven loops** can rewire 3D contacts independently of CTCF ([[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]).
- **Lamin depletion** raises conformational heterogeneity genome-wide, predicting an increase in transcriptional noise ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).

## Foundational bulk maps

These studies defined the features that single-cell methods now try to recover from sparse data ([[10-Summaries/durand-2016-juicer|Juicer]]).

| Study | Assay | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/lieberman-aiden-2009-hic\|Lieberman-Aiden 2009]] | Hi-C | Biotin fill-in at the ligation junction; 1 Mb maps from 8.4 million read pairs | The founding assay: A/B compartments by PCA, chromosome territories, the fractal-globule model and the *n*²-resolution rule; FISH validation at Spearman ρ = −0.916 between contact count and 3D distance ([[10-Summaries/lieberman-aiden-2009-hic\|Lieberman-Aiden 2009]]) |
| [[10-Summaries/dixon-2012-tads\|Dixon 2012]] | Hi-C | >1.7 billion read pairs, below 100 kb | Topological domains from the directionality index — 2,200 domains in mouse ES cells, median 880 kb, ~91% of the genome; boundaries marked by CTCF *plus* housekeeping genes, tRNAs and SINEs, yet only 15% of CTCF sites fall at boundaries ([[10-Summaries/dixon-2012-tads\|Dixon 2012]]) |
| [[10-Summaries/naumova-2013-mitotic-chromosome\|Naumova 2013]] | 5C + Hi-C | Interphase vs mitosis; HeLa S3, K562, HFF1 | Two folding states, not a continuum: compartments and TADs vanish in metaphase (see below) ([[10-Summaries/naumova-2013-mitotic-chromosome\|Naumova 2013]]) |
| [[10-Summaries/li-2014-chia-pet\|Li 2014]] | ChIA-PET | Protein-anchored proximity ligation | Source of the ">40% of enhancers skip their nearest promoter" statistic; this branch has no single-cell member ([[10-Summaries/li-2014-chia-pet\|Li 2014]]). See [[30-Concepts/chia-pet]] |
| [[10-Summaries/rao-2014-in-situ-hic\|Rao 2014]] | In situ Hi-C | Kilobase resolution | ~10,000 convergent-CTCF loops, 185 kb contact domains, six subcompartments, diploid and inactive-X maps ([[10-Summaries/rao-2014-in-situ-hic\|Rao 2014]]) |
| [[10-Summaries/hsieh-2015-micro-c\|Hsieh 2015]] | Micro-C | Nucleosome resolution, yeast | Gene-scaled domains bounded at promoters; compaction tied to transcription, RSC, Mediator, Rtt109 and the H4 tail ([[10-Summaries/hsieh-2015-micro-c\|Micro-C]]) |

**Mitotic chromosomes.** Interphase (G₁/S) 5C and Hi-C patterns correlate with each other (Spearman r > 0.67) but not with mitosis (r < 0.27); in metaphase both compartments and TADs disappear genome-wide, giving a homogeneous fold identical across HeLa S3, K562 and primary HFF1 ([[10-Summaries/naumova-2013-mitotic-chromosome|Naumova 2013]]).

- Mitotic structure is a compressed array of consecutive ~80–120 kb loops: *P(s)* ~ s^−0.5 from 100 kb to 10 Mb with a fall-off at 10 Mb; polymer simulation rejects hierarchical coiling and requires stochastic, consecutive loops plus axial compression — loop extrusion inferred from contact-probability shape ([[10-Summaries/naumova-2013-mitotic-chromosome|Naumova 2013]]).
- Epigenetic memory cannot live in the fold: since compartments and cell-type-invariant TADs are both absent in mitosis, higher-order structure must be rebuilt de novo in early G₁ from marks and bookmarking proteins ([[10-Summaries/naumova-2013-mitotic-chromosome|Naumova 2013]]).

## Single-cell assays

The single-cell 3D-genome story spans three measurement modalities — proximity ligation (scHi-C family, [[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]] + [[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]), protein-tethered methylation (DamID lineage, Kind/Rooijers/de Luca), and polymer modeling (Onufriev). The three should be read together (synthesis).

| Study | Year | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/nagano-2013-nature\|Nagano 2013]] | 2013 | First single-cell Hi-C | Cell-to-cell variability in TADs ([[10-Summaries/nagano-2013-nature\|Nagano 2013]]) |
| [[10-Summaries/ramani-2017-scihi-c\|sciHi-C]] | 2017 | Combinatorial indexing | 10,696 single-cell maps; in-silico cell-cycle sorting from the *P(s)* scaling coefficient alone ([[10-Summaries/ramani-2017-scihi-c\|Ramani 2017]]) |
| [[10-Summaries/tan-2018-science\|Dip-C]] | 2018 | Diploid Hi-C | Haplotype-resolved single-cell 3D structures ([[10-Summaries/tan-2018-science\|Tan 2018]]); see [[30-Concepts/dip-c]] |
| [[10-Summaries/arrastia-2022-scsprite\|scSPRITE]] | 2022 | Split-pool barcoding of crosslinked clusters | Multi-way single-cell contacts, nuclear-body hubs and heterogeneous TADs in mESCs ([[10-Summaries/arrastia-2022-scsprite\|scSPRITE]]); see [[30-Concepts/sc-sprite]] |
| [[10-Summaries/li-2023-scnanohi-c\|scNanoHi-C]] | 2023 | Long-read single-cell concatemer sequencing | Direct multi-way enhancer–promoter and ecDNA hubs ([[10-Summaries/li-2023-scnanohi-c\|scNanoHi-C]]) |
| [[10-Summaries/chang-2025-droplet-hi-c\|Droplet Hi-C]] | 2025 | Single-cell Hi-C on the 10x scATAC/Multiome kits; Paired Hi-C | Cortex 3D maps, multi-way hubs, ecDNA/HSR calling in tumours ([[10-Summaries/chang-2025-droplet-hi-c\|Droplet Hi-C]]) |

## Pipelines, storage and visualization

Two findings here are caveats on every 3D claim on this page: **TAD calls are caller-dependent** and **pipeline filtering stringency is a free parameter** ([[10-Summaries/kerpedjiev-2018-higlass|HiGlass]]; [[10-Summaries/servant-2015-hicpro|HiC-Pro]]).

| Tool | Year | Task | Note |
|---|---|---|---|
| [[10-Summaries/servant-2015-hicpro\|HiC-Pro]] | 2015 | Bulk processing | Valid-pair filtering, sparse ICE, allele-specific maps; 0.83 correlation against hiclib on identical input ([[10-Summaries/servant-2015-hicpro\|HiC-Pro]]) |
| [[10-Summaries/durand-2016-juicer\|Juicer]] | 2016 | Bulk processing and feature calling | HiCCUPS loops with 7/7 CRISPR-validated anchors, Arrowhead contact domains, the `.hic` format at 18 resolutions ([[10-Summaries/durand-2016-juicer\|Juicer]]) |
| [[10-Summaries/kerpedjiev-2018-higlass\|HiGlass]] | 2018 | Visualization | Composable linked views; seven TAD callers produce inconsistent domains of widely varying size on one matrix ([[10-Summaries/kerpedjiev-2018-higlass\|HiGlass]]) |
| [[10-Summaries/abdennur-2020-cooler\|Cooler]] | 2020 | Storage | Sparse HDF5 storage; 4D Nucleome standard; multi-resolution `.mcool` ([[10-Summaries/abdennur-2020-cooler\|Cooler]]) |
| [[10-Summaries/galasso-2026-map3c\|map3C]] | 2026 | Multiomic scHi-C processing | Contact calling, QC and SV-breakpoint annotation ([[10-Summaries/galasso-2026-map3c\|map3C]]) |

## Single-cell analysis methods

These tools extend scHi-C analysis from clustering to per-feature calling ([[10-Summaries/yu-2021-snaphic|SnapHiC]]; [[10-Summaries/xiong-2024-scghost|scGHOST]]; [[10-Summaries/park-2026-mintsc|MINTsC]]; [[10-Summaries/chakraborty-2022-dchic|dcHiC]]). Related concepts: [[30-Concepts/stark]] (unified sc3DG-seq analysis pipeline), [[30-Concepts/sscce]] (single-cell structural quality metric), [[30-Concepts/empty-cells-algorithm]] (filtering sc3DG-seq barcodes).

| Tool | Year | Task | Approach | Note |
|---|---|---|---|---|
| [[10-Summaries/zhou-2019-schicluster\|scHiCluster]] | 2019 | Embedding and clustering | Convolution + random-walk imputation | Coverage bias is the leading factor in scHi-C clustering ([[10-Summaries/zhou-2019-schicluster\|scHiCluster]]) |
| [[10-Summaries/zhang-2022-higashi\|Higashi]] | 2022 | Embedding, compartments, domains | Hypergraph representation learning | Per-cell compartments and sliding TAD-like boundaries ([[10-Summaries/zhang-2022-higashi\|Higashi]]) |
| [[10-Summaries/zhang-2022-fast-higashi\|Fast-Higashi]] | 2022 | Embedding | Tensor decomposition | Interpretable meta-interactions ([[10-Summaries/zhang-2022-fast-higashi\|Fast-Higashi]]) |
| [[10-Summaries/zheng-2022-bandnorm-scvi-3d\|BandNorm/scVI-3D]] | 2022 | Normalization benchmark | Band scaling vs imputation | Simple band scaling beats imputation except for rare or very sparse cells ([[10-Summaries/zheng-2022-bandnorm-scvi-3d\|BandNorm/scVI-3D]]) |
| [[10-Summaries/yu-2021-snaphic\|SnapHiC]] | 2021 | Loop calling | Cells as replicates, not as reads | 1,050–1,420 loops from 75 cells; 788 SNP–gene linkages for neuropsychiatric GWAS variants, including astrocyte-specific *APOE* enhancer loops ([[10-Summaries/yu-2021-snaphic\|SnapHiC]]); see [[30-Concepts/chromatin-loop]] |
| [[10-Summaries/li-2022-snaphic2\|SnapHiC2]] | 2022 | Loop calling | — | Efficient 5 kb single-cell loop calling ([[10-Summaries/li-2022-snaphic2\|SnapHiC2]]) |
| [[10-Summaries/liu-2024-snaphic-g\|SnapHiC-G]] | 2024 | Enhancer–promoter calling | Global background model | Cell-type-specific GWAS target-gene mapping ([[10-Summaries/liu-2024-snaphic-g\|SnapHiC-G]]) |
| [[10-Summaries/xiong-2024-scghost\|scGHOST]] | 2024 | Subcompartments | Graph embedding substitutes for the *trans* reads scHi-C lacks | ~50% of marker genes switch subcompartment *before* upregulation ([[10-Summaries/xiong-2024-scghost\|scGHOST]]) |
| [[10-Summaries/chakraborty-2022-dchic\|dcHiC]] | 2022 | Differential compartments | — | ~26% of significant compartment changes involve no A↔B flip; works on pseudobulk scHi-C from as few as 100 cells per condition ([[10-Summaries/chakraborty-2022-dchic\|dcHiC]]) |
| [[10-Summaries/park-2026-mintsc\|MINTsC]] | 2026 | Multi-way interactions | scHi-C as a multilayer network; a multi-way contact is a clique | Used to collapse the multiple-testing burden for epistatic eQTLs ([[10-Summaries/park-2026-mintsc\|MINTsC]]); see [[30-Concepts/multi-way-chromatin-interaction]] |
| [[10-Summaries/peng-2026-scdiagram\|scDIAGRAM]] | 2026 | A/B compartments | Imputation-free, single matrix | Compartment heterogeneity per cell ([[10-Summaries/peng-2026-scdiagram\|scDIAGRAM]]) |

**A cross-cutting gap.** SnapHiC, scGHOST, MINTsC and dcHiC report features per *cell type*, not per cell, and all assume within-cluster homogeneity. The single-cell formulation currently buys statistical power rather than per-cell feature variability. (synthesis)

## Nuclear lamina and nuclear bodies

Spatial positioning against the lamina is read with DamID rather than proximity ligation ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca 2021]]). Related concepts: [[30-Concepts/nuclear-lamina]] (peripheral organizing surface), [[30-Concepts/damid]] (protein–DNA contact mapping; the lamina assay class), [[30-Concepts/scdamt-seq]] (joint genome–protein + transcriptome readout).

- **LADs review.** The canonical LADs review describes three-compartment competition between the nuclear lamina, nucleoli and pericentric heterochromatin ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]).
- **scDamID protocol.** The canonical bench protocol for Dam-LMNB1 ↔ lamina contacts in single mammalian cells ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca 2021]]).
- **scDam&T-seq.** Joint protein–DNA contacts and transcriptome in the same cell via T7-IVT linear amplification; the lamina ↔ transcription coupling is concentrated in **fLADs (H3K27me3-rich)**, not in constitutive cLADs ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).
- **Nucleolus.** Genome organization in and around the nucleolus ([[10-Summaries/bersaglieri-2019-cells|Bersaglieri 2019]]).

## Heterogeneity metrics and physical mechanisms

Related concepts: [[30-Concepts/chromatin-phase-separation]] (LLPS condensates as a 3D-organization mechanism), [[30-Concepts/chromatin-mechanical-properties]] (viscoelastic / rigidity sub-axis).

- **Conformational heterogeneity.** C.H. = stdev_cells(⟨R_s⟩) measures cell-to-cell 3D variability; bulk-Hi-C-trained and scHi-C-trained *Drosophila* models diverge at 1–10 Mb, and lamin depletion raises C.H. genome-wide, predicting more transcriptional noise ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).
- **Phase-separation loops.** LLPS-competent IDR fusions (NUP98-HOXA9) induce **CTCF-independent chromatin loops** at oncogenic targets — a 3D-rearrangement class beyond SV- and CN-driven loops ([[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]).
- **Nuclear-body mechanics.** In polymer simulation, viscoelastic chromatin arrests nucleolus coalescence, stabilizing multi-droplet nuclear bodies ([[10-Summaries/qi-zhang-2021-nucleoli-coalescence|Qi & Zhang 2021]]).

## Structural variants and disease

- **TAD-boundary disruption** is causal for disease, and boundary-sparing controls of the same size are benign ([[10-Summaries/lupianez-2015-tad-disruption|Lupiáñez 2015]]).
- **SV taxonomy.** Intra-TAD, TAD-fusion, neo-TAD and TAD-shuffling SVs ([[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]).
- **Repeat expansions.** In laryngeal squamous cell carcinoma, nanopore-detected repeat expansions regulate *TP53BP2*/*FBXO28* via spatial proximity ([[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]).
- **Predicted 3D disruption in paediatric tumours.** Sequence-predicted 3D disruption from somatic SVs flags five recurrently disrupted 1 Mb regions, with ABC-weighted scoring prioritising SVs near PDGFRA, ID2 and the ATRT candidates NASP/MSH6/FOXJ2 ([[10-Summaries/gjoni-2026-pediatric-tumor-3d|Gjoni 2026]]).
- **ecDNA.** Droplet Hi-C and scNanoHi-C call ecDNA/HSR and ecDNA hubs in tumour cells ([[10-Summaries/chang-2025-droplet-hi-c|Droplet Hi-C]]; [[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).

## Sequence and foundation models

| Model | Year | Training data | Key result |
|---|---|---|---|
| [[10-Summaries/fang-2025-evo2hic\|Evo2HiC]] | 2025 | Evo 2 distilled into a small CNN, guided by 138 human ENCODE/4DN Hi-C maps | Improves sequence-to-contact prediction over Orca by 10.9% Spearman; enables Hi-C-conditioned, cell-type-specific motif attribution ([[10-Summaries/fang-2025-evo2hic\|Evo2HiC]]) |
| [[10-Summaries/wang-2026-hicfoundation\|HiCFoundation]] | 2026 | — | On low-coverage Hi-C from HSPCs and neutrophils, a genome-wide loss and weakening of short-range loops in neutrophils and after lamin B1 knockdown, while loops at neutrophil genes such as CEBPA and CEBPE were kept and rewired ([[10-Summaries/wang-2026-hicfoundation\|HiCFoundation]]) |

## Reviews and labs

- [[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]] — comprehensive review of sc3DG-seq technologies.
- [[10-Summaries/dautle-2025-schic-review|Dautle 2025]] — 13 scHi-C protocols scored on contacts and cis/trans; tool catalogue across QC, imputation, compartments, TADs, loops, 3D reconstruction and differential analysis.
- [[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]] — canonical LADs review.
- Labs: [[20-Entities/hua-jun-wu]] (Wu lab; STARK + scNucleome), [[20-Entities/fuying-dao]] (Dao lab; sc 3D genome review), [[20-Entities/jop-kind]] (Kind lab; scDamID + scDam&T-seq), [[20-Entities/alexey-onufriev]] (Onufriev lab; polymer models + C.H. metric).

## Open questions

- **Resolution.** Most sc3DG methods give ~1 Mb effective resolution per cell; bulk Hi-C achieves ~kb. Will ultra-deep single-cell or imaging-based methods (multiplexed FISH) close the gap? (synthesis)
- **Causality.** Do TAD/loop changes drive gene-expression changes or follow them? Multi-omics methods (sn-m3C, HiRES, scDam&T-seq) begin to address this ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]). (synthesis)
- **SV-driven 3D rearrangements.** Those detected by bulk nanopore sequencing point to a new genome-instability axis; single-cell resolution and contact-map validation are still missing ([[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]). (synthesis)
- **Why fLADs?** Why does the lamina ↔ transcription coupling restrict to fLADs (H3K27me3) and not cLADs (H3K9me3) ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]])? The differential heterochromatin "floor" vs "regulatable" interpretation needs perturbation testing.
- **Does imputation manufacture the variability it measures?** Both scHi-C imputation frameworks smooth toward neighbouring cells, so per-cell compartment and boundary variability is partly a function of the algorithm; neither quantifies the trade ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]; [[10-Summaries/zhang-2022-higashi|Higashi]]).
- **Which TAD definition is canonical?** Caller disagreement is documented but undiagnosed ([[10-Summaries/kerpedjiev-2018-higlass|HiGlass]]), and Dixon's own caveat — that cell-type differences in domain calls may be noise — remains unresolved ([[10-Summaries/dixon-2012-tads|Dixon 2012]]).
- **Orthogonal models?** Are bulk-Hi-C and scHi-C trained 3D models genuinely orthogonal in what they capture ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]])? The C.H. divergence at 1–10 Mb suggests yes.

## Related

> [!cards]
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — How DNA is packaged with proteins along chromosomes, and how that packaging varies across fibers, haplotypes and cells.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Methods that measure two or more molecular modalities in the same single cell.
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — Third-generation platforms that read DNA molecules of kilobases to hundreds of kilobases in single reads.
> - `note` [[50-Notes/regulatory-layers-overview|Regulatory layers overview]] — The 3D genome as one of the molecular regulatory layers.

## All sources on this page

> [!info]- 44 summaries cited here
> - [[10-Summaries/abdennur-2020-cooler|Abdennur & Mirny 2020]]
> - [[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]
> - [[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]
> - [[10-Summaries/bersaglieri-2019-cells|Bersaglieri & Santoro 2019]]
> - [[10-Summaries/chakraborty-2022-dchic|Chakraborty 2022]]
> - [[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]
> - [[10-Summaries/dautle-2025-schic-review|Dautle 2025]]
> - [[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]
> - [[10-Summaries/dixon-2012-tads|Dixon 2012]]
> - [[10-Summaries/durand-2016-juicer|Durand 2016]]
> - [[10-Summaries/fang-2025-evo2hic|Evo2HiC 2025]]
> - [[10-Summaries/galasso-2026-map3c|Galasso 2026]]
> - [[10-Summaries/gjoni-2026-pediatric-tumor-3d|Gjoni 2026]]
> - [[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]
> - [[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]
> - [[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]
> - [[10-Summaries/kerpedjiev-2018-higlass|Kerpedjiev 2018]]
> - [[10-Summaries/li-2014-chia-pet|Li & Ruan 2014]]
> - [[10-Summaries/li-2022-snaphic2|Li 2022]]
> - [[10-Summaries/li-2023-scnanohi-c|Li 2023]]
> - [[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]
> - [[10-Summaries/liu-2024-snaphic-g|Liu 2024]]
> - [[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]
> - [[10-Summaries/lupianez-2015-tad-disruption|Lupiáñez 2015]]
> - [[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]
> - [[10-Summaries/nagano-2013-nature|Nagano 2013]]
> - [[10-Summaries/naumova-2013-mitotic-chromosome|Naumova 2013]]
> - [[10-Summaries/park-2026-mintsc|Park 2026]]
> - [[10-Summaries/peng-2026-scdiagram|Peng 2026]]
> - [[10-Summaries/qi-zhang-2021-nucleoli-coalescence|Qi & Zhang 2021]]
> - [[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]
> - [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]
> - [[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]
> - [[10-Summaries/servant-2015-hicpro|Servant 2015]]
> - [[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]
> - [[10-Summaries/tan-2018-science|Tan 2018]]
> - [[10-Summaries/van-steensel-2017-lads-review|van Steensel & Belmont 2017]]
> - [[10-Summaries/wang-2026-hicfoundation|HiCFoundation 2026]]
> - [[10-Summaries/xiong-2024-scghost|Xiong 2024]]
> - [[10-Summaries/yu-2021-snaphic|Yu 2021]]
> - [[10-Summaries/zhang-2022-fast-higashi|Zhang 2022]]
> - [[10-Summaries/zhang-2022-higashi|Zhang 2022]]
> - [[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]
> - [[10-Summaries/zhou-2019-schicluster|Zhou 2019]]
