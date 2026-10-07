---
type: summary
title: "Li et al. 2024 — scNanoSeq-CUT&Tag: a single-cell long-read CUT&Tag sequencing method for efficient chromatin modification profiling within individual cells"
source: "[[00-Sources/papers/scNanoSeq-CUT&Tag_ a single-cell long-read CUT&Tag sequencing method for efficient chromatin modification profiling within individual cells]]"
source_quality: full
source_sha256: "174de0cc6b17b12a32dae97cf2c8b34e1ee966eaadc03bbcbe6a224bbee30513"
source_kind: paper
author: "Qingqing Li, Yuqing Guo, Zixin Wu, Xueqiang Xu, Zhenhuan Jiang, Shuyue Qi, Zhenyu Liu, Lu Wen, Fuchou Tang"
published: 2024-10-07
ingested: 2026-10-07
doi: "10.1038/s41592-024-02453-w"
journal: "Nature Methods 21(11):2044–2057"
tags: [scNanoSeq-CUT&Tag, CUT&Tag, nanopore, long-read, single-cell, histone-modifications, H3K4me3, H3K27ac, H3K9me3, CTCF, RAD21, allele-specific, L1Hs, L1Md, blacklist-regions, spermatogenesis, 5-azacytidine]
entities: ["[[fuchou-tang]]"]
concepts: ["[[cut-and-tag]]", "[[oxford-nanopore]]", "[[tn5-tagmentation]]", "[[transposable-elements]]", "[[highly-repetitive-regions]]", "[[mappability]]", "[[chromatin-compartments]]", "[[allele-specific-methylation]]", "[[peak-calling]]", "[[decitabine]]"]
topics: ["[[histone-modifications]]", "[[long-read-sequencing]]", "[[single-cell-multiomics]]"]
---

