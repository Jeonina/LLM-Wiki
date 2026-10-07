---
type: summary
title: "Weinreb et al. 2020 — Lineage tracing on transcriptional landscapes links state to fate during differentiation (LARRY)"
source: "[[00-Sources/papers/Lineage tracing on transcriptional landscapes links state to fate during differentiation]]"
source_quality: full
source_sha256: "2300c00728ef83ab6593d05bd3081d68547de829bab3ecba13e70b9d6b5b429a"
source_kind: paper
author: "Caleb Weinreb, Alejo Rodriguez-Fraticelli, Fernando D. Camargo, Allon M. Klein (corresponding)"
published: 2020-02-14
ingested: 2026-10-07
doi: "10.1126/science.aaw3381"
journal: "Science 367(6479):eaaw3381"
tags: [LARRY, expressed-barcodes, lentiviral-barcoding, state-fate, lineage-tracing, scRNA-seq, hematopoiesis, fate-prediction, hidden-variables, monocyte-ontogeny, pseudotime, trajectory-inference-benchmark]
entities: ["[[alejo-rodriguez-fraticelli]]"]
concepts: ["[[lineage-tracing]]", "[[hematopoietic-differentiation]]", "[[trajectory-inference]]", "[[scrna-seq]]", "[[epigenetic-memory]]", "[[crispr-lineage-recording]]"]
topics: ["[[single-cell-lineage-tracing]]"]
---

