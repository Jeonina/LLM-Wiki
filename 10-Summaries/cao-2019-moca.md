---
type: summary
title: "Cao et al. 2019 — The single-cell transcriptional landscape of mammalian organogenesis (MOCA, sci-RNA-seq3, Monocle 3)"
source: "[[00-Sources/papers/The single-cell transcriptional landscape of mammalian organogenesis]]"
source_kind: paper
author: "Junyue Cao, Malte Spielmann, Xiaojie Qiu, Xingfan Huang, Daniel M. Ibrahim, Andrew J. Hill, Fan Zhang, Stefan Mundlos, Lena Christiansen, Frank J. Steemers, Cole Trapnell, Jay Shendure (corresponding)"
published: 2019-02-20
ingested: 2026-08-10
doi: "10.1038/s41586-019-0969-x"
journal: "Nature"
tags: [MOCA, sci-RNA-seq3, Monocle3, combinatorial-indexing, organogenesis, atlas, trajectory, 2-million-cells]
entities: ["[[jay-shendure]]", "[[cole-trapnell]]"]
concepts: ["[[combinatorial-indexing]]", "[[trajectory-inference]]", "[[cell-type-annotation]]", "[[clustering-algorithms]]", "[[doublet-detection]]", "[[umi-molecular-barcoding]]"]
topics: ["[[single-cell-lineage-tracing]]", "[[computational-methods]]", "[[single-cell-multiomics]]"]
---

