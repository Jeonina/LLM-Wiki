---
type: entity
title: Zhana Duren
aliases: [Duren lab, Clemson, LINGER, ISON]
entity_kind: person
tags: [gene-regulatory-network, multi-omics-integration, spatial-omics, Clemson]
created: 2026-08-13
updated: 2026-08-13
---

# Zhana Duren

> Clemson University. Gene regulatory network inference from single-cell multi-omic data (LINGER), extended to spatial contexts.

## Mentions

- **2026-08-13** — Corresponding author of [[debnath-2026-ison]] (ISON), which infers **spatial chromatin accessibility** by learning a shared embedding from spatial transcriptomics plus single-cell multiome, then decoding spatial RNA through the multiome's ATAC decoder — a computational substitute for spatial multiome kits that do not commercially exist.
- The paper's boldest claim is that the *inferred* accessibility recovers regulatory signal **better than the directly measured** spatial ATAC, supported by two external references: *cis*-eQTL AUPR 6% above random for predicted vs at-random for experimental, and Hi-C AUPR 15% vs 10% ([[debnath-2026-ison]]).
- A useful counterexample to the field's default: the **linear KL-NMF model consistently beat the contrastive VAE** across both datasets and both metrics ([[debnath-2026-ison]]). (synthesis)

## Related

- [[spatial-multiomics]] · [[multimodal-integration-methods]] · [[gene-regulatory-network]] · [[40-Topics/single-cell-multiomics]]

## Added 2026-08-17

Corresponding author of [[10-Summaries/yuan-2024-linger]] (LINGER), the GRN method that ISON later builds on. LINGER treats GRN inference as a data problem — most single cells are not independent, so the effective sample size is far below the cell count — and imports atlas-scale external **bulk** data by lifelong learning, with motif priors injected via manifold regularisation. Reported fourfold to sevenfold relative accuracy increase over a field the paper describes as previously "only marginally better than random prediction".
