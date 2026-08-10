---
type: topic
title: Single-cell multi-omics
aliases: [single-cell multiomics, sc-multiomics, multimodal omics]
tags: [single-cell, methods, multiomics, multi-omics]
created: 2026-05-07
updated: 2026-08-10
---

# Single-cell multi-omics

> Methods that measure two or more molecular modalities (DNA sequence, RNA, chromatin accessibility, surface protein, methylation, …) in the same single cell, enabling joint analysis that uncoupled single-modality assays cannot.

Single-cell multi-omics is the maturing axis of single-cell biology: most modality *pairs* (and some triples) are now technically feasible, and computational integration has become the dominant bottleneck ([[10-Summaries/baysoy-2023-multiomics-landscape]], [[10-Summaries/vandereyken-2023-scmultiomics-review]]). The recurring tension is **breadth vs depth**: droplet platforms scale to 10⁵+ cells but profile each modality coarsely; single-molecule and plate-based platforms profile deeply but at much lower cell number ([[10-Summaries/swanson-2025-daf-seq]], [[10-Summaries/izzo-2024-got-cha]]). The wiki's current sources span both ends of that spectrum.

## Organizing axes

Two axes organize the method landscape ([[10-Summaries/baysoy-2023-multiomics-landscape]], [[10-Summaries/vandereyken-2023-scmultiomics-review]]):

**1. By modality pair:**
- scRNA + scATAC (10x Multiome, SHARE-seq) ([[10-Summaries/ma-2020-share-seq]]).
- scRNA + surface protein (CITE-seq, REAP-seq) — see [[cite-seq]] ([[10-Summaries/baysoy-2023-multiomics-landscape]]).
- scDNA + scRNA (G&T-seq — see [[gt-seq]], DR-seq, SIDR-seq, DNTR-seq) ([[10-Summaries/macaulay-2015-gt-seq]], [[10-Summaries/dey-2015-dr-seq]]).
- scRNA + methylome (scM&T-seq, snmCT-seq) ([[10-Summaries/vandereyken-2023-scmultiomics-review]]).
- CRISPR-perturbed scRNA (Perturb-seq, CROP-seq) ([[10-Summaries/bi-2024-multiomics-review]]).
- scDNA + scRNA + protein (DOGMA-seq variants) — see [[dogma-seq]] ([[10-Summaries/izzo-2024-got-cha]]).
- scDNA + scATAC + RNA + protein (GoT–ChA + DOGMA via imputation) ([[10-Summaries/izzo-2024-got-cha]]).

**2. By when modalities are uncoupled:**
- Before library prep — physical separation (G&T-seq, SIDR-seq) ([[10-Summaries/macaulay-2015-gt-seq]]).
- During library prep — joint barcoding ([[10-Summaries/vandereyken-2023-scmultiomics-review]]).
- After library prep — diagonal computational integration ([[10-Summaries/wang-2023-multimodal-review]]).

## Why it matters

- Lets the same cell answer multiple questions at once: "what is this cell's genotype, and what does it express?" ([[10-Summaries/nam-2019-got]]).
- Provides the **phenotypic association** capability of the [[scdna-capabilities-framework]] (synthesis).
- Cell-type atlases (Human Cell Atlas) and disease atlases are increasingly multi-omic by default ([[10-Summaries/baysoy-2023-multiomics-landscape]]).

## Core concepts