**Citation:** Cao et al. (2019) — *The single-cell transcriptional landscape of mammalian organogenesis* — *Nature* 566, 496–502. [DOI](https://doi.org/10.1038/s41586-019-0969-x)

# Cao 2019 — MOCA

> **Two million cells from 61 mouse embryos in a single experiment**, spanning E9.5–E13.5, the four days in which nearly every major organ system forms. sci-RNA-seq3 makes the scale possible at under **$0.01 per cell**; Monocle 3 turns it into 38 major cell types, 655 subtypes and 56 trajectories.

## Key claims

- **sci-RNA-seq3**, the third-generation combinatorial indexing protocol, arrived from screening **>1,000 experimental conditions**. Four changes matter: nuclei extracted directly from fresh tissue without enzymatic treatment then fixed and stored; the third indexing level switched from **Tn5 tagmentation to hairpin ligation**; individual enzymatic reactions optimized; and FACS replaced by dilution with added sonication and filtration to break aggregates. One researcher, one week, no automation.
- **Scale and design**: 61 C57BL/6 embryos at five stages, nuclei from each deposited into individual wells of four 96-well plates so the **first index identifies the embryo of origin**. One NovaSeq run, 11 billion reads, **2,058,652 embryo cells** recovered at ≥200 UMIs, plus 13,359 spiked HEK-293T/NIH-3T3 control cells.
- **Quality profile, stated plainly.** 3% species collisions. Median 671 UMIs (519 genes) per cell at ~5,000 raw reads and 46% duplicates; 3.7× deeper sequencing of a subset nearly doubled complexity to 1,142 UMIs at 87% duplicates. **59% of UMIs map to introns, 25% to exons** — nuclear RNA, so the profiles primarily reflect **nascent transcription**, temporally offset from but predictive of the cellular transcriptome. Scrublet detected 4.3% likely doublets, implying ~10.3% including within-cluster doublets.
- **A stated limitation**: only ~7% of input cells were ultimately profiled, lost mostly at the aggregate-removal filtration steps.
- **Shotgun cellular coverage** framing: 0.8× at E9.5 (200,000 cells per embryo) declining to 0.03× at E13.5 (13 million cells per embryo) — i.e. 3–80% of an individual embryo's cellular content.
- **38 major cell types** from Louvain clustering of 40 clusters (two erythroid clusters merged, one 52%-doublet cluster discarded), then **655 subclusters** by iterative re-clustering, of which 13% were annotated as likely artefacts (>10% predicted doublets), leaving **572 subtypes**. Cell types range from 1,000 (neutrophils) to 144,648 cells (connective tissue progenitors); subtypes from 51 to 65,894.
- **Marker discovery at scale**: 17,789 of 26,183 genes (68%) differentially expressed across major cell types at 5% FDR; **2,863 cell-type-specific markers** (>2-fold between first- and second-ranked type), a median of 20 markers per subtype. Most were not previously known as markers — e.g. *Tox2*, *Stxbp6*, *Schip1*, *Frmd4b* as notochord markers alongside the known *Shh*, with *Tox2* confirmed by whole-mount *in situ* hybridization at E10.5.
- **Dynamics visible only across time**: primitive erythroid cells (yolk-sac origin, *Hbb-bh1*) are progressively replaced by the definitive lineage (fetal liver, *Hbb-bs*) and are gone by E13.5. Pseudobulk pseudotime ordering of the 61 embryos shows two prominent gaps (E9.5–E10.5 and E11.5–E12.5).
- Cross-atlas matching linked 96 cell types of the adult-focused Mouse Cell Atlas to 58 MOCA subtypes and 48 brain-atlas types to 68 MOCA subtypes.

## Methods / evidence

Species-mixing controls for collision rate, Scrublet for doublets, replicate embryos per stage checked for concordant distribution, orthogonal WISH validation of a novel marker, iterative subclustering with an explicit artefact-annotation rule, and downsampling analysis showing **sensitivity to detect subtypes depended on the number of cells profiled** — the paper's own evidence that the scale was necessary rather than decorative.

## Surprising or load-bearing bits

- **Sensitivity to cell types scales with cell number, and the paper demonstrates it rather than asserting it.** 56 trajectories and hundreds of subtypes are "detected only because of the depth of cellular coverage." That is the quantitative case for atlas-scale experiments, and the same argument [[zahn-2017-dlp|DLP]] makes for subclone detection in cancer.
- **Nuclear RNA is mostly intronic, so this atlas measures nascent transcription.** 59% intronic is not a defect — it is what makes RNA velocity possible — but it means MOCA expression is not directly comparable to whole-cell scRNA-seq, a caveat that travels with every reuse of the dataset.
- **The 7% recovery rate is unusually candid**, and it is the hidden cost of aggregate filtration in combinatorial indexing. Throughput here comes from cheap barcoding, not from efficient capture.
- **Combinatorial indexing means the first index is the sample**, so embryo of origin is recoverable per cell with no separate multiplexing reagent — the same architecture as [[ramani-2017-scihi-c|sciHi-C]] and [[cusanovich-2015-sciatac|sciATAC]], applied to a developmental time course.
- **13% of subtypes were called artefacts on doublet grounds.** Publishing that number, and the rule used, is the kind of disclosure most atlas papers omit; subtype counts from atlases without such a rule should be read as upper bounds.
- The **two pseudotime gaps** (E9.5–E10.5 and E11.5–E12.5) suggest developmental change is not uniform in time — but they are equally consistent with uneven sampling, and the paper does not separate the two.

## Entities mentioned

- [[jay-shendure]] — corresponding author; the combinatorial-indexing program running through [[ramani-2017-scihi-c]] and [[cusanovich-2015-sciatac]].
- [[cole-trapnell]] — co-corresponding; Monocle lineage.

## Concepts touched

- [[combinatorial-indexing]] — third-generation implementation with ligation-based third-level indexing.
- [[trajectory-inference]] — Monocle 3's 56 trajectories on two million cells.
- [[doublet-detection]] — Scrublet plus an explicit subtype-level artefact rule.

## Connections to other sources

- Shared indexing architecture: [[ramani-2017-scihi-c]], [[cusanovich-2015-sciatac]].
- Trajectory alternatives: [[wolf-2019-paga]]; integration at this scale: [[korsunsky-2019-harmony]], [[hao-2024-seurat-v5]].
- Regulatory-network inference built on such atlases: [[pliner-2018-cicero]], [[kamimoto-2023-celloracle]], [[bravo-2023-scenicplus]].
- Brain atlas comparison: [[lake-2018-brain-snrna-scths]].

## Open questions

- **Whether the pseudotime gaps are biology or sampling** is not resolved.
- Subtype boundaries are operational — the paper says so explicitly, defining "cell type" as the 38 major clusters and "subtype" as the 655 subclusters *specific to this manuscript*. There is no external criterion, so subtype counts are not directly comparable across atlases.
- Mesenchymal and connective-tissue clusters were the hardest to annotate for lack of known markers, so the largest cell populations in the atlas are the least confidently identified.

## Related

- [[combinatorial-indexing]] · [[wolf-2019-paga]] · [[trajectory-inference]] · [[single-cell-lineage-tracing]]
