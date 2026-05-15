---
type: summary
title: "Guo 2013 — Single-cell methylome landscapes by reduced representation bisulfite sequencing (scRRBS)"
aliases: [Guo 2013, scRRBS, Hongshan 2013]
tags: [scbs-seq, scRRBS, dna-methylation, single-cell-methylome, foundational, embryo]
created: 2026-05-12
updated: 2026-05-12
sources: ["00-Sources/papers/Hongshan_2013_GenomeResearch.pdf"]
---

**Citation:** Guo et al. (2013) — *Single-cell methylome landscapes by reduced representation bisulfite sequencing (scRRBS)* — *Genome Research*. [DOI](https://doi.org/10.1101/gr.161679.113)

# Guo et al. 2013 — scRRBS foundational

> Hongshan Guo, Ping Zhu, Xinglong Wu, Xianlong Li, Lu Wen, **Fuchou Tang**. *Genome Research* **23**, 2126–2135 (2013). DOI: 10.1101/gr.161679.113. Peking University + Peking-Tsinghua Center.

## Thesis

**scRRBS (single-cell Reduced Representation Bisulfite Sequencing)** is the foundational single-cell DNA methylome method. Combines MspI digestion (cuts at CCGG → enriches for CpG-rich regions including CGIs) with single-tube cell lysis + bisulfite conversion + library construction. Recovers **0.5–1.5 million CpG sites per single mESC** (~40% of bulk RRBS coverage), with bisulfite conversion rates >99%. Demonstrated that **the male pronucleus demethylates faster than the female pronucleus** in mouse zygotes — first single-cell demonstration of asymmetric parental-genome demethylation kinetics.

## Mechanism

1. Single cell lysed in one tube; genomic DNA released, NOT purified.
2. λ DNA spike-in (for bisulfite-conversion-rate measurement).
3. MspI digestion of naked dsDNA at CCGG.
4. End-repair, dA-tailing, adaptor ligation, bisulfite conversion — all in the same tube.
5. Two rounds of PCR enrichment with carrier tRNA, deep sequencing.

## Key claims

- **0.5–1.5M CpG sites per single mESC** detected at ≥1× (1.5M = 63% of bulk RRBS coverage with maximal effort; 40% of all detectable RRBS sites typically).
- Eight individual mESCs analyzed; methylome profile is reproducible (R = 0.67 ± across pairs); aggregate of 8 cells correlates with bulk mESC RRBS at R = 0.90.
- **scRRBS is digital**: 88–94% of CpG sites in a single sperm cell are either fully methylated (100%) or fully unmethylated (0%) — confirms haploid sperm methylation is binary, validating the method's single-CpG accuracy.
- **Demethylation kinetics asymmetry**: male pronucleus demethylates faster than female pronucleus after fertilization (gene-body regions); first single-cell observation of this developmental hallmark.

## Surprising / load-bearing for the review

- **The chemical chassis behind [[sctrio-seq|scTrio-seq]]** — Hou 2016 explicitly builds on the same Tang-lab scRRBS protocol with mild cytoplasm-only lysis to also retain mRNA.
- The **digital binary methylation observation in sperm** is the foundational evidence that single-CpG-level methylation in haploid cells is essentially deterministic — the noise visible in diploid bulk data is mostly cell-to-cell heterogeneity, not within-cell stochasticity. This matters for interpreting any scBS / scRRBS / scNMT-seq dataset.
- For §3.3 of the planned review, scRRBS is the entry point for the entire single-cell methylome family that grew into snmC-seq, snmC-seq2, sciMETv2, scBS-seq, [[scnmt-seq]], [[sctrio-seq]].

## Entities / concepts touched

[[scbs-seq]] · [[bisulfite-sequencing]] · [[dna-methylation]] · [[cpg-island]] · [[20-Entities/xiaoying-fan]] · [[40-Topics/dna-methylation]]

## Related summaries

- [[chongyuan-2018-naturecommunications]] — snmC-seq2, modern atlas-scale follow-on.
- [[single-cell-triple-omics-sequencing-reveals-genetic-epigenetic-and-transcriptomic-heterogeneity-in-hepatocellular-carcinomas]] — scTrio-seq, direct extension adding RNA arm.
- [[zachary-2013-naturereviewsgenetics]] — Smith/Meissner 2013 review citing this paper.

---
**Source:** [DOI](https://doi.org/10.1101/gr.161679.113) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/24179143/)

---
**Source:** [DOI](https://doi.org/10.1101/gr.161679.113) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/24179143/)
