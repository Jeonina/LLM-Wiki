---
type: topic
title: DNA methylation
explainer: dna-methylation
aliases: [5mC, cytosine methylation, methylation]
tags: [methylation, epigenetics, regulation]
created: 2026-05-11
updated: 2026-10-12
paper_section: ["3.3"]
---

# DNA methylation

> Covalent modification of the fifth carbon of cytosine to produce 5-methylcytosine (5mC), predominantly at symmetric CpG dinucleotides in mammals ([[10-Summaries/smith-2013-methylation-development|Smith 2013]]). It is the most stable and best-studied epigenetic mark, maintained through mitosis by DNMT1 and contributing to cell identity ([[10-Summaries/kim-2017-methylation-memory-review|Kim 2017]]); it silences transposons, establishes imprints, and is dysregulated in cancer and aging ([[10-Summaries/smith-2013-methylation-development|Smith 2013]]). This hub covers the biology of methylation, the measurement chemistries (bisulfite, enzymatic, long-read direct detection), single-cell methods and tools, and the enzymatic machinery (DNMT, TET).

> [!abstract] 한눈에
> DNA methylation은 세포 분열을 거쳐 유지되는 가장 안정적인 후성유전 표지이지만, 같은 5mC라도 TSS에 있느냐 gene body에 있느냐에 따라 하는 일이 다르다 ([[10-Summaries/kim-2017-methylation-memory-review|Kim 2017]]; [[10-Summaries/jones-2012-dna-methylation-functions|Jones 2012]]). single-cell 방법은 커버리지와 처리량 중 어느 쪽을 택하느냐로 갈리고, 최근에는 bisulfite 없이 5mC와 5hmC를 단일 염기 수준에서 구분하는 화학도 나왔다 ([[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 DNA methylation](../60-Explainers/dna-methylation.html)
<!-- /explainer-links -->

## Key points

- **The mark does not carry a fixed meaning; context does.** Methylation near the TSS blocks initiation, gene-body methylation does not and may stimulate elongation, and in *Neurospora* the relationship is inverted ([[10-Summaries/jones-2012-dna-methylation-functions|Jones 2012]]).
- **Silencing usually comes first.** De novo methylation needs a nucleosome and active TSSs are nucleosome-depleted, so methylation locks an already-silenced state ([[10-Summaries/jones-2012-dna-methylation-functions|Jones 2012]]).
- **Single-cell methods sit at different points on the coverage–throughput axis.** scBS-seq reaches ~50% of CpGs per cell, scRRBS reads the same ~1M CpGs in every cell ([[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]; [[10-Summaries/guo-2015-scrrbs-protocol|Guo 2015]]), while combinatorial indexing and droplets trade depth for cell number ([[10-Summaries/mulqueen-2018-sci-met|sci-MET]]; [[10-Summaries/zhang-2023-drop-bs|Drop-BS]]).
- **mCH makes sparse methylomes usable for cell typing.** Because mCH is modulated over large domains, 100-kb-bin estimates hold at 4.7–5.7% coverage per cell ([[10-Summaries/luo-2017-snmc-seq|Luo 2017]]).
- **Bisulfite cannot tell 5mC from 5hmC; newer chemistries can.** The two are indistinguishable by bisulfite ([[10-Summaries/huang-2010-5hmc-bisulfite|Huang 2010]]), and bisulfite-free single-cell chemistry now separates them at single-base resolution ([[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/bisulfite-sequencing|Bisulfite sequencing]] — The standard short-read methylation assay, with the consolidated single-cell protocol comparison table.
> - `concept` [[30-Concepts/cpg-island|CpG island]] — Short, CpG-dense, constitutively unmethylated regions at housekeeping and developmental promoters.
> - `concept` [[30-Concepts/5hmc|5hmC]] — TET-generated oxidation product of 5mC: demethylation intermediate and stable mark.
> - `concept` [[30-Concepts/epigenetic-memory|Epigenetic memory]] — The mitotically heritable record of past cellular states.
> - `concept` [[30-Concepts/methylation-clones-epimutation|Methylation clones and epimutation]] — Heritable CpG changes used as endogenous lineage markers and clocks.
> - `note` [[50-Notes/regulatory-layers-overview|Regulatory layers overview]] — Methylation as one of the molecular regulatory layers read by the field.

## Biology and definition

In mammals, ~60–80% of the ~28 million CpG dinucleotides in the human genome are methylated ([[10-Summaries/smith-2013-methylation-development|Smith 2013]]). Less than 10% of CpGs sit in **CpG islands** — short (~200–2000 bp) regions of high CpG density at promoters of housekeeping and developmental genes, which are constitutively unmethylated ([[10-Summaries/smith-2013-methylation-development|Smith 2013]]). Methylation is globally reset during two developmental windows: pre-implantation and primordial germ cell specification ([[10-Summaries/smith-2013-methylation-development|Smith 2013]]).

Other modification forms ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]):

- **5-hydroxymethylcytosine (5hmC)** — [[tet-enzymes|TET]]-catalyzed oxidation intermediate; a functional readout in some contexts ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]); its enzymatic origin was shown for TET1 ([[10-Summaries/tahiliani-2009-tet1-5hmc|Tahiliani 2009]]), and SIMPLE-seq measures it jointly with 5mC ([[10-Summaries/bai-2024-simple-seq|SIMPLE-seq]]).
- **N6-methyladenine (6mA)** — common in prokaryotes; rare in mammals ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).
- **N4-methylcytosine (4mC)** — prokaryotic ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).
- **Non-CpG 5mC (mCpH)** — found in brain and pluripotent cells ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).

