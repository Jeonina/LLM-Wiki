---
type: summary
title: "Zhu, Preissl & Ren 2020 — Single-cell multimodal omics: the power of many"
source: "[[00-Sources/papers/Single-cell multimodal omics_ the power of many]]"
source_kind: paper
author: "Chenxu Zhu, Sebastian Preissl, Bing Ren (corresponding)"
published: 2020-01-06
ingested: 2026-08-10
doi: "10.1038/s41592-019-0691-5"
journal: "Nature Methods (Comment)"
tags: [multimodal-omics, joint-assays, review, taxonomy, throughput-vs-depth, Method-of-the-Year-2019]
entities: ["[[bing-ren]]"]
concepts: ["[[joint-single-cell-multi-omics]]", "[[sci-car]]", "[[scnmt-seq]]", "[[gt-seq]]", "[[dr-seq]]", "[[sctrio-seq]]", "[[nome-seq]]", "[[cite-seq]]"]
topics: ["[[single-cell-multiomics]]"]
---

**Citation:** Zhu, Preissl & Ren (2020) — *Single-cell multimodal omics: the power of many* — *Nature Methods* 17, 11–14. [DOI](https://doi.org/10.1038/s41592-019-0691-5)

# Zhu 2020 — the power of many

> The Comment that accompanied Nature Methods' Method-of-the-Year designation for single-cell multimodal omics, and the paper that fixed the field's organizing axis: joint assays split into **one-cell-at-a-time, deep** methods versus **droplet/combinatorial-indexing, scalable** methods, and every design choice trades between them.

## Key claims

- The two-category taxonomy is the paper's contribution: (i) plate/tube-based assays maximizing modalities and coverage per cell at low throughput and high cost; (ii) droplet or split-pool combinatorial-indexing assays reaching thousands-to-millions of cells at the cost of sparsity.
- Genome × transcriptome: [[dr-seq]] (primer-based separation) and [[gt-seq]] (physical bead separation) connect sequence variation to expression phenotype in the same cell — the founding pair for genotype–phenotype joint assays.
- Methylome × transcriptome: scM&T-seq, scMT-seq, [[sctrio-seq]], snmCT-seq; the payoff cited is linking heterogeneously methylated elements to variable expression in mouse ES cells.
- Epigenetic-layer crosstalk: scCOOL-seq and scNOMe-seq ([[nome-seq]]) profile nucleosome occupancy plus methylome; snNMT-seq and scNOMeRe-seq add transcription for tri-omic profiles.
- Accessibility × transcriptome at scale: [[sci-car]] (two-round sci), Paired-seq (ligation-based multi-round barcoding, millions of nuclei), SNARE-seq *(not bookmarked)* (droplet).
- 3D genome × methylome: scMethyl-HiC and [[lee-2019-natmethods|snm3C-seq]] — chromatin conformation annotated by methylome-derived cell type.
- Perturbation and protein layers: Perturb-seq/CRISP-seq, Perturb-ATAC, [[cite-seq]]/REAP-seq/ECCITE-seq.

## Methods / evidence

A Comment, not a benchmark — its weight is taxonomic and agenda-setting, and it is written by the Ren lab, i.e. by participants (Paired-seq is theirs). Read it as a map of what existed in late 2019 and as an explicit statement of what the authors thought should be built next.

## Surprising or load-bearing bits

- The stated gaps are the interesting part, and they aged well:
  1. **Histone modifications and TF occupancy were missing** from every scalable joint assay. The authors point at Kaya-Okur's pA-Tn5 ([[kaya-okur-2019-cut-and-tag]]) and propose combining it with sci-CAR/SNARE-seq/Paired-seq — which is precisely what [[zhang-2022-sccut-tag-pro]] and scCUT&Tag-derived joint assays then did.
  2. **Transcriptome × proteome** joint profiling: called out as blocked because RNA and protein resist conversion to a common capture chemistry, and single-cell proteomics was not established. Still largely true in this corpus.
  3. **Spatial** integration (Slide-seq, imaging), with the specific ask that in-situ profiling be extended to methylation and accessibility — answered later by [[cardilla-2025-spatial-methylome]] and [[morriss-2024-spatial-genomics-clonal]].
- Data sparsity is named as possibly requiring "fundamentally new biochemistry" rather than better protocols — a stronger claim than most reviews make, and one that the corpus's imputation tools ([[scatac-imputation]], [[angermueller-2017-genomebiol|DeepCpG]]) implicitly dispute.
- Conspicuously absent from the 2020 taxonomy: the **genotype × epigenome** cell, which had no scalable method until [[izzo-2024-got-cha|GoT-ChA]]. That absence is a direct citation for this wiki's [[mosaicism-and-epigenome-the-synthesis-gap|synthesis gap]] framing.

## Entities mentioned

- [[bing-ren]] — corresponding author; Paired-seq and the sci-based scalability line come from this lab.

## Concepts touched

- [[joint-single-cell-multi-omics]] — this is the canonical taxonomy source for the page.
- The depth-vs-throughput axis it names is the same axis [[droplet-vs-single-molecule-scdna]] applies on the DNA side.

## Connections to other sources

- Superseded in coverage by [[vandereyken-2023-scmultiomics-review]], [[baysoy-2023-multiomics-landscape]] and [[bi-2024-multiomics-review]], but none of them replaces its two-category framing.
- Its predicted CUT&Tag × transcriptome combination is realized in [[zhang-2022-sccut-tag-pro]] and [[bartosovic-2022-nano-cut-tag]].
- Layer-pair coverage is tracked in this wiki at [[joint-assays-by-layer-pair]].

## Open questions

- The proteome gap is still open in this corpus — no single-cell proteomics source is bookmarked at all.
- Whether sparsity is a biochemistry problem or a computation problem is the live disagreement between this Comment and the imputation literature.

## Related

- [[joint-assays-by-layer-pair]] · [[joint-single-cell-multi-omics]] · [[single-cell-multiomics]] · [[vandereyken-2023-scmultiomics-review]]
