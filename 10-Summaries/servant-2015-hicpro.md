---
type: summary
title: "Servant et al. 2015 — HiC-Pro: an optimized and flexible pipeline for Hi-C data processing"
source: "[[00-Sources/papers/HiC-Pro_ an optimized and flexible pipeline for Hi-C data processing]]"
source_kind: paper
author: "Nicolas Servant, Nelle Varoquaux, Bryan R. Lajoie, Eric Viara, Chong-Jian Chen, Jean-Philippe Vert, Edith Heard, Job Dekker, Emmanuel Barillot"
published: 2015-12-01
ingested: 2026-08-10
doi: "10.1186/s13059-015-0831-x"
journal: "Genome Biology"
tags: [HiC-Pro, pipeline, ICE, iterative-correction, allele-specific, parallelization, valid-pairs]
entities: ["[[job-dekker]]"]
concepts: ["[[hi-c-normalization]]", "[[single-cell-hi-c]]", "[[chromatin-compartments]]", "allele-specific analysis", "X inactivation", "[[read-alignment]]"]
topics: ["[[3d-genome]]", "[[computational-methods]]"]
---

**Citation:** Servant et al. (2015) — *HiC-Pro: an optimized and flexible pipeline for Hi-C data processing* — *Genome Biology* 16, 259. [DOI](https://doi.org/10.1186/s13059-015-0831-x)

# Servant 2015 — HiC-Pro

> Raw Hi-C reads to normalized contact maps in four modules — align, filter valid interactions, bin, normalize — with parallelization by read chunk and a fast sparse implementation of **iterative correction (ICE)**. Its distinguishing capability at publication was **allele-specific contact maps** from phased genotypes.

## Key claims

- **Four-module architecture**: (i) read alignment, (ii) detection and filtering of valid ligation products, (iii) binning, (iv) contact map normalization — the steps on which the field had already converged but for which no stable, flexible, parallel implementation existed.
- **Two-step mapping instead of iterative mapping.** hiclib aligned 35 bp reads in four progressive steps; HiC-Pro's two-step strategy (full read, then chimeric rescue of the unmapped) is the main source of its speed advantage.
- Performance: the Dixon IMR90 dataset (**397.2 million read pairs**, 84 chunks) completed in **2 hours on 168 CPUs**; valid interactions extracted in under 30 minutes. On 8 CPUs without chunking, HiC-Pro took **under 15 hours versus 28 hours for hiclib**.
- Scale test: the Rao IMR90 dataset — **1.5 billion read pairs**, 160 chunks, 320 CPUs — produced 5 kb maps in **12 hours**, with the expected chromatin loops visible.
- **Concordance with hiclib** despite different filtering: mean Spearman correlation of normalized intra-chromosomal maps **0.83 (0.65–0.95)**; inter-chromosomal coverage vectors 0.75 (0.46–0.98). HiC-Pro's defaults are **less stringent**, retaining more valid interactions.
- **ICE implementation.** Released standalone as `iced` as well as inside the pipeline. A compressed-sparse-row implementation normalizes a 20 kb human genome map in **under 30 minutes with 5 GB RAM**, and genome-wide 5 kb in under 2.5 hours with 24 GB. Sparse beats parallel-dense (HiCorrector) below 40 kb bins; dense wins at 500 kb–1 Mb by a negligible margin.
- **Allele-specific maps.** With 2,239,492 phased heterozygous SNPs from the Illumina Platinum Genomes Project, the hg19 reference is N-masked at SNP positions and re-indexed for bowtie2. Of 826 million GM12878 read pairs, **61% were valid interactions and ~6% of those could be assigned to a parental allele**. The resulting inactive X map shows the expected **two mega-domains** with the boundary near the **DXZ4** microsatellite; the active X does not.
- Works with restriction-enzyme Hi-C and with nuclease-based protocols (DNase Hi-C, Micro-C).

## Methods / evidence

Two public datasets spanning an order of magnitude in size; head-to-head runtime and result concordance against hiclib, the then-standard; normalization benchmarked separately against HiCorrector at matched iteration counts across five resolutions; and a biological positive control (the inactive-X mega-domain structure) for the allele-specific mode.

## Surprising or load-bearing bits

- **Only ~6% of valid interactions are allele-assignable**, even with 2.2 million phased SNPs. Allele-specific 3D genome analysis costs roughly a 16-fold loss in effective depth — which is why it stays confined to well-phased cell lines and to megabase-scale features like the X mega-domains rather than loops.
- **Filtering stringency is a free parameter, not a fact.** HiC-Pro and hiclib produce maps correlating at 0.83, not 1.0, from identical raw data, purely from differing valid-pair definitions. Any cross-study comparison of Hi-C features inherits that pipeline-dependent variance — a quiet confound behind disagreements over TAD calls ([[kerpedjiev-2018-higlass|HiGlass]] visualizes exactly this, showing seven TAD callers disagreeing on the same matrix).
- **Chimeric rescue is not optional.** A proximity-ligation read *is* chimeric by construction, so aligners that discard chimeras ([[li-2009-bwa|BWA aln]] behaviour) silently drop informative pairs — the specific deficiency HiC-Pro names in HiCdat, HiC-inspector and HiCbox.
- The **sparse-versus-dense crossover at ~40 kb** is a concrete statement of when Hi-C data stops being a matrix and starts being a list — the same observation [[abdennur-2020-cooler|Cooler]] built a file format around, and it is why single-cell Hi-C, which is sparser still, needs sparse-native tooling throughout.
- HiC-Pro's restriction-fragment definitions are used well outside its own pipeline — [[ramani-2017-scihi-c|sciHi-C]] uses them for DpnII site enumeration.

## Entities mentioned

- [[job-dekker]] — co-author; 3C/Hi-C originated in this lab ([[lieberman-aiden-2009-hic]]).

## Concepts touched

- [[hi-c-normalization]] — ICE as the standard matrix-balancing procedure, and its sparse implementation.
- allele-specific analysis — N-masking plus phased SNPs as the standard allele-assignment approach.

## Connections to other sources

- Assay: [[lieberman-aiden-2009-hic]]; features it is used to call: [[dixon-2012-tads]].
- Contemporary/alternative pipelines: [[durand-2016-juicer]] (Juicer), [[heinz-2010-homer]] (HOMER).
- Storage successor for its outputs: [[abdennur-2020-cooler]]; visualization: [[kerpedjiev-2018-higlass]].
- Single-cell consumers: [[ramani-2017-scihi-c]], [[zhou-2019-schicluster]], [[zhang-2022-higashi]].

## Open questions

- The paper reports concordance with hiclib but never establishes which filtering stringency is *correct* — there is no ground truth for a valid interaction, only conventions.
- ICE assumes equal visibility for all bins after correction, an assumption unexamined here and known to be strained in aneuploid genomes — directly relevant to cancer Hi-C ([[cancer-clonal-evolution]]).

## Related

- [[hi-c-normalization]] · [[durand-2016-juicer]] · [[abdennur-2020-cooler]] · [[3d-genome]]
