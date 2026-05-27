---
type: summary
title: "Doughty et al. 2024 — Single-molecule chromatin configurations link TF binding to expression in human cells (bioRxiv preprint)"
source: "[[00-Sources/papers/Single-molecule chromatin configurations link transcription factor binding to expression in human cells]]"
source_kind: paper
author: Benjamin R. Doughty, Michaela M. Hinks, Julia M. Schaepe, ..., Lacramioara Bintu, William J. Greenleaf (co-corresponding)
published: 2024-02-04
ingested: 2026-05-27
doi: "10.1101/2024.02.02.578660"
journal: "bioRxiv preprint"
tags: [single-molecule-footprinting, transcription-factors, chromatin, preprint, abstract-only-ingest, greenleaf-lab]
entities: ["[[20-Entities/william-greenleaf]]"]
concepts: ["[[30-Concepts/single-molecule-footprinting]]", "[[30-Concepts/fiber-seq]]", "[[30-Concepts/samosa]]"]
topics: ["[[40-Topics/chromatin-architecture]]"]
---

**Citation:** Doughty et al. (2024) — *Single-molecule chromatin configurations link transcription factor binding to expression in human cells* — bioRxiv 2024.02.02.578660. [DOI](https://doi.org/10.1101/2024.02.02.578660)

# Doughty 2024 — single-molecule TF→expression linkage (abstract-only ingest)

> **Abstract-only ingest** — the source clipping captured only references (the bioRxiv preprint full text was not extracted into the clipping; only the citation list is present). Recorded here for discoverability and graph wiring; full reading deferred until a complete PDF/HTML copy is added to `00-Sources/`.

## What this paper is (from title + cited literature pattern)

A Greenleaf / Bintu collaboration applying **single-molecule footprinting** (the same methodological family as Fiber-seq, SAMOSA, DiMeLo-seq) to directly observe coordinated TF binding configurations and link them to gene expression in human cells. References include the canonical Stergachis Fiber-seq paper (Ref 14), Shipony 2020 (long-read SMF, Ref 13), Krebs 2017 (single-molecule footprinting at paused promoters, Ref 12), Sönmezer 2021 (molecular co-occupancy, Ref 15) — placing this firmly in the single-molecule chromatin lineage that the wiki covers via [[30-Concepts/fiber-seq]], [[30-Concepts/daf-seq]], [[30-Concepts/samosa]], and [[30-Concepts/single-molecule-footprinting]].

## Why it's load-bearing for this wiki

The wiki's central thesis around single-molecule chromatin (see [[50-Notes/droplet-vs-single-molecule-scdna]]) treats single-molecule footprinting as the technology that resolves *which TFs are co-bound on the same DNA fiber*, vs bulk ChIP-seq's averaging. Doughty 2024 likely closes the loop by directly correlating per-fiber TF configurations with gene expression in a multi-modal assay. If full-text confirms this, this is a key reference for the per-fiber-to-expression linkage that GoT-ChA / SHARE-seq do at single-cell resolution and that Fiber-seq does at single-molecule resolution.

## Authors of note

- **William J. Greenleaf** (Stanford, [[20-Entities/william-greenleaf]]) — co-corresponding; ATAC-seq inventor, single-molecule chromatin pioneer
- **Lacramioara Bintu** (Stanford) — co-corresponding; quantitative gene regulation
- Andrew B. Stergachis is *not* on the author list — different group than the Fiber-seq / DAF-seq lineage; this is a parallel Stanford-side development of single-molecule chromatin.

## Status

**FOLLOW-UP NEEDED.** The current source clipping is references-only. To complete this ingest:
1. Add full HTML or PDF of the preprint to `00-Sources/papers/`.
2. Re-read; replace this stub with a proper Key-claims / Methods / Surprising-bits summary.
3. Update touch points: [[30-Concepts/single-molecule-footprinting]], [[50-Notes/droplet-vs-single-molecule-scdna]] (if the per-fiber-to-expression linkage materializes as claimed), and [[40-Topics/chromatin-architecture]].

## Related

- [[30-Concepts/single-molecule-footprinting]] · [[30-Concepts/fiber-seq]] · [[30-Concepts/daf-seq]] · [[30-Concepts/samosa]]
- [[40-Topics/chromatin-architecture]]
- [[50-Notes/droplet-vs-single-molecule-scdna]]
- [[10-Summaries/andrewb-2020-science]] — Stergachis 2020 Fiber-seq, the methodological predecessor
- [[10-Summaries/altemose-2022-dimelo-seq]] — protein-target SMF variant
- [[10-Summaries/abdulhay-2020-samosa]] — Henikoff-lab SMF variant
