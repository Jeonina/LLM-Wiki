---
type: summary
title: "Rotem 2015 — Drop-ChIP: single-cell ChIP-seq reveals chromatin-state subpopulations"
aliases: ["Rotem 2015 Drop-ChIP", "Drop-ChIP", "scChIP-seq"]
tags: [Drop-ChIP, scChIP-seq, microfluidics, DBM, H3K4me3, H3K4me2, founding-method, Bernstein-lab, Weitz-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Assaf_2015_NatureBiotechnology.pdf"]
---

Rotem, Ram, Shoresh et al. (Bernstein, Weitz, Goren labs; Broad/Harvard) developed **Drop-ChIP**, the founding single-cell ChIP-seq method. The platform uses a drop-based microfluidics (DBM) device to encapsulate single cells in ~50-μm aqueous drops with weak detergent + MNase, then merges each chromatin drop with a barcode drop containing a unique oligonucleotide adaptor (library of 1,152 barcodes). Barcoded chromatin from many cells is pooled before bulk immunoprecipitation, dramatically lowering input requirements per cell. Profiled H3K4me3 and H3K4me2 in mixed populations of ES cells, MEFs, and hematopoietic progenitors at ~1,000 unique reads per cell. Despite sparsity, the method identified chromatin-state subpopulations within ES cells corresponding to pluripotency and differentiation priming — features not visible in matched scRNA-seq.

## Why this matters

Founding paper for single-cell ChIP-seq. Establishes the DBM + barcode-merge architecture later inherited by drop-seq, sciATAC, 10x platforms. Anchors §3.2 (chromatin assays beyond ATAC) and §3.4 (histone-modification scDNA). Predecessor of scCUT&Tag (Kaya-Okur 2019) which replaced ChIP with Tn5 tethering, and CoBATCH/uliCUT&RUN. Important historical citation when describing the chromatin-assay landscape.

## Related

- [[10-Summaries/buenrostro-2015-nature]]
- [[10-Summaries/cusanovich-2015-sciatac]]
- [[30-Concepts/single-cell-chromatin-profiling]]
