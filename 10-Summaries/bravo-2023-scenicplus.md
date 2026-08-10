---
type: summary
title: "Bravo González-Blas et al. 2023 — SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks"
source: "[[00-Sources/papers/SCENIC+_ single-cell multiomic inference of enhancers and gene regulatory networks]]"
source_kind: paper
author: "Carmen Bravo González-Blas, Seppe De Winter, Gert Hulselmans, Nikolai Hecker, Irina Matetovici, Valerie Christiaens, Suresh Poovathingal, Jasper Wouters, Sara Aibar, Stein Aerts (corresponding)"
published: 2023-07-13
ingested: 2026-08-10
doi: "10.1038/s41592-023-01938-4"
journal: "Nature Methods"
tags: [SCENIC+, eGRN, eRegulon, motif-collection, cisTarget, pycisTopic, GRNBoost2, ENCODE-benchmark, cross-species]
entities: ["[[stein-aerts]]"]
concepts: ["[[gene-regulatory-network]]", "[[transcription-factor-motif]]", "[[enhancer-states]]", "[[cis-regulatory-element]]", "[[scatac-seq]]", "[[de-novo-motif-discovery]]", "[[multimodal-integration-methods]]"]
topics: ["[[computational-methods]]", "[[single-cell-multiomics]]", "[[chromatin-architecture]]"]
---