- [[30-Concepts/got]] — single-cell genotype + transcriptome on droplet 10x scRNA-seq.
- [[30-Concepts/got-cha]] — single-cell genotype + chromatin accessibility on droplet 10x scATAC-seq, via gDNA capture.
- [[30-Concepts/dd-seq]] — single-cell DNA–protein/TF binding via nanobody-deaminase footprinting; composes with GoT–ChA (D&D-GoT-ChA) for genotype + TF binding.
- [[30-Concepts/resolveome]] — PTA genome-wide genotype + full transcriptome in the same cell.
- [[30-Concepts/circularization-got]] — extension of GoT for distal mutation loci.
- [[30-Concepts/daf-seq]] — single-cell, single-molecule chromatin + DNA sequence at near-nucleotide resolution via deaminase footprinting.
- [[30-Concepts/fiber-seq]] — bulk single-molecule chromatin via methyltransferase stenciling; methodological ancestor of DAF-seq.
- [[30-Concepts/single-molecule-footprinting]] — the broader method class.
- [[30-Concepts/dogma-seq]] — chromatin + RNA + protein trimodal platform; integrated with GoT–ChA via imputation in [[10-Summaries/izzo-2024-got-cha]].
- [[30-Concepts/cite-seq]] — scRNA + surface protein via antibody-derived tags.
- [[30-Concepts/gt-seq]] — G&T-seq, physical-separation scDNA + scRNA (1st joint DNA+RNA assay).
- [[30-Concepts/dr-seq]] — DR-seq, one-pot quasilinear scDNA + scRNA alternative to G&T-seq.
- [[30-Concepts/defnd-seq]] — DEFND-seq, scalable droplet whole-genome + RNA via nucleosome depletion on stock 10x Multiome.
- [[30-Concepts/sdr-seq]] — SDR-seq, targeted droplet DNA + RNA on Tapestri with low allelic dropout and per-cell zygosity.
- [[30-Concepts/sci-car]] — sci-CAR, combinatorial-indexing scATAC + scRNA at thousands of cells.
- [[30-Concepts/share-seq]] — SHARE-seq, split-pool scATAC + scRNA at tens of thousands of cells; introduces chromatin-potential framework.
- [[30-Concepts/scnmt-seq]] — scNMT-seq, first single-cell triple-omics (methylation + accessibility + RNA).
- [[30-Concepts/sctrio-seq]] — scTrio-seq, alternative triple-omics (CNV + methylation + RNA); closest existing precedent for DNA-anchored mutation + epi + transcriptome.
- [[30-Concepts/igs]] — IGS, in-situ genome sequencing for spatial 3D-DNA at single-cell resolution.
- [[30-Concepts/spatial-multiomics]] — spatially-resolved multi-omic measurements.
- [[30-Concepts/chromatin-accessibility]] — readout layer.
- [[30-Concepts/chromatin-actuation]] — single-molecule refinement of accessibility.
- [[30-Concepts/simple-seq]] — joint 5mC + 5hmC in single cells.
- [[30-Concepts/splicool-seq]] — 5mC + accessibility (GpC) in single cells, high throughput.
- [[30-Concepts/scepi2-seq]] — single-cell histone mark + 5mC.
- [[30-Concepts/6-base-cut-and-tag]] — fragment-level histone mark + 5mC + 5hmC (bulk).
- [[30-Concepts/scchix-seq]] — two histone marks per cell with computational deconvolution.
- [[30-Concepts/scicut-tag]], [[30-Concepts/multi-tag]] — combinatorial-indexing single-cell CUT&Tag, multi-epitope.
- [[30-Concepts/samosa-tag]], [[30-Concepts/smrt-tag]] — long-read multi-modal chromatin.

## Variants and refinements

- **Spatial multi-omics** — preserves tissue context; imaging-based (MERFISH, seqFISH, in situ) vs NGS-based (Visium, Slide-seq, Stereo-seq) ([[10-Summaries/vandereyken-2023-scmultiomics-review]]). See [[30-Concepts/spatial-multiomics]].
- **Multi-omic best practices** — modality-specific QC and integration recommendations documented in [[10-Summaries/heumos-2023-best-practices]].

## Key entities

- [[20-Entities/dan-a-landau]] — leads the GoT → GoT–ChA methods program at the Landau Lab.
- [[20-Entities/franco-izzo]] — first author of GoT–ChA; co-author on the original GoT and on D&D-seq.
- [[20-Entities/jay-a-a-west]] — corresponding author of ResolveOME; BioSkryb / PTA commercialization.
- [[20-Entities/anna-s-nam]] — first author of the original GoT paper.
- [[20-Entities/landau-lab]] — group behind GoT, circularization GoT, and GoT–ChA.
- [[20-Entities/elliott-g-swanson]] — co-first author of DAF-seq.
- [[20-Entities/andrew-b-stergachis]] — senior author of DAF-seq and developer of Fiber-seq.
- [[20-Entities/thierry-voet]] — KU Leuven; G&T-seq co-developer.
- [[20-Entities/rong-fan]] — Yale; spatial multi-omics.
- [[20-Entities/rahul-satija]] — NYGC; Seurat integration toolkit.
- [[20-Entities/fabian-theis]] — Helmholtz Munich; best-practices recommendations.
- [[20-Entities/alexander-van-oudenaarden]] — sortChIC, scChIX-seq, scEpi²-seq.
- [[20-Entities/chengqi-yi]] — SIMPLE-seq joint 5mC+5hmC.
- [[20-Entities/xiaoying-fan]] — SpliCOOL-seq.
- [[20-Entities/shankar-balasubramanian]] — 6-base-CUT&Tag.
- [[20-Entities/steven-henikoff]] — sciCUT&Tag, MulTI-Tag.
- [[20-Entities/vijay-ramani]] — SMRT-Tag, SAMOSA-Tag.

## Sources, by sub-theme

### Foundational joint DNA + RNA assays (one cell)

