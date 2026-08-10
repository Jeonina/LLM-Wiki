---
type: concept
title: Peak Calling
aliases: [peak detection, enrichment calling, domain calling]
tags: [ChIP-seq, CUT&Tag, ATAC-seq, statistics, background-model]
created: 2026-08-10
updated: 2026-08-10
---

# Peak Calling

> Identifying genomic regions where a chromatin signal is enriched over background. The central lesson of this corpus is that **the caller must match the assay's background regime**, not merely its signal type.

## The two regimes

**High background, deep sequencing (ChIP-seq).** Callers are optimized for **recall** — pulling signal out of a noisy genome. MACS supplies the canonical machinery: empirically estimate the fragment shift *d* from the bimodal Watson/Crick tag pattern and shift tags by *d*/2, then test each candidate against a **dynamic local background** λ_local = max(λ_BG, λ_1k, λ_5k, λ_10k) rather than a genome-wide Poisson rate ([[zhang-2008-macs]]). Without a control, using λ_local instead of global λ_BG drops the FDR at 7,000 peaks from 41.2% to 3.8% ([[zhang-2008-macs]]).

**Low background, sparse data (CUT&RUN, CUT&Tag, single-cell pseudo-bulk).** The same optimization for recall becomes a liability: on a mostly empty genome any stray background read looks locally enriched ([[meers-2019-seacr]]). SEACR abandons the statistical model entirely, parsing fragments into contiguous **signal blocks** and setting an empirical threshold from the global background distribution ([[meers-2019-seacr]]).

## The decisive benchmark

Sox2 is expressed only in hESCs and FoxA2 only in definitive endoderm. In the cell type where the factor is absent, SEACR called **1–2 peaks** while MACS2 and HOMER called up to **~900** at default thresholds ([[meers-2019-seacr]]). Any CUT&RUN or CUT&Tag analysis run through ChIP-era defaults should be assumed to carry a comparable false-positive load (synthesis).

## Narrow versus broad

Shape-modelling callers need separate narrow and broad modes. Signal blocks have no shape prior, so a TF site and an H3K27me3 domain are the same kind of object: SEACR called far fewer H3K27me3 regions than MACS2 or HOMER (28,803 vs 97,247 vs 104,524) yet covered more sequence (31.4 Mb vs 28.1 and 18.3), keeping domains such as *HOXD* intact where the others fragmented them ([[meers-2019-seacr]]).

## A systematic bias worth knowing

Compact chromatin sonicates poorly and yields longer fragments disfavoured by size selection, so **ChIP-seq efficiency for H3K27me3 and H3K9me3 declines as cells differentiate** — exactly when those marks spread ([[zhang-2008-macs]]). Signal loss reads as biology when it is chemistry, and it is a standing argument for in-situ methods that skip sonication ([[kaya-okur-2019-cut-and-tag]]).

## Related

- [[chip-seq]] · [[cut-and-tag]] · [[cut-and-run]] · [[computational-methods]]
