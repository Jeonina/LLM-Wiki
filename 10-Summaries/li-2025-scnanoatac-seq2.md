---
type: summary
title: "Li et al. 2025 — Chromatin accessibility landscape of mouse early embryos revealed by single-cell NanoATAC-seq2"
source: "[[00-Sources/papers/Chromatin accessibility landscape of mouse early embryos revealed by single-cell NanoATAC-seq2]]"
source_kind: paper
author: "Mengyao Li, Zhenhuan Jiang, Xueqiang Xu, Xinglong Wu, Yun Liu, Kexuan Chen, Yuhan Liao, Wen Li, Xiao Wang, Yuqing Guo, Bo Zhang, Lu Wen, Kehkooi Kee, Fuchou Tang (conceived project)"
published: 2025-03-28
ingested: 2026-10-07
doi: "10.1126/science.adp4319"
journal: "Science 387(6741):eadp4319"
tags: [scNanoATAC-seq2, scATAC-seq, long-read, Oxford-Nanopore, preimplantation-embryo, ZGA, lineage-segregation, imprinted-XCI, Xist, Tsix, noncanonical-imprinting, LINE1, MERVL, repetitive-elements, paralogs, allele-specific-accessibility]
entities: ["[[20-Entities/fuchou-tang]]"]
concepts: ["[[scatac-seq]]", "[[oxford-nanopore]]", "[[transposable-elements]]", "[[mappability]]", "[[highly-repetitive-regions]]", "[[tn5-tagmentation]]", "[[cis-regulatory-element]]", "[[chromatin-compartments]]", "[[transcription-factor-motif]]"]
topics: ["[[single-cell-atac-seq]]", "[[long-read-sequencing]]"]
---

