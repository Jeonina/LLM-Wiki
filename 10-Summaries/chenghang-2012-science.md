---
type: summary
title: "Zong 2012 — Genome-wide SNV + CNV detection of a single human cell (MALBAC foundational)"
aliases: [Zong 2012, MALBAC 2012, Chenghang 2012]
tags: [scWGA, MALBAC, foundational, scDNA-seq, copy-number]
created: 2026-05-12
updated: 2026-05-12
source: "[[00-Sources/papers/Genome-Wide Detection of Single-Nucleotide and Copy-Number Variations of a Single Human Cell]]"
sources: ["00-Sources/papers/Chenghang_2012_Science.pdf"]
---

**Citation:** Zong et al. (2012) — *Genome-wide SNV + CNV detection of a single human cell (MALBAC foundational)* — *Science*. [DOI](https://doi.org/10.1126/science.1229164)

# Zong et al. 2012 — MALBAC foundational

> Chenghang Zong, Sijia Lu, Alec R. Chapman, X. Sunney Xie. *Science* **338**, 1622–1626 (21 Dec 2012). DOI: 10.1126/science.1229164. Harvard.

## Thesis

**MALBAC (Multiple Annealing and Looping-Based Amplification Cycles)** is a new single-cell WGA method that uses quasilinear preamplification with looping protection of full-length amplicons followed by exponential PCR. Achieves **93% genome coverage at ≥1× from a single human SW480 cancer cell at 25× depth** — far better uniformity than MDA. The first method to enable reliable CNV calls and SNV-from-kindred-cells discovery at single-cell resolution.

## Mechanism

1. Single cell lysed; gDNA melted at 94°C.
2. **MALBAC primers** (common 27-nt + 8 random nucleotides) hybridize at 0°C.
3. Strand-displacing polymerase extends at 65°C → semi-amplicons of 0.5–1.5 kb.
4. Melting 94°C → looping at 58°C: full amplicons self-loop (5′ and 3′ ends are complementary), preventing further use as template → **quasilinear amplification**.
5. Five preamplification cycles, then exponential PCR using the common 27-nt sequence.

## Key claims

- **93% coverage at ≥1× / 25× depth** vs MDA's 72% on the same cells. **76% SNV detection efficiency** for MALBAC vs 41% for MDA.
- Lorenz curve of MALBAC sits close to bulk; power spectrum shows minimal large-scale bias (unlike MDA which has high low-frequency amplitudes = megabase-scale over/underamplification).
- CNV calls from three single SW480 cells at 0.8× depth match bulk; **single-cell CNV differences within the bulk are resolvable** (region in dashed box of Fig. 3).
- **SNV detection from kindred-cell comparison**: 148 newly acquired SNVs from 2 kindred cells (~100 false positives from C→T deamination); 35 from 3 kindred cells. **Purine-pyrimidine exchanges occurred unusually frequently** among newly acquired SNVs — first observation of mutation-spectrum bias from single-cell scWGA.

## Surprising / load-bearing for the review

- **The foundational paper for §3.1 (Genotype-Centric DNA Profiling) scWGA section.** MALBAC, MDA, DOP-PCR are the three chemistries the review's §3.1 WGA-chemistry comparison table needs to anchor. Subsequent methods ([[chen-2017-lianti|LIANTI]] 2017, [[pta]] 2021) explicitly benchmark against MALBAC.
- The "purine-pyrimidine SNV bias" finding is the prior art for the C→T deamination artifact problem that [[chen-2017-lianti|LIANTI]] later attributed to cytosine deamination after cell lysis and that [[pta]] later quantified.

## Entities / concepts touched

[[malbac]] · [[scwga]] · [[30-Concepts/scdna-seq]] · [[mda]] · [[dop-pcr]] · [[allele-dropout]] · [[20-Entities/stephen-quake]] · [[40-Topics/whole-genome-amplification]]

## Related summaries

- [[chen-2017-lianti]] — LIANTI; next-generation WGA chemistry.
- [[gawad-2016-scgenome-review]] — Gawad/Quake 2016 review citing MALBAC.
- [[evrony-2021-scDNA-applications-review]] — Evrony 2021 capabilities framework.

---
**Source:** [DOI](https://doi.org/10.1126/science.1229164) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/23258894/)
