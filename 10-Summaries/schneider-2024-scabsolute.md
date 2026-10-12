---
type: summary
title: "Schneider et al. 2024 — scAbsolute: measuring single-cell ploidy and replication status"
source: "[[00-Sources/papers/scAbsolute_ measuring single-cell ploidy and replication status]]"
source_quality: full
source_sha256: "54994e63e11a662f9562c427ead0afe096f1a3f9cd6511ddb4da2d9743b88c9a"
source_kind: paper
author: "Michael P. Schneider, Amy E. Cullen, Justina Pangonyte, Jason Skelton, Harvey Major, Elke Van Oudenhove, Maria J. Garcia, Blas Chaves Urbano, Anna M. Piskorz, James D. Brenton, Geoff Macintyre, Florian Markowetz"
published: 2024-03-04
ingested: 2026-10-12
doi: "10.1186/s13059-024-03204-y"
journal: "Genome Biology"
aliases: ["Schneider 2024", "scAbsolute"]
tags: [scAbsolute, ploidy-estimation, whole-genome-doubling, S-phase-detection, cell-cycle, read-density, Dirichlet-process-GMM, DLP+, ACT, 10x-CNV, FUCCI, shallow-scWGS, Markowetz-lab, Cambridge]
entities: []
concepts: ["[[copy-number-variation]]", "[[whole-genome-doubling]]", "[[replication-timing]]", "[[chromosomal-instability]]", "[[dlp-plus]]", "[[tn5-tagmentation]]", "[[intratumor-heterogeneity]]", "[[doublet-detection]]", "[[sequencing-depth-and-coverage]]", "[[mappability]]"]
topics: ["[[cancer-clonal-evolution]]", "[[computational-methods]]", "[[scdna-cancer-applications]]", "[[whole-genome-amplification]]"]
---

