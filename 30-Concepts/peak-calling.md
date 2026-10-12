---
type: concept
title: Peak Calling
aliases: [peak detection, enrichment calling, domain calling]
tags: [ChIP-seq, CUT&Tag, ATAC-seq, statistics, background-model]
created: 2026-08-10
updated: 2026-10-12
---

# Peak Calling

> Identifying genomic regions where a chromatin signal is enriched over background. The central lesson of this corpus is that **the caller must match the assay's background regime**, not merely its signal type ([[10-Summaries/meers-2019-seacr|SEACR]]; [[10-Summaries/zhang-2008-macs|MACS]]).

> [!abstract] 한눈에
> Peak calling은 chromatin 신호가 background보다 높은 구간을 찾는 일이고, 중요한 것은 신호 종류보다 assay의 background 수준에 맞는 caller를 고르는 것이다. Background가 거의 없는 CUT&RUN·CUT&Tag에 ChIP-seq용 기본값을 쓰면, 표적 인자가 없는 세포에서도 수백 개의 가짜 peak가 나온다 ([[10-Summaries/meers-2019-seacr|SEACR]]).

## Definition

Peak calling identifies genomic regions where a chromatin signal is enriched over background ([[10-Summaries/zhang-2008-macs|MACS]]). Callers differ less in the signal they target than in the background they assume (synthesis).

## Why it matters

Sox2 is expressed only in hESCs and FoxA2 only in definitive endoderm. In the cell type where the factor is absent, SEACR called **1–2 peaks** while MACS2 and HOMER called up to **~900** at default thresholds ([[10-Summaries/meers-2019-seacr|SEACR]]). Any CUT&RUN or CUT&Tag analysis run through ChIP-era defaults should be assumed to carry a comparable false-positive load (synthesis).

## Background regimes

**High background, deep sequencing (ChIP-seq).** Callers are optimized for **recall** — pulling signal out of a noisy genome. MACS supplies the canonical machinery: empirically estimate the fragment shift *d* from the bimodal Watson/Crick tag pattern and shift tags by *d*/2, then test each candidate against a **dynamic local background** λ_local = max(λ_BG, λ_1k, λ_5k, λ_10k) rather than a genome-wide Poisson rate ([[10-Summaries/zhang-2008-macs|MACS]]).

**Low background, sparse data (CUT&RUN, CUT&Tag, single-cell pseudo-bulk).** The same optimization for recall becomes a liability: on a mostly empty genome any stray background read looks locally enriched ([[10-Summaries/meers-2019-seacr|SEACR]]). SEACR abandons the statistical model entirely, parsing fragments into contiguous **signal blocks** and setting an empirical threshold from the global background distribution ([[10-Summaries/meers-2019-seacr|SEACR]]).

| Approach | Assay / regime | How it calls | Source |
|---|---|---|---|
| MACS / MACS2 | ChIP-seq, high background | Shift model plus dynamic local background λ_local | ([[10-Summaries/zhang-2008-macs\|MACS]]) |
| SEACR | CUT&RUN, CUT&Tag, low background | Model-free signal blocks with an empirical global threshold | ([[10-Summaries/meers-2019-seacr\|SEACR]]) |
| Metilene on differentially converted regions | Conversion-based assays (DeChIC-seq) | Compared against an IgG or simulated pseudo-IgG track | ([[10-Summaries/shi-2026-dechic-seq\|DeChIC-seq]]) |
| PATTY correction | CUT&Tag | Corrects Tn5 open-chromatin bias in the profile, used in place of MACS2 peaks | ([[10-Summaries/hu-2026-patty\|PATTY]]) |
| Pseudobulk peaks (MACS2 via Signac/ArchR) | scCUT&Tag | Peaks called on pseudobulk; broad mode for H3K27me3 | ([[10-Summaries/wu-2026-sccut-tag-review\|Wu 2026]]) |
| Fixed-size bins | scHPTM embeddings | No peak calling; generally more competitive than MACS2 or SICER peak sets | ([[10-Summaries/raimundo-2023-schptm-benchmark\|Raimundo 2023]]) |

## Narrow versus broad

Shape-modelling callers need separate narrow and broad modes. Signal blocks have no shape prior, so a TF site and an H3K27me3 domain are the same kind of object: SEACR called far fewer H3K27me3 regions than MACS2 or HOMER (28,803 vs 97,247 vs 104,524) yet covered more sequence (31.4 Mb vs 28.1 and 18.3), keeping domains such as *HOXD* intact where the others fragmented them ([[10-Summaries/meers-2019-seacr|SEACR]]).

## Evidence and examples

- Without a control, using λ_local instead of global λ_BG drops the MACS FDR at 7,000 peaks from 41.2% to 3.8% ([[10-Summaries/zhang-2008-macs|MACS]]).
- For CUT&Tag, SEACR (stringent, threshold 0.01) and MACS2 (narrow, q = 1 × 10⁻⁵, no local lambda) gave similar ~50% ENCODE recall ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]).
- In the same benchmark SEACR had slightly higher precision and was robust to duplication but called wider peaks (1.35–1.68 MACS2 peaks per SEACR peak), while MACS2 called spurious heterochromatic peaks when duplicates were kept in high-duplication samples ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]).
- For CUT&Tag, PATTY-corrected profiles correlated better with expression and antagonistic marks than MACS2 peaks with or without IgG control ([[10-Summaries/hu-2026-patty|PATTY]]).
- For scHPTM embeddings, MACS2 and SICER pseudobulk peak sets and GeneTSS annotations were generally less competitive than fixed-size bins; the gap was smaller for small-peak marks (H3K4me1, H3K4me3) ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]).
- In scCUT&Tag, published "peaks" are often actually fixed bins ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).

## Contested points

- **A systematic bias worth knowing.** Compact chromatin sonicates poorly and yields longer fragments disfavoured by size selection, so **ChIP-seq efficiency for H3K27me3 and H3K9me3 declines as cells differentiate** — exactly when those marks spread ([[10-Summaries/zhang-2008-macs|MACS]]). Signal loss reads as biology when it is chemistry, and it is a standing argument for in-situ methods that skip sonication ([[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]).
- **How large is the SEACR–MACS2 gap?** At default thresholds MACS2 called up to ~900 peaks where the factor was absent ([[10-Summaries/meers-2019-seacr|SEACR]]), whereas with a stringent q-value and no local lambda it matched SEACR's ENCODE recall on CUT&Tag ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]); the gap may depend mostly on MACS2 settings (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/chip-seq|ChIP-seq]] — The high-background assay that MACS-style callers were built for.
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — pA-Tn5 tagmentation at antibody-bound chromatin; low background.
> - `concept` [[30-Concepts/cut-and-run|CUT&RUN]] — pA-MNase cleavage with low background, the setting SEACR targets.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — Analysis tools across the single-cell layers.

## All sources on this page

> [!info]- 8 summaries cited here
> - [[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]
> - [[10-Summaries/hu-2026-patty|Hu 2026]]
> - [[10-Summaries/kaya-okur-2019-cut-and-tag|Kaya-Okur 2019]]
> - [[10-Summaries/meers-2019-seacr|Meers 2019]]
> - [[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]
> - [[10-Summaries/shi-2026-dechic-seq|Shi 2026]]
> - [[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]
> - [[10-Summaries/zhang-2008-macs|Zhang 2008]]
