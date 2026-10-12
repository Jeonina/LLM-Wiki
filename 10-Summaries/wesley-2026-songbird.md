---
type: summary
title: "Wesley et al. 2026 — Wavelet-based whole genome doubling aware single-cell copy number calling"
source: "[[00-Sources/papers/Wavelet-based whole genome doubling aware single-cell copy number calling]]"
source_quality: full
source_sha256: "fff3d0e1550f6ec8868047e4557f064783a8b2e0f372907a3d94b56339d77009"
source_kind: paper
author: "Benjamin K. Wesley, Frank Wos, Soren Germer, Jade E. B. Carter, Silas Maniatis, Khanh Dinh, James S. Roche, Timothy R. Chu, Nicolas Robine, Rebecca C. Fitzgerald, Lizhe Zhuang, Simon Tavaré, Karol Nowicki-Osuch"
published: 2026-10-09
ingested: 2026-10-12
doi: "10.1093/nar/gkag960"
journal: "Nucleic Acids Research 54(18):gkag960"
aliases: ["Wesley 2026", "Songbird", "Songbird copy number caller"]
tags: [Songbird, copy-number-calling, whole-genome-doubling, ploidy-estimation, unbalanced-Haar-wavelet, segmentation, DLP+, Tn5, scWGS, artifactual-fragments, ecDNA, BFB, esophageal-adenocarcinoma, ploidy-ladder, New-York-Genome-Center]
entities: []
concepts: ["[[copy-number-variation]]", "[[whole-genome-doubling]]", "[[dlp-plus]]", "[[tn5-tagmentation]]", "[[duplicate-marking]]", "[[structural-variants]]", "[[chromosomal-instability]]", "[[intratumor-heterogeneity]]", "[[sequencing-depth-and-coverage]]", "[[mappability]]"]
topics: ["[[cancer-clonal-evolution]]", "[[computational-methods]]", "[[scdna-cancer-applications]]"]
---

