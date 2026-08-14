---
type: topic
title: 3D genome
aliases: [chromatin conformation, Hi-C, nuclear architecture, 3D chromatin organization]
tags: [Hi-C, TAD, compartments, loops, single-cell, chromatin-structure, chromatin]
created: 2026-05-12
updated: 2026-08-10
---

# 3D genome

> The three-dimensional organization of DNA within the nucleus — chromosome territories, A/B compartments (active vs inactive) ([[10-Summaries/van-steensel-2017-lads-review]]), topologically associating domains (TADs) ([[10-Summaries/nagano-2013-nature]]), chromatin loops (e.g. enhancer–promoter, CTCF-anchored) ([[10-Summaries/ahn-2021-llps-cancer-looping]]), and **spatial positioning relative to the nuclear lamina** ([[10-Summaries/van-steensel-2017-lads-review]]) — is a regulatory layer that shapes gene expression, replication timing, and cellular identity. Bulk Hi-C revealed the principles ([[10-Summaries/nagano-2013-nature]]); single-cell methods (scHi-C, sciHi-C, Dip-C, scSPRITE, scNanoHi-C, scDamID) revealed the heterogeneity ([[10-Summaries/hong-2025-sc3d-genome-review]]), with TAD boundaries, compartments, loops, and lamina contacts varying substantially between cells in ways that bulk data cannot resolve ([[10-Summaries/tan-2018-science]]; [[10-Summaries/mali-2025-conformational-heterogeneity]]).

## Hierarchical organization

The 3D genome is organized hierarchically across scales: chromosomes → compartments (~5–10 Mb) → TADs (~100 kb–1 Mb) → loops (kb-scale) ([[10-Summaries/hong-2025-sc3d-genome-review]]; [[10-Summaries/nagano-2013-nature]]). It is mapped via 3C-family proximity-ligation methods — 3C, 4C, 5C, ChIA-PET, Hi-C, Capture Hi-C, Micro-C ([[10-Summaries/hong-2025-sc3d-genome-review]]). Single-cell variants — scHi-C, sciHi-C, Dip-C, scSPRITE, scNanoHi-C — extend these to per-cell 3D measurement ([[10-Summaries/hong-2025-sc3d-genome-review]]; [[10-Summaries/tan-2018-science]]), revealing substantial cell-to-cell variability in compartments and TAD boundaries that bulk Hi-C smears together ([[10-Summaries/nagano-2013-nature]]; [[10-Summaries/mali-2025-conformational-heterogeneity]]).

## Why it matters

- **Regulatory layer**: enhancer–promoter loops drive gene expression, while TAD boundaries constrain which regulatory interactions occur ([[10-Summaries/hong-2025-sc3d-genome-review]]).
- **Compartment switching** tracks cell-state changes during development and in cancer ([[10-Summaries/hong-2025-sc3d-genome-review]]).
- **LADs ≈ Compartment B** at megabase scale — lamina-associated domains coincide with the inactive B compartment ([[10-Summaries/van-steensel-2017-lads-review]]).
- **LLPS-driven loops** can rewire 3D contacts independently of CTCF ([[10-Summaries/ahn-2021-llps-cancer-looping]]).
- **Lamin depletion** raises conformational heterogeneity genome-wide → predicted increase in transcriptional noise ([[10-Summaries/mali-2025-conformational-heterogeneity]]).

## Core concepts

- [[30-Concepts/single-cell-hi-c]] — the assay class
- [[30-Concepts/topologically-associating-domain]] — TADs
- [[30-Concepts/chromatin-compartments]] — A/B compartments
- [[30-Concepts/sc-sprite]] — sonication-based multi-way contact capture
- [[30-Concepts/dip-c]] — diploid Hi-C
- [[30-Concepts/stark]] — unified sc3DG-seq analysis pipeline
- [[30-Concepts/sscce]] — single-cell structural quality metric
- [[30-Concepts/empty-cells-algorithm]] — filtering sc3DG-seq barcodes
- [[30-Concepts/nuclear-lamina]] — peripheral organizing surface
- [[30-Concepts/lamina-associated-domains]] — LADs; the cLAD/fLAD distinction (compartment B substrate)
- [[30-Concepts/damid]] — protein–DNA contact mapping; the lamina assay class
- [[30-Concepts/scdamt-seq]] — joint genome–protein + transcriptome readout
- [[30-Concepts/conformational-heterogeneity]] — across-cell 3D variability metric
- [[30-Concepts/chromatin-phase-separation]] — LLPS condensates as a 3D-organization mechanism
- [[30-Concepts/chromatin-mechanical-properties]] — viscoelastic / rigidity sub-axis

