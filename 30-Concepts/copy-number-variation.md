---
type: concept
title: Copy Number Variation
aliases: [CNV, CNA, copy number alteration, copy number profiling]
tags: [CNV, aneuploidy, cancer, single-cell, segmentation]
created: 2026-08-10
updated: 2026-10-07
---

# Copy Number Variation

> Gains and losses of genomic segments, from focal events to whole chromosomes. The most tractable single-cell genomic readout, because it needs breadth rather than depth — and therefore the first thing shallow single-cell WGS could measure well.

## Calling approaches

- **HMM over binned read counts.** Mappability-variable bins averaging ~1 Mb, GC-corrected, with states from nullisomy to decasomy — negative binomial for all states except nullisomy, which takes a delta distribution because zero copies means zero reads, not a low count ([[bakker-2016-aneufinder]]).
- **Segmentation-based** calling with variable bins ([[garvin-2015-natmethods]]) and latent-factor normalization ([[wang-2020-scope]]).
- **From transcriptomes rather than genomes** ([[tickle-2019-infercnv]], [[gao-2021-copykat]]) — convenient but weaker as a clonality signal than mtDNA variants ([[ludwig-2019-mtdna-lineage-tracing]]).

## Resolution

- Amplification-free shallow libraries detect 1–5 Mb segments routinely against a clonal profile, and 100–500 kb in the deepest cells ([[zahn-2017-dlp]]).
- Modern platforms reach ~100 kb at ~0.1× per cell across tens of thousands of cells ([[wang-2021-medalt]]).
- Contemporaneous WGA-based single cells could not reliably detect germline variants below 5 Mb ([[zahn-2017-dlp]]).

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

In an AML tumour/normal genome, 46.4% of BreakDancer deletion calls overlapped known inherited CNVs in DGV, and 37 of 116 array-detected inherited CNVs (31.9%) were recovered ([[10-Summaries/chen-2009-breakdancer]]). Single-cell genome plus chromatin-accessibility co-profiling (wellDA-seq) reports CNA-bearing cell types in normal breast tissue and CNA-bearing non-epithelial microenvironment cells in breast tumours (abstract-level claim) ([[10-Summaries/wang-2024-wellda-seq]]).


## Related

- [[chromosomal-instability]] · [[intratumor-heterogeneity]] · [[phylogenetic-inference]] · [[cancer-clonal-evolution]]
