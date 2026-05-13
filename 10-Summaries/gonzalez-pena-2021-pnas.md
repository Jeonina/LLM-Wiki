---
type: summary
title: "Gonzalez-Pena 2021 — Accurate genomic variant detection in single cells with primary template-directed amplification (PTA)"
aliases: ["PTA", "Gonzalez-Pena 2021", "Primary template-directed amplification"]
tags: [scWGA, PTA, single-cell, mutation-detection, Gawad-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Veronica_2021_PNAS.pdf"]
---

Gonzalez-Pena and colleagues (Gawad lab, Stanford / St. Jude) introduced primary template-directed amplification (PTA), an isothermal whole-genome amplification chemistry that captures >95% of single-cell genomes uniformly and substantially reduces variant-calling error relative to MDA. PTA modifies the canonical $\phi$29 MDA reaction by adding irreversible-terminator dideoxynucleotides at low concentration. The terminators stochastically halt amplification at short distances ($\sim$100-bp amplicons), so the reaction operates on the primary template rather than on daughter amplicons — converting MDA's exponential, error-propagating amplification into a quasilinear, primary-template-restricted amplification.

The chemistry's principal benefits: (1) coverage uniformity dramatically improved over MDA — example chromosome-1 coverage tracks show flat, near-uniform depth instead of MDA's order-of-magnitude amplicon-to-amplicon variation; (2) allelic balance retained at near 0.5 (vs. MDA's heavy skewing); (3) per-cell coverage breadth of $\sim$95% of the genome at $\sim$30× depth, suitable for high-confidence SNV calling without LiRA- or SCAN-SNV-style allele-balance correction; (4) reduced per-cell input requirement.

The authors demonstrate two applications: direct measurement of environmental mutagenicity (DMEM) at single-cell base-pair resolution, and genome-wide off-target detection in CRISPR-edited cells.

## Why this matters

PTA is now the chemistry of choice for cohort-scale single-cell mosaicism studies. Anchors §3.1 (genotype-centric profiling) as the current state-of-the-art scWGA chemistry — substantially superior to MDA, MALBAC, and LIANTI on the coverage uniformity and variant-calling-accuracy metrics that determine cohort-scale feasibility. Bae 2022 \citep{bae2022} and subsequent BSMN cohort studies use PTA chemistry.

## Related

- [[30-Concepts/scwga-chemistries]]
- [[30-Concepts/primary-template-directed-amplification]]
- [[10-Summaries/chenghang-2012-science]]
- [[10-Summaries/chongyi-2017-science]]
- [[10-Summaries/macaulay-2014-plosgenet]]
- [[20-Entities/charles-gawad]]
