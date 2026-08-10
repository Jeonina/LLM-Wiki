---
type: concept
title: Copy Number Variation
aliases: [CNV, CNA, copy number alteration, copy number profiling]
tags: [CNV, aneuploidy, cancer, single-cell, segmentation]
created: 2026-08-10
updated: 2026-08-10
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

## Related

- [[chromosomal-instability]] · [[intratumor-heterogeneity]] · [[phylogenetic-inference]] · [[cancer-clonal-evolution]]
