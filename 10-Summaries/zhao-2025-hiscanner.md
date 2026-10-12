---
type: summary
title: "Zhao et al. 2025 — High-resolution detection of copy number alterations in single cells with HiScanner"
source: "[[00-Sources/papers/High-resolution detection of copy number alterations in single cells with HiScanner]]"
source_quality: full
source_sha256: "29ca0ae6319d5c3b93944ef93958bea8cffd783670025d568c4e121a4b79fdbf"
source_kind: paper
author: "Yifan Zhao, Lovelace J. Luquette, Alexander D. Veit, Xiaochen Wang, Ruibin Xi, Vinayak V. Viswanadham, Yuwei Zhang, Diane D. Shao, Christopher A. Walsh, Hong Wei Yang, Mark D. Johnson, Peter J. Park"
published: 2025-07-01
ingested: 2026-10-12
doi: "10.1038/s41467-025-60446-5"
journal: "Nature Communications"
aliases: ["Zhao 2025", "HiScanner", "ViScanner"]
tags: [HiScanner, ViScanner, copy-number-calling, allele-specific-CNA, BAF, cnLOH, allelic-dropout, bin-size, joint-segmentation, BIC-seq2, PTA, neurons, oligodendrocytes, meningioma, SECEDO, Park-lab]
entities: ["[[20-Entities/peter-park]]", "[[20-Entities/christopher-walsh]]", "[[20-Entities/lovelace-luquette]]", "[[20-Entities/diane-d-shao]]"]
concepts: ["[[copy-number-variation]]", "[[allele-dropout]]", "[[pta]]", "[[mda]]", "[[whole-genome-doubling]]", "[[intratumor-heterogeneity]]", "[[sequencing-depth-and-coverage]]", "[[mappability]]"]
topics: ["[[brain-somatic-mosaicism]]", "[[somatic-mosaicism]]", "[[cancer-clonal-evolution]]", "[[scdna-cancer-applications]]", "[[computational-methods]]", "[[whole-genome-amplification]]"]
---

**Citation:** Zhao et al. (2025) — *High-resolution detection of copy number alterations in single cells with HiScanner* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-025-60446-5)

# Zhao 2025 — HiScanner

> Single-cell CNA callers were built for shallow, cancer-scale data and mostly report chromosome-arm events. High-coverage PTA data could resolve much smaller CNAs, but amplification artifacts — above all allelic dropout (ADO), which looks like a copy loss in read depth — get in the way. **HiScanner** (High-resolution Single-Cell Allelic copy Number callER, Park lab) combines read-depth ratio (RDR), B-allele frequency (BAF) and reference-based haplotype phasing. It sets the bin size from the measured size distribution of ADO events, segments all cells of a sample jointly with a multi-sample BIC, and estimates segment BAF with a fast LOH test that avoids CHISEL-style EM. It infers integer allele-specific copy number and ploidy per cell. In simulations it matches the best callers at 3–5 Mb and beats them at 200 kb–1 Mb. Applied to 65 PTA brain cells, it calls 614 mostly sub-3 Mb CNAs and finds that neurons carry mostly private losses while oligodendrocytes carry clonal gains. In a grade II → grade III meningioma pair (179 cells at 0.5×), its CNA clusters agree with an independent SNV-based clustering (ARI 0.83).

> [!abstract] 한눈에
> HiScanner는 RDR, BAF, haplotype phasing을 결합하고 ADO 크기 분포로 bin 크기를 정해 PTA 데이터에서 고해상도 allele-specific CNA를 찾는다. 200 kb–1 Mb 구간에서 기존 caller보다 우수했고, 뇌 세포 65개에서 neuron은 주로 private loss를, oligodendrocyte는 clonal gain을 지녔다.

## Key claims

