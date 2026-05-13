---
type: summary
title: "Hainer 2019 — Profiling of pluripotency factors in single cells and early embryos (uliCUT&RUN)"
aliases: [Hainer 2019, Sarah 2019, uliCUT&RUN, ultra-low-input CUT&RUN]
tags: [chromatin, CUT&RUN, single-cell, transcription-factor, pluripotency, embryo, method]
created: 2026-05-12
updated: 2026-05-12
sources: ["00-Sources/papers/Sarah_2019_Cell.pdf"]
---

# Hainer et al. 2019 — Ultra-low-input CUT&RUN (uliCUT&RUN)

> Sarah J. Hainer, Ana Bošković, Kurtis N. McCannell, Oliver J. Rando, **Thomas G. Fazzio\***. *Cell* **177**, 1319–1329 (16 May 2019). DOI: 10.1016/j.cell.2019.03.014. UMass + Pittsburgh.

> **Not a neuro-mosaicism paper despite filename collision in this batch.** This is a chromatin / TF mapping method paper. Included in this ingest because it was in the neuro-batch by filename but represents a key methodological neighbor for the scCUT&Tag family already in the wiki.

## Thesis

Modified the CUT&RUN protocol (Skene & Henikoff 2017) into **ultra-low-input uliCUT&RUN** that profiles transcription-factor binding and histone modifications from **as few as 10 cells, single cells, and individual pre-implantation embryos** (blastocysts ~30–80 cells). Demonstrated for CTCF, H3K4me3, OCT4, SOX2, NANOG, BRG1, H3K27ac, H3K27me3, SUZ12 in mouse ESCs. Identified that **NANOG binding to its genomic targets in mouse blastocysts depends on the SWI/SNF chromatin remodeler BRG1** in vivo, despite being largely BRG1-independent in cultured cells.

## Method

1. CUT&RUN ([[cut-and-run]]) uses protein A-MNase fusion guided to chromatin by an antibody against the target protein; MNase cleaves nearby DNA, releasing fragments without crosslinking or sonication. The original protocol required ~100,000 cells minimum for ChIP-quality TF maps.
2. **uliCUT&RUN modifications**: altered buffers, sample volumes, incubation times, spike-in DNA quantities, and library-prep + purification methods. Two biological replicates per condition.
3. Validated across **a titration: 500,000 → 50,000 → 5,000 → 500 → 50 → 10 cells**, with IgG no-antibody controls at each cell number.
4. Single-cell experiments: 120 individual mESCs profiled for CTCF, 26 each for SOX2 and NANOG, with 47 no-antibody control single cells.
5. Pre-implantation embryo experiments: individual mouse blastocysts profiled for CTCF; BRG1 (Smarca4) depletion by zygote-injected esiRNA followed by uliCUT&RUN for NANOG at early blastocyst stage.

## Key claims

1. **uliCUT&RUN profiles CTCF binding from as few as 10 cells**: 10-cell CTCF maps identify 25–42% of established CTCF binding sites; 50-cell libraries identify 57–99%. H3K4me3 slightly less robust at very low cell numbers (23–35% at 10–50 cells; 42–94% at ≥500 cells).
2. **Broad utility across chromatin protein classes**: OCT4, SOX2, NANOG, BRG1, H3K27ac, H3K27me3, SUZ12 all profile robustly from 50-cell samples. **79–96% of established SOX2/NANOG binding sites recovered from 50-cell libraries**; 54–74% for OCT4.
3. **Single-cell TF profiling is feasible**: averaged across 120 CTCF single cells or 26 SOX2/NANOG single cells, read density at established binding sites is significantly elevated vs no-antibody controls (Mann-Whitney P < 2.2×10⁻¹⁶). DNA-sequence motif enrichment (CTCF/CTCFL motif) is significant from as few as 5 combined single-cell maps.
4. **Fractional TF occupancy is variable across single cells and predicts multi-cell ChIP-seq peak intensity**: SOX2 and NANOG binding sites in the top 20% of multi-cell ChIP-seq peak intensity (top quintile) are overrepresented in single-cell uliCUT&RUN reads. This is the **first direct test (and confirmation) of the assumption that multi-cell ChIP-seq peak intensity reflects fractional cell occupancy**.
5. **NANOG binding in mouse blastocysts depends on BRG1 in vivo** (P = 1.67×10⁻⁵), in contrast to cultured mESCs where NANOG binding is largely BRG1-independent. Suggests that initial NANOG genome binding *requires* SWI/SNF-mediated chromatin opening at the late morula/early blastocyst stage, with subsequent maintenance becoming chromatin-remodeler-independent.

## Surprising / load-bearing for the review

- **uliCUT&RUN sits at the methodological boundary** between [[cut-and-run]] (bulk) and [[scchic-seq]] / [[scicut-tag]] (combinatorial-indexing scaled single-cell TF / histone mapping). For the review's §3.4 (Chromatin State / histone & TF occupancy single-cell methods), uliCUT&RUN is the **ultra-low-input → small-population → single-cell TF mapping** anchor that predates the high-throughput sciCUT&Tag scaling.
- **The Smarca4/BRG1 in-vivo vs in-vitro NANOG-binding discrepancy** is a key methodological lesson: cultured-cell ChIP / CUT&RUN can miss requirements that are obvious in primary tissue. For mosaicism researchers using bulk-epigenome annotation reference data, the lesson is that **the chromatin context interpreting a mosaic mutation may differ between cultured-cell reference and primary-tissue reality**.
- **Not directly relevant to the planned review's somatic-mosaicism focus**, but a useful neighbor in the multi-omics + chromatin space. The wiki keeps the summary as a hub for chromatin-method coverage.

## Why this paper landed in the neuro-mosaicism batch

The filename `Sarah_2019_Cell.pdf` was tagged for this batch on the assumption of being a Walsh-lab or Lodato-style neuro-mosaicism paper. It is in fact the Fazzio-lab uliCUT&RUN method paper. **No actual single-neuron-sequencing primary papers from Lodato 2015/2018 or Evrony 2012/2015 are in the wiki yet** — those remain pending in 00-Sources for a future neuro-mosaicism batch. Bae 2018 references Lodato 2015 (ref 13) and Lodato 2018 (ref 29) as companion papers; the wiki should ingest them next.

## Entities / concepts touched

[[cut-and-run]] · [[chip-seq]] · [[transcription-factor-motif]] · [[chromatin-accessibility]] · [[scchic-seq]] · [[scicut-tag]] · [[20-Entities/steven-henikoff]] · [[40-Topics/histone-modifications]] · [[40-Topics/chromatin-architecture]]

## Related summaries

- [[10-Summaries/single-cell-chromatin-immunocleavage-sequencing-scchic-seq-to-profile-histone-modification]] — Ku/Zhao scChIC-seq.
- [[10-Summaries/scalable-single-cell-profiling-of-chromatin-modifications-with-scicut-tag]] — Janssens/Henikoff sciCUT&Tag (40k cells/chip).
- [[10-Summaries/scchix-seq-infers-dynamic-relationships-between-histone-modifications-in-single-cells]] — scChIX-seq.
