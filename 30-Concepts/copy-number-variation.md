---
type: concept
title: Copy Number Variation
aliases: [CNV, CNA, copy number alteration, copy number profiling, copy number]
tags: [CNV, aneuploidy, cancer, single-cell, segmentation]
created: 2026-08-10
updated: 2026-10-12
---

# Copy Number Variation

> Gains and losses of genomic segments, from focal events to whole chromosomes. The most tractable single-cell genomic readout, because it needs breadth rather than depth — and therefore the first thing shallow single-cell WGS could measure well.

## Calling approaches

- **HMM over binned read counts.** Mappability-variable bins averaging ~1 Mb, GC-corrected, with states from nullisomy to decasomy — negative binomial for all states except nullisomy, which takes a delta distribution because zero copies means zero reads, not a low count ([[bakker-2016-aneufinder]]).
- **Segmentation-based** calling with variable bins ([[garvin-2015-natmethods]]) and latent-factor normalization ([[wang-2020-scope]]).
- **From transcriptomes rather than genomes** ([[tickle-2019-infercnv]], [[gao-2021-copykat]]) — convenient but weaker as a clonality signal than mtDNA variants ([[ludwig-2019-mtdna-lineage-tracing]]).
- **Absolute ploidy from fragment overlap.** Fitting a per-cell scale factor cannot tell a profile from its double or half. ASCENT resolves this by comparing observed fragment overlap per copy state with a closed-form expectation, then adjusting ploidy at P < 1% ([[10-Summaries/kolbeinsdottir-2025-ascent]]).

## Resolution

- Amplification-free shallow libraries detect 1–5 Mb segments routinely against a clonal profile, and 100–500 kb in the deepest cells ([[zahn-2017-dlp]]).
- Modern platforms reach ~100 kb at ~0.1× per cell across tens of thousands of cells ([[wang-2021-medalt]]).
- In direct-tagmentation scWGS, 10–40 kb bins segmented better than the usual 200–500 kb once sensitivity was scaled to per-bin depth, with no loss of sensitivity down to 100,000 reads per cell ([[10-Summaries/kolbeinsdottir-2025-ascent]]). Re-segmenting clone pseudobulks at 10 kb found a 140 kb segment, and 11 of 13 bulk-WGS segments above 100 kb ([[10-Summaries/kolbeinsdottir-2025-ascent]]).
- Contemporaneous WGA-based single cells could not reliably detect germline variants below 5 Mb ([[zahn-2017-dlp]]).
- With high-coverage PTA data (20–30×), HiScanner sets the smallest bin from the size distribution of allelic-dropout events (100 kb for PTA) and calls CNAs down to ~300 kb. In 65 neurotypical brain cells, 609 of its 614 CNAs (99.3%) were below the ~3 Mb floor of earlier single-cell surveys, with an estimated FDR of 26.3% ([[10-Summaries/zhao-2025-hiscanner]]).
- In simulations every caller tested (HiScanner, Ginkgo, SCOPE, SCYN, CHISEL) struggled below 500 kb. Only BAF-aware callers (HiScanner, CHISEL) can call copy-neutral LOH, and CHISEL did better on cnLOH above ~1 Mb ([[10-Summaries/zhao-2025-hiscanner]]).

## Why single cells change the interpretation

- **Bulk and single-cell views of the same sample disagree by construction.** Pooling 25 T-ALL cells reproduces the aCGH karyotype exactly, while 56% of the individual cells carry a unique karyotype ([[bakker-2016-aneufinder]]).
- Minor clones present at 6–10% "are not evident in the combined profile" ([[zahn-2017-dlp]]).
- Recurrent aneuploidy is evidence about **selection**, not about stability ([[bakker-2016-aneufinder]]) — see [[chromosomal-instability]].

## The phylogenetic complication

A genomic locus is repeatedly altered by successive CNAs, so the **infinite-sites assumption underlying standard phylogenetics is violated**, and Euclidean, Hamming or correlation distances misrepresent the segmental, non-linear nature of CNA evolution ([[wang-2021-medalt]]). Minimal event distance is the CNA-appropriate metric ([[wang-2021-medalt]]); see [[phylogenetic-inference]].

## Added 2026-10-07

scATAC-seq read depth can be used to call per-cell CNAs without a euploid reference: epiAneufinder bins reads at 100 kb, GC-corrects, and segments each cell by Anderson–Darling binary segmentation into loss/normal/gain, correlating with scWGS at r = 0.86 in SNU601 versus 0.74 for Copy-scAT and 0.61 for inferCNV ([[10-Summaries/ramakrishnan-2023-epianeufinder]]). It cannot detect whole-genome duplications or deletions, because these shift the genome-wide baseline ([[10-Summaries/ramakrishnan-2023-epianeufinder]]).

Targeted (Tapestri) scDNA-seq can call CNAs and CNLOH alongside SNVs when amplicon-specific coverage is modelled: in 123 AML patients COMPASS found CNAs in 42 samples (31 CNLOH, 26 deletions, 12 gains), majority-clone calls largely confirmed by bulk sequencing or SNP arrays, plus subclonal events invisible in bulk [[10-Summaries/sollier-2023-compass]].

Single-cell Hi-C contacts can also be used to infer copy number. Droplet Hi-C estimated per-cell copy number with NeoLoopFinder (assuming a diploid baseline) and recovered *MYC* amplification in COLO320 lines, chr7 gain and chr10 loss in a primary glioblastoma, and malignant-versus-normal separation ([[10-Summaries/chang-2025-droplet-hi-c]]). The authors note that *cis*-short (<1 kb) contacts, usually discarded, are useful for CNV and SV analysis ([[10-Summaries/chang-2025-droplet-hi-c]]).

