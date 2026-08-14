---
type: summary
title: "Huang et al. 2015 — Single-Cell Whole-Genome Amplification and Sequencing: Methodology and Applications"
source: "[[00-Sources/papers/Single-Cell Whole-Genome Amplification and Sequencing_ Methodology and Applications]]"
source_kind: paper
author: "Lei Huang, Fei Ma, Alec Chapman, Sijia Lu, Xiaoliang Sunney Xie (corresponding)"
published: 2015-08-24
ingested: 2026-08-13
doi: "10.1146/annurev-genom-090413-025352"
journal: "Annual Review of Genomics and Human Genetics 16:79–102"
tags: [WGA-review, DOP-PCR, MDA, MALBAC, chimera, allele-dropout, CTC, PGD, PGS, meiotic-recombination, review]
entities: []
concepts: ["[[scwga]]", "[[scwga-chemistries]]", "[[dop-pcr]]", "[[mda]]", "[[malbac]]", "[[allele-dropout]]", "[[copy-number-variation]]", "[[structural-variants]]", "[[quality-control-metrics]]"]
topics: ["[[whole-genome-amplification]]", "[[scdna-seq]]", "[[scdna-cancer-applications]]"]
---

**Citation:** Huang, Ma, Chapman, Lu & Xie (2015) — *Single-Cell Whole-Genome Amplification and Sequencing: Methodology and Applications* — *Annual Review of Genomics and Human Genetics* 16, 79–102. [DOI](https://doi.org/10.1146/annurev-genom-090413-025352)

# Huang 2015 — scWGA methodology review

> The canonical review of the three pre-PTA amplification chemistries, from the lab that invented one of them. Its lasting contribution is not the chemistry descriptions but the **parameter vocabulary**: coverage, uniformity, reproducibility, unmappable rate, **chimera rate**, allele dropout rate, SNV false-positive rate, and CNV-calling ability — eight axes that the field still uses to argue about WGA.

## Key claims

- **WGA quality is eight-dimensional, and no chemistry dominates all eight.** Naming the axes is the review's structural contribution: a method can be excellent on uniformity and useless on ADO, and a single "accuracy" number hides that.
- **Three chemistries, three logics.** [[dop-pcr|DOP-PCR]] (Telenius 1992) descends from PEP-PCR and uses degenerate primers — exponential, biased, but even at coarse scale. [[mda|MDA]] (Dean 2002) uses φ29's strand displacement — isothermal, high fidelity, high yield, but wildly non-uniform. [[malbac|MALBAC]] (Zong 2012, this lab) uses quasi-linear pre-amplification via looped amplicons before PCR, explicitly to break the exponential bias compounding of the other two.
- **Chimeras are a first-class problem, not a footnote.** The review names chimera formation as the reason **structural variations are difficult to observe at the single-cell level**, while CNVs from hundreds of kilobases to megabases are detectable relatively easily. This is the cleanest statement in the corpus of *why* single-cell SV calling lagged single-cell CNV calling by a decade.
- **Contamination control is a physical-plant requirement, not a protocol step.** The authors state WGA should run in a dedicated clean room with controlled air pressure and quality; under those conditions bacterial contamination stays below 0.1% of a human cell's DNA. Microfluidic devices are the alternative, and are described as *particularly* important for bacterial WGA — where the contaminating and target genomes are the same kind of thing.
- **Five commercial kits are compared by deep sequencing of multiple single cells** — an in-review benchmark rather than a literature summary.
- **The application list defines the field's early market**: whole-genome de novo mutation rates, early cancer genome evolution, circulating tumour cells, meiotic recombination in germ cells, and preimplantation genetic diagnosis/screening (PGD/PGS) for IVF embryos. PGD/PGS is the clinical application that funded much of the chemistry development and is largely absent from the neuro- and cancer-focused parts of this wiki.
- **Four reasons single-cell genomes are needed**, stated crisply: cells that are precious and rare (oocytes, CTCs); cells that are intrinsically unique (every sperm differs by recombination); temporal evolution readable from stochastic change; and distributions rather than means in heterogeneous tissue.
- **The review explicitly excludes the epigenome.** Single-cell methylomes are acknowledged as achieved but declared out of scope — a boundary that the field spent the following decade erasing.

## Methods / evidence

Narrative review plus original comparative deep sequencing of five commercial kits. Written by the MALBAC originators, which is worth holding in mind when reading the comparative sections — though the parameter framework itself is chemistry-neutral and has been adopted by groups with no stake in MALBAC.

## Surprising or load-bearing bits

- **"Structural variations are difficult to observe … because of chimeras" is the sentence to cite** when explaining why [[falconer-2012-natmethods|Strand-seq]] and [[sanders-2020-sctrip|scTRIP]] took a completely different route (template-strand inheritance) to single-cell SV detection rather than improving WGA.
- **The clean-room requirement is a scaling constraint that later chemistries did not remove.** It applies equally to [[pta|PTA]]. Any protocol amplifying picograms of DNA inherits it.
- **Naming "reproducibility" as a distinct axis from "uniformity"** is subtle and useful: a method can be consistently biased (reproducible, non-uniform — which is fine for CNV calling with matched controls) or randomly biased (non-reproducible — which is not).
- **Sperm-cell recombination as a motivating application** is the one use case where single-cell resolution is not a convenience but a logical necessity: the recombination pattern *only exists* per cell.
- Read against [[hou-2015-wga-comparison]], published three weeks earlier in the same year, the two reviews converge on the same chemistry ordering from independent data — an unusual concordance for WGA benchmarking.

## Concepts touched

- [[scwga-chemistries]] — the canonical three-chemistry taxonomy and the eight evaluation parameters.
- [[structural-variants]] — the chimera explanation for why SVs resist single-cell detection.
- [[quality-control-metrics]] — the eight-axis vocabulary.

## Connections to other sources

- Matched independent benchmark published the same year: [[hou-2015-wga-comparison]].
- Chemistry primaries: [[telenius-1992-dop-pcr]], [[dean-2002-mda]], [[chenghang-2012-science]] (MALBAC, this lab), [[zong-2017-malbac-protocol]].
- Later chemistries that reset the parameter table: [[chen-2017-lianti]], [[gonzalez-pena-2021-pnas]] (PTA).
- The amplification-free alternative the review predates: [[zahn-2017-dlp]], [[laks-2019-dlp-plus]].
- Broader single-cell genome reviews: [[gawad-2016-scgenome-review]], [[evrony-2021-scDNA-applications-review]], [[shao-2025-scDNA-mosaicism-review]].
- The chimera problem in a different setting: [[chitsaz-2011-velvet-sc]] and [[bankevich-2012-spades]] treat MDA chimeras as an assembly-graph problem rather than a calling problem.
- The excluded epigenome: [[guo-2013-scrrbs]], [[smallwood-2014-natmethods]] were already published when this review declared methylation out of scope.

## Open questions

- The review's parameter framework has no axis for **indels**, which later proved to be the most chemistry-sensitive variant class ([[luquette-2021-scan2]]).
- Chimera *rate* is named as a parameter but the review does not establish a standard way to measure it; no consensus assay exists in the corpus.
- Whether the clean-room contamination floor (0.1%) is achievable in routine clinical PGD settings is asserted rather than demonstrated.

## Related

- [[hou-2015-wga-comparison]] · [[scwga-chemistries]] · [[40-Topics/whole-genome-amplification]] · [[50-Notes/pta-inflection-point]]
