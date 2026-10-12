---
type: summary
title: "Kolbeinsdottir et al. 2025 — Absolute copy number aware CNV calling of sub-megabase segments in ultra-low coverage single-cell DNA sequencing data"
source: "[[00-Sources/papers/Absolute copy number aware CNV calling of sub-megabase segments in ultra-low coverage single-cell DNA sequencing data]]"
source_quality: full
source_sha256: "f18c2f375420c99ad6f163103f540ce1ef776cb1ecdf768161cf252b27788957"
source_kind: paper
author: "Solrun Kolbeinsdottir, Vasilios Zachariadis, Christian Sommerauer, Olli Lohi, Merja Heinäniemi, Martin Enge (corresponding)"
published: 2025-09-18
ingested: 2026-10-12
doi: "10.1093/nar/gkaf919"
journal: "Nucleic Acids Research 53(17):gkaf919"
aliases: ["Kolbeinsdottir 2025", "ASCENT", "Absolute Single cell Copy number Evaluation and subcloNe Topology"]
tags: [ASCENT, copy-number-calling, absolute-copy-number, ploidy, fragment-overlap, direct-tagmentation, DNTR-seq, allele-specific-CNV, copy-neutral-LOH, MEDICC2, B-ALL, ultra-low-coverage, Enge-lab, Karolinska]
entities: []
concepts: ["[[copy-number-variation]]", "[[whole-genome-doubling]]", "[[tn5-tagmentation]]", "[[phylogenetic-inference]]", "[[intratumor-heterogeneity]]", "[[sequencing-depth-and-coverage]]", "[[pseudo-bulk]]", "[[mappability]]"]
topics: ["[[cancer-clonal-evolution]]", "[[scdna-cancer-applications]]", "[[hematopoietic-malignancies]]", "[[computational-methods]]"]
---

