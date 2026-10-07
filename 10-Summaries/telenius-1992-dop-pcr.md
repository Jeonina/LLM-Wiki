---
type: summary
title: "Telenius et al. 1992 — Degenerate oligonucleotide-primed PCR (DOP-PCR)"
source: "[[00-Sources/papers/Degenerate oligonucleotide-primed PCR_ General amplification of target DNA by a single degenerate primer.pdf]]"
source_quality: full
source_sha256: "ce1957490074f099a4ca98ccf6c82e5c5df440ed4faa1473ef5474523417c5bc"
source_kind: paper
author: "Håkan Telenius (corresponding), Nigel P. Carter, Charlotte E. Bebb, Magnus Nordenskjöld, Bruce A. J. Ponder, Alan Tunnacliffe"
published: 1992-07
ingested: 2026-08-10
updated: 2026-10-07
doi: "10.1016/0888-7543(92)90147-K"
journal: "Genomics 13:718–725"
tags: [DOP-PCR, whole-genome-amplification, scWGA, founding-method, PCR, historical-anchor, flow-sorted-chromosomes, chromosome-painting, FISH, IRS-PCR, Alu-PCR]
entities: []
concepts: ["[[dop-pcr]]", "[[scwga]]", "[[scwga-chemistries]]"]
topics: ["[[whole-genome-amplification]]"]
---

