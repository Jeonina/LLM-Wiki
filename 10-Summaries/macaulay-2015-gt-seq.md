---
type: summary
title: "Macaulay 2015 — G&T-seq: separation and parallel sequencing of genome and transcriptome of single cells"
aliases: ["Macaulay 2015 G&T-seq", "G&T-seq", "genome and transcriptome sequencing"]
tags: [G&T-seq, parallel-scDNA-scRNA, multi-omics, oligo-dT, founding-method, Voet-lab, Ponting-lab, Sanger]
created: 2026-05-13
updated: 2026-05-13
sources: ["Iain_2015_NatureMethods.pdf"]
---

**Citation:** Macaulay et al. (2015) — *G&T-seq: separation and parallel sequencing of genome and transcriptome of single cells* — *Nature Methods*. [DOI](https://doi.org/10.1038/nmeth.3370)

Macaulay, Haerty, Kumar, Li, Hu et al. (Voet, Ponting labs; Sanger + Oxford + Leuven) developed **G&T-seq** (Genome and Transcriptome sequencing), the founding method for **parallel** scDNA + scRNA from the same cell. Workflow: single-cell lysate is incubated with biotinylated oligo-dT beads to capture poly(A) mRNA; the bead-bound RNA fraction is separated from the genomic DNA supernatant using a magnet. The mRNA fraction enters Smart-seq2-like full-length cDNA amplification; the DNA fraction enters MDA, PCR, or DA-PCR whole-genome amplification. Both fractions can subsequently be sequenced by short-read or long-read platforms. Demonstrated on HCC38 breast cancer and mouse ESCs, the method recovers both transcriptome and genome from individual cells with reduced cross-contamination compared to in-tube co-amplification.

## Why this matters

Founding paper for the entire single-cell **multimodal scDNA+scRNA** family. Direct predecessor of scMT-seq (DNA-methylation + RNA), DR-seq, sci-CAR (chromatin + RNA), scNMT-seq (Clark 2018, triple), and ultimately the 10x Multiome. Anchors §3.1 (parallel scDNA+scRNA) — every subsequent multi-omics paper must reference G&T-seq as the conceptual origin. From the Voet lab (Leuven) — major Strand-seq/scTRIP backbone — and shared infrastructure with the Sanger single-cell genomics centre.

---
**Source:** [DOI](https://doi.org/10.1038/nmeth.3370) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/25915121/)

---
**Source:** [DOI](https://doi.org/10.1038/nmeth.3370) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/25915121/)

## Related

- [[10-Summaries/clark-2018-scnmt]]
- [[10-Summaries/cao-2018-sciCAR]]
- [[10-Summaries/vandereyken-2023-scmultiomics-review]]
- [[10-Summaries/baysoy-2023-multiomics-landscape]]
- [[20-Entities/thierry-voet]]
- [[30-Concepts/parallel-scDNA-scRNA]]
