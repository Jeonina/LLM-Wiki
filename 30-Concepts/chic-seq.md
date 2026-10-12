---
type: concept
title: ChIC-seq
aliases: [chromatin immunocleavage]
tags: [histone-modifications, MNase, Schmid]
created: 2026-05-12
updated: 2026-10-12
---

# ChIC-seq

> The original 2004 chromatin immunocleavage method (Schmid et al., Laemmli lab) that uses antibody-tethered MNase to cut at specific chromatin sites. Foundational ancestor of CUT&RUN, CUT&Tag, sortChIC, and scChIC-seq.

> [!abstract] 한눈에
> ChIC-seq는 항체에 MNase를 붙여 표적 chromatin 부위만 자르는 2004년 방법으로, CUT&RUN·CUT&Tag·sortChIC·scChIC-seq로 이어지는 antibody-tethered nuclease 계열의 출발점이다. MNase 기반 scChIC-seq는 Tn5 기반 방법보다 accessibility bias를 덜 받는다 ([[10-Summaries/ludwig-2019-sc-chromatin-modifications-review|Ludwig 2019]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 히스톤 변형](../60-Explainers/histone-modifications.html)
<!-- /explainer-links -->

## Definition

Antibody tethered to MNase (via protein A or covalent linkage) recruits the nuclease to target sites, where local cleavage produces small fragments enriched at the antibody's epitope.

## Why it matters

- First "no-ChIP-needed" chromatin profiling approach.
- Established the antibody-tethered-nuclease paradigm now widespread in CUT&-family methods.
- **Less accessibility bias than Tn5.** A 2019 review notes that MNase-based scChIC-seq is less affected by accessibility bias than Tn5-based methods for H3K27me3 (bulk correlation r = 0.67 vs 0.26–0.31 for ChIL-seq) ([[10-Summaries/ludwig-2019-sc-chromatin-modifications-review|Ludwig 2019]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/cut-and-run|CUT&RUN]] — pA-MNase tethered by antibody, with Ca²⁺-triggered release of cut fragments.
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — pA-Tn5 tagmentation at antibody-bound chromatin.
> - `concept` [[30-Concepts/scchic-seq|scChIC-seq]] — Single-cell antibody-MNase profiling of histone marks.
> - `concept` [[30-Concepts/sortchic|sortChIC]] — pA-MNase profiling with FACS sorting into 384-well plates.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone marks and how they are profiled.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/ludwig-2019-sc-chromatin-modifications-review|Ludwig & Bintu 2019]]
