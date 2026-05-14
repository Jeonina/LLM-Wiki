---
type: summary
title: "Svensson 2017 — Power analysis of single-cell RNA-sequencing experiments"
aliases: ["Svensson 2017", "scRNA-seq power analysis", "Svensson power analysis"]
tags: [scRNA-seq, benchmarking, ERCC, spike-in, sensitivity, accuracy, dropout, UMI, Teichmann-lab, EMBL-EBI, Sanger]
created: 2026-05-14
updated: 2026-05-14
sources: ["Svensson_2017_NatureMethods.md"]
---

Svensson, Natarajan, Ly et al. (Teichmann lab, EMBL-EBI / Wellcome Sanger) performed the **first unified benchmark of scRNA-seq protocol sensitivity and accuracy** ([DOI](https://doi.org/10.1038/nmeth.4220)). Using ERCC spike-in RNAs at known molar concentrations as ground truth, they re-analyzed 18,123 publicly available samples across **15 protocols and 28 studies** (17 whole-transcript coverage protocols + 11 UMI-based), plus four protocols (Smart-seq2, SMARTer, STRT-seq, 10x Chromium) freshly run in-house on batch-matched mESCs. Two metrics were operationalised: **accuracy** = Pearson correlation between log-input concentration and log-measured expression per cell (range), and **sensitivity** = the molecular input level at which the logistic detection probability reaches 50%. Key findings: (i) scRNA-seq accuracy is generally high — most protocols achieve Pearson r > 0.6 per cell — but systematically lower than bulk RNA-seq; (ii) sensitivity varies over **four orders of magnitude** across protocols, with the best (SMARTer/CEL-Seq2 on Fluidigm C1, STRT-Seq, inDrop) detecting single-digit input molecules; (iii) **endogenous mRNA is captured ~10× more efficiently than ERCC spike-ins** (smFISH cross-check) — published sensitivities are conservative; (iv) UMI counts saturate sublinearly with input molecules (best-fit exponent ≈0.8, not 1), so the assumption of perfect digital quantification is approximate; (v) sequencing depth strongly drives sensitivity but barely affects accuracy — recommendation: **~1M reads per cell** is the saturation target for gene detection. Freeze-thaw experiments quantified an ~20% spike-in degradation rate per cycle, broadly conserved between ERCCs and SIRVs.

## Why this matters

**The reference paper for "what scRNA-seq actually measures vs. what it claims to measure."** Every review of scRNA-seq, multi-omics, or single-cell technology needs to quantify the gap between bulk and single-cell sensitivity — Svensson 2017 is that quantification, conducted with the rigor of a meta-analysis across the published landscape. For a multi-omics review, the paper grounds three load-bearing claims:

1. **The dropout problem is real and measurable.** Capture rates of 1–25% mean that absence of detected transcript ≠ absence of expression — this drives the need for imputation methods (MAGIC, scVI), zero-inflated models (ZINB-WaVE), and the cautious interpretation of differential expression across rare cell types.
2. **Protocol choice matters more than throughput choice.** Plate-based microfluidic methods (CEL-Seq2/C1, SMARTer/C1) outperform droplet methods (Drop-seq, inDrop, 10x) on per-cell sensitivity by ~10×. Reviews that conflate "scRNA-seq" into a single category mislead — the throughput-sensitivity tradeoff is a design axis, not a coincidence.
3. **UMIs are not perfect digital counters.** The sublinear UMI saturation (exponent ≈0.8) means quantitative claims at high expression levels still have residual amplification bias. This nuance matters for any multi-omics method that integrates UMI-tagged scRNA-seq with non-UMI modalities (e.g. full-length transcripts, scATAC peaks).

## Key numbers (for review writing)

| Metric | Result |
|---|---|
| Bulk RNA-seq Pearson accuracy | r ≈ 0.95–0.99 |
| scRNA-seq Pearson accuracy (typical) | r ≈ 0.6–0.95 (protocol-dependent) |
| Sensitivity range across protocols | ~1 to ~1,000 input molecules at 50% detection |
| Drop-seq capture vs. smFISH | ~5–10× underestimate (ERCC-based) → ~10–25% true endogenous capture |
| UMI saturation exponent | ~0.8 (perfect digital counting would give 1.0) |
| Sequencing-depth saturation for accuracy | ~250,000 reads/sample |
| Sequencing-depth saturation for sensitivity | ~4.5M reads/sample (1M = good practical target) |
| Spike-in degradation per freeze-thaw cycle | ~20% (95% CI: 18.5–19.7%) |

## Limitations of the benchmark itself

- ERCC spike-ins have short poly-A tails (~24 nt vs. ~250 nt for endogenous mRNA) and no 5' cap → consistently lower capture than endogenous transcripts; sensitivity numbers are *relative* not absolute.
- Cross-laboratory protocol implementation is uncontrolled — a "poor" protocol score may reflect operator skill rather than chemistry.
- Mostly mESC/cell-line data; performance in primary or fixed tissue may differ.
- 2017 vintage — does not cover newer chemistries (10x v3, Smart-seq3, Parse Bio, BD Rhapsody, Fluent BioSciences PIPseq) that closed some of the sensitivity gap.

## Related

- [[30-Concepts/scrna-seq]]
- [[10-Summaries/tang-2009-scrna-seq]] — the founder protocol benchmarked here against later methods
- [[10-Summaries/macosko-2015-drop-seq]] — one of the protocols compared (Drop-seq sits in the high-throughput / mid-sensitivity quadrant)
- [[30-Concepts/umi-molecular-barcoding]] — Svensson's sublinear-UMI finding refines the UMI concept page
- [[10-Summaries/gur-2025-scatac-vs-bulk]] — analogous bulk-vs-single-cell benchmark for ATAC
- [[20-Entities/sarah-teichmann]] · [[20-Entities/valentine-svensson]]

## Citation

Svensson V, Natarajan KN, Ly L-H, Miragaia RJ, Labalette C, Macaulay IC, Cvejic A, Teichmann SA. *Nat Methods* 14(4): 381–387 (2017). PMID: 28263961. PMC: PMC5376499. [DOI](https://doi.org/10.1038/nmeth.4220). According to PubMed.
