---
type: concept
title: "Non-CG methylation (mCH)"
aliases: []
tags: []
created: 2026-10-07
updated: 2026-10-12
sources: ["[[10-Summaries/liu-2012-bis-snp]]", "[[10-Summaries/luo-2017-snmc-seq]]", "[[10-Summaries/rylaarsdam-2025-amethyst]]", "[[10-Summaries/spix-2025-scdeep-mc]]"]
---

# Non-CG methylation (mCH)

> Cytosine methylation outside CpG context (CA, CT, CC; mostly CAC in mammals), abundant in brain and used as a high-resolution cell-typing signal, historically treated as neuron-specific ([[10-Summaries/rylaarsdam-2025-amethyst|Amethyst]]).

> [!abstract] 한눈에
> mCH는 CpG 밖(CA, CT, CC)의 cytosine methylation으로 뇌에 많고, 출생 후 쌓이며 mCG보다 세포 아형을 더 잘 구분해 single-cell methylation을 cell typing 도구로 만든 신호다 ([[10-Summaries/luo-2017-snmc-seq|Luo 2017]]). 오랫동안 neuron 특이적이라고 여겨졌지만 astrocyte와 oligodendrocyte에서도 유전자 특이적 hyper-mCH가 보인다 ([[10-Summaries/rylaarsdam-2025-amethyst|Amethyst]]).

## Definition

Non-CG methylation is cytosine methylation in CA, CT or CC context, mostly CAC in mammals ([[10-Summaries/rylaarsdam-2025-amethyst|Amethyst]]). mCH accumulates postnatally and is described as more subtype-specific than mCG ([[10-Summaries/luo-2017-snmc-seq|Luo 2017]]).

## Why it matters

- mCH was the signal that first made single-cell methylation a cell-typing modality in cortex ([[10-Summaries/luo-2017-snmc-seq|Luo 2017]]).
- Combining mCG and mCH features improved brain clustering over either alone (silhouette 0.67 vs 0.57/0.50) ([[10-Summaries/rylaarsdam-2025-amethyst|Amethyst]]).

## Measurement

- Bulk bisulfite genotyping tools report CH-context methylation separately; mouse frontal cortex showed elevated CpH methylation ([[10-Summaries/liu-2012-bis-snp|Bis-SNP]]).
- Random-priming scWGBS designs that assume unmethylated CpH may bias against high-mCH regions (synthesis from [[10-Summaries/spix-2025-scdeep-mc|scDEEP-mC]]).
- Spatial-DMT measures mCA alongside mCG in tissue sections ([[10-Summaries/cardilla-2025-spatial-methylome|Lee 2025]]).

## Evidence and examples

- Astrocytes and oligodendrocytes carry gene-specific hyper-mCH that is anticorrelated with expression and CAC-dominated, like neurons, though only 0.1% of hyper-mCH regions in a cortex dataset were glial ([[10-Summaries/rylaarsdam-2025-amethyst|Amethyst]]).
- Females show hyper-mCH over X-inactivation-escape genes such as *USP9X* in neurons and ectoderm-derived glia but not in microglia ([[10-Summaries/rylaarsdam-2025-amethyst|Amethyst]]).
- In P21 mouse brain, spatial-DMT measured mCA at ~3–4% (<1% in embryos) ([[10-Summaries/cardilla-2025-spatial-methylome|Lee 2025]]).
- Hippocampal genes were tied to mCG only (*Ntrk3*, *Satb1*), to both marks (*Prox1*, *Bcl11b*) or region-dependently (*Cux1*) ([[10-Summaries/cardilla-2025-spatial-methylome|Lee 2025]]).

## Contested points

- **Neuron-specific or not.** mCH has historically been treated as neuron-specific, yet glia carry gene-specific hyper-mCH, though only 0.1% of hyper-mCH regions in a cortex dataset were glial ([[10-Summaries/rylaarsdam-2025-amethyst|Amethyst]]).
- **Assay bias.** Primer designs that assume unmethylated CpH may under-sample exactly the high-mCH regions this signal is used for (synthesis from [[10-Summaries/spix-2025-scdeep-mc|scDEEP-mC]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/bisulfite-sequencing|Bisulfite sequencing]] — Conversion chemistry that reads CG and CH methylation.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — Methylation chemistry, assays and analysis.

See also the single-cell methylome protocol snmC-seq2 ([[10-Summaries/luo-2018-snmc-seq2|Luo 2018]]).

## All sources on this page

> [!info]- 6 summaries cited here
> - [[10-Summaries/cardilla-2025-spatial-methylome|Lee 2025]]
> - [[10-Summaries/liu-2012-bis-snp|Liu 2012]]
> - [[10-Summaries/luo-2017-snmc-seq|Luo 2017]]
> - [[10-Summaries/luo-2018-snmc-seq2|Luo 2018]]
> - [[10-Summaries/rylaarsdam-2025-amethyst|Rylaarsdam 2025]]
> - [[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]
