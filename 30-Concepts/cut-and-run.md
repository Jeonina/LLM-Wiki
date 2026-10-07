---
type: concept
title: CUT&RUN
aliases: [Cleavage Under Targets and Release Using Nuclease]
tags: [histone-modifications, MNase, Henikoff-lab, low-input]
created: 2026-05-12
updated: 2026-10-07
---

# CUT&RUN

> An antibody-directed chromatin profiling method developed by Skene & Henikoff (2017). Tethers protein-A-MNase to histone-mark-bound chromatin via antibody, then Ca²⁺-triggered MNase digestion releases target fragments into solution for purification and sequencing.

## Definition

CUT&RUN inherits the antibody-MNase tethering principle from Schmid et al.'s ChIC, adds in-situ release of soluble target DNA, and enables lower-input chromatin profiling than ChIP (the founding paper used 600,000–10 million K562 cells and did not test ~100-cell input; [[10-Summaries/skene-2017-cut-and-run]]).

## Why it matters

- Lower input than ChIP-seq.
- Avoids fragmentation/sonication biases.
- Predecessor to CUT&Tag (same principle but Tn5 instead of MNase).

## Added 2026-10-07

**Founding paper details.** CUT&RUN immobilises unfixed nuclei on concanavalin-A beads, tethers pA-MNase via antibody and cleaves at 0 °C so that TF–DNA complexes diffuse into the supernatant; it needed ~1/10th the sequencing depth of ChIP and gave ~20 bp TF footprints in yeast ([[10-Summaries/skene-2017-cut-and-run]]). Low background makes a heterologous *Drosophila* DNA spike-in necessary for quantification ([[10-Summaries/skene-2017-cut-and-run]]). Note: the founding paper used 600,000–10 million K562 cells, so the '~100 cells' input figure on this page is not supported by it ([[10-Summaries/skene-2017-cut-and-run]]).

**CUT&RUN peaks include indirect sites.** Comparing CTCF CUT&RUN (~22,000 sites) with native ChIP (2,298 direct, high-motif sites) and ChIA-PET suggests many CUT&RUN-only peaks are 3D contact partners rather than direct binding sites ([[10-Summaries/skene-2017-cut-and-run]]).


## Related

- [[30-Concepts/cut-and-tag]] · [[30-Concepts/chic-seq]] · [[30-Concepts/scchic-seq]] · [[40-Topics/histone-modifications]] · [[20-Entities/steven-henikoff]]