**Citation:** Bravo González-Blas et al. (2023) — *SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks* — *Nature Methods* 20, 1355–1367. [DOI](https://doi.org/10.1038/s41592-023-01938-4)

# Bravo 2023 — SCENIC+

> The original SCENIC inferred regulons from coexpression plus motif enrichment, but could not say **which** *cis*-regulatory element a TF acts through, and used only a small fraction of a gene's regulatory space. SCENIC+ adds chromatin accessibility so that the unit of inference becomes the **eRegulon**: a transcription factor together with its target *enhancers* and, through them, its target genes.

## Key claims

- **Three-step workflow**: identify candidate enhancers → find enriched TF-binding motifs in them → link TFs to enhancers and to target genes. Output is a set of eRegulons forming an enhancer-driven GRN (eGRN).
- **Candidate enhancers from two sources.** scATAC-seq is preprocessed with **pycisTopic** (a faster Python reimplementation of cisTopic), and both differentially accessible regions and **topics** — sets of co-accessible regions — serve as candidates. **Topics are more enriched for functional enhancers than DARs.**
- **The motif collection is the paper's infrastructural contribution**: **32,765 unique motifs from 29 collections**, spanning 1,553 human, 1,357 mouse and 467 fly TFs — the largest at the time. Motifs are clustered by similarity, and **scoring regions with all motifs in a cluster gives significantly higher precision and recall than using one "archetype" motif per cluster**.
- **pycisTarget** implements two enrichment algorithms: the ranking-and-recovery cisTarget algorithm, and **DEM** (differential enrichment of motifs), a Wilcoxon rank-sum test that can detect differential motifs among region sets with similar motif content. Both outperform HOMER.
- **Linking** uses **GRNBoost2** to quantify the importance of TFs and enhancer candidates for target genes, with the direction of regulation (activating or repressing) from linear correlation, then a second enrichment analysis to recover the best TF per motif set.
- **PBMC illustration** (9,409 multiome cells): eRegulon enrichment scores alone separate the main cell states. 53 activator eRegulons targeting 23,470 regions and 6,142 genes. **89% of genes have 1–10 predicted enhancers; 49% of enhancers are predicted to regulate the most proximal gene** — so roughly half do not. Known master regulators recovered for B cells (EBF1, PAX5, POU2F2/POU2AF1), T cells (TCF7, GATA3, BCL11B), NK cells (EOMES, RUNX3, TBX21), dendritic cells (SPIB, IRF8) and monocytes (SPI1, CEBPA), with predicted target enhancers overlapping the corresponding ChIP-seq.
- **Cooperativity is inferable**: the top cell-type-specific TFs largely co-bind shared enhancers, and this is not seen for TFs specific to different cell types — an emergent property of the eRegulon representation rather than an added analysis.
- **ENCODE benchmark** on simulated multiome data from eight deeply profiled cell lines, against CellOracle, Pando, FigR, GRaNIE and SCENIC as baseline. SCENIC+ identified 178 TFs (GRaNIE 39, FigR 71, SCENIC 108, Pando 157, CellOracle 235), averaging **471 target genes and 1,152 target regions per eRegulon**.
- Applied across human PBMCs, ENCODE lines, melanoma cell states, *Drosophila* retinal development, and conserved TF/enhancer/GRN comparison between human and mouse cerebral cortex; also used for trajectory-resolved regulatory dynamics and TF-perturbation effects on cell state.
- **Cost is stated honestly**: 1 hour and 21 GB for the smallest dataset, **44 hours and 461 GB for the largest**.

## Methods / evidence

Benchmarking against five contemporary eGRN methods on ENCODE cell lines with independent ChIP-seq validation of predicted TF target regions, plus ablation of the method's own design choices (topics versus DARs; motif clusters versus archetypes; cisTarget and DEM versus HOMER) so each component's contribution is separately demonstrated. Cross-species application (human, mouse, fly) tests generality rather than tuning to one system.

## Surprising or load-bearing bits

- **49% of enhancers regulate their most proximal gene — meaning about half do not.** That single number is the quantitative case for enhancer-driven GRN inference over promoter-proximal assignment, and it is a caution for every analysis that assigns a peak to its nearest gene, including [[mclean-2010-great|GREAT]]-style annotation.
- **Motif clusters beat archetype motifs.** A single representative motif per family loses real binding preferences among paralogous TFs; scoring with the whole cluster recovers them. This is the practical reason the 32,765-motif collection exists, and it is a general lesson for motif analysis — collapsing a family to its consensus is lossy.
- **Topics outperform differentially accessible regions as enhancer candidates.** DARs are defined by contrast between predefined groups; topics are defined by co-accessibility structure across the data. The latter finds regulatory modules that do not align with the cluster labels you happened to choose — the same insight as [[pliner-2018-cicero|Cicero]]'s co-accessibility, applied at the topic level.
- **TF cooperativity falls out of the representation.** Because an eRegulon carries its target *regions*, overlap between two TFs' regions is directly computable; a gene-level regulon could never show co-binding. Representing the intermediate layer is what makes the mechanistic question askable.
- **The benchmark does not simply crown SCENIC+.** CellOracle identifies *more* TFs (235 vs 178) — more TFs is not obviously better, and the paper reports the comparison rather than framing it as a win. TF count and target-set size are different axes from precision.
- **461 GB is a real barrier.** This is not a tool that runs on a laptop at scale, which stands in direct contrast to [[korsunsky-2019-harmony|Harmony]]'s 7 GB for 500,000 cells. Method choice in practice is often decided by compute availability.

## Entities mentioned

- [[stein-aerts]] — corresponding author; the SCENIC/cisTarget lineage.

## Concepts touched

- [[gene-regulatory-network]] — the eRegulon as TF + enhancers + genes, superseding gene-only regulons.
- [[de-novo-motif-discovery]] — motif clustering and the cisTarget/DEM pair.
- [[enhancer-states]] — topics as enhancer candidates.

## Connections to other sources

- Benchmarked against [[kamimoto-2023-celloracle]] and against SCENIC as baseline; shares the enhancer-identification problem with [[pliner-2018-cicero]].
- Outperforms [[heinz-2010-homer]] on motif enrichment; complements [[mclean-2010-great]] region-to-gene assignment.
- Assay inputs: [[cusanovich-2015-sciatac]], [[hao-2024-seurat-v5]] (multiome handling); single-cell TF-binding alternatives it cites as unscalable: [[wu-2021-sccut-tag]], [[rooijers-2019-scdamt-seq]].
- Trajectory context: [[wolf-2019-paga]], [[cao-2019-moca]].

## Open questions

- **Predicted enhancer–gene links are validated against ChIP-seq for TF binding, not against functional perturbation of the enhancer.** Binding is not regulation; the fraction of predicted links that are functionally required is unaddressed.
- Motif-based TF assignment cannot distinguish family members sharing a motif; clustering improves recall but the identity of the actual bound paralogue remains inferred from expression.
- The 44-hour/461 GB ceiling constrains what datasets this can be run on, and no downsampling guidance is given for when it cannot.

## Related

- [[gene-regulatory-network]] · [[kamimoto-2023-celloracle]] · [[pliner-2018-cicero]] · [[single-cell-multiomics]]
