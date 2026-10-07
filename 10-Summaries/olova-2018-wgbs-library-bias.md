---
type: summary
title: "Olova et al. 2018 — Comparison of whole-genome bisulfite sequencing library preparation strategies identifies sources of biases affecting DNA methylation data"
source: "[[00-Sources/papers/Comparison of whole-genome bisulfite sequencing library preparation strategies identifies sources of biases affecting DNA methylation data]]"
source_kind: paper
author: "Nelly Olova, Felix Krueger, Simon Andrews, David Oxley, Rebecca V. Berrens, Miguel R. Branco, Wolf Reik (corresponding)"
published: 2018-03-15
ingested: 2026-10-07
doi: "10.1186/s13059-018-1408-2"
journal: "Genome Biology 19:33"
tags: [WGBS, bisulfite-conversion, PBAT, amplification-free, PCR-bias, library-preparation, non-CG-methylation, conversion-artefact, Bismark, bam2nuc, benchmark]
entities: ["[[wolf-reik]]"]
concepts: ["[[bisulfite-sequencing]]", "[[scbs-seq]]", "[[dnmt]]", "[[5hmc]]", "[[cpg-island]]", "[[quality-control-metrics]]"]
topics: ["[[dna-methylation]]"]
---

**Citation:** Olova et al. (2018) — *Comparison of whole-genome bisulfite sequencing library preparation strategies identifies sources of biases affecting DNA methylation data* — *Genome Biology* 19:33. [DOI](https://doi.org/10.1186/s13059-018-1408-2)

# Olova 2018 — WGBS library biases

> WGBS is treated as the gold-standard methylation readout, but its numbers depend on how the library was made. Comparing five bisulfite (BS) conversion protocols and seven library strategies — plus a cross-lab panel of 225 libraries — the authors show that **bisulfite conversion itself is the root bias**: it preferentially degrades unmethylated C-rich DNA, so methylated sequence is over-represented; PCR then amplifies that skew and any unconverted-cytosine artefacts. Most amplified protocols **overestimate global methylation**, local and relative methylation differ between methods, and **amplification-free PBAT** is the least biased.

## Key claims

- **BS-induced degradation is sequence- and methylation-selective.** With Heat-denaturing BS treatment, a C-poor (15% C) synthetic fragment was recovered twofold better than a C-rich (30% C) one; Alkaline denaturation reduced this to 1.3-fold; ammonium bisulfite (Am-BS, 9 M) showed no C-content difference. 5mC or 5hmC in the fragment gave ~fourfold higher recovery of the C-rich sequence under Heat — cytosine modification protects against degradation.
- **Strand coverage is skewed in real data.** In amplification-free PBAT, the C-poor strands of mouse major satellite and mtDNA were covered more than C-rich strands, and telomere G-strand reads were up to 1000-fold more frequent than C-strand reads.
- **Degradation alone inflates methylation.** LC-MS of BS-treated mESC DNA showed Heat and Am-BS protocols cause a direct 5–10% increase in global methylation estimates; the milder Alkaline protocol did not.
- **PCR builds on the bias.** All methods showed significant dinucleotide coverage bias vs a non-BS control, mostly G-enrichment and AT-depletion; KAPA HiFi Uracil+ instead showed balanced G, depleted C and enriched AT. Only amplification-free PBAT showed no significant CG-dinucleotide coverage deviation.
- **Global methylation overestimation.** In mESCs, Heat and Alkaline (Pfu Turbo Cx) WGBS gave about double the LC-MS 5mC value; KAPA and post-BS methods overestimated less; amplification-free PBAT was not significantly different from LC-MS.
- **Methylation level changes the bias.** In vitro M.CviPI-methylated DNMT-TKO DNA (~20% methylation) had ~15% higher coverage at C-containing dinucleotides than unmethylated TKO DNA; WGBS overestimated meTKO 5mC by ~40% versus ~100% for WT mESCs. CGI coverage was most biased with Heat pre-BS and decreased in unmethylated samples.
- **Incomplete conversion is a separate artefact, concentrated in CH context.** Alkaline denaturation left fourfold more unconverted cytosines than Heat (LC-MS); in unmethylated TKO data from the Alkaline protocol, unconverted cytosines exceeded the real 5mC level of WT mESCs. Pre-BS Alkaline data showed false CH-methylation strand asymmetry at major satellites; post-BS methods did not.
- **Local and relative estimates differ by method.** iDMR methylation ranged from 44% (PBAT) to 58% (EpiGnome); the largest discrepancies were at intermediately methylated regions (enhancers, promoters, TF binding sites). For sperm vs ESC differences >20%, more than half of Heat-defined regions were also found with PBAT, but most PBAT-defined regions were not found with Heat. The authors state that changes of up to 20% can be purely technical.
- **Mitigations.** New Bismark modules: *bam2nuc* (mono/dinucleotide composition vs genome; C depletion flags degradation, C enrichment flags poor conversion) and *filter_non_conversion* (drop reads with ≥3 unconverted CH). Averaging per-cytosine methylation within a region beats pooling all calls; minimum-coverage filters (≥5 or ≥10×) reinforce coverage bias. For CH methylation, a threshold cut-off is least effective; the 3×C read filter and subtraction of an unmethylated-genome (TKO) control are better.

## Methods / evidence

Synthetic M13 fragments (C-poor/C-rich, unmodified/5mC/5hmC) under five BS protocols; LC-MS/MS of BS-treated genomic DNA for 5mC and unconverted C; own WGBS libraries (pre-BS Heat/Alkaline with Pfu Turbo Cx, TKO and meTKO) plus a retrospective cross-study, cross-species panel (225 libraries including non-BS controls; each method represented by ≥2 studies from different labs where possible); BS cloning of major satellites as a reference for CH methylation. Methods compared: pre-BS Heat, Alkaline, Am-BS, KAPA (Uracil+); post-BS PBAT (amplification-free), ampPBAT, EpiGnome/TruSeq.

Weight: strong — orthogonal LC-MS ground truth, multi-lab data that guard against batch effects, and mechanistic fragment experiments. Limits: mostly mouse ESC, mostly Illumina; Am-BS lacked mESC WGBS data; KAPA and EpiGnome lacked unmethylated controls for the CGI analysis.

## Surprising or load-bearing bits

- **The bias is in the chemistry, not the polymerase.** Changing the polymerase moves the G/AT skew around, but the C-rich, unmethylated depletion comes from conversion and is there before PCR.
- **Methylation protects DNA from degradation**, so methylated sequence is over-sampled — the measurement interacts with what it measures.
- **"Up to 20% can be purely technical"** is a useful prior for any cross-protocol or cross-lab methylation comparison, including integration of public datasets. (synthesis)
- **For single-cell bisulfite work this is the bulk rationale for PBAT**: the post-BS design that makes scBS-seq feasible is also the least biased. Single-cell protocols that add many amplification rounds may inherit the amplified-library biases described here, though this paper does not test single-cell data. (synthesis)

## Concepts touched

- [[bisulfite-sequencing]] — systematic map of degradation, PCR and conversion artefacts across WGBS protocols.
- [[scbs-seq]] — supports the PBAT post-bisulfite design used by single-cell methods.
- [[5hmc]] — 5hmC protects fragments against BS degradation as 5mC does (BS cannot distinguish them).
- [[cpg-island]] — CGI coverage bias depends on protocol and methylation status.
- [[quality-control-metrics]] — bam2nuc composition check and the CH non-conversion filter as WGBS QC.

## Connections to other sources

- The aligner/caller extended here with bam2nuc and filter_non_conversion: [[krueger-2011-bismark]].
- Single-cell bisulfite methods built on PBAT: [[smallwood-2014-natmethods]], [[clark-2017-scbs-seq-protocol]], [[mulqueen-2018-sci-met]], [[luo-2017-snmc-seq]].
- Bisulfite-free alternatives that sidestep degradation and conversion artefacts: [[chen-2025-sctaps-sccaps-plus]] (TAPS), [[fu-2025-longread-methylation]].
- Method-landscape reviews: [[iqbal-2023-methylome-review]], [[lim-2024-single-cell-omics-review]].

## Open questions

- How large are these biases in single-cell libraries with heavy amplification, where per-cell coverage is too sparse for bam2nuc-style composition checks? (synthesis)
- Non-CG methylation calls made without unmethylated-genome controls or 3×C filtering may partly be conversion artefacts; how many published CH claims survive is untested here.
- The paper notes PBAT itself can be affected by HiSeq base-calling software versions — a different source of bias it does not dissect.

## Related

- [[bisulfite-sequencing]] · [[40-Topics/dna-methylation]] · [[krueger-2011-bismark]] · [[clark-2017-scbs-seq-protocol]]
