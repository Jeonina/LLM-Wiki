---
type: concept
title: Bisulfite sequencing
aliases: [BS-seq, WGBS, whole-genome bisulfite sequencing]
tags: [methylation, sequencing, method]
created: 2026-05-11
updated: 2026-10-12
---

# Bisulfite sequencing

> Standard short-read method for measuring DNA methylation: sodium bisulfite converts unmethylated C → U → T (after PCR) while 5mC is protected, so sequencing the converted DNA reveals methylation status at base resolution. The dominant methylation assay for ~20 years, but it suffers from a structural alignment problem in repeats and structural variants ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).

> [!abstract] 한눈에
> Bisulfite sequencing은 메틸화되지 않은 C를 T로 바꿔 읽어 CpG 메틸화를 염기 단위로 재는 표준 방법이지만, 변환 자체가 DNA를 손상시키고 비메틸화 C-rich 서열을 더 많이 잃게 해 측정에 편향을 남긴다 ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]; [[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]). single-cell에서는 PBAT, combinatorial indexing, droplet 방식이 세포당 CpG coverage와 처리량을 서로 맞바꾸고, EM-seq 같은 효소 변환이 대안으로 시험되고 있다 ([[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]; [[10-Summaries/mulqueen-2018-sci-met|sci-MET]]; [[10-Summaries/nichols-2025-scimetv3|sciMETv3]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 DNA methylation](../60-Explainers/dna-methylation.html)
<!-- /explainer-links -->

## Definition

Sodium bisulfite treatment deaminates unmethylated cytosines to uracils, which become thymidines after PCR amplification; 5-methylcytosine resists bisulfite conversion ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]). Sequenced reads are aligned to a reference where all cytosines are converted to thymidines (and vice versa for the reverse strand) — the **"three-base alignment problem"** ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).

Per-CpG methylation = count of unconverted C / total reads at the site.

## Why it matters

