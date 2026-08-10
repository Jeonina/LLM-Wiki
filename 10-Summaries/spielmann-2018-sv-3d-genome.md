---
type: summary
title: "Spielmann, Lupiáñez & Mundlos 2018 — Structural variation in the 3D genome"
source: "[[00-Sources/papers/Structural variation in the 3D genome - Nature Reviews Genetics]]"
source_kind: paper
author: "Malte Spielmann, Darío G. Lupiáñez, Stefan Mundlos (corresponding)"
published: 2018-04-24
ingested: 2026-08-10
doi: "10.1038/s41576-018-0007-0"
journal: "Nature Reviews Genetics"
tags: [structural-variation, TAD, enhancer-hijacking, neo-TAD, TAD-shuffling, position-effect, clinical-interpretation, review]
entities: []
concepts: ["[[structural-variants]]", "[[topologically-associating-domain]]", "[[cis-regulatory-element]]", "[[enhancer-states]]", "[[single-cell-hi-c]]", "[[highly-repetitive-regions]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]", "[[cancer-clonal-evolution]]"]
---

**Citation:** Spielmann, Lupiáñez & Mundlos (2018) — *Structural variation in the 3D genome* — *Nature Reviews Genetics* 19, 453–467. [DOI](https://doi.org/10.1038/s41576-018-0007-0)

# Spielmann 2018 — SV in three dimensions

> The framework paper that generalizes [[lupianez-2015-tad-disruption|the *EPHA4* result]] into a clinical taxonomy: SVs must be classified not by size or copy-number change but by **their position relative to TAD boundaries**, because that determines whether they alter gene dosage, enhancer dosage, or the 3D regulatory architecture itself.

## Key claims

- SV = deletions, duplications, inversions, insertions, translocations; **CNV is the unbalanced subset**. Balanced rearrangements change no genetic material and are the hardest to interpret.
- Detection is the bottleneck: array CGH has low resolution, cannot see balanced events, and has "low efficacy in mosaic individuals"; short-read WGS misses breakpoints in repetitive regions where breakpoints preferentially occur; long reads solve this but were then too expensive for routine use.
- **>30,000 SVs per human genome** using all current methods, yet the de novo SV rate is unknown and estimates disagree wildly: ~0.16/generation (Genome of the Netherlands), 0.092/generation (476 ASD quartets), 0.05 (~50 quartets), versus 70–100 de novo SNVs per generation. Three studies using the *same* ASD dataset reached three different conclusions about non-coding SV contribution.
- The taxonomy that organizes the review:
  - **Intra-TAD SVs** → change *enhancer dosage*. Deletions cause tissue-specific loss of function (*SOX9*, *DLX5/6*, *ATOH7*, *PAX6*); duplications cause overexpression/misexpression (*IHH* duplications → craniosynostosis by overexpression, synpolydactyly by misexpression). **No pathogenic intra-TAD inversion has been described.**
  - **TAD fusion** (deletion crossing a boundary) → ectopic enhancer–promoter contact. *EPHA4*; and in T-ALL, recurrent microdeletions of CTCF boundaries activate proto-oncogenes, with CRISPR deletion in non-malignant cells sufficient to reproduce activation.
  - **Neo-TADs** (duplication spanning a boundary) → a new insulated domain. *SOX9*/*KCNJ2* Cooks syndrome: the duplicated *Kcnj2* enters a neo-TAD with duplicated *Sox9* enhancers. A slightly smaller duplication also forms a neo-TAD but causes nothing, because no gene is inside it.
  - **TAD shuffling** (inversion/translocation) → enhancer adoption plus regulatory loss of function, often simultaneously.
- Frequency is phenotype-specific: enhancer hijacking in cancer may be "comparable to recurrent in-frame gene fusions"; ~7% of balanced translocations in neurodevelopmental disorders disrupt TADs; **57% of congenital limb malformation CNVs act through cis-regulatory position effects**.
- Enhancer redundancy is the norm: the *IHH* landscape has nine overlapping enhancers; individual deletions give variable partial loss, duplications give tissue-specific gain. Redundancy means heterozygous loss of single enhancers is often tolerated — which raises the bar for calling a non-coding deletion pathogenic.
- Boundary deletion is **not universally sufficient**: deleting only the boundary and its CTCF sites at *Sox9* had no major effect. TAD stability does not rest on boundaries alone.
- Enhancer–promoter insulation is not absolute — the *SHH* ZRS enhancer can act across a boundary when genomic distance is reduced enough.
- TAD calling itself is unstable: identification "relies heavily on computational methods, which display a high degree of variation depending on the resolution and the adjustment of thresholds," and substantial genome regions have no detectable TADs.

## Methods / evidence

Review. Its distinctive value is a clinical-interpretation workflow (their Fig. 6) and unusual candor about what does not work: five explicit remaining challenges — insufficient SV detection and breakpoint resolution, scattered databases, limited knowledge of the non-coding genome, inadequate prediction tools, and low clinical awareness of 3D position effects "leaving many patients without a diagnosis."

## Surprising or load-bearing bits

- **Array CGH has "low efficacy in mosaic individuals."** Stated in passing, but it is the sentence that connects this review to this wiki: somatic/mosaic SV is under-ascertained by the standard clinical technology, which is a direct argument for single-cell SV methods ([[falconer-2012-natmethods|Strand-seq]], [[sanders-2020-sctrip|scTRIP]]).
- The de novo SV rate disagreement — three analyses, one dataset, three answers — is a caution that generalizes: SV calling is method-dependent enough that rate estimates are not comparable across pipelines. Somatic SV rates in single cells inherit this problem in worse form.
- **Same phenotype from opposite variant classes** (duplication ≡ inversion in F-syndrome; duplication ≡ deletion in polydactyly) breaks the intuition that copy-number direction predicts effect.
- The "minimal critical region" approach — standard clinical practice — is declared **insufficient**: overlapping *SOX9* duplications produce completely unrelated phenotypes depending on size, content and position.
- CESAM (cis-expression structural alteration mapping) combining expression + WGS + domain context found recurrent *SNCAIP* SVs driving *PRDM6* overexpression in 491 medulloblastomas — an enhancer-hijacking screen at cohort scale. This is the closest thing in the corpus to a systematic somatic enhancer-hijacking method.
- Patient fibroblasts recapitulate developmental TAD disruptions because 60–70% of TADs are invariant across cell types — making 3C a retrospective diagnostic on inaccessible developmental events.

## Concepts touched

- [[structural-variants]] — the intra-TAD / TAD-fusion / neo-TAD / TAD-shuffling taxonomy belongs on this page.
- [[topologically-associating-domain]] — adds the honest caveats: TAD calls are threshold-dependent, insulation is not absolute, boundaries are not the only determinant of domain stability.
- [[highly-repetitive-regions]] — breakpoints preferentially occur where short reads fail.
- [[single-cell-hi-c]] — the review notes microscopy methods are "limited to the study of selected genomic regions in single cells" while 3C methods are population averages; the gap between them is what single-cell Hi-C occupies.

## Connections to other sources

- Generalizes [[lupianez-2015-tad-disruption]] (same senior author) from one locus to a framework.
- Answers the interpretive gap posed by [[eichler-2007-completing-sv-map]]: the 2007 proposal said we need sequence-resolved SV; this says we also need domain context to read it.
- [[naumova-2013-mitotic-chromosome]] constrains the mechanism — TADs are interphase-only, so position effects operate on a structure rebuilt every cycle.
- Long-read SV resolution: [[liu-2025-nanopore-lscc-svs]], [[nanda-2024-smrt-tag]].
- Cites [[roadmap-2015-111-epigenomes]] as the enhancer-annotation substrate.

## Open questions

- **Somatic** SV in the 3D genome at single-cell resolution is essentially absent — the review's cancer examples are all bulk-cohort. Whether subclonal enhancer hijacking exists and at what frequency is open; relevant to [[cancer-clonal-evolution]] and tracked at [[open-questions]].
- The review's own conclusion that intra-TAD inversions have never been shown pathogenic is a stated gap, not a settled negative — inversions are simply the hardest class to detect.
- TAD-call instability means "SV crosses a boundary" is itself a threshold-dependent judgment. No source here quantifies how often reclassification flips clinical interpretation.

## Related

- [[lupianez-2015-tad-disruption]] · [[structural-variants]] · [[topologically-associating-domain]] · [[3d-genome]]
