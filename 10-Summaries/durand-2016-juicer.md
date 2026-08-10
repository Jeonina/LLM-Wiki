---
type: summary
title: "Durand et al. 2016 — Juicer: a one-click system for analyzing loop-resolution Hi-C experiments"
source: "[[00-Sources/papers/Juicer Provides a One-Click System for Analyzing Loop-Resolution Hi-C Experiments]]"
source_kind: paper
author: "Neva C. Durand, Muhammad S. Shamim, Ido Machol, Suhas S. P. Rao, Miriam H. Huntley, Eric S. Lander, Erez Lieberman Aiden (corresponding)"
published: 2016-07-27
ingested: 2026-08-10
doi: "10.1016/j.cels.2016.07.002"
journal: "Cell Systems"
tags: [Juicer, Hi-C, HiCCUPS, Arrowhead, loop-calling, contact-domains, computational-tool, pipeline]
entities: []
concepts: ["[[single-cell-hi-c]]", "[[topologically-associating-domain]]", "[[chromatin-compartments]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]"]
---

**Citation:** Durand et al. (2016) — *Juicer provides a one-click system for analyzing loop-resolution Hi-C experiments* — *Cell Systems* 3, 95–98. [DOI](https://doi.org/10.1016/j.cels.2016.07.002)

# Durand 2016 — Juicer

> An end-to-end, hardware-accelerated Hi-C pipeline: reads → deduplicated contact list → multi-resolution normalized contact matrices in the compressed `.hic` format → automatic annotation of loops (HiCCUPS), contact domains (Arrowhead) and aggregate peak signal (APA). Built to make terabase-scale kilobase-resolution Hi-C tractable by non-specialists.

## Key claims

- Existing Hi-C pipelines were not designed for terabase-scale data nor for annotating structural features; Juicer addresses both in one automated run.
- The `.hic` format is the load-bearing engineering decision: 1 TB of raw sequence compresses to an ~80 GB file holding normalized and raw matrices at **18 resolutions**, from 2.5 Mb down to single restriction fragment (~400 bp for a 4-cutter).
- Loop calling via **HiCCUPS** — local-background enrichment over trillions of pixels, GPU-implemented out of necessity — plus FIMO-based identification of the CTCF motif anchoring each loop.
- Contact domains via **Arrowhead**, a dynamic-programming call on the transformed normalized matrix Aᵢ,ᵢ₊d = (M\*ᵢ,ᵢ₋d − M\*ᵢ,ᵢ₊d)/(M\*ᵢ,ᵢ₋d + M\*ᵢ,ᵢ₊d).
- Loop-anchor calls are experimentally validated: CRISPR disruption of seven HiCCUPS-identified CTCF motifs disrupted the corresponding loops in every case.

## Methods / evidence

Benchmarked on 1.5 billion paired-end reads across four cluster configurations (AWS g2.8xlarge, Broad UGE, Rice PowerOmics, PowerOmics+FPGA). Alignment dominates cost — 8,745 core-hours on AWS vs **1.5 core-hours** with an Edico DRAGEN FPGA, collapsing total runtime from ~8,900 to ~609 core-hours. Quality statistics are computed before deep sequencing so a failed library can be caught early. Normalization offers both the original scheme and matrix balancing.

## Surprising or load-bearing bits

- The CRISPR validation of loop anchors is the reason HiCCUPS calls carry more weight than typical peak calls — 7/7 is a small n but a direct causal test, rare for a pipeline paper.
- The FPGA line item (5,800× on alignment) is a reminder that Hi-C's compute profile is alignment-bound, not algorithm-bound — relevant when planning scaling for single-cell Hi-C where cell count multiplies the alignment burden.
- Juicer is **bulk-first**. For [[single-cell-hi-c]] the corpus's working stack is [[abdennur-2020-cooler|Cooler]] + [[zhang-2022-higashi|Higashi]]/[[zhou-2019-schicluster|scHiCluster]]; Juicer contributes the *feature definitions* (loops, contact domains) that single-cell methods then try to recover from sparse data.

## Concepts touched

- [[topologically-associating-domain]] — Arrowhead "contact domains" are the operational definition used in much of the 3D-genome literature; note this is a different call from the Dixon insulation-score TAD.
- [[chromatin-compartments]] — multi-resolution matrices are the substrate for compartment calling.
- [[single-cell-hi-c]] — Juicer's outputs are the bulk reference against which single-cell contact maps are judged.

## Connections to other sources

- Downstream of [[lieberman-aiden-2009-hic|Lieberman-Aiden 2009 (Hi-C)]] (the assay) and Rao 2014 (the kilobase-resolution maps the pipeline was built to process).
- Complementary to [[abdennur-2020-cooler|Abdennur & Mirny 2020 (Cooler)]] — `.hic` vs `.cool` is the field's format split; Cooler is the one that scales to per-cell matrices.
- Visualization companion Juicebox; [[kerpedjiev-2018-higlass|HiGlass]] is the alternative viewer used with the Cooler ecosystem.
- [[servant-2015-hicpro|Servant 2015 (HiC-Pro)]] is the other major bulk pipeline; HiC-Pro is more modular, Juicer more automated.

## Open questions

- HiCCUPS requires read depth that no single cell provides. Which loop-level features survive at single-cell coverage, and at what pooling depth do Juicer-defined loops become recoverable? Not addressed here, and only partly by Higashi.

## Related

- [[abdennur-2020-cooler|Abdennur & Mirny 2020 (Cooler)]] · [[servant-2015-hicpro|Servant 2015 (HiC-Pro)]] · [[topologically-associating-domain]] · [[3d-genome]]
