---
type: concept
title: Doublet Detection
aliases: [doublets, collisions, multiplets]
tags: [QC, artefacts, single-cell, barcoding]
created: 2026-08-10
updated: 2026-08-10
---

# Doublet Detection

> Two cells sharing one barcode produce a chimeric profile that clustering will place somewhere plausible and wrong. Every single-cell platform generates them; the rate and the detectability differ by platform.

## Rates and mechanisms

- **Combinatorial indexing** produces collisions at the birthday-problem rate given nuclei per well: 4.53%/4.40% measured by species mixing in sciHi-C ([[ramani-2017-scihi-c]]), 3% in sci-RNA-seq3 ([[cao-2019-moca]]).
- **Within-species collisions are invisible** to species-mixing controls and are expected at a similar rate ([[ramani-2017-scihi-c]]).
- Computational detection: Scrublet found 4.3% likely doublets, implying ~10.3% including within-cluster doublets ([[cao-2019-moca]]).
- **Two distinct levels** in lineage tracing — intra-doublets from a cell's own molecules, and inter-doublets between clones — are handled separately ([[jones-2020-cassiopeia]]).
- **Physical prevention**: on-chip imaging distinguishes single cells from doublets and debris before library construction ([[zahn-2017-dlp]]).

## Downstream consequences

- Whole clusters can be doublet artefacts: one 40-cluster analysis discarded a cluster with a 52% detected doublet rate, and 13% of 655 subclusters were annotated as artefacts under a >10% predicted-doublet rule ([[cao-2019-moca]]). Subtype counts from atlases without such a rule should be read as upper bounds (synthesis).
- In lineage tracing a doublet's chimeric character vector is placed on the tree, producing a false relationship rather than an obvious outlier ([[jones-2020-cassiopeia]]).

## Related

- [[quality-control-metrics]] · [[combinatorial-indexing]] · [[cell-type-annotation]] · [[computational-methods]]
