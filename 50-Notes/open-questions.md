---
type: note
title: Open Questions
description: Tensions and gaps surfaced during ingest or lint. Resolve, then move out.
tags: [meta, open-questions]
created: 2026-05-13
updated: 2026-05-19
---

# Open Questions

Tensions and gaps surfaced during ingest or lint. When a question is resolved, remove it here and update the relevant concept/topic page with the resolution.

## Duplex sequencing

- ~~**Single-cell + duplex**~~ — Resolved 2025: closed from two directions ([[50-Notes/single-cell-duplex-sequencing]]). Remaining sub-questions: Duplex-Multiome generalization beyond brain ([[10-Summaries/kriz-2025-duplex-multiome]]); cross-method single-cell duplex benchmark needed.
- Mutation-rate concordance across duplex platforms (SMaHT benchmark) — does it hold for brain, aging muscle, FFPE samples?
- UDSeq vs the SMaHT-benchmarked methods — no cross-comparison yet.
- **Methylation layer absent from single-cell duplex** — Duplex-Multiome reads accessibility + RNA + mutations but not methylation. Closing this would give all four regulatory layers ([[50-Notes/regulatory-layers-overview]]).

## scDNA-seq methods

- Where does scDAF-seq's per-cell ~99% coverage / ~10-cell throughput win over GoT–ChA's ~38% genotyping / 10⁵-cell throughput? See [[50-Notes/droplet-vs-single-molecule-scdna]] for the full breadth-vs-depth synthesis.
- Throughput vs depth: DLP+ (>10⁴ cells low coverage) vs PTA (384 cells, ~95% coverage). Right operating point per question? ([[50-Notes/droplet-vs-single-molecule-scdna]])
- Why is intra-cell haplotype actuation divergence (~61%) nearly equal to inter-cell divergence (~63%)?

## Mosaicism biology

- Tissue-specific mosaic mutation rates beyond skin/intestine/brain.
- **Smoking × somatic SV** burden mechanism in head-and-neck cancer.
- Causality of cell-type-specific somatic mutation burden in AD.
- IRE1-XBP1 as a therapeutic target in CALR-mutant MPN.
- mtDNA heteroplasmy drop at P6 in mouse — mechanism unclear.

## Methylation / chromatin

- 5mC vs 5hmC functional distinction — most measurements still conflate.
- **Causal vs consequential**: does methylation-loss-driven viral mimicry require additional gating factors (e.g., SETDB1, TF availability)?
- Methylation calling accuracy benchmarking across long-read platforms.
- Single-cell long-read methylation — emerging but not routine.
- Decitabine vs azacitidine: distinct demethylation patterns, mechanistic basis unknown.

## 3D genome

- TAD/loop **causality** — drive expression or follow it?
- Per-cell 3D resolution still ~1 Mb; gap to bulk Hi-C ~kb.
- Sonication-based methods (scSPRITE) capture more contacts; will they generalize?

## Wiki

- Does flat-file + `index.md` navigation scale to ~150 pages?
- Practical contradiction-resolution policy beyond flagging.
- Measuring whether the wiki is actually compounding vs accumulating.

## Related

- [[50-Notes/synthesis-targets]] — promising syntheses that would resolve clusters of these questions
- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — the central conceptual gap this wiki is built around
