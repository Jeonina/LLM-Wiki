---
type: topic
title: Single-cell DNA sequencing (scDNA-seq)
aliases: [single-cell DNA sequencing, scDNA-seq, scDNAseq]
tags: [single-cell, scDNA-seq, methods]
created: 2026-05-11
updated: 2026-10-12
paper_section: ["3.1"]
---

# Single-cell DNA sequencing (scDNA-seq)

> Umbrella term for technologies that interrogate the DNA of single cells — either by amplifying single-cell genomes ([[scwga]] + scWGS) or by reading single DNA molecules with strand-paired error correction ([[40-Topics/duplex-sequencing]]) — giving single-cell resolution of somatic genomic variation that bulk DNA sequencing cannot detect ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

> [!abstract] 한눈에
> scDNA-seq는 단일 세포 게놈을 증폭해 읽는 scWGA + scWGS와, 두 가닥을 짝지어 오류를 걸러내는 단일 분자 duplex sequencing이라는 두 갈래로 나뉜다 ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). 어떤 방법도 fidelity, co-presence, phenotypic association을 한꺼번에 최대로 얻지 못하며, 세포당 데이터 양과 세포 수 사이에서 균형을 잡아야 한다 ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]; [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).

## Key points

- **Two branches with opposite strengths.** scWGA + scWGS assigns variants to specific cells but carries amplification errors (allelic dropout, single-strand dropout, polymerase error); duplex sequencing reaches error rates as low as ~10⁻¹⁶ but mostly cannot assign variants to cells ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **DNA is the hardest single-cell layer.** The genome is 20–50× larger than the transcribed or accessible genome and each locus has only two molecules per cell, which is why scRNA-seq and scATAC-seq matured years earlier ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Capabilities, not chemistries, organise the design space.** Fidelity, co-presence and phenotypic association trade off, so no single method is universally best ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]).
- **Depth per cell versus cells per experiment is the field's central trade-off.** PTA reaches ~95% genome coverage per cell while DLP+ scales to >10,000 cells at very low per-cell coverage ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).
- **Multi-omic extensions link genotype to phenotype.** GoT pairs genotype with RNA and GoT–ChA with chromatin accessibility on droplet platforms ([[10-Summaries/nam-2019-got|GoT]]; [[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/scwga|scWGA]] — Amplifying the ~6 pg of DNA in one diploid cell enough to sequence it; the central technical challenge.
> - `concept` [[30-Concepts/pta|PTA]] — Φ29 amplification with chain terminators that favours priming from the native template.
> - `concept` [[30-Concepts/dlp-plus|DLP+]] — Tn5-based microfluidic method trading per-cell coverage for >10,000 cells per run.
> - `concept` [[30-Concepts/meta-cs|META-CS]] — The only duplex-sequencing method applied to single cells rather than bulk DNA.
> - `concept` [[30-Concepts/scdna-capabilities-framework|scDNA capabilities framework]] — Fidelity, co-presence and phenotypic association as the axes of scDNA-seq design.
> - `concept` [[30-Concepts/got-cha|GoT–ChA]] — Somatic genotype and chromatin accessibility from the same nucleus in 10x scATAC droplets.

## The two methodological branches

scDNA-seq encompasses two methodological branches ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]):

| Branch | Members | Variant assignment | Main limitation |
|---|---|---|---|
| scWGA + scWGS | [[scwga]] methods — [[dop-pcr\|DOP-PCR]], [[mda\|MDA]], [[30-Concepts/pta\|PTA]], [[malbac\|MALBAC]], LIANTI, PicoPLEX, [[dlp-plus\|DLP+]] — followed by short- or long-read sequencing of the amplicon | To specific cells | Amplification-induced errors: allelic dropout, single-strand dropout, polymerase error ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| Single-molecule duplex sequencing | [[40-Topics/duplex-sequencing\|Duplex sequencing]]: BotSeqS, NanoSeq, CODEC, HiDEF-seq, SMM-seq; [[meta-cs]] for single-cell duplex | Mostly per molecule only, except [[30-Concepts/meta-cs\|META-CS]] | Watson and Crick strands are barcoded and must agree, giving error rates as low as ~10⁻¹⁶ (HiDEF-seq), at the cost of per-cell assignment ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |

[[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]] frames the design space through three capabilities ([[30-Concepts/scdna-capabilities-framework]]; [[scdna-capabilities-framework]]): **fidelity** (detecting low-mosaicism variants), **co-presence** (which variants co-occur in the same cell) and **phenotypic association** (linking genotype to RNA, chromatin or protein) ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]).

## Why it matters, and how the field got here

