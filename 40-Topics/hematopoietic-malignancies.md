---
type: topic
title: Hematopoietic malignancies
aliases: [blood cancers, myeloid malignancies]
tags: [hematology, cancer, clonal-evolution]
created: 2026-05-07
updated: 2026-08-10
---

# Hematopoietic malignancies

> Cancers and pre-cancerous clonal expansions arising from hematopoietic stem and progenitor cells. The wiki's current focus is on [[30-Concepts/myeloproliferative-neoplasm|myeloproliferative neoplasms]] (MPN) — a tractable model for studying how single somatic mutations corrupt normal hematopoiesis.

The two single-cell methods papers in the vault both use MPN as their proving ground, for the same reason: bulk and uncoupled single-cell assays cannot resolve mutated vs wild-type cells in the same patient because they share surface markers, and MPNs offer recurrent, well-characterized drivers in clinically obtainable CD34⁺ samples.

## Core concepts

- [[30-Concepts/myeloproliferative-neoplasm]] — the disease class (ET, PV, MF) and its driver landscape.
- [[40-Topics/clonal-hematopoiesis]] — mosaic HSC clonal expansions; precursor state to MPN/MDS/AML.
- [[30-Concepts/calr-mutation]] — driver in ~25–30% of MPN; chaperone disruption → UPR; cell-identity-dependent transcriptional output.
- [[30-Concepts/jak2-v617f]] — most common MPN driver; constitutive JAK-STAT activation; cell-intrinsic chromatin priming visible at clonal hematopoiesis.
- [[30-Concepts/unfolded-protein-response]] — load-bearing biological output of CALR mutation, with branch deployment depending on cell type.
- [[30-Concepts/hematopoietic-differentiation]] — the native scaffold against which mutated clones are mapped.

## Key entities

- [[20-Entities/anna-s-nam]] — first author of the GoT paper; pathologist-scientist at Weill Cornell.
- [[20-Entities/franco-izzo]] — first author of GoT–ChA; postdoc-to-PI trajectory in the Landau lab.
- [[20-Entities/dan-a-landau]] — senior author of both GoT and GoT–ChA; clonal-evolution methods PI.
- [[20-Entities/landau-lab]] — group hub for the GoT family of methods applied to hematopoietic malignancies.

## Sources, by sub-theme

### CALR-mutated MPN — transcriptomic dissection

- [[10-Summaries/nam-2019-got]] — GoT in CALR-mutated ET and MF; UPR / NF-κB cell-identity-dependent outputs.

### JAK2V617F MPN — chromatin dissection

- [[10-Summaries/izzo-2024-got-cha]] — GoT–ChA in JAK2V617F MF, PV→MF, and clonal hematopoiesis; cell-intrinsic pro-inflammatory chromatin priming.

## Synthesized notes

_None yet._

## Open questions

- Why is CALR-mutant fitness advantage **differentiation-dependent in ET** but **already strong in HSPCs in MF**? ([[10-Summaries/nam-2019-got]] observes the difference but does not explain the switch.)
- Is the cell-intrinsic NF-κB chromatin program in JAK2V617F HSCs ([[10-Summaries/izzo-2024-got-cha]]) **causal** for clonal expansion, or downstream of it?
- Does the IRE1-XBP1 therapeutic hypothesis from [[10-Summaries/nam-2019-got]] hold up in MPN clinical trials? Wiki has no source on this yet.
- Ruxolitinib reverses the chromatin TF-motif phenotype but not the clone ([[10-Summaries/izzo-2024-got-cha]]). Does combination therapy targeting the cell-intrinsic chromatin program (e.g. NF-κB or BET inhibitors) eliminate the clone in vivo?
- Other hematopoietic malignancies (AML, CLL, MDS) are not yet represented in the vault — the [[20-Entities/landau-lab]] history references CLL clonal-evolution work that would extend this topic substantially.

## Related

- [[40-Topics/clonal-hematopoiesis]] · [[40-Topics/cancer-clonal-evolution]] · [[30-Concepts/intratumor-heterogeneity]] · [[30-Concepts/chromosomal-instability]]

## Added 2026-08-13

[[10-Summaries/gawad-2014-all-clonal-origins]] adds the childhood ALL clonal-architecture baseline: 1,479 single cells from six patients, **codominant clones in five of six**, structural variants acquired before point mutations, an APOBEC-like TC-motif cytosine bias, subclonal and late *KRAS*, and clones arrested at different B-cell developmental stages within the same patient.
