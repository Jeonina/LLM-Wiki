---
type: summary
title: "Abbasova et al. 2025 — CUT&Tag recovers up to half of ENCODE ChIP-seq histone acetylation peaks"
source: "[[00-Sources/papers/CUT&Tag recovers up to half of ENCODE ChIP-seq histone acetylation peaks]]"
source_kind: paper
author: "Leyla Abbasova, Paulina Urbanaviciute, Di Hu, Joy N. Ismail, Brian M. Schilder, Alexi Nott, Nathan G. Skene, Sarah J. Marzi (corresponding)"
published: 2025-03-27
ingested: 2026-10-07
doi: "10.1038/s41467-025-58137-2"
journal: "Nature Communications 16:2993"
tags: [CUT&Tag, ChIP-seq, ENCODE, H3K27ac, H3K27me3, benchmark, peak-calling, MACS2, SEACR, PCR-duplicates, EpiCompare, K562]
entities: ["[[steven-henikoff]]"]
concepts: ["[[cut-and-tag]]", "[[chip-seq]]", "[[cut-and-run]]", "[[peak-calling]]", "[[duplicate-marking]]", "[[tn5-tagmentation]]", "[[enhancer-states]]", "[[quality-control-metrics]]"]
topics: ["[[histone-modifications]]"]
---