**Citation:** Li et al. (2024) — *scNanoSeq-CUT&Tag: a single-cell long-read CUT&Tag sequencing method for efficient chromatin modification profiling within individual cells* — *Nature Methods* 21(11):2044–2057. [DOI](https://doi.org/10.1038/s41592-024-02453-w)

# Li 2024 — scNanoSeq-CUT&Tag

> scNanoSeq-CUT&Tag moves single-cell CUT&Tag onto Oxford Nanopore. The key chemical change is a **pG-Tn5 loaded with a single adaptor**, so every tagmented fragment (not ~50% as with two-adaptor Tn5) is PCR-recoverable as a long amplicon; cells are plate-sorted with a 24-bp inner barcode, pre-amplified, pooled and re-amplified with outer barcodes (up to 96 × 96). The payoff of multi-kilobase reads is access to what short reads cannot map — **individual L1Hs copies (>99% identical), H3K9me3-dense heterochromatin and blacklist regions** — plus haplotype-resolved (allele-specific) peaks and direct single-molecule evidence that two neighbouring peaks carry the same mark on the same allele in the same cell.

## Key claims

- **Scale and depth.** Six human cell lines (K562, 293T, GM12878, HG002, H9, HFF1), five histone marks (H3K4me3, H3K27ac, H3K36me3, H3K27me3, H3K9me3) and two chromatin proteins (CTCF, RAD21): **17,211 high-quality cells, 3.5 Tb**, median read length 3.4–4.4 kb. Up to **13,373 unique reads per cell**, described as clearly better than Paired-Tag and CoBATCH; FRiP comparable to NGS scCUT&Tag.
- **Low cross-talk.** Human 293T / mouse 3T3 species mixing gave an expected collision rate of 1.6% (2 × 0.8% detected human–mouse collisions).
- **Fidelity to bulk.** TSS scores comparable to Paired-Tag and ChIP-seq except H3K27ac (lower, attributed to loss of short fragments); >50% of peaks unique to scNanoSeq-CUT&Tag fall in ENCODE cCREs; merged tracks from **as few as 146 cells** were highly comparable with bulk ChIP-seq.
- **Cell typing.** Every mark separates all six cell lines; H3K4me3 and CTCF reads capture the K562 *BCR–ABL1* fusion. In 2,471 mouse PBMCs (H3K4me3), B, CD4+ T, CD8+ T cells and monocytes separate, consistent with scRNA-seq projection; downsampled to **1,000 reads/cell**, 99.5% of B, 98.3% of T cells and 99.3% of monocytes were correctly assigned (97.3% classical, 90.4% non-classical monocytes), but CD4 vs CD8 T cells were mostly not separable per cell (on 250 downsampled PBMCs). Authors project ~10,000 cells per PromethION 48 run at 1,000 reads/cell, ~$0.1 sequencing cost per cell.
- **Allele-specific peaks.** At least threefold more peaks containing heterozygous SNPs detected than in NGS ChIP-seq; **388 allele-specific H3K4me3 peaks** in GM12878, only 22.2% (86/388) with a het SNP inside the peak (phasing via flanking SNPs within 10 kb). ASPs concentrate on chrX (XIST signal skewed to the paternal allele) and are cross-validated at imprinted loci.
- **Neighbouring-region co-occupancy.** A Kolmogorov–Smirnov test of read-length distributions (supporting reads with ends within 1 kb of the target peak vs background within 100 kb) detects hundreds to thousands of same-mark co-occupancy events per dataset, mostly within 10 kb (e.g., *EPB41* promoter with three upstream enhancers).
- **Repeats and blacklist regions.** Hundreds to thousands of H3K4me3/H3K27ac peaks on LINE/LTR elements absent from NGS ChIP-seq; ~50% validated by scNanoATAC-seq. For 320 full-length L1Hs, mappability/discernibility was **96.5%** for scNanoSeq-CUT&Tag H3K9me3 and 97.0% for SMOOTH-seq, compared with NGS WGS. H3K4me3 peaks on full-length L1Hs in *CAMK4* and *RAG1* specifically in K562. Clear H3K27ac/H3K9me3 peaks in human blacklist regions (3.0% of genome, ~91 Mb, excluding centromeres and rDNA), which remain hard to map even with long reads.
- **Mouse spermatogenesis (H3K4me3).** 2,656 cells, median 11,977 unique reads/cell, median FRiP >50%; seven spermatogenic types + Sertoli cells; 1,251–2,831 co-occupancy events per type. L1Md_A / L1Md_T elements with H3K4me3 peaks rise from late primary spermatocytes to a maximum at the Sperm1 stage.
- **DNA demethylation → H3K27ac at repeats.** K562 treated with 5 μM 5-azacytidine for 5 days (WGBS-confirmed demethylation): 2,169 cells; 201 individual repetitive elements gained H3K27ac peaks; 102 of these were detectable in scNanoCOOL-seq data and all had lost methylation; one L1Hs copy lost methylation, gained H3K27ac and was transcribed.

## Methods / evidence

Plate-based: antibody → secondary → pG-Tn5 (single Tn5-Apt1 adaptor + ME block) → Mg²⁺ tagmentation → FACS into 96-well lysis with inner-barcode primer → 22-cycle long-range pre-amplification (PrimeSTAR GXL) → pool 48 cells → 8–10 cycles with outer barcodes → ONT PromethION 48 (R9.4.1). In practice 48 inner × 24 outer barcodes (1,152 cells/experiment). Analysis: nanoplexer demultiplexing, NanoFilt (q ≥7, ≥100 bp), minimap2, MAPQ ≥30, read ends ±50 bp as signal, ArchR (iterative LSI) for clustering, SEACR peak calling with cell-support filter. NGS comparators: ENCODE ChIP-seq, Paired-Tag, CoBATCH, scCUT&Tag.

Weight: large and multi-mark, but mostly cell lines; "better than Paired-Tag and CoBATCH" is a reads-per-cell comparison, not a head-to-head on the same cells. Repeat-peak validation relies on the same lab's long-read companion assays (scNanoATAC-seq, scNanoCOOL-seq, SMOOTH-seq). The co-occupancy statistic assumes uniform read lengths for truly co-occupied pairs — plausible but not validated orthogonally.

## Surprising or load-bearing bits

- **Single-adaptor Tn5 doubles recoverable fragments** in principle (vs ~50% with two different adaptors) — a library-chemistry change that matters as much as the sequencer. (synthesis on emphasis)
- **Only 22% of allele-specific peaks contain a het SNP** — long reads phase via flanking SNPs, so allele-specific chromatin becomes visible at peaks short reads cannot phase.
- **Blacklists are a short-read artefact, not a biology filter**: blacklist regions carried consistent H3K27ac peaks across all six cell lines and are enriched for cCREs. (synthesis on emphasis)
- **Per-copy L1 epigenetics**: methylation-dependent silencing can be attributed to an individual L1Hs locus, not just the family.

## Concepts touched

- [[cut-and-tag]] — long-read, single-adaptor single-cell variant.
- [[oxford-nanopore]] / [[mappability]] / [[highly-repetitive-regions]] — reads spanning repeats with unique flanks.
- [[transposable-elements]] — per-copy L1Hs/L1Md chromatin states and their response to demethylation.
- [[chromatin-compartments]] — active marks resolved on short A compartments embedded in long B compartments.
- [[allele-specific-methylation]] — analogous haplotype-resolved logic applied to histone marks (closest existing page). (synthesis)
- [[decitabine]] — related hypomethylating-agent concept; this study uses 5-azacytidine.

## Connections to other sources

- Short-read CUT&Tag lineage: [[kaya-okur-2019-cut-and-tag]], [[bartosovic-2021-sccut-tag]], [[wu-2021-sccut-tag]], [[zhang-2022-sccut-tag-pro]], [[bartosovic-2022-nano-cut-tag]], [[janssens-2023-scicut-tag]]; the early sparse single-cell ChIP it improves on: [[rotem-2015-drop-chip]].
- Bulk long-read protein–DNA mapping it extends to single cells: [[altemose-2022-dimelo-seq]].
- Tooling reused: [[granja-2021-archr]], [[meers-2019-seacr]].
- Long-read epigenome review context: [[liu-2025-long-read-epigenome-review]]; methylation + histone in one cell by other routes: [[geisenberger-2025-scepi2-seq]], [[tavares-2026-6-base-cut-tag]].

## Open questions

- Centromeres (~59 Mb) and rDNA remain unmappable even here; whether newer basecalling/assemblies (T2T) resolve them is not tested. (synthesis)
- Plate-based sorting caps throughput; the projected 10,000 cells/run assumes a combinatorial format not demonstrated at that scale.
- Co-occupancy beyond ~10 kb is inferred from cross-cell correlation, not single molecules — the long-read advantage stops at read length.

## Related

- [[cut-and-tag]] · [[altemose-2022-dimelo-seq]] · [[transposable-elements]] · [[40-Topics/histone-modifications]] · [[40-Topics/long-read-sequencing]]
