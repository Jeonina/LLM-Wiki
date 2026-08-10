---
type: summary
title: "Chen et al. 2025 — Direct, bisulfite-free 5mC and 5hmC sequencing at single-cell resolution with scTAPS and scCAPS+"
source: "[[00-Sources/papers/Direct and bisulfite-free 5-methylcytosine and 5-hydroxymethylcytosine sequencing at single-cell resolution with scTAPS and scCAPS +]]"
source_kind: paper
author: "Xiufei Chen, Jingfei Cheng, Linzhen Kong, Xiao Shu, Haiqi Xu, Masato Inoue, Marion Silvana Fernández-Berrocal, Dagny Sanden Døskeland, Magnar Bjørås, Shivan Sivakumar, Yibin Liu, Jing Ye, Chun-Xiao Song (corresponding)"
published: 2025-08-18
ingested: 2026-08-10
doi: "10.1186/s13059-025-03708-1"
journal: "Genome Biology"
tags: [scTAPS, scCAPS-plus, TAPS, bisulfite-free, 5hmC, 5mC, pyridine-borane, Tn5, aging, hippocampus]
entities: ["[[chun-xiao-song]]"]
concepts: ["[[taps]]", "[[5hmc]]", "[[bisulfite-sequencing]]", "[[scbs-seq]]", "[[tet-enzymes]]", "[[tn5-tagmentation]]", "[[epigenetic-aging]]", "[[simple-seq]]"]
topics: ["[[dna-methylation]]"]
---