## Function and regulatory logic

- **Stable propagation of cell identity** — marks established during differentiation are maintained through mitosis, contributing to [[epigenetic-memory|epigenetic memory]] ([[10-Summaries/kim-2017-methylation-memory-review|Kim 2017]]).
- **Genomic imprinting and X-inactivation** — methylation establishes parent-of-origin and chromosome-of-origin expression patterns, with imprinting marks erased in primordial germ cells and re-established during gametogenesis ([[10-Summaries/smith-2013-methylation-development|Smith 2013]]). X-inactivation is random monoallelic silencing maintained via methylation of XIST and downstream genes ([[10-Summaries/smith-2013-methylation-development|Smith 2013]]).
- **Transposon silencing** — most repetitive elements are heavily methylated ([[10-Summaries/smith-2013-methylation-development|Smith 2013]]); loss of methylation can derepress LINE-1, SINE and ERV elements, triggering "viral mimicry" interferon responses ([[10-Summaries/hunt-2022-sctem-seq|Hunt 2022]]).
- **Context-dependent function** — methylation near the TSS blocks initiation; gene-body methylation does not block and may stimulate elongation and affect splicing; in *Neurospora* the relationship is exactly inverted ([[10-Summaries/jones-2012-dna-methylation-functions|Jones 2012]]).
- **Silencing usually precedes methylation** — de novo methylation requires a nucleosome and active TSSs are nucleosome-depleted, so methylation acts as a lock on an already-silenced state; the less-expressed allele is preferentially methylated ([[10-Summaries/jones-2012-dna-methylation-functions|Jones 2012]]).
- **Methylation-dependent activation** — KLF2/KLF4/KLF5 bind specific sequences *because* they are methylated, and 5mC recognition stimulates KLF4-mediated transcription, breaking the silencing dogma ([[10-Summaries/rothbart-2014-histone-dna-language|Rothbart 2014]]).
- **Enhancers as low-methylated regions** — their intermediate bulk values must reflect either dynamic turnover or inefficient maintenance through division, the bulk statement of why methylation epimutation clocks work ([[10-Summaries/jones-2012-dna-methylation-functions|Jones 2012]]); this is operationalized as de novo VMR discovery in single cells ([[10-Summaries/kremer-2024-methscan|MethSCAn]]). At population scale, >18,000 intermediate-methylation regions (~57% mCpG) persist within purified cell types, "probably reflecting a stable state of cell-to-cell variability" ([[10-Summaries/roadmap-2015-111-epigenomes|Roadmap 2015]]).
- **Coupling with chromatin accessibility** — methylation–accessibility coupling strengthens along differentiation ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).
- **Largely independent of CNVs** — CNVs drive expression but do not propagate to local methylation state ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]).