CNVs can be called from single-cell Hi-C contact maps. In scNanoHi-C, 93 of 262 GM12878 cells carried CNVs, mostly on chr1 or chr16, matching MALBAC scWGS (35% vs 38% of cells with clear CNVs). Merged data from 88 K562 cells correlated with ~60× WGS better than bulk Hi-C did ([[10-Summaries/li-2023-scnanohi-c]]).

SCICoNE calls single-cell copy numbers jointly with a CNA event tree, so shared evolutionary history denoises shallow (≤0.1×) per-cell data instead of feeding pre-called profiles into tree inference ([[10-Summaries/kuipers-2025-scicone]]). In simulations at 2–8 reads per bin it had lower CN error than HMMcopy, Ginkgo, SCOPE, CONET and NestedBD ([[10-Summaries/kuipers-2025-scicone]]). Comparing diploid- and tetraploid-rooted trees by likelihood detected a whole-genome duplication in a 2053-cell 10x TNBC dataset ([[10-Summaries/kuipers-2025-scicone]]).

Songbird segments DLP+ read depth with an unbalanced Haar wavelet, which can split a span at any point rather than only at its midpoint. Down to 0.01× per cell (about 100,000 fragment pairs), it recovered as many true HEK293T breakpoints as HMMCopy, HaarSeg, CoNVEX and CBS, or more ([[10-Summaries/wesley-2026-songbird]]). It fits integer copy number by likelihood ratio against a uniform null, because a plain likelihood always favours higher ploidy ([[10-Summaries/wesley-2026-songbird]]). On a ploidy ladder, the read-depth-only callers HMMCopy and SCOPE called 2× and 3× hTERT wells as copy number 2 ([[10-Summaries/wesley-2026-songbird]]).

Absolute copy number from single cells is underdetermined: diploid and tetraploid fits of the same profile are equally good. scAbsolute fits the scaling factor ρ (reads per copy per bin) with a grid-constrained Dirichlet-process Gaussian mixture, then checks it against read density, i.e. overlapping unique read pairs. This check needs paired-end, amplification-free data at ρ ≥ 75 (~0.01–0.02×) ([[10-Summaries/schneider-2024-scabsolute]]). The authors state it is meant for ploidy estimation, not accurate copy-number calls ([[10-Summaries/schneider-2024-scabsolute]]).

CNRein applies the same idea to haplotype-specific copy number: a per-tumour neural network, trained by reinforcement learning, gives the probability of each CNA step from the normal cell, and each cell's call balances its own read depth and BAF against this shared model ([[10-Summaries/ivanovic-2025-cnrein]]). In 20 simulations of 1000 cells its median accuracy was 0.956, against 0.882 for SIGNALS and 0.857 for CHISEL ([[10-Summaries/ivanovic-2025-cnrein]]). On a 10x breast tumour it called 206 unique profiles among 785 cells, where SIGNALS, CHISEL and Alleloscope called 785, 737 and 747; the same pipeline without the evolutionary model (CNNaive) called 628 ([[10-Summaries/ivanovic-2025-cnrein]]).

In an AML tumour/normal genome, 46.4% of BreakDancer deletion calls overlapped known inherited CNVs in DGV, and 37 of 116 array-detected inherited CNVs (31.9%) were recovered ([[10-Summaries/chen-2009-breakdancer]]). Single-cell genome plus chromatin-accessibility co-profiling (wellDA-seq) found rare aneuploid cells in two normal breasts (10/1,339 = 0.75% and 5/1,115 = 0.45%), all with LumSec chromatin identity and all carrying a chr1q gain; in 9 ER+ breast tumours, 80.88% of 225 aneuploid non-epithelial cells had chrX loss, mainly T cells (4.30% of 2,838) and pericytes (5.50%, 49/891) ([[10-Summaries/wang-2024-wellda-seq]]).

Genome reads from a Multiome-type assay allow direct per-cell CNA calling. With DNA libraries at ~20% saturation, SPLONGGET derived 3,800 single-cell copy-number profiles (ASCAT.sc, 500 kb bins) across four B-ALL time points, and InferCNVpy on the matching transcriptomes supported the calls ([[10-Summaries/pancikova-2025-splongget]]). In the same cells, a chr7p loss and 7q gain lowered 7p expression and accessibility and raised 7q, measured against a DNA-based CN call rather than inferred from RNA ([[10-Summaries/pancikova-2025-splongget]]).

## Added 2026-10-09 — foundation-model gap evidence

- CoT clusters cells from transformer embeddings and then fits a clone-specific HMM (states up to 10 copies), reaching copy-number F-measure 0.81–0.84 against CHISEL calls on three 10x breast tumour sections, compared with 0.73–0.78 for rcCAE ([[10-Summaries/liu-2024-cot]])
- MutationProjector represents copy number as binary per-gene amplification and deletion states over 468 panel genes, and its masked-gene pretraining recovers dependencies such as CCND1–CDKN2A co-occurrence in head and neck cancer ([[10-Summaries/kong-2026-mutationprojector]])
- In TESSERA's CNA encoder, one block of attention between segments raised masked segment-mean prediction from Pearson r 0.222 to 0.779 and LOH AUC from 0.683 to 0.943, and transfer to MSK-IMPACT panels reached r 0.727–0.746 after quantile normalisation ([[10-Summaries/sidhom-2026-tessera]])

## Related

- [[chromosomal-instability]] · [[intratumor-heterogeneity]] · [[phylogenetic-inference]] · [[cancer-clonal-evolution]]
