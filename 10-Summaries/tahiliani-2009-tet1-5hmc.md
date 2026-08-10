---
type: summary
title: "Tahiliani et al. 2009 — Conversion of 5-methylcytosine to 5-hydroxymethylcytosine in mammalian DNA by MLL partner TET1"
source: "[[00-Sources/papers/Conversion of 5-Methylcytosine to 5-Hydroxymethylcytosine in Mammalian DNA by MLL Partner TET1]]"
source_kind: paper
author: "Mamta Tahiliani, Kian Peng Koh, Yinghua Shen, William A. Pastor, Hozefa Bandukwala, Yevgeny Brudno, Suneet Agarwal, Lakshminarayan M. Iyer, David R. Liu, L. Aravind, Anjana Rao (corresponding)"
published: 2009-04-17
ingested: 2026-08-10
doi: "10.1126/science.1170116"
journal: "Science"
tags: [5hmC, TET1, DNA-methylation, demethylation, founding-paper, oxidative-modification, embryonic-stem-cells]
entities: []
concepts: ["[[5hmc]]", "[[tet-enzymes]]", "[[dnmt]]"]
topics: ["[[dna-methylation]]"]
---

**Citation:** Tahiliani et al. (2009) — *Conversion of 5-methylcytosine to 5-hydroxymethylcytosine in mammalian DNA by MLL partner TET1* — *Science* 324, 930–935. [DOI](https://doi.org/10.1126/science.1170116)

# Tahiliani 2009 — TET1 makes 5hmC

> A computational homology search for mammalian relatives of the trypanosome base-J enzymes JBP1/JBP2 identified the TET family; TET1 is a 2-oxoglutarate- and Fe(II)-dependent dioxygenase that oxidizes 5-methylcytosine to 5-hydroxymethylcytosine, both in vitro and in cells — establishing 5hmC as an enzymatically generated mammalian DNA base and opening the active-demethylation field.

## Key claims

- TET1/2/3 are mammalian homologs of JBP1/JBP2, sharing the double-stranded β-helix (DSBH) fold of 2OG-Fe(II) oxygenases; TET1 and TET3 additionally carry a CXXC zinc-binding domain that in other proteins discriminates methylated from unmethylated DNA.
- TET1 overexpression in HEK293 cells reduces 5mC antibody staining and produces a novel labeled nucleotide on TLC; the catalytically dead H1671Y/D1673A mutant does not — the effect is enzymatic, not binding.
- High-resolution MS and MS/MS identify the novel species as hm-dCMP (m/z 336.0582, C₁₀H₁₅NO₈P⁻), matching authentic hm-dCMP from unglucosylated T4 phage DNA.
- Recombinant TET1 catalytic domain converts 5mC→5hmC on fully and hemimethylated duplex oligos, with absolute dependence on Fe(II) and 2OG; it does not convert thymine to hmU, i.e. it is 5mC-specific.
- 5hmC is a physiological constituent of mouse ES cell DNA: 4–6% of cytosine species at MspI sites (vs 55–60% 5mC), ~1 base in 3,000 genome-wide (~2 × 10⁶ per haploid genome). It is not detected in activated human T cells or mouse dendritic cells.
- 5hmC levels track TET1: LIF withdrawal drops *Tet1* mRNA ~80% and 5hmC ~40%; RNAi knockdown gives ~87% mRNA loss and ~40% 5hmC loss (residual attributed to TET2/TET3).

## Methods / evidence

Iterative sequence-profile searching plus secondary-structure prediction for the family assignment; immunofluorescence, thin-layer chromatography of end-labeled MspI/HpaII/TaqαI fragments, LC-ESI-MS and MS/MS for chemical identification; recombinant Sf9-expressed TET1-CD for in vitro catalysis; RNAi and differentiation time courses for physiological relevance. The wild-type-vs-catalytic-mutant contrast is the load-bearing control and it is applied consistently across every assay. Weight is high for "TET1 makes 5hmC"; the genomic *distribution* of 5hmC is explicitly left open.

## Surprising or load-bearing bits

- The discovery route was comparative genomics on a trypanosome DNA modification, not a mammalian methylation screen — a reminder that the 5hmC field arrived sideways.
- The authors already lay out the three mechanistic possibilities that framed the next decade: 5hmC as a stable mark excluding MBPs, 5hmC as a passive-demethylation route (DNMT1 reads it poorly), and 5hmC as an active-demethylation intermediate.
- The methods caveat that matters for [[bisulfite-sequencing]]: they state plainly that distinguishing 5hmC from 5mC from C "will require the development of tools" — the exact problem [[chen-2025-sctaps-sccaps-plus|scTAPS/scCAPS+]] and long-read basecalling later attack.
- *TET1* was already known as an MLL fusion partner in AML and *TET2* as deleted in myeloproliferative disorders — the cancer link was present at the founding, not retrofitted.

## Entities mentioned

- Anjana Rao lab (Harvard/Immune Disease Institute) — corresponding author group; Aravind & Iyer (NCBI) supplied the comparative-genomics identification.
- Kriaucionis & Heintz — companion Science paper reporting 5hmC in Purkinje neurons; the two papers established 5hmC jointly.

## Concepts touched

- [[5hmc]] — this is the founding paper for the mark's enzymatic origin; supplies the ES-cell abundance figure (4–6% of CpG cytosines at MspI sites).
- [[tet-enzymes]] — defines the family, the 2OG/Fe(II) requirement, and the domain architecture (CXXC + Cys-rich + DSBH).
- [[dnmt]] — poor DNMT1 recognition of hemi-hydroxymethylated CpG is the proposed passive-demethylation mechanism.
- [[epigenetic-memory]] — 5hmC is offered as the escape hatch from otherwise-heritable 5mC.

## Connections to other sources

- Upstream of [[chen-2025-sctaps-sccaps-plus]], which finally separates 5mC from 5hmC at single-cell resolution — the tool Tahiliani asked for.
- Context for [[kim-2017-methylation-memory-review]] and [[schubeler-2015-methylation-review]], both of which treat oxidized cytosines as a standard layer.
- The bisulfite blind spot it exposes is the reason [[smallwood-2014-natmethods|scBS-seq]]-family methods report "5mC+5hmC" rather than 5mC.

## Open questions

- Genomic localization of 5hmC was unresolved here; whether 5hmC is a stable mark or purely an intermediate remains contested in the corpus.
- Single-cell 5hmC remains sparse relative to 5mC: does the 4–6% bulk figure hold cell-to-cell, or is it dominated by a subpopulation? Not addressed by any source currently in this wiki.

## Related

- [[5hmc]] · [[tet-enzymes]] · [[dna-methylation]] · [[chen-2025-sctaps-sccaps-plus]]
