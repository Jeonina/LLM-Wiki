---
type: summary
title: "Creyghton 2010 — H3K27ac separates active from poised enhancers and predicts developmental state"
source: "[[00-Sources/papers/Histone H3K27ac separates active from poised enhancers and predicts developmental state]]"
source_kind: paper
author: Menno P. Creyghton, Albert W. Cheng, G. Grant Welstead, Tristan Kooistra, Bryce W. Carey, Eveline J. Steine, Jacob Hanna, Michael A. Lodato, Garrett M. Frampton, Phillip A. Sharp, Laurie A. Boyer, Richard A. Young, Rudolf Jaenisch (corresponding)
published: 2010-10-26
ingested: 2026-05-27
doi: "10.1073/pnas.1016071107"
journal: "PNAS"
tags: [h3k27ac, h3k4me1, enhancers, chip-seq, mESC, ipsc, foundational]
entities: ["[[20-Entities/menno-p-creyghton]]", "[[20-Entities/rudolf-jaenisch]]", "[[20-Entities/richard-a-young]]"]
concepts: ["[[30-Concepts/enhancer-states]]", "[[30-Concepts/histone-modifications]]", "[[30-Concepts/chip-seq]]", "[[30-Concepts/cis-regulatory-element]]"]
topics: ["[[40-Topics/histone-modifications]]", "[[40-Topics/chromatin-architecture]]"]
---