**Citation:** Abbasova et al. (2025) — *CUT&Tag recovers up to half of ENCODE ChIP-seq histone acetylation peaks* — *Nature Communications* 16:2993. [DOI](https://doi.org/10.1038/s41467-025-58137-2)

# Abbasova 2025 — CUT&Tag vs ENCODE

> CUT&Tag is widely adopted as a low-input, low-depth replacement for ChIP-seq, but had not been systematically benchmarked against reference ChIP data. Profiling **H3K27ac** (in depth) and **H3K27me3** in K562 — 38 new datasets plus published CUT&Tag and CUT&RUN — against matched ENCODE ChIP-seq, the authors find CUT&Tag recovers on average **~54% of ENCODE peaks**, specifically the **strongest, most accessible** ones, with the same GO and motif enrichments. For the acetyl mark, the advertised signal-to-noise advantage over ChIP-seq **did not materialise**; for the methyl mark it did.

## Key claims

- **Recall ceiling around half.** Average ENCODE recall across CUT&Tag experiments was 54% (sd 4.99), comparable for MACS2 and SEACR; maximum 63% (Diagenode antibody, duplicates retained, MACS2). Published data from the method developers reached 41% (H3K27ac CUT&Tag, MACS2) and 53% (CUT&RUN, SEACR). H3K27me3 CUT&Tag reached ~58% despite many more peaks. Merging high-complexity samples raised recall (to over 70% per the Discussion) at the cost of precision. Published HCT116 H3K27me3 CUT&Tag showed even poorer ENCODE capture.
- **CUT&Tag captures the strongest peaks.** Captured ENCODE peaks had higher ENCODE significance and more ATAC reads than missed ones (p < 2 × 10⁻¹⁶ for q-values; p = 2.4 × 10⁻⁸ for ATAC reads). Nearly all H3K27ac CUT&Tag regions fell in H3K27ac regions shared with ATAC peaks, not in ATAC-only regions; ~70% of ENCODE H3K27ac peaks overlap ATAC peaks.
- **No signal-to-noise advantage for H3K27ac.** H3K27ac FRiP (MACS2 means 32–43% across antibodies) was similar to ENCODE peaks (37%) and the reported ENCODE ChIP FRiP of 42%; in overlapping regions H3K27ac FRiP was similar to ChIP while H3K27me3 gave about twice as many reads. H3K27me3 CUT&Tag FRiP (~73%) exceeded ENCODE's reported 66%. At down-sampled depth (0.5–2 M unique reads), only the Diagenode antibody beat ENCODE FRiP.
- **Experimental knobs mostly don't help.** HDAC inhibitors (TSA 1 µM; sodium butyrate 5 mM by qPCR) did not improve peaks, signal-to-noise or ENCODE capture. Duplication rates were high (mean 82.25%, range 55.49–98.45%); 11 or 13 PCR cycles modestly reduced duplication; 15 cycles with SDS-based extraction gave the most unique fragments, but this did not improve ENCODE coverage after down-sampling. Best H3K27ac antibodies: Abcam ab4729 (the antibody ENCODE used) and Diagenode.
- **Peak-caller behaviour.** Optimal settings (target precision >75%): SEACR stringent, threshold 0.01 (0.1 for H3K27me3); MACS2 narrow, q = 1 × 10⁻⁵, local lambda off (broad for H3K27me3). SEACR gave slightly higher precision and F1 and was robust to high duplication; MACS2 called excessive spurious peaks when duplicates were kept in high-duplication samples, many in heterochromatin. SEACR H3K27ac peaks were wider — 1.35–1.68 MACS2 peaks per SEACR peak on average — which may merge neighbouring elements. MACS2 peaks were more consistent and more ENCODE-like.
- **Recommendation: drop duplicates.** Duplicates did not affect SEACR precision/recall; with MACS2 they slightly raised recall and lowered precision. Overall the authors favour MACS2 without duplicates.
- **Biology preserved.** CUT&Tag recovered all top ENCODE K562 H3K27ac GO terms and most top TF motifs (BACH1/2, FOSL2, GATA1/2/6, JUN-AP1, JUNB, NFE2-family), plus some motifs ENCODE did not show (ELK1, ELK4, GATA3, GATA4).
- **Short fragments track open chromatin.** ~8% of H3K27me3 CUT&Tag reads fell in ATAC peaks; removing <100-bp fragments reduced H3K27ac reads overlapping ATAC peaks from 29% to 20%.

## Methods / evidence

Bench-top CUT&Tag on 500,000 K562 cells per condition; four H3K27ac antibodies at three dilutions screened by qPCR against top/bottom ENCODE peaks; HiSeq 4000 PE75. Processing: Trim Galore, Bowtie2, Picard, MACS2 2.2.9.1, SEACR 1.3, DiffBind, chromVAR (FRiP), ChIPseeker, ChromHMM states via genomation, clusterProfiler, HOMER. Ground truth: ENCODE replicated peaks (ENCSR000AKP, ENCSR000EWB); orthogonal checks with ENCODE ATAC, DNase-filtered STARR-seq enhancers. Comparator data: Kaya-Okur 2019 CUT&Tag and published CUT&RUN. Released EpiCompare and PeakyFinders R packages.

Weight: careful, single-cell-line benchmark (K562) with ENCODE as the reference — which the authors note may not be ground truth. ChromHMM states derive from ENCODE ChIP, so state overlaps are partly circular. Antibody ab4729 may be favoured because ENCODE used it.

## Surprising or load-bearing bits

- **CUT&Tag's headline advantage is mark-dependent.** The low-background, low-depth claim was shown on methyl marks; for H3K27ac it was equal or noisier than ChIP. Any single-cell CUT&Tag study of acetylation inherits this ceiling. (synthesis)
- **The ~50% recall is selective, not random**: CUT&Tag sees peaks that coincide with open chromatin. Whether the missed ChIP peaks are real but weak, or ChIP artefacts from crosslinking and sonication, is left open — the paper does not settle which assay is closer to truth.
- **Tn5's accessibility preference shows up even in a targeted assay** (short fragments overlapping ATAC peaks), a reminder that CUT&Tag signal is partly accessibility. (synthesis)
- Practical: high duplication plus MACS2 creates false heterochromatic "H3K27ac" peaks.

## Concepts touched

- [[cut-and-tag]] — quantitative recall/precision vs ENCODE; mark-dependent performance.
- [[chip-seq]] — ENCODE ChIP as the (imperfect) reference.
- [[peak-calling]] — MACS2 vs SEACR parameter optimisation for CUT&Tag.
- [[duplicate-marking]] — duplicates inflate MACS2 false peaks; recommended removal.
- [[tn5-tagmentation]] — open-chromatin bias of pA-Tn5 visible in short fragments.
- [[enhancer-states]] — H3K27ac CUT&Tag peaks in promoters and strong enhancers; SEACR also picks up weak enhancers.

## Connections to other sources

- Original method and claims being tested: [[kaya-okur-2019-cut-and-tag]]; CUT&RUN peak caller: [[meers-2019-seacr]]; ChIP-seq caller: [[zhang-2008-macs]]; motif tool: [[heinz-2010-homer]]; FRiP via [[schep-2017-chromvar]].
- H3K27ac as active-enhancer mark: [[creyghton-2010-h3k27ac-enhancers]].
- Single-cell CUT&Tag methods that inherit these bulk limits: [[bartosovic-2021-sccut-tag]], [[wu-2021-sccut-tag]], [[janssens-2023-scicut-tag]], [[zhang-2022-sccut-tag-pro]], [[bartosovic-2022-nano-cut-tag]], [[gopalan-2022-multi-cut-and-tag]].

## Open questions

- Do CUT&Tag-missed ENCODE H3K27ac peaks validate functionally? STARR-seq and MPRA checks were inconclusive.
- Is the acetyl-mark shortfall general (other acetyl marks) or K562- and antibody-specific?
- Would CUT&Tag-specific peak callers (GoPeaks is named) or linear amplification (TIP-seq) raise the ceiling?

## Related

- [[cut-and-tag]] · [[40-Topics/histone-modifications]] · [[kaya-okur-2019-cut-and-tag]] · [[meers-2019-seacr]]
