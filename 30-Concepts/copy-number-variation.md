---
type: concept
title: Copy Number Variation
aliases: [CNV, CNA, copy number alteration, copy number profiling, copy number]
tags: [CNV, aneuploidy, cancer, single-cell, segmentation]
created: 2026-08-10
updated: 2026-10-12
---

# Copy Number Variation

> Gains and losses of genomic segments, from focal events to whole chromosomes. The most tractable single-cell genomic readout, because it needs breadth rather than depth — and therefore the first thing shallow single-cell WGS could measure well ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]; [[10-Summaries/wang-2021-medalt|MEDALT]]).

> [!abstract] 한눈에
> CNV는 유전체 구간의 copy 수가 늘거나 줄어든 변화이고, 읽기 깊이보다 유전체 전체를 고르게 덮는 것이 중요해서 얕은 single-cell WGS로도 잘 잡힌다 ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]). 최근 caller는 sub-Mb 해상도, 절대 ploidy 추정, 진화 모델과의 결합으로 나아가고 있지만, 한 세포의 profile이 diploid인지 tetraploid인지 가리는 문제는 여전히 핵심 쟁점이다 ([[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]; [[10-Summaries/schneider-2024-scabsolute|scAbsolute]]; [[10-Summaries/ivanovic-2025-cnrein|CNRein]]).

## Definition

Copy number variation covers gains and losses of genomic segments, from focal events to whole chromosomes ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]). In single cells it is usually called from read counts in genomic bins that are GC-corrected and then segmented into integer copy states ([[10-Summaries/bakker-2016-aneufinder|AneuFinder]]; [[10-Summaries/garvin-2015-natmethods|Ginkgo]]). Recurrent aneuploidy is evidence about **selection**, not about stability ([[10-Summaries/bakker-2016-aneufinder|AneuFinder]]) — see [[chromosomal-instability]].

## Why it matters

Single cells change how a copy-number profile is read, because bulk and single-cell views of the same sample disagree by construction:

- Pooling 25 T-ALL cells reproduces the aCGH karyotype exactly, while 56% of the individual cells carry a unique karyotype ([[10-Summaries/bakker-2016-aneufinder|AneuFinder]]).
- Minor clones present at 6–10% "are not evident in the combined profile" ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- Targeted scDNA-seq finds subclonal CNAs that are invisible in bulk ([[10-Summaries/sollier-2023-compass|COMPASS]]).

## Calling approaches

### From single-cell genome reads

