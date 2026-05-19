---
type: summary
title: "van Steensel & Belmont 2017 — Lamina-associated domains: links with chromosome architecture, heterochromatin and gene repression"
source: "[[00-Sources/papers/Lamina-associated domains_ links with chromosome architecture, heterochromatin and gene repression]]"
source_kind: paper
author: Bas van Steensel (NKI), Andrew S. Belmont (UIUC)
published: 2017-05-18
ingested: 2026-05-19
doi: "10.1016/j.cell.2017.04.022"
journal: "Cell"
tags: [review, LADs, nuclear-lamina, heterochromatin, DamID, H3K9me2, H3K9me3, structural-axis]
entities: ["[[20-Entities/bas-van-steensel]]", "[[20-Entities/andrew-s-belmont]]", "[[20-Entities/jop-kind]]"]
concepts: ["[[30-Concepts/lamina-associated-domains]]", "[[30-Concepts/damid]]", "[[30-Concepts/chromatin-compartments]]", "[[30-Concepts/histone-modifications]]", "[[30-Concepts/3d-genome]]"]
topics: ["[[40-Topics/3d-genome]]", "[[40-Topics/chromatin-architecture]]"]
---

**Citation:** van Steensel & Belmont (2017) — *Lamina-associated domains: links with chromosome architecture, heterochromatin and gene repression* — *Cell*. [DOI](https://doi.org/10.1016/j.cell.2017.04.022)

# van Steensel 2017 — LADs review

> The canonical review on Lamina-Associated Domains: what they are, how they're mapped, what molecular features define them, and how they fit into the broader heterochromatin / nuclear compartment landscape. Crucially, it articulates LADs as one component of a *competitive* sorting system across three repressive compartments (NL, nucleoli, pericentromeric heterochromatin) that collectively organize the B-compartment.

## Key claims

- **LADs cover >35% of the mammalian genome.** Mouse/human cells have ~1,000–1,500 LADs, sized 10 kb – 10 Mb (median ~0.5 Mb), distributed across all chromosomes.
- **LADs are heterochromatic.** Late-replicating, gene-poor, H3K9me2/H3K9me3-enriched; some boundaries enriched for H3K27me3. **Not** enriched for cytosine methylation — in colorectal cancer, large hypomethylated regions overlap LADs.
- **Two classes: constitutive (cLAD) and facultative (fLAD).** cLADs are cell-type invariant, AT-rich, LINE-rich, gene-poor; positions (not sequences) conserved between mouse and human → likely structural "backbone" for chromosome folding. fLADs are >50% of all LADs, more gene-dense, cell-type-specific; detachment correlates with gene activation during differentiation.
- **Single-cell DamID reveals stochasticity.** Each LAD has a characteristic NL contact frequency. cLADs contact NL in nearly every cell; many fLADs do so in only a subset. ~15% of genome (mostly cLADs with <1 gene/Mb) acts as robust anchors. LAD nuclear position is partially randomized after each mitosis.
- **Anchoring is multivalent and redundant.** No single sequence motif targets LADs to the NL; multiple non-overlapping fragments (4–32 kb each) can independently confer NL targeting. H3K9 methyltransferases (G9a for H3K9me2; SUV39H1/2 for H3K9me3) act redundantly — only triple knockdown peels the HBB LAD region from the NL.
- **NL proteins are also redundant.** Lamins, LBR, and emerin can independently or jointly anchor LADs. Mouse ES cell lamin triple-KO has marginal effect on NL contacts; in post-mitotic LBR+LMNA double-KO cells, heterochromatin coalesces in the nuclear interior.
- **LADs ≈ Compartment B ≈ inactive heterochromatin.** Hi-C compartment B/A maps and NL contact maps are nearly identical at megabase scale. cLADs occupy compartment B; inter-LADs occupy compartment A. The relationship with TADs is less clean — high-level (meta-)TADs match LADs better than low-level TADs.
- **Three competing repressive compartments.** LADs (NL), NADs (nucleolus-associated domains), and pericentromeric heterochromatin partially overlap and compete for the same genomic regions. Disrupting nucleoli shifts loci toward the NL; deleting NL-targeting sequences shifts loci toward pericentric heterochromatin. **The repressive outcome may be invariant** — any heterochromatin compartment is sufficient for silencing.
- **NPCs are NOT LAD-associated.** Nuclear pore complex–interacting loci are excluded from LADs and from LAD borders, despite being at the nuclear periphery — they're a distinct, often active/enhancer-associated subcompartment.
- **Mechanotransduction.** LAD–NL anchors may stiffen the nucleus and serve as entry points for force signaling (LINC complex). Bead-pulling experiments show chromatin stretching within seconds, correlated with increased transcription.

## Methods / evidence

This is a **review** of work primarily from the van Steensel and Belmont groups. The empirical backbone is: bulk DamID (Pickersgill 2006, Guelen 2008), single-cell DamID (Kind 2013, 2015), microscopy with m6A-tracer proteins, tethering experiments, single-LAD deletion/transplant assays, and Hi-C comparisons. Most claims are well-supported by multiple labs; the authors flag specific open mechanistic questions throughout.

## Surprising or load-bearing bits

- **The cLAD/fLAD distinction is not a continuous spectrum** — they have distinct sequence features (cLADs are AT-rich gene deserts), distinct conservation patterns (cLAD *positions* conserved across mouse-human despite divergent *sequences*), and distinct biology (cLADs = structural anchors; fLADs = regulatory toggles).
- **NL contact alone is probably not sufficient for repression.** Tethering experiments give modest effects (2–3× reduction); CEC-4 (C. elegans NL anchor) loss derepresses only one gene whereas H3K9me loss derepresses many. The current best model: NL is a *physical container* for the heterochromatin compartment, but the active repressive machinery is the heterochromatin marks themselves.
- **Tug-of-war mechanism.** LAD borders are 5–10 kb *outside* LADs and enriched for active promoters / CTCF. Active promoters and CTCF loops pull LAD edges toward the nuclear interior; H3K9me-binding proteins pull LAD interiors toward the NL. The final position reflects this balance — and cell-to-cell stochasticity in this balance underlies the variable NL contact frequencies seen in single-cell DamID.
- **For mosaicism interpretation:** a somatic mutation in an fLAD vs cLAD vs inter-LAD has very different consequences. cLAD mutations sit in a stable repressive backbone; fLAD mutations sit in a population-stochastic environment; inter-LAD mutations sit in active compartment A. None of this is visible from sequence alone — requires the structural-axis measurement.

## Entities mentioned

- [[20-Entities/bas-van-steensel]] — first author; NKI; built DamID + scDamID
- [[20-Entities/andrew-s-belmont]] — co-author; UIUC; tethering experiments, microscopy of nuclear architecture
- [[20-Entities/jop-kind]] — pioneered single-cell DamID and m6A-tracer live-cell imaging (Kind 2013, 2015)
- Wendy Bickmore lab — tethering/repression experiments (Reddy 2008, Finlan 2008)
- Susan Gasser lab — C. elegans CEC-4 and H3K9 methylation studies

## Concepts touched

- [[30-Concepts/lamina-associated-domains]] — this is the canonical review; extends the cLAD/fLAD distinction and the three-compartment competition framework
- [[30-Concepts/damid]] — the workhorse technology
- [[30-Concepts/chromatin-compartments]] — LADs ≈ compartment B at megabase scale
- [[30-Concepts/histone-modifications]] — H3K9me2/3 anchor LADs; H3K27me3 at boundaries; redundant methyltransferases
- [[30-Concepts/3d-genome]] — NL anchoring shapes interphase chromosome topology
- [[30-Concepts/chromatin-mechanical-properties]] — LADs may serve mechanotransduction; LINC complex
- [[30-Concepts/chromatin-phase-separation]] — implicit: peripheral heterochromatin behaves as a compartment, even without explicit LLPS language

## Connections to other sources

- **Extends** [[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019 scDam&T-seq]] — Rooijers' single-cell joint DamID + transcriptome refines this review's prediction that fLAD detachment precedes transcription; confirms negative coupling is concentrated in low-CF fLADs, not cLADs.
- **Echoes** [[10-Summaries/de-luca-2021-scdamid-protocol|De Luca 2021]] — the scDamID protocol paper builds on Kind 2013/2015 methodology referenced here.
- **Echoes** [[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]] — lamin depletion increases chromatin conformational heterogeneity, consistent with this review's structural-anchor model.
- **Connects to** [[10-Summaries/qi-zhang-2021-nucleoli-coalescence]] — nucleoli are one of the three competing heterochromatin compartments discussed here.
- **Connects to** [[10-Summaries/gibson-2019-chromatin-llps]] and [[10-Summaries/ahn-2021-llps-cancer-looping]] — LLPS-mediated heterochromatin condensates may be the molecular basis for the NL/nucleolar/pericentric "compartments" framework.
- **Foundational for** [[50-Notes/regulatory-layers-overview]] — provides the structural/physical axis (fifth layer) discussion.
- **Foundational for** [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — relevant because LAD position predicts ~all four molecular regulatory layers simultaneously; a mosaic mutation's LAD status is highly informative.

## Open questions

- How heterogeneous are LADs within themselves? The review predicts multiple anchoring mechanisms even within a single LAD; needs systematic dissection.
- Are NL contacts causal for repression, or just a byproduct of being heterochromatic? Tethering experiments give mixed results; species differs (Drosophila strongly NL-dependent; C. elegans not).
- What is the macromolecular structure of the LAD–NL interaction interface? Currently completely unknown at high resolution.
- Do LADs control DNA replication timing, or merely correlate with it? And do they bias DSB repair pathway choice (HR vs NHEJ)?
- For laminopathies (HGPS, mandibuloacral dysplasia): are tissue-specific phenotypes explained by altered LAD–NL interactions in specific cell types?
- **Not in review, but relevant for mosaicism:** does a somatic point mutation in a cLAD ever become regulatory if it disrupts H3K9me2 deposition?