- [[10-Summaries/macaulay-2015-gt-seq]] — Macaulay 2015: G&T-seq, separation-based scDNA + scRNA; trisomy-11 subclone in HCC38-BL.
- [[10-Summaries/dey-2015-dr-seq]] — Dey 2015: DR-seq, one-pot scDNA + scRNA; CNVs drive expression variability.
- [[10-Summaries/olsen-2025-defnd-seq]] — Olsen/Sims 2025: DEFND-seq, scalable droplet whole-genome + RNA on 10x Multiome; glioblastoma CNV/SNV-to-expression links.
- [[10-Summaries/lindenhofer-2025-sdr-seq]] — Lindenhofer/Steinmetz 2025: SDR-seq, targeted Tapestri DNA + RNA (≤480 loci+genes), ~90% allele recovery; B-cell lymphoma clonal/variant phenotyping.

### Joint chromatin + RNA (accessibility-anchored)

- [[10-Summaries/cao-2018-sci-car]] — Cao 2018: sci-CAR, scATAC + scRNA at thousands of cells.
- [[10-Summaries/ma-2020-share-seq]] — Ma 2020 (NRG perspective): SHARE-seq, chromatin potential framework.

### Triple-omics (methylation + accessibility + RNA, or CNV + methylation + RNA)

- [[10-Summaries/clark-2018-scnmt-seq]] — Clark 2018: scNMT-seq, first triple-omics; methylation-accessibility coupling strengthens along differentiation.
- [[10-Summaries/hou-2016-sctrio-seq]] — Hou 2016: scTrio-seq; CNVs drive expression but not methylation; HCC subpopulation analysis.

### Spatial single-cell DNA

- [[10-Summaries/andrewc-2020-science]] — Payne 2021: IGS (In Situ Genome Sequencing); 3D-resolved single-cell genomes.

### Genotype + transcriptome (droplet)

- [[10-Summaries/nam-2019-got]] — GoT method paper; CALR-mutated MPN.

### Genotype + chromatin (droplet, gDNA capture)

- [[10-Summaries/izzo-2024-got-cha]] — GoT–ChA; JAK2V617F MPN; cell-intrinsic chromatin priming of HSCs.

### Genotype + chromatin (single-molecule, deaminase)

- [[10-Summaries/swanson-2025-daf-seq]] — DAF-seq / scDAF-seq; chromosome-length single-cell single-molecule chromatin maps.

### Genotype + TF binding / DNA–protein interaction

- [[10-Summaries/chi-2026-dd-seq]] — Chi 2026: D&D-seq / D&D-GoT-ChA; nanobody-deaminase TF footprinting, CTCF binding in closed chromatin, IDH2-mutant T cells show disrupted CTCF binding.

### Genotype + transcriptome (genome-wide, PTA)

- [[10-Summaries/marks-2023-resolveome]] — Marks 2023: ResolveOME; PTA whole-genome + full transcriptome same cell; AML quizartinib resistance (FLT3 + AXL) and breast cancer PIK3CA.

### Reviews of the multi-omics landscape

- [[10-Summaries/baysoy-2023-multiomics-landscape]] — Baysoy/Fan/Satija technological landscape.
- [[10-Summaries/vandereyken-2023-scmultiomics-review]] — Vandereyken/Voet methods and applications, including spatial.
- [[10-Summaries/heumos-2023-best-practices]] — Heumos/Theis best-practices analysis recommendations.
- [[10-Summaries/wang-2023-multimodal-review]] — Wang/Jin methods catalog + integration tool taxonomy (matrix factorization vs manifold alignment vs deep generative).
- [[10-Summaries/bi-2024-multiomics-review]] — Bi & Weng methods catalog organized by integration topology (horizontal/vertical/diagonal) and protein-quantification lineage (NGS-based vs mass-spectrometry-based); covers CRISPR-perturbation dual-modal family explicitly.

### Methylation × chromatin / histone-mark single-cell methods

- [[10-Summaries/bai-2024-simple-seq]] (SIMPLE-seq).
- [[10-Summaries/shen-2026-splicool-seq]] (SpliCOOL-seq).
- [[10-Summaries/geisenberger-2025-scepi2-seq]] (scEpi²-seq).
- [[10-Summaries/tavares-2026-6-base-cut-tag]] (6-base-CUT&Tag).
- [[10-Summaries/yeung-2023-scchix-seq]] (scChIX-seq).
- [[10-Summaries/janssens-2023-scicut-tag]] (sciCUT&Tag).

### Long-read multi-modal chromatin

- [[10-Summaries/abdulhay-2020-samosa]] (SAMOSA-Tag).

## Synthesized notes

- [[50-Notes/joint-assays-by-layer-pair]] — joint single-cell assays organized by which layer-pair they bridge (genotype-anchored first), climaxing on Duplex-Multiome; methodological-integration companion to the synthesis-gap note.

## Contested points

- Cost-per-cell scaling: multi-omic methods are substantially more expensive than unimodal assays at equal cell number ([[10-Summaries/baysoy-2023-multiomics-landscape]]).
- Integration accuracy across diagonal (different cells, different modalities) approaches is hard to benchmark ([[10-Summaries/wang-2023-multimodal-review]]).

