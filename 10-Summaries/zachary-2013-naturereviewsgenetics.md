---
type: summary
title: "Smith & Meissner 2013 — DNA methylation: roles in mammalian development"
source: "[[00-Sources/papers/Zachary_2013_NatureReviewsGenetics]]"
source_kind: paper
author: "Zachary D. Smith, Alexander Meissner"
published: 2013-03
ingested: 2026-05-11
doi: "10.1038/nrg3354"
journal: "Nature Reviews Genetics 14:204–220"
tags: [review, DNA-methylation, development, ESC, CpG-islands, DNMT, TET]
entities:
  - "[[20-Entities/alexander-meissner]]"
concepts:
  - "[[30-Concepts/dna-methylation]]"
  - "[[30-Concepts/cpg-island]]"
  - "[[30-Concepts/dnmt]]"
  - "[[30-Concepts/tet-enzymes]]"
topics:
  - "[[40-Topics/dna-methylation]]"
---

**Citation:** Smith et al. (2013) — *DNA methylation: roles in mammalian development* — *Nature Reviews Genetics*. [DOI](https://doi.org/10.1038/nrg3354)

# Smith & Meissner 2013 — DNA methylation: roles in mammalian development

> Thesis: DNA methylation (5-methylcytosine, primarily at symmetric CpG dinucleotides) is mostly stable throughout life, propagated by DNMT1 at S phase, but it is dynamically erased and reset during two developmental windows — primordial germ cell specification and pre-implantation development — and serves as both a localized regulatory signal and a genome-wide silencing mechanism for repetitive elements and imprints.

## Key claims

- **Global methylation landscape**: 60–80% of the ~28 million CpGs in the human genome are methylated. <10% of CpGs occur in CpG islands, most of which are at TSSs of housekeeping/developmental genes and are constitutively *unmethylated*.
- **DNMT enzymes**: DNMT1 maintains symmetric methylation through S phase by recognizing hemimethylated substrates (via UHRF1); DNMT3A/3B perform de novo methylation. Loss of any is embryonic-lethal.
- **TET enzymes** (TET1/2/3) oxidize 5mC to 5hmC, an intermediate for full demethylation; TET1 binds CpG island promoters and may function as a general "epigenetic proofreader."
- **Targets of methylation regulation**:
  - Promoter CpG islands (mostly unmethylated, actively excluded from methylation by H3K4 methyltransferases and TF binding).
  - Repetitive elements / transposons (mostly methylated to silence them).
  - Imprinted loci (parent-of-origin-specific methylation marks established in PGCs).
- **Two developmental windows of global demethylation**:
  - **Pre-implantation embryo**: paternal genome rapidly demethylated at fertilization; both genomes globally depleted over early embryonic progression.
  - **PGC specification**: near-complete erasure to enable re-establishment of imprints.
- **Hematopoiesis** highlighted as a lineage where methylation contributes to differentiation decisions through both global modulation and locus-specific changes.

## Methods / evidence

Synthesizing review across mouse and human studies, with extensive ESC focus. Meissner lab (Harvard) is a major methylation-mapping group.

## Surprising or load-bearing bits

- **DNMT1 fidelity is structurally dependent on hemimethylated substrate** — it cannot methylate fully unmethylated DNA on its own, which prevents spurious genome-wide methylation gains. UHRF1 enforces the targeting.
- **CpG islands hypermethylate during tumorigenesis** — a key cancer-epigenetics observation that motivates therapeutic strategies (DNMT inhibitors) and biomarkers.
- **TET-mediated demethylation pathway** is the breakthrough that explains how locus-specific demethylation can be actively achieved (rather than passively via replication without DNMT1).

## Entities mentioned

- [[20-Entities/alexander-meissner]] — senior author; Harvard; major methylation methods PI.

## Concepts touched

- [[30-Concepts/dna-methylation]] — central concept.
- [[30-Concepts/cpg-island]] — defined here as the constitutively unmethylated regulatory features.
- [[30-Concepts/dnmt]] — maintenance and de novo methyltransferases.
- [[30-Concepts/tet-enzymes]] — active demethylation.

## Connections to other sources

- **Methodological foundation for** [[10-Summaries/yilei-2025-naturereviewsgenetics]] — Yilei 2025 reviews the computational analysis of DNA methylation from long-read sequencing, building on the biological framework Smith & Meissner establish here.
- **Provides developmental context for** [[10-Summaries/ian-2015-trendsingenetics]] and [[10-Summaries/lars-2017-naturereviewsgenetics]] — methylation reprogramming windows partly overlap with the developmental periods of high genome instability and mosaicism.

## Open questions

- Locus-specific timing of methylation establishment in human development — much known from mouse, less from human.
- The functional significance of non-CpG methylation (mCpH) in adult tissues, especially in the brain.
- 5hmC and other oxidative intermediates as functional marks vs transient intermediates — still unresolved at time of writing.

---
**Source:** [DOI](https://doi.org/10.1038/nrg3354)