**Citation:** Creyghton et al. (2010) — *Histone H3K27ac separates active from poised enhancers and predicts developmental state* — *PNAS* 107(50): 21931–21936. [DOI](https://doi.org/10.1073/pnas.1016071107)

# Creyghton 2010 — H3K27ac as the active-enhancer mark

> Foundational ChIP-seq paper establishing **H3K27ac as the discriminating mark between active and poised enhancers**. Prior work used H3K4me1 alone to call enhancers, but only a subset of H3K4me1+ regions drove gene expression. Creyghton et al. show that adding H3K27ac partitions H3K4me1+ enhancers into an *active* class (H3K4me1+/H3K27ac+) whose proximal genes are upregulated and emit eRNAs, and a *poised* class (H3K4me1+/H3K27ac−) whose genes await activation. The framework predicts both current and future developmental state and shows enhancers are reset to an ES-like configuration during iPS reprogramming.

## Key claims

1. **H3K27ac discriminates active from inactive enhancers.** Among ~25,000 H3K4me1-marked distal regions in mouse ES cells, only H3K27ac+ ones correlate with elevated proximal gene expression (p = 1.0E-5); H3K27ac− regions show no expression boost above average. eRNA production tracks H3K27ac+ regardless of H3K4me1 enrichment (p = 1E-154).
2. **The active enhancer pool is smaller than previously believed.** H3K4me1 alone over-counted enhancers; only ~30% are H3K27ac+. The "active global enhancer network of a cell is smaller than previously anticipated."
3. **Generalizes across cell types.** Pattern holds in mESC, neural progenitors (NPCs), proB cells, and adult liver. Across 4 cell types, ~94,437 H3K4me1+ regions and ~40,274 H3K27ac+ distal regions were identified with strong cell-type specificity (Pearson correlations 0.01–0.19 across types).
4. **Poised enhancers predict future fate.** In NPCs, H3K4me1+/H3K27ac− enhancers GO-annotate adult-neuron functions (synaptic transmission, neurotransmitter receptors), while H3K27ac+ enhancers annotate progenitor functions (anatomical structure development). 361 ES-cell poised enhancers gain H3K27ac specifically in NPCs (not liver/proB) and activate proximal genes like Neuroglycan-C and Neurophilin-2.
5. **Reprogramming resets enhancer state.** Fibroblast→iPS conversion redistributes H3K4me1 to ES-like patterns (Pearson 0.81 vs ES) compared to parental fibroblasts (0.19) — enhancer rewiring is part of pluripotency acquisition.
6. **Oct4/Sox2 mark inactive enhancers.** In mESCs, Oct4-bound (p = 0.008) and Sox2-bound (p = 0.002) enhancers correlate with *lower* proximal gene expression, suggesting these pluripotency TFs help keep developmental enhancers poised — analogous to Polycomb at bivalent promoters, but without H3K27me3 enrichment.

## Methods / evidence

ChIP-seq for H3K4me1, H3K4me3, H3K27ac, H3K27me3, p300, Oct4, Sox2, Klf4, Nanog, Foxa2, PU.1, Rfx1 across mESC (C57BL6/N), proB cells, NPCs, adult liver, fibroblasts, and Jaenisch-lab iPSCs (GA2X sequencer; antibodies Abcam ab8580, ab8895, ab4729). Microarray expression in duplicate for proximal gene calls. Validation against published H3K4me1 in 129/C57BL6 F1 ES cells (Meissner 2008) — Pearson 0.76, demonstrating reproducibility. Data deposited at GEO (GSE24164, GSE24165, GSE23907).

## Surprising or load-bearing bits

- **The terminology trap.** Creyghton's "poised" = H3K4me1+/H3K27ac−. In later literature, "poised" was reserved for H3K4me1+/H3K27me3+ (bivalent) enhancers and the H3K4me1+-only class was renamed **"primed."** The wiki's [[30-Concepts/enhancer-states]] uses the later convention. Creyghton found *no* H3K27me3 enrichment at most of these H3K27ac− enhancers (only 1.2% of identified enhancers carry H3K27me3) — so their "poised" class is mostly what we now call primed, not bivalent.
- **Oct4/Sox2 as enhancer brakes.** Strikingly counter-intuitive that the master pluripotency TFs would mark *less-active* enhancers. The paper suggests they function as Polycomb-like keepers, holding developmental enhancers in standby — but the mechanism is not H3K27me3-mediated, which leaves the standby mechanism unspecified.
- **iPS enhancer reset (Pearson 0.81 vs ES).** This was important early evidence that pluripotency reprogramming is not just transcriptional but rewires the entire enhancer landscape. The iPS line tested is the Wernig/Jaenisch tetraploid-competent line — the gold standard at the time.
- **eRNA confirmation.** The fact that short bidirectional RNAs are specifically produced at H3K27ac+ enhancers (citing Seila 2008, Kim 2010) was contemporaneous evidence that "active enhancer" wasn't a circular ChIP-mark definition — these regions are transcriptionally engaged.

## Entities mentioned

- [[20-Entities/menno-p-creyghton]] — first author, Jaenisch lab postdoc at the time
- [[20-Entities/rudolf-jaenisch]] — corresponding author, Whitehead/MIT; iPS reprogramming pioneer
- [[20-Entities/richard-a-young]] — co-author; subsequent super-enhancer concept builds on this framework

## Concepts touched

- [[30-Concepts/enhancer-states]] — this paper *defines* the operational distinction; the wiki's current 4-state model extends it
- [[30-Concepts/histone-modifications]] — establishes H3K27ac as the canonical active-enhancer mark
- [[30-Concepts/chip-seq]] — methodology
- [[30-Concepts/cis-regulatory-element]] — enhancers are the central CRE class here

## Connections to other sources

- **Extends** Heintzman 2009 *Nature* (H3K4me1 as enhancer mark) by adding the activity dimension.
- **Foundational for** later super-enhancer work (Whyte/Hnisz/Young 2013, *Cell*) which uses H3K27ac density to define super-enhancers — not yet ingested.
- **Used by** the wiki's chromatin-state vocabulary throughout: see [[10-Summaries/klemm-2019-chromatin-accessibility-review]] for the mature 4-state model, and [[10-Summaries/tavares-2026-6-base-cut-tag]] for the recent extension adding 5mC/5hmC as a fourth coordinate distinguishing primed from active.
- **Mirrors** the Polycomb/bivalent-promoter logic (Bernstein 2006, *Cell*) — the same "marked but inactive" pattern was already known for promoters; Creyghton extends it to enhancers.

## Open questions

- What holds Oct4/Sox2-marked enhancers in standby if not H3K27me3? The paper raises this but does not resolve it. Later DNA-methylation-based enhancer-priming work (e.g., the 6-base-CUT&Tag finding that primed enhancers have the highest 5mC and 5hmC) may partially answer this.
- The 30% active fraction is a 2010 estimate from bulk ChIP-seq. How does this hold up under single-cell histone profiling (scCUT&Tag, scChIC, scEpi²-seq) where enhancer activity may be more heterogeneous across cells than the bulk average suggests?

## Related

- [[30-Concepts/enhancer-states]] · [[30-Concepts/histone-modifications]] · [[30-Concepts/chip-seq]]
- [[40-Topics/histone-modifications]] · [[40-Topics/chromatin-architecture]]
- [[10-Summaries/klemm-2019-chromatin-accessibility-review]] — modern synthesis of the enhancer-state framework
- [[10-Summaries/tavares-2026-6-base-cut-tag]] — adds 5mC/5hmC as a fourth coordinate on primed vs active