**Citation:** Li et al. (2025) — *Chromatin accessibility landscape of mouse early embryos revealed by single-cell NanoATAC-seq2* — *Science* 387(6741):eadp4319. [DOI](https://doi.org/10.1126/science.adp4319)

# Li 2025 — scNanoATAC-seq2

> scNanoATAC-seq2 is a **single-cell-input, single-tube** scATAC protocol: isolation, nuclear extraction, digitonin permeabilisation and Tn5 transposition all happen in one tube, followed by **Oxford Nanopore long-read sequencing**. It suits scarce samples down to one cell. Applied to 3,302 cells across **10 mouse preimplantation stages** (zygote to late blastocyst), with each cell's embryo of origin recorded, it maps ZGA reprogramming and EPI/PE/TE segregation. Long reads add what short-read ATAC cannot: **allele-resolved accessibility** for imprinting and X inactivation, and **copy-resolved accessibility of individual repeats (LINE1, MERVL) and paralog families (*Zscan4*, *Tcstv*, *Obox*)**.

## Key claims

- **Data quality.** After QC, 3,302 cells with a median of 23,160 fragments and median fragment length 5,486 bp. Mitochondrial fragments were a median **0.65%** per cell, against >50% in short-read embryo ATAC even after mtDNA depletion. 240,494 peaks across 11 cell types (≈22,000–102,000 per type; promoter peaks 8–24%). Peak calling was similar to short-read methods in mappable regions and recalled more peaks in repeats. Cell-line tests showed minimal cross-contamination.
- **Cell numbers.** 547 zygote, 278 early 2-cell, 205 late 2-cell, 193 4-cell, 387 8-cell, 265 morula, 303 ICM, 325 early TE, 221 EPI, 178 PE, 263 late TE.
- **ZGA.** Accessibility generally precedes RNA by only a few hours. A subset of genes differentially accessible between early and late 2-cell (*Kdm5b*, *Obox6*, *Crxos*, *Tcstv3*, *Rps3*, *Dhx9*) opens long before expression. Accessibility change is best explained by H3K27ac and RNAP II. Net of those, H3K4me3 and A-compartment status associate positively and H3K27me3 negatively (P < 0.05). α-amanitin- or DRB-treated late 2-cell embryos looked zygote-like and failed to open **5,269** loci. Of 3,252 genes sensitive to both drugs, 438 were also α-amanitin-sensitive in human embryos (enrichment P = 3 × 10⁻⁴⁷).
- **Lineage segregation.** ICM/TE intraembryonic heterogeneity is evident at the **16-cell stage**, before unsupervised clustering separates ICM and TE (late morula). EPI: SOX2, NANOG, KLF2; PE: SOX17, HNF1B, GATA4/6; TE: TEAD4, GATA3, CDX2, ELF3. ~14–16% of late-2-cell putative enhancers remain open at late blastocyst. 8 of 14 tested EPI enhancer candidates were active in naïve mESC reporter assays. *Nanog* gene-score activation precedes its TF-binding score.
- **Noncanonical imprinting.** Allele-specific accessible genes (ASGs) decline sharply at the blastocyst stage, and paternal ASGs dominate in cleavage stages. **325 ASGs (317 paternal, 8 maternal)** at the 8-cell stage were supported across three genetic backgrounds (C57×DBA, DBA×C57, C57×CAST). Median allele tagging rates were 96.8% in C57×CAST (>20 M het SNPs) and 47% in C57×DBA (4 M). ASGs track reciprocal-allele H3K27me3.
- **Imprinted XCI.** Xm is more accessible than Xp from zygote to blastocyst. The skew grows from 4-cell to morula, increases further in PE/TE, and diminishes but is **incompletely erased** in EPI. Allelic control **shifts from the *Xist* domain** (paternal-biased, zygote–8-cell) **to the *Tsix* domain** (maternal-biased) in PE and TE. In EPI both domains become allele-balanced (only a minor *Tsix* maternal bias remains). Reciprocal crosses support this.
- **Repeats.** Of 16,882 full-length LINE1 copies, **157 were significantly activated** from zygote to morula. Activation is 4.3-fold enriched in the A compartment (2.05% of 5,013 vs 0.48% of 11,221 in B) and is driven by evolutionarily young subfamilies. Two intact LINE1s with 99.68% identity, and two MERVLs with 98.24% identity, show different accessibility; short-read data could not resolve these. MT2-Mm LTRs at MERVL ends are open in late 2-cell while internal ORFs are closed. Repeat activity and promoter proximity predict ZGA gene activation (ERVL slope 0.23, P = 4.57 × 10⁻⁵), e.g., *Sp110*, *Sp140*, *Zscan4c/d* near active MERVLs.
- **Paralogs.** A key intronic CRE in every *Zscan4* paralog opens at late 2-cell and is partly missed by short-read ATAC because of low mappability. *Tcstv* family members could be annotated individually.

## Methods / evidence

C57BL/6N × DBA/2N embryos (plus reciprocal and CAST crosses), with all cells per embryo profiled up to the 16-cell stage and subsets thereafter. Cell- and plate-barcoded PCR libraries were sequenced on PromethION 48. Analyses: Monocle3 pseudotime, motif enrichment, integration with public scRNA-seq and histone data, RNAP II inhibitors, and enhancer reporter assays.

Weight: a large, carefully designed atlas with orthogonal checks (reciprocal crosses, drug perturbation, reporter assays, RNA concordance). Many regulatory conclusions are **correlational** (TF gene score vs binding-site accessibility, repeat proximity vs expression). The repeat and paralog advantages rest on long-read mappability, which is the method's strongest unique contribution. (synthesis)

## Surprising or load-bearing bits

- **Low mtDNA background is itself a protocol advantage**: 0.65% vs >50% in short-read embryo ATAC, so nearly all reads are informative.
- **Hand-off of XCI control between TAD-scale domains.** Paternal *Xist*-domain accessibility drives iXCI in cleavage stages; maintenance in extraembryonic lineages relies on maternal *Tsix*-domain accessibility.
- **Long-read ATAC as a copy-resolved repeat assay.** Individual LINE1/MERVL copies differ in accessibility despite >98% identity, which short reads collapse. Repeat regulation is copy-specific, not family-wide. (synthesis)
- **Embryo identity per cell** turns scATAC into a within-embryo heterogeneity assay. That is how the 16-cell epigenomic split becomes visible.

## Concepts touched

- [[scatac-seq]] / [[tn5-tagmentation]] — single-cell-input, single-tube Tn5 with long-read readout.
- [[oxford-nanopore]] — long fragments (median 5.5 kb) give SNP phasing and repeat mappability.
- [[transposable-elements]] / [[highly-repetitive-regions]] / [[mappability]] — copy-level LINE1/MERVL accessibility.
- [[chromatin-compartments]] — A-compartment enrichment of activated LINE1s.
- [[cis-regulatory-element]] / [[transcription-factor-motif]] — stage- and lineage-specific CREs and TF activity.

## Connections to other sources

- Lab lineage: [[fuchou-tang]] (also [[tang-2009-scrna-seq]]). The predecessor scNanoATAC-seq is cited but not in the wiki.
- Short-read scATAC foundations it contrasts with: [[buenrostro-2015-nature]], [[cusanovich-2015-sciatac]]; repeat blind spots in short-read epigenomics: [[mappability]].
- Long-read single-cell genomics peers: [[hard-2023-long-read-scwgs]], [[liu-2025-long-read-epigenome-review]], [[fu-2025-longread-methylation]]. (synthesis)
- Methyltransferase-based single-cell accessibility in early embryos is cited as the prior single-cell map; NOMe-type approaches in the wiki: [[nome-seq]]. (synthesis)

## Open questions

- Do the >100 accessible full-length LINE1s actually retrotranspose, i.e., is accessibility a proxy for mobilisation competence?
- Throughput: plate-based, one-cell-per-tube processing limits scale. How does it compare in cost to droplet scATAC for non-scarce samples? (synthesis)
- Accessibility at a TF gene "preceding" binding-site accessibility is inferred from pseudotime, so causality is untested.

## Related

- [[fuchou-tang]] · [[scatac-seq]] · [[oxford-nanopore]] · [[40-Topics/single-cell-atac-seq]] · [[40-Topics/long-read-sequencing]]