**Citation:** Schneider et al. (2024) — *scAbsolute: measuring single-cell ploidy and replication status* — *Genome Biology*. [DOI](https://doi.org/10.1186/s13059-024-03204-y)

# Schneider 2024 — scAbsolute

> Absolute copy number from a shallow single-cell genome is underdetermined: a diploid and a tetraploid fit of the same profile are equally good, so G1 vs G2 cells and cells just after whole-genome doubling (WGD) cannot be told apart from copy-number profiles alone. **scAbsolute** first fits the ploidy scaling factor ρ (average reads per copy per bin) with a constrained Dirichlet-process Gaussian mixture, then breaks the tie with **read density** — how many unique read pairs physically overlap. In amplification-free, tagmentation-based data (DLP+, ACT) overlapping reads are capped by the number of physical DNA copies, so read density at a given ρ reveals the true ploidy. A separate, unsupervised **cycling-activity** statistic flags S-phase cells from read-count trends against replication time. The tool is explicitly about ploidy and replication status, not about accurate copy-number calling.

> [!abstract] 한눈에
> scAbsolute는 copy-number profile만으로는 구분할 수 없는 G1·G2 세포와 WGD 직후 세포를 read density로 가려 절대 ploidy를 추정하고 복제 상태까지 판별한다. ploidy benchmark에서 잘못된 ploidy 비율이 5%로 CHISEL, HMMCopy, Ginkgo보다 낮았지만, read density를 쓰려면 WGA 없이 얻은 paired-end 데이터가 필요하다.

## Key claims

- **Four-step algorithm.** (1) PELT change-point segmentation with a negative-binomial likelihood on 500 kb bins; (2) a constrained DPGMM on the marginal distribution of segmented counts, with Gaussian means forced onto a 1-D grid (μ_k = k·ξ), fitted by stochastic variational inference in TensorFlow; (3) choose the multiple of ρ with minimum RMSE inside a ploidy window (default 1.1–8.0); (4) flag wrong ploidy fits (G2, WGD, outliers) by deviation of observed from expected read density, and refit with a cell-specific ploidy window.
- **Read density needs three conditions**: no whole-genome amplification, paired-end reads, and enough coverage — at least ρ = 75 at 500 kb, about 0.01–0.02× or roughly a million reads for a diploid human cell. Single-end data would need much higher depth. The authors call this the first use of read density for cell ploidy.
- **Hold-out DLP+ libraries**: G1 and G2 cells separate by read density, with S-phase cells in between. Accuracy was 89% for T-47D (196 G1, 154 G2 cells) and about 66% for normal SA928 (664 G1, 362 G2) at ρ ≥ 75; the authors attribute part of the gap to FACS/DAPI gating errors and to outliers in diploid regression.
- **FUCCI and artificial multiplets** (new mDLP+ data, PEO1-STOP ovarian cancer line, ~triploid): 288 cells per phase (G1, S, G2) plus 288 wells holding 1–5 cells (3N–15N). G1 vs G2/S separated with 97% accuracy at ρ ≈ 200 (50% downsampled); G1 vs 6N–12N multiplets also 97%, both downsampled (ρ ≈ 200) and at full depth (ρ ≈ 400). The multiplets could not be told apart from copy-number profiles alone.
- **Replication detection.** Cycling activity = length-weighted median of per-segment partial Spearman trend statistics of counts vs ENCODE Repli-chip replication time, controlling for GC and mappability (per-cell GAM). Default S-phase cutoff: 1.5 SD above the median, SD taken from the left half of the distribution.
  - Random forest on four features (read depth, overdispersion, cycling activity, mutual information between reads and replication state): **92%** accuracy on Laks et al. data, where the original feature-based classifier reached 90%.
  - Unsupervised (cycling activity + mutual information): 86% overall — 90% on normal SA928, 78% on T-47D.
  - PEO1 FUCCI, balanced G1/S test set (thresholds from 200 G1 cells, tested on 85 G1 + 85 S): 89%, vs 71% for an early release of PERT on the same data.
  - Across 10 cell lines sequenced with 10x, proportion of cycling cells correlated negatively with doubling time (r = −0.75, p = 0.02).
- **Ploidy benchmark (steps 1–3 only)** on ACT breast cancer cell lines and tumours (Minussi et al.), with FACS/DAPI ploidy as reference and a ±0.5 window: mean wrong-ploidy rate **5% scAbsolute, 11% CHISEL, 16% HMMCopy, 27% Ginkgo**. Worst samples: scAbsolute 18% (TN5), 17% (TN4), 11% (MB-453); Ginkgo 69/66/59%; HMMCopy 40/34/31%; CHISEL 47/43/8%. CHISEL had to run in *nonormal* mode (pseudobulk SNPs phased against TOPMed). Step 4 could not be applied because ACT data are single-end.
- **Against original CHISEL** on a ~10,000-cell 10x breast sample, predictions mostly agreed. In discordant cells, CHISEL sometimes chose higher ploidy not supported by copy-number levels; scAbsolute failed where segmentation was wrong and, at about 1%, in very uniform cells.
- **Robustness**: on SCICoNE-simulated profiles it called the right ploidy (±0.5) with about 2% error for tetraploid cells; results were robust to the segmentation algorithm and to bin sizes up to 1 Mb, best at ≤500 kb.

## Methods / evidence

Statistical method with a new bin blacklist built from >7,000 diploid cells across 10x, DLP+ and an in-house protocol (JBL); about 16% of bins (≈9% of autosomal reads) are removed. Validation combines public data from three technologies (10x CNV, DLP+, ACT) with newly generated PEO1 FUCCI and multiplet libraries (mDLP+, PE-50 on NovaSeq 6000, ~6 M reads per cell target; ENA PRJEB61928). Ground truth is experimental: FACS/DAPI, FUCCI markers, karyotypes, or known cell counts per well. Runtime is 3–10 min per cell at 500 kb; on 64 cores, 1,100 ACT cells took about 2 h and 5,000 MKN45 cells about 14 h. The ACT outlier table assumes that cells outside the DAPI window are prediction errors, not true ploidy variation.

## Limitations

**Authors' own:**
- Cannot distinguish G2 cells from WGD cells; this needs extra information such as Geminin staining or the expected fraction of G2 cells in the population.
- Read-density correction (step 4) works only with paired-end reads, sufficient depth and amplification-free protocols; no public data exist to test single-end reads at higher depth.
- Not meant to give highly accurate copy-number calls; segmentation is a stepping stone and wrong segmentation causes ploidy failures.
- The read-density model is strongest at ρ 75–150 and less reliable at higher ρ, where training cells are fewer and high-ploidy cells are often G2/S; it assumes most reference cells are G1 and correctly fitted.
- Diploid normal cells are harder because the per-cell regression is more sensitive to outliers; the DAPI-sorted cell-cycle labels used for validation are themselves noisy.

**Reviewer notes:**
- The headline 5% vs 11–27% benchmark covers only steps 1–3 on one technology (ACT); the WGD-resolving step 4 was validated on cell lines and artificial multiplets, not on patient tumours. (synthesis)
- The read-density reference model was trained on DLP+/mDLP+ cells; how well it transfers to other amplification-free chemistries without retraining is not shown. (synthesis)
- Several authors are founders or shareholders of Tailor Bio Ltd (declared competing interest). (synthesis)

## Surprising or load-bearing bits

- **Physical molecule counting resolves ploidy.** In amplification-free data, overlapping unique reads are bounded by the number of DNA copies, so read density measures DNA content directly. This turns a library-prep property (no WGA) into the key constraint for absolute copy number.
- **Recent WGD is invisible to BAF methods.** CHISEL-style allele-frequency approaches need mutations to accumulate on different alleles, so a WGD with no later copy-number change cannot be seen. The authors call scAbsolute the only tool that can identify such a WGD computationally in DLP/ACT data.
- **FACS/DAPI is a poor gold standard.** DAPI gating let a large share of S-phase cells into "G1/G2" gates unless done very carefully, which also biases cell-cycle classifiers trained on those labels. The authors propose scAbsolute as an alternative to FACS ploidy sorting, noting FACS cutoffs may select more homogeneous populations and understate heterogeneity.
- Proposed use for doublet detection in future droplet-based, amplification-free protocols.

## Concepts touched

- [[copy-number-variation]] — absolute scaling of shallow scWGS counts; ploidy as a prerequisite for CN calling, phylogenies and SNV calling.
- [[whole-genome-doubling]] — detection of recent WGD without later CNAs from read density.
- [[replication-timing]] — per-cell S-phase detection from count trends against replication time.
- [[chromosomal-instability]] — motivating context: CIN makes cancer-cell ploidy variable.
- [[dlp-plus]] / [[tn5-tagmentation]] — amplification-free direct tagmentation makes read density informative.
- [[doublet-detection]] — artificial multiplets used as ploidy ground truth; doublet detection named as an application.
- [[intratumor-heterogeneity]] — argues computational ploidy avoids FACS selection bias.

## Connections to other sources

- Data and comparator: [[laks-2019-dlp-plus]] (DLP+ data; its S-phase classifier, 90%, vs 92% here) and [[zahn-2017-dlp]] (amplification-free DLP chemistry).
- Benchmarked tools: [[zaccaria-2021-chisel]] (CHISEL; BAF-based, misses recent WGD), [[garvin-2015-natmethods]] (Ginkgo). SCOPE ([[wang-2020-scope]]) is criticised for needing normal cells.
- Simulator used for validation: [[kuipers-2025-scicone]] (SCICoNE).
- Ploidy unidentifiability flagged by [[mallory-2020-cna-review]].
- WGD-aware downstream analyses: [[kaufmann-2022-medicc2]], [[mcpherson-2025-ongoing-wgd]].

## Open questions

- Whether single-end reads at higher depth can support read-density ploidy calls (no public data).
- How to separate G2 from WGD cells without staining or population-level G2 frequencies.
- How clonal decomposition before ploidy calling compares with FACS-based subpopulation selection for measuring intratumour heterogeneity (authors call for more work).

## Related

- [[copy-number-variation]] · [[whole-genome-doubling]] · [[replication-timing]] · [[40-Topics/cancer-clonal-evolution]] · [[zaccaria-2021-chisel]]