## Disease and therapy

- **Cancer** — promoter hypermethylation silences tumour suppressors such as CDKN2A, MLH1 and BRCA1, while global hypomethylation enables oncogene activation and chromosome instability ([[10-Summaries/smith-2013-methylation-development|Smith 2013]]).
- **Clonal hematopoiesis** — DNMT3A R882 mutations perturb early progenitor states through selective hypomethylation ([[10-Summaries/nam-2022-natgenet|Nam 2022]]).
- **Hypomethylating agents** — [[dnmt|DNMT]] inhibitors are approved for MDS/AML ([[10-Summaries/hunt-2022-sctem-seq|Hunt 2022]]); [[decitabine]] and azacitidine produce divergent demethylation patterns ([[10-Summaries/shen-2026-splicool-seq|SpliCOOL-seq]]).
- **Tissue of origin** — methylation serves as a classifier for [[30-Concepts/cancer-of-unknown-primary|cancer of unknown primary]].

## Measurement chemistries

| Chemistry | Principle | Note |
|---|---|---|
| [[30-Concepts/bisulfite-sequencing\|Bisulfite sequencing]] | C→U→T conversion of unmethylated C | The standard short-read assay; suffers from the three-base alignment problem ([[10-Summaries/fu-2025-longread-methylation\|Fu 2025]]). 5hmC is indistinguishable from 5mC and its CMS adduct stalls Taq, biasing quantification ([[10-Summaries/huang-2010-5hmc-bisulfite\|Huang 2010]]). Among WGBS library preps, amplification-free PBAT is least biased, and non-CG methylation needs conversion controls ([[10-Summaries/olova-2018-wgbs-library-bias\|Olova 2018]]) |
| EM-seq | Enzymatic conversion | Bisulfite-free, GC-even, works from 100 pg input ([[10-Summaries/vaisvila-2021-em-seq\|EM-seq]]); less DNA damage than bisulfite ([[10-Summaries/fu-2025-longread-methylation\|Fu 2025]]) |
| [[30-Concepts/taps\|TAPS]] | TET + borane | Bisulfite-free 5mC chemistry ([[10-Summaries/fu-2025-longread-methylation\|Fu 2025]]); extended to single cells as scTAPS/scCAPS+ ([[10-Summaries/chen-2025-sctaps-sccaps-plus\|Chen 2025]]) |
| Long-read direct detection ([[40-Topics/long-read-sequencing\|long-read sequencing]]) | PacBio kinetic features; ONT current changes through the pore | No base conversion, so alignment quality is preserved in repeats and structural variants ([[10-Summaries/fu-2025-longread-methylation\|Fu 2025]]; [[10-Summaries/liu-2025-long-read-epigenome-review\|Liu & Conesa 2025]]); the kinetic route dates to SMRT sequencing ([[10-Summaries/flusberg-2010-smrt-methylation\|Flusberg 2010]]); STAM-seq reads accessibility + methylation in plant HRRs by nanopore adaptive sampling ([[10-Summaries/mo-2023-stam-seq\|STAM-seq]]) |
| [[30-Concepts/nome-seq\|NOMe-seq]] | GpC methyltransferase footprint | Accessibility readout ([[10-Summaries/clark-2018-scnmt-seq\|Clark 2018]]) |
| Microarrays | Probes at pre-selected CpGs | Limited to ~935,000 CpGs (synthesis; standard EPIC array specification) |

## Single-cell methylation methods

