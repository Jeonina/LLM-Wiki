---
type: concept
title: Single-cell variant calling
aliases: [scSNV calling, single-cell SNV detection, scDNA variant calling]
tags: [scDNA-seq, variant-calling, SNV, computational]
created: 2026-05-19
updated: 2026-10-12
paper_section: ["4.1"]
---

# Single-cell variant calling

> Algorithms for detecting somatic single-nucleotide variants and indels from single-cell DNA sequencing data, which is dominated by amplification artifacts, allelic dropout, and uneven coverage that conventional bulk callers (GATK, MuTect2) handle poorly ([[10-Summaries/valecha-2022-scsnv-review|Valecha 2022]]; [[10-Summaries/lahnemann-2021-natcomm|ProSolo]]).

> [!abstract] 한눈에
> Single-cell variant calling은 증폭 artifact, allele dropout, 고르지 않은 coverage가 섞인 single-cell DNA 데이터에서 체세포 SNV와 indel을 찾는 알고리즘이다 ([[10-Summaries/valecha-2022-scsnv-review|Valecha 2022]]). 도구들은 bulk caller의 diploid·균일 coverage 가정을 버리고 allele balance, 세포 계통수, 상보 가닥 같은 다른 단서를 쓰지만, single-cell에서만 보이는 변이는 여전히 대부분 검증되지 않는다 ([[10-Summaries/mckenna-2010-gatk|GATK]]; [[10-Summaries/wang-2014-nuc-seq|Wang 2014]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [모자이크 변이 검출력 시뮬레이터](../60-Explainers/mosaic-variant-calling.html)
<!-- /explainer-links -->

## Definition

Single-cell variant calling detects somatic single-nucleotide variants and indels from single-cell DNA sequencing data ([[10-Summaries/valecha-2022-scsnv-review|Valecha 2022]]). A 2020 community review classifies scDNA WGA failures into imbalanced allele proportions, allele dropout and complete site dropout ([[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]); conventional bulk callers (GATK, MuTect2) handle these poorly ([[10-Summaries/valecha-2022-scsnv-review|Valecha 2022]]; [[10-Summaries/lahnemann-2021-natcomm|ProSolo]]).

## Why it matters

- Because somatic evolution is asexual and recombination-free, the shared cell lineage tree can serve as a constraint for joint variant calling ([[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]).
- Better callers revise biological constants: matched to [[30-Concepts/pta|PTA]], SCAN2 put neuronal somatic SNV accumulation at **16.5 SNVs/year**, with the revision attributed to artifacts in the older amplification chemistries ([[10-Summaries/luquette-2022-neuron-scan2-indels|SCAN2]]).
- In 2020 the field knew of no scDNA-seq indel caller and no systematic comparison of SNV or CNV callers ([[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]).

## The bulk null model these tools reject

- **GATK is the substrate and the assumption.** Its locus-based traversal (all reads spanning each base, plus reference-ordered data) is the data model every single-cell caller inherits; what they replace is its **diploid, uniform-coverage prior**, which WGA violates ([[10-Summaries/mckenna-2010-gatk|GATK]]).
- The demonstration genotyper in that paper is explicitly naïve — 99.76% concordance but only 81.70% dbSNP rate against ~90% expected, i.e. an honestly-reported false-positive problem ([[10-Summaries/mckenna-2010-gatk|GATK]]).
- **Multi-locus traversals were never implemented** in the original framework and were flagged as memory-expensive — which is why haplotype-aware and phasing-based methods needed separate engineering rather than a walker ([[10-Summaries/mckenna-2010-gatk|GATK]]).
- **VarScan** is an early, aligner-agnostic bulk caller built on read-level filters and simple thresholds (coverage, base quality, supporting reads, variant frequency); it reports per-allele read counts rather than diploid genotypes ([[10-Summaries/koboldt-2009-varscan|VarScan]]).
- **MuTect** uses a free-allele-fraction Bayesian test plus artifact filters and a panel of normals, but assumes a matched normal and independent sequencing errors ([[10-Summaries/cibulskis-2013-mutect|MuTect]]).
- **LOH detection reuses the same logic in reverse**: restrict to ancestral heterozygous sites, then read allele fraction, calling tracts from ≥3 consecutive deviating SNPs ([[10-Summaries/smukowski-heil-2023-loh|Smukowski Heil 2023]]). In single cells this collides with allele dropout, which produces the identical signature (synthesis).

## Tools

### Per-cell callers on scDNA-seq

| Tool | Approach | Source |
|---|---|---|
| Monovar | First scSNV caller; multi-cell joint likelihood | ([[10-Summaries/zafar-2016-monovar\|Monovar]]) |
| SCcaller | Local-allele-frequency model | ([[10-Summaries/dong-2017-sccaller\|SCcaller]]) |
| ProSolo | Pairs bulk + single-cell | ([[10-Summaries/lahnemann-2021-natcomm\|ProSolo]]) |
| SCOUT | Leverages local genome territory for genotyping | ([[10-Summaries/tu-2021-scout-genotyper\|SCOUT]]) |
| LiRA | Validates singleton sSNVs by read-backed phasing with nearby germline heterozygous SNPs | ([[10-Summaries/bohrson-2019-lira\|LiRA]]) |
| SCAN2 | Adds a mutation-signature rescue step to SCAN-SNV's allele-balance model, plus the first single-cell somatic indel caller; matched to PTA rather than MDA | ([[10-Summaries/luquette-2022-neuron-scan2-indels\|SCAN2]]) |
| SIEVE | Calls single and double mutant genotypes from raw four-nucleotide counts conditional on an inferred cell phylogeny | ([[10-Summaries/kang-2022-sieve\|SIEVE]]) |
| MosaiCatcher v2 | Strand-seq workflow for single-cell structural-variant calling and genotyping; normalizes read counts by library size, GC correction and VST | ([[10-Summaries/weber-2023-mosaicatcher-v2\|MosaiCatcher v2]]) |

### Mosaic callers for bulk sequencing

| Tool | Approach | Source |
|---|---|---|
| MosaicHunter | Control-free mosaic SNV detection | ([[10-Summaries/huang-2017-mosaichunter\|MosaicHunter]]) |
| MosaicForecast | Random-forest classifier | ([[10-Summaries/dou-2020-mosaicforecast\|MosaicForecast]]) |
| DeepMosaic | Deep-learning mosaic caller | ([[10-Summaries/yang-2023-deepmosaic\|DeepMosaic]]) |

### Calling from RNA or chromatin reads

| Tool | Approach | Source |
|---|---|---|
| Monopogen | SNV calls from scRNA/scATAC | ([[10-Summaries/dou-2023-monopogen\|Monopogen]]) |
| SComatic | De novo somatic SNVs from scRNA-seq and scATAC-seq without matched DNA: pools reads per cell type, tests against a beta-binomial background error model fitted on non-neoplastic samples, and discards variants seen in more than one cell type as germline or artefact | ([[10-Summaries/muyas-2024-scomatic\|SComatic]]) |

### Other routes

- **Clone-level aggregation is the amplification-free alternative** to per-cell calling: cluster on copy number, treat each clone as pseudo-bulk, then call SNVs, breakpoints and allele-specific copy number per clone ([[10-Summaries/laks-2019-dlp-plus|DLP+]]).
- **Chemistry-side strand confirmation.** META-CS requires the variant on both complementary strands, calls SNVs from ≥4 reads (≥2 per strand), and does not depend on heterozygous germline SNPs, so it also works in haploid or aneuploid cells ([[10-Summaries/xing-2021-meta-cs|META-CS]]).
- **Genotype likelihoods downstream.** Tree inference can use genotype likelihoods instead of hard calls: CellPhy reads the VCF PL field ([[10-Summaries/kozlov-2022-cellphy|CellPhy]]).
- **Targeted re-amplification of droplet libraries.** SPLONGGET re-amplifies barcoded libraries with biotinylated multiplex PCR to genotype known driver sites ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).
- **Post-calling prioritisation.** SCARCE ranks variants by odds-ratio enrichment (Wald or Fisher test, Benjamini–Yekutieli FDR) in one cell group versus all others, with groups taken from ADT surface markers or variant clustering ([[10-Summaries/gillman-2026-scarce|SCARCE]]).

## Evidence and examples

**Benchmarks**

- [[10-Summaries/ha-2023-natmethods|Ha 2023]] benchmarks 11 strategies on a constructed reference standard from 6 mixed cell lines ([[10-Summaries/ha-2023-natmethods|Ha 2023]]).
- On synthetic diploid X data, SCAN2 raised sSNV sensitivity from 25% to 46% at similar FDR, and recovered 33.6% of spiked indels at <2% FDR where GATK HaplotypeCaller+VQSR had >99% FDR ([[10-Summaries/luquette-2022-neuron-scan2-indels|SCAN2]]).
- LiRA filtered 92% of phaseable MDA candidates as artifacts versus 2% of germline–germline pairs ([[10-Summaries/bohrson-2019-lira|LiRA]]).
- In simulations SIEVE's single-mutant recall was 0.16–18.55% above SCIPhI and 28.89–71.74% above Monovar ([[10-Summaries/kang-2022-sieve|SIEVE]]).
- Against DNA-confirmed mutations in 30 tumours SComatic's precision was 0.67–0.87 versus 0.06–0.24 for Strelka2, the next best, although Strelka2, VarScan2 and SCReadCounts had higher sensitivity ([[10-Summaries/muyas-2024-scomatic|SComatic]]).
- Using genotype likelihoods improved CellPhy's accuracy most at low (5×) depth ([[10-Summaries/kozlov-2022-cellphy|CellPhy]]).

**Bulk reference points**

- MuTect reached 95.6% sensitivity at 30× for AF 0.2 ([[10-Summaries/cibulskis-2013-mutect|MuTect]]).
- VarScan's per-allele counts let it detect ~1%-frequency SNPs in a ~6,000× pooled sample; pooled allele-frequency estimates correlated with known frequencies at r = 0.962, but high-VAF variants were slightly underestimated because variant-carrying short reads map less well ([[10-Summaries/koboldt-2009-varscan|VarScan]]).

**Coverage of sparse libraries**

- Untargeted SPLONGGET covered 0.01% of cells on average at known B-ALL driver sites ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).
- Targeted re-amplification raised on-target coverage 3,242-fold (DNA) and 4,402-fold (cDNA), and on average 18.4% of cells (range 0–75.1%) could then be genotyped; targeted VAFs correlated with MissionBio Tapestri at PCC 0.92 ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).

**Biological findings**

- Somatic indels accumulate at ~3/year per neuron and are enriched in conserved sequence and neuronal enhancers ([[10-Summaries/luquette-2022-neuron-scan2-indels|SCAN2]]).

## Contested points

- **Validation is the recurring weak point.** Duplex sequencing of nuc-seq calls found that only **19.4–27.0% of single-cell-only ("de novo") mutations validated**, against 90.5–64.8% of subclonal and 94.4–99.7% of clonal calls ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]). Read the other way, the majority of single-cell-only calls are artifact even in a high-quality library — which is why the field converged on orthogonal duplex confirmation ([[50-Notes/single-cell-duplex-sequencing]]) (synthesis).
- **The PL field is not a standard.** It means different things in different callers: SC-Caller's must be converted before use, while Monovar writes a standard PL ([[10-Summaries/kozlov-2022-cellphy|CellPhy]]).
- **Indels are a chemistry result as much as an algorithm result.** Indels were effectively unmeasurable before PTA because MDA's polymerase-slippage artifacts sit on top of the indel signal (synthesis).
- **An old problem in a new data type.** The abundance-inversion problem these callers negotiate — where an artifact in a well-amplified region outweighs a true signal in a poorly-amplified one — was first named a decade earlier in [[30-Concepts/single-cell-genome-assembly|single-cell assembly]] ([[10-Summaries/peng-2012-idba-ud|IDBA-UD]]) (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/pta|PTA]] — Primary template amplification, the chemistry SCAN2 is matched to.
> - `concept` [[30-Concepts/single-cell-genome-assembly|Single-cell genome assembly]] — Where the abundance-inversion problem was first named.
> - `hub` [[40-Topics/scdna-seq|scDNA-seq]] — Technologies that interrogate the DNA of single cells.
> - `hub` [[40-Topics/mosaic-variant-calling|Mosaic variant calling]] — Detecting low-allele-frequency somatic variants in bulk, single-cell DNA, or scRNA/scATAC.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Strand-paired single-molecule sequencing used to confirm single-cell calls.

