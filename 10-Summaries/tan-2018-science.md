---
type: summary
title: "Tan 2018 — Three-dimensional genome structures of single diploid human cells (Dip-C)"
source: "[[00-Sources/papers/Three-dimensional genome structures of single diploid human cells]]"
aliases: ["Dip-C", "Tan 2018", "diploid single-cell 3D"]
tags: [scHi-C, Dip-C, 3D-genome, diploid, haplotype-resolved, Xie-lab]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Tan et al. (2018) — *Three-dimensional genome structures of single diploid human cells (Dip-C)* — *Science*. [DOI](https://doi.org/10.1126/science.aat5641)

Tan, Xing, Chang, Li and Xie (Harvard / Peking U) introduced Dip-C, the first single-cell chromatin-conformation method that reconstructs diploid (haplotype-resolved) 3D genome structures of single human cells. The chemistry combines an improved in-situ 3C protocol (no biotin pulldown) with META — multiplex end-tagging amplification — to substantially increase the number of detected chromatin contacts per cell. Dip-C detected a median of 1.04 million contacts per GM12878 cell (range 0.71–1.48 M), $\sim 5\times$ more than prior scHi-C methods, and 0.84 million per PBMC.

The Dip-C imputation algorithm assigns each contact to one of the two parental haplotypes using nearby germline-SNP-resolved contacts: nearby contacts (in genomic distance) tend to occupy the same homolog, so unknown haplotypes can be imputed from the haplotype identity of their neighbors. Cross-validation accuracy is $\sim$96\% per haplotype. The reconstructed 3D models at 20-kb resolution showed that the two alleles of imprinted loci and the two X chromosomes in female cells adopt statistically distinct genome structures — direct demonstration that haplotype-resolved single-cell 3D folding distinguishes parent-of-origin and X-inactivation states.

## Why this matters

Major methodological advance over the original scHi-C (Nagano 2013) and sciHi-C (Ramani 2017): Dip-C produces $\sim$5× more contacts per cell, resolves the two parental haplotypes separately, and supports 3D model reconstruction at $\sim$100-nm spatial resolution per 20-kb chromatin bead. Anchors §3.5 (3D genome) as the haplotype-resolved single-cell-3D method against which sn-m3C-seq (Lee 2019), Liu 2023 brain atlas, and IGS (Payne 2021) are compared.

---
**Source:** [DOI](https://doi.org/10.1126/science.aat5641) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/30166492/)

---
**Source:** [DOI](https://doi.org/10.1126/science.aat5641) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/30166492/)

## Related

- [[30-Concepts/dip-c]]
- [[30-Concepts/single-cell-hi-c]]
- [[10-Summaries/lee-2019-natmethods]]
- [[10-Summaries/liu-2023-mouse-brain-methylome-3d]]
- [[20-Entities/sunney-xie]]
