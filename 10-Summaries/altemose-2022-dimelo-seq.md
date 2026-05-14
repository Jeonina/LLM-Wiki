---
type: summary
title: "Altemose 2022 — DiMeLo-seq: long-read single-molecule mapping of protein-DNA interactions"
aliases: ["Altemose 2022 DiMeLo-seq", "DiMeLo-seq"]
tags: [DiMeLo-seq, long-read, pA-Hia5, antibody-directed-methylation, protein-DNA-mapping, CENP-A, repetitive-regions, Straight-lab, Streets-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Nicolas_2022_NatureMethods.pdf"]
---

Altemose, Maslan, Smith, Sundararajan et al. (Straight, Streets labs; UC Berkeley + Stanford + UCSC) developed **DiMeLo-seq** (Directed Methylation with Long-read sequencing) for genome-wide single-molecule protein-DNA interaction mapping. Workflow: permeabilized nuclei → bind primary antibody to target protein → bind **pA-Hia5** (protein A fused to the non-specific adenine methyltransferase Hia5) → add SAM → Hia5 deposits m6A near the antibody's binding site on native DNA → long-read sequencing (ONT/PacBio) reads m6A + endogenous CpG methylation simultaneously. Advantages: (i) **no DNA amplification** — preserves endogenous modifications; (ii) **single-molecule resolution** — multiple binding events per fiber; (iii) **haplotype-resolved** binding maps via heterozygous SNPs; (iv) maps protein-DNA interactions in **repetitive regions** (e.g., centromeres) that are unmappable with short-read approaches. Applied to LADs, CTCF, and CENP-A — including density estimation of CENP-A molecules along single chromatin fibers.

## Why this matters

A major §3.2/§3.3 anchor for **next-generation protein-DNA mapping** — bridges the chromatin-accessibility assays (ATAC, DNase) and the antibody-based ChIP/CUT&RUN family with long-read single-molecule SMF (Fiber-seq, SMAC-seq, nanoNOMe). Critical when discussing centromere biology and repetitive-region accessibility, which other methods cannot address. Existing bibkey `altemose2022` may not exist — needs check; otherwise add. Important precursor to scDAF-seq (Swanson 2025) which removes the m6A → C→T trade-off.

---
**Source:** [DOI](https://doi.org/10.1038/s41592-022-01475-6) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/35396487/)

## Related

- [[10-Summaries/shipony-2020-smac]]
- [[10-Summaries/lee-2020-nanonome]]
- [[10-Summaries/swanson-2025-daf-seq]]
- [[10-Summaries/peter-2024-brain-fiberseq]]
- [[30-Concepts/single-molecule-footprinting]]
