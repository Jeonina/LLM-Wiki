---
type: summary
title: "Marks et al. 2023 — Unifying comprehensive genomics and transcriptomics in individual cells (ResolveOME)"
source: "[[00-Sources/papers/Unifying comprehensive genomics and transcriptomics in individual cells to illuminate oncogenic and drug resistance mechanisms]]"
source_kind: paper
author: "Jeffrey R. Marks, Jon S. Zawistowski, ..., Charles Gawad, E. Shelley Hwang, Jay A.A. West (corresponding)"
published: 2023
ingested: 2026-06-26
doi: "10.1101/2022.04.29.489440"
journal: "bioRxiv (preprint)"
tags: [single-cell, PTA, whole-genome, transcriptome, DNA+RNA, drug-resistance, cancer, method]
entities: ["[[20-Entities/charles-gawad]]", "[[20-Entities/jay-a-a-west]]"]
concepts: ["[[30-Concepts/resolveome]]", "[[30-Concepts/pta]]", "[[30-Concepts/scwga]]", "[[30-Concepts/scdna-capabilities-framework]]"]
topics: ["[[40-Topics/single-cell-multiomics]]", "[[40-Topics/scdna-cancer-applications]]"]
---

**Citation:** Marks et al. (2023) — *Unifying comprehensive genomics and transcriptomics in individual cells to illuminate oncogenic and drug resistance mechanisms* — *bioRxiv*. [DOI](https://doi.org/10.1101/2022.04.29.489440)

# Marks 2023 — ResolveOME

> ResolveOME is a single-cell assay that pairs **PTA-based whole-genome amplification** (for accurate, genome-wide SNV/CNV calling) with **full-transcript RNA-seq** from the same cell, so that a cell's complete genotype can be read alongside the transcriptomic readout of its identity and state. It is the DNA-first realization of the "scTrio-seq with a low-error WGA" combination — trading methylation for genome-wide point-mutation fidelity, and commercialized by BioSkryb as the ResolveOME kit.

## Key claims

- Combining PTA (Gonzalez-Pena 2021 chemistry) with full-transcript reverse transcription on the same cell yields accurate complete-genome SNV assessment **plus** a full-length transcriptome — neither modality is sacrificed to capture the other.
- In cultured AML cells resistant to the FLT3 inhibitor **quizartinib**, ResolveOME uncovered a FLT3 missense mutation together with matched transcriptional upregulation of **AXL signal-transduction** and enhancer-factor programs — a same-cell genotype → drug-resistance-expression link.
- In primary breast cancer (DCIS-related), it detected oncogenic **PIK3CA N345K** mutations and heterogeneous classes of chromosomal loss, and crucially could interpret those genotypes using cell identity/state inferred from the same cell's transcriptome.
- The transcriptome supplies the cell-identity context required to make a genome variant interpretable — the genotype alone does not say which cell type carries it or what it does there.

## Methods / evidence

Proof-of-concept method paper (bioRxiv preprint, v2). Benchmarks against G&T-seq and standard scRNA/scWGS references; demonstrates on two cancer systems (an AML drug-resistance model and primary breast cancer cells). Bioinformatics handled by BioSkryb's BaseJumper platform. As a preprint with cell-line and limited-primary-sample demonstrations, throughput, allelic-dropout characteristics at scale, and cost are only partially characterized. Methylation and chromatin are **not** measured — this is a DNA-sequence + RNA assay.

## Surprising or load-bearing bits

- ResolveOME fills the hypothetical the synthesis-gap note flagged — "scTrio-seq with WGA (instead of RRBS) on the nuclear fraction → SNV + RNA at higher cost." It exists, it's productized, and it is genome-wide for point mutations rather than CNV-only.
- Its capability profile is **fidelity (PTA) + co-presence (per cell) + phenotypic association (RNA)** — the same three-of-three that GoT-ChA achieves for chromatin, but here genome-wide for sequence variants rather than at targeted loci.
- The drug-resistance application (FLT3 mutation + AXL upregulation in the same cell) is a clean demonstration of why same-cell genotype+expression beats bulk: resistance mechanism = which mutation co-occurs with which compensatory transcriptional program, per cell.

## Entities mentioned

- [[20-Entities/charles-gawad]] — co-author; single-cell genomics / scWGA expertise (PTA lineage).
- [[20-Entities/jay-a-a-west]] — corresponding author; BioSkryb Genomics (ResolveOME/PTA commercialization).

## Concepts touched

- [[30-Concepts/resolveome]] — defines this method.
- [[30-Concepts/pta]] — the WGA chemistry that gives ResolveOME its genome-wide SNV fidelity.
- [[30-Concepts/scdna-capabilities-framework]] — ResolveOME occupies the fidelity + co-presence + RNA-association cell in the capability table.

## Connections to other sources

- Realizes the "scTrio-seq + WGA" hypothetical named in [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — genome-wide SNV + RNA same-cell, no methylation.
- Complements [[10-Summaries/izzo-2024-got-cha]] (targeted genotype + chromatin) by giving genome-wide genotype + RNA instead.
- Built on the PTA chemistry foundational to [[50-Notes/pta-inflection-point]] and [[10-Summaries/luquette-2025-pta-duplex-mosaicism]].

## Open questions

- No epigenetic layer (no methylation, no chromatin) — interpretation of variants' regulatory consequences still relies on the transcriptome, not direct epigenome measurement.
- Preprint status (2022/2023); peer-reviewed throughput, ADO, and cost characterization at cohort scale remain to be established.
- How does PTA allelic dropout in the genome arm interact with low-input full-transcript RT in the same tube?
