---
type: note
title: "Methylation-based cancer-of-origin classifiers — clinical-grade epigenetic memory"
aliases: [methylation classifiers, EPICUP, MNP classifier, tissue-of-origin methylation]
tags: [synthesis, methylation, cancer, classifier, EPICUP, brain-tumor-MNP, epigenetic-memory]
created: 2026-05-19
updated: 2026-05-19
sources: [
  "[[10-Summaries/kim-2017-methylation-memory-review]]",
  "[[10-Summaries/kim-2017-methylation-memory-review]]",
  "[[10-Summaries/smith-2013-methylation-development]]",
  "[[10-Summaries/smith-2013-methylation-development]]",
  "[[10-Summaries/fu-2025-longread-methylation]]",
  "[[10-Summaries/hunt-2022-sctem-seq]]",
  "[[10-Summaries/shen-2026-splicool-seq]]",
  "[[10-Summaries/cardilla-2025-spatial-methylome]]"
]
---

# Methylation-based cancer-of-origin classifiers — clinical-grade epigenetic memory

> DNA methylation patterns are heritable across cell divisions and act as a record of cell-type identity ([[10-Summaries/kim-2017-methylation-memory-review]]; [[10-Summaries/smith-2013-methylation-development]]). Cancer cells retain these signatures even after metastatic spread, which makes **methylation classifiers a practical clinical tool for identifying tissue-of-origin** in difficult diagnostic cases ([[10-Summaries/kim-2017-methylation-memory-review]]). Three deployments have moved methylation-classifier technology from research curiosity to clinical-grade diagnostic: **EPICUP** for cancer of unknown primary (CUP) ([[10-Summaries/kim-2017-methylation-memory-review]]; [[30-Concepts/cancer-of-unknown-primary]]), the **Heidelberg brain-tumor MNP classifier** for CNS neoplasms, and emerging **AML methylation classifiers** for myeloid leukemia subtyping ([[30-Concepts/cancer-of-unknown-primary]]). All three exploit the same underlying biology: methylation is laid down during differentiation by lineage-specific DNMT/TET activity and is largely preserved through tumorigenesis ([[10-Summaries/smith-2013-methylation-development]]; [[10-Summaries/kim-2017-methylation-memory-review]]).

> **Note on corpus coverage** — this wiki ingests Kim 2017 *Experimental & Molecular Medicine* (memory review) and Yilei 2025 *NRG* (computational long-read methylation), which together describe the EPICUP classifier and the broader memory framework. The primary classifier papers (Moran et al. 2016 *Lancet Oncology* on EPICUP, Capper et al. 2018 *Nature* on the brain-tumor MNP classifier) are not directly ingested. This synthesis therefore relies on review summaries rather than primary methods papers, and flags specific claims as `(review-citation)` where they trace through review chains rather than primary sources.

## The biological substrate: methylation as cell-type memory

DNA methylation at CpG dinucleotides is established during differentiation and maintained through cell division by DNMT1 ([[10-Summaries/kim-2017-methylation-memory-review]]). Different cell lineages develop distinct methylation landscapes — bivalent promoters resolved one way or the other, lineage-specific enhancers demethylated, alternative-lineage enhancers methylated ([[10-Summaries/smith-2013-methylation-development]]). The result is a **tissue-of-origin signature** that persists through subsequent mitoses ([[10-Summaries/kim-2017-methylation-memory-review]]).

This signature is **remarkably stable in cancer**. Tumor cells acquire many methylation changes (global hypomethylation, focal promoter hypermethylation) but typically retain the **broad tissue-of-origin pattern** that distinguishes, e.g., a colon-origin carcinoma from a lung-origin carcinoma even after metastasis ([[10-Summaries/kim-2017-methylation-memory-review]]). This stability is the substrate that makes classifier-based diagnosis possible.

## Three deployments

### EPICUP — methylation classifier for CUP

