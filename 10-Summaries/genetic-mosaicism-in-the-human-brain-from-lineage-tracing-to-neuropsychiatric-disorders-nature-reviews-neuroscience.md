---
type: summary
title: "Bizzotto & Walsh 2022 — Genetic mosaicism in the human brain: lineage tracing and neuropsychiatric disease"
source: "[[00-Sources/papers/Genetic mosaicism in the human brain_ from lineage tracing to neuropsychiatric disorders - Nature Reviews Neuroscience]]"
source_kind: paper
author: "Sara Bizzotto, Christopher A. Walsh (corresponding)"
published: 2022-03-23
ingested: 2026-05-12
doi: "10.1038/s41583-022-00572-x"
journal: "Nature Reviews Neuroscience"
tags: [review, brain-mosaicism, lineage-tracing, FCD, ASD, somatic-SNVs, neurodevelopment]
entities:
  - "[[20-Entities/sara-bizzotto]]"
  - "[[20-Entities/christopher-walsh]]"
concepts:
  - "[[30-Concepts/somatic-mosaicism]]"
  - "[[30-Concepts/lineage-tracing]]"
  - "[[30-Concepts/post-zygotic-variation]]"
  - "[[30-Concepts/focal-cortical-dysplasia]]"
  - "[[30-Concepts/autism-spectrum-disorder]]"
  - "[[30-Concepts/mtor-pathway]]"
  - "[[30-Concepts/mitochondrial-lineage-tracing]]"
topics:
  - "[[40-Topics/somatic-mosaicism]]"
  - "[[40-Topics/scdna-seq]]"
---

# Bizzotto & Walsh 2022 — Genetic mosaicism in the human brain

> Thesis: Somatic mutations begin from the first post-zygotic division, accumulate at gradient rates through development and aging, and turn the adult human brain into a **clonal mosaic of intermingled lineages** traceable back to the early embryo. These mosaic variants are simultaneously (a) a natural barcoding system for retrospective lineage tracing in humans and (b) drivers of focal cortical malformations and a contributor to autism spectrum disorder.

## Key claims

- **Mutation-rate gradient through development**: ~2.4–3.4 SNVs per cell across each of the first two postzygotic divisions; rate drops to ~1–2/division from the 8-cell stage. Neural progenitors at gestational week 20 carry 200–300 SNVs each (~5.1/day, ~8.6/division). Postmitotic neurons accumulate 15–20 SNVs/year, reaching 2,500–4,000 SNVs/genome in 80-year-olds. NanoSeq and PTA give concordant rates.
- **Asymmetric inheritance from the early embryo**: the two daughters of the zygote contribute 50:50–93:7 (variable across tissues and individuals) to the brain. About 50–100 founder neuroectoderm progenitors give rise to the human forebrain; ~170 epiblast cells at gastrulation onset.
- **Lineage tracing in humans is feasible via developmental SNVs as natural barcodes**: early variants span the whole cortex; later variants restrict to single lobes; some clones are spatially confined to <2 cm patches. PRDD-seq combines targeted DNA variant calling with subset-gene RNA expression to assign clones to excitatory vs inhibitory neuron lineages.
- **Mutation signatures change over time**: SBS1 (CpG → TpG via 5mC deamination) dominates early; SBS5 (clock-like) dominates in aging neurons; oxidative-damage C>A transversions appear later in neural progenitors.
- **Pathogenic mosaicism**: gain-of-function mTOR-pathway SNVs (AKT3, PIK3CA, RHEB, MTOR) plus loss-of-function in TSC1/2, DEPDC5, PTEN, NPRL2/3 cause FCD type 2 / HME (50–60% of these cases). Excitatory-neuron-restricted Pik3ca^H1047R causes severe cortical phenotype; inhibitory-restricted does not — the **cell type carrying the mutation matters as much as the mutation itself**. ASD: somatic SNVs and large mosaic CNVs contribute to risk in ~5% of probands.

## Methods / evidence

Authoritative review. Synthesizes ~150 references including the lab's own deep-WGS work on >70 individual brains, PRDD-seq, retrospective lineage trees from MDA/PTA/MEDA-cs/NanoSeq, FCD/HME mosaic-variant landscape papers, and the Sci-LIANTI/mtscATAC-seq/EMBLEM future-direction methods.

## Surprising or load-bearing bits

- The framing that **GM is a natural human barcoding system** is the conceptual through-line. It positions retrospective single-cell genomics as a way to do in humans what CRISPR scarring does in zebrafish/mouse.
- The variability of zygotic asymmetry (50:50 to 93:7) is a striking insight from population-scale mosaic data.
- The cell-type-restricted FCD phenotype experiments (Emx1-Cre vs Nkx2.1-Cre) demonstrate that mTOR mosaicism in excitatory neurons is what drives megalencephaly.

## Connections to other sources

- Direct conceptual ancestor of [[10-Summaries/a-comprehensive-view-of-somatic-mosaicism-by-single-cell-dna-analysis]] — Walsh is co-senior on both. The SMaHT comprehensive-view paper operationalizes the mosaicism framework for non-brain tissues.
- Extends [[10-Summaries/diane-2025-naturereviewsgenetics]] (Shao/Walsh 2025 in scDNA-seq methods) on the biology side.
- Connects [[10-Summaries/lars-2017-naturereviewsgenetics]] (Forsberg mosaicism in health/disease) and [[10-Summaries/ian-2015-trendsingenetics]] (Campbell/Lupski transmission genetics).

## Open questions

- ASD: what fraction of risk comes from intronic/intergenic somatic variants invisible to exome sequencing? Recent deep-WGS suggests an excess of mosaic mutations in brain-active enhancers in ASD brains, but cohort size is the limit.
- Lineage tracing remains expensive: WGS of thousands of cells is prohibitive; targeted approaches (Sci-LIANTI, EMBLEM/mtscATAC) trade depth for breadth.

## Related

- [[40-Topics/somatic-mosaicism]] · [[30-Concepts/lineage-tracing]] · [[30-Concepts/focal-cortical-dysplasia]] · [[30-Concepts/autism-spectrum-disorder]] · [[20-Entities/christopher-walsh]]