| Approach | Example tools | Input | What it adds | Source |
|---|---|---|---|---|
| HMM over binned read counts | [[10-Summaries/bakker-2016-aneufinder\|AneuFinder]] | scWGS read counts in mappability-variable bins averaging ~1 Mb, GC-corrected | States from nullisomy to decasomy; negative binomial for all states except nullisomy, which takes a delta distribution because zero copies means zero reads, not a low count | ([[10-Summaries/bakker-2016-aneufinder\|AneuFinder]]) |
| Segmentation with variable bins | [[10-Summaries/garvin-2015-natmethods\|Ginkgo]] | Low-depth (<1×) scDNA-seq read counts | Segmentation-based integer calling with variable bins | ([[10-Summaries/garvin-2015-natmethods\|Ginkgo]]) |
| Latent-factor normalization | [[10-Summaries/wang-2020-scope\|SCOPE]] | Sparse scDNA-seq read counts | Normalization by a latent-factor model before segmentation | ([[10-Summaries/wang-2020-scope\|SCOPE]]) |
| Unbalanced Haar wavelet segmentation | [[10-Summaries/wesley-2026-songbird\|Songbird]] | DLP+ read depth, down to 0.01× per cell | Splits a span at any point rather than only at its midpoint; fits integer copy number by likelihood ratio against a uniform null, because a plain likelihood always favours higher ploidy | ([[10-Summaries/wesley-2026-songbird\|Songbird]]) |
| Absolute ploidy from fragment overlap | [[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]] | Direct-tagmentation scWGS | Compares observed fragment overlap per copy state with a closed-form expectation, then adjusts ploidy at P < 1% | ([[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]]) |
| Absolute ploidy from scaling factor and read density | [[10-Summaries/schneider-2024-scabsolute\|scAbsolute]] | Paired-end, amplification-free data at ρ ≥ 75 (~0.01–0.02×) | Fits ρ (reads per copy per bin) with a grid-constrained Dirichlet-process Gaussian mixture, checked against overlapping unique read pairs | ([[10-Summaries/schneider-2024-scabsolute\|scAbsolute]]) |
| Joint calling with an event tree | [[10-Summaries/kuipers-2025-scicone\|SCICoNE]] | Shallow (≤0.1×) per-cell data | Shared evolutionary history denoises per-cell calls instead of feeding pre-called profiles into tree inference | ([[10-Summaries/kuipers-2025-scicone\|SCICoNE]]) |
| Evolution-aware haplotype-specific calling | [[10-Summaries/ivanovic-2025-cnrein\|CNRein]] | Per-cell read depth and BAF | A per-tumour neural network, trained by reinforcement learning, gives the probability of each CNA step from the normal cell; each call balances the cell's own data against this shared model | ([[10-Summaries/ivanovic-2025-cnrein\|CNRein]]) |
| BAF-aware high-resolution calling | [[10-Summaries/zhao-2025-hiscanner\|HiScanner]] | High-coverage PTA (20–30×) | Sets the smallest bin from the size distribution of allelic-dropout events; can call copy-neutral LOH | ([[10-Summaries/zhao-2025-hiscanner\|HiScanner]]) |
| Clone clustering then clone-specific HMM | [[10-Summaries/liu-2024-cot\|CoT]] | scDNA-seq read counts | Clusters cells from transformer embeddings, then fits an HMM per clone with states up to 10 copies | ([[10-Summaries/liu-2024-cot\|CoT]]) |
| Targeted amplicon panels | [[10-Summaries/sollier-2023-compass\|COMPASS]] | Tapestri amplicon scDNA-seq | Calls CNAs and CNLOH alongside SNVs when amplicon-specific coverage is modelled | ([[10-Summaries/sollier-2023-compass\|COMPASS]]) |

### From other modalities

| Approach | Example tools | Input | What it adds | Source |
|---|---|---|---|---|
| Expression-based inference | [[10-Summaries/tickle-2019-infercnv\|inferCNV]], [[10-Summaries/gao-2021-copykat\|CopyKAT]] | scRNA-seq | Convenient, but weaker as a clonality signal than mtDNA variants | ([[10-Summaries/tickle-2019-infercnv\|inferCNV]]; [[10-Summaries/gao-2021-copykat\|CopyKAT]]; [[10-Summaries/ludwig-2019-mtdna-lineage-tracing\|Ludwig 2019]]) |
| Chromatin-accessibility read depth | [[10-Summaries/ramakrishnan-2023-epianeufinder\|epiAneufinder]] | scATAC-seq, 100 kb bins, GC-corrected | Per-cell loss/normal/gain by Anderson–Darling binary segmentation, without a euploid reference | ([[10-Summaries/ramakrishnan-2023-epianeufinder\|epiAneufinder]]) |
| Hi-C contact maps | NeoLoopFinder in [[10-Summaries/chang-2025-droplet-hi-c\|Droplet Hi-C]]; [[10-Summaries/li-2023-scnanohi-c\|scNanoHi-C]] | Single-cell Hi-C contacts | Copy number from the same cells as chromatin architecture; *cis*-short (<1 kb) contacts, usually discarded, are useful for CNV and SV analysis | ([[10-Summaries/chang-2025-droplet-hi-c\|Chang 2025]]; [[10-Summaries/li-2023-scnanohi-c\|scNanoHi-C]]) |
| Genome reads in a multiome assay | ASCAT.sc in [[10-Summaries/pancikova-2025-splongget\|SPLONGGET]]; [[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]] | Per-cell DNA library alongside RNA and/or accessibility | Direct per-cell CNA calls measured on DNA rather than inferred from RNA, linked to the same cell's phenotype | ([[10-Summaries/pancikova-2025-splongget\|SPLONGGET]]; [[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]]) |

### Bulk and foundation-model representations

