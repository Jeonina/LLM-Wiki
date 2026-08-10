---
type: summary
title: "Peric-Hupkes et al. 2010 — Molecular maps of the reorganization of genome-nuclear lamina interactions during differentiation"
source: "[[00-Sources/papers/Molecular Maps of the Reorganization of Genome-Nuclear Lamina Interactions during Differentiation]]"
source_kind: paper
author: "Daan Peric-Hupkes, Wouter Meuleman, Ludo Pagie, ... Bas van Steensel (corresponding)"
published: 2010-05-28
ingested: 2026-08-10
doi: "10.1016/j.molcel.2010.03.016"
journal: "Molecular Cell"
tags: [LAD, DamID, nuclear-lamina, differentiation, gene-unlocking, Lamin-B1, ESC-NPC-astrocyte]
entities: ["[[bas-van-steensel]]"]
concepts: ["[[lamina-associated-domains]]", "[[nuclear-lamina]]", "[[damid]]", "[[replication-timing]]", "[[epigenetic-memory]]", "[[chromatin-compartments]]"]
topics: ["[[chromatin-architecture]]", "[[3d-genome]]"]
---

**Citation:** Peric-Hupkes et al. (2010) — *Molecular maps of the reorganization of genome-nuclear lamina interactions during differentiation* — *Molecular Cell* 38, 603–613. [DOI](https://doi.org/10.1016/j.molcel.2010.03.016)

# Peric-Hupkes 2010 — LADs across differentiation

> Lamin B1 DamID maps across an isogenic ESC → neural precursor → astrocyte lineage, plus fibroblasts as an out-group. The result is a two-part picture: a **stable backbone** of ~1,100–1,400 lamina-associated domains covering ~40% of the genome in every cell type, and, on top of it, hundreds of genes that detach or attach at each differentiation step — often as **single transcription units**.

## Key claims

- **DamID method**: a Lamin B1–*E. coli* Dam fusion adenine-methylates sequences contacting the nuclear lamina; free Dam serves as the accessibility-correcting reference. Validated here against published FISH radial positions (loci that shift between ESC and NPC show proportional DamID changes) and by two-colour FISH on the DamID material itself.
- **~1,100–1,400 LADs per cell type, 40 kb to 15 Mb, covering ~40% of the genome** — closely matching the ~1,300 LADs of 80 kb–30 Mb in human fibroblasts.
- The authors flag a conceptual caveat rarely repeated downstream: **binary LAD/inter-LAD classification is an oversimplification**; each locus more accurately has a *probability* of contacting the lamina, reflected in the continuous DamID log ratio.
- **LADs are repressive in all four cell types**: lower gene density, median expression 5–10× lower inside than outside, promoters mostly lacking Pol II and H3K4me2, enriched for late replication and H3K9me2. Yet LADs still contain **13–18% of all genes**.
- Replication timing correlates globally with LAD organization but **does not follow the sharp LAD boundaries**, so near boundaries it is not a reliable predictor of lamina contact.
- **Architecture is largely shared**: genome-wide DamID correlations 0.64 (ESC↔AC) to 0.9 (NPC↔AC); LAD overlap 73–87% between cell types. Because ESCs and NPCs proliferate while astrocytes do not, mitosis does not strongly shape the population-level pattern.
- **Relocation is often gene-sized.** 847 genes lose and 633 gain lamina contact in ESC→NPC; 239 and 390 in NPC→AC. Averaged profiles show the change is confined to the transcription unit with flanking sequence much less affected. 54–82% relocate as **singletons**; the remainder in clusters of two to five genes.
- **Changes are cumulative and lineage-specific**: the ESC→NPC and NPC→AC steps move largely different gene sets, so astrocyte architecture departs further from the ESC "basal state" than NPC does; fibroblasts diverge on a separate branch.
- Relocation tracks identity: *Nanog*, *Klf4* and *Oct4* gain lamina contact in NPCs; 27 GO categories relating to neural physiology lose contact in ESC→NPC; **cell-cycle categories gain** contact in NPC→AC, plausibly contributing to the astrocyte's proliferative arrest.
- **The unlocking result.** About one-third of relocating genes show no expression change — and these are genes silent in both states. Silent genes that *detached* from the lamina in ESC→NPC are significantly **more likely to be activated later** in astrocytes and across ten CNS tissues; silent genes that *attached* are less likely. The effect is weaker but still present across 77 non-neural tissues.
- Unlocking is explicitly **distinct from polymerase poising** — the detached silent genes have no detectable Pol II at their promoters.

## Methods / evidence

Isogenic lineage (NPCs from the same ESC population; astrocytes derived twice independently), each cell type separately transduced to prevent carryover of adenine methylation between stages, marker-confirmed purity (92% Nestin⁺, 92% GFAP⁺), two biological replicates per cell type (r = 0.77–0.92), quantile normalization across cell types, and a gene-level statistical test on continuous DamID signal rather than on binary LAD status.

Stated limitation: ESC DamID had a slightly lower dynamic range, which could mean less robust or more variable lamina interactions in ESCs — or a technical difference in Dam expression or nuclear morphology. The authors decline to choose.

## Surprising or load-bearing bits

- **Unlocking is a chromatin-level record of developmental potential.** A gene can leave the lamina, stay silent, and become activatable one differentiation step later. That is competence written in nuclear position rather than in transcription — the same class of phenomenon as the regulatory priming found in repressive chromatin by [[zhang-2022-sccut-tag-pro|scCUT&Tag-pro]], reached by a completely different assay two decades apart.
- The **"each locus has a contact probability"** framing is the paper's most single-cell-relevant statement, made in 2010 from population data. A 40%-lamina-contact locus in DamID is either 40% of cells or 40% of the time — and DamID, which integrates residence time, cannot separate them. This is the same ambiguity [[jones-2012-dna-methylation-functions|Jones]] identifies for intermediate methylation and [[roadmap-2015-111-epigenomes|Roadmap]] for intermediate-methylation regions.
- **Gene-sized relocation** argues that lamina detachment is not bulk domain movement but can be resolved to individual transcription units — which constrains any mechanistic model to something that acts at gene scale.
- Replication timing decoupling from LAD boundaries is a useful negative: the two domain organizations correlate globally and diverge locally, so one cannot substitute for the other. Consistent with [[dixon-2012-tads|Dixon 2012]]'s finding that TADs are related to but independent of LADs and replication zones.
- The causality question is left genuinely open — the authors propose a **positive feedback loop** where the lamina enhances repression and lack of transcription strengthens lamina contact, which would stabilize cell-type programs without either being the sole cause.
- Stemness genes moving to the lamina in every non-ESC cell type is a concrete mechanism for why reprogramming is inefficient: the pluripotency loci are architecturally locked.

## Entities mentioned

- [[bas-van-steensel]] — corresponding author; DamID and the LAD program originate here.

## Concepts touched

- [[lamina-associated-domains]] — this is the founding differentiation-dynamics source; supplies the size, count and coverage figures.
- [[damid]] — validation logic and the residence-time semantics that make DamID signal a probability rather than a state.
- [[epigenetic-memory]] — locking/unlocking as an architectural memory distinct from mark-based memory.

## Connections to other sources

- Cited by [[dixon-2012-tads]] as one of the domain organizations TADs are compared against; LAD/non-LAD transitions coincide with a subset of TAD boundaries.
- [[van-steensel-2017-lads-review]] is the same lab's later review; [[roadmap-2015-111-epigenomes]] links 2 Mb chromatin-state clusters to lamina association at population scale.
- Single-cell DamID descendants: [[rooijers-2019-scdamt-seq]], [[de-luca-2021-scdamid-protocol]] — the assays that can actually resolve the contact-probability ambiguity this paper names.
- Compartment context from [[lieberman-aiden-2009-hic]]; mitotic reset from [[naumova-2013-mitotic-chromosome]].

## Open questions

- **Cause or consequence?** The authors explicitly allow both directions and propose a feedback loop; no source in this corpus resolves it.
- Whether the lower ESC dynamic range reflects genuinely more variable lamina contact in pluripotent cells — a single-cell DamID question, still open here.
- Whether unlocked genes are unlocked *for* the neural lineage or simply released from an ESC-specific constraint; the 77-tissue analysis gives a partial, not decisive, answer.

## Related

- [[lamina-associated-domains]] · [[damid]] · [[van-steensel-2017-lads-review]] · [[chromatin-architecture]]