Cancer of unknown primary (CUP) is a metastatic cancer where the primary tumor cannot be localized by imaging/histology — ~3-9% of cancer diagnoses, fourth most common cause of cancer-related death ([[30-Concepts/cancer-of-unknown-primary]]). Median survival is 9 months without origin-targeted therapy; identifying the primary site dramatically improves outcomes.

**EPICUP** (Moran et al. 2016, review-citation via [[10-Summaries/kim-2017-methylation-memory-review]]) trained a methylation-microarray classifier on >2,800 tumors of known origin, then applied it to CUP cases. Reported performance: **188/216 (87%) of CUP cases identified to primary site at 99.6% specificity and 97.7% sensitivity** ([[10-Summaries/kim-2017-methylation-memory-review]]; also [[30-Concepts/cancer-of-unknown-primary]]).

The strength: methylation-classifier predictions inform targeted therapy choices that improve survival. The classifier is now in some clinical workflows in Europe (review-citation).

### Heidelberg MNP — brain-tumor methylation classifier

The DKFZ/Heidelberg brain-tumor **Methylation Network for Pediatric/CNS** classifier (Capper et al. 2018, not directly ingested but referenced via [[30-Concepts/cancer-of-unknown-primary]]) handles CNS tumors specifically — a domain where histological classification has notoriously high inter-observer variability, especially for pediatric and rare entities. Reported clinical-grade discrimination across ~80 brain-tumor classes.

The classifier is **deployed clinically** in major neuropathology centers and has substantially reduced misclassification rates. CNS tumor pathology may be the strongest current case for methylation-classifier-mediated clinical practice — the biology (tissue-of-origin memory) and the diagnostic need (high inter-observer histology variance) align unusually well.

### AML methylation classifiers

Myeloid leukemias show distinct methylation patterns by genetic subtype (DNMT3A R882 vs IDH1/2 vs TET2 vs MLL-rearranged, etc.) ([[10-Summaries/nam-2022-natgenet]]; [[30-Concepts/cancer-of-unknown-primary]]). Methylation-classifier approaches are emerging for AML subtyping, with the underlying biology being that:
- DNMT3A R882 mutations cause selective hypomethylation ([[10-Summaries/nam-2022-natgenet]]).
- IDH1/2 mutations produce 2-hydroxyglutarate, inhibiting TET enzymes → hypermethylation ([[10-Summaries/kim-2017-methylation-memory-review]]).
- MLL-fusion-mediated transformation produces a distinct enhancer-methylation pattern.

Single-cell methylation in AML has progressed via scTEM-seq ([[10-Summaries/hunt-2022-sctem-seq]]) and SpliCOOL-seq ([[10-Summaries/shen-2026-splicool-seq]]). These methods reveal that **decitabine vs azacitidine produce divergent demethylation patterns in AML** ([[10-Summaries/shen-2026-splicool-seq]]) — clinically important because the two hypomethylating agents are usually treated as interchangeable.

## Why methylation succeeds where other epigenetic marks struggle

Several epigenetic axes record cell-type identity (histone marks, accessibility, 3D genome — see [[50-Notes/regulatory-layers-overview]]), but methylation classifiers have outperformed alternatives clinically:

- **Stability through tumorigenesis** — methylation is more stable than histone marks or accessibility, which can drift substantially during clonal evolution ([[10-Summaries/kim-2017-methylation-memory-review]]).
- **Per-CpG measurement** — methylation gives ~28 million distinct binary signals per genome ([[10-Summaries/smith-2013-methylation-development]]), enabling fine-grained classifiers. Histone marks give peak-level signal that's coarser.
- **Sample compatibility** — formalin-fixed paraffin-embedded (FFPE) samples retain methylation well; chromatin and RNA degrade more readily. Clinical pathology archives are FFPE.
- **Microarray maturity** — Illumina 450K/EPIC microarrays gave a standardized, scalable, reproducible measurement platform years before clinical-grade ATAC or CUT&Tag existed (synthesis).

The implication: **methylation classifiers have a 5-10-year head start on chromatin-based or accessibility-based classifiers** because the measurement infrastructure matured first.

## What single-cell methylation adds