- MutationProjector represents copy number as binary per-gene amplification and deletion states over 468 panel genes ([[10-Summaries/kong-2026-mutationprojector|MutationProjector]]).
- TESSERA's CNA encoder works on segment means and LOH, with attention between segments ([[10-Summaries/sidhom-2026-tessera|TESSERA]]).

## Resolution

| Platform / chemistry | Smallest reliable segment | Source |
|---|---|---|
| Contemporaneous WGA-based single cells | Could not reliably detect germline variants below 5 Mb | ([[10-Summaries/zahn-2017-dlp\|Zahn 2017]]) |
| Earlier single-cell surveys | ~3 Mb floor | ([[10-Summaries/zhao-2025-hiscanner\|HiScanner]]) |
| Amplification-free shallow libraries (DLP) | 1–5 Mb routinely against a clonal profile; 100–500 kb in the deepest cells | ([[10-Summaries/zahn-2017-dlp\|Zahn 2017]]) |
| Modern platforms, ~0.1× per cell across tens of thousands of cells | ~100 kb | ([[10-Summaries/wang-2021-medalt\|MEDALT]]) |
| High-coverage PTA (20–30×) | ~300 kb (smallest bin 100 kb) | ([[10-Summaries/zhao-2025-hiscanner\|HiScanner]]) |
| Direct-tagmentation scWGS, clone pseudobulks re-segmented at 10 kb | 140 kb segment found | ([[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]]) |
| Simulations across callers (HiScanner, Ginkgo, SCOPE, SCYN, CHISEL) | All struggled below 500 kb | ([[10-Summaries/zhao-2025-hiscanner\|HiScanner]]) |

- In direct-tagmentation scWGS, 10–40 kb bins segmented better than the usual 200–500 kb once sensitivity was scaled to per-bin depth, with no loss of sensitivity down to 100,000 reads per cell ([[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]).
- Re-segmenting clone pseudobulks at 10 kb recovered 11 of 13 bulk-WGS segments above 100 kb ([[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]).
- HiScanner sets its smallest bin from the size distribution of allelic-dropout events, which gives 100 kb for PTA ([[10-Summaries/zhao-2025-hiscanner|HiScanner]]).
- Only BAF-aware callers (HiScanner, CHISEL) can call copy-neutral LOH, and CHISEL did better on cnLOH above ~1 Mb ([[10-Summaries/zhao-2025-hiscanner|HiScanner]]).

## Evidence and examples

**Benchmarks of callers**

- In simulations at 2–8 reads per bin, SCICoNE had lower CN error than HMMcopy, Ginkgo, SCOPE, CONET and NestedBD ([[10-Summaries/kuipers-2025-scicone|SCICoNE]]).
- Comparing diploid- and tetraploid-rooted trees by likelihood, SCICoNE detected a whole-genome duplication in a 2053-cell 10x TNBC dataset ([[10-Summaries/kuipers-2025-scicone|SCICoNE]]).
- Down to 0.01× per cell (about 100,000 fragment pairs), Songbird recovered as many true HEK293T breakpoints as HMMCopy, HaarSeg, CoNVEX and CBS, or more ([[10-Summaries/wesley-2026-songbird|Songbird]]).
- On a ploidy ladder, the read-depth-only callers HMMCopy and SCOPE called 2× and 3× hTERT wells as copy number 2 ([[10-Summaries/wesley-2026-songbird|Songbird]]).
- In 20 simulations of 1000 cells, CNRein's median accuracy was 0.956, against 0.882 for SIGNALS and 0.857 for CHISEL ([[10-Summaries/ivanovic-2025-cnrein|CNRein]]).
- On a 10x breast tumour, CNRein called 206 unique profiles among 785 cells, where SIGNALS, CHISEL and Alleloscope called 785, 737 and 747; the same pipeline without the evolutionary model (CNNaive) called 628 ([[10-Summaries/ivanovic-2025-cnrein|CNRein]]).
- CoT reached copy-number F-measure 0.81–0.84 against CHISEL calls on three 10x breast tumour sections, compared with 0.73–0.78 for rcCAE ([[10-Summaries/liu-2024-cot|CoT]]).
- In 65 neurotypical brain cells, 609 of HiScanner's 614 CNAs (99.3%) were below the ~3 Mb floor of earlier single-cell surveys, with an estimated FDR of 26.3% ([[10-Summaries/zhao-2025-hiscanner|HiScanner]]).
- In an AML tumour/normal genome, 46.4% of BreakDancer deletion calls overlapped known inherited CNVs in DGV, and 37 of 116 array-detected inherited CNVs (31.9%) were recovered ([[10-Summaries/chen-2009-breakdancer|BreakDancer]]).

**Copy number from other modalities**

- epiAneufinder correlated with scWGS at r = 0.86 in SNU601, versus 0.74 for Copy-scAT and 0.61 for inferCNV ([[10-Summaries/ramakrishnan-2023-epianeufinder|epiAneufinder]]).
- Droplet Hi-C estimated per-cell copy number with NeoLoopFinder (assuming a diploid baseline) and recovered *MYC* amplification in COLO320 lines, chr7 gain and chr10 loss in a primary glioblastoma, and malignant-versus-normal separation ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]).
- In scNanoHi-C, 93 of 262 GM12878 cells carried CNVs, mostly on chr1 or chr16, matching MALBAC scWGS (35% vs 38% of cells with clear CNVs) ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).
- Merged scNanoHi-C data from 88 K562 cells correlated with ~60× WGS better than bulk Hi-C did ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).
- With DNA libraries at ~20% saturation, SPLONGGET derived 3,800 single-cell copy-number profiles (ASCAT.sc, 500 kb bins) across four B-ALL time points, and InferCNVpy on the matching transcriptomes supported the calls ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).
- In the same SPLONGGET cells, a chr7p loss and 7q gain lowered 7p expression and accessibility and raised 7q, measured against a DNA-based CN call rather than inferred from RNA ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).

