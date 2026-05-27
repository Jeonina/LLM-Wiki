---
type: concept
title: Enhancer states
aliases: [active enhancer, primed enhancer, poised enhancer]
tags: [enhancers, histone-modifications, regulatory-elements]
created: 2026-05-12
updated: 2026-05-27
---

# Enhancer states

> Distinct functional states of enhancers defined by combinations of histone modifications ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]):
> - **Active**: H3K4me1 + H3K27ac ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]])
> - **Primed**: H3K4me1 alone (no H3K27ac, no H3K27me3) ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]])
> - **Poised**: H3K4me1 + H3K27me3 (bivalent)
> - **Decommissioned**: lost H3K4me1

## Foundational source

The active-vs-inactive split was established by [[10-Summaries/creyghton-2010-h3k27ac-enhancers]] in mESC, NPC, proB, and liver. The paper showed only ~30% of H3K4me1+ enhancers carry H3K27ac, and only those drive proximal gene expression and emit eRNAs — meaning the active enhancer pool is much smaller than H3K4me1 alone suggests ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]).

## Terminology drift (historical note)

Creyghton 2010 used "**poised**" for what later literature renamed "**primed**" (H3K4me1+/H3K27ac−, no H3K27me3) ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]). In Creyghton's data only 1.2% of identified enhancers carried H3K27me3, so the "poised" class was overwhelmingly what is now called primed ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]). The modern convention reserves "poised" for the H3K27me3-bivalent class (analogous to bivalent promoters). The 4-state model above uses the modern convention.

## Why it matters

Enhancer state predicts gene-expression activity and cell-fate commitment ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]). Newer findings ([[10-Summaries/tavares-2026-6-base-cut-tag]]) add **DNA methylation as a fourth coordinate**: primed enhancers have the highest 5mC and 5hmC at H3K4me1-marked nucleosomes, distinguishing them from active and poised enhancers.

Enhancer rewiring is also part of pluripotency reprogramming: fibroblast→iPS conversion redistributes H3K4me1 patterns to the ES-cell configuration (Pearson 0.81 vs ES, vs 0.19 in parental fibroblasts) ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]).

## Related

- [[30-Concepts/histone-modifications]] · [[30-Concepts/cis-regulatory-element]] · [[30-Concepts/6-base-cut-and-tag]] · [[40-Topics/chromatin-architecture]]
- [[10-Summaries/creyghton-2010-h3k27ac-enhancers]] — foundational source for the active/poised partition