**Citation:** Weinreb et al. (2020) — *Lineage tracing on transcriptional landscapes links state to fate during differentiation* — *Science* 367:eaaw3381. [DOI](https://doi.org/10.1126/science.aaw3381)

# Weinreb 2020 — LARRY

> scRNA-seq destroys the cell it measures, so it cannot directly tell which progenitor state leads to which fate. **LARRY** (lineage and RNA recovery) puts a random, **expressed** 28-mer barcode in the 3′ UTR of a lentiviral eGFP, so clones are read out by scRNA-seq. Barcoding mouse haematopoietic progenitors, letting them divide, and sampling sisters early and late (in culture and after transplantation) links early transcriptional state to later clonal fate across >300,000 cells. Two conclusions carry the paper: fate priming lies on a **continuous** landscape, and **sister cells agree on fate far more than transcriptionally similar cells do** — scRNA-seq misses heritable, cell-autonomous fate information (perhaps chromatin state).

## Key claims

- **Tool.** Library of ~0.5 × 10⁶ barcodes, sufficient to label 5,000 cells with <1% overlap between clones; barcodes detected in 93% of GFP⁺ cells; 0.3% of 5,000 barcodes recurred between replicate transductions (chance level).
- **Scale.** 130,887 transcriptomes from culture and 182,173 after transplantation into 10 mice; 38% and 63% of cells in clones of ≥2 cells (5,864 and 7,751 clones), 1,816 and 817 clones spanning early and late time points. Overall: 10,968 single-time-point informative clones and 2,632 multi-time-point clones.
- **Sisters are similar enough to stand in for single-cell trajectories**: day-2 sister pairs had median expression correlation R = 0.846 and 70% fell in the same or neighbouring cluster; ~10% diverged (outside a four-cluster radius, vs 80% for random pairs).
- **Fate priming is a structured continuum.** Unilineage fate domains are well delineated on the day-2 landscape with extended bipotent boundaries rather than discrete stepwise transitions. 447 (391 unique) fate-associated genes in vitro and 190 (173 unique) before transplantation at FDR 0.05; e.g. *Ikzf2* enriched in eosinophil and mast-cell progenitors.
- **Fate is only partly predictable from expression.** Best early prediction accuracy 60% in vitro and 51% in vivo. Transcription factors (n = 1,811) were only marginally better than random gene sets (10% in vitro, 3% in vivo); differentially expressed genes were much better (38%, 20%); adding all highly variable genes did not help.
- **Hidden heritable variables.** Predicting from late, separated sisters beat predicting from early state (76% vs 60% in vitro; 70% vs 52% in vivo). Sisters in separate wells produced identical fate combinations 70% of the time (22% by chance); in separate mice, same dominant fate 71% (23% by chance). In split-well clones (n = 408), mixed outcomes were rarer than expected for uncommitted progenitors across all fate choices tested — priming or precommitment exists within a single measured scRNA state.
- **Two monocyte routes.** Monocytes span a neutrophil-like to DC-like spectrum that tracks clonal coupling to neutrophils (p < 10⁻⁷) or DCs/lymphoid cells (p < 10⁻¹⁷); their progenitors differ (*Flt3*, *Bcl11a*, *Cd74* vs *Elane*, *Mpo*, *Gfi1*) and colocalise with sorted MDPs and GMPs. In native haematopoiesis (transposon barcoding, 12-week chase), Neu–Mo–DC clones were 2.5-fold depleted vs independence (p < 0.001).
- **Benchmark of dynamic inference.** Population balance analysis, WaddingtonOT and FateID missed the early Neu/Mo bifurcation in CD34⁺ progenitors (R < 0.26 vs R = 0.5 for held-out clonal data); top-10 fate-correlated genes (e.g. *Gata2*, *Mef2c*) outperformed the algorithms, but choosing them required clonal data. **Pseudotime held up**: consistent forward velocity, MPP → myelocyte in ~10 days, sister pseudotimes correlated R ≥ 0.89. State-distance and clonal-coupling hierarchies agreed in vitro (r = 0.93) but less in vivo (r = 0.58, p = 0.065).

## Methods / evidence

Lentiviral LARRY barcoding of Lin⁻Kit⁺ (Sca1⁻ or LSK) progenitors in multilineage culture and Lin⁻Sca^hi^Kit⁺ cells transplanted into sublethally irradiated mice; inDrop scRNA-seq; SPRING layouts; machine-learning fate prediction (logistic regression, MLP, NB, KNN, RF) with a data-processing-inequality argument for hidden variables; MDP/GMP sorting and transposon-based native barcoding for validation.

Weight: large, carefully controlled; the hidden-variable inference is indirect (could be noisy scRNA sampling rather than non-transcriptional state — the authors say they cannot distinguish). Restricted to culture and transplantation (lentiviral delivery), which perturb haematopoiesis; cannot resolve events faster than one cell cycle.

## Surprising or load-bearing bits

- **Transcription factors are poor fate predictors** compared with a few hundred differentially expressed genes of all kinds — a counterpoint to TF-centric fate models.
- **"Sisters agree more than look-alikes"** is the result later work keeps citing: it motivates adding epigenomic layers to lineage tracing, and [[li-2023-darlin]] found DNA methylation (not expression or accessibility) carries clonal memory in HSCs. (synthesis)
- **Trajectory algorithms place fate boundaries too late**, while pseudotime ordering itself is validated — a useful split verdict for anyone using RNA-only dynamics.
- Unlike CRISPR recorders, LARRY needs no tree inference, has low barcode dropout and one component, but labels only once (no hierarchy).

## Concepts touched

- [[lineage-tracing]] — expressed static barcodes for state–fate mapping across time points.
- [[hematopoietic-differentiation]] — continuous priming, monocyte dual ontogeny (MDP vs GMP).
- [[trajectory-inference]] — clonal ground truth benchmark: pseudotime yes, fate-boundary placement no.
- [[epigenetic-memory]] — heritable fate bias invisible to scRNA-seq, chromatin proposed as carrier.
- [[crispr-lineage-recording]] — contrasted: LARRY trades hierarchy for simplicity and coverage.

## Connections to other sources

- Successor mouse model from the same groups (inducible CRISPR barcodes + epigenome): [[li-2023-darlin]] (DARLIN, Camellia-seq; CoSpar for fate inference).
- LARRY-barcoded HSCs used as ground truth for epimutation-based clones: [[scherer-2025-nature]].
- CRISPR recorders: [[mckenna-2016-science]], [[jones-2020-cassiopeia]]; endogenous barcodes: [[ludwig-2019-mtdna-lineage-tracing]], [[chen-2025-methyltree]].
- Trajectory methods context: [[wolf-2019-paga]]; reviews: [[rodriguez-fraticelli-2026-lineage-tracing-review]], [[wang-2026-multimodal-lineage-computational]].

## Open questions

- What is the hidden heritable variable — undersampled mRNA, chromatin, protein, organisation, or niche?
- Do state–fate relationships seen in culture/transplant hold in unperturbed haematopoiesis beyond the monocyte test?
- Why do state and clonal hierarchies diverge in vivo (sampling interval vs environment)?

## Related

- [[lineage-tracing]] · [[40-Topics/single-cell-lineage-tracing]] · [[li-2023-darlin]] · [[hematopoietic-differentiation]]