**Citation:** Kolbeinsdottir et al. (2025) — *Absolute copy number aware CNV calling of sub-megabase segments in ultra-low coverage single-cell DNA sequencing data* — *Nucleic Acids Research* 53(17), gkaf919. [DOI](https://doi.org/10.1093/nar/gkaf919)

# Kolbeinsdottir 2025 — ASCENT

> **ASCENT** (Absolute Single cell Copy number Evaluation and subcloNe Topology) is an end-to-end Snakemake pipeline built for ultra-low coverage (0.01×–0.1×) scWGS made by **direct tagmentation without preamplification**. It makes three changes to the usual workflow. (1) It segments at high resolution (10–40 kb bins), not the field's 200–500 kb, then refines breakpoints on clone pseudobulks. (2) It fixes ploidy errors (doubling or halving) with a statistic based on **fragment overlap**: Tn5 destroys the template, so overlapping fragments can only come from different copies, and the overlap rate rises with copy number in a predictable way. (3) It calls allele-specific copy number and copy-neutral LOH per clone, with no matched normal or bulk reference. On a paediatric B-ALL sample (ALL40) it found a minor clone (3% of tumour cells) and a small copy-neutral LOH that bulk WGS did not show, and it scored above scAbsolute, Alleloscope and CHISEL against bulk WGS.

## Key claims

- **Higher resolution segments better, even at low depth.** On ALL40 cells downsampled to 20,000–400,000 counts, joint segmentation (mpcf) beat hypothesis-free LLR segmentation in all conditions above 30,000 reads. With sensitivity parameters scaled to per-bin depth, every resolution lost no sensitivity down to 100,000 reads per cell, and all but 10 kb held down to 50,000. The best results came at 40 kb (LLR) and 10 kb (mpcf), not at 200–500 kb. The authors conclude that low-resolution joint segmentation brings no benefit.
- **Pseudobulk refinement reaches ~100 kb.** Single-cell mpcf struggles below 500 kb, but re-segmenting clone pseudobulks at 10 kb found a 140 kb segment on Chr22 confirmed by bulk WGS. Of 13 bulk-WGS segments above the 100 kb detection threshold, ASCENT found 11. The two misses were a pericentromeric event with poor coverage and a borderline bulk call in a TCR region. ASCENT also found four segments that bulk WGS did not.
- **Minor clone missed by bulk.** In ALL40, 324 of 384 cells passed QC. Clustering gave four subclones plus diploid cells. The smallest clone had 8 cells (3% of tumour cells) and was defined by a 11q deletion and a 16p gain, plus small chr1 and chr4 deletions seen at pseudobulk level. None of its private breakpoints were found by bulk WGS.
- **Fragment overlap fixes ploidy.** The per-cell scale factor is fitted by maximum likelihood (factors 1.2–4.5 tested) to make segment values close to integers. That fit cannot tell a profile from its double or half. ASCENT subsamples each copy state to 0.5% coverage (mean of 20 samplings), counts bases covered twice, and compares these counts with a closed-form expected overlap per copy number (10% noise). It adjusts ploidy when the doubling or halving log-odds passes 4.6 (P < 1%).
- **Validation on sorted HCT116 cells.** In G1 HCT116, copy states 1, 2 and 3 gave separate standardized-overlap distributions. Standardized overlap did not correlate with read depth, duplicate rate or insert size. With the P < 1% cutoff, cells sorted as S, G2M or multiplets were detected and their ploidy adjusted. In ALL40, six cells were corrected, and all five that had mRNA libraries were in G2M by cell-cycle markers. scAbsolute missed tetraploid cells (89% false-negative rate for G2M cells).
- **Benchmark against bulk WGS (ALL40 major clone).** Median accuracy was 0.999 for ASCENT and 0.996 for scAbsolute (total CN only, run at 1 Mb). Alleloscope reached 0.85 for allele-specific CN and 0.94 for total CN; its authors recommend ≥1 million SNPs, about five times what this sample had. CHISEL scored below 0.01, because its SNP-based segmentation lacks enough heterozygous SNPs at this depth and cell number.
- **Reference-free allele-specific CN and LOH.** Heterozygous SNPs come from pooled single-cell reads. They are phased with Eagle2 against a reference panel and summed in 50 kb blocks per clone, and rule-based major/minor allele assignment produces a "corrected BAF". Fully homozygous segments are flagged as LOH in all cells. ASCENT found a small (sub-5 Mb) copy-neutral LOH on chr12 that separates two clones, confirmed by paired bulk WGS, plus a clonal chr3 LOH. MEDICC2 then builds a haplotype-aware phylogeny.
- **Robustness.** Accuracy stayed high at 10–50% tumour purity. Accuracy was still high with 3-cell clones but dropped clearly from 5 to 3 cells, so 5 cells is the minimum clone size.
- **Works on other protocols.** On an ACT breast cancer sequenced single-end (TN2), clones looked similar to the original publication and 10 kb pseudobulk segmentation added several small subclonal CNVs. TN2 showed large LOH on several chromosomes, as described before. On an FFPE DCIS prepared with ARC-well (P4P), ASCENT reproduced the published CNV patterns (subclonal chr13 deletion, 19q gain) but called 21 clones against 9.
- **Runtime** is about 7 CPU minutes per cell: 1,024 cells at 2.5 million reads per cell took 10 h on 12 cores.

## Methods / evidence

New data: DNTR-seq (direct tagmentation of nuclei plus mRNA from the same cell) on HCT116 cells sorted by Hoechst DNA content, and on a diagnostic bone-marrow sample from one paediatric B-ALL patient (ALL40, 384 cells, ~280,000 read pairs per cell). Bulk tumour–normal WGS of ALL40 (ASCAT) serves as ground truth. The pipeline runs bwa/GRCh38, Picard deduplication and bin filtering (mappability ≥0.8, GC ≥0.2, plus empirically flagged "bad bins"), which leaves 260,289 bins at 10 kb. Segmentation is either per-cell LLR on a Poisson model or joint mpcf from the copynumber package after Freeman–Tukey transform and normal-cell normalization. Clones come from UMAP + hdbscan, then k-means sub-clustering and residual-based refinement on 10 kb pseudobulks. Absolute CN comes from the overlap statistic, allelic CN from cellsnp-lite + Eagle2 per clone, and the tree from MEDICC2. Supporting evidence includes simulations of the overlap statistic across ploidy and noise, downsampling, purity mixes and two public external datasets.

Weight: the segmentation reference profile for downsampling was itself built by ASCENT (refined clones), so the resolution benchmark is partly self-referential, although Chr12/Chr22 results were also checked against bulk WGS. The accuracy benchmark uses one patient and the major clone only.

## Limitations

**Authors' own:**
- Allele-specific data are not used in segmentation, so ASCENT misses copy-neutral LOH below chromosome-arm level when neighbouring segments share the same copy state. CHISEL, which segments on SNPs as well, can find these.
- With short reads, translocations and other structural rearrangements are usually not resolved to base-pair breakpoints. The authors suggest long reads as a future fix.
- ASCENT is built only for direct-tagmentation scWGS and should not be used on random-priming data, because the absolute-CN theory needs the template split into non-overlapping fragments.
- In the FFPE sample, artefactual mutations prevented reliable allele-specific copy numbers (data not shown).
- Detection is limited to about 100 kb by the segment-size cutoff. T2T alignment improved coverage in some regions (e.g. Chr22p) but was too sparse to add results and introduced artefacts.
- Patterned flow-cell (NovaSeq) chemistry raised artefactual overlap at copy state 1, which the authors link to index hopping.
- Choosing the gamma parameter partly relies on visual inspection of clone heatmaps.

**Reviewer notes:**
- All ground-truth comparisons come from a single B-ALL patient, and the reported accuracy covers only the major clone, so the gain over other tools at minor-clone level is shown qualitatively. (synthesis)
- The competing tools were run outside their stated operating range (CHISEL without a matched normal; scAbsolute changed to run on GRCh38 at 1 Mb), so the benchmark measures fitness for this data regime rather than general accuracy. (synthesis)
- The external breast-cancer datasets have no independent ground truth. "More clones (21 vs 9)" is a resolution claim, not a demonstrated accuracy gain. (synthesis)

## Surprising or load-bearing bits

- **Overlap as a ploidy readout.** The fragment-overlap logic is specific to tagmentation: in a haploid region, every observed overlap is an artefact. This gives absolute ploidy without index sorting, BAF or a reference, and it detects perfectly balanced doublings (G2M cells, WGD) that BAF-based methods miss.
- **"Larger bins reduce noise" is contradicted** when segmentation sensitivity is scaled to per-bin depth: 10–40 kb outperformed 200–500 kb.
- **A single 384-well plate** is presented as enough for subclonal structure, LOH and phylogeny without bulk or normal data.
- Standardized overlap is insensitive to depth, duplicates and insert size but sensitive to sequencer chemistry. This is a practical QC flag for NovaSeq-era libraries.

## Concepts touched

- [[copy-number-variation]] — pushes shallow single-cell CN calling to ~100 kb segments and absolute (not relative) copy states.
- [[whole-genome-doubling]] — fragment overlap separates true doublings and G2M cells from diploid profiles, which scale-factor fitting alone cannot do.
- [[tn5-tagmentation]] — the destructive, non-overlapping fragmentation of the template is what makes the overlap ploidy statistic possible.
- [[phylogenetic-inference]] — allele-specific CN feeds MEDICC2 for a haplotype-aware clone tree.
- [[intratumor-heterogeneity]] — an 8-cell (3%) B-ALL subclone with private breakpoints that bulk WGS missed.
- [[pseudo-bulk]] — clone pseudobulks are used for breakpoint refinement and per-clone haplotyping.
- [[sequencing-depth-and-coverage]] — accurate segmentation down to 100,000 reads per cell, and 0.5% coverage subsampling to make overlap depth-independent.
- [[mappability]] — bins below 0.8 mappability are excluded, and coverage is modelled with GC and mappability terms.

## Connections to other sources

- Benchmarked against [[zaccaria-2021-chisel]] (CHISEL), which failed here (median accuracy <0.01) because at ultra-low depth and a few hundred cells it lacks the SNP density for its segmentation; ASCENT's per-clone 50 kb block haplotyping relies on the observation, cited to CHISEL, that reference-backed phasing is usually correct within short segments.
- Uses [[kaufmann-2022-medicc2]] (MEDICC2) as its phylogeny step, described here as the only WGD-aware phylogenetic tool designed for scWGS.
- Cited among direct-tagmentation scWGS protocols: [[zahn-2017-dlp]], [[laks-2019-dlp-plus]] (DLP/DLP+).
- Contrasts with other single-cell CN callers: [[garvin-2015-natmethods]] (Ginkgo), [[bakker-2016-aneufinder]] (HMM), [[wang-2020-scope]]; SCICoNE ([[kuipers-2025-scicone]]) instead denoises through a CNA tree, and also infers WGD, by comparing tetraploid- and diploid-rooted trees.
- Review context: [[mallory-2020-cna-review]].
- B-ALL single-cell CN in a different design: [[pancikova-2025-splongget]] (longitudinal B-ALL, ASCAT.sc at 500 kb).
- WGD biology at scale: [[mcpherson-2025-ongoing-wgd]].
- LOH background: [[smukowski-heil-2023-loh]].

## Open questions

- How the overlap statistic behaves on droplet or other high-throughput tagmentation platforms with different duplicate and index-hopping profiles. (synthesis)
- Whether adding SNP information to segmentation, as CHISEL does, could recover sub-arm copy-neutral LOH at ultra-low depth without needing a matched normal.
- Accuracy at minor-clone level against an orthogonal ground truth.

## Related

- [[copy-number-variation]] · [[whole-genome-doubling]] · [[tn5-tagmentation]] · [[40-Topics/cancer-clonal-evolution]] · [[40-Topics/hematopoietic-malignancies]] · [[zaccaria-2021-chisel]] · [[kaufmann-2022-medicc2]]
