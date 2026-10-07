---
type: concept
title: "Non-CG methylation (mCH)"
aliases: []
tags: []
created: 2026-10-07
updated: 2026-10-07
sources: ["[[10-Summaries/liu-2012-bis-snp]]", "[[10-Summaries/luo-2017-snmc-seq]]", "[[10-Summaries/rylaarsdam-2025-amethyst]]", "[[10-Summaries/spix-2025-scdeep-mc]]"]
---

# Non-CG methylation (mCH)

> Cytosine methylation outside CpG context (CA, CT, CC; mostly CAC in mammals), abundant in brain and used as a high-resolution cell-typing signal, historically treated as neuron-specific ([[10-Summaries/rylaarsdam-2025-amethyst]]).

## Key points

- mCH accumulates postnatally and is described as more subtype-specific than mCG; it was the signal that first made single-cell methylation a cell-typing modality in cortex ([[10-Summaries/luo-2017-snmc-seq]]).
- Astrocytes and oligodendrocytes carry gene-specific hyper-mCH that is anticorrelated with expression and CAC-dominated, like neurons, though only 0.1% of hyper-mCH regions in a cortex dataset were glial ([[10-Summaries/rylaarsdam-2025-amethyst]]).
- Females show hyper-mCH over X-inactivation-escape genes such as *USP9X* in neurons and ectoderm-derived glia but not in microglia ([[10-Summaries/rylaarsdam-2025-amethyst]]).
- Combining mCG and mCH features improved brain clustering over either alone (silhouette 0.67 vs 0.57/0.50) ([[10-Summaries/rylaarsdam-2025-amethyst]]).
- Bulk bisulfite genotyping tools report CH-context methylation separately; mouse frontal cortex showed elevated CpH methylation ([[10-Summaries/liu-2012-bis-snp]]).
- Random-priming scWGBS designs that assume unmethylated CpH may bias against high-mCH regions (synthesis from [[10-Summaries/spix-2025-scdeep-mc]]).

## Added 2026-10-07

In P21 mouse brain, spatial-DMT measured mCA at ~3–4% (<1% in embryos), and hippocampal genes were tied to mCG only (*Ntrk3*, *Satb1*), to both marks (*Prox1*, *Bcl11b*) or region-dependently (*Cux1*) ([[10-Summaries/cardilla-2025-spatial-methylome]]).

## Related

- [[bisulfite-sequencing]] · [[luo-2018-snmc-seq2]] · [[40-Topics/dna-methylation]]
