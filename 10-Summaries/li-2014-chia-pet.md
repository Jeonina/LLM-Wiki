---
type: summary
title: "Li et al. 2014 — Chromatin Interaction Analysis with Paired-End Tag (ChIA-PET) sequencing technology and application"
source: "[[00-Sources/papers/Chromatin Interaction Analysis with Paired-End Tag (ChIA-PET) sequencing technology and application]]"
source_kind: paper
author: "Guoliang Li, Liuyang Cai, Huidan Chang, Ping Hong, Qiangwei Zhou, Ekaterina V. Kulakova, Nikolay A. Kolchanov, Yijun Ruan"
published: 2014-12-19
ingested: 2026-08-13
doi: "10.1186/1471-2164-15-S12-S11"
journal: "BMC Genomics 15(Suppl 12):S11"
tags: [ChIA-PET, 3C-derivatives, enhancer-promoter, chromatin-interaction-network, RNAPII, CTCF, review, protein-anchored]
entities: ["[[yijun-ruan]]"]
concepts: ["[[chia-pet]]", "[[chip-seq]]", "[[chromatin-loop]]", "[[cis-regulatory-element]]", "[[enhancer-states]]", "[[gene-regulatory-network]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]"]
---

**Citation:** Li et al. (2014) — *Chromatin Interaction Analysis with Paired-End Tag (ChIA-PET) sequencing technology and application* — *BMC Genomics* 15(Suppl 12), S11. [DOI](https://doi.org/10.1186/1471-2164-15-S12-S11)

# Li 2014 — ChIA-PET

> A protocol-and-applications review of the **protein-anchored** branch of the 3C family. The argument for ChIA-PET over Hi-C is a resolution-versus-scope trade: ChIA-PET restricts attention to interactions involving one protein of interest, and in exchange gets **higher resolution and a functional handle** — you know which factor the loop is about. Its lasting empirical contribution is the demonstration that **over 40% of enhancers do not regulate their nearest promoter**.

## Key claims

- **ChIP-based methods and 3C-based methods each have a blind spot that ChIA-PET closes.** ChIP-chip/ChIP-PET/ChIP-seq locate transcription-factor binding but cannot name the target gene of a distal site, nor say whether that site is functional. 3C is low-throughput; 4C and 5C cannot map interacting regions at high resolution genome-wide. ChIA-PET is unbiased, genome-wide, high-throughput, and de novo.
- **Versus Hi-C**, ChIA-PET's advantage is stated as higher resolution *associated with a protein of interest*, plus a more reliable route to both TF binding sites and interactions in one assay.
- **Three interaction classes, and the nearest-gene result.** ChIA-PET analyses identified enhancer–promoter, enhancer–enhancer, and promoter–promoter interactions, and demonstrated that **>40% of enhancers do not regulate their nearest promoters** — the empirical foundation for why enhancer-to-gene assignment needs 3D data rather than proximity heuristics.
- **Chromatin interaction networks are scale-free and hierarchical.** Sandhu et al.'s analysis of ChIA-PET data found the human genome converges on a scale-free, hierarchical network with function-enriched "chromatin communities" — an early framing of 3D architecture as a network rather than a list of loops.
- **Applied across proteins and systems**: ER-α, RNA polymerase II, CTCF, and SMC1A, in human MCF7, cancer cells, T cells, and mouse ESCs, neural progenitors, and B cells.
- **The protocol is complex — three parts, not two.** Wet-lab experiments, data analysis, and **experimental verification** are treated as co-equal stages, an unusual and honest structure for a method review.

## Methods / evidence

Narrative review of the protocol, the analysis pipeline, and the published application landscape, with a comparison figure of 3C, 4C, 5C, Hi-C and ChIA-PET reproduced from de Wit & de Laat. Includes a tabulated list of ChIA-PET applications known to the authors at the time.

Weight: a 2014 supplement review. It is useful here as the **definitional source for ChIA-PET** and for the enhancer-nearest-gene statistic, not as primary evidence.

## Surprising or load-bearing bits

- **">40% of enhancers skip their nearest promoter" is the number to cite** whenever justifying why an enhancer-to-gene link needs a contact measurement. It is the premise beneath [[yu-2021-snaphic|SnapHiC]]'s GWAS-SNP-to-gene assignment and beneath the ABC-score and cCRE-link validations used by [[park-2026-mintsc|MINTsC]].
- **ChIA-PET is the ancestor of the protein-anchored assays that later became the reference standard for single-cell loop calling.** PLAC-seq and HiChIP — the assays [[yu-2021-snaphic|SnapHiC]] benchmarks against — are direct descendants of the ChIP + proximity-ligation logic described here. The 2014 review is therefore upstream of how 2021 single-cell loop accuracy is even defined.
- **No single-cell version exists in this corpus.** ChIA-PET requires immunoprecipitation of a specific protein from many cells; the protein-anchored branch has no single-cell member, which is why [[single-cell-hi-c|scHi-C]] (protein-agnostic) is the only 3D modality in the single-cell toolkit. That asymmetry is worth naming: the single-cell 3D field lost the functional handle when it gained per-cell resolution.
- **"Chromatin communities" prefigures the network formulations** that reappear in [[park-2026-mintsc|MINTsC]]'s multilayer-graph framing and [[xiong-2024-scghost|scGHOST]]'s graph embedding — a decade apart, the same intuition that 3D architecture is better described as a graph than as a matrix.

## Entities mentioned

- [[yijun-ruan]] — senior author; ChIA-PET originator.

## Concepts touched

- [[chia-pet]] — this is the definitional source for the concept page.
- [[chromatin-loop]] — the protein-anchored route to loop detection.
- [[cis-regulatory-element]] — the >40% nearest-promoter result.

## Connections to other sources

- Genome-wide protein-agnostic counterpart: [[lieberman-aiden-2009-hic]]; single-cell descendants [[nagano-2013-nature]], [[ramani-2017-scihi-c]], [[tan-2018-science]].
- Its methodological descendants used as reference truth in single-cell work: PLAC-seq and HiChIP, via [[yu-2021-snaphic]].
- Domain-level architecture: [[dixon-2012-tads]], [[lupianez-2015-tad-disruption]], [[spielmann-2018-sv-3d-genome]].
- ChIP lineage: [[chip-seq]], and the single-cell chromatin-profiling alternatives that replaced ChIP at low input — [[rotem-2015-drop-chip]], [[kaya-okur-2019-cut-and-tag]], [[ku-2019-scchic-seq]].
- Enhancer annotation context: [[creyghton-2010-h3k27ac-enhancers]], [[roadmap-2015-111-epigenomes]].
- Pipeline and visualisation ecosystem: [[servant-2015-hicpro]], [[durand-2016-juicer]], [[kerpedjiev-2018-higlass]].

## Open questions

- **No single-cell ChIA-PET.** Whether protein-anchored interaction mapping can ever reach single-cell resolution — and what would substitute for immunoprecipitation if not — is the open structural question this review implies but does not raise.
- The review predates the 2015+ loop-extrusion consensus and does not engage with mechanism.
- The scale-free-network claim rests on one reanalysis and has not been revisited in this corpus.

## Related

- [[chia-pet]] · [[lieberman-aiden-2009-hic]] · [[yu-2021-snaphic]] · [[40-Topics/3d-genome]]
