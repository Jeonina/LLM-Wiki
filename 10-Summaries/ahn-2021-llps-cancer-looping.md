---
type: summary
title: "Ahn et al. 2021 — Phase separation drives aberrant chromatin looping in cancer (NUP98-HOXA9)"
source: "PubMed abstract / no local PDF (2026-05-15 ingest)"
source_kind: paper
author: "Jeong Hyun Ahn, Eric S. Davis, Timothy A. Daugird, Shuai Zhao, Ivana Yoseli Quiroga, ... Wesley R. Legant, Douglas H. Phanstiel, Gang Greg Wang (corresponding)"
published: 2021-06-23
ingested: 2026-05-15
ingest_depth: abstract-only
doi: "10.1038/s41586-021-03662-5"
journal: "Nature"
tags: [LLPS, phase-separation, cancer, leukemia, NUP98, HOXA9, IDR, chromatin-loops, CTCF, super-enhancer]
entities: []
concepts:
  - "[[30-Concepts/chromatin-phase-separation]]"
  - "[[30-Concepts/topologically-associating-domain]]"
topics:
  - "[[40-Topics/chromatin-architecture]]"
  - "[[40-Topics/hematopoietic-malignancies]]"
---

**Citation:** Ahn et al. (2021) — *Phase separation drives aberrant chromatin looping in cancer (NUP98-HOXA9)* — *Nature*. [DOI](https://doi.org/10.1038/s41586-021-03662-5)

# Ahn et al. 2021 — LLPS drives oncogenic chromatin looping

> Thesis: recurrent nucleoporin chimeras in hematological malignancies — **NUP98-HOXA9** as the prototype — owe their oncogenic activity to **liquid–liquid phase separation** driven by their intrinsically disordered regions (IDRs). LLPS-competent NUP98-HOXA9 forms nuclear puncta that (i) increase chromatin occupancy of the chimera, (ii) create broad super-enhancer-like binding patterns at leukemogenic genes, and (iii) **induce CTCF-independent chromatin loops** enriched at proto-oncogenes. Swapping the NUP98 phenylalanine-glycine IDR for an unrelated FUS-protein IDR reproduces the effect, proving LLPS itself — not the specific IDR sequence — is the driving feature.

## Key claims (from abstract)

- NUP98-HOXA9 contains the FG (phenylalanine-glycine) repeat IDRs of nucleoporin NUP98 fused to the HOXA9 homeodomain TF. The IDR is **necessary** for LLPS puncta formation and for leukemic transformation in vivo.
- LLPS **enhances chromatin occupancy** of the chimera and **broadens the binding footprint** into super-enhancer-like patterns at oncogenic targets.
- **Artificial IDR swap** (FUS-IDR replacing FG repeats) recapitulates LLPS, chromatin binding, and target gene activation — IDR identity is interchangeable; LLPS competence is the load-bearing property.
- **Hi-C** of phase-separated NUP98-HOXA9 shows **CTCF-independent chromatin loops** enriched at proto-oncogenes — a new class of cancer-driving 3D rearrangements.
- Generalizable: many disease-associated mutations target IDR-containing proteins; LLPS-driven aberrant transcription factor condensation may be a broad oncogenic mechanism.

## Why this matters for the wiki

- **Bridges Genetic → Structural-Physical axis** of DNA locus state. A point genetic alteration (translocation) creates an IDR-containing fusion that reshapes 3D chromatin architecture via biophysics. This is the cleanest molecular example of cross-axis coupling in the user's framework.
- **CTCF-independent loops** are a new mechanism for 3D-genome rewiring; complements [[10-Summaries/zaccaria-2021-chisel]] / [[10-Summaries/sanders-2020-sctrip]] (CN-driven 3D changes) and [[10-Summaries/nanopore-sequencing-unveils-somatic-structural-variations-as-biomarkers-in-laryngeal-squamous-cell-carcinoma-genomes]] (SV-driven loops).
- Therapeutic implication: targeting LLPS competence (rather than chimera function directly) is an emerging drug strategy.

## Connections to other sources

- **Builds on** [[10-Summaries/gibson-2019-chromatin-llps]] — establishes that chromatin LLPS is a normal feature; Ahn 2021 shows how oncogenic IDR fusions hijack it.
- **Cancer-3D-rearrangement counterpart**: [[10-Summaries/nanopore-sequencing-unveils-somatic-structural-variations-as-biomarkers-in-laryngeal-squamous-cell-carcinoma-genomes]] (Liu 2025, SV-driven 3D changes in LSCC).
- **Methodological adjacency**: [[10-Summaries/daugird-2024-viscoelastic-chromatin]] — same Legant lab co-author; chromatin viscoelasticity influences condensate dynamics.

## Open questions (raised by this source)

- How many other recurrent fusion oncoproteins (NUP214 chimeras, EWS-FLI1, FUS fusions in sarcoma) act primarily through LLPS competence rather than novel DNA-binding specificity?
- Can the CTCF-independent loop class be **single-cell mapped** with scHi-C in patient samples? If so, LLPS-driven loops could become a clinical biomarker.
- Do non-cancer LLPS condensates (heterochromatin foci, transcriptional hubs) create benign analogues of the same loops, and what distinguishes pathological from physiological condensate-loops?

## Note on ingest depth

Built from PubMed abstract + general knowledge of the published paper. Full PDF re-ingest required to populate quantitative details (Hi-C resolution, condensate dynamics rates, GO enrichment of loop anchors, in vivo transformation assay parameters).

---
**Source:** [DOI](https://doi.org/10.1038/s41586-021-03662-5) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/34163069/) · [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8647409/)

## Related

- [[30-Concepts/chromatin-phase-separation]] · [[30-Concepts/topologically-associating-domain]]
- [[10-Summaries/gibson-2019-chromatin-llps]] · [[10-Summaries/daugird-2024-viscoelastic-chromatin]]
- [[40-Topics/chromatin-architecture]] · [[40-Topics/hematopoietic-malignancies]]