**Biological findings**

- In 123 AML patients, COMPASS found CNAs in 42 samples (31 CNLOH, 26 deletions, 12 gains); majority-clone calls were largely confirmed by bulk sequencing or SNP arrays, and subclonal events were invisible in bulk ([[10-Summaries/sollier-2023-compass|COMPASS]]).
- wellDA-seq found rare aneuploid cells in two normal breasts (10/1,339 = 0.75% and 5/1,115 = 0.45%), all with LumSec chromatin identity and all carrying a chr1q gain ([[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]).
- In 9 ER+ breast tumours, 80.88% of 225 aneuploid non-epithelial cells had chrX loss, mainly T cells (4.30% of 2,838) and pericytes (5.50%, 49/891) ([[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]).

**Foundation-model gap evidence**

- MutationProjector's masked-gene pretraining recovers dependencies such as CCND1–CDKN2A co-occurrence in head and neck cancer ([[10-Summaries/kong-2026-mutationprojector|MutationProjector]]).
- In TESSERA's CNA encoder, one block of attention between segments raised masked segment-mean prediction from Pearson r 0.222 to 0.779 and LOH AUC from 0.683 to 0.943, and transfer to MSK-IMPACT panels reached r 0.727–0.746 after quantile normalisation ([[10-Summaries/sidhom-2026-tessera|TESSERA]]).

## Contested points

- **Absolute ploidy is underdetermined.** Fitting a per-cell scale factor cannot tell a profile from its double or half ([[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]); diploid and tetraploid fits of the same profile are equally good ([[10-Summaries/schneider-2024-scabsolute|scAbsolute]]). ASCENT and scAbsolute use fragment overlap or read density to break the tie ([[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]; [[10-Summaries/schneider-2024-scabsolute|scAbsolute]]), Songbird uses a likelihood ratio against a uniform null ([[10-Summaries/wesley-2026-songbird|Songbird]]), and SCICoNE compares diploid- and tetraploid-rooted trees ([[10-Summaries/kuipers-2025-scicone|SCICoNE]]).
- **scAbsolute is not a copy-number caller.** The authors state it is meant for ploidy estimation, not accurate copy-number calls ([[10-Summaries/schneider-2024-scabsolute|scAbsolute]]).
- **Baseline-relative methods miss genome-wide changes.** epiAneufinder cannot detect whole-genome duplications or deletions, because these shift the genome-wide baseline ([[10-Summaries/ramakrishnan-2023-epianeufinder|epiAneufinder]]). Droplet Hi-C copy-number calls also assume a diploid baseline ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]), so the same limit likely applies there (synthesis).
- **Transcriptome-derived CNV is a weaker clonality signal** than mtDNA variants ([[10-Summaries/ludwig-2019-mtdna-lineage-tracing|Ludwig 2019]]).
- **Sub-megabase calls carry a real false-discovery cost.** HiScanner's sub-3 Mb calls came with an estimated FDR of 26.3% ([[10-Summaries/zhao-2025-hiscanner|HiScanner]]), while ASCENT reports that 10–40 kb bins segment better than 200–500 kb bins down to 100,000 reads per cell ([[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]); the two use different chemistries and validation designs, so their resolution claims are not directly comparable (synthesis).
- **CNAs violate the infinite-sites assumption.** A genomic locus is repeatedly altered by successive CNAs, so the infinite-sites assumption underlying standard phylogenetics is violated, and Euclidean, Hamming or correlation distances misrepresent the segmental, non-linear nature of CNA evolution ([[10-Summaries/wang-2021-medalt|MEDALT]]). Minimal event distance is the CNA-appropriate metric ([[10-Summaries/wang-2021-medalt|MEDALT]]); see [[phylogenetic-inference]].

## Related

> [!cards]
> - `concept` [[30-Concepts/chromosomal-instability|Chromosomal instability]] — The rate of mis-segregation, as opposed to aneuploidy, the resulting state.
> - `concept` [[30-Concepts/intratumor-heterogeneity|Intratumor heterogeneity]] — Variation between cells within one tumour, and the clone-detection design rule.
> - `concept` [[30-Concepts/phylogenetic-inference|Phylogenetic inference]] — Reconstructing a cell-division tree from heritable markers; why CNAs need event distances.
> - `hub` [[40-Topics/cancer-clonal-evolution|Cancer clonal evolution]] — Somatic mutation and clonal selection reconstructed from bulk and single-cell DNA.

## All sources on this page

> [!info]- 24 summaries cited here
> - [[10-Summaries/bakker-2016-aneufinder|Bakker 2016]]
> - [[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]
> - [[10-Summaries/chen-2009-breakdancer|Chen 2009]]
> - [[10-Summaries/gao-2021-copykat|Gao 2021]]
> - [[10-Summaries/garvin-2015-natmethods|Garvin 2015]]
> - [[10-Summaries/ivanovic-2025-cnrein|Ivanovic & El-Kebir 2025]]
> - [[10-Summaries/kolbeinsdottir-2025-ascent|Kolbeinsdottir 2025]]
> - [[10-Summaries/kong-2026-mutationprojector|Kong 2026 (Cancer Discov)]]
> - [[10-Summaries/kuipers-2025-scicone|Kuipers 2025]]
> - [[10-Summaries/li-2023-scnanohi-c|Li 2023]]
> - [[10-Summaries/liu-2024-cot|Liu 2024 (Brief Bioinform)]]
> - [[10-Summaries/ludwig-2019-mtdna-lineage-tracing|Ludwig 2019]]
> - [[10-Summaries/pancikova-2025-splongget|Pančíková 2025 (bioRxiv preprint)]]
> - [[10-Summaries/ramakrishnan-2023-epianeufinder|Ramakrishnan 2023]]
> - [[10-Summaries/schneider-2024-scabsolute|Schneider 2024]]
> - [[10-Summaries/sidhom-2026-tessera|Sidhom 2026 (bioRxiv)]]
> - [[10-Summaries/sollier-2023-compass|Sollier 2023]]
> - [[10-Summaries/tickle-2019-infercnv|Tickle 2019]]
> - [[10-Summaries/wang-2020-scope|Wang 2020]]
> - [[10-Summaries/wang-2021-medalt|Wang 2021]]
> - [[10-Summaries/wang-2024-wellda-seq|Wang 2024]]
> - [[10-Summaries/wesley-2026-songbird|Wesley 2026]]
> - [[10-Summaries/zahn-2017-dlp|Zahn 2017]]
> - [[10-Summaries/zhao-2025-hiscanner|Zhao 2025]]
