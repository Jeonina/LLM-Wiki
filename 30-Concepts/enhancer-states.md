---
type: concept
title: Enhancer states
aliases: [active enhancer, primed enhancer, poised enhancer]
tags: [enhancers, histone-modifications, regulatory-elements]
created: 2026-05-12
updated: 2026-10-12
---

# Enhancer states

> Distinct functional states of enhancers — active, primed, poised and decommissioned — defined by combinations of histone modifications ([[10-Summaries/creyghton-2010-h3k27ac-enhancers|Creyghton 2010]]).

> [!abstract] 한눈에
> Enhancer는 H3K4me1, H3K27ac, H3K27me3의 조합에 따라 active, primed, poised, decommissioned 상태로 나뉘고, H3K4me1을 가진 enhancer 가운데 H3K27ac까지 가진 일부만 실제로 유전자 발현을 이끈다 ([[10-Summaries/creyghton-2010-h3k27ac-enhancers|Creyghton 2010]]). 최근에는 DNA methylation이 primed enhancer를 가르는 또 하나의 축으로 더해졌으며, "poised"라는 용어는 문헌마다 가리키는 상태가 달라 주의가 필요하다 ([[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]).

## Definition

The active-vs-inactive split was established in mESC, NPC, proB and liver: only a subset of H3K4me1+ enhancers carry H3K27ac, and only those drive proximal gene expression and emit eRNAs, so the active enhancer pool is much smaller than H3K4me1 alone suggests ([[10-Summaries/creyghton-2010-h3k27ac-enhancers|Creyghton 2010]]).

**Terminology drift.** Creyghton 2010 used "**poised**" for what later literature renamed "**primed**" (H3K4me1+/H3K27ac−, no H3K27me3) ([[10-Summaries/creyghton-2010-h3k27ac-enhancers|Creyghton 2010]]). In Creyghton's data only 1.2% of identified enhancers carried H3K27me3, so the "poised" class was overwhelmingly what is now called primed ([[10-Summaries/creyghton-2010-h3k27ac-enhancers|Creyghton 2010]]). The modern convention reserves "poised" for the H3K27me3-bivalent class (analogous to bivalent promoters); the four-state table below uses the modern convention.

## Why it matters

- Enhancer state predicts gene-expression activity and cell-fate commitment ([[10-Summaries/creyghton-2010-h3k27ac-enhancers|Creyghton 2010]]).
- **DNA methylation is a fourth coordinate**: primed enhancers have the highest 5mC and 5hmC at H3K4me1-marked nucleosomes, distinguishing them from active and poised enhancers ([[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]).
- Enhancer rewiring is part of pluripotency reprogramming: fibroblast→iPS conversion redistributes H3K4me1 patterns to the ES-cell configuration (Pearson 0.81 vs ES, against 0.19 in parental fibroblasts) ([[10-Summaries/creyghton-2010-h3k27ac-enhancers|Creyghton 2010]]).

## The four states

| State | Marks | Source |
|---|---|---|
| Active | H3K4me1 + H3K27ac | ([[10-Summaries/creyghton-2010-h3k27ac-enhancers\|Creyghton 2010]]) |
| Primed | H3K4me1 alone (no H3K27ac, no H3K27me3); highest 5mC/5hmC at H3K4me1-marked nucleosomes | ([[10-Summaries/creyghton-2010-h3k27ac-enhancers\|Creyghton 2010]]; [[10-Summaries/tavares-2026-6-base-cut-tag\|Tavares 2026]]) |
| Poised | H3K4me1 + H3K27me3 (bivalent) | — |
| Decommissioned | Lost H3K4me1 | — |

## Reading enhancer state

### Histone marks and the origins of the vocabulary

- **Bivalent (poised) promoters.** ES cells carry large H3K27me3 domains containing smaller H3K4me3 sites, 93% of them at developmental TF genes; sequential ChIP shows both marks on the same chromatin, and the domains resolve to one mark or the other on differentiation according to whether the gene is induced ([[10-Summaries/bernstein-2006-bivalent-chromatin|Bernstein 2006]]).
- **Refinement of bivalency.** The two marks are not on the same H3 tail but on **adjacent histones within one nucleosome**, consistent with PRC2 being unable to methylate H3K27 when H3K4me3 is present in *cis* ([[10-Summaries/rothbart-2014-histone-dna-language|Rothbart & Strahl 2014]]).
- **Primed enhancers.** Collaborative binding of small sets of lineage-determining TFs at closely spaced motifs displaces nucleosomes and induces H3K4me1 ([[10-Summaries/heinz-2010-homer|Heinz 2010]]).
- **H3K27ac as an active-enhancer surrogate.** CoBATCH used H3K27ac to find dynamic gastrulation enhancers in single E6.5–E7.75 embryos and enhancer modules in endothelial cells ([[10-Summaries/wang-2019-cobatch|CoBATCH]]).
- **Chromatin-state segmentation.** Enhancer/promoter signatures cover ~5% of each of 127 reference epigenomes ([[10-Summaries/roadmap-2015-111-epigenomes|Roadmap 2015]]). ChromHMM applied to pseudobulk scCUT&Tag tracks of six histone marks in human PBMC recovers promoter, enhancer, repressive and heterochromatin states, with cell-type-specific differences such as broader repressive-domain coverage in monocytes ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).

### DNA methylation

- Primed enhancers carry the highest 5mC and 5hmC at H3K4me1-marked nucleosomes ([[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]).
- Enhancer methylation is the fastest-moving compartment of the methylome in single cells ([[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]).

### Sequence models

- Basenji gradient saliency on 128 bp bins recovered ENCODE GM12878 enhancers (KS P = 2e-183) and gave signed scores, showing that promoters often contain repressive segments ([[10-Summaries/kelley-2018-basenji|Basenji]]).
- Sei finds enhancer sequence classes under bidirectional selection ([[10-Summaries/chen-2022-sei|Sei]]).
- CREsted designs enhancers by in silico evolution with an L2 target-vector cost ([[10-Summaries/kempynck-2026-crested|CREsted]]).

## Evidence and examples

- Only ~15% of PU.1 sites drove constitutive reporter activity, while 10/11 LXR-co-bound regions were ligand-dependent — primed is not active ([[10-Summaries/heinz-2010-homer|Heinz 2010]]).
- Across 127 reference epigenomes, enhancer/promoter states are enriched for evolutionarily conserved non-exonic regions, H3K4me1-associated states are the most tissue-specific, and **repressive marks carry no GWAS enrichment at all** ([[10-Summaries/roadmap-2015-111-epigenomes|Roadmap 2015]]).
- **Regulatory priming persists into repressive chromatin.** Of 1,597 monocyte-specific repressive-state TSS shifts, only 16.1% have a matching transcriptional shift; the rest are silent in every cell type yet cell-type-specifically marked ([[10-Summaries/zhang-2022-sccut-tag-pro|Zhang 2022]]).
- Enhancers of essentially any lineage lost methylation faster than expected under 2i, ESC-specific enhancers fastest, and the same sets regained methylation fastest during EB/ATRA differentiation ([[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]).
- Both gains and losses of activity in Sei's enhancer sequence classes are depleted among common variants, unlike CTCF classes where only losses are strongly constrained ([[10-Summaries/chen-2022-sei|Sei]]).
- CREsted's designed cardiac and somatic-muscle enhancers were all specifically active in zebrafish embryos; only one of three endothelial designs was both strong and specific ([[10-Summaries/kempynck-2026-crested|CREsted]]).
- In T-ALL xenografts, somatic indels or ITDs reactivate a TAL1 enhancer that is open in HSCs and progenitors but closed in mature T cells, with H3K27ac on the mutant haplotype and H3K27me3 on the wild-type haplotype at the exon-4 promoter ([[10-Summaries/terekhanova-2026-tal1-enhancer|Terekhanova 2026]]).

## Contested points

- **"Poised" means different things in different papers.** Creyghton 2010's "poised" class is mostly what is now called primed; only 1.2% of its enhancers carried H3K27me3 ([[10-Summaries/creyghton-2010-h3k27ac-enhancers|Creyghton 2010]]). Older papers need to be read with this in mind before comparing class sizes (synthesis).
- **Is H3K4me1-without-H3K4me3 an enhancer signature?** An earlier T-cell atlas reported all three H3K4 methylation states, H2A.Z and H3K9me1 enriched at 3,507 non-promoter, non-CTCF DNase HS sites and at known *IFNG* and *IL13* enhancers, explicitly disputing an H3K4me1-but-not-H3K4me3 enhancer signature ([[10-Summaries/barski-2007-histone-methylation-chip-seq|Barski 2007]]).
- **H3K4me1 is not an enhancer proxy in the zygote.** In mouse zygotes H3K4me1 accumulates genome-wide without the enhancer and promoter enrichment seen in differentiated cells and does not correlate with expression ([[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/cis-regulatory-element|Cis-regulatory element]] — Non-coding DNA regions such as enhancers and promoters that control gene expression through TF binding.
> - `concept` [[30-Concepts/6-base-cut-and-tag|6-base CUT&Tag]] — Joint histone-mark and 5mC/5hmC profiling; the source of the methylation coordinate.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone-tail modifications that demarcate functional chromatin states.
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — How DNA is packaged along chromosomes and how that varies across fibers, haplotypes and cells.

## All sources on this page

> [!info]- 16 summaries cited here
> - [[10-Summaries/barski-2007-histone-methylation-chip-seq|Barski 2007]]
> - [[10-Summaries/bernstein-2006-bivalent-chromatin|Bernstein 2006]]
> - [[10-Summaries/chen-2022-sei|Sei 2022]]
> - [[10-Summaries/creyghton-2010-h3k27ac-enhancers|Creyghton 2010]]
> - [[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]
> - [[10-Summaries/heinz-2010-homer|Heinz 2010]]
> - [[10-Summaries/kelley-2018-basenji|Basenji 2018]]
> - [[10-Summaries/kempynck-2026-crested|CREsted 2026]]
> - [[10-Summaries/roadmap-2015-111-epigenomes|Roadmap Epigenomics 2015]]
> - [[10-Summaries/rothbart-2014-histone-dna-language|Rothbart & Strahl 2014]]
> - [[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]
> - [[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]
> - [[10-Summaries/terekhanova-2026-tal1-enhancer|Terekhanova 2026]]
> - [[10-Summaries/wang-2019-cobatch|Wang 2019]]
> - [[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]
> - [[10-Summaries/zhang-2022-sccut-tag-pro|Zhang 2022]]
