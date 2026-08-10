---
type: note
title: "Open questions — tensions and gaps by domain"
aliases: [open questions, open threads, unresolved tensions]
description: Tensions and gaps surfaced during ingest or lint. Resolve, then move out.
tags: [meta, open-questions]
created: 2026-05-13
updated: 2026-08-10
---

# Open Questions

Tensions and gaps surfaced during ingest or lint. When a question is resolved, remove it here and update the relevant concept/topic page with the resolution.

## Duplex sequencing

- ~~**Single-cell + duplex**~~ — Resolved 2025: closed from two directions ([[50-Notes/single-cell-duplex-sequencing]]). Remaining sub-questions: Duplex-Multiome generalization beyond brain ([[10-Summaries/kriz-2025-duplex-multiome]]); cross-method single-cell duplex benchmark needed.
- Mutation-rate concordance across duplex platforms (SMaHT benchmark) — does it hold for brain, aging muscle, FFPE samples?
- UDSeq vs the SMaHT-benchmarked methods — no cross-comparison yet.
- **Methylation layer absent from single-cell duplex** — Duplex-Multiome reads accessibility + RNA + mutations but not methylation. Closing this would give all four regulatory layers ([[50-Notes/regulatory-layers-overview]]).

## scDNA-seq methods

- Where does scDAF-seq's per-cell ~99% coverage / ~10-cell throughput win over GoT–ChA's ~38% genotyping / 10⁵-cell throughput? See [[50-Notes/droplet-vs-single-molecule-scdna]] for the full breadth-vs-depth synthesis.
- Throughput vs depth: DLP+ (>10⁴ cells low coverage) vs PTA (384 cells, ~95% coverage). Right operating point per question? ([[50-Notes/droplet-vs-single-molecule-scdna]])
- Why is intra-cell haplotype actuation divergence (~61%) nearly equal to inter-cell divergence (~63%)?

## Mosaicism biology

- Tissue-specific mosaic mutation rates beyond skin/intestine/brain.
- **Smoking × somatic SV** burden mechanism in head-and-neck cancer.
- Causality of cell-type-specific somatic mutation burden in AD.
- IRE1-XBP1 as a therapeutic target in CALR-mutant MPN.
- mtDNA heteroplasmy drop at P6 in mouse — mechanism unclear.

## Methylation / chromatin

- 5mC vs 5hmC functional distinction — most measurements still conflate.
- **Causal vs consequential**: does methylation-loss-driven viral mimicry require additional gating factors (e.g., SETDB1, TF availability)?
- Methylation calling accuracy benchmarking across long-read platforms.
- Single-cell long-read methylation — emerging but not routine.
- Decitabine vs azacitidine: distinct demethylation patterns, mechanistic basis unknown.

## 3D genome

- TAD/loop **causality** — drive expression or follow it?
- Per-cell 3D resolution still ~1 Mb; gap to bulk Hi-C ~kb.
- Sonication-based methods (scSPRITE) capture more contacts; will they generalize?

## Wiki

- Does flat-file + `index.md` navigation scale to ~150 pages?
- Practical contradiction-resolution policy beyond flagging.
- Measuring whether the wiki is actually compounding vs accumulating.


## Added 2026-08-10 (foundational/infrastructure ingest)

**Cross-cutting artifact confounds**
- **ADO vs LOH are the same signature in single cells.** LOH detection restricts to ancestral heterozygous sites and reads allele fraction ([[10-Summaries/smukowski-heil-2023-loh]]) — exactly what WGA-induced allele dropout produces. No source in this corpus separates them. The yeast LOH rate (5 orders of magnitude above point mutation) has no human somatic equivalent measured.
- **All bisulfite-based methylomes report 5mC+5hmC.** In hippocampal neurons 5hmC is 22.04% of CpGs ([[10-Summaries/chen-2025-sctaps-sccaps-plus]]) — so brain methylome atlases built on [[10-Summaries/luo-2018-snmc-seq2|snmC-seq2]]/[[10-Summaries/nichols-2022-scimet-v2|sciMETv2]] carry an unquantified composite. Where does it change conclusions?
- **74% of Roadmap "data" is imputed** ([[10-Summaries/roadmap-2015-111-epigenomes]]). Analyses using Roadmap tracks rarely state whether a given track was observed or predicted.
- **Cell-line aneuploidy rates overstate tissue rates ~4–8×** (5.2% vs 0.6–1.2%; [[10-Summaries/laks-2019-dlp-plus]]). Somatic-aneuploidy estimates benchmarked on lines are measuring culture.

**Method assumptions nobody has tested at single-cell scale**
- **Leiden's badly-connected-community defect** was measured on web and citation graphs (14–25%) — never on sparse binary scATAC/scBS kNN graphs, where every published cell-type call depends on it ([[10-Summaries/traag-2019-leiden]]).
- **UMAP distortion on sparse binary epigenomic matrices** is unbenchmarked ([[10-Summaries/mcinnes-2018-umap]]).
- **GREAT's binomial null** assumes point-binding events over a fixed regulatory-domain rule; whether it holds for pseudo-bulked, cluster-size-dependent scATAC differential peaks is unaddressed ([[10-Summaries/mclean-2010-great]]).
- **No systematic benchmark exists** for tagmentation-based joint accessibility+transcriptome methods — stated outright in [[10-Summaries/vandereyken-2023-spatial-multiomics]].
- **No diagonal integration of an epigenomic modality has been validated against ground truth** in this corpus, though matched multimodal assays are the obvious standard ([[10-Summaries/argelaguet-2021-integration-principles]]).

**Biology left open**
- **Is TAD boundary insulation all-or-none per cell, or probabilistic across a population?** Bulk 4C cannot distinguish "every cell leaks a little" from "10% leak a lot" ([[10-Summaries/lupianez-2015-tad-disruption]]).
- **Can 3D-genome measurement distinguish cell identity in a mitotic cell?** Metaphase folding is cell-type-invariant ([[10-Summaries/naumova-2013-mitotic-chromosome]]) — a hard limit for single-cell Hi-C in proliferating tissue.
- **Is bivalency per-cell or a population average?** Sequential ChIP settled it for chromatin fibers; the marks sit on adjacent histones in one nucleosome ([[10-Summaries/rothbart-2014-histone-dna-language]]), and no single-cell method operates at nucleosome-face resolution.
- **Are enhancer LMRs dynamic turnover or maintenance failure?** [[10-Summaries/jones-2012-dna-methylation-functions|Jones 2012]] poses both; the epimutation-clock literature assumes the second without excluding the first.
- **Is the glioblastoma H3K27me3 heterogeneity clonal or plastic?** [[10-Summaries/wu-2021-sccut-tag]] has no paired genotype — the [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|synthesis gap]] restated for histone marks.
- **Do regulatory-primed loci actually get induced later?** 1,340 monocyte-specific repressive-state genes are silent in every cell type ([[10-Summaries/zhang-2022-sccut-tag-pro]]); the priming interpretation is a hypothesis.

**Methods that do not exist**
- Methylome + 3D structure + transcriptome in one cell ([[10-Summaries/vandereyken-2023-spatial-multiomics]]).
- Single-cell proteome-wide analysis alongside other omics layers.
- A bridge for modalities with no RNA-paired multiomic assay — single-cell Hi-C and most scDNA-seq have none, so bridge integration cannot reach them ([[10-Summaries/hao-2024-seurat-v5]]).

## Related

- [[50-Notes/synthesis-targets]] — promising syntheses that would resolve clusters of these questions
- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — the central conceptual gap this wiki is built around
