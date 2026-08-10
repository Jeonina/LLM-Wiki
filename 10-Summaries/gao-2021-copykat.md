---
type: summary
title: "Gao et al. 2021 — Delineating copy number and clonal substructure in human tumors from single-cell transcriptomes (CopyKAT)"
source: "[[00-Sources/papers/Delineating copy number and clonal substructure in human tumors from single-cell transcriptomes]]"
source_kind: paper
author: "Ruli Gao, Shanshan Bai, Ying C. Henderson, ... Ken Chen, Stephen Y. Lai, Nicholas E. Navin (corresponding)"
published: 2021-01-18
ingested: 2026-08-10
doi: "10.1038/s41587-020-00795-2"
journal: "Nature Biotechnology"
tags: [CopyKAT, CNV-inference, scRNA-seq, aneuploidy, tumor-normal-classification, clonal-substructure, Bayesian-segmentation, computational-tool]
entities: ["[[nicholas-navin]]"]
concepts: ["[[scrna-seq]]", "[[structural-variants]]", "[[umi-molecular-barcoding]]", "[[drop-seq]]"]
topics: ["[[cancer-clonal-evolution]]", "[[scdna-cancer-applications]]"]
---

**Citation:** Gao et al. (2021) — *Delineating copy number and clonal substructure in human tumors from single-cell transcriptomes* — *Nature Biotechnology* 39, 599–608. [DOI](https://doi.org/10.1038/s41587-020-00795-2)

# Gao 2021 — CopyKAT

> The successor inferCNV's own maintainers now point users toward. CopyKAT infers genome-wide copy number at ~5 Mb resolution from **high-throughput 3′ scRNA-seq** — the sparse, 3′-biased data that first-generation CNV-from-RNA tools were not built for — and uses aneuploidy as a marker-free criterion to separate malignant cells from the tumor microenvironment, at 98% accuracy across 21 tumors.

## Key claims

- The problem: distinguishing tumor cells from stromal/immune cells by expression alone fails because **normal epithelial cells express the same epithelial markers as cancer cells**. Aneuploidy is the discriminator — present in ~88% of human tumors, absent from stroma.
- Prior tools ([[tickle-2019-infercnv|inferCNV]], HoneyBadger) were designed for low-throughput, high-coverage first-generation scRNA-seq and are "not suitable" for droplet/nanowell data with whole-transcriptome amplification and 3′/5′-end-only sparse coverage. They also could not resolve breakpoint coordinates or classify cells from their profiles.
- Pipeline: order genes by genomic coordinate → Freeman–Tukey variance stabilization → polynomial dynamic linear modeling to smooth outliers → **identify confident diploid cells** by pooling into small hierarchical clusters and taking the minimum-variance cluster via GMM (with a fallback per-cell "GMM definition" mode requiring ≥99% of expressed genes in neutral state, for tumors with few normal cells or near-diploid genomes) → Poisson-gamma model with MCMC for posterior means per gene window → **KS tests to join adjacent windows** into segments → convert gene space to 220 kb variable bins → hierarchical clustering to split aneuploid from diploid, then to call subclones.
- Validation against flow-sorted bulk DNA-seq of the same premalignant breast tumor (DCIS1, 1,480 cells): CopyKAT Pearson r = **0.82** vs bulk; inferCNV r = 0.79 but with lower signal and **no breakpoint coordinates**. CopyKAT segmentation is significantly closer to the DNA reference (P < 0.001) and more stable across gene-window sizes 5–500.
- Resolution honestly bounded by bootstrapping: **19% of CNAs detected at 1 Mb, 56% at 5 Mb, 88% at 20 Mb** — consistent with the claimed 5 Mb average.
- Parameter sensitivity stated: KS.cut controls breakpoint stringency, with a substantial accuracy drop above 0.3.
- Applied to 46,501 cells from 21 tumors (PDAC, TNBC, ATC, DCIS, IDC, GBM): **98% ± 3% accuracy** in tumor/normal classification, verified by colocalization with epithelial-marker expression clusters. Works across 3′ 10x, 5′ 10x, and full-length SMART-seq2 data.
- Tumor purity spans 2–97% across samples and the method works at both extremes — PDAC 6–18% (matching known high-stromal histopathology), ATC 2–80%, TNBC 34–83%, IDC 87–97%.
- **A biologically informative negative**: in all five PDAC tumors, only one of two epithelial clusters carried CNAs — the other was normal diploid epithelium that gene expression alone could not distinguish. Same in TNBC3.
- Clonal substructure in three TNBC tumors: two subclones each, on distinct neighbor-joining lineages, with 329/158/89 differentially expressed genes between them of which **47%/42%/66% lie inside subclonal CNA regions**. GSVA links subclones to distinct hallmarks (EMT, androgen response, WNT/Hedgehog, interferon, TNF-α, hypoxia, angiogenesis).
- Two independent TNBC tumors harbor rare minor subclones (7%, 18%) with **12p13.1–q12 amplification upregulating *KRAS***.

## Methods / evidence

The design strength is the ground truth: flow-sorted aneuploid cells from the same tumor, bulk whole-genome sequenced, compared at matched 220 kb resolution, with the competing method converted to the same bins for a fair comparison. Detection sensitivity is reported as a resolution curve with bootstrap resampling rather than a single number, and the key tuning parameter's failure threshold is stated.

Accuracy is measured as concordance with epithelial-marker expression clusters — a reasonable but not independent criterion, since both derive from the same transcriptome.

## Surprising or load-bearing bits

- **The 5 Mb resolution ceiling is the honest headline.** Only 19% of CNAs are detected at 1 Mb. Anything focal — the amplifications and deletions that usually matter for driver genes — is invisible. Expression-inferred CNV answers "is this cell aneuploid, and roughly how" and cannot answer "what is the copy number at this locus."
- That gap is precisely the argument for DNA-native single-cell methods. Compare [[laks-2019-dlp-plus|DLP+]], which resolves clone-specific focal amplifications and **allele-specific** copy number including copy-neutral LOH — a state expression-based inference cannot see at all, since it has no allelic information.
- The **normal diploid epithelium** result is the practical payoff and the strongest argument for running CopyKAT even when cell types look obvious: transcriptome clustering silently merges normal and malignant epithelium in a majority of the PDAC samples here.
- Recurrent rare *KRAS*-amplified subclones at 7% and 18% in two independent TNBCs is the kind of finding only per-cell resolution surfaces — bulk deconvolution would average it away.
- 47–66% of subclone-differential genes lying in subclonal CNA regions is a **dosage-driven** genotype–phenotype link, but it also means the remaining third to half are not explained by copy number, and the analysis cannot distinguish causal dosage effects from the circularity of inferring CNV *from* expression.

## Entities mentioned

- [[nicholas-navin]] — corresponding author; the same lab that founded single-cell tumor CNV sequencing in [[navin-2011-sns-tumor-evolution]], here doing it from RNA.

## Concepts touched

- [[structural-variants]] — arm-to-5 Mb-scale CNA inference, the coarsest rung of the SV-detection ladder.
- [[scrna-seq]] — CopyKAT is a genomics tool that runs on transcriptomic input, so it belongs on both pages.

## Connections to other sources

- Named successor to [[tickle-2019-infercnv]], which is now unsupported and redirects users here.
- DNA-native contrast: [[laks-2019-dlp-plus]], [[garvin-2015-natmethods|Ginkgo]], [[zaccaria-2021-chisel|CHISEL]], [[wang-2020-scope|SCOPE]].
- Lineage from [[navin-2011-sns-tumor-evolution]]; chemoresistance application in [[kim-2018-tnbc-chemoresistance]].
- Reviewed in [[mallory-2020-cna-review]] and [[lu-2024-cnaphylogeny-review]].
- The genotype-to-phenotype link it approximates is measured directly by joint DNA–RNA assays: [[gt-seq]], [[dr-seq]], [[lindenhofer-2025-sdr-seq]], [[nam-2019-got|GoT]].

## Open questions

- **Numbat** — the allele-aware successor also named in inferCNV's deprecation notice — is not bookmarked in this corpus and is the obvious comparison this summary cannot make.
- Expression-inferred CNV cannot separate dosage effects from expression-program confounding (a proliferating cluster can mimic a gain). The paper does not test this directly.
- No benchmark here against DNA-derived single-cell copy number from the *same* cells; the DCIS1 comparison is bulk DNA vs single-cell RNA.

## Related

- [[tickle-2019-infercnv]] · [[laks-2019-dlp-plus]] · [[zaccaria-2021-chisel]] · [[cancer-clonal-evolution]]