## Open questions

- Where does scDAF-seq's per-cell ~99% genome coverage / ~10-cell throughput become more useful than GoT–ChA's ~38% genotyping / 10⁵-cell throughput? What experimental questions sit on each side of that line?
- All three current sources use **within-patient WT cells as comparators** (or, for DAF-seq, within-cell haplotypes). Are there single-cell multi-omic questions where this design doesn't apply?
- Imputation-based multi-omic integration (GoT–ChA + DOGMA-seq via mt-variants and surface proteins) works in MPN. How well does it generalize?
- For chromatin: bulk Fiber-seq → single-cell DAF-seq closed a major gap. What's the analogous gap for [[got]]/[[got-cha]] — is there a "single-molecule, per-fiber" extension waiting to be built?

## Linked summaries (lint pass 2026-05-21)

- [[10-Summaries/ma-2020-cell]] — Ma 2020 — SHARE-seq: shared single-cell RNA + chromatin profiling reveals chromatin potential.
- [[10-Summaries/macaulay-2016-gt-seq-protocol]] — Macaulay 2016 — G&T-seq protocol: parallel single-cell genome + transcriptome.
- [[10-Summaries/shen-2026-splicool-seq]] — Shen 2025 — SpliCOOL-seq: scalable scDNA methylation + chromatin via split-pool.

## Additions — 2026-08-10 ingest

Three complementary taxonomies now anchor this topic:

- **By throughput vs depth** — one-cell-at-a-time deep assays vs droplet/combinatorial-indexing scalable assays, with histone modifications, proteome and spatial named as the 2020 gaps ([[10-Summaries/zhu-2020-multimodal-power-of-many]]).
- **By coupling mechanism** — when the analytes are uncoupled: physical separation, preamplification-and-split, seq-split by differential barcoding, or combinatorial indexing. This predicts each method's throughput ceiling, and explains why genome+transcriptome lags epigenome+transcriptome ([[10-Summaries/vandereyken-2023-spatial-multiomics]]).
- **By computational anchor** — horizontal / vertical / diagonal / mosaic ([[10-Summaries/argelaguet-2021-integration-principles]]), with bridge integration removing the gene-activity assumption diagonal methods otherwise require ([[10-Summaries/hao-2024-seurat-v5]]).

Results worth carrying:

- **Dosage compensation breaks CNV→expression inference**: DNTR-seq showed *MYC* and *TCF7L2* largely unaffected by copy number despite strong structural imbalance ([[10-Summaries/vandereyken-2023-spatial-multiomics]]).
- **~16% of *OCT4*-edited human embryo cells carried unintended edits** — LOH beyond the on-target locus plus chromosome-6 segmental changes — detectable only by reading genome and transcriptome in the same cells ([[10-Summaries/vandereyken-2023-spatial-multiomics]]).
- **GpC-methyltransferase accessibility gives higher promoter coverage than ATAC** and distinguishes truly closed from unsampled, because every read reports ([[10-Summaries/vandereyken-2023-spatial-multiomics]]).
- **Protein as the integration currency**: 173 surface antibodies let six separately-measured histone marks be harmonized and interpolated per cell, though not co-measured ([[10-Summaries/zhang-2022-sccut-tag-pro]]).
- Layer-by-layer protocol catalog, including the single-cell proteome methods this wiki otherwise lacks, in [[10-Summaries/lim-2024-single-cell-omics-review]].

## Added 2026-08-10

Integration methods now span three strategies: embedding correction with multi-covariate support and the LISI metric pair ([[10-Summaries/korsunsky-2019-harmony]]), factorization into shared *and* dataset-specific factors so differences stay legible ([[10-Summaries/welch-2019-liger]]), and joint modelling where a co-assayed modality is a prediction target rather than an input ([[10-Summaries/zhang-2022-higashi]]).

Regulatory-network inference from joint accessibility and expression: [[10-Summaries/pliner-2018-cicero]] links elements to genes by co-accessibility; [[10-Summaries/kamimoto-2023-celloracle]] uses the resulting network as a simulation operator for in-silico TF perturbation; [[10-Summaries/bravo-2023-scenicplus]] infers enhancer-driven regulons and reports that only 49% of enhancers regulate their most proximal gene.


## Related

- [[got]], [[got-cha]], [[daf-seq]]
- [[cite-seq]]
- [[gt-seq]]
- [[dogma-seq]]
- [[spatial-multiomics]]
- [[scdna-capabilities-framework]]
- [[50-Notes/joint-assays-by-layer-pair]]
- [[10-Summaries/argelaguet-2021-integration-principles]] · [[10-Summaries/hao-2024-seurat-v5]] · [[10-Summaries/vandereyken-2023-spatial-multiomics]] · [[10-Summaries/lim-2024-single-cell-omics-review]]