**Citation:** Wesley et al. (2026) — *Wavelet-based whole genome doubling aware single-cell copy number calling* — *Nucleic Acids Research* 54(18), gkag960. [DOI](https://doi.org/10.1093/nar/gkag960)

# Wesley 2026 — Songbird

> Read-depth-ratio copy-number callers cannot see whole-genome doubling (WGD), because a doubled cell has the same depth ratios between regions as its undoubled parent. **Songbird** (an R package) gets absolute ploidy from fragment geometry instead. In amplification-free Tn5 libraries such as [[dlp-plus|DLP+]], every unique fragment comes from one copy of the genome. A fragment that starts within the minimum fragment length upstream of a reference fragment must come from one of the other *n* − 1 copies, while a fragment starting more than the maximum fragment length upstream can come from any of the *n* copies. The ratio of these two local densities is about (*n* − 1)/*n*, and the per-cell recovery probability cancels out. Songbird combines this ploidy estimate with unbalanced-Haar-wavelet segmentation, breakpoint-based subclone clustering, a per-subclone WGD test, and a likelihood-ratio integer fit. On an hTERT/HEK293T ploidy ladder (expected ploidy 2–10), it is one of only two tools (with ASCENT) that called the 2× hTERT wells correctly, and its median ploidy is accurate up to 6.

> [!abstract] 한눈에
> Songbird는 amplification-free Tn5 라이브러리에서 겹치는 fragment와 upstream fragment의 밀도 비로 절대 ploidy를 추정해, read-depth 비율만 보는 caller가 놓치는 whole-genome doubling을 잡아낸다. hTERT/HEK293T ploidy ladder에서 2× hTERT를 올바르게 부른 도구는 ASCENT와 Songbird뿐이었다.

## Key claims

- **Artifactual fragments in Tn5 libraries.** In 100 diploid hTERT cells there were far more 0→2 overlap transitions than random placement predicts. The pairs that cause them share a start or an end but differ in length, so standard deduplication (same start, end and orientation) keeps them. Same-orientation pairs outnumber opposite-orientation pairs nearly 10:1. They are amplified 1:1 or 1:2, which points to an origin before or within the first PCR cycle. They make up less than 1% of fragments but a large share of overlapping ones. Songbird discards the shorter member of each pair.
- **Proposed mechanism.** The authors suspect incomplete Tn5 adapter insertion: one member of the Tn5 dimer is inactive, or neutralisation interrupts tagmentation. They did no biochemical test. ASCENT also found these fragments and removes them in a comparable way.
- **Segmentation (simulation).** In 4,000 CINner-simulated cells with rising missegregation rates, Songbird's filtered unbalanced Haar beat HMMCopy, HaarSeg, CoNVEX and plain unbalanced Haar on breakpoint Jaccard index, and was comparable to circular binary segmentation. It did slightly better than CBS in samples with high copy-number diversity. On Wasserstein distance, all tools except HMMCopy recovered the profile well.
- **Segmentation (real data).** On 100 HEK293T cells scored against ASCAT, Songbird recovered the same number of true breakpoints as every other tool, or more, down to 0.01× per cell (about 100,000 properly paired fragments at 2 × 150 nt). Below 0.005×, HMMCopy and CoNVEX scored better, but both oversegment. Subsamples at 0.01× still correlated above 0.9 (Pearson) with the full-depth segmentation, and Wasserstein error was about 0.2 copies for all tools except HMMCopy.
- **Ploidy ladder.** Wells held 1–4 hTERT cells, one HEK293T cell, or mixtures, 100 wells per condition. Read-depth-only tools (HMMCopy, SCOPE) called the 2× and 3× hTERT wells as copy number 2. Alleloscope and scAbsolute also tended to call diploid. Only Songbird and ASCENT called the 2× hTERT conditions correctly. Songbird underestimated the copy number 7, 8 and 10 conditions.
- **Robustness of the ploidy estimate.** Results did not depend on genome version (hg19, hg38, hs.1). Estimates stayed consistent with bins down to 50 kb, and down to 0.01× in high-CNA cells with average ploidy about 5. Across ploidies, the correct ploidy was recovered at 0.0025× to 0.01× coverage. The estimator also matched published ploidy ladders: the DLP+ cell-cycle ladder from Laks 2019 and the scAbsolute PEO1 ladder.
- **Other Tn5 protocols.** The ploidy estimator transfers directly to DnTR-Seq and "shows promise" on [[chen-2017-lianti|LIANTI]] and SmoothSeq (PacBio long reads). These protocols needed looser deduplication windows: 10 nt for LIANTI, 100 nt for SmoothSeq, plus an 8-kb maximum fragment length for SmoothSeq. Even so, one third of SmoothSeq cells were still incompletely deduplicated and gave ploidy estimates below zero.
- **Final copy number.** RMSE against ASCAT across the ladder was better than existing tools. ASCENT was more consistent (smaller interquartile range) in the 1× and 2× hTERT wells. HMMCopy did well in the diverse 1× HEK and 1× hTERT + 1× HEK wells.
- **Esophageal adenocarcinoma organoid (CAM277).** This subclonal, aneuploid organoid has no per-bin ground truth. Reads that Songbird assigned to each copy number were closer to normally distributed (1 − Shapiro–Wilk) than those from SCOPE, scAbsolute, HMMCopy or ASCENT.
- **ecDNA versus BFB.** At 50-kb bins in CAM277, Songbird approximated the breakpoints of an ecDNA that had been mapped by nanopore long reads. The ecDNA bins varied in copy number between cells but kept constant ratios to each other within each cell, as expected for an element inherited intact. A breakage–fusion–bridge (BFB) further along the chromosome had high, variable copy number and inconsistent ratios between bins, as expected for a lesion that changes composition with each cycle. Segmentation stayed faithful down to 30-kb bins relative to 500 kb.

## Methods / evidence

Four modules:

1. **Segmentation.** QDNAseq bins reads (default 500 kb) and applies GC and mappability correction. The unbalanced Haar transform runs over the whole genome as one series, with a threshold set to the median absolute deviation. Unbalanced Haar can place a split anywhere in a span, not only at the midpoint. Single-bin "singlet" segments below the 90th-percentile depth are merged into the previous segment. Singlets above it keep their own depth, because they may be ecDNA or BFB.
2. **Ploidy estimation.** Filtering removes the shorter fragment of each shared-coordinate pair, fragments shorter than *L*min or longer than the 99th-percentile length, bins under 90% mappability or under 90% assembled, ENCODE exclusion-list bins, and the first 10 nt of each fragment (to correct for the duplication Tn5 creates between adjacent fragments). This removes about 45% of the genome. Overlap and upstream counts are summed per bin, the middle 98% are kept, and the ratio is averaged across bins. Ploidy is then *n* ≈ 1/(1 − overlap density/upstream density).
3. **Subclones and WGD.** Breakpoints present in 10–90% of cells are smoothed with a box kernel and clustered with PhenoGraph. Within each subclone, *k* = 2 k-means is run on the ploidy of cells with more than 50,000 reads. If between-cluster variance / total variance is ≤0.7 and the centroids are close to 1:2, the higher cluster is flagged as WGD. Ploidy is then averaged separately for WGD and non-WGD cells.
4. **Integer fitting.** The reads-per-copy-number (RpCN) scale is the modal depth (Sheather–Jones KDE) divided by a candidate ploidy, with candidates from 0.75 to 1.5 times the estimate. Each candidate is scored by the log-likelihood ratio of a Gaussian read model against a Uniform(10th–90th percentile) null. A plain likelihood would always favour higher ploidy, which is why the null is needed. A Gaussian penalty applies for deviation from the estimated ploidy, and bins above the 90th-percentile segment are excluded from scoring.

Ground truth came from ASCAT on 100-cell pseudobulks of the 1× hTERT and 1× HEK293T wells. Multiplet truths are sums of these two. In LOH regions, SNPs were randomly designated heterozygous with BAF 1. For CAM277 (about 40% LOH) the truth is "less confident" by the authors' own description. Data were DLP+ on NovaSeq 6000, 2 × 150 bp. The ladder is BioProject PRJNA1493277. Code is at GitHub GastroEsoLab/Songbird and on Zenodo.

## Limitations

**Authors' own:**
- Validation covers only a few cell lines and one organoid line. Patient data may be more variable in quality and may need further refinement of the tool.
- Initial per-cell ploidy estimates are noisy and correlate slightly with coverage, partly because S/G2-phase cells have more DNA. In a few high-coverage cells, mean ploidy is overestimated.
- Ploidy is underestimated above about 6 (the copy number 7, 8 and 10 wells).
- Cells are treated as nearly independent. Cells share information only through clustering for ploidy correction. At coarse bins, a focal amplification is estimated from a single bin.
- The overlap-counting estimator could be replaced by a Poisson or binomial sampling model.
- The artifactual-fragment mechanism has not been tested biochemically.
- The CAM277 ground truth is uncertain because of extensive LOH. Karyotyping is only qualitative support.

**Reviewer notes:**
- The whole method depends on near-complete deduplication of unique Tn5 fragments. Outside DLP+, the deduplication window has to be tuned per protocol, and one third of SmoothSeq cells still failed. "Extensible to other Tn5 methods" is therefore demonstrated for ploidy only, not for the full pipeline. (synthesis)
- Ladder multiplet truths are sums of two singlet ASCAT profiles, and the WGD module is never tested against cells with a known doubling inside a tumour subclone. WGD-calling accuracy as such is not directly measured. (synthesis)
- ASCENT ran with gamma parameters chosen per condition against ground truth, while other tools used defaults or documented settings. The comparison is uneven, though in ways that favour the competitor. (synthesis)

## Surprising or load-bearing bits

- **The ploidy signal is purely geometric.** It needs no SNPs and no copy-number variation, so it works even on a perfectly doubled diploid genome, where allele ratios stay 1:1. The authors say this case defeats CHISEL and Alleloscope.
- **"Every retained read is a unique template" is not quite true for Tn5 libraries.** Same-start, different-length fragment pairs survive coordinate deduplication and inflate overlap counts. Two independent groups (Songbird, ASCENT) now filter them, and the authors recommend that future scWGS callers do the same.
- **DLP+ maximum coverage is half the cell's ploidy**, because adapter pairing on fragments is random.
- **The authors' takeaway:** the two tools that recovered multiplied diploid genomes (Songbird, ASCENT) both count fragment overlaps, so future ploidy estimators should model overlap patterns.

## Entities mentioned

- No wiki entity pages exist for the authors (Tavaré, Nowicki-Osuch, Fitzgerald) or for the New York Genome Center.

## Concepts touched

- [[copy-number-variation]] — absolute, WGD-sensitive integer copy number from shallow amplification-free scWGS.
- [[whole-genome-doubling]] — per-subclone WGD detection from fragment-geometry ploidy, without allelic information.
- [[dlp-plus]] — artifactual same-start fragments, the half-ploidy coverage ceiling, and a new ploidy ladder.
- [[tn5-tagmentation]] — incomplete Tn5 insertion proposed as the source of artifactual fragment pairs.
- [[duplicate-marking]] — coordinate deduplication is insufficient for Tn5 scWGS.
- [[structural-variants]] — ecDNA and BFB distinguished by between-bin copy ratio across cells.
- [[chromosomal-instability]] — CINner simulations with varying missegregation rates.

## Connections to other sources

- Extends [[laks-2019-dlp-plus]] (platform; its cell-cycle ladder is reused) and [[zahn-2017-dlp]] (unique-template argument, which this paper qualifies).
- WGD context: [[mcpherson-2025-ongoing-wgd]] calls WGD from allele-specific copy number and filters out perfectly doubled cells. Songbird targets exactly that blind spot.
- Benchmarked or discussed callers with wiki summaries: [[wang-2020-scope]] (SCOPE), [[zaccaria-2021-chisel]] (CHISEL, needs phasing depth). Other benchmarked tools (HMMCopy, scAbsolute, ASCENT, Alleloscope) have no wiki summary.
- Other per-cell and tree-based callers: [[garvin-2015-natmethods]] (Ginkgo), [[kuipers-2025-scicone]] (SCICoNE, which detects WGD by comparing tetraploid and diploid roots), [[mallory-2020-cna-review]].
- Tn5 protocols tested: [[chen-2017-lianti]].
- Esophageal adenocarcinoma context: [[frankell-2019-eac-landscape]].

## Open questions

- Does the per-subclone 1:2 k-means test detect WGD in real tumours with mixed WGD multiplicities, such as those reported in [[mcpherson-2025-ongoing-wgd]]? (synthesis)
- Would a sampling-model estimator extend accurate ploidy above 6?
- What is the biochemical origin of the artifactual fragment pairs?

## Related

- [[copy-number-variation]] · [[whole-genome-doubling]] · [[dlp-plus]] · [[40-Topics/cancer-clonal-evolution]] · [[40-Topics/computational-methods]]