scBS-seq, scRRBS, snmC-seq2 and sciMETv2 are sparse but compatible with multi-omic combinations ([[10-Summaries/iqbal-2023-methylome-review|Iqbal 2023]]). Two protocols define opposite ends of the coverage axis, and two strategies define throughput ([[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]; [[10-Summaries/guo-2015-scrrbs-protocol|Guo 2015]]; [[10-Summaries/mulqueen-2018-sci-met|sci-MET]]; [[10-Summaries/zhang-2023-drop-bs|Drop-BS]]). See [[bisulfite-sequencing]] for the consolidated comparison table.

| Method | Year | Readout | Design | Key point |
|---|---|---|---|---|
| [[10-Summaries/guo-2015-scrrbs-protocol\|scRRBS]] | 2015 | 5mC | One-tube MspI-based reduced representation | ~1M CpGs but consistently the same CpGs across cells, ~70% of CGIs ([[10-Summaries/guo-2015-scrrbs-protocol\|Guo 2015]]) |
| [[10-Summaries/farlik-2015-scwgbs\|scWGBS]] | 2015 | 5mC | No pre-amplification | Region-set lineage plots of methylation cell-state dynamics ([[10-Summaries/farlik-2015-scwgbs\|Farlik 2015]]) |
| [[10-Summaries/clark-2017-scbs-seq-protocol\|scBS-seq]] | 2017 | 5mC | PBAT, five-round preamplification | ~50% of CpGs per cell ([[10-Summaries/clark-2017-scbs-seq-protocol\|Clark 2017]]) |
| [[10-Summaries/luo-2017-snmc-seq\|snmC-seq]] | 2017 | mCG + mCH | — | Founding cell-typing result: 16 mouse / 21 human cortical neuron clusters, ~500,000 CG-DMRs per species (68–73% >10 kb from any TSS), ISH-validated prediction that cluster mDL-2 differs in projection target; its DMRs are now the annotation reference higher-throughput methods depend on ([[10-Summaries/luo-2017-snmc-seq\|Luo 2017]]) |
| [[10-Summaries/luo-2018-snmc-seq2\|snmC-seq2]] | 2018 | 5mC | — | Robust single-cell methylome profiling ([[10-Summaries/luo-2018-snmc-seq2\|Luo 2018]]) |
| [[10-Summaries/mulqueen-2018-sci-met\|sci-MET]] | 2018 | 5mC | Combinatorial indexing, cytosine-depleted adaptors | Alignment rate 68 ± 8% vs the field's 25 ± 20% ([[10-Summaries/mulqueen-2018-sci-met\|sci-MET]]) |
| [[10-Summaries/nichols-2022-scimet-v2\|sciMETv2]] | 2022 | 5mC | — | Robust high-throughput scMethylation ([[10-Summaries/nichols-2022-scimet-v2\|Nichols 2022]]) |
| [[10-Summaries/zhang-2023-drop-bs\|Drop-BS]] | 2023 | 5mC | Droplets, in-droplet bisulfite conversion | Up to 10,000 cells in 2 days; 9× more library than bulk conversion ([[10-Summaries/zhang-2023-drop-bs\|Drop-BS]]) |
| [[10-Summaries/acharya-2024-scimet-cap\|sciMET-cap]] | 2024 | 5mC | Targeted capture | ~200–275k reads per cell; cluster on targets, call DMRs genome-wide from pooled off-target reads ([[10-Summaries/acharya-2024-scimet-cap\|Acharya 2024]]) |
| [[10-Summaries/nichols-2025-scimetv3\|sciMETv3]] | 2025 | 5mC | Three-tier combinatorial indexing | Atlas-scale profiling ([[10-Summaries/nichols-2025-scimetv3\|Nichols 2025]]) |
| [[10-Summaries/spix-2025-scdeep-mc\|scDEEP-mC]] | 2025 | 5mC, allele-resolved | High-coverage scWGBS | Hemi-methylation, X-inactivation, S-phase maintenance dynamics ([[10-Summaries/spix-2025-scdeep-mc\|Spix 2025]]) |
| [[30-Concepts/sctem-seq\|scTEM-seq]] | 2022 | SINE Alu methylation | Amplicon | Global-methylation proxy ([[10-Summaries/hunt-2022-sctem-seq\|Hunt 2022]]) |
| [[30-Concepts/simple-seq\|SIMPLE-seq]] | 2024 | 5mC + 5hmC | — | Joint, base resolution ([[10-Summaries/bai-2024-simple-seq\|Bai 2024]]) |
| scTAPS / scCAPS+ | 2025 | 5mC, 5hmC | Bisulfite-free | Separates 5mC from 5hmC at single-base resolution ([[10-Summaries/chen-2025-sctaps-sccaps-plus\|Chen 2025]]) |

### Multi-omic readouts with methylation

| Method | Year | Readout | Key point |
|---|---|---|---|
| [[10-Summaries/hou-2016-sctrio-seq\|scTrio-seq]] | 2016 | CNV + methylome + transcriptome | CNVs do not propagate to local methylation state ([[10-Summaries/hou-2016-sctrio-seq\|Hou 2016]]) |
| [[10-Summaries/clark-2018-scnmt-seq\|scNMT-seq]] | 2018 | Accessibility + methylation + transcription | Methylation–accessibility coupling strengthens along differentiation ([[10-Summaries/clark-2018-scnmt-seq\|Clark 2018]]) |
| [[30-Concepts/splicool-seq\|SpliCOOL-seq]] | 2026 | 5mC + accessibility | Split-pool barcoding; divergent decitabine vs azacitidine demethylation ([[10-Summaries/shen-2026-splicool-seq\|Shen 2026]]) |
| [[30-Concepts/scepi2-seq\|scEpi²-seq]] | 2025 | Histone mark + 5mC | ([[10-Summaries/geisenberger-2025-scepi2-seq\|Geisenberger 2025]]) |
| [[30-Concepts/6-base-cut-and-tag\|6-base-CUT&Tag]] | 2026 | 5mC + 5hmC at histone-marked fragments | ([[10-Summaries/tavares-2026-6-base-cut-tag\|Tavares 2026]]) |

## Computational tools

| Tool | Year | Input | Model | Note |
|---|---|---|---|---|
| [[10-Summaries/krueger-2011-bismark\|Bismark]] | 2011 | Bisulfite-seq reads | Aligner and methylation caller | ([[10-Summaries/krueger-2011-bismark\|Bismark]]) |
| [[10-Summaries/liu-2012-bis-snp\|Bis-SNP]] | 2012 | Directional bisulfite-seq | Joint SNP and methylation calling | ([[10-Summaries/liu-2012-bis-snp\|Bis-SNP]]) |
| [[10-Summaries/kremer-2024-methscan\|MethSCAn]] | 2024 | Single-cell bisulfite data | De novo VMR discovery | ([[10-Summaries/kremer-2024-methscan\|MethSCAn]]) |
| [[10-Summaries/zhou-2024-scdmv\|scDMV]] | 2024 | scBS-seq | Zero-one inflated beta mixture | Single-cell DMR detection ([[10-Summaries/zhou-2024-scdmv\|scDMV]]) |
| [[10-Summaries/rylaarsdam-2025-amethyst\|Amethyst]] | 2025 | sciMET | R package | Atlas-scale analysis; glial hyper-mCH and X-escape mCH ([[10-Summaries/rylaarsdam-2025-amethyst\|Amethyst]]) |
| [[10-Summaries/zhao-2025-mambacpg\|MambaCpG]] | 2025 | Single-cell CpG states | Mamba state-space model | CpG imputation ([[10-Summaries/zhao-2025-mambacpg\|MambaCpG]]) |
| [[10-Summaries/duan-2026-mist\|mist]] | 2026 | Single-cell methylation | Hierarchical Bayesian | Differential methylation along pseudotime ([[10-Summaries/duan-2026-mist\|mist]]) |
| [[10-Summaries/liang-2026-scmeth-imputation-benchmark\|Liang 2026]] | 2026 | Single-cell methylation | Imputation benchmark | First systematic scDNAm imputation benchmark; entropy and sparsity drive accuracy; BridgeCpG and divide-and-conquer ([[10-Summaries/liang-2026-scmeth-imputation-benchmark\|Liang 2026]]) |

Reviews: computational approaches in epigenetic research ([[10-Summaries/ghorbani-2019-comp-epigenetics|Ghorbani 2019]]); single-cell methylome analysis ([[10-Summaries/iqbal-2023-methylome-review|Iqbal 2023]]); long-read methylation analysis ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]); the long-read epigenome ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]]).

