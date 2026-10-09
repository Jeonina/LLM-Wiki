---
type: concept
title: Enhancer states
aliases: [active enhancer, primed enhancer, poised enhancer]
tags: [enhancers, histone-modifications, regulatory-elements]
created: 2026-05-12
updated: 2026-10-09
---

# Enhancer states

> Distinct functional states of enhancers defined by combinations of histone modifications ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]):
> - **Active**: H3K4me1 + H3K27ac ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]])
> - **Primed**: H3K4me1 alone (no H3K27ac, no H3K27me3) ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]])
> - **Poised**: H3K4me1 + H3K27me3 (bivalent)
> - **Decommissioned**: lost H3K4me1

## Foundational source

The active-vs-inactive split was established by [[10-Summaries/creyghton-2010-h3k27ac-enhancers]] in mESC, NPC, proB, and liver. The paper showed only a subset of H3K4me1+ enhancers carry H3K27ac, and only those drive proximal gene expression and emit eRNAs — meaning the active enhancer pool is much smaller than H3K4me1 alone suggests ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]).

## Terminology drift (historical note)

Creyghton 2010 used "**poised**" for what later literature renamed "**primed**" (H3K4me1+/H3K27ac−, no H3K27me3) ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]). In Creyghton's data only 1.2% of identified enhancers carried H3K27me3, so the "poised" class was overwhelmingly what is now called primed ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]). The modern convention reserves "poised" for the H3K27me3-bivalent class (analogous to bivalent promoters). The 4-state model above uses the modern convention.

## Why it matters

Enhancer state predicts gene-expression activity and cell-fate commitment ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]). Newer findings ([[10-Summaries/tavares-2026-6-base-cut-tag]]) add **DNA methylation as a fourth coordinate**: primed enhancers have the highest 5mC and 5hmC at H3K4me1-marked nucleosomes, distinguishing them from active and poised enhancers.

Enhancer rewiring is also part of pluripotency reprogramming: fibroblast→iPS conversion redistributes H3K4me1 patterns to the ES-cell configuration (Pearson 0.81 vs ES, vs 0.19 in parental fibroblasts) ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]).

## The 2006–2010 vocabulary, and its population-scale confirmation

- **Bivalent (poised) promoters.** ES cells carry large H3K27me3 domains containing smaller H3K4me3 sites, 93% of them at developmental TF genes; sequential ChIP shows both marks on the same chromatin, and the domains resolve to one mark or the other on differentiation according to whether the gene is induced ([[10-Summaries/bernstein-2006-bivalent-chromatin]]).
- **Refinement**: the two marks are not on the same H3 tail but on **adjacent histones within one nucleosome**, consistent with PRC2 being unable to methylate H3K27 when H3K4me3 is present in *cis* ([[10-Summaries/rothbart-2014-histone-dna-language]]).
- **Primed enhancers.** Collaborative binding of small sets of lineage-determining TFs at closely spaced motifs displaces nucleosomes and induces H3K4me1; only ~15% of PU.1 sites drove constitutive reporter activity, while 10/11 LXR-co-bound regions were ligand-dependent — primed ≠ active ([[10-Summaries/heinz-2010-homer]]).
- **Population scale.** Enhancer/promoter signatures cover ~5% of each of 127 reference epigenomes and are enriched for evolutionarily conserved non-exonic regions; H3K4me1-associated states are the most tissue-specific, and **repressive marks carry no GWAS enrichment at all** ([[10-Summaries/roadmap-2015-111-epigenomes]]).
- **Regulatory priming persists into repressive chromatin.** Of 1,597 monocyte-specific repressive-state TSS shifts, only 16.1% have a matching transcriptional shift; the rest are silent in every cell type yet cell-type-specifically marked ([[10-Summaries/zhang-2022-sccut-tag-pro]]).

## Added 2026-10-07

Enhancer methylation is the fastest-moving compartment of the methylome in single cells. Enhancers of essentially any lineage lost methylation faster than expected under 2i, ESC-specific enhancers fastest, and the same sets regained methylation fastest during EB/ATRA differentiation ([[10-Summaries/farlik-2015-scwgbs]]).

H3K4me1 in mouse zygotes accumulates genome-wide without the enhancer and promoter enrichment seen in differentiated cells and does not correlate with expression. It is therefore not an enhancer proxy at that stage ([[10-Summaries/schwager-2026-onecell-cut-tag]]). CoBATCH used H3K27ac as an active-enhancer surrogate to find dynamic gastrulation enhancers in single E6.5–E7.75 embryos and enhancer modules in endothelial cells ([[10-Summaries/wang-2019-cobatch]]).

An earlier T-cell atlas reported all three H3K4 methylation states, H2A.Z and H3K9me1 enriched at 3,507 non-promoter, non-CTCF DNase HS sites and at known *IFNG* and *IL13* enhancers, explicitly disputing an H3K4me1-but-not-H3K4me3 enhancer signature ([[10-Summaries/barski-2007-histone-methylation-chip-seq]]).

ChromHMM applied to pseudobulk scCUT&Tag tracks of six histone marks in human PBMC recovers promoter, enhancer, repressive and heterochromatin states, with cell-type-specific differences such as broader repressive-domain coverage in monocytes ([[10-Summaries/wu-2026-sccut-tag-review]]).


## Added 2026-10-08 — sequence models & foundation models

- Basenji gradient saliency on 128 bp bins recovered ENCODE GM12878 enhancers (KS P = 2e-183) and gave signed scores, showing that promoters often contain repressive segments ([[10-Summaries/kelley-2018-basenji]])
- Sei finds enhancer sequence classes under bidirectional selection (both gains and losses of activity are depleted among common variants), unlike CTCF classes where only losses are strongly constrained ([[10-Summaries/chen-2022-sei]])
- CREsted designed cardiac and somatic-muscle enhancers by in silico evolution with an L2 target-vector cost, and all of them were specifically active in zebrafish embryos; only one of three endothelial designs was both strong and specific ([[10-Summaries/kempynck-2026-crested]]).

## Added 2026-10-09 — foundation-model gap evidence

- In T-ALL xenografts, somatic indels or ITDs reactivate a TAL1 enhancer that is open in HSCs and progenitors but closed in mature T cells, with H3K27ac on the mutant haplotype and H3K27me3 on the wild-type haplotype at the exon-4 promoter ([[10-Summaries/terekhanova-2026-tal1-enhancer]])

## Related

- [[40-Topics/histone-modifications]] · [[30-Concepts/cis-regulatory-element]] · [[30-Concepts/6-base-cut-and-tag]] · [[40-Topics/chromatin-architecture]]
- [[10-Summaries/creyghton-2010-h3k27ac-enhancers]] — foundational source for the active/poised partition
- [[10-Summaries/bernstein-2006-bivalent-chromatin]] · [[10-Summaries/heinz-2010-homer]] · [[10-Summaries/roadmap-2015-111-epigenomes]] · [[10-Summaries/zhang-2022-sccut-tag-pro]]
