---
type: concept
title: Bisulfite sequencing
aliases: [BS-seq, WGBS, whole-genome bisulfite sequencing]
tags: [methylation, sequencing, method]
created: 2026-05-11
updated: 2026-10-07
---

# Bisulfite sequencing

> Standard short-read method for measuring DNA methylation. Sodium bisulfite converts unmethylated C → U → T (after PCR); methylated 5mC is protected. Sequencing the converted DNA reveals methylation status at base resolution. The dominant methylation assay for ~20 years but suffers from a structural alignment problem in repeats and structural variants.

## Definition

Sodium bisulfite treatment deaminates unmethylated cytosines to uracils, which become thymidines after PCR amplification. 5-methylcytosine resists bisulfite conversion. Sequenced reads are aligned to a reference where all cytosines are converted to thymidines (and vice versa for the reverse strand) — the **"three-base alignment problem"** ([[10-Summaries/fu-2025-longread-methylation]]).

Per-CpG methylation = count of unconverted C / total reads at the site.

## Why it matters

- Established the methylation field's resolution standard — per-base, genome-wide.
- ENCODE WGBS atlas, the Roadmap Epigenomics Consortium, and the BLUEPRINT consortium all built on bisulfite sequencing.

**Limitations** that motivated long-read alternatives:

- **Three-base alignment problem**: degrades mapping in repeats and structural variants — exactly the regions where methylation has key roles (transposon silencing).
- **DNA damage** from bisulfite treatment leads to incomplete conversion and fragment loss.
- **Enzymatic alternatives** (EM-seq, TAPS-seq) have similar genome-wide coverage with less DNA damage.

## Variants and refinements

- **WGBS** (whole-genome bisulfite sequencing) — covers all CpGs but expensive.
- **RRBS** (reduced representation bisulfite sequencing) — enriches CpG-rich regions; cheaper but lower CpG coverage.
- **EM-seq** — enzymatic methyl sequencing; replaces bisulfite with TET2 + APOBEC.
- **TAPS-seq** — TET-assisted pyridine borane sequencing.

## Contested points

- Whether bisulfite sequencing remains the gold standard given long-read direct methylation detection — for most applications, yes; for repeat-rich regions, no ([[10-Summaries/fu-2025-longread-methylation]]).

## Examples

- Roadmap Epigenomics methylation atlas — predominantly WGBS-derived.
- Cancer methylation biomarker assays (e.g., Cologuard methylation-based colorectal screening) — bisulfite-based.

## Added 2026-10-07

Beyond conflating 5mC with 5hmC, bisulfite treatment creates a coverage bias: the 5hmC adduct CMS stalls Taq during PCR (strongest at tandem CC contexts, weaker at CpGs), so CMS-dense templates amplify inefficiently ([[10-Summaries/huang-2010-5hmc-bisulfite]]). This was shown on synthetic oligonucleotides, not genomic DNA ([[10-Summaries/huang-2010-5hmc-bisulfite]]).

Bisulfite conversion itself is the main source of WGBS bias: it preferentially degrades unmethylated, C-rich DNA (twofold lower recovery of a 30%-C vs 15%-C fragment under heat denaturation), while 5mC/5hmC protect fragments, so methylated sequence is over-represented [[10-Summaries/olova-2018-wgbs-library-bias]]. PCR amplifies these skews and unconverted-cytosine artefacts; amplified protocols overestimated mESC global 5mC (up to about double the LC-MS value), whereas amplification-free PBAT matched LC-MS [[10-Summaries/olova-2018-wgbs-library-bias]]. Differences of up to 20% between protocols can be purely technical, and absolute and relative methylation calls at intermediately methylated regions vary most [[10-Summaries/olova-2018-wgbs-library-bias]].

Breadth beats depth for low-input methylomes. Deeper sequencing of one library added 62–86% CpG coverage at high duplicate rates, whereas combining a few dozen low-coverage one-cell or four-cell samples covered >90% of CpGs in human and mouse ([[10-Summaries/farlik-2015-scwgbs]]).

