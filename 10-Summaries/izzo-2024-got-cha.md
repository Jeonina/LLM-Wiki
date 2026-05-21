---
type: summary
title: "Izzo et al. 2024 — GoT–ChA: genotyping with single-cell chromatin accessibility"
source: "[[00-Sources/papers/Franco_2024_Nature]]"
source_kind: paper
author: "Franco Izzo, Robert M. Myers, Saravanan Ganesan, Levan Mekerishvili, ... Dan A. Landau (corresponding)"
published: 2024-05-08
ingested: 2026-05-07
doi: "10.1038/s41586-024-07388-y"
journal: "Nature 629, 1149–1157"
tags: [single-cell, scATAC-seq, genotyping, hematology, MPN, JAK2, GoT-ChA, chromatin]
entities:
  - "[[20-Entities/franco-izzo]]"
  - "[[20-Entities/dan-a-landau]]"
  - "[[20-Entities/landau-lab]]"
concepts:
  - "[[30-Concepts/got-cha]]"
  - "[[30-Concepts/got]]"
  - "[[30-Concepts/jak2-v617f]]"
  - "[[30-Concepts/myeloproliferative-neoplasm]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/dogma-seq]]"
  - "[[30-Concepts/hematopoietic-differentiation]]"
topics:
  - "[[40-Topics/single-cell-multiomics]]"
  - "[[40-Topics/hematopoietic-malignancies]]"
---

