---
type: entity
title: Soumya Raychaudhuri
aliases: [Raychaudhuri lab, Brigham]
entity_kind: person
tags: [immunogenomics, integration, statistical-genetics, Broad]
created: 2026-08-10
updated: 2026-08-10
---

# Soumya Raychaudhuri

> Brigham and Women's Hospital / Broad Institute. Immunogenomics and statistical genetics; the multi-cohort meta-analysis setting that motivated multi-covariate batch correction.

## Mentions

- **2026-08-10** — Corresponding author of [[korsunsky-2019-harmony]] (Harmony), correcting simultaneously over donor and technology and introducing the LISI integration/accuracy metric pair.

## Related

- [[batch-effect]] · [[multimodal-integration-methods]] · [[computational-methods]]

## Added 2026-08-17

Corresponding author of [[10-Summaries/kang-2021-symphony]] (Symphony), built on the same group's [[10-Summaries/korsunsky-2019-harmony]]. Symphony makes **reference atlas mapping** a distinct operation from integration: compress an integrated reference into a portable form and localise query cells within the **frozen** embedding in seconds, rather than re-integrating de novo — which is intractable at atlas scale and corrupts the annotated reference.

Its most striking capability is inferring a modality the query never measured — surface protein predicted by mapping onto a CITE-seq atlas. See [[30-Concepts/reference-atlas-mapping]].