**Citation:** Chen et al. (2025) — *Direct and bisulfite-free 5-methylcytosine and 5-hydroxymethylcytosine sequencing at single-cell resolution with scTAPS and scCAPS+* — *Genome Biology* 26, 244. [DOI](https://doi.org/10.1186/s13059-025-03708-1)

# Chen 2025 — scTAPS / scCAPS+

> The chemistry that finally separates 5mC from 5hmC in single cells. TAPS converts the **modified** base (5mC/5hmC → T) rather than the unmodified one, so genomic complexity is preserved instead of destroyed — giving ~90% mapping efficiency where bisulfite methods struggle, with no DNA-damaging bisulfite step at all.

## Key claims

- The problem with everything before: bisulfite methods cause substantial DNA damage and limited mapping efficiency. Existing "bisulfite-free" alternatives still work **indirectly** by converting unmodified cytosine, which collapses sequence complexity just as bisulfite does.
- **scTAPS** (TET-assisted pyridine borane sequencing) reads 5mC + 5hmC; **scCAPS+** (chemical-assisted pyridine borane sequencing plus) reads 5hmC specifically. Both convert the modified base directly to T.
- Workflow: FACS-sort single cells or nuclei into 96-well plates → lysis and fragmentation with **barcoded Tn5** → gap fill and purify → **pool 96 cells** → run TAPS or CAPS+ chemistry on the pool. Doing the chemistry after barcoding and pooling is what makes it tractable per cell.
- Performance: mapping **93.0% (scTAPS) / 89.4% (scCAPS+)**. Spike-in-measured conversion: scTAPS 5mCG 96.6%, 5hmCG 85.0%; scCAPS+ 5hmCG 93.0%. False positives on unmodified C: **0.19% and 0.38%**; scCAPS+ false positive on 5mCG 0.25% — i.e. it genuinely ignores 5mC.
- Coverage: at 4.8M and 7.7M 120 bp paired-end reads per cell, mean **2.0M and 2.3M CpG sites covered (8.08% and 10.88% of all CpGs)** — higher CpG and genomic coverage than published methods at comparable depth, and not yet saturated.
- Bulk-to-single-cell agreement: merged 96 cells vs bulk Pearson r = **0.95 (TAPS) / 0.98 (CAPS+)**; individual cell vs bulk ~0.700 and ~0.785.
- **Head-to-head with SIMPLE-seq**, published during manuscript preparation and which itself incorporates TAPS chemistry: SIMPLE-seq has lower 5mC conversion (~87%, requiring a standard curve to correct modification levels) and much lower genome coverage (1.96% for 5mC, 0.79% for 5hmC) — attributed to its high throughput compromising depth per cell. The authors frame the two as complementary, analogous to Smart-seq3 vs 10x.
- Biology: hippocampal neurons carry far more 5hmC than non-neurons (**22.04% vs 9.29%**). Gene-body 5hmC alone clusters cells into FACS-matched neuron/non-neuron groups, and Tabula Muris annotation identifies the non-neuronal cluster as **OPCs**. Marker genes behave as expected: *Cnksr3/Mob3b/Sema4d/Dock5* hydroxymethylated in non-neurons, *Cntnap2/Rbfox3/Syt1/Grm1* in neurons.
- **Aging**: young (3 mo) vs aged (18 mo) cells separate on 5hmC signal in *both* neurons and non-neurons. Genes whose expression rises with age (*Edil3*, *Prr5l*, *Galntl6*, *Atg10*) gain 5hmC; genes whose expression falls (*Epha3*, *Srrm4*, *Eps8*, *Acvr1*) lose it — most clearly in non-neurons. **APP moves in opposite directions**: 5hmC up in aged non-neurons, down in aged neurons.

## Methods / evidence

Spike-in controls for every conversion and false-positive rate — unmodified C, 5mCG and 5hmCG separately — which is what lets the accuracy claims be quantitative rather than comparative. Validation in two systems (human CD8⁺ T cells for scTAPS, mESC for scCAPS+), bulk-vs-merged-vs-single-cell correlation, and a saturation curve showing coverage is depth-limited not method-limited.

Stated limitation: plate-based, 96 cells per run. The authors position this as a deliberate depth-for-throughput trade and call for future high-throughput adaptation.

## Surprising or load-bearing bits

- **This closes the loop opened by [[tahiliani-2009-tet1-5hmc|Tahiliani 2009]]**, which discovered 5hmC and stated explicitly that appreciating its biology "will require the development of tools that allow hmC, 5mC, and C to be distinguished unequivocally." Sixteen years later, in single cells.
- **Every bisulfite-based methylation measurement in this corpus is a 5mC+5hmC composite** — [[smallwood-2014-natmethods|scBS-seq]], [[luo-2018-snmc-seq2|snmC-seq2]], [[nichols-2022-scimet-v2|sciMETv2]], and everything analyzed by [[kremer-2024-methscan|MethSCAn]]. In hippocampal neurons, where 5hmC is **22% of CpGs**, that conflation is not a rounding error. Neuronal methylome studies specifically need this correction.
- The *direct* conversion argument is the technically important one: converting the modified base preserves complexity, which is why mapping is ~90% rather than the much lower rates typical of methods that collapse C→T genome-wide. Sequence complexity is the hidden currency in methylation sequencing.
- Doing conversion chemistry **after** barcoding and pooling is the architectural trick that makes harsh chemistry survivable per cell — the same logic as bulk-tagmentation-then-split in [[kaya-okur-2019-cut-and-tag|CUT&Tag]].
- **5hmC works as a cell-type classifier on its own**, without any transcriptome or accessibility data. That is a genuinely new claim about 5hmC's information content, and it makes 5hmC a candidate lineage/state marker rather than a demethylation intermediate.
- The bidirectional *APP* result — opposite 5hmC change in aged neurons vs non-neurons — is a concrete argument for cell-type-resolved epigenomics in neurodegeneration; bulk hippocampus would average it to nothing. Connects to [[miller-2022-nature]] and [[kousi-2022-ad-mosaicism]].

## Entities mentioned

- [[chun-xiao-song]] — corresponding author; TAPS and CAPS+ chemistry originate in this lab.

## Concepts touched

- [[taps]] — single-cell implementation of the chemistry.
- [[5hmc]] — first quantitative single-cell, single-base 5hmC map; supplies the 22% neuronal figure.
- [[bisulfite-sequencing]] — the limitations this method exists to remove.
- [[epigenetic-aging]] — 5hmC as an aging-associated signal separable by cell type.

## Connections to other sources

- Answers the tool gap stated in [[tahiliani-2009-tet1-5hmc]]; alternative route to the same discrimination is kinetic ([[flusberg-2010-smrt-methylation]]) or long-read basecalling (Simpson 2017 (nanopore methylation) *(not bookmarked)*).
- Direct comparison target: SIMPLE-seq ([[simple-seq]], [[bai-2024-simple-seq]]) — depth vs throughput, explicitly framed as complementary.
- Supersedes the 5mC/5hmC conflation in [[smallwood-2014-natmethods]], [[guo-2013-scrrbs]], [[luo-2018-snmc-seq2]], [[nichols-2022-scimet-v2]].
- Brain aging and neuronal epigenome context: [[lodato-2017-aging-neurons]], [[lake-2018-brain-snrna-scths]], [[liu-2023-mouse-brain-methylome-3d]].
- Reviewed in [[iqbal-2023-methylome-review]].

## Open questions

- **How much of the published single-cell "methylome" literature is actually reporting 5mC+5hmC, and where does it matter?** Nowhere quantified in this corpus. Given 22% 5hmC in neurons, brain methylome atlases are the obvious place to check.
- Throughput: 96 cells per plate-based run cannot build atlases. Whether the chemistry survives combinatorial indexing or droplet formats is the stated open engineering problem.
- The multi-omics integration the authors anticipate — TAPS chemistry alongside transcriptome or genome in the same cell — does not yet exist.

## Related

- [[taps]] · [[5hmc]] · [[tahiliani-2009-tet1-5hmc]] · [[dna-methylation]]
