---
type: summary
title: "de Luca & Kind 2021 — Single-cell DamID protocol for nuclear-lamina contacts in mammalian cells"
source: "[[00-Sources/papers/Single-Cell DamID to Capture Contacts Between DNA and the Nuclear Lamina in Individual Mammalian Cells]]"
source_kind: paper
author: "Kim L. de Luca, Jop Kind"
published: 2021
ingested: 2026-05-15
doi: "10.1007/978-1-0716-0664-3_9"
journal: "Methods in Molecular Biology vol. 2157"
tags: [protocol, single-cell, DamID, scDamID, lamina, LAD, nuclear-periphery, methods]
entities:
  - "[[20-Entities/jop-kind]]"
  - "[[20-Entities/kim-de-luca]]"
concepts:
  - "[[30-Concepts/damid]]"
  - "[[30-Concepts/lamina-associated-domains]]"
  - "[[30-Concepts/nuclear-lamina]]"
topics:
  - "[[40-Topics/3d-genome]]"
  - "[[40-Topics/chromatin-architecture]]"
---

# de Luca & Kind 2021 — scDamID protocol (MMB 2157)

> Thesis: this is the canonical step-by-step **bench protocol** for performing single-cell DamID (Dam-LMNB1 ↔ nuclear-lamina contacts + untethered-Dam accessibility control) in mammalian cells. Where Kind 2013/2015 established the chemistry and Rooijers 2019 added multi-omic + linear-amplification, this chapter documents the workflow as a community-facing recipe — plasmids, induction systems, FACS strategy, MboI-qPCR clone screen, DpnI/adapter ligation/PCR cycle counts, and pooling for Illumina libraries.

## Key claims

- **scDamID requires clonal Dam-LMNB1 + untethered-Dam cell lines** with controllable expression (ProteoTuner Shield1 stabilization or auxin-inducible degron). Background methylation noise scales with constitutive expression — clone selection is mandatory, not optional. Plasmid backbones: pPTuner IRES2 (transfection) or pCCL.sin.cPPT.hPGK lentiviral.
- **MboI-qPCR is the gating QC**. MboI cuts only *unmethylated* GATC, so percentage methylation = 1/2^(Ct_digested − Ct_undigested) × 100%. Acceptance: Dam-LMNB1 clones with LAD methylation >40% and LAD/iLAD ratio >3; Dam-only controls with LAD <20% and ratio <1. Out of ~200 seeded clones, 10–60% pass.
- **Throughput scaffold**: FACS-sort single cells into 96-well plates with 3 μL lysis buffer (Tris/Mg/K-acetate + Tween/IGEPAL + Proteinase K fresh). All subsequent steps are additive — no purification between digest, ligation, PCR — minimizing material loss.
- **PCR uses cell-specific barcoded primers** hybridizing to a universal T7-promoter-containing adapter. Multiplex hundreds of cells into one Illumina library. Recommended depth: ~500K raw reads per single-cell sample for Dam-LMNB1 in mammals.
- **Cell-cycle gating matters**: Dam methylation accumulates in G1/G2; DNA replication erases hemimethylated marks. Collect cells at G1/S or G2/M transitions via Hoechst staining or FUCCI reporter.

## Methods / evidence

- **Chemistry chain**: cells → Proteinase-K lysis (42°C 4h, 80°C 20min inactivate) → DpnI digest of m6A-GATC (37°C 8h) → T4 ligation of double-stranded adapter (16°C 12–16h) → PCR with cell-specific barcoded primer; 20-cycle starter, titrate by gel.
- **Adapter**: T7-promoter-containing fork structure; bottom strand 5'-TCCTCGGCCGCG-3' with 5' phosphate; top strand carries T7+Illumina+barcode+CA. Annealed slow-cool from 94°C.
- **No MboI digest in scDamID** (unlike bulk DamID) — single-cell input is too low; relying on adapter-primer specificity for methylated-fragment enrichment.
- **Comparator coverage**: ChIP-seq, ATAC-seq, 3C/4C/5C/Hi-C, ChIA-PET all discussed; scDamID is positioned as the easy-implementation, single-cell, high-coverage (~10 kb resolution) entry into nuclear-organization assays.

## Surprising or load-bearing bits

- The **methylation cumulativity** of DamID is *the* feature that enables single-cell readout — unlike ChIP, which captures an instantaneous crosslink, DamID integrates contact history over hours. Tunable via induction window (typically 12 h).
- **Survival of FACS-cloned cells: 5–90%** depending on cell line. Practical reality often missed in methods papers — the cell-line-establishment step can take longer than the actual single-cell experiment.
- **No clean-up between reactions** (lysis → DpnI → ligation → PCR all in one well) is the throughput trick. Total reaction volume scales additively (~3 → 10 → 20 → 50 μL); cross-well contamination is the only failure mode worth obsessing over.
- The protocol is **explicitly designed for `Dam-POI` extensibility** — anything that can be fused to Dam (LMNB1, RING1B, PRC2, TFs, etc.) becomes a single-cell mapping target. This is what positions scDamID as a *platform*, not just a lamina assay.

## Entities mentioned

- [[20-Entities/jop-kind]] — co-author; Hubrecht; scDamID developer.
- [[20-Entities/kim-de-luca]] — first author; Hubrecht.
- Bas van Steensel — DamID inventor (van Steensel 2000) — ancestral.

## Concepts touched

- [[30-Concepts/damid]] — protocol-level definition for single-cell adaptation.
- [[30-Concepts/lamina-associated-domains]] — defines the assay's primary biological target.
- [[30-Concepts/nuclear-lamina]] — operationalizes its definition as the LMNB1-tethered Dam contact surface.

## Connections to other sources

- **Companion to** [[10-Summaries/rooijers-2019-scdamt-seq]] — same lab; scDam&T-seq is the multi-omic descendant of this protocol.
- **Ancestor**: Kind 2013 (Cell 153) introduced bulk DamID-on-chip single-cell adaptation; Kind 2015 (Cell 163) established single-cell DamID with FACS+PCR; this 2021 chapter is the consolidated bench recipe.
- **Used as reference data by** [[10-Summaries/mali-2025-conformational-heterogeneity]] — lamina-DamID contact probability vector feeds 3D chromatin polymer models.

## Open questions

- Throughput ceiling: even with 384-well robotics, scDamID tops out at hundreds-to-thousands of cells per run. Combinatorial-indexing adaptations (cf. sciATAC) are an obvious extension that the chapter does not address.
- Methylation cumulativity time window: 12-h induction is convenient but blurs short-lived contacts. Inducible-degron variants offer finer time resolution but require additional clone engineering.
- Cross-species portability: documented for KBM7 (human) and mESCs (mouse) — performance in primary tissue, organoids, or other non-cycling cells (neurons, hepatocytes) is unaddressed.

---
**Source:** [DOI](https://doi.org/10.1007/978-1-0716-0664-3_9) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32820403/)

## Related

- [[30-Concepts/damid]] · [[30-Concepts/lamina-associated-domains]] · [[30-Concepts/nuclear-lamina]]
- [[10-Summaries/rooijers-2019-scdamt-seq]] — multi-omic extension
- [[10-Summaries/mali-2025-conformational-heterogeneity]] — downstream use of lamina-DamID as 3D-model constraint
- [[40-Topics/3d-genome]] · [[40-Topics/chromatin-architecture]]