**Citation:** Izzo et al. (2024) — *GoT–ChA: genotyping with single-cell chromatin accessibility* — *Nature*. [DOI](https://doi.org/10.1038/s41586-024-07388-y)

# Izzo et al. 2024 — GoT–ChA: genotyping with single-cell chromatin accessibility

> Thesis: somatic mutations rewire chromatin, but in human samples mutated and wild-type cells are admixed and bulk assays cannot resolve their distinct epigenomes. The authors invent **GoT–ChA**, the gDNA-genotyping analog of [[30-Concepts/got]] — link single-cell ATAC profiles to genotype by amplifying the mutation locus from genomic DNA inside droplets. Applied to JAK2V617F MPN, they show the mutation produces a **cell-intrinsic pro-inflammatory chromatin state in HSCs** before any overt blood phenotype, and a **profibrotic chromatin landscape in MkPs** during myelofibrosis.

## Key claims

- **GoT–ChA captures genotype + chromatin accessibility in the same single nucleus.** Two custom primers added to the 10x scATAC-seq cell-barcoding PCR amplify the mutation-containing genomic locus directly from gDNA — bypassing both expression-level dependence and the transcript-distance limitation that motivated [[30-Concepts/circularization-got]] in [[10-Summaries/nam-2019-got]].
- **Cell-line validation across multiple targets:** TP53 R248 (49.5–49.8% genotyping, 99.7% accuracy), JAK2 V617 (63.2% / 96.2%), NRAS Q61, TP53 M133. CNV scores from scATAC orthogonally confirm genotypes. Multiplexable up to 4 targets simultaneously; genotyping efficiency is independent of locus accessibility.
- **In primary human JAK2V617F MPN (21 samples, 19 patients, 150,643 cells)**: GoT–ChA genotyped 38.1% of cells on average vs **7–10% by RNA-based GoT/scRNA-seq genotyping** — a major throughput gain for low-expression drivers like JAK2.
- **Cell-intrinsic pro-inflammatory phenotype in JAK2V617F-mutant HSCs:** increased gene accessibility for NF-κB target genes (TRAPPC9), TGF-β superfamily (BMPR1B receptor and GDF10 ligand), and MMP15 (matrix remodeling). WT HSCs preferentially accessible at stem/quiescence genes (FRY, HLF, PBX1).
- **STAT motif accessibility is increased in mutant HSCs**, including STAT1/5 — visible already at the **JAK2V617F clonal-hematopoiesis stage**, *before* overt MPN. NFKB1 and REL motifs are specifically increased in homozygous mutant cells.
- **Ruxolitinib (JAK1/2 inhibitor) abolishes the cell-intrinsic TF motif differences** between WT and mutant HSCs, but does not eliminate the mutated clone — consistent with cytokine-suppression rather than clone-eradication.
- **MkPs in myelofibrosis show a distinct, profibrotic inflammatory chromatin landscape** — different signature from the HSC pro-inflammatory state.
- **GoT–ChA + DOGMA-seq integration** (via mitochondrial variant + cell-surface protein imputation): single-cell capture of genotype, chromatin accessibility, RNA, and surface protein simultaneously.

## Methods / evidence

Engineering: scATAC-seq with two extra primers in the cell-barcoding PCR; locus-specific GoT–ChA primers + linear amplification + exponential amplification; library construction. Computational framework released as an R package. Cohort: 18 untreated/ruxolitinib-treated MF patients + 1 longitudinal PV→MF + 1 JAK2V617F clonal hematopoiesis sample. Comparisons within-patient between WT and mutant cells of the same cluster — same design move as [[10-Summaries/nam-2019-got]].

Strong validation chain: cell-line mixing, CNV concordance, multi-locus multiplexing, comparison vs prior cDNA-based methods, longitudinal sampling of one patient through PV→MF transition.

## Surprising or load-bearing bits

- **Pro-inflammatory chromatin priming of HSCs is cell-intrinsic and occurs before overt disease.** Inflammation in MPN was previously framed as microenvironmental; this paper shows the mutated stem cell already carries an open NF-κB/TGF-β chromatin program at the clonal hematopoiesis stage. That's a meaningful causal reframing.
- **Genotyping rate jumps from ~7–10% to ~38%** by switching from cDNA to gDNA capture. This is the single biggest practical improvement over [[30-Concepts/got]] — JAK2 is too lowly expressed for cDNA-based methods to genotype reliably, and gDNA is one copy per cell.
- **Ruxolitinib reverses the chromatin difference but not the clone.** That's a clean mechanistic story for why the drug controls symptoms but doesn't cure: it suppresses the *consequence* (cytokine-driven motif activity) without removing the *cause* (the mutant clone).
- **Compatibility with DOGMA-seq** quietly turns this into a 4-modality assay (genotype + chromatin + RNA + protein) — the most multi-omic single-cell readout in the lineage to date.

## Entities mentioned

- [[20-Entities/franco-izzo]] — first author; co-author on [[10-Summaries/nam-2019-got]] five years prior. Now at Mount Sinai (Icahn).
- [[20-Entities/dan-a-landau]] — senior/corresponding author. Same role on Anna 2019.
- [[20-Entities/landau-lab]] — NYGC/Weill Cornell. The GoT → GoT–ChA evolution is from this group.

## Concepts touched

- [[30-Concepts/got-cha]] — defined here.
- [[30-Concepts/got]] — explicitly framed as the predecessor; this paper notes the cDNA-method limitations that GoT–ChA solves.
- [[30-Concepts/jak2-v617f]] — driver studied; cell-intrinsic chromatin program characterized.
- [[30-Concepts/myeloproliferative-neoplasm]] — disease context (CH, PV, MF).
- [[30-Concepts/chromatin-accessibility]] — single-cell ATAC framework extended with genotyping.
- [[30-Concepts/dogma-seq]] — multi-omic platform integrated by imputation.
- [[30-Concepts/hematopoietic-differentiation]] — JAK2V617F differentiation skews mapped at chromatin level.

## Connections to other sources

- **Directly extends** [[10-Summaries/nam-2019-got]]: same lab (Landau), same disease (MPN), but moves from cDNA→gDNA capture and RNA→chromatin readout. The Anna 2019 paper's "circularization GoT" was a workaround for the transcript-distance problem; GoT–ChA solves the problem at its root by reading the genome directly.
- **Conceptually parallel to** [[10-Summaries/swanson-2025-daf-seq]] (DAF-seq): both link DNA sequence variation to chromatin state in single cells. GoT–ChA scales (10⁵ cells) at the cost of profiling only one chromatin modality (Tn5 accessibility) at one resolution; DAF-seq trades cell number for single-molecule, single-nucleotide resolution and full-length-fiber coverage.

## Open questions

- The pro-inflammatory chromatin program is shown to be cell-intrinsic at the clonal hematopoiesis stage, but the **mechanism** linking JAK2V617F → NF-κB chromatin remodeling is not nailed down (STAT-mediated? direct?).
- Imputation-based DOGMA integration depends on having mitochondrial variants and surface proteins as bridges — how well does this generalize to settings without those signals?
- GoT–ChA captures only *one* mutation per cell by default; multiplexing was demonstrated but at lower per-locus efficiency. How does this scale for clones defined by 4+ co-occurring mutations?

---
**Source:** [DOI](https://doi.org/10.1038/s41586-024-07388-y)