## Key entities

- [[20-Entities/hua-jun-wu]] — Wu lab; STARK + scNucleome
- [[20-Entities/fuying-dao]] — Dao lab; sc 3D genome review
- [[20-Entities/jop-kind]] — Kind lab; scDamID + scDam&T-seq
- [[20-Entities/alexey-onufriev]] — Onufriev lab; polymer models + C.H. metric

## Sources, by sub-theme

### Review
- [[10-Summaries/hong-2025-sc3d-genome-review]] — Hong/Dao 2025. Comprehensive review of sc3DG-seq technologies.
- [[10-Summaries/van-steensel-2017-lads-review]] — van Steensel & Belmont 2017. Canonical LADs review; three-compartment competition (NL/nucleoli/pericentric).

### Foundational Hi-C
- [[10-Summaries/lieberman-aiden-2009-hic]] — Lieberman-Aiden et al. 2009. The founding assay; A/B compartments, chromosome territories, fractal globule, and the *n*²-resolution rule.
- [[10-Summaries/dixon-2012-tads]] — Dixon et al. 2012. Topological domains from the directionality index; boundaries marked by CTCF *plus* housekeeping genes, tRNAs and SINEs.
- [[10-Summaries/naumova-2013-mitotic-chromosome]] — Naumova et al. 2013. Compartments and TADs both vanish in metaphase; two folding states, not a continuum.
- [[10-Summaries/nagano-2013-nature]] — Nagano et al. 2013. First single-cell Hi-C; cell-to-cell variability in TADs.
- [[10-Summaries/ramani-2017-scihi-c]] — Ramani et al. 2017. sciHi-C; combinatorial indexing to 10,696 cells, in-silico cell-cycle sorting.
- [[10-Summaries/tan-2018-science]] — Tan et al. 2018. Dip-C; haplotype-resolved single-cell 3D structures.

### Pipelines, storage, visualization
- [[10-Summaries/servant-2015-hicpro]] — Servant et al. 2015. Valid-pair filtering, sparse ICE, allele-specific maps; filtering stringency is a free parameter (0.83 correlation against hiclib on identical input).
- [[10-Summaries/durand-2016-juicer]] — Durand et al. 2016. Juicer, HiCCUPS loops, Arrowhead domains, the `.hic` format.
- [[10-Summaries/abdennur-2020-cooler]] — Abdennur & Mirny 2020. Sparse HDF5 storage; 4D Nucleome standard; multi-resolution `.mcool`.
- [[10-Summaries/kerpedjiev-2018-higlass]] — Kerpedjiev et al. 2018. Composable linked views; seven TAD callers disagree on one matrix.
- [[10-Summaries/zhou-2019-schicluster]] — Zhou et al. 2019. Convolution + random-walk imputation; coverage bias is the leading factor in scHi-C clustering.
- [[10-Summaries/zhang-2022-higashi]] — Zhang et al. 2022. Hypergraph representation learning; per-cell compartments and sliding TAD-like boundaries.