## All sources on this page

> [!info]- 27 summaries cited here
> - [[10-Summaries/bohrson-2019-lira|Bohrson 2019]]
> - [[10-Summaries/cibulskis-2013-mutect|Cibulskis 2013]]
> - [[10-Summaries/dong-2017-sccaller|Dong 2017]]
> - [[10-Summaries/dou-2020-mosaicforecast|Dou 2020]]
> - [[10-Summaries/dou-2023-monopogen|Dou 2023]]
> - [[10-Summaries/gillman-2026-scarce|Gillman 2026]]
> - [[10-Summaries/ha-2023-natmethods|Ha 2023]]
> - [[10-Summaries/huang-2017-mosaichunter|Huang 2017]]
> - [[10-Summaries/kang-2022-sieve|Kang 2022]]
> - [[10-Summaries/koboldt-2009-varscan|Koboldt 2009]]
> - [[10-Summaries/kozlov-2022-cellphy|Kozlov 2022]]
> - [[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]
> - [[10-Summaries/lahnemann-2021-natcomm|Lähnemann 2021]]
> - [[10-Summaries/laks-2019-dlp-plus|Laks 2019]]
> - [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]
> - [[10-Summaries/mckenna-2010-gatk|McKenna 2010]]
> - [[10-Summaries/muyas-2024-scomatic|Muyas 2024]]
> - [[10-Summaries/pancikova-2025-splongget|Pančíková 2025 (bioRxiv preprint)]]
> - [[10-Summaries/peng-2012-idba-ud|Peng 2012]]
> - [[10-Summaries/smukowski-heil-2023-loh|Smukowski Heil 2023]]
> - [[10-Summaries/tu-2021-scout-genotyper|Tu 2021]]
> - [[10-Summaries/valecha-2022-scsnv-review|Valecha 2022]]
> - [[10-Summaries/wang-2014-nuc-seq|Wang 2014]]
> - [[10-Summaries/weber-2023-mosaicatcher-v2|Weber 2023]]
> - [[10-Summaries/xing-2021-meta-cs|Xing 2021]]
> - [[10-Summaries/yang-2023-deepmosaic|Yang 2023]]
> - [[10-Summaries/zafar-2016-monovar|Zafar 2016]]