## Foundation models

Bulk-methylation foundation models arrived in 2024; the first single-cell one followed in 2025 ([[10-Summaries/delimacamillo-2024-cpgpt|CpGPT]]; [[10-Summaries/ying-2024-methylgpt|MethylGPT]]; [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]).

| Model | Year | Training data | Architecture | Note |
|---|---|---|---|---|
| [[10-Summaries/delimacamillo-2024-cpgpt\|CpGPT]] | 2024 | 155k Illumina-array samples | Each locus keyed by a DNA-language-model embedding | Imputes unmeasured CpGs across array platforms and species ([[10-Summaries/delimacamillo-2024-cpgpt\|CpGPT]]) |
| [[10-Summaries/ying-2024-methylgpt\|MethylGPT]] | 2024 | 49,156 EWAS-selected array CpGs | — | Predicts age and 10-year risk of 60 diseases (test AUC 0.72 in Generation Scotland) ([[10-Summaries/ying-2024-methylgpt\|MethylGPT]]) |
| [[10-Summaries/liang-2025-scdnam-gpt\|scDNAm-GPT]] | 2025 | Single-cell methylomes | Mamba | Reads every covered CpG of a cell (up to about 20M tokens) without genomic binning ([[10-Summaries/liang-2025-scdnam-gpt\|scDNAm-GPT]]) |