- **Bin size is set by the data, not the user.** A two-state HMM (ADO / non-ADO, fit by Baum–Welch) on binarised BAF at germline heterozygous SNPs (gHETs) finds dropout events; the 95th percentile of their sizes becomes the smallest permitted bin. Mean dropout size differed by two orders of magnitude between PTA and MDA (~10³ bp vs ~10⁵ bp), so the bin must be fit per protocol. For the brain PTA data this gave 100 kb bins.
- **Joint segmentation across cells.** BICseq2's bottom-up merge of adjacent bins is extended to G cells by summing per-cell log-likelihoods and scaling the penalty by G. This promotes shared breakpoints, keeps bin adjacency (which CHISEL's global clustering ignores), and penalises over-segmentation. Cells are assumed independent, which the authors call an approximation.
- **Cheap BAF estimation.** Reads at phased gHETs are summed per bin (phased BAF). Per segment, LOH is detected by a Kolmogorov–Smirnov test comparing BAF before and after a haplotype-specific "shift" that exploits GC bias, which affects both alleles equally unless one is missing. BAF peaks near 0 or 1 in non-LOH segments are discarded as dropout. Phase-switch errors in reference phasing run at 1–2%. CHISEL defaults to ~5 Mb bins and Alleloscope computes BAF only on pseudobulk segments, partly because their EM steps are expensive.
- **Ploidy and allele-specific copy number** follow CHISEL's likelihood framework: "balanced" bins (0.45 < BAF < 0.55) are clustered by a GMM over RDR, the largest cluster sets the scale factor γ for each candidate WGD count, and RDR+BAF Gaussian mixtures pick each segment's allelic state.
- **Simulation benchmark** (synthetic diploid X built from two male haploid X chromosomes; single-copy losses, single- and two-copy gains, cnLOH; 13 sizes from 200 kb to 5 Mb; 100 events each; 1% phase-switch rate; 30×, 100 kb bins):
  - Single-copy loss ≥1 Mb: HiScanner sensitivity ~0.90 vs Ginkgo 0.85, both at ~0.96 precision; CHISEL 0.80 sensitivity, 0.51 precision.
  - Single-copy gain: HiScanner ~0.65 sensitivity at 500 kb; HiScanner and Ginkgo >0.90 above 2 Mb.
  - Two-copy gain: HiScanner and Ginkgo ~0.85 sensitivity, ~0.90 precision at ≥2.5 Mb. SCOPE and SCYN missed these entirely because SCOPE's normalisation treats the amplification as technical error.
  - cnLOH: only HiScanner and CHISEL can call it; CHISEL was better above ~1 Mb (>0.90 precision and sensitivity), which the authors attribute to its joint RDR+BAF clustering versus HiScanner's RDR-only multi-sample segmentation.
  - All tools struggled below 500 kb.
- **Depth and bin size.** 50 kb bins gained sensitivity below 500 kb but lost precision; 100 kb was the best balance. 10× was only modestly worse than 30×; 0.5× was much worse for single-copy and small events but kept reasonable accuracy above 2 Mb and for two-copy gains.
- **One aneuploid PTA neuron (29×).** HiScanner and Ginkgo agreed on losses on chr2, 5, 6, 8, 11, 12 and 17 (300 kb to whole-chromosome). CHISEL called a tetraploid baseline and 10,322 breakpoints (0.38 per 100 kb), even after tuning. Ginkgo and CHISEL called spurious high-copy focal gains near centromeres; Ginkgo called small losses without BAF support.
- **Brain (65 PTA cells, 11 neurotypical donors aged 0.4–83, 20–30× per cell).** 2/65 cells (3.1%) were aneuploid, closer to Knouse et al.'s 2.2% than to the 33.8% reported with PTA by Kalef-Ezra et al. Beyond these, HiScanner called 614 CNAs, 609 (99.3%) under 3 Mb, median 612 kb (300 kb–24.1 Mb). Estimated FDR is 26.3%. 77% (24/31) of neurons and 53% (17/32) of oligodendrocytes had at least one CNA. There were 72 clonal events (identical start/end bins across cells).
- **Cell-type contrast.** Neurons carried both gains and losses, mostly losses; oligodendrocytes carried almost only gains (odds ratio of losses vs gains in neurons vs oligodendrocytes = 61, Fisher p = 1e−23). Only 5% of neuronal losses were clonal, against 78% of neuronal gains and 81% of oligodendrocyte gains. The authors read this as gains arising during development (replicative mechanisms) and neuronal losses arising post-mitotically (e.g. NHEJ/MMEJ after activity-induced double-strand breaks). cnLOH ≥2 Mb occurred in 8 neurons (one neuron had 12 events) and in no oligodendrocyte.
- **Age.** A linear mixed model found only a weak negative age slope for non-clonal gains in oligodendrocytes (−0.020 CNA/year, p = 0.010). Neuronal gains and losses in either cell type showed no age trend. This contrasts with the earlier meta-analysis reporting a linear decline of CNA neurons with age (R² = 0.92).
- **Ginkgo disagrees on the same brain cells.** Ginkgo called nearly 10-fold more private neuronal losses and many oligodendrocyte losses. Of its calls, 97% (581/599) in oligodendrocytes and 66% (1410/2121) in neurons were discordant with local BAF. The authors recommend size or BAF-based filtering of Ginkgo calls on PTA data.
- **Meningioma (one patient, grade II initial 88 cells + grade III recurrence 91 cells, PTA, 0.5×, 500 kb bins).** Hierarchical clustering gave four clusters: CNA-free cells (mixed grades); a grade II clone with 1p and 22q losses; a mostly grade III clone that inherits those and adds 6q, 9p and 11q losses; and a small tetraploid grade III group with copy states 2–6. One grade II cell sits in the grade III clone, which suggests the extra CNAs arose during natural tumour evolution rather than from adjuvant therapy. SECEDO clustering on bulk-Mutect2-restricted sSNVs agreed with the CNA clusters (ARI 0.83) but did not separate diploid from tetraploid grade III cells.
- **ViScanner**, a React/HiGlass browser, zooms HiScanner output continuously and keeps data in the local browser.

