---
type: summary
title: "Laks et al. 2019 — Clonal decomposition and DNA replication states defined by scaled single-cell genome sequencing (DLP+)"
source: "[[00-Sources/papers/Clonal Decomposition and DNA Replication States Defined by Scaled Single-Cell Genome Sequencing]]"
source_kind: paper
author: "Emma Laks, Andrew McPherson, Steven Poon, ... Samuel Aparicio, Sohrab P. Shah (corresponding)"
published: 2019-11-14
ingested: 2026-08-10
doi: "10.1016/j.cell.2019.10.026"
journal: "Cell"
tags: [DLP+, amplification-free, tagmentation, nanowell, copy-number, aneuploidy, replication-state, clonal-decomposition, imaging-QC, resource]
entities: ["[[nicholas-navin]]"]
concepts: ["[[dlp-plus]]", "[[scwga]]", "[[scwga-chemistries]]", "[[tn5-tagmentation]]", "[[pseudo-bulk]]", "[[replication-timing]]", "[[phylogenetic-inference]]", "[[structural-variants]]", "[[combinatorial-indexing]]"]
topics: ["[[cancer-clonal-evolution]]", "[[scdna-cancer-applications]]", "[[whole-genome-amplification]]"]
---

**Citation:** Laks et al. (2019) — *Clonal decomposition and DNA replication states defined by scaled single-cell genome sequencing* — *Cell* 179, 1207–1221.e22. [DOI](https://doi.org/10.1016/j.cell.2019.10.026)

# Laks 2019 — DLP+

> The amplification-free branch of single-cell genomics, scaled. DLP+ replaces custom microfluidics with off-the-shelf piezo dispensing into commodity nanowell arrays, adds **real-time imaging before reagent dispensing** so doublets and debris are excluded before library prep, and delivers a resource of **51,926 single-cell genomes**. No WGA means no amplification bias — and no amplification bias means integer copy number, clean allele ratios, and detectable replication state.

## Key claims

- **Why amplification-free**: DOP-PCR, MDA and MALBAC all "introduce both coverage and polymerase bias into sequences, leading to lower fidelity representations of the genome and analytical scenarios where duplicate sequences cannot be easily resolved." SCI-seq raises throughput but suffers high duplication and low coverage breadth. Microfluidic DLP fixed the bias but was limited by device fabrication and by cell size (large cells clog, small cells pass through traps).
- **Imaging-based QC is the platform's distinguishing feature.** A transparent nozzle plus integrated camera performs object recognition at nozzle and well imaging steps, so doublets, empty wells and contaminated cells are excluded *before* library construction — bypassing Poisson loading limits entirely.
- Success rates from 51,926 libraries, defined as quality score ≥0.75 from an **18-feature classifier trained on 20,000 manually curated libraries**: 65.0% of live cells (25,270/38,705), median 73.3% per sample, range 30.6–96.0%; **36.0% of dead cells still produce high-quality libraries** (3,776/10,577); nuclei 66.0%, with metrics comparable to cells from the same sample and intermixing in copy-number clustering.
- Works across cell sizes 5–80 µm and sample types: cell lines, breast cancer PDX, mouse synovial sarcoma, frozen follicular lymphoma, a diagnostic **fine-needle aspirate**, and nuclei from flash-frozen tissue.
- **Clone-resolution somatic variants from low-coverage cells.** Cluster cells by copy-number profile → treat each clone as a pseudo-bulk → call SNVs, breakpoints and allele-specific copy number per clone. On 1,966 libraries from three clonally related HGS ovarian lines: 9 clones (62–145 cells, median 15× per clone). Haplotype blocks phased with Shape-IT/1000G gave usable allelic measurements for **92–94% of genomic bins**.
- Clone E shows a textbook WGD signature: chr1/7/10/11 at 4 copies with MAF ~0.5; chr2/5/9 segments at 3 copies with MAF 0.33 (single loss post-WGD); chr3/4/6/12 at 5 copies with MAF 0.4 (gain post-WGD); chr17 at MAF 0 = LOH, as expected in nearly all HGS ovarian cancers.
- Phylogenies from SNVs (14,068 passing; 84% fitting the tree — 28% ancestral, 9% clone-specific, 63% clade-specific) and independently from breakpoints (538; 88% fitting) have **identical topology**, with correlated branch counts (Spearman p < 2.1 × 10⁻⁷).
- **Single-cell beats bulk deconvolution.** Against in-silico mixtures, ReMixT, THetA2 and CloneHD all underperform DLP+ clustering on clonal fraction, clone number, and per-clone copy-number architecture — the identifiability problem from the interaction of tumor content, cancer cell fraction, ploidy and genotype simply does not arise.
- **FNA proof of principle**: 62 diploid cells serve as the internal germline reference for 220 aneuploid cells from the same aspirate, yielding allele-specific copy number and LOH for 3 clones — ancestral *MCL1*/*MYC*/*CCNE1* amplifications, clone-specific *RAD18*/*RAB18*, and clonal *BRCA2* LOH coinciding with a germline loss-of-function allele.
- **Whole-chromosome mis-segregation rates measured directly**: 5.2% in 184-hTERT wild-type and *TP53*-null lines, 2.6% in GM18507, but only **0.6% in follicular lymphoma tissue and 1.2% in a mouse sarcoma** — cell lines mis-segregate far more than tissues. Gains exceed losses in wild-type lines; in the isogenic *TP53*-null the direction **reverses**, with losses slightly exceeding gains at the same overall rate. No dependence on chromosome size.
- **Replication state is readable from coverage**: flow-sorted G1/S/G2 cells show S-phase cells have a distinctive GC-content-vs-coverage signature, because early- and late-replicating regions differ in GC and partially replicated genomes shift the distribution.

## Methods / evidence

A resource paper with an unusually complete engineering account: Colossus (per-cell metadata) and Tantalus (sequencing datasets) databases, a cloud workflow engine, an HMM-based copy-number/ploidy caller, and Montage, a linked-chart Elasticsearch visualization frontend, all open-source, with data browsable at cellmine.org. Reaction conditions were optimized systematically (lysis volume and buffer, Tn5 concentration, PCR cycles, solubilization time, viability) using the quality score as the objective.

Flow-sorted cell-cycle fractions provide the ground truth for the replication-state claim rather than inference from the data itself.

## Surprising or load-bearing bits

- **The cell-line vs tissue aneuploidy gap (≈5% vs ≈1%) is the number to carry.** Rates of chromosomal instability measured in cultured lines overstate what happens in tissue by roughly 4–8×. Any somatic-aneuploidy estimate benchmarked on cell lines is measuring culture, not biology — directly relevant to [[mukamel-2025-aneuploidy-brain]] and the brain-aneuploidy literature.
- **The *TP53*-null reversal is subtle and specific**: p53 loss does not change *how often* chromosomes mis-segregate, it changes *which direction survives*. Rate and spectrum are separable phenotypes.
- Dead cells yielding 36% usable libraries matters practically — post-mortem, autopsy and archival material is not automatically lost, which is exactly the constraint on human somatic-mosaicism sampling.
- The **clone-as-pseudo-bulk** strategy is the general answer to low per-cell coverage in amplification-free data: don't try to call SNVs per cell, call them per clone after clustering on copy number. That trade (many cells × low coverage, aggregate by inferred clone) is the structural opposite of PTA's (few cells × high coverage per cell), and [[droplet-vs-single-molecule-scdna]] is where the wiki tracks that axis.
- Replication state as a *free* readout of coverage/GC structure means S-phase cells — normally a confounder in copy-number calling — become a measurable biological variable.
- The FNA result is the clinical headline: a minimally invasive aspirate is enough for clone-resolved allele-specific copy number **with its own internal germline reference**, no matched normal required.

## Concepts touched

- [[dlp-plus]] — this is the founding source for the page.
- [[scwga-chemistries]] — DLP+ is the branch that opts *out* of WGA entirely; it belongs in the chronology as the amplification-free alternative to PTA rather than a successor to it.
- [[replication-timing]] — S-phase identification from GC/coverage.
- [[phylogenetic-inference]] — SNV and breakpoint trees cross-validating each other.

## Connections to other sources

- Direct successor to [[zahn-2017-dlp|Zahn 2017 (DLP)]], addressing its microfluidic scalability and cell-size limits.
- Rejects the WGA chemistries of [[dean-2002-mda]], [[telenius-1992-dop-pcr]], [[zong-2017-malbac-protocol]]; contrast the opposite design philosophy in [[gonzalez-pena-2021-pnas|PTA]].
- Copy-number calling context: [[garvin-2015-natmethods|Ginkgo]], [[bakker-2016-aneufinder|AneuFinder]], [[wang-2020-scope|SCOPE]]; allele-specific copy number in [[zaccaria-2021-chisel|CHISEL]]; LOH framing in [[smukowski-heil-2023-loh]].
- Phylogenetic downstream: [[kaufmann-2022-medicc2]], [[satas-2020-scarlet]], [[lu-2024-cnaphylogeny-review]].
- Tumor-evolution lineage from [[navin-2011-sns-tumor-evolution]]; chemoresistance application in [[kim-2018-tnbc-chemoresistance]].

## Open questions

- Per-cell SNV calling remains out of reach at DLP+ coverage — clone-level aggregation is a workaround, and it cannot see private mutations in single cells. That is the boundary PTA + duplex methods occupy ([[single-cell-duplex-sequencing]]).
- Whether the tissue mis-segregation rates (0.6–1.2%) generalize beyond lymphoma and a mouse sarcoma — two tissue types is thin for a claim this consequential.
- The paper measures replication state but does not use it to correct copy-number calls in S-phase cells; whether S-phase cells should be excluded or modeled is left open.

## Related

- [[dlp-plus]] · [[zahn-2017-dlp|Zahn 2017 (DLP)]] · [[gonzalez-pena-2021-pnas]] · [[cancer-clonal-evolution]]