## Methylation as a timer: epimutation clocks

Two sources use methylation as a **timer** rather than as a cell-type fingerprint (see [[30-Concepts/methylation-clones-epimutation]] and [[30-Concepts/epigenetic-aging|methylation clocks]]):

- **AlphaBeta (plants)** estimates forward and backward epimutation rates from pedigree data and establishes the three properties a clock needs — neutral accumulation, somatic origin and demonstrable age-dating ([[10-Summaries/shahryary-2020-alphabeta|AlphaBeta]]).
- **EVOFLUx (human)** reads fluctuating CpGs from bulk methylation arrays across 1,976 lymphoid cancers to infer growth rate, malignancy age, epimutation rate and subclonal structure at clinical scale ([[10-Summaries/gabbutt-2025-evoflux|EVOFLUx]]).

Both share an unquantified limit: gain/loss equilibrium means the clock saturates, bounding how far back it can read (synthesis).

## Enzymatic machinery and core concepts

- [[cpg-island]] — unmethylated regulatory features.
- [[30-Concepts/dnmt]] — methyltransferase enzymes (maintenance + de novo).
- [[30-Concepts/uhrf1]] — DNMT1 maintenance cofactor.
- [[30-Concepts/tet-enzymes]] — active demethylation pathway.
- [[5hmc]] — oxidative intermediate / stable enhancer mark.
- [[30-Concepts/transposable-elements]] — silenced by methylation; [[30-Concepts/viral-mimicry]] when re-expressed.

## Key entities

- [[20-Entities/alexander-meissner]] — foundational methylation development review.
- [[20-Entities/fritz-sedlazeck]] — long-read methylation analysis.
- [[20-Entities/winston-timp]] — nanopore methylation pioneer.
- [[20-Entities/chengqi-yi]] — bisulfite-free chemistry (SIMPLE-seq, hmC-CATCH).
- [[20-Entities/chun-xiao-song]] — TAPS chemistry inventor.
- [[20-Entities/heather-lee]] — scTEM-seq, single-cell methylation in AML.
- [[20-Entities/xiaoying-fan]] — SpliCOOL-seq high-throughput multi-omics.
- [[20-Entities/joseph-costello]] — glioma methylation, EPICUP classifier.
- [[20-Entities/shankar-balasubramanian]] — 6-base sequencing (biomodal evoC).
- [[20-Entities/biomodal]] — 6-base sequencing kits (5mC + 5hmC).

## Open questions

