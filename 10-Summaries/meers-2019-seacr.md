---
type: summary
title: "Meers, Tenenbaum & Henikoff 2019 — Peak calling by Sparse Enrichment Analysis for CUT&RUN (SEACR)"
source: "[[00-Sources/papers/Peak calling by Sparse Enrichment Analysis for CUT&RUN chromatin profiling - Epigenetics & Chromatin]]"
source_kind: paper
author: "Michael P. Meers, Dan Tenenbaum, Steven Henikoff (corresponding)"
published: 2019-07-12
ingested: 2026-08-10
doi: "10.1186/s13072-019-0287-4"
journal: "Epigenetics & Chromatin"
tags: [SEACR, peak-calling, CUT&RUN, CUT&Tag, sparse-data, specificity, model-free, broad-domains]
entities: ["[[steven-henikoff]]"]
concepts: ["[[peak-calling]]", "[[cut-and-run]]", "[[cut-and-tag]]", "[[histone-modifications]]", "heterochromatin"]
topics: ["[[computational-methods]]", "[[histone-modifications]]"]
---

**Citation:** Meers, Tenenbaum & Henikoff (2019) — *Peak calling by sparse enrichment analysis for CUT&RUN chromatin profiling* — *Epigenetics & Chromatin* 12, 42. [DOI](https://doi.org/10.1186/s13072-019-0287-4)

# Meers 2019 — SEACR

> CUT&RUN's advantage — almost no background — breaks the peak callers built for ChIP-seq. Poisson and negative-binomial models are tuned to pull signal out of a noisy genome; on a genome that is mostly *empty*, any stray background read looks like local enrichment. SEACR's answer is to abandon the statistical model entirely and set an **empirical threshold from the global distribution of background signal**.

## Key claims

- **The diagnosis.** ChIP-seq is deeply sequenced with high background, so its peak callers are optimized for **recall**. CUT&RUN has low read depth and sparse background, so what it needs is **precision**. The mismatch, not any bug, is why standard callers over-call on CUT&RUN.
- **The algorithm is model-free.** Fragment-spanning read pairs are parsed into **signal blocks** — maximal segments of continuous non-zero depth — and each block's signal is the summed read count. Plotting the proportion of target versus IgG blocks against a signal threshold identifies the value that maximizes target-vs-IgG retention; blocks below it are dropped, as are blocks overlapping a threshold-passing IgG block (which removes multi-mapping and known false-positive artefacts).
- **Two options only**, by design: an IgG control or a global numeric threshold (default IgG), and *stringent* (threshold at the curve's maximum) versus *relaxed* (halfway between the maximum and the knee); default stringent.
- **The true-negative test is the decisive result.** Sox2 is expressed only in hESCs and FoxA2 only in definitive endoderm. In the cell type where the factor is absent, SEACR called **1–2 peaks**; MACS2 and HOMER called **up to ~900** at default thresholds. The selectivity held even in relaxed mode.
- **Precision across depth**: on H3K4me2 subsampled ten times each at twelve depths from 2 to 45 million reads, SEACR exceeded **85% precision** against a stringent ENCODE truth set in every stringent-mode test; MACS2 and HOMER at default cutoffs never reached it. By F1, SEACR relaxed mode won above ~7.5 M reads, and beat even FDR-tightened MACS2 **below 10 M fragments**.
- **Broad domains stay intact.** On K562 H3K27me3, SEACR called far fewer regions than MACS2 or HOMER (28,803 vs 97,247 vs 104,524) yet covered **more sequence** (31.4 Mb vs 28.1 and 18.3) — average region width nearly an order of magnitude greater. At loci like *HOXD*, MACS2 and HOMER fragment the domain; SEACR keeps it as a few large blocks.
- Under 5 minutes per run at every depth tested, with competitive read/write memory.
- Distributed with a web server (seacr.fredhutch.org) for users without command-line access.

## Methods / evidence

Precision–recall against ENCODE ChIP-seq peak calls at multiple subsampling levels for H3K4me2, H3K4me3, H3K27me3 and CTCF; the Sox2/FoxA2 expression-restricted design as a genuine true-negative benchmark (rare in peak-caller papers, and the reason the specificity claim is credible); ablation of MACS2's local lambda as a controlled comparison; runtime and memory profiling over ten trials per depth.

The authors state the circularity risk themselves: the ENCODE truth set was originally called with MACS2, which if anything biases the comparison *against* SEACR.

## Surprising or load-bearing bits

- **Being agnostic to region width is what lets one caller handle both TFs and broad domains.** ChIP-era tools need separate "narrow" and "broad" modes because they model peak shape; signal blocks have no shape prior, so an H3K27me3 domain and a CTCF site are the same kind of object. That the domain-preserving result and the TF-specificity result come from the same default settings is the paper's strongest structural argument.
- **The 900-false-peaks figure is the number to remember**, because it is measured where truth is known by biology rather than by another algorithm. Any CUT&RUN or CUT&Tag analysis run through MACS2 defaults should be assumed to carry a comparable false-positive load.
- SEACR's advantage is **largest at low depth** — which is exactly the single-cell regime. Single-cell CUT&Tag pseudo-bulk tracks per cluster are sparse by construction, so the caller choice matters more there than in bulk, and this is why SEACR is the standard downstream of [[kaya-okur-2019-cut-and-tag|CUT&Tag]] and [[wu-2021-sccut-tag|scCUT&Tag]].
- Interestingly, **disabling MACS2's local lambda improved it for H3K27me3 but not for the other targets** — partial confirmation that local background modelling is specifically what misfires on sparse broad-domain data.
- Model-free means **no parameter to tune and no *p*-value to report**. The threshold is data-derived, which is robust but gives no per-peak significance statistic — a real trade for anyone who needs one.

## Entities mentioned

- [[steven-henikoff]] — corresponding author; developed CUT&RUN and CUT&Tag, so the caller and the assay come from the same lab.

## Concepts touched

- [[peak-calling]] — establishes that the caller must match the assay's background regime, not just the signal type.
- [[cut-and-run]] / [[cut-and-tag]] — SEACR is the default analysis path for both.

## Connections to other sources

- Direct comparison target: [[zhang-2008-macs]] (and HOMER, [[heinz-2010-homer]]).
- Assay context: [[kaya-okur-2019-cut-and-tag]], [[wu-2021-sccut-tag]], [[zhang-2022-sccut-tag-pro]], [[gopalan-2022-multi-cut-and-tag]].
- Alignment input: [[li-2009-bwa]], [[li-2009-samtools]], [[zhang-2021-chromap]].

## Open questions

- The benchmark truth set is MACS2-derived ENCODE ChIP-seq, so "precision" here means agreement with a ChIP-seq consensus. Regions genuinely detectable only by CUT&RUN would be scored as false positives — the evaluation cannot reward them.
- No per-peak significance value is produced, so downstream methods requiring peak-level statistics (differential binding with uncertainty) need another layer.
- Performance on single-cell pseudo-bulk specifically is not tested here; the low-depth results are subsampled bulk, which has different sparsity structure than aggregated single cells.

## Related

- [[peak-calling]] · [[zhang-2008-macs]] · [[kaya-okur-2019-cut-and-tag]] · [[computational-methods]]