## Methods / evidence

Algorithm built on BICseq2 normalisation (nucleotide-level GC model, uniquely mappable positions, MAPQ ≥30) and BICseq2 segmentation. gHETs come from GATK HaplotypeCaller on matched bulk, phased with SHAPEIT2 against 1000 Genomes Phase 3. Comparators are Ginkgo, SCOPE, SCYN and CHISEL. Alleloscope was excluded because it detects only clonal events. The benchmark targets **non-clonal** (single-cell-private) CNAs. Simulation uses the synthetic diploid X approach from [[luquette-2019-natcomm]] so that haplotype structure and real amplification noise are preserved; the authors argue read-count simulations (e.g. Lorenz-curve sampling, as in [[mallory-2020-cna-review]]) cannot test allele-specific callers. For a fair segmentation comparison, CHISEL's segmentation was fed HiScanner-preprocessed RDR and BAF. On the real neuron, CHISEL was tuned (sensitivity 10, maxploidy 3, k 10) after it predicted high ploidy. The brain data are reanalysed published PTA cells (Luquette 2022; Ganz 2024); bulk-overlapping CNAs and sex chromosomes were removed, and the two aneuploid neurons were excluded from size/prevalence analyses. The meningioma cells are new (Bioskryb ResolveDNA, NextSeq, ~8 M read pairs per cell).

## Limitations

**Authors' own:**
- The joint-segmentation model assumes cells are independent. This is violated in clonal populations such as tumours, but it is kept for computational cost; conditional random fields or deep models are named as future work.
- The small sample (65 cells from 11 brains) gave insufficient power to test CNA burden against age.
- "Clonal" means identical start/end bins across cells. Some such events could be independent recurrent mutations rather than true clonal expansions.
- cnLOH analysis was restricted to >2 Mb, where simulations showed ~0.9 precision and sensitivity; CHISEL outperforms HiScanner on large cnLOH.
- All tools, HiScanner included, struggle with CNAs below 500 kb. The estimated FDR on the brain calls is 26.3%.
- The tetraploid meningioma cluster needs orthogonal validation (e.g. FISH). Radiotherapy may still have shaped the grade III clone's expansion by selection.
- The ADO-size HMM assumes CNAs are rare relative to dropout in the training cells (oligodendrocytes with minimal aneuploidy were used).

**Reviewer notes:**
- The simulation inserts events on chromosome X only, from three oligodendrocytes of two donors. Performance on autosomes with different mappability and GC landscapes is assumed rather than shown. (synthesis)
- The neuronal-loss versus oligodendrocyte-gain contrast rests on ~31 neurons and 32 oligodendrocytes with a 26% estimated FDR. The real-data comparison with other callers relies on BAF concordance, which is HiScanner's own modelling signal, rather than an orthogonal truth set. (synthesis)
- Some counts in the text do not reconcile: "614 smaller, mostly private CNAs (314 private losses and 57 private gains)" sums to 371, not 614, and the Discussion says HiScanner outperformed the others on cnLOH although the Results show CHISEL ahead for large cnLOH. (synthesis)

## Surprising or load-bearing bits

