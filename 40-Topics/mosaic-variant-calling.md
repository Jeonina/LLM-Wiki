---
type: topic
title: Mosaic variant calling
explainer: mosaic-variant-calling
aliases: [mosaic SNV calling, low-VAF variant calling, mosaicism callers]
tags: [mosaicism, variant-calling, SNV, low-VAF, benchmarking]
created: 2026-05-19
updated: 2026-10-12
paper_section: ["4.1"]
---

# Mosaic variant calling

> The algorithmic problem of detecting low-allele-frequency somatic variants from sequencing data — bulk DNA, single-cell DNA, or scRNA/scATAC. Mosaic variants violate the assumptions of germline callers (variant allele frequency ≪ 50%); specialized callers and reference benchmarks have proliferated ([[10-Summaries/ha-2023-natmethods|Ha 2023]]).

> [!abstract] 한눈에
> mosaic 변이는 VAF가 50%보다 훨씬 낮아 germline caller의 가정이 맞지 않으므로, bulk·single-cell·scRNA/scATAC 데이터마다 전용 caller가 따로 발전했다 ([[10-Summaries/ha-2023-natmethods|Ha 2023]]; [[10-Summaries/muyas-2024-scomatic|SComatic]]). single-cell에서만 나온 call은 duplex 같은 독립 검증을 거쳐야 하며, 증폭 화학이 바뀌자 뉴런의 SNV 축적 속도 추정치 자체가 수정되었다 ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]; [[10-Summaries/luquette-2022-neuron-scan2-indels|SCAN2]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [모자이크 변이 검출력 시뮬레이터](../60-Explainers/mosaic-variant-calling.html)
<!-- /explainer-links -->

## Key points

- **Germline callers do not fit mosaic variants.** Their VAF ≪ 50% breaks the germline assumptions, and Ha 2023 benchmarked 11 mosaic-calling strategies against a reference standard ([[10-Summaries/ha-2023-natmethods|Ha 2023]]).
- **Single-cell-only calls need an independent arbiter.** Only 19.4–27.0% of single-cell-only mutation calls survived orthogonal duplex confirmation ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]), and SCAN2 on PTA neurons revised the neuronal SNV accumulation rate to 16.5 SNVs/year, attributing the change to artifacts in older amplification chemistries ([[10-Summaries/luquette-2022-neuron-scan2-indels|SCAN2]]).
- **Per-cell callers cannot recover a lost allele.** A mutation lost to dropout or LOH cannot be recovered from within one cell; SCIΦ instead uses the cell lineage tree as a prior and can assign a mutation to a cell with zero variant-read support ([[10-Summaries/singer-2018-sciphi|SCIΦ]]).
- **Calling has moved beyond scDNA.** SComatic calls somatic SNVs de novo from scRNA/scATAC data without matched DNA ([[10-Summaries/muyas-2024-scomatic|SComatic]]).
- **Rare clones need enrichment rather than per-cell thresholds.** SCARCE ranks rare-clone variants by 1-vs-all enrichment testing and isolates a 10-cell KG-1 clone among 16,316 cells ([[10-Summaries/gillman-2026-scarce|SCARCE]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/single-cell-variant-calling|Single-cell variant calling]] — The computational problem: calling SNVs and indels from data dominated by amplification artifacts, allelic dropout and uneven coverage.
> - `concept` [[30-Concepts/allele-dropout|Allele dropout]] — One parental allele fails to amplify, so a heterozygous variant looks homozygous.
> - `concept` [[30-Concepts/pta|PTA]] — Primary template amplification, the scWGA chemistry behind SCAN2's revised neuronal rates.
> - `note` [[50-Notes/single-cell-duplex-sequencing|Single-cell duplex sequencing]] — How strand-paired error correction reached single cells.
> - `note` [[50-Notes/pta-inflection-point|The PTA inflection point]] — When PTA displaced MDA for cohort-scale mosaicism studies.

## Bulk and control-free callers

Callers built for bulk DNA, from threshold heuristics to models that work without a matched control.

