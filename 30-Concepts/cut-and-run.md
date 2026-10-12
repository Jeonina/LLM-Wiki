---
type: concept
title: CUT&RUN
aliases: [Cleavage Under Targets and Release Using Nuclease]
tags: [histone-modifications, MNase, Henikoff-lab, low-input]
created: 2026-05-12
updated: 2026-10-12
---

# CUT&RUN

> An antibody-directed chromatin profiling method developed by Skene & Henikoff (2017). Tethers protein-A-MNase to histone-mark-bound chromatin via antibody, then Ca²⁺-triggered MNase digestion releases target fragments into solution for purification and sequencing ([[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]).

> [!abstract] 한눈에
> CUT&RUN은 항체로 pA-MNase를 표적 chromatin에 붙인 뒤 잘라낸 조각만 용액으로 흘려 보내 읽는 방법으로, ChIP보다 sequencing depth가 약 1/10이면 되고 background가 낮다 ([[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]). 다만 원 논문은 600,000–1,000만 개 K562 세포를 썼고, peak 상당수는 직접 결합이 아니라 3D contact 상대일 수 있다 ([[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 히스톤 변형](../60-Explainers/histone-modifications.html)
<!-- /explainer-links -->

## Definition

CUT&RUN inherits the antibody-MNase tethering principle from Schmid et al.'s ChIC ([[30-Concepts/chic-seq|ChIC-seq]]), adds in-situ release of soluble target DNA, and enables lower-input chromatin profiling than ChIP (the founding paper used 600,000–10 million K562 cells and did not test ~100-cell input; [[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]).

**Protocol.** CUT&RUN immobilises unfixed nuclei on concanavalin-A beads, tethers pA-MNase via antibody and cleaves at 0 °C so that TF–DNA complexes diffuse into the supernatant ([[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]). Low background makes a heterologous *Drosophila* DNA spike-in necessary for quantification ([[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]).

## Why it matters

- Lower input than ChIP-seq ([[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]).
- Avoids fragmentation/sonication biases.
- Predecessor to [[30-Concepts/cut-and-tag|CUT&Tag]] (same principle but Tn5 instead of MNase).

## Evidence and examples

- CUT&RUN needed ~1/10th the sequencing depth of ChIP and gave ~20 bp TF footprints in yeast ([[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]).
- Comparing CTCF CUT&RUN (~22,000 sites) with native ChIP (2,298 direct, high-motif sites) and ChIA-PET suggests many CUT&RUN-only peaks are 3D contact partners rather than direct binding sites ([[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]).

## Contested points

- **Input size.** The founding paper used 600,000–10 million K562 cells, so a '~100 cells' input figure previously on this page is not supported by it ([[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]).
- **CUT&RUN peaks include indirect sites**, so peak counts overstate direct binding (see Evidence above) ([[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — Same antibody-tethering principle with Tn5 instead of MNase.
> - `concept` [[30-Concepts/chic-seq|ChIC-seq]] — The antibody-MNase tethering method CUT&RUN builds on.
> - `concept` [[30-Concepts/scchic-seq|scChIC-seq]] — Single-cell antibody-tethered MNase profiling.
> - `entity` [[20-Entities/steven-henikoff|Steven Henikoff]] — Co-developer of CUT&RUN (Skene & Henikoff 2017).
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone marks and the methods that profile them in single cells.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]
