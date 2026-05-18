---
type: summary
title: "Kim & Costello 2017 — DNA methylation as an epigenetic mark of cellular memory"
source: "[[00-Sources/papers/DNA methylation_ an epigenetic mark of cellular memory]]"
source_kind: paper
author: "Mirang Kim, Joseph F. Costello (corresponding)"
published: 2017-04-28
ingested: 2026-05-12
doi: "10.1038/emm.2017.10"
journal: "Experimental & Molecular Medicine"
tags: [review, DNA-methylation, epigenetic-memory, stem-cells, cancer, CUP, iPSCs]
entities:
  - "[[20-Entities/joseph-costello]]"
  - "[[20-Entities/mirang-kim]]"
concepts:
  - "[[30-Concepts/dna-methylation]]"
  - "[[30-Concepts/dnmt]]"
  - "[[30-Concepts/tet-enzymes]]"
  - "[[30-Concepts/uhrf1]]"
  - "[[30-Concepts/bisulfite-sequencing]]"
  - "[[30-Concepts/epigenetic-memory]]"
  - "[[30-Concepts/cancer-of-unknown-primary]]"
  - "[[30-Concepts/cpg-island]]"
topics:
  - "[[40-Topics/dna-methylation]]"
---

**Citation:** Kim et al. (2017) — *DNA methylation as an epigenetic mark of cellular memory* — *Exp Mol Med*. [DOI](https://doi.org/10.1038/emm.2017.10)

# Kim & Costello 2017 — DNA methylation as cellular memory

> Thesis: DNA methylation patterns are heritable across cell divisions and act as an **epigenetic memory** that records cell-type identity, developmental history, and pathological trajectory. This memory has practical consequences: iPSCs retain residual methylation from their donor cells and preferentially differentiate back toward those lineages; cancer cells retain methylation signatures of their tissue of origin even at metastatic sites, enabling **EPICUP**-style methylation classifiers for cancer of unknown primary.

## Key claims

- **Maintenance machinery**: DNMT1 with PCNA + UHRF1 at the replication fork; UHRF1 reads hemimethylated CpGs via its SRA domain; H3K9me3 recruits UHRF1 and stabilizes DNMT1. LSD1/KDM1 demethylates DNMT1 and modulates its stability. The maintenance machinery is **chromatin-coupled** — it isn't a standalone enzymatic system but a chromatin-state-dependent module.
- **Active demethylation**: TET1/2/3 oxidize 5mC → 5hmC → 5fC → 5caC; thymine-DNA glycosylase excises 5fC/5caC for base-excision repair. Passive demethylation occurs when DNMT1 fails during replication.
- **De novo methylation**: DNMT3A/B + DNMT3L (catalytically inactive cofactor that reads H3K4me0). Recruited to repressive chromatin via H3K9 methyltransferases (G9A) and chromatin remodelers (LSH).
- **Stem-cell memory**: iPSCs retain donor-cell methylation signatures and preferentially differentiate toward original lineage. ESCs uniquely tolerate non-CpG methylation (~25% of methylated Cs at CpA in human ESCs). MSCs methylation differences between donors predict differentiation propensity — a quality-control biomarker.
- **Cancer memory**: hypermethylated cancer CpG islands are biased to PRC2/H3K27me3 targets in normal cells (cancer hijacks the embryonic-progenitor methylation program). IDH1/2 mutations sequester α-ketoglutarate, inhibiting TET and KDM enzymes — explaining glioma G-CIMP and AML hypermethylation. Intratumoral methylation heterogeneity reconstructs tumor evolution with histories consistent with mutation/CNV-based phylogenies.
- **EPICUP** classifier: methylation signatures identify primary site in 87% of cancer of unknown primary cases, with 99.6% specificity and 97.7% sensitivity in validation.

## Methods / evidence

Authoritative review. Three sections: (1) DNA methylation biology and analysis methods (WGBS, RRBS, 450k/EPIC array); (2) stem cells (ESC, iPSC, HSC, MSC, NSC); (3) cancer (tumor initiation, evolution, CUP).

## Surprising or load-bearing bits

- Methylation as a **"clinically diagnostic clock"** for cancer origin: EPICUP gets close to oncologist-grade tissue-of-origin calls from a single epigenetic readout.
- The framing that methylation is **simultaneously a memory and a clock** is the through-line: memory of cell type (CUP), memory of donor lineage (iPSC), and a clock for aging (epigenetic age).
- The IDH-mutation → α-KG depletion → TET/KDM inhibition → hypermethylation causal chain unifies multiple cancer methylation phenomena.

## Connections to other sources

- Foundational background for [[10-Summaries/sctem-seq-single-cell-analysis-of-transposable-element-methylation-to-link-global-epigenetic-heterogeneity-with-transcriptional-programs]] (TE methylation as bulk surrogate), [[10-Summaries/simultaneous-single-cell-analysis-of-5mc-and-5hmc-with-simple-seq]] (SIMPLE-seq joint 5mC/5hmC), and [[10-Summaries/high-throughput-single-cell-dna-methylation-and-chromatin-accessibility-co-profiling-with-splicool-seq]] (SpliCOOL-seq).
- Extends the methylation/lineage memory framing from [[10-Summaries/zachary-2013-naturereviewsgenetics]] (Smith/Meissner 2013) and intersects with [[10-Summaries/yilei-2025-naturereviewsgenetics]] (long-read methylation).
- The MSC quality-control implication is a notable industry-applicable claim — methylation as a regenerative-medicine release criterion.

## Open questions

- Single-cell methylation tools were still emerging in 2017; this review predates SIMPLE-seq, scTEM-seq, SpliCOOL-seq, and modern single-cell joint readouts. Today's wiki cluster represents that maturation.

---
**Source:** [DOI](https://doi.org/10.1038/emm.2017.10)
## Related

- [[40-Topics/dna-methylation]] · [[30-Concepts/dnmt]] · [[30-Concepts/tet-enzymes]] · [[30-Concepts/uhrf1]] · [[30-Concepts/cancer-of-unknown-primary]]
