---
type: summary
title: "Nam et al. 2019 — Genotyping of Transcriptomes (GoT)"
source: "[[00-Sources/papers/Anna_2019_Nature]]"
source_kind: paper
author: "Anna S. Nam, Kyu-Tae Kim, Ronan Chaligné, Franco Izzo, ... Dan A. Landau (corresponding)"
published: 2019-07-18
ingested: 2026-05-07
doi: "10.1038/s41586-019-1367-0"
journal: "Nature 571, 355–360"
tags: [single-cell, scRNA-seq, genotyping, hematology, MPN, CALR, GoT]
entities:
  - "[[20-Entities/anna-s-nam]]"
  - "[[20-Entities/franco-izzo]]"
  - "[[20-Entities/dan-a-landau]]"
  - "[[20-Entities/landau-lab]]"
concepts:
  - "[[30-Concepts/got]]"
  - "[[30-Concepts/circularization-got]]"
  - "[[30-Concepts/calr-mutation]]"
  - "[[30-Concepts/myeloproliferative-neoplasm]]"
  - "[[30-Concepts/unfolded-protein-response]]"
  - "[[30-Concepts/hematopoietic-differentiation]]"
topics:
  - "[[40-Topics/single-cell-multiomics]]"
  - "[[40-Topics/hematopoietic-malignancies]]"
---

# Nam et al. 2019 — Genotyping of Transcriptomes (GoT)

> Thesis: malignant cells often share surface markers with non-neoplastic cells, so to study how somatic mutations corrupt human hematopoiesis you need to genotype and transcribe the *same* single cells. The authors invent **GoT** — a droplet-based amplicon trick on top of 10x Genomics scRNA-seq — apply it to CALR-mutated MPN, and find that CALR's transcriptional impact (UPR, NF-κB, fitness) depends on the progenitor's *native* identity, not on the mutation alone.

## Key claims

- **GoT links genotype to transcriptome in thousands of single cells.** Modify 10x Genomics: amplify the targeted transcript and locus of interest from the cDNA before short-read sequencing, then use shared cell barcodes to assign genotype to single-cell expression profiles. Genotyping rates ~88% in CD34+ MPN samples vs ~1.4% from default 10x reads.
- **CALR-mutant cells span the entire HSPC differentiation hierarchy** — they do not form distinct transcriptional clusters. scRNA-seq alone cannot distinguish mutant from wild-type.
- **Mutant fitness advantage *grows* with myeloid differentiation.** In essential thrombocythemia (ET), normalized mutant frequency was higher in committed myeloid progenitors and especially MkPs (megakaryocytic progenitors) vs uncommitted HSPCs (P < 10⁻¹⁰, linear mixed model). Validated orthogonally with FACS-sorted ddPCR.
- **The transcriptional readout of CALR mutations depends on cell identity:**
  - **MkPs**: dominant **UPR** activation (HSPA5/BiP, ATF6 chaperone targets, IRE1–XBP1 splicing), increased proliferation correlated with patient platelet counts.
  - **HSPCs**: predominantly **NF-κB pathway** upregulation (CXCL2, NFKBIA) plus anti-apoptosis genes — proposed as a mechanism for HSC self-renewal/outgrowth.
- **Multiplexed GoT** dissects clonal architecture by genotyping multiple loci (CALR, NFE2, SF3B1) simultaneously, recovering the nested clonal evolution structure (concordant with single-cell cloning).
- **Circularization GoT** extends genotyping to mutations distant from transcript ends (e.g. JAK2 V617F at ~2.3 kb from 3′ end). Sequential rounds of intramolecular ligation + inverse PCR shrink the amplicon to short-read-compatible size while preserving the cell barcode. Validated against Oxford Nanopore long-read sequencing.
- **In CALR-mutated myelofibrosis (MF)**: mutant cells already enriched in HSPCs (no further enrichment with differentiation), and MkPs upregulate TGFB1 — proposed mechanism for marrow fibrosis. IRE1-mediated UPR persists into MF.

