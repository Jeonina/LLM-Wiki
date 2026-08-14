---
type: summary
title: "Chakraborty, Wang & Ay 2022 — dcHiC detects differential compartments across multiple Hi-C datasets"
source: "[[00-Sources/papers/dcHiC detects differential compartments across multiple Hi-C datasets]]"
source_kind: paper
author: "Abhijit Chakraborty, Jeffrey G. Wang, Ferhat Ay (corresponding)"
published: 2022-11-11
ingested: 2026-08-13
doi: "10.1038/s41467-022-34626-6"
journal: "Nature Communications 13:6827"
tags: [dcHiC, differential-compartments, Mahalanobis-distance, quantile-normalization, IHW, lamin-B1, replication-timing, pseudobulk-scHiC]
entities: ["[[ferhat-ay]]"]
concepts: ["[[chromatin-compartments]]", "[[hi-c-normalization]]", "[[dimensionality-reduction]]", "[[replication-timing]]", "[[lamina-associated-domains]]", "[[nuclear-lamina]]", "[[pseudo-bulk]]", "[[single-cell-hi-c]]"]
topics: ["[[3d-genome]]", "[[computational-methods]]", "[[chromatin-architecture]]"]
---

**Citation:** Chakraborty, Wang & Ay (2022) — *dcHiC detects differential compartments across multiple Hi-C datasets* — *Nature Communications* 13, 6827. [DOI](https://doi.org/10.1038/s41467-022-34626-6)

# Chakraborty 2022 — dcHiC

> Compartment analysis had a scaling problem hiding in plain sight: PCA runs on **one contact map at a time**, so comparing many datasets means choosing the right PC and its sign for each, then reconciling scales. dcHiC fixes both ends — automated PC selection and quantile normalisation of compartment scores, then a **Mahalanobis distance** across ≥2 samples with χ² significance. Its most consequential finding is not a method benchmark but a category: **~26% of significant compartment changes involve no A↔B flip at all**, and those within-compartment changes carry real biology.

## Key claims

- **Within-compartment changes are a quarter of the signal and are routinely discarded.** In the ESC→NPC transition, of 1,981 significant 100-kb bins (7.5% of genome), ~74% were flips (A→B 30%, B→A 44%) and **~26% were A→A or B→B** — "strong A in ESCs to weak A in NPCs" and similar. These matched-compartment changes show the same monotonic relationships with lamin B1 association, replication timing, and expression as flips do. Every method that only reports flips misses them by construction.
- **The pipeline is four steps.** Memory-efficient parallel partial SVD (Filebacked Big Matrix, computing only the first few eigenvectors) → automated selection of the PC and sign best correlated with gene density and GC content per sample → quantile normalisation across samples/replicates → Mahalanobis distance with an outlier-trimmed covariance re-estimation, and independent hypothesis weighting on replicate variance for multiple-testing correction.
- **Compartment calls agree with established tools.** Against HOMER (PCA) and CscoreTool on mESC at 100 kb: pairwise Pearson r = 0.96–0.98, and all three correlate with lamin B1 at r ≈ −0.89 to −0.91.
- **dcHiC's differential calls are better supported than HOMER's.** 1,355 of HOMER's 3,042 differential bins overlap dcHiC's 1,981. Method-specific calls from dcHiC show significantly larger ESC-vs-NPC differences in lamin B1, replication timing, and log₂ expression (unpaired *t*-test P < 0.05), more differentially expressed genes, and more histone-mark peak differences per 100 kb for H3K4me1, H3K4me3 and H3K27ac.
- **Speed is a real enabler**: 4–13× faster than CscoreTool and 22–33× faster than HOMER at matched settings; 1.3–15× and 10–52× across all depths and resolutions genome-wide. HOMER did not finish 10-kb genome-wide mESC analysis in 100 hours. Peak memory is comparable (~0.24–1.3 GB).
- **Robustness is characterised, not assumed.** >80% recall of full-depth calls down to 40% downsampling at 100 kb–25 kb; 10 kb needs 60%. Replicates below ~100M reads contribute little. Type-1 error: comparing ESC replicates against each other gives a median of 2 significant bins at 100 kb (vs 1,981 for ESC-vs-NPC), but a median of 751 at 10 kb — **higher-resolution differential analysis is more false-positive-prone**. Comparing samples differing >2–3-fold in depth generates substantial false positives, driven by five chromosomes (4, 5, 14, 17, X) whose compartment scores degrade first at low depth.
- **Differential compartments imply sub-compartment transitions.** 97.5% of dcHiC differential bins with Calder labels in both cell types overlap differential sub-compartment labels, versus 57.5% of non-differential bins — but because 60.5% of all bins show some sub-compartment transition, sub-compartment differencing alone would have poor specificity. dcHiC calls are enriched for transitions of hierarchical distance ≥3 (e.g. A.1.1→A.2.2 or A.1.1→B.1.1).
- **Differential interaction analysis extends the framework.** Users can feed in Fit-Hi-C/HiCCUPS/Mustache calls, filter to differential compartments, and test contact-count differences. At *Dppa2/4*, NPC-specific upstream interactions appear while downstream ones are unchanged; at *Ephb1*, ESC-specific interactions with two upstream B compartments weaken as it moves to A in NPCs.
- **Compartment change and expression are not always coupled.** *Pou5f1/Oct4* is ESC-specifically expressed but does not change radial position or compartment during the transition — consistent with prior FISH.
- **Scales from bulk to pseudobulk scHi-C.** Demonstrated on four collections: mouse neural differentiation (n = 3), mouse hematopoiesis (n = 10, revealing changes at *Sox6*, *Meis1*, *Runx2*, *Klf5*), 20 human LCLs, and **single-cell Hi-C from post-natal mouse brain at three developmental stages with as few as 100 cells per time point**.

## Methods / evidence

Four dataset collections spanning bulk and single-cell, resolutions 10–250 kb, with orthogonal validation against lamin B1 association, replication timing, RNA-seq differential expression, histone ChIP-seq peaks, DNA FISH radial-positioning literature, and Calder sub-compartments. Downsampling, resolution sweeps, and replicate-vs-replicate type-1 error experiments.

Weight: the robustness characterisation is the most useful part for practitioners — the 10-kb false-positive result and the depth-mismatch warning are concrete operational limits that most tool papers omit.

## Surprising or load-bearing bits

- **"Strong A → weak A" is a real biological category.** The binary A/B vocabulary has been forcing a continuous quantity into two bins, and a quarter of the changes fall in the gap. This is the same argument [[xiong-2024-scghost|scGHOST]] makes at single-cell resolution via subcompartments — two independent routes to the conclusion that A/B is too coarse.
- **Automated PC-and-sign selection is unglamorous and necessary.** It is the step that makes many-sample comparison tractable at all; the field had been doing it by hand and per-dataset.
- **The 10-kb type-1 error result (median 751 false bins) should be read as a warning label.** High-resolution differential compartment analysis is tempting and, on current data, unreliable.
- **Five chromosomes fail first at low depth** (4, 5, 14, 17, X). A concrete, actionable QC observation that generalises beyond this tool.
- **Sub-compartment differencing has poor specificity** because 60% of bins transition — so the finer annotation does not replace a statistical test. This is a useful caution for anyone tempted to substitute [[xiong-2024-scghost|scGHOST]]-style labels for differential testing.
- **Pseudobulk scHi-C from 100 cells suffices for compartment differencing** — a much lower bar than loop calling ([[yu-2021-snaphic|SnapHiC]]'s 75-cell claim is at 10-kb loops, so the two are comparable and both surprisingly low).

## Entities mentioned

- [[ferhat-ay]] — corresponding author; Hi-C statistical methods (Fit-Hi-C lineage).

## Concepts touched

- [[chromatin-compartments]] — differential analysis, and the within-compartment change category.
- [[hi-c-normalization]] — quantile normalisation of compartment scores as the cross-sample comparability step.
- [[replication-timing]] · [[lamina-associated-domains]] — the orthogonal signals used for validation.

## Connections to other sources

- Compartment framework it extends: [[lieberman-aiden-2009-hic]].
- Single-cell subcompartment counterpart: [[xiong-2024-scghost]]; single-cell loop counterpart: [[yu-2021-snaphic]].
- Tools compared against: HOMER ([[heinz-2010-homer]]), CscoreTool, Fit-Hi-C/HiCCUPS ([[durand-2016-juicer]]).
- Pipeline and storage ecosystem: [[servant-2015-hicpro]], [[abdennur-2020-cooler]], [[kerpedjiev-2018-higlass]].
- Nuclear-organisation validation signals: [[peric-hupkes-2010-lad-differentiation]], [[van-steensel-2017-lads-review]].
- Domain-level structure: [[dixon-2012-tads]], [[lupianez-2015-tad-disruption]].
- Hematopoiesis context: [[hematopoietic-differentiation]], [[40-Topics/clonal-hematopoiesis]].
- Peak calling used for the histone comparison: [[zhang-2008-macs]].

## Open questions

- **Why chromosomes 4, 5, 14, 17 and X degrade first at low depth** is observed and not explained.
- 10-kb differential analysis is offered but its false-positive rate is high; no correction is proposed.
- The single-cell application uses pseudobulk, so cell-to-cell compartment variability — the thing scHi-C uniquely offers — is not exploited.
- Whether within-compartment ("strong A → weak A") changes have a distinct mechanistic basis from flips, or are simply smaller versions of the same process, is untested.

## Related

- [[xiong-2024-scghost]] · [[chromatin-compartments]] · [[lieberman-aiden-2009-hic]] · [[40-Topics/3d-genome]]