Bulk methylation classifiers (EPICUP, MNP) work on tumor bulk. Single-cell methylation methods open complementary diagnostic possibilities:

- **Intratumor heterogeneity of methylation classifiers** — does a tumor contain multiple methylation-defined subclones, possibly with different tissue-of-origin signatures? ([[10-Summaries/shen-2026-splicool-seq]]).
- **Per-cell response to hypomethylating agents** — the divergent decitabine vs azacitidine demethylation patterns in single AML cells suggest classifier signatures themselves are perturbed by treatment ([[10-Summaries/hunt-2022-sctem-seq]]).
- **Spatial methylation classifiers** — Cardilla 2025 spatial methylome + transcriptome ([[10-Summaries/cardilla-2025-spatial-methylome]]) shows methylation classification can be done with spatial resolution, identifying tissue-of-origin signatures that vary across regions of the same tumor.

These extensions remain pre-clinical but are the natural successors to bulk classifiers.

## Open questions

- **Cross-classifier comparison** — EPICUP, MNP, and AML classifiers were developed independently. No cross-validation on shared samples has been published (to the wiki's knowledge).
- **Drift under treatment** — chemotherapy and hypomethylating-agent treatment perturb methylation patterns. Do classifiers remain accurate in post-treatment biopsies? ([[10-Summaries/shen-2026-splicool-seq]] hints at divergent demethylation).
- **Single-cell-grade clinical classifiers** — none yet deployed. The infrastructure (sciMETv2, snmC-seq3, SpliCOOL-seq) exists but per-cell sparsity is the bottleneck.
- **Liquid biopsy methylation classifiers** — circulating tumor DNA methylation profiling for tissue-of-origin is emerging but not yet at clinical-grade.
- **Methylation + mutation joint classifiers** — methylation patterns plus driver mutations (DNMT3A, IDH1/2, MLL) jointly are more discriminating than either alone. Joint classifiers underexplored.

## What this synthesis reveals

The methylation-classifier success story has three implications for the wiki's broader framing:

1. **Epigenetic memory is the load-bearing concept** — methylation classifiers work *because* methylation is heritable through mitosis. Other epigenetic marks could in principle yield classifiers, but methylation reached clinical-grade first because it's the most stable. The success of classifiers retroactively validates the [[30-Concepts/epigenetic-memory]] framework.

2. **Tissue-of-origin is a single-axis question** — most clinical diagnostic problems reduce to "which lineage did this tumor come from?" Methylation answers this from a single epigenetic axis; the [[50-Notes/regulatory-layers-overview|four molecular regulatory layers]] are *complementary*, not interchangeable, for this question.

3. **The clinical pipeline lags single-cell** — even now (2026), clinical methylation classifiers run on bulk DNA via microarray. Single-cell-grade methylation classifiers are 5+ years from clinical deployment despite the methodology existing. The gap is regulatory and infrastructure, not biological.

## Limitations of this synthesis

This note is the weakest of the wiki's 5 synthesis notes because the corpus does not directly ingest the primary classifier papers (Moran 2016, Capper 2018). Specific quantitative claims (87% accuracy, 99.6% specificity) trace through review chains rather than primary sources. **Resolving this gap would require ingesting Moran et al. 2016** *Lancet Oncology* **and Capper et al. 2018** *Nature*. Both are well within the wiki's scope and would convert this note from a review-citation synthesis to a primary-source synthesis. Flagged in [[50-Notes/synthesis-targets]] as a follow-up ingest priority.

## Related

- [[30-Concepts/cancer-of-unknown-primary]] · [[30-Concepts/epigenetic-memory]] · [[40-Topics/dna-methylation]]
- [[40-Topics/dna-methylation]] · [[40-Topics/scdna-cancer-applications]]
- [[50-Notes/regulatory-layers-overview]] — methylation as one of four molecular regulatory layers
- [[50-Notes/synthesis-targets]] — this note resolves the "DNA-methylation-based cancer-of-origin classifiers" target, but with the caveat that primary sources are missing