- Established the methylation field's resolution standard — per-base, genome-wide.
- ENCODE WGBS atlas, the Roadmap Epigenomics Consortium, and the BLUEPRINT consortium all built on bisulfite sequencing.
- Bisulfite chemistry also underlies the single-cell methylome methods in this wiki, from [[30-Concepts/scbs-seq|scBS-seq]] to droplet assays ([[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]; [[10-Summaries/zhang-2023-drop-bs|Drop-BS]]).

## Variants and refinements

- **WGBS** (whole-genome bisulfite sequencing) — covers all CpGs but expensive.
- **RRBS** (reduced representation bisulfite sequencing) — enriches CpG-rich regions; cheaper but lower CpG coverage.
- **PBAT** (post-bisulfite adaptor tagging) — amplification-free PBAT matched LC-MS global 5mC where amplified protocols overestimated it ([[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]).
- **Post-bisulfite hybrid capture** — the Twist Human Methylome Panel (~123 Mbp of regulatory regions) enriches libraries after conversion ([[10-Summaries/acharya-2024-scimet-cap|sciMET-cap]]).
- **EM-seq** — enzymatic methyl sequencing; replaces bisulfite with TET2 + T4-BGT protection and APOBEC3A deamination, producing the same C/T readout but GC-even libraries ([[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]).
- **TAPS-seq** — TET-assisted pyridine borane sequencing.

### Single-cell throughput strategies

| Strategy | Per-cell CpG coverage | Throughput | Source |
|---|---|---|---|
| Tubes / plates ([[30-Concepts/scbs-seq\|scBS-seq]], PBAT) | ~50% | tens–hundreds | ([[10-Summaries/clark-2017-scbs-seq-protocol\|Clark 2017]]) |
| Reduced representation (scRRBS) | ~1M CpGs, ~70% of CGIs, **consistent** across cells | tens–hundreds | ([[10-Summaries/guo-2015-scrrbs-protocol\|Guo 2015]]) |
| Plate + indexed random primers (snmC-seq) | 4.7–5.7% of genome | thousands | ([[10-Summaries/luo-2017-snmc-seq\|snmC-seq]]) |
| Combinatorial indexing (sci-MET) | mean 1.1% of CpGs | thousands | ([[10-Summaries/mulqueen-2018-sci-met\|sci-MET]]) |
| Droplet (Drop-BS) | ~13,500 CpGs/cell | up to 10,000 in 2 days | ([[10-Summaries/zhang-2023-drop-bs\|Drop-BS]]) |

## Sources of bias

- **Three-base alignment problem.** Degrades mapping in repeats and structural variants — exactly the regions where methylation has key roles (transposon silencing) ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).
- **DNA damage** from bisulfite treatment leads to incomplete conversion and fragment loss.
- **Conversion degrades unmethylated, C-rich DNA.** Bisulfite conversion itself is the main source of WGBS bias: 5mC/5hmC protect fragments, so methylated sequence is over-represented ([[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]).
- **PCR amplifies the skew.** PCR amplifies these skews and unconverted-cytosine artefacts ([[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]).
- **5hmC.** Beyond conflating 5mC with 5hmC, the 5hmC adduct CMS stalls Taq during PCR (strongest at tandem CC contexts, weaker at CpGs), so CMS-dense templates amplify inefficiently ([[10-Summaries/huang-2010-5hmc-bisulfite|Huang 2010]]).
- **Alignment rate is an underrated bottleneck.** Classic one-cell-per-well scWGBS runs at 25 ± 20%, meaning three of four reads are wasted ([[10-Summaries/mulqueen-2018-sci-met|sci-MET]]).
- **Enzymatic alternatives** (EM-seq, TAPS-seq) have similar genome-wide coverage with less DNA damage.

## Genotyping from bisulfite reads

- In directional libraries the strand opposite a cytosine is unaffected by conversion, so Bis-SNP can call C>T SNPs and methylation jointly ([[10-Summaries/liu-2012-bis-snp|Bis-SNP]]).
- At single-cell scale, within-read heterozygous SNPs can phase methylation calls to alleles without a custom reference ([[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]).

## Evidence and examples

**Bias magnitudes**

- Bisulfite gave twofold lower recovery of a 30%-C than a 15%-C fragment under heat denaturation ([[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]).
- Amplified protocols overestimated mESC global 5mC (up to about double the LC-MS value), whereas amplification-free PBAT matched LC-MS ([[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]).
- Differences of up to 20% between protocols can be purely technical, and absolute and relative methylation calls at intermediately methylated regions vary most ([[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]).

**Low-input and single-cell chemistry**

- Breadth beats depth for low-input methylomes: deeper sequencing of one library added 62–86% CpG coverage at high duplicate rates, whereas combining a few dozen low-coverage one-cell or four-cell samples covered >90% of CpGs in human and mouse ([[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]).
- Cytosine-depleted transposome adaptors survive bisulfite treatment, which is what makes indexed tagmentation compatible with conversion ([[10-Summaries/mulqueen-2018-sci-met|sci-MET]]).
- Transposase-based adaptor incorporation lifts the alignment rate to 68 ± 8% ([[10-Summaries/mulqueen-2018-sci-met|sci-MET]]).
- Bisulfite conversion **inside droplets yields 9× more library** than the same conversion in bulk, at 99.0% conversion — unexplained, and potentially relevant to any low-input BS protocol ([[10-Summaries/zhang-2023-drop-bs|Drop-BS]]).
- Post-bisulfite capture enriched single-cell sciMETv2 libraries 7–8-fold; site-level calls agreed with uncaptured libraries (Pearson ≥0.96), with no strand bias ([[10-Summaries/acharya-2024-scimet-cap|sciMET-cap]]).
- Bulk libraries reach about 12–18-fold enrichment with capture, roughly twice the single-cell figure ([[10-Summaries/acharya-2024-scimet-cap|sciMET-cap]]).

**Enzymatic conversion**

- EM-seq libraries cover ~54 M of 56 M CpGs at 1× from 10–200 ng and work from 100 pg, cfDNA and FFPE DNA ([[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]).
- In sciMETv3, EM-seq conversion roughly doubled insert size (163 vs 78 bp) and gave methylation profiles and cell-type proportions comparable to bisulfite ([[10-Summaries/nichols-2025-scimetv3|sciMETv3]]).
- In sciMETv3, TET2 over-converted methylated adapter cytosines in the Illumina read-2 primer region, impairing Illumina runs but not Ultima sequencing ([[10-Summaries/nichols-2025-scimetv3|sciMETv3]]).
- In single cells, an enzymatic-conversion protocol (Cabernet) showed incomplete CpY conversion in 43–49% of reads when reprocessed alongside bisulfite methods ([[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]).

**Genotyping**

- Bis-SNP called 95.22% of homozygous cytosines and 93.18% of heterozygous SNPs at 32× against a SNP array ([[10-Summaries/liu-2012-bis-snp|Bis-SNP]]).

**Applications**

- Roadmap Epigenomics methylation atlas — predominantly WGBS-derived.
- Cancer methylation biomarker assays (e.g., Cologuard methylation-based colorectal screening) — bisulfite-based.

## Contested points

- **Is bisulfite still the gold standard?** Given long-read direct methylation detection — for most applications, yes; for repeat-rich regions, no ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).
- **Enzymatic conversion in single cells.** sciMETv3 found EM-seq comparable to bisulfite ([[10-Summaries/nichols-2025-scimetv3|sciMETv3]]), while Cabernet's enzymatic conversion was incomplete in 43–49% of reads ([[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]); the two use different protocols and evaluations (synthesis).
- **The 5hmC PCR bias was shown on synthetic oligonucleotides, not genomic DNA** ([[10-Summaries/huang-2010-5hmc-bisulfite|Huang 2010]]).
- **All high-throughput methods share an annotation dependency**: they cluster on mCH bins and then label clusters against snmC-seq reference DMRs, rather than annotating de novo from their own data ([[10-Summaries/mulqueen-2018-sci-met|sci-MET]]; [[10-Summaries/zhang-2023-drop-bs|Drop-BS]]) (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/scbs-seq|scBS-seq]] — Single-cell bisulfite sequencing of genome-wide CpG methylation, with sparse per-cell coverage.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC at CpG dinucleotides: assays, single-cell methods and analysis.
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — Direct methylation detection as the alternative to bisulfite conversion.

## All sources on this page

> [!info]- 14 summaries cited here
> - [[10-Summaries/acharya-2024-scimet-cap|Acharya 2024]]
> - [[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]
> - [[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]
> - [[10-Summaries/fu-2025-longread-methylation|Fu 2025]]
> - [[10-Summaries/guo-2015-scrrbs-protocol|Guo 2015]]
> - [[10-Summaries/huang-2010-5hmc-bisulfite|Huang 2010]]
> - [[10-Summaries/liu-2012-bis-snp|Liu 2012]]
> - [[10-Summaries/luo-2017-snmc-seq|Luo 2017]]
> - [[10-Summaries/mulqueen-2018-sci-met|Mulqueen 2018]]
> - [[10-Summaries/nichols-2025-scimetv3|Nichols 2025]]
> - [[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]
> - [[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]
> - [[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]
> - [[10-Summaries/zhang-2023-drop-bs|Zhang 2023]]