- **ADO size distribution as the resolution limit.** The minimum usable bin is a property of the amplification chemistry and can be measured from BAF, which is why PTA permits much smaller bins than MDA.
- **Sub-3 Mb CNAs are common in normal brain cells.** About 3 Mb was the lower bound of earlier single-cell CNA surveys; 99.3% of HiScanner's 614 brain CNAs fall below it.
- **Neurons lose, oligodendrocytes gain.** Neuronal losses are almost all private (post-mitotic), while gains in both cell types are largely clonal (developmental or progenitor-derived). This gives a mechanism-level hypothesis about the timing of somatic CNAs in the brain.
- **Choice of caller changes the biology.** Ginkgo on the same cells yields a fundamentally different neuron/oligodendrocyte CNA picture, with most of its small calls contradicted by BAF.
- **CHISEL is a poor fit outside its design target.** CHISEL tuned for megabase clonal cancer CNAs over-segments and inflates ploidy on a single high-coverage cell. The authors regard this as expected, not a bug.
- **Orthogonal SNV and CNA clusterings agree on low-pass PTA data (ARI 0.83)**, and the SNV-versus-CNA discordances are informative about event order: WGD before most sSNVs, some sSNVs before CNAs.

## Entities mentioned

- [[20-Entities/peter-park]] — senior author; HiScanner builds on his lab's BIC-seq2 bulk caller.
- [[20-Entities/christopher-walsh]] — co-author; brain PTA data come from Walsh/Park collaborations.
- [[20-Entities/lovelace-luquette]] — co-author; his SDX simulation design and neuron PTA data are reused.
- [[20-Entities/diane-d-shao]] — co-author.

## Concepts touched

- [[copy-number-variation]] — pushes single-cell CNA resolution to the 200 kb–1 Mb range and adds allele-specific states and cnLOH in non-cancer cells.
- [[allele-dropout]] — ADO is modelled explicitly and turned into the bin-size criterion rather than treated only as noise.
- [[pta]] / [[mda]] — PTA dropout events are ~100-fold shorter than MDA's, which is what enables small bins.
- [[whole-genome-doubling]] — ploidy inference allows multiple WGDs; a tetraploid meningioma subclone is reported.
- [[intratumor-heterogeneity]] — four CNA clusters across a primary/recurrence meningioma pair.
- [[sequencing-depth-and-coverage]] — 10× is close to 30× for most CNA types; 0.5× suffices only for large events.
- [[mappability]] — uniquely mappable positions and nucleotide-level normalisation are credited for stable calls near centromeres.

## Connections to other sources

- Benchmarked callers with wiki summaries: [[garvin-2015-natmethods]] (Ginkgo: high RDR sensitivity, many BAF-discordant small calls on PTA data), [[wang-2020-scope]] (SCOPE: conservative, over-corrects amplifications in few-cell data), [[zaccaria-2021-chisel]] (CHISEL: shares the ploidy likelihood; better on large cnLOH; over-segments a single high-coverage cell).
- Same lab and data lineage: [[luquette-2019-natcomm]] (SDX simulation), [[luquette-2022-neuron-scan2-indels]] (source of the PTA neuron genomes), [[luquette-2025-pta-duplex-mosaicism]].
- PTA chemistry: [[gonzalez-pena-2021-pnas]]. Low-breadth CNA assays it contrasts with: [[zahn-2017-dlp]], [[laks-2019-dlp-plus]].
- Benchmarking practice it argues against for allele-specific callers: [[mallory-2020-cna-review]].
- Contrast with shallow-data joint calling: [[kuipers-2025-scicone]] denoises via a shared CNA tree at ≤0.1×, while HiScanner denoises via joint breakpoints and BAF at high depth. (synthesis)
- Brain context: [[bizzotto-2022-brain-mosaicism-review]], [[mcconnell-2017-science]].

## Open questions

- Would modelling dependency between cells (shared clonal structure) close the gap with CHISEL on large cnLOH and improve sensitivity below 500 kb?
- How the neuron-loss / oligodendrocyte-gain pattern holds with many more cells and with an orthogonal validation of sub-Mb calls.
- The three discordant estimates of brain CNA prevalence (meta-analysis decline with age; Knouse 2.2%; Kalef-Ezra 33.8%) are only partly reconciled here, with 3.1% large-scale aneuploidy but many small CNAs.

## Related

- [[copy-number-variation]] · [[allele-dropout]] · [[40-Topics/brain-somatic-mosaicism]] · [[40-Topics/cancer-clonal-evolution]] · [[zaccaria-2021-chisel]] · [[garvin-2015-natmethods]]
