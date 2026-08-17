---
type: summary
title: "Kwok et al. 2022 — MQuad enables clonal substructure discovery using single cell mitochondrial variants"
source: "[[00-Sources/papers/MQuad enables clonal substructure discovery using single cell mitochondrial variants]]"
source_kind: paper
author: "Aaron Wing Cheung Kwok, Chen Qiao, Rongting Huang, Mai-Har Sham, Joshua W. K. Ho, Yuanhua Huang (corresponding)"
published: 2022-03-08
ingested: 2026-08-17
doi: "10.1038/s41467-022-28845-0"
journal: "Nature Communications 13:1205"
tags: [MQuad, mtDNA-heteroplasmy, clonal-inference, binomial-mixture, BIC, cellsnp-lite, vireoSNP, mgatk, scRNA-seq, scATAC-seq]
entities: []
concepts: ["[[mitochondrial-heteroplasmy]]", "[[mitochondrial-lineage-tracing]]", "[[lineage-tracing]]", "[[single-cell-variant-calling]]", "[[copy-number-variation]]", "[[clustering-algorithms]]"]
topics: ["[[single-cell-lineage-tracing]]", "[[cancer-clonal-evolution]]", "[[computational-methods]]"]
---

**Citation:** Kwok et al. (2022) — *MQuad enables clonal substructure discovery using single cell mitochondrial variants* — *Nature Communications* 13, 1205. [DOI](https://doi.org/10.1038/s41467-022-28845-0)

# Kwok 2022 — MQuad

> mtDNA heteroplasmy is an attractive endogenous lineage barcode — high copy number, mutation rate >10× the nuclear genome — but most mtDNA variants are **noise or non-clonal**, and telling them apart is the whole problem. MQuad's answer is a **binomial mixture test per variant**: fit one shared allele frequency across all cells (H₀) versus a two-component mixture (H₁), and rank variants by **ΔBIC**. A variant that splits the population into two heteroplasmy levels is clonally informative; one that does not is noise.

## Key claims

- **Nuclear callers fail on mtDNA for a structural reason**: [[zafar-2016-monovar|Monovar]] and Conbase assume a **diploid context**, which the mitochondrial genome violates. MQuad's binomial parameter ranges freely from 0 to 1 to accommodate any heteroplasmy level.
- **The ΔBIC cutoff is set automatically** at the inflection ("knee") point of the cumulative ΔBIC distribution — no arbitrary threshold.
- **Large margins over both alternatives on simulated Smart-seq2-like data**: AUPRC 0.976 for MQuad versus 0.800 for mgatk and 0.147 for Monovar (AUROC 1.00 / 0.999 / 0.968). The authors note AUROC is uninformative here because of extreme class imbalance — 15–150 clonal variants against >16,000 true negatives — so **AUPRC is the metric that matters**.
- **Why each competitor fails is diagnosed**, not just measured. Monovar's diploid assumption produces many false positives. mgatk's variance–mean ratio is hard to estimate reliably and suffers high uncertainty in scRNA-seq, where low-allele-frequency variants and sequencing errors abound.
- **Robust across simulation parameters** — number of informative variants per clone, clonal allele frequency, clone-size ratio, evolutionary model — with one exception: **at ≤1% allele frequency all tools fail**, unsurprising since average technical noise sits at 0.44%. Linear evolution is the hardest model for every tool, because clone sizes skew and most variants are shared between clones.
- **It is a pipeline component, not a standalone tool**: cellSNP-lite → MQuad → vireoSNP forms an end-to-end path from genotyping to clonal reconstruction.
- **Assay-agnostic**: works on scRNA-seq, scDNA-seq and scATAC-seq, and complements nuclear SNVs and CNVs to reach finer clonal resolution.

## Methods / evidence

Simulated Smart-seq2-like data with controlled clonal structure and a noisy background, plus multiple experimental datasets across protocols. Benchmarked against mgatk (built for scATAC) and Monovar (built for nuclear diploid genomes).

Weight: the diagnosis of *why* competitors fail is more valuable than the AUPRC numbers, since both comparators were designed for other data types. The 1%-allele-frequency floor is the honest limit.

## Surprising or load-bearing bits

- **The 1% floor sits right on top of the technical noise level (0.44%)**, which means MQuad is not conservative — it is at the physical limit of what the data supports. Any claim about rarer mtDNA subclones needs deeper or cleaner data, not a better algorithm. (synthesis)
- **Linear evolution is the hardest topology to detect**, for a reason that generalises far beyond mtDNA: when clones nest rather than branch, most variants are shared, and shared variants carry little discriminative signal. Star-like clonal expansions are easy; chains are not. (synthesis)
- **AUROC is misleading under class imbalance**, and the paper says so explicitly. Worth carrying into any benchmark reading: with 150 positives against 16,000 negatives, AUROC >0.95 is nearly automatic.
- **mtDNA is the cheap lineage barcode.** Nuclear SNV lineage tracing needs deep WGS of every cell; mtDNA variants come along free with any scRNA/scATAC experiment. MQuad is the filter that makes that free signal usable, and it is why mtDNA tracing scaled while nuclear-SNV tracing did not. (synthesis)
- The clonal-resolution argument is **complementarity, not replacement** — mtDNA variants combined with nuclear SNVs and CNVs give finer structure than any one alone.

## Concepts touched

- [[mitochondrial-heteroplasmy]] — heteroplasmy level as a continuous quantity requiring a non-diploid model.
- [[mitochondrial-lineage-tracing]] — the variant-selection step that makes mtDNA tracing practical.
- [[single-cell-variant-calling]] — a domain-specific caller where general-purpose ones structurally fail.

## Connections to other sources

- The mtDNA lineage-tracing line it serves: [[ludwig-2019-mtdna-lineage-tracing]], [[ludwig-2020-mtscatac-seq]] (the source of mgatk), [[miller-2022-maester]], [[sun-2025-scmitomut]], [[glynos-2023-mtdna-mosaicism]], [[hsieh-2026-scmtmpm-scwmss]].
- Nuclear caller whose diploid assumption it critiques: [[zafar-2016-monovar]].
- Alternative endogenous barcodes: [[scherer-2025-nature]] (epimutation), [[chen-2025-methyltree]] (methylation), [[coorens-2021-nature]] (nuclear somatic SNVs).
- Engineered-recorder alternatives: [[jones-2020-cassiopeia]], [[sashittal-2023-startle]], [[chu-2025-laml]].
- Tree building downstream of clonal assignment: [[jahn-2016-scite]], [[ross-2016-onconem]].
- Review context: [[rodriguez-fraticelli-2026-lineage-tracing-review]], [[wang-2026-multimodal-lineage-computational]].

## Open questions

- **Below 1% heteroplasmy nothing works** — the boundary of mtDNA-based clonal resolution, and it is set by chemistry, not statistics.
- MQuad selects informative variants but does not itself build a lineage tree; the downstream clustering (vireoSNP) is a separate assumption layer.
- Whether mtDNA-defined clones correspond to nuclear-genome-defined clones is addressed as complementarity but not resolved — the two barcodes could in principle disagree. (synthesis)

## Related

- [[ludwig-2019-mtdna-lineage-tracing]] · [[mitochondrial-lineage-tracing]] · [[40-Topics/single-cell-lineage-tracing]]