**Citation:** Telenius et al. (1992) — *Degenerate oligonucleotide-primed PCR: general amplification of target DNA by a single degenerate primer* — *Genomics* 13, 718–725. [DOI](https://doi.org/10.1016/0888-7543%2892%2990147-K)

# Telenius 1992 — DOP-PCR

> Telenius and colleagues (Cambridge CRC group, with Karolinska) introduce **degenerate oligonucleotide-primed PCR**: one 22-nt primer with a fixed 5′ cloning tag, six degenerate positions and six fixed 3′ bases. Five low-temperature (30 °C) cycles let the short 3′ sequence prime at "multiple (e.g., ~10⁶ in human) evenly dispersed sites", and 25–35 later cycles at 62 °C amplify the tagged products. The paper is a **genome-mapping and cytogenetics** method, not a single-cell one. Inputs are nanograms of genomic DNA, cosmids, and **500 flow-sorted chromosomes**. The argument is made against **interspersed repetitive sequence PCR (IRS-PCR / Alu-PCR)**: DOP-PCR works in every species tested with the same primer, and its FISH paints cover chromosomes more evenly than Alu-PCR paints. The authors also argue that, because primer and polymerase run out early, DOP-PCR is effectively a **linear** amplification per fragment, each fragment ending "only 35–40 times the original concentration".

## Key claims

- **Primer design.** 6-MW is `5′ CCGACTCGAGNNNNNNATGTGG 3′`: an XhoI site at the 5′ end, six degenerate N, six specified 3′ bases. A second primer, 6-M, had a NotI site and only three specified 3′ bases. Both gave a smear on genomic DNA, but 6-MW amplified more efficiently, "possibly reflecting more efficient annealing" (Fig. 1a).
- **The low-temperature cycles are required.** With 6-MW on genomic DNA and no low-annealing cycles, "no amplification was detected". The degenerate positions are thought to stabilise annealing of the specified 3′ end. The authors conclude that priming in the first cycles "can therefore be regarded as being determined solely by the six 3′-most specified bases".
- **Priming is site-specific, not random.** Cosmid DNA amplified with 6-MW gave discrete, reproducible bands over a smear (Fig. 1b). A non-degenerate primer from the RET locus (RetA) also amplified the cosmid after low-temperature cycles, but "not to the same extent". The authors read this as a degenerate primer having access to more priming sites. RetA also gave unexplained bands with no template, which the authors could not account for.
- **Yield depends mainly on Taq concentration.** Product concentration tracked polymerase concentration (Fig. 2, lanes 7–9) and, less strongly, primer concentration in the 2–3 µM range. At 6.25 U/50 µl, primer-derived products appeared in the negative control. Routine conditions: 2–4 µM primer, 1.25–4 U polymerase per 50 µl, 2 mM MgCl₂, pH 8.4 (or 9.3 with TAPS, protocol B). Best yield was "up to 7 µg in 50 µl", from protocol B. Band patterns were stable across most conditions, but shifted at 5 mM MgCl₂ and at 8 µM primer.
- **Species independence.** The same primer amplified human, mouse and *Drosophila* genomic DNA as smears, and also flow-sorted chromosome 15. A 2.4-kb fragment amplified "to a lesser extent, in accordance with its lower sequence complexity" (Fig. 3).
- **More even than Alu-PCR by FISH.** Products from DOP-PCR and two Alu primers (517 and A1S) were biotinylated and painted onto normal male metaphases under identical confocal settings. DOP-PCR "produced more even hybridization, reaching saturation of the genome at a lower fluorescence signal amplifier gain". Both signal area and signal intensity confirmed this (Figs. 4–5). The authors explain the Alu bias by Alu's preference for G-light bands.
- **Cloning from flow-sorted translocation chromosomes.** DOP-PCR products from 500 flow-sorted copies of each t(10;18) derivative were cloned. Of 19 clones, 4 were highly repetitive (**21%**), compared with 17/55 (31%) and 7/18 (39%) reported for IRS-PCR libraries. Single-copy clones mapped back to the expected chromosome regions on a somatic-cell hybrid panel (Table 2). The authors suggest DOP-PCR amplifies "more uniformly along the chromosomes", whereas IRS-PCR "is directed toward repeat-rich regions".
- **Why amplification becomes linear (Discussion).** Because 6-MW primes about every 4 kb, the starting primer-to-target ratio is "300,000 fold less" than in single-locus PCR (4.4 × 10⁸). At 100% efficiency the primers would be used up after 10 cycles, against 29 for a single-locus primer. Polymerase runs out even sooner: at 1.25 U per 50 µl, "the enzyme will already be limiting during the second cycle". So "we thus observe a linear amplification by DOP-PCR of any one fragment", and each fragment ends at "only 35–40 times the original concentration". The authors call this model simplified.

## Methods / evidence

Cycling: 5 min at 95 °C, then 5 cycles of 94 °C 1 min / 30 °C 1.5 min / 3-min ramp from 30 to 72 °C / 72 °C 3 min, then 25–35 cycles of 94 °C 1 min / 62 °C 1 min / 72 °C 3 min (adding 1 s per cycle), with a final 10-min extension (Table 1). Templates: 100 ng human, mouse and *Drosophila* genomic DNA; 500 copies of flow-sorted chromosome 15; 10 ng cosmid cTBIRBP-9; 10 ng of a 2.4-kb RET fragment. All readouts are **agarose gels, FISH chromosome paints (with image analysis of signal area and intensity), cloning, and Southern mapping on a hybrid panel**. Nothing is sequenced, and locus-to-locus bias is never measured quantitatively.

Weight: a short methods paper (8 pages). The evidence is qualitative: gel smears and band patterns, a two-parameter FISH comparison on one metaphase set per primer, and 19 clones. It establishes that DOP-PCR works and is species-independent, and that it paints more evenly than Alu-PCR. It says nothing about single-cell input, coverage breadth or quantitative uniformity. The linear-amplification argument is a back-of-envelope calculation, not a measurement. (synthesis)

## Limitations

**Authors' own:**
- No-template bands from unique primers such as RetA, and occasionally from the degenerate primer, are "unexplained". Plasmid or cosmid contamination of primers is suggested and judged unlikely.
- Yield is capped by polymerase. Primer artefacts at 6.25 U/50 µl "probably put an upper limit on the amount of enzyme that can be used", and yields "varied considerably" between polymerase preparations.
- The linear-amplification model is presented as "simplified".
- The hybrid panel alone could not exclude other map locations for the chromosome-18 clones; a chromosome paint from the same material was needed.

**Reviewer notes:**
- The smallest input is 500 chromosome copies or about 10 ng of DNA. No single cell or single chromosome is amplified, so later single-cell use of DOP-PCR rests on other papers. (synthesis)
- "Evenly dispersed" priming is inferred from FISH evenness at the resolution of chromosome bands. Megabase-scale evenness does not imply locus-level uniformity, and later quantitative work found large locus-to-locus bias ([[10-Summaries/dean-2002-mda]]). (synthesis)
- Uniformity is compared only with Alu-PCR, on one metaphase set per primer. There is no comparison with linker-adapter PCR, the other alternative the Introduction discusses, and no replicate statistics. (synthesis)

## Surprising or load-bearing bits

- **The founding paper calls DOP-PCR linear.** The wiki usually describes DOP-PCR as the exponential, bias-compounding PCR chemistry. Telenius et al. argue the opposite for their conditions: amplification is limited by primer and polymerase almost from the start. The "exponential bias" description comes from later single-cell work, not from this paper. (synthesis)
- **The comparator was IRS-PCR, not MDA.** In 1992 the point of DOP-PCR was to escape the species dependence and G-light-band bias of Alu-PCR. Its evenness claim is relative to Alu paints.
- **It was built for chromosome painting and marker cloning.** The applications are flow-sorted translocation chromosomes, breakpoint mapping and region-specific libraries, which explains why DOP-PCR later remained a coarse-resolution (CNV/karyotype) chemistry. (synthesis)
- **Repeat depletion was visible from the start.** Only 21% of DOP-PCR clones were repetitive, against 31–39% for IRS-PCR. This matches the later finding that DOP-PCR depth is depleted in Alu and L1 regions ([[10-Summaries/hou-2015-wga-comparison]]). (synthesis)

## Concepts touched

- [[dop-pcr]] — founding citation; primer architecture, two-phase cycling and the authors' linear-amplification model.
- [[scwga-chemistries]] — DOP-PCR sits first in the chronology DOP-PCR → [[mda]] → [[malbac]] → [[pta]], though this paper itself is not a single-cell paper.
- [[scwga]] / [[whole-genome-amplification]] — "general amplification" of any target DNA is the conceptual origin of WGA.

## Connections to other sources

- [[dean-2002-mda]] measured DOP-PCR/PEP locus-to-locus bias at 4–6 orders of magnitude against <3-fold for MDA. That is the source of the quantitative bias figure; Telenius did not measure it.
- [[hou-2015-wga-comparison]] found commercial DOP-PCR kits the most even in read distribution and best for CNV, but lowest in genome recovery (~6% detection efficiency) and depleted in Alu and L1 regions. This fits Telenius's FISH evenness and low repeat fraction.
- [[zahn-2017-dlp]] and [[laks-2019-dlp-plus]] reject DOP-PCR along with the other WGA chemistries on duplicate and coverage-saturation grounds.
- Reviews placing DOP-PCR in the WGA lineage: [[gawad-2016-scgenome-review]], [[huang-2015-scwga-review]], [[lim-2024-single-cell-omics-review]].

## Open questions

- How did the authors' linear-amplification model hold up once single-cell inputs were used, where the primer-to-target ratio is far higher than with 100 ng of DNA? (synthesis)
- Which single-cell DOP-PCR application first established the method for single cells? It is not this paper, and the wiki does not yet have that primary source. (synthesis)

## Related

- [[dop-pcr]] · [[scwga-chemistries]] · [[whole-genome-amplification]] · [[dean-2002-mda]] · [[hou-2015-wga-comparison]]