### Clinical / cancer SVs (related to 3D regulation)
- [[10-Summaries/liu-2025-nanopore-lscc-svs]] — Liu et al. 2025. Repeat expansions regulating *TP53BP2*/*FBXO28* via spatial proximity.

### Nuclear lamina / spatial positioning (DamID lineage)

- [[10-Summaries/de-luca-2021-scdamid-protocol]] — de Luca & Kind 2021. Canonical bench protocol for scDamID; Dam-LMNB1 ↔ lamina contacts in single mammalian cells.
- [[10-Summaries/rooijers-2019-scdamt-seq]] — Rooijers/Kind/Dey 2019. **scDam&T-seq**: joint protein–DNA contacts + transcriptome in same cell via T7-IVT linear amplification. Reveals that the lamina↔transcription coupling is concentrated in **fLADs (H3K27me3-rich)**, not in constitutive cLADs.

### Conformational heterogeneity (single-cell 3D metrics)

- [[10-Summaries/mali-2025-conformational-heterogeneity]] — Mali/Onufriev 2025. Defines **C.H. = stdev_cells(⟨R_s⟩)** as a metric for cell-to-cell 3D variability. Bulk-Hi-C-trained vs scHi-C-trained *Drosophila* models diverge at 1–10 Mb; lamin depletion raises C.H. genome-wide → prediction of increased transcriptional noise.

### Phase separation × 3D architecture

- [[10-Summaries/ahn-2021-llps-cancer-looping]] — Ahn/Wang 2021. LLPS-competent IDR fusions induce **CTCF-independent chromatin loops** at oncogenic targets. New 3D-rearrangement class beyond SV/CN-driven loops.
- [[10-Summaries/qi-zhang-2021-nucleoli-coalescence]] — Qi/Zhang 2021. Polymer simulation: viscoelastic chromatin arrests nucleolus coalescence, stabilizing multi-droplet nuclear bodies.

## Synthesized notes

The single-cell 3D-genome story spans three measurement modalities — proximity ligation (scHi-C family, Hong 2025 + Jiang 2026), protein-tethered methylation (DamID lineage, Kind/Rooijers/de Luca), and polymer modeling (Onufriev). The three should be read together.

## Open questions

- Resolution: most sc3DG methods give ~1 Mb effective resolution per cell; bulk Hi-C achieves ~kb. Will ultra-deep single-cell or imaging-based methods (multiplexed FISH) close the gap?
- Causality: do TAD/loop changes drive gene-expression changes or follow them? Multi-omics methods (sn-m3C, HiRES, scDam&T-seq) begin to address this.
- Single-cell SV-driven 3D rearrangements (Liu 2025) point to a new genome-instability axis.
- Why does the lamina↔transcription coupling restrict to fLADs (H3K27me3) and not cLADs (H3K9me3) ([[10-Summaries/rooijers-2019-scdamt-seq]])? The differential heterochromatin "floor" vs "regulatable" interpretation needs perturbation testing.
- **Does imputation manufacture the variability it measures?** Both scHi-C imputation frameworks smooth toward neighbouring cells, so per-cell compartment and boundary variability is partly a function of the algorithm; neither quantifies the trade ([[10-Summaries/zhou-2019-schicluster]], [[10-Summaries/zhang-2022-higashi]]).
- **Which TAD definition is canonical?** Caller disagreement is documented but undiagnosed ([[10-Summaries/kerpedjiev-2018-higlass]]), and Dixon's own caveat — that cell-type differences in domain calls may be noise — remains unresolved ([[10-Summaries/dixon-2012-tads]]).
- Are bulk-Hi-C and scHi-C trained 3D models genuinely orthogonal in what they capture ([[10-Summaries/mali-2025-conformational-heterogeneity]])? The C.H. divergence at 1–10 Mb suggests yes.

## Additions — 2026-08-10 ingests

- **Two folding states, not a continuum.** Interphase (G₁/S) 5C and Hi-C patterns correlate with each other (Spearman r > 0.67) but not with mitosis (r < 0.27); in metaphase both compartments and TADs disappear genome-wide, giving a homogeneous fold identical across HeLa S3, K562 and primary HFF1 ([[10-Summaries/naumova-2013-mitotic-chromosome]]).
- **Mitotic structure is a compressed array of consecutive ~80–120 kb loops.** *P(s)* ~ s^−0.5 from 100 kb to 10 Mb with a fall-off at 10 Mb; polymer simulation rejects hierarchical coiling and requires stochastic, consecutive loops plus axial compression — loop extrusion inferred from contact-probability shape ([[10-Summaries/naumova-2013-mitotic-chromosome]]).
- **Epigenetic memory cannot live in the fold.** Since compartments and cell-type-invariant TADs are both absent in mitosis, higher-order structure must be rebuilt de novo in early G₁ from marks and bookmarking proteins ([[10-Summaries/naumova-2013-mitotic-chromosome]]).
- **Boundary disruption is causal for disease** — and boundary-sparing controls of the same size are benign ([[10-Summaries/lupianez-2015-tad-disruption]]); the clinical taxonomy of intra-TAD / TAD-fusion / neo-TAD / TAD-shuffling SVs is in [[10-Summaries/spielmann-2018-sv-3d-genome]].
- **Bulk feature definitions** (HiCCUPS loops with 7/7 CRISPR-validated anchors, Arrowhead contact domains, `.hic` at 18 resolutions) come from [[10-Summaries/durand-2016-juicer]]; single-cell methods try to recover them from sparse data.

**Foundational layer, now in place.** [[10-Summaries/lieberman-aiden-2009-hic]] is the founding Hi-C paper — biotin fill-in at the ligation junction, 1 Mb contact maps from 8.4 million read pairs, the discovery of A/B compartments by PCA, FISH validation at Spearman ρ = −0.916 between contact count and 3D distance, and the fractal-globule model. [[10-Summaries/dixon-2012-tads]] pushes resolution below 100 kb with >1.7 billion read pairs and identifies topological domains via the directionality index — 2,200 domains in mouse ES cells, median 880 kb, covering ~91% of the genome, with only 15% of CTCF sites falling at boundaries.

The single-cell branch: [[10-Summaries/ramani-2017-scihi-c]] applies combinatorial indexing to conformation, producing 10,696 single-cell maps and demonstrating in-silico cell-cycle sorting from the *P(s)* scaling coefficient alone.

Infrastructure is catalogued under *Pipelines, storage, visualization* above. Two findings from it belong here as caveats on every 3D claim on this page: **TAD calls are caller-dependent** — seven callers produce inconsistent domains of widely varying size on one matrix ([[10-Summaries/kerpedjiev-2018-higlass]]) — and **pipeline filtering stringency is a free parameter**, with two pipelines correlating at only 0.83 on identical raw data ([[10-Summaries/servant-2015-hicpro]]).


## Related

- [[40-Topics/chromatin-architecture]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/long-read-sequencing]]
- [[50-Notes/regulatory-layers-overview]] — 3D genome as one of the four molecular regulatory layers

## Linked summaries (lint pass 2026-05-21)

- [[10-Summaries/bersaglieri-2019-cells]] — Bersaglieri & Santoro 2019 — Genome organization in and around the nucleolus.
- [[10-Summaries/naumova-2013-mitotic-chromosome]] · [[10-Summaries/lupianez-2015-tad-disruption]] · [[10-Summaries/spielmann-2018-sv-3d-genome]] · [[10-Summaries/durand-2016-juicer]]

## Added 2026-08-13

Five sources ingested 2026-08-13 extend the single-cell 3D toolkit from clustering to per-feature calling, and add the protein-anchored branch.

- **Loops**: [[10-Summaries/yu-2021-snaphic]] (SnapHiC) — cells as replicates, not as reads; 1,050–1,420 loops from 75 cells; 788 SNP–gene linkages for neuropsychiatric GWAS variants including astrocyte-specific *APOE* enhancer loops. See [[30-Concepts/chromatin-loop]].
- **Subcompartments**: [[10-Summaries/xiong-2024-scghost]] (scGHOST) — graph embedding substitutes for the *trans* reads scHi-C does not have; ~50% of marker genes switch subcompartment *before* upregulation.
- **Multi-way interactions**: [[10-Summaries/park-2026-mintsc]] (MINTsC) — scHi-C as a multilayer network, multi-way contact as a clique; used to collapse the multiple-testing burden for epistatic eQTLs. See [[30-Concepts/multi-way-chromatin-interaction]].
- **Differential compartments**: [[10-Summaries/chakraborty-2022-dchic]] (dcHiC) — ~26% of significant compartment changes involve no A↔B flip; works on pseudobulk scHi-C from as few as 100 cells per condition.
- **The protein-anchored branch**: [[10-Summaries/li-2014-chia-pet]] — source of the ">40% of enhancers skip their nearest promoter" statistic, and of the observation that this branch has no single-cell member. See [[30-Concepts/chia-pet]].

**A cross-cutting gap.** All four single-cell methods report features per *cell type*, not per cell, and all assume within-cluster homogeneity. The single-cell formulation currently buys statistical power rather than per-cell feature variability. (synthesis)
