---
type: summary
title: "Falconer 2012 — DNA template strand sequencing of single-cells maps genomic rearrangements at high resolution (Strand-seq)"
aliases: ["Strand-seq founding paper", "Falconer 2012"]
tags: [Strand-seq, scDNA-seq, SCE, structural-variant, single-cell, Lansdorp-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Ester_2012_NatureMethods.pdf"]
---

Falconer, Hills, Naumann and Lansdorp introduced Strand-seq, the founding single-cell DNA-strand-sequencing method. Cells are cultured for one division in BrdU; daughter cells are sorted at G1; BrdU-substituted nascent strands are nicked photolytically (Hoechst + UV) so that PCR amplifies only the original parental template strand, producing directional libraries that preserve Watson/Crick identity at base resolution.

Demonstrated on 62 single mouse embryonic stem cells, Strand-seq mapped sister chromatid exchanges (SCEs) at $\sim$23 bp resolution — orders of magnitude better than any pre-existing single-cell method — and detected aneuploidy and CNVs from single replication rounds. Strikingly, Strand-seq identified $\sim$17 misoriented contigs totaling $\sim$25.57 Mb ($\sim$1% of the genome) in the mm9 mouse reference assembly that had persisted through several iterations and were undetectable by conventional sequencing.

Strand-seq's directional information enables haplotype-phase resolution, sister-chromatid-exchange detection (a sensitive biomarker for genotoxic stress and Bloom's syndrome), and identification of inversions/translocations missed by symmetric methods. The trade-off: BrdU labeling requires one round of division, so Strand-seq cannot be applied to postmitotic cells (e.g., adult neurons) and is incompatible with whole-genome amplification protocols that require both strands.

## Why this matters

Founding paper of the Strand-seq family. Anchors §3.1 (genotype-centric, structural-variant axis) and provides the directional read-out used downstream by DLP+, scNOVA (Jeong 2023), and SV-functional analyses. A complementary axis to MDA/MALBAC/PTA chemistries: where those amplify both strands non-uniformly, Strand-seq sacrifices both-strand readout to gain directional resolution.

---
**Source:** [DOI](https://doi.org/10.1038/nmeth.2206) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/23042453/)

## Related

- [[30-Concepts/strand-seq]]
- [[30-Concepts/scwga-chemistries]]
- [[20-Entities/peter-lansdorp]]
- [[10-Summaries/hyobin-2023-naturebiotechnology]]