- Methylation-calling accuracy across PacBio and ONT platforms has no community-standard benchmark ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).
- Is 5hmC a functional mark or only an intermediate? Unresolved ([[10-Summaries/bai-2024-simple-seq|Bai 2024]]; [[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).
- Single-cell methylation at scale: current methods are sparse, and the intersection with [[40-Topics/scdna-seq|scDNA-seq]] remains an open methodological frontier ([[10-Summaries/iqbal-2023-methylome-review|Iqbal 2023]]).
- What is the functional significance of non-CpG methylation (mCpH) in adult tissues, especially brain ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]])?
- Are HMAs (decitabine vs azacitidine) clinically interchangeable? Single-cell data argue no — divergent demethylation patterns, and a viral-mimicry response decoupled from raw methylation loss ([[10-Summaries/shen-2026-splicool-seq|Shen 2026]]; [[10-Summaries/hunt-2022-sctem-seq|Hunt 2022]]).
- How far back can epimutation clocks read before gain/loss equilibrium saturates them ([[10-Summaries/shahryary-2020-alphabeta|AlphaBeta]]; [[10-Summaries/gabbutt-2025-evoflux|EVOFLUx]])? (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — PacBio HiFi and ONT single-molecule reads that detect base modifications directly.
> - `hub` [[40-Topics/scdna-seq|scDNA-seq]] — Technologies that interrogate the DNA of single cells.

## All sources on this page

> [!info]- 48 summaries cited here
> - [[10-Summaries/acharya-2024-scimet-cap|Acharya 2024]]
> - [[10-Summaries/bai-2024-simple-seq|Bai 2024]]
> - [[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]
> - [[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]
> - [[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]
> - [[10-Summaries/delimacamillo-2024-cpgpt|CpGPT 2024]]
> - [[10-Summaries/duan-2026-mist|Duan 2026]]
> - [[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]
> - [[10-Summaries/flusberg-2010-smrt-methylation|Flusberg 2010]]
> - [[10-Summaries/fu-2025-longread-methylation|Fu 2025]]
> - [[10-Summaries/gabbutt-2025-evoflux|Gabbutt 2025]]
> - [[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]
> - [[10-Summaries/ghorbani-2019-comp-epigenetics|Ghorbani 2019]]
> - [[10-Summaries/guo-2015-scrrbs-protocol|Guo 2015]]
> - [[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]
> - [[10-Summaries/huang-2010-5hmc-bisulfite|Huang 2010]]
> - [[10-Summaries/hunt-2022-sctem-seq|Hunt 2022]]
> - [[10-Summaries/iqbal-2023-methylome-review|Iqbal 2023]]
> - [[10-Summaries/jones-2012-dna-methylation-functions|Jones 2012]]
> - [[10-Summaries/kim-2017-methylation-memory-review|Kim & Costello 2017]]
> - [[10-Summaries/kremer-2024-methscan|Kremer 2024]]
> - [[10-Summaries/krueger-2011-bismark|Krueger 2011]]
> - [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT 2025]]
> - [[10-Summaries/liang-2026-scmeth-imputation-benchmark|Liang 2026]]
> - [[10-Summaries/liu-2012-bis-snp|Liu 2012]]
> - [[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]]
> - [[10-Summaries/luo-2017-snmc-seq|Luo 2017]]
> - [[10-Summaries/luo-2018-snmc-seq2|Luo 2018]]
> - [[10-Summaries/mo-2023-stam-seq|Mo 2023]]
> - [[10-Summaries/mulqueen-2018-sci-met|Mulqueen 2018]]
> - [[10-Summaries/nam-2022-natgenet|Nam 2022]]
> - [[10-Summaries/nichols-2022-scimet-v2|Nichols 2022]]
> - [[10-Summaries/nichols-2025-scimetv3|Nichols 2025]]
> - [[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]
> - [[10-Summaries/roadmap-2015-111-epigenomes|Roadmap Epigenomics 2015]]
> - [[10-Summaries/rothbart-2014-histone-dna-language|Rothbart & Strahl 2014]]
> - [[10-Summaries/rylaarsdam-2025-amethyst|Rylaarsdam 2025]]
> - [[10-Summaries/shahryary-2020-alphabeta|Shahryary 2020]]
> - [[10-Summaries/shen-2026-splicool-seq|Shen 2026]]
> - [[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]
> - [[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]
> - [[10-Summaries/tahiliani-2009-tet1-5hmc|Tahiliani 2009]]
> - [[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]
> - [[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]
> - [[10-Summaries/ying-2024-methylgpt|MethylGPT 2024]]
> - [[10-Summaries/zhang-2023-drop-bs|Zhang 2023]]
> - [[10-Summaries/zhao-2025-mambacpg|Zhao 2025]]
> - [[10-Summaries/zhou-2024-scdmv|Zhou 2024]]