**Bisulfite-free conversion.** EM-seq replaces bisulfite with TET2 + T4-BGT protection and APOBEC3A deamination, producing the same C/T readout but GC-even libraries that cover ~54 M of 56 M CpGs at 1× from 10–200 ng and work from 100 pg, cfDNA and FFPE DNA ([[10-Summaries/vaisvila-2021-em-seq]]). In single cells, however, an enzymatic-conversion protocol (Cabernet) showed incomplete CpY conversion in 43–49% of reads when reprocessed alongside bisulfite methods ([[10-Summaries/spix-2025-scdeep-mc]]).

**Genotyping from bisulfite reads.** In directional libraries the strand opposite a cytosine is unaffected by conversion, so Bis-SNP can call C>T SNPs and methylation jointly (95.22% of homozygous cytosines and 93.18% of heterozygous SNPs at 32× vs a SNP array) ([[10-Summaries/liu-2012-bis-snp]]). At single-cell scale, within-read heterozygous SNPs can phase methylation calls to alleles without a custom reference ([[10-Summaries/spix-2025-scdeep-mc]]).

**Enzymatic vs bisulfite in single cells.** In sciMETv3, EM-seq conversion roughly doubled insert size (163 vs 78 bp) and gave methylation profiles and cell-type proportions comparable to bisulfite, but TET2 over-converted methylated adapter cytosines in the Illumina read-2 primer region, impairing Illumina runs but not Ultima sequencing ([[10-Summaries/nichols-2025-scimetv3]]).

Post-bisulfite hybrid capture with the Twist Human Methylome Panel (~123 Mbp of regulatory regions) enriched single-cell sciMETv2 libraries 7–8-fold ([[10-Summaries/acharya-2024-scimet-cap]]). Site-level methylation calls agreed with uncaptured libraries (Pearson ≥0.96), with no strand bias ([[10-Summaries/acharya-2024-scimet-cap]]). Bulk libraries reach about 12–18-fold enrichment with capture, roughly twice the single-cell figure ([[10-Summaries/acharya-2024-scimet-cap]]).


## Related

- [[40-Topics/dna-methylation]]
- [[40-Topics/long-read-sequencing]] — direct methylation detection alternative.
- [[40-Topics/dna-methylation]]

## Added 2026-08-13

Three throughput strategies for single-cell bisulfite sequencing, and what each costs:

| Strategy | Per-cell CpG coverage | Throughput | Source |
|---|---|---|---|
| Tubes / plates ([[30-Concepts/scbs-seq|scBS-seq]], PBAT) | ~50% | tens–hundreds | ([[10-Summaries/clark-2017-scbs-seq-protocol]]) |
| Reduced representation (scRRBS) | ~1M CpGs, ~70% of CGIs, **consistent** across cells | tens–hundreds | ([[10-Summaries/guo-2015-scrrbs-protocol]]) |
| Plate + indexed random primers (snmC-seq) | 4.7–5.7% of genome | thousands | ([[10-Summaries/luo-2017-snmc-seq]]) |
| Combinatorial indexing (sci-MET) | mean 1.1% of CpGs | thousands | ([[10-Summaries/mulqueen-2018-sci-met]]) |
| Droplet (Drop-BS) | ~13,500 CpGs/cell | up to 10,000 in 2 days | ([[10-Summaries/zhang-2023-drop-bs]]) |

**Two chemistry findings worth carrying.** Cytosine-depleted transposome adaptors survive bisulfite treatment, which is what makes indexed tagmentation compatible with conversion ([[10-Summaries/mulqueen-2018-sci-met]]). And bisulfite conversion **inside droplets yields 9× more library** than the same conversion in bulk, at 99.0% conversion — unexplained, and potentially relevant to any low-input BS protocol ([[10-Summaries/zhang-2023-drop-bs]]).

**Alignment rate is an underrated bottleneck**: classic one-cell-per-well scWGBS runs at 25 ± 20%, meaning three of four reads are wasted; transposase-based adaptor incorporation lifts it to 68 ± 8% ([[10-Summaries/mulqueen-2018-sci-met]]).

**All high-throughput methods share an annotation dependency**: they cluster on mCH bins and then label clusters against snmC-seq reference DMRs, rather than annotating de novo from their own data ([[10-Summaries/mulqueen-2018-sci-met]]; [[10-Summaries/zhang-2023-drop-bs]]). (synthesis)
