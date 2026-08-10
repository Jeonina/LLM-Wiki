---
type: summary
title: "Tickle et al. 2019 — inferCNV (Trinity CTAT): inferring CNV from single-cell RNA-seq"
source: "[[00-Sources/papers/broadinstitute_infercnv_ Inferring CNV from Single-Cell RNA-Seq]]"
source_kind: paper
author: "Timothy Tickle, Itay Tirosh, Christophe Georgescu, Maxwell Brown, Brian Haas (Broad Institute)"
published: 2019
ingested: 2026-08-10
doi: ""
journal: "Software (Broad Institute Trinity CTAT project) — https://github.com/broadinstitute/inferCNV"
tags: [inferCNV, CNV-inference, scRNA-seq, computational-tool, deprecated-tool, expression-based-CNV]
entities: []
concepts: ["[[scrna-seq]]", "[[structural-variants]]"]
topics: ["[[cancer-clonal-evolution]]", "[[scdna-cancer-applications]]"]
---

**Citation:** Tickle, Tirosh, Georgescu, Brown & Haas (2019) — *inferCNV of the Trinity CTAT Project* — Broad Institute. [GitHub](https://github.com/broadinstitute/inferCNV)

# Tickle 2019 — inferCNV

> The canonical tool for inferring large-scale copy-number alterations from single-cell **transcriptomes**: average expression across genomically-ordered windows relative to a normal reference cell set, then read chromosome-arm-scale gain/loss from the smoothed residual. It made CNV clone structure readable from scRNA-seq without any DNA assay — and is now formally unsupported.

> ⚠️ **Source caveat + status change.** The bookmarked clipping is the GitHub README, and its first line is a deprecation notice: *"InferCNV is no longer supported."* The maintainers redirect users to **inferCNA**, **CopyKAT** ([[gao-2021-copykat]]) and **Numbat**. Any wiki claim that inferCNV is a current recommendation is now stale.

## Key claims

- CNVs can be inferred from expression averaged over genomic neighborhoods, because arm-level dosage shifts move many genes coherently.
- A normal-cell reference set is required; the inference is relative, not absolute.
- Tumor subclustering resolution is the primary tunable and the primary failure mode — the README singles out oversplitting as the setting most runs must adjust, with Leiden-based subclustering as the preferred mode.

## Methods / evidence

No paper: the artifact is software plus a project wiki and video tutorial. Its evidential standing in the literature comes from downstream use (originally Tirosh/Patel-style melanoma and glioma scRNA-seq studies), not from a self-contained benchmark. That makes it a tool this wiki should cite *as used by others*, and increasingly as a historical baseline.

## Surprising or load-bearing bits

- The deprecation is itself the most useful fact here. inferCNV is cited in a very large fraction of scRNA-seq tumor papers; a review written now should describe it in the past tense and name the successors.
- The "infer DNA from RNA" strategy is a fundamentally different epistemic move from the DNA-native tools in this wiki ([[garvin-2015-natmethods|Ginkgo]], [[bakker-2016-aneufinder|AneuFinder]], [[zaccaria-2021-chisel|CHISEL]]): it trades direct measurement for the ubiquity of scRNA-seq data. Resolution is arm-scale at best, and expression-program confounding (a proliferating cluster can mimic a gain) is unresolvable within the modality.
- Leiden-based subclustering being the "preferred" mode ties this tool to [[traag-2019-leiden]].

## Concepts touched

- [[structural-variants]] — expression-inferred CNV is the lowest-resolution rung of the SV-detection ladder.
- Sets up the contrast that motivates joint DNA–RNA assays ([[gt-seq]], [[dr-seq]], [[sdr-seq]]): if you can measure both, you do not have to infer one from the other.

## Connections to other sources

- Superseded by [[gao-2021-copykat]] (named successor) and, on the DNA side, by [[zaccaria-2021-chisel]] for allele- and haplotype-specific copy number.
- Contrast with [[garvin-2015-natmethods]] and [[bakker-2016-aneufinder|Bakker 2016 (AneuFinder)]], which read CNV from single-cell DNA directly.
- [[lu-2024-cnaphylogeny-review]] surveys where expression-inferred CNV can and cannot feed phylogenetic inference.

## Open questions

- With inferCNV unmaintained, which successor should this wiki treat as canonical — CopyKAT (bookmarked) or Numbat (not bookmarked, and allele-aware)? Numbat is a gap in the corpus.

## Related

- [[gao-2021-copykat]] · [[zaccaria-2021-chisel]] · [[cancer-clonal-evolution]] · [[structural-variants]]
