---
type: summary
title: "Dean 2002 — Comprehensive human genome amplification using multiple displacement amplification (MDA)"
source: "[[00-Sources/papers/Comprehensive human genome amplification using multiple displacement amplification]]"
aliases: ["Dean 2002", "MDA founding paper", "Φ29 WGA"]
tags: [MDA, scWGA, Phi29, isothermal-amplification, founding-method, whole-genome-amplification, Molecular-Staging]
created: 2026-05-14
updated: 2026-05-14
doi: "10.1073/pnas.082089499"
url: "https://www.pnas.org/doi/10.1073/pnas.082089499"
---

**Citation:** Dean et al. (2002) — *Comprehensive human genome amplification using multiple displacement amplification (MDA)* — *?*. [DOI](https://doi.org/10.1073/pnas.082089499)

Dean, Hosono, Fang et al. (Molecular Staging Inc., New Haven CT) introduced **Multiple Displacement Amplification (MDA)** ([DOI](https://doi.org/10.1073/pnas.082089499)), the **founding whole-genome amplification chemistry** that subsequently became the dominant scWGA method for the 15+ years preceding PTA. The method exploits the high processivity (~70 kb), strand-displacement activity, and low error rate (~10⁻⁶/base) of bacteriophage φ29 DNA polymerase paired with exonuclease-resistant random hexamer primers. Reactions run isothermally at 30 °C without thermal cycling: hexamers prime the genome at thousands of sites, φ29 extends and displaces downstream strands, displaced strands serve as templates for further priming, and amplification cascades exponentially until reagents saturate (~4–6 h). Key validation: starting from 0.3–300 ng human genomic DNA (down to single-digit cell-equivalents), MDA yielded ~20–30 µg of >10-kb product with **<3-fold locus-to-locus amplification bias** across 8 chromosomal positions — versus 4–6 orders of magnitude bias for DOP-PCR or PEP (PCR-based WGA), establishing MDA as quantitatively superior for unbiased whole-genome representation. Authors demonstrated downstream compatibility with SNP genotyping, RFLP, Southern blot, comparative genome hybridization, subcloning, and direct sequencing. MDA worked from whole blood lysate without DNA purification.

## Why this matters

**The chemistry that made scDNA-seq possible.** Every PTA, MALBAC variant, and single-cell genomics method that uses Φ29-based amplification descends from this paper. The <3-fold uniformity claim was the central technical justification for moving WGA away from PCR-based DOP-PCR/PEP toward isothermal strand-displacement. MDA's properties — high coverage, long product (>10 kb amenable to library prep), tolerance of crude lysates — became the template that scWGA chemistries refined: PTA (Gonzalez-Pena 2021) preserves Φ29 + random primer architecture while engineering against MDA's main failure modes (allelic dropout, chimera formation, exponential→quasi-linear amplification). For a scDNA-seq review, Dean 2002 is the historical anchor for the WGA branch — it is what "scWGA" in modern nomenclature operationally inherits.

## Key claims and evidence

- **Locus-to-locus bias**: <3× across 8 loci for MDA vs. 4–6 orders of magnitude for DOP-PCR (TaqMan quantification, **Table 1** of paper).
- **Product length**: >10 kb average (alkaline gel electrophoresis).
- **Input sensitivity**: ~20–30 µg yield from inputs as low as 0.3 ng (≈90 genome copies, ~1–10 human cells).
- **Direct from biological material**: amplification from whole blood lysate without genomic DNA purification.
- **Downstream compatibility**: SNP genotyping accurately recapitulated (24/24 RFLP genotypes from MDA product matched ground-truth Coriell genotypes), CGH profiles matched unamplified, restriction-fragment patterns matched, Southern signals matched.

## Limitations (anticipated and later confirmed)

The 2002 paper does *not* yet describe what would later become MDA's defining problems at single-cell scale:
- **Allelic dropout**: at single-cell input, one of the two parental alleles often fails to amplify — central issue for heterozygous variant calling and quantified extensively in [[10-Summaries/gawad-2016-scgenome-review|Gawad & Quake 2016]] and [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]].
- **Chimera formation**: strand displacement occasionally joins distant genome segments — a structural-variant noise floor.
- **Exponential kinetics**: stochastic amplification timing leads to read-depth imbalance between loci that does not appear at the bulk inputs (0.3+ ng) tested here.
- **High error vs. duplex**: MDA error rate (~10⁻⁶) is high relative to duplex sequencing approaches (~10⁻⁹). Subsequent single-cell variant calling requires either deep coverage or specialized callers ([[30-Concepts/sccaller|SCcaller]], [[30-Concepts/monovar|MonoVar]]).

These limitations motivated successor chemistries — **MALBAC** (Zong/Xie 2012; quasilinear pre-amplification), **LIANTI** (Chen/Xie 2017), and **PTA** (Gonzalez-Pena 2021; quasilinear via terminator-augmented Φ29) — each addressing one or more MDA failure modes.

## Place in scWGA lineage

| Year | Method | Key advance over predecessor |
|---|---|---|
| ~1990s | DOP-PCR / PEP | First WGA; PCR-based, severe bias |
| **2002** | **MDA (Dean)** | **Φ29 + random hexamer; <3× bias** |
| 2007 | Microfluidic MDA | Reduced contamination, better uniformity |
| 2012 | MALBAC | Quasilinear pre-amplification reduces exponential bias |
| 2017 | LIANTI | Linear amplification via transposition + IVT |
| 2021 | PTA | Φ29 + terminators → quasilinear; near-bulk uniformity |

## Related

- [[30-Concepts/mda]] — concept page anchored by this paper
- [[30-Concepts/scwga]] · [[30-Concepts/pta]] · [[30-Concepts/malbac]] · lianti
- [[30-Concepts/allele-dropout]] — the failure mode that motivated MDA's successors
- [[10-Summaries/gawad-2016-scgenome-review]] — Gawad & Quake review benchmarking MDA against successors
- [[10-Summaries/shao-2025-scDNA-mosaicism-review]] — Shao 2025 review with current scWGA landscape
- [[40-Topics/whole-genome-amplification]]

## Citation

Dean FB, Hosono S, Fang L, Wu X, Faruqi AF, Bray-Ward P, Sun Z, Zong Q, Du Y, Du J, Driscoll M, Song W, Kingsmore SF, Egholm M, Lasken RS. *Proc Natl Acad Sci USA* 99(8): 5261–5266 (2002). [DOI](https://doi.org/10.1073/pnas.082089499) · [PNAS](https://www.pnas.org/doi/10.1073/pnas.082089499)