## Methods / evidence

Empirical method paper plus discovery application. Engineering: a modified 10x v2/v3 chemistry workflow with custom gene-specific primer + P5_generic + RPI-x; species-mixing study (mouse Ba/F3 + human UT7) showed 96.7% concordance. Cohort: 38,290 CD34+ cells from 5 ET patients, 11,093 cells from 4 MF patients, plus a triple-mutant MF case. Statistical claims use linear mixed models, Wilcoxon rank-sum, Fisher's combined test with BH correction, downsampling to 1 genotyping UMI per cell.

The strongest design choice: WT cells from the same patient serve as the comparison set, controlling for genetic background and microenvironment. This is the move that makes the cell-identity-dependent claims clean.

## Surprising or load-bearing bits

- The headline finding isn't "CALR causes UPR" — that was known. It's that **the same mutation produces different transcriptional outputs in different progenitor cell states**, with HSPCs taking the NF-κB route and MkPs taking the UPR route. This reframes "what does this mutation do" as "what does this mutation do *in this cell type*."
- **The wild-type comparison from the same patient sample** is what makes this claim defensible — you cannot do this with bulk sequencing or with cross-patient comparisons.
- **IRE1-XBP1 as a therapeutic target** in CALR-mutant HSPCs is a directly actionable claim that emerged from the cell-identity-dependent analysis; it's only visible because UPR was selectively activated in the mutated stem cell pool.
- The technical limitation that drove circularization GoT — **mutations far from transcript ends fail to amplify** — is also exactly the limitation that motivated [[30-Concepts/got-cha]] five years later (Franco 2024 moved to gDNA precisely to avoid this).

## Entities mentioned

- [[20-Entities/anna-s-nam]] — first author; pathology, Weill Cornell.
- [[20-Entities/franco-izzo]] — co-author here; first author of [[10-Summaries/franco-2024-nature]] (GoT-ChA) five years later.
- [[20-Entities/dan-a-landau]] — corresponding/senior author; group continues this line of work.
- [[20-Entities/landau-lab]] — NYGC/Weill Cornell group behind GoT and GoT-ChA.

## Concepts touched

- [[30-Concepts/got]] — defined here. The droplet-based genotyping-of-transcriptomes platform.
- [[30-Concepts/circularization-got]] — extension introduced in this paper for distal loci.
- [[30-Concepts/calr-mutation]] — driver mutation studied; UPR + NF-κB outputs characterized.
- [[30-Concepts/myeloproliferative-neoplasm]] — disease context (ET, MF).
- [[30-Concepts/unfolded-protein-response]] — central biological finding; cell-identity-dependent UPR branches.
- [[30-Concepts/hematopoietic-differentiation]] — fitness landscape mapped onto progenitor hierarchy.

## Connections to other sources

- **Direct ancestor of** [[10-Summaries/franco-2024-nature]] (GoT-ChA): same lab, same disease focus, but Franco 2024 moves from RNA to chromatin accessibility *and* from cDNA-based to gDNA-based capture, eliminating the expression-level and transcript-distance limitations that motivated circularization GoT here.
- **Conceptually parallel to** [[10-Summaries/elliott-2025-naturebiotechnology]] (DAF-seq): both link DNA sequence variants to chromatin/expression state at single-molecule or single-cell resolution. Different lab, different chemistry, but same overarching question — *how does sequence change shape the regulatory state of an individual cell?*

## Open questions

- The IRE1-XBP1 therapeutic target claim is hypothesis, not validated in patients.
- The HSPC NF-κB signature is shown but the upstream mechanism (which receptor, which ligand) is not nailed down.
- Why doesn't ET-stage CALR drive HSPC fitness, but MF-stage CALR does? The paper notes the difference but doesn't explain the switch.

---
**Source:** [DOI](https://doi.org/10.1038/s41586-019-1367-0)