| Tool | Year | Input | Model | Note |
|---|---|---|---|---|
| [[10-Summaries/koboldt-2009-varscan\|VarScan]] | 2009 | Individual and pooled samples | Thresholds on coverage, base quality, supporting reads, variant frequency | SNP/indel caller; historical baseline for low-VAF detection ([[10-Summaries/koboldt-2009-varscan\|VarScan]]) |
| [[10-Summaries/chen-2009-breakdancer\|BreakDancer]] | 2009 | Paired-end reads | Clusters of anomalously mapped read pairs | Early bulk SV caller; its tumour-only putative somatic indels all validated as germline ([[10-Summaries/chen-2009-breakdancer\|BreakDancer]]) |
| [[10-Summaries/cibulskis-2013-mutect\|MuTect]] | 2013 | Tumour–normal | Bayesian likelihood ratio with a free allele fraction; panel of normals | Low-AF somatic SNVs; virtual-tumor benchmarking ([[10-Summaries/cibulskis-2013-mutect\|MuTect]]) |
| [[10-Summaries/huang-2017-mosaichunter\|MosaicHunter]] | 2017 | Unpaired, trio or paired WGS/WES | Bayesian genotyper | Postzygotic SNVs without a matched control ([[10-Summaries/huang-2017-mosaichunter\|MosaicHunter]]) |
| [[10-Summaries/dou-2020-mosaicforecast\|MosaicForecast]] | 2020 | Bulk sequencing, no matched control | Read-based phasing + random forest | Mosaic SNVs and indels ([[10-Summaries/dou-2020-mosaicforecast\|MosaicForecast]]) |
| [[10-Summaries/yang-2023-deepmosaic\|DeepMosaic]] | 2023 | WGS/WES, no matched control | CNN on pileup images | Control-independent mosaic SNVs ([[10-Summaries/yang-2023-deepmosaic\|DeepMosaic]]) |

## Single-cell callers

Callers designed for amplified single-cell genomes, or for single-cell data of other modalities.

| Tool | Year | Input | Model | Note |
|---|---|---|---|---|
| [[10-Summaries/zafar-2016-monovar\|Monovar]] | 2016 | scDNA-seq, many cells | Pools evidence across cells | Assumes independence across sites ([[10-Summaries/singer-2018-sciphi\|SCIΦ]]; [[10-Summaries/zafar-2016-monovar\|Monovar]]) |
| [[10-Summaries/dong-2017-sccaller\|SCcaller]] | 2017 | MDA scWGS | Local allelic amplification bias, per cell | Needs germline SNPs (unavailable for panel data); cannot recover mutations lost to dropout or LOH ([[10-Summaries/singer-2018-sciphi\|SCIΦ]]; [[10-Summaries/dong-2017-sccaller\|SCcaller]]) |
| [[10-Summaries/bohrson-2019-lira\|LiRA]] | 2019 | MDA single cells | Read-backed phasing with nearby germline SNPs | Validates singleton sSNVs ([[10-Summaries/bohrson-2019-lira\|LiRA]]) |
| [[10-Summaries/lahnemann-2021-natcomm\|ProSolo]] | 2021 | One MDA cell + a bulk sample | Joint probabilistic model of the cell and bulk | ([[10-Summaries/lahnemann-2021-natcomm\|ProSolo]]) |
| [[10-Summaries/tu-2021-scout-genotyper\|SCOUT]] | 2021 | Single cell | Base counts from the local genome territory | Genotyping without external data ([[10-Summaries/tu-2021-scout-genotyper\|SCOUT]]) |
| [[10-Summaries/luquette-2022-neuron-scan2-indels\|SCAN2]] | 2022 | PTA scWGS | Allele-balance model + signature rescue | PTA-native; first single-cell indel caller; ~3 indels/year and 16.5 SNVs/year per neuron ([[10-Summaries/luquette-2022-neuron-scan2-indels\|SCAN2]]) |
| [[10-Summaries/dou-2023-monopogen\|Monopogen]] | 2023 | scRNA, snRNA, scATAC or scDNA | Linkage disequilibrium with a population reference | ([[10-Summaries/dou-2023-monopogen\|Monopogen]]) |
| [[10-Summaries/muyas-2024-scomatic\|SComatic]] | 2024 | scRNA/scATAC, no matched DNA | Reads pooled by cell type; beta-binomial background error | De novo somatic SNVs; per-cell-type burdens and signatures ([[10-Summaries/muyas-2024-scomatic\|SComatic]]) |
| [[10-Summaries/gillman-2026-scarce\|SCARCE]] | 2026 | Tapestri/VCF scDNA | Light filtering, then 1-vs-all enrichment testing | Ranks rare-clone variants; isolates a 10-cell KG-1 clone among 16,316 cells ([[10-Summaries/gillman-2026-scarce\|SCARCE]]) |

## Lineage-aware joint calling

