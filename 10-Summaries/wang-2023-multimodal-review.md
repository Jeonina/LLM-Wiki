---
type: summary
title: "Wang, Wu, Hong & Jin 2023 — Progress in single-cell multimodal sequencing and multi-omics data integration"
source: "[[00-Sources/papers/Progress in single-cell multimodal sequencing and multi-omics data integration]]"
source_kind: paper
author: Xuefei Wang, Xinchao Wu, Ni Hong, Wenfei Jin (corresponding)
published: 2023-07-15
ingested: 2026-05-19
doi: "10.1007/s12551-023-01092-3"
journal: "Biophysical Reviews"
tags: [review, single-cell, multiomics, integration, scNMT, CITE-seq, SHARE-seq, MOFA, GLUE]
entities: ["[[20-Entities/wenfei-jin]]", "[[20-Entities/rahul-satija]]"]
concepts: ["[[30-Concepts/single-cell-multiomics]]", "[[30-Concepts/scnmt-seq]]", "[[30-Concepts/sctrio-seq]]", "[[30-Concepts/cite-seq]]", "[[30-Concepts/dogma-seq]]"]
topics: ["[[40-Topics/single-cell-multiomics]]"]
---

**Citation:** Wang et al. (2023) — *Progress in single-cell multimodal sequencing and multi-omics data integration* — *Biophysical Reviews*. [DOI](https://doi.org/10.1007/s12551-023-01092-3)

# Wang 2023 — multimodal review

> A practical inventory of single-cell multimodal sequencing methods organized by which modality pairs they read (genome+RNA, epigenome+RNA, 3D+epigenome, RNA+protein, spatial+omics), paired with a tour of computational integration tools (matrix factorization, manifold alignment, deep learning). Comprehensive but largely encyclopedic — value is in the table of methods + integration tool taxonomy, not novel synthesis.

## Key claims

- **Transcriptome is the linkage center.** Across all multimodal platforms, RNA is the most common pairing partner — every other modality (genome, epigenome, proteome, spatial) is most often joint-profiled *with* RNA. This reflects the central dogma framing and the maturity of scRNA-seq protocols.
- **Joint genome+RNA at single-cell resolution is hard.** Reviewed methods: DR-seq (one-pot, no separation), G&T-seq (oligo-dT separation), SIDR-seq (total RNA), TARGET-seq (targeted somatic mutations). All are low-throughput; manual cell pickup limits scale; high WGS cost limits applications.
- **Joint epigenome+RNA is the largest category.** Methylation+RNA: scM&T-seq, scMT-seq. Chromatin accessibility+RNA: sci-CAR, scCAT-seq, SNARE-seq/SNARE-seq2, Paired-seq, SHARE-seq, ISSAAC-seq, EpiDamID. Triple-omics: scTrio-seq (CNV+mC+RNA), scNMT-seq (accessibility+mC+RNA), single-cell COOL-seq (chromatin state+mC+CNVs+ploidy), scNOMeRe-seq, scChaRM-seq.
- **3D+epigenome single-cell methods exist but are limited.** Methyl-HiC, sn-m3C-seq combine Hi-C with WGBS. No reviewed method reads 3D + accessibility + RNA simultaneously at scale.
- **Protein+RNA via DNA-barcoded antibodies is mature.** CITE-seq and REAP-seq target surface proteins; ECCITE-seq adds V(D)J + CRISPR; Perturb-CITE-seq adds perturbations. For intracellular/intranuclear proteins: RAID, QuRIE-seq, INs-seq, inCITE-seq.
- **Multi-modality (4+ layers) is emerging.** Tapestri (genome + surface protein), TEA-seq (surface protein + accessibility + RNA), NEAT-seq (intranuclear protein + accessibility + RNA), DOGMA-seq / ASAP-seq (chromatin + RNA + protein + mtDNA), PHAGE-ATAC (surface/intra protein + accessibility + mtDNA).
- **Spatial multi-omics is the newest frontier.** DBiT-seq, SM-Omics (spatial transcriptome+protein), spatial CITE-seq, CosMx SMI. Most spatial methods still require paired scRNA-seq for noise reduction.
- **Integration falls into three computational families:**
  - **Matrix factorization**: MOFA, MOFA+, LIGER — extract latent factors per modality; struggle with technical noise and high dimensionality
  - **Manifold alignment / anchoring**: CCA, MNN, WNN (all in Seurat), Tangram, Cell2location
  - **Deep generative models**: totalVI, sciPENN, scMVP, MultiVI, Cobolt, scJoint, GLUE, Symphony — better for atlas-scale; can integrate paired and unpaired data

## Methods / evidence

This is a review paper (no new data). The methods catalog is fairly complete through ~early 2023 but predates: Duplex-Multiome (2025), GoT-ChA (2024), 6-base-CUT&Tag (2024), SIMPLE-seq (2024), DAF-seq single-cell extensions (2025). For current state, supplement with [[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]] (NRMCB) and [[10-Summaries/katy-2023-naturereviewsgenetics|Vandereyken 2023]] (NRG).

## Surprising or load-bearing bits

- **The information-extraction angle.** The review's final section notes that single-cell mono-omics data often contains *additional* hidden modalities — scRNA-seq can yield CNV calls, allele-specific expression, somatic SNVs; scDNase-seq can yield TF-binding SNV effects. This is a cheaper alternative to true multimodal experiments and is the conceptual foundation for tools like [[10-Summaries/eran-2025-neuron|Mukamel 2025]] (CNV from snmC-seq2) and [[10-Summaries/dou-2020-monovar|Monopogen]] (SNV from scATAC/scRNA).
- **The 3-modality ceiling.** Authors acknowledge that >3 modalities from the same cell is fundamentally limited by molecule loss; future progress will come more from computational integration of paired-with-different-thirds datasets than from cramming more modalities into one assay. This framing is conservative — DOGMA-seq and PHAGE-ATAC already read 4 modalities; Duplex-Multiome reads 3+ with genotype.
- **Methylation+CNV is positively correlated; methylation+expression is negatively correlated; CNV+expression is positively correlated.** Per scTrio-seq findings recapped here: CNV drives expression but does *not* drive local methylation. This decoupling is what makes [[50-Notes/regulatory-layers-overview|regulatory layers]] genuinely orthogonal axes.
- **Paired vs unpaired integration is a different problem.** Paired-data tools (CCA, MNN, WNN) align cells across modalities measured *together*. Unpaired-data tools (GLUE, MOFA+, MultiVI, Cobolt) try to integrate modalities measured *separately on different cells from the same tissue*. The latter is harder and is where deep generative models dominate.

## Entities mentioned

- [[20-Entities/wenfei-jin]] — corresponding author; SUSTech; developed scDNase-seq, scNOMeRe-seq
- [[20-Entities/rahul-satija]] — NYGC; Seurat (CCA, MNN, WNN)
- [[20-Entities/dan-a-landau]] — implicit (TARGET-seq referenced; Landau lab develops GoT family)
- [[20-Entities/fabian-theis]] — implicit (Theis lab develops MultiVI, scVI ecosystem)
- Jay Shendure / Cole Trapnell — sci-CAR, Paired-seq, fetal cell atlas
- Howard Chang — SHARE-seq

## Concepts touched

- [[30-Concepts/single-cell-multiomics]] — comprehensive catalog
- [[30-Concepts/scnmt-seq]], [[30-Concepts/sctrio-seq]] — covered with their key findings
- [[30-Concepts/cite-seq]] — CITE-seq family
- [[30-Concepts/dogma-seq]] — DOGMA-seq as 4-modality platform
- [[30-Concepts/share-seq]] — SHARE-seq chromatin potential
- [[30-Concepts/got]] — TARGET-seq mentioned as cousin (Landau lab)
- [[30-Concepts/spatial-multiomics]] — DBiT-seq, spatial CITE-seq
- [[30-Concepts/anndata]], [[30-Concepts/episcanpy]] — implicit in deep-learning toolchain
- [[30-Concepts/latent-dirichlet-allocation]] — implicit in matrix factorization family

## Connections to other sources

- **Echoes** [[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]] and [[10-Summaries/katy-2023-naturereviewsgenetics|Vandereyken 2023]] — three near-contemporaneous multi-omics reviews; this one is more methods-encyclopedic, Baysoy is more applications-focused, Vandereyken includes spatial in depth.
- **Echoes** [[10-Summaries/lukas-2023-naturereviewsgenetics|Heumos 2023]] best-practices analysis — Heumos focuses on the *analysis* side; Wang focuses on the *measurement+integration* side.
- **Predates** the Duplex-Multiome / mosaicism+epigenome convergence described in [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]].
- **Supports** [[50-Notes/regulatory-layers-overview]] — the methods-by-layer table in that note draws on the same catalog this review compiles.

## Open questions

- The review's "3-modality ceiling" prediction is already being challenged (DOGMA-seq, Duplex-Multiome, PHAGE-ATAC). Is the actual limit higher? What's the noise floor as modalities multiply?
- How well do unpaired-data integration tools (GLUE, MOFA+) actually scale to atlas-level when the modalities come from very different protocols (e.g., scNMT-seq methylation + 10x Multiome accessibility)?
- The review barely discusses single-molecule (Fiber-seq, DAF-seq) approaches. As of 2026 these are essential for accessibility+sequence at single-fiber resolution; an updated review would need a dedicated section.
- Spatial multi-omics is "the frontier" in 2023; by 2026 this should be commodity. What's the bottleneck — sensitivity, throughput, or integration with non-spatial single-cell data?