- **The obstacle.** The human genome is 20–50× larger than the transcribed or chromatin-accessible genomes, and each locus has only two molecules per cell, so scDNA-seq needs either amplification (introducing errors) or single-molecule chemistry (sacrificing per-cell assignment) ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **The lag.** For two decades this was the major obstacle; scRNA-seq and scATAC-seq matured years ahead of scDNA-seq for this reason ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **The chemistry arc.** Low-coverage [[30-Concepts/dop-pcr|DOP-PCR]] (2008) gave way to [[30-Concepts/mda|MDA]] and [[30-Concepts/malbac|MALBAC]] (2010s) and then PTA plus duplex sequencing (2020s), which made routine human-tissue mosaicism and lineage-tracing studies feasible ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Early primary work.** Pre-2016 methodology includes nuc-seq with G2/M input ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]), microfluidic targeted sequencing of 1,479 cells ([[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]) and two 2015 WGA benchmarks ([[10-Summaries/hou-2015-wga-comparison|Hou 2015]]; [[10-Summaries/huang-2015-scwga-review|Huang 2015]]). See [[40-Topics/whole-genome-amplification]] for the amplification chemistry in detail.

## Depth per cell versus cells per experiment

- The axis that organises the field is stated most clearly by Gawad 2014: "a carefully calibrated balance in the trade-off between the amount of data obtained per cell versus the number of cells that can be practically analyzed" ([[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).
- PTA reaches ~95% genome coverage per cell, while DLP+ scales to >10,000 cells at very low per-cell coverage ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- The same axis reappears in single-cell methylation ([[30-Concepts/bisulfite-sequencing]]). (synthesis)

## Multi-omic extensions

| Method | Year | Pairs DNA with | Design | Source |
|---|---|---|---|---|
| [[30-Concepts/got\|GoT]] ([[got]]) | 2019 | RNA | Droplet; genotype + transcriptome | ([[10-Summaries/nam-2019-got\|GoT]]) |
| [[30-Concepts/got-cha\|GoT–ChA]] ([[got-cha]]) | 2024 | Chromatin accessibility | Droplet; genotype + chromatin | ([[10-Summaries/izzo-2024-got-cha\|GoT–ChA]]) |
| [[30-Concepts/daf-seq\|DAF-seq]] | 2025 | Chromatin (single-molecule) | Single-molecule chromatin + DNA sequence | ([[10-Summaries/swanson-2025-daf-seq\|DAF-seq]]) |
| [[30-Concepts/gt-seq\|G&T-seq]] | — | RNA | Physical separation of DNA and RNA | ([[gt-seq]]) |

## Analysis tooling

| Tool | Year | Data | What it does |
|---|---|---|---|
| [[10-Summaries/garvin-2015-natmethods\|Ginkgo]] | 2015 | scDNA-seq | Interactive analysis of single-cell CNVs ([[10-Summaries/garvin-2015-natmethods\|Garvin 2015]]) |
| [[10-Summaries/wang-2020-scope\|SCOPE]] | 2020 | scDNA-seq | Normalization and copy-number estimation ([[10-Summaries/wang-2020-scope\|Wang 2020]]) |
| [[10-Summaries/liu-2024-cot\|CoT]] | 2024 | Per-cell bin counts | Chunked tokens into a six-layer transformer autoencoder; mean ARI 0.99 vs 0.97 for the convolutional rcCAE on simulated tetraploid data with 19 clones ([[10-Summaries/liu-2024-cot\|Liu 2024]]) |
| [[10-Summaries/sanders-2020-sctrip\|scTRIP]] | 2020 | Strand-seq | Structural variants and complex rearrangements; the original MosaiCatcher ([[10-Summaries/sanders-2020-sctrip\|Sanders 2020]]) |
| [[10-Summaries/weber-2023-mosaicatcher-v2\|MosaiCatcher v2]] | 2023 | Strand-seq | Workflow from FASTQ to single-cell SV calls, with ArbiGent genotyping and scNOVA modules ([[10-Summaries/weber-2023-mosaicatcher-v2\|Weber 2023]]) |
| [[10-Summaries/chitsaz-2011-velvet-sc\|Velvet-SC]] | 2011 | Single-cell bacterial short reads | De novo assembly of single-cell genomes ([[10-Summaries/chitsaz-2011-velvet-sc\|Chitsaz 2011]]) |
| [[10-Summaries/peng-2012-idba-ud\|IDBA-UD]] | 2012 | Single-cell and metagenomic reads with highly uneven depth | De novo assembly ([[10-Summaries/peng-2012-idba-ud\|Peng 2012]]) |
| [[10-Summaries/bankevich-2012-spades\|SPAdes]] | 2012 | Single-cell reads | Genome assembly algorithm applied to single-cell sequencing ([[10-Summaries/bankevich-2012-spades\|Bankevich 2012]]) |

## Applications

- **Somatic mosaicism** — detection of low-VAF variants in single cells ([[40-Topics/somatic-mosaicism]]; [[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]; [[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]]).
- **Lineage tracing** — natural mutation accumulation (~2–4 per division) as endogenous lineage markers in human tissue ([[30-Concepts/lineage-tracing]]; [[lineage-tracing]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Clonal hematopoiesis** and **developmental mutation timing** ([[40-Topics/clonal-hematopoiesis]]; [[30-Concepts/developmental-mutation-timing]]).
- **Pre-implantation genetic screening** — aneuploidy and CNV detection from single embryonic cells ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Cancer subclonal evolution** — joint detection of mutations and inference of clonal hierarchy ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Microbial dark matter** is among the application areas named by Evrony 2021 ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]).

Worked examples:

- The Walsh lab tracks human cortical neuron lineages via [[pta]] of single neurons ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- 40% of mid-gestation human prenatal neurons harbour complex CNV (Diane 2025 preprint reference) ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- DOP-PCR showed 49% of single cells in human early cleavage-stage embryos to be aneuploid ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

## Key people

- [[20-Entities/diane-d-shao]] — first author of the keystone 2025 review.
- [[20-Entities/christopher-walsh]] — Walsh lab; brain mosaicism program.
- [[20-Entities/charles-gawad]] — foundational 2016 review; pediatric oncology methods.
- [[20-Entities/stephen-quake]] — microfluidic single-cell genomics pioneer.
- [[20-Entities/gilad-evrony]] — applications-framework architect.
- [[20-Entities/dan-a-landau]] — Landau Lab; GoT and GoT–ChA methods.
- [[20-Entities/thierry-voet]] — G&T-seq; KU Leuven LISCO.
- [[20-Entities/andrew-b-stergachis]] — Fiber-seq and DAF-seq lineage.

## Reviews and surveys

- [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]] — keystone 2025 review; current state of the field.
- [[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]] — foundational 2016 review; pre-PTA landscape.
- [[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]] — applications and capabilities framework.
- [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]] — single-cell and spatial multi-omics methods.
- [[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]] — multi-omics technological landscape.
- [[10-Summaries/heumos-2023-best-practices|Heumos 2023]] — best practices for single-cell analysis.
- [[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]] and [[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]] — somatic mosaicism reviews.

## Open questions

- Where does scDAF-seq (single-cell, single-molecule, ~99% genome) win over GoT–ChA (10⁵ cells, single chromatin modality) ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]] vs [[10-Summaries/izzo-2024-got-cha|GoT–ChA]])?
- Throughput vs depth: PTA reaches ~95% genome coverage per cell while DLP+ scales to >10,000 cells at very low per-cell coverage; the right operating point for a given biological question is rarely benchmarked ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- The fidelity vs co-presence vs phenotypic association trade-off means no single method is universally best ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]).
- Cost: can single-cell duplex sequencing be made cost-competitive for cohort-scale studies? (synthesis)
- How well does imputation-based multi-omic integration (e.g., GoT–ChA + DOGMA via mt-variant bridges) generalise beyond MPN? (synthesis)
- Is there a "single-molecule, per-fiber" extension of GoT / GoT–ChA waiting to be built — the analogue to what DAF-seq is to Fiber-seq? (synthesis)
- Notes not yet written: (a) droplet-scale vs single-molecule scDNA-seq trade-offs; (b) the PTA inflection point that enabled current applications; (c) a "what capability does my question need?" decision tree from the Evrony framework. (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/whole-genome-amplification|Whole-genome amplification]] — Biochemical methods that bridge the ~6 pg of DNA in one cell to sequencing input.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Single-molecule strategy that calls a base only when both strands agree.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one body.
> - `hub` [[40-Topics/clonal-hematopoiesis|Clonal hematopoiesis]] — Age-related expansion of a blood stem-cell clone carrying a driver mutation.

## All sources on this page

> [!info]- 23 summaries cited here
> - [[10-Summaries/bankevich-2012-spades|Bankevich 2012]]
> - [[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]
> - [[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]]
> - [[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]
> - [[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]
> - [[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]
> - [[10-Summaries/garvin-2015-natmethods|Garvin 2015]]
> - [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]
> - [[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]
> - [[10-Summaries/heumos-2023-best-practices|Heumos 2023]]
> - [[10-Summaries/hou-2015-wga-comparison|Hou 2015]]
> - [[10-Summaries/huang-2015-scwga-review|Huang & Xie 2015]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/liu-2024-cot|Liu 2024 (Brief Bioinform)]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
> - [[10-Summaries/peng-2012-idba-ud|Peng 2012]]
> - [[10-Summaries/sanders-2020-sctrip|Sanders 2020]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
> - [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]
> - [[10-Summaries/wang-2014-nuc-seq|Wang 2014]]
> - [[10-Summaries/wang-2020-scope|Wang 2020]]
> - [[10-Summaries/weber-2023-mosaicatcher-v2|Weber 2023]]