- **The tree as a prior.** Rather than calling per cell or by pooling, SCIΦ uses the cell lineage tree as a prior, so a mutation can be assigned to a cell with very low or even zero variant-read support because the tree places it there ([[10-Summaries/singer-2018-sciphi|SCIΦ]]).
- **Its critique of the alternatives.** GATK and SAMtools assume bulk noise profiles; Monovar pools across cells but assumes independence across sites; SCcaller models local allelic amplification bias but works per cell, needs germline SNPs and cannot recover mutations lost to dropout or LOH ([[10-Summaries/singer-2018-sciphi|SCIΦ]]; [[10-Summaries/zafar-2016-monovar|Monovar]]; [[10-Summaries/dong-2017-sccaller|SCcaller]]).
- **A structural limit.** No per-cell caller can recover an absent allele from within one cell ([[10-Summaries/singer-2018-sciphi|SCIΦ]]).

## Validation and benchmarks

- **Reference benchmark.** Ha 2023 is a comprehensive benchmark of 11 mosaic-calling strategies ([[10-Summaries/ha-2023-natmethods|Ha 2023]]).
- **Duplex cross-benchmark.** SMaHT compared duplex-sequencing methods on the same samples ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]); see [[40-Topics/duplex-sequencing]] for fidelity at extreme low VAF.
- **Ultra-rare SNVs in bulk.** SMM-seq uses RCA-based multi-copy consensus for ultra-rare SNVs in bulk DNA, calibrated against single-cell results from the same liver samples ([[10-Summaries/maslov-2022-smm-seq|SMM-seq]]).
- **Single-cell-only calls.** Only 19.4–27.0% of single-cell-only mutation calls survived orthogonal duplex confirmation ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]).
- **Chemistry changes a biological number.** SCAN2 revised the neuronal SNV accumulation rate to 16.5 SNVs/year, attributing the revision to artifacts in older amplification chemistries ([[10-Summaries/luquette-2022-neuron-scan2-indels|SCAN2]]). It is the sharpest case in the corpus of chemistry setting a biological number, and with Wang 2014 it points one way: single-cell-only calls need an independent arbiter (synthesis).

## Reviews

- [[10-Summaries/valecha-2022-scsnv-review|Valecha 2022]] — somatic SNV calling from scDNA-seq data.
- [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]] — advances in scDNA-seq for somatic mosaicism.

## Open questions

- Per-cell call sensitivity at <1% VAF is still tool-dependent. (synthesis)
- Mutation-spectrum biases vary by caller. (synthesis)
- Most callers ignore copy-number state; integration with CNV context is open. (synthesis)
- When the lineage tree is wrong, tree-as-prior calling manufactures correlated false positives; this risk is not addressed ([[10-Summaries/singer-2018-sciphi|SCIΦ]]). (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one body.
> - `hub` [[40-Topics/scdna-seq|Single-cell DNA sequencing]] — Technologies that interrogate the DNA of single cells, by scWGA or by strand-paired single-molecule reads.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Calling a base only when both strands of a molecule agree; fidelity at extreme low VAF.

## All sources on this page

> [!info]- 22 summaries cited here
> - [[10-Summaries/bohrson-2019-lira|Bohrson 2019]]
> - [[10-Summaries/chen-2009-breakdancer|Chen 2009]]
> - [[10-Summaries/cibulskis-2013-mutect|Cibulskis 2013]]
> - [[10-Summaries/dong-2017-sccaller|Dong 2017]]
> - [[10-Summaries/dou-2020-mosaicforecast|Dou 2020]]
> - [[10-Summaries/dou-2023-monopogen|Dou 2023]]
> - [[10-Summaries/gillman-2026-scarce|Gillman 2026]]
> - [[10-Summaries/ha-2023-natmethods|Ha 2023]]
> - [[10-Summaries/huang-2017-mosaichunter|Huang 2017]]
> - [[10-Summaries/koboldt-2009-varscan|Koboldt 2009]]
> - [[10-Summaries/lahnemann-2021-natcomm|Lähnemann 2021]]
> - [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]
> - [[10-Summaries/maslov-2022-smm-seq|Maslov 2022]]
> - [[10-Summaries/muyas-2024-scomatic|Muyas 2024]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/singer-2018-sciphi|Singer 2018]]
> - [[10-Summaries/tu-2021-scout-genotyper|Tu 2021]]
> - [[10-Summaries/valecha-2022-scsnv-review|Valecha 2022]]
> - [[10-Summaries/wang-2014-nuc-seq|Wang 2014]]
> - [[10-Summaries/yang-2023-deepmosaic|Yang 2023]]
> - [[10-Summaries/zafar-2016-monovar|Zafar 2016]]
> - [[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]
