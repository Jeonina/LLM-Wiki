---
type: summary
title: "Zhang et al. 2008 — Model-based Analysis of ChIP-Seq (MACS)"
source: "[[00-Sources/papers/Model-based Analysis of ChIP-Seq (MACS)]]"
source_kind: paper
author: "Yong Zhang, Tao Liu, Clifford A. Meyer, Jérôme Eeckhoute, David S. Johnson, Bradley E. Bernstein, Chad Nusbaum, Richard M. Myers, Myles Brown, Wei Li, X. Shirley Liu (corresponding)"
published: 2008-09-17
ingested: 2026-08-10
doi: "10.1186/gb-2008-9-9-r137"
journal: "Genome Biology"
tags: [MACS, peak-calling, ChIP-seq, dynamic-lambda, Poisson, FDR, shift-model]
entities: ["[[bradley-bernstein]]"]
concepts: ["[[peak-calling]]", "[[chip-seq]]", "[[histone-modifications]]", "[[scatac-seq]]", "[[cut-and-tag]]"]
topics: ["[[computational-methods]]", "[[histone-modifications]]"]
---

**Citation:** Zhang et al. (2008) — *Model-based analysis of ChIP-Seq (MACS)* — *Genome Biology* 9, R137. [DOI](https://doi.org/10.1186/gb-2008-9-9-r137)

# Zhang 2008 — MACS

> The peak caller that became the field default, on two ideas. First, **empirically estimate the fragment shift** from the bimodal Watson/Crick tag pattern instead of asking the user for it. Second, replace the genome-wide Poisson background with a **local λ** computed in windows around each candidate peak, so regional bias in copy number, chromatin and mappability is subtracted rather than ignored.

## Key claims

- **The shift model.** ChIP-seq tags are fragment *ends*, so a true binding site shows Watson tags upstream and Crick tags downstream. MACS samples 1,000 high-confidence peaks, aligns their strand-separated tags, measures the mode-to-mode distance *d*, and shifts every tag *d*/2 toward the 3′ end.
- The model is accurate against an independent motif-based estimate: FoxA1 *d* = 126 bp (motif estimate 122), NRSF 96 bp (motif 70), CTCF 76 bp (motif 62) — in each case **far below the ~500 bp sonication size**, implying short-read platforms preferentially sequence shorter fragments.
- **Dynamic local background**: λ_local = max(λ_BG, [λ_1k,] λ_5k, λ_10k), estimated from the control where available and from the ChIP sample where not. Candidate peaks are called by Poisson *p*-value against λ_local (default 10⁻⁵) in sliding 2*d* windows, merged, and the maximum-pileup position is reported as the **summit**.
- Redundant tags beyond what sequencing depth warrants (binomial *p* < 10⁻⁵) are removed as amplification artefacts.
- **λ_local matters most when there is no control.** To call 7,000 FoxA1 peaks: FDR 0.4% with a control; **3.8% without a control but using λ_local; 41.2% without a control using global λ_BG**.
- FDR is estimated empirically by **sample swap** — calling control-over-ChIP peaks with identical parameters — rather than by tag randomization.
- Against ChIPSeq Peak Finder, FindPeaks and QuEST, MACS gave fewer false positives, higher motif occurrence within 50 bp of the summit, and better spatial resolution across FoxA1, NRSF and CTCF.
- ChIP-seq versus ChIP-chip on the same factor: 65.4% of ChIP-seq peaks were also found by ChIP-chip; only **21.4% were genuinely sequencing-platform-specific** after accounting for array tiling gaps. ChIP-chip peaks average twice the width of ChIP-seq peaks.

## Methods / evidence

Three public human ChIP-seq datasets (FoxA1/MCF7 generated for the paper, NRSF/Jurkat, CTCF/CD4⁺ T), motif occurrence and summit-to-motif distance as ground-truth-free accuracy proxies, sample-swap FDR, ablation of each of the two contributions (unshifted tags; global λ) to show each is load-bearing, and a saturation table reporting recoverable site fraction at 90%–20% subsampling per fold-enrichment stratum.

## Surprising or load-bearing bits

- **The repressive-mark warning is the most transferable finding, and it is buried in the discussion.** Compact chromatin sonicates poorly and yields longer fragments that are disfavoured by size selection — so ChIP-seq efficiency for **H3K27me3 and H3K9me3 declines as cells differentiate**, exactly when those marks are spreading. Signal loss reads as biology when it is chemistry. This is a systematic bias against the marks that matter most in heterochromatin and it is a standing argument for in-situ methods like [[kaya-okur-2019-cut-and-tag|CUT&Tag]] that skip sonication entirely.
- **λ_local generalizes beyond ChIP-seq** — the authors explicitly propose it for copy-number and digital gene expression, and it is the intellectual ancestor of local-background models throughout the field.
- The 41.2% versus 3.8% FDR gap for control-free calling is the single most practical number here: without an input control, the background model is doing all the work.
- **MACS is the wrong default for CUT&RUN/CUT&Tag**, and by the same token this paper is the necessary background for understanding why: MACS is tuned for high-background, deeply sequenced data and optimized for recall, so on sparse low-background data every spurious read becomes a peak. That is precisely the argument [[meers-2019-seacr|SEACR]] makes — and MACS with local λ *disabled* is the closest ChIP-era approximation of the CUT&RUN regime.
- The FDR caveat the authors flag themselves: when ChIP has more tags than the control, sample-swap FDR is **overly optimistic** even after normalization.

## Entities mentioned

- [[bradley-bernstein]] — co-author; also the source of the bivalent-domain work in [[bernstein-2006-bivalent-chromatin]].

## Concepts touched

- [[peak-calling]] — the founding source for the shift model and dynamic local background.
- [[chip-seq]] — including its systematic bias against repressive marks.

## Connections to other sources

- Superseded for low-background in-situ assays by [[meers-2019-seacr]]; the comparison baseline in that paper.
- The assays whose chemistry avoids the sonication bias diagnosed here: [[kaya-okur-2019-cut-and-tag]], [[wu-2021-sccut-tag]].
- Alternative peak/motif toolkit: [[heinz-2010-homer]]; region-to-function: [[mclean-2010-great]].
- Input format from [[li-2009-samtools]]; a modern fast aligner path via [[zhang-2021-chromap]].

## Open questions

- The magnitude of the repressive-mark efficiency loss is shown qualitatively (from Mikkelsen's data) but never calibrated, so there is no correction factor — only the recommendation to sonicate harder and size-select larger.
- Sequencing saturation is explicitly left to the user, with a per-fold-enrichment saturation table rather than a rule.

## Related

- [[peak-calling]] · [[meers-2019-seacr]] · [[heinz-2010-homer]] · [[computational-methods]]
