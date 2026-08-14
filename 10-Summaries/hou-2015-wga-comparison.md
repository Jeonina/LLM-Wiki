---
type: summary
title: "Hou et al. 2015 — Comparison of variations detection between whole-genome amplification methods used in single-cell resequencing"
source: "[[00-Sources/papers/Comparison of variations detection between whole-genome amplification methods used in single-cell resequencing]]"
source_kind: paper
author: "Yong Hou, Kui Wu, Xulian Shi, Fuqiang Li, … Michael Dean, Han Liang, Xun Xu, Ling Wang, Jun Wang"
published: 2015-08-06
ingested: 2026-08-13
doi: "10.1186/s13742-015-0068-3"
journal: "GigaScience 4:37"
tags: [WGA-benchmark, DOP-PCR, MDA, MALBAC, allele-dropout, CNV-detection, SNV-detection, kit-comparison]
entities: []
concepts: ["[[scwga]]", "[[scwga-chemistries]]", "[[dop-pcr]]", "[[mda]]", "[[malbac]]", "[[allele-dropout]]", "[[copy-number-variation]]", "[[sequencing-depth-and-coverage]]", "[[quality-control-metrics]]"]
topics: ["[[whole-genome-amplification]]", "[[scdna-seq]]", "[[computational-methods]]"]
---

**Citation:** Hou et al. (2015) — *Comparison of variations detection between whole-genome amplification methods used in single-cell resequencing* — *GigaScience* 4, 37. [DOI](https://doi.org/10.1186/s13742-015-0068-3)

# Hou 2015 — WGA kit benchmark

> Seven **commercial kits**, three chemistries, 29 single cells, one conclusion that has aged well: **there is no best WGA method, there is a best WGA method per variant class.** [[dop-pcr|DOP-PCR]] wins on read evenness and therefore [[copy-number-variation|CNV]] accuracy; [[mda|MDA]] wins on genome recovery (~84% vs ~6%) and therefore SNV detection; [[malbac|MALBAC]] sits between them.

## Key claims

- **The chemistry ranking inverts depending on what you are calling.** DOP-PCR has the highest duplication ratio and the worst genome recovery, but the most even read distribution and the best reproducibility — so it is the best CNV caller substrate. MDA has ~84% consensus-genotype detection efficiency against ~6% for DOP-PCR and ~52% for MALBAC — so it is the best SNV substrate. This is the paper's whole point and it is a *design-selection* result, not a winner announcement.
- **Kit identity matters as much as chemistry identity.** Three MDA kits behaved very differently: Qiagen REPLI-g Single Cell (MDA-2) gave the highest genome coverage (8.84% at 0.1× extraction) and best effective depth (82.2% of genome at ≥10×), while REPLI-g Mini (MDA-1) had the *highest* read-distribution bias of all seven kits and GenomiPhi V2 (MDA-3) showed strong GC dependence (59.5% at ≥10×). Reporting "we used MDA" is insufficient methods description.
- **Mapping and duplication separate cleanly by chemistry.** Mean mapping ratio: MDA 98.36% (SD 0.92), MALBAC 97.68% (SD 0.17), DOP 89.31% (SD 2.41). DOP-PCR's whole-genome duplication ratio reaches 39.24%, which is why 30× raw sequencing yields only ~3× mapped and 23.23% genome coverage.
- **Unmapped-read composition differs by mechanism, not GC.** GC content of unmapped reads did not differ across methods; the **N ratio** did — highest for MALBAC, lowest for MDA, attributed to φ29's fidelity.
- **DOP-PCR is specifically depleted in repeat regions.** Normalised depth in Alu and L1 regions is significantly below its own genome-wide level, and the gap is larger than for any other method — a direct consequence of degenerate-primer annealing.
- **Both MDA and MALBAC detect real cancer CNVs.** In a gastric cancer line (BGC823) at ~0.5× depth, both recovered 12p11.22 (*KRAS*) and 9p24.1 (*JAK2*, *CD274*, *PDCD1LG2*) amplifications with comparable sensitivity and specificity.
- **Concordance is high even where detection efficiency is low.** MDA-2: 84.57% detection (up to 94.62%) at 97.10% concordance; MALBAC 51.87% at 96.74%; MDA-3 66.63% at 97.12%; DOP-1 6.00% at only 82.05%. The lesson: low recovery and low accuracy are separable failure modes, and DOP-PCR suffers both for SNVs.

## Methods / evidence

A deliberate **narrowing-down design**: (a) low-coverage WGS (~0.5×, downsampled to a uniform 0.1×) on 20 YH lymphoblastoid single cells across all seven kits to compare mapping, duplication, and uniformity; (b) deep (~30×) WGS on the best performers plus published MALBAC SW480 data for bias and SNV analysis; (c) real CNV detection on 10 BGC823 gastric cancer cells (5 MALBAC, 5 MDA-2) on Ion Proton. Bulk YH and BGC823 data as unamplified controls; "golden control" genotype sets defined by intersecting bulk consensus with the Illumina 2.5M Omni chip.

Seven kits: GenomePlex (DOP-1), Silicon Biosystems Ampli1 (DOP-2), NEB (DOP-3), REPLI-g Mini (MDA-1), REPLI-g Single Cell (MDA-2), GenomiPhi V2 (MDA-3), Yikon MALBAC.

Weight: n is small per kit (29 cells across seven kits, deep sequencing on five), and the MALBAC deep data is downloaded from a different cell line (SW480) rather than generated on YH — so the MALBAC-vs-MDA deep comparison is confounded by cell line and lab. The low-coverage comparison, which *is* matched, is the more trustworthy half.

## Surprising or load-bearing bits

- **The 0.1× downsampling step is the methodological move worth copying.** Without normalising depth across kits, every uniformity comparison is confounded by sequencing effort. Most WGA comparisons before and since skip this.
- **"MDA" is not one thing.** The MDA-1 vs MDA-2 vs MDA-3 spread here is wider than the gap between chemistries in some metrics — a result that quietly undermines a decade of papers citing "MDA bias" as a single property.
- **DOP-PCR's ~6% SNV recovery is the number that killed it for variant work** while its evenness kept it alive for CNV work — and this split is exactly why [[navin-2011-sns-tumor-evolution|SNS]] used DOP-PCR for copy number and [[wang-2014-nuc-seq|nuc-seq]] switched to MDA for point mutations.
- Only ~5.93% of the genome reached ≥10× in DOP-1 deep data despite 30× raw input. Raw sequencing depth is a near-meaningless quality metric for amplified single cells.
- **This benchmark predates [[pta|PTA]] entirely.** Read against [[gonzalez-pena-2021-pnas]], it documents the problem PTA was built to solve — and its "no best method" conclusion is precisely the claim PTA later challenged.

## Concepts touched

- [[scwga-chemistries]] — the three-chemistry landscape with per-kit resolution.
- [[allele-dropout]] — measured alongside false-positive ratio; MDA and MALBAC comparable, DOP-PCR far worse.
- [[quality-control-metrics]] — mapping ratio, duplication ratio, normalised depth distribution vs a Poisson reference, cumulative depth curves, CGDE and concordant ratio.

## Connections to other sources

- Contemporaneous review covering the same three chemistries with the Xie lab's own data: [[huang-2015-scwga-review]] — the two should be read together; they agree on the chemistry ordering.
- Founding chemistry papers: [[telenius-1992-dop-pcr]], [[dean-2002-mda]], [[chenghang-2012-science]] (MALBAC), protocol at [[zong-2017-malbac-protocol]].
- Cited comparisons it builds on: Quake lab's *E. coli* three-way comparison and an 11-hippocampal-neuron comparison (both referenced, neither ingested).
- Superseded on the accuracy frontier by: [[chen-2017-lianti]] (LIANTI), [[gonzalez-pena-2021-pnas]] (PTA).
- The amplification-free escape route: [[zahn-2017-dlp]], [[laks-2019-dlp-plus]].
- Downstream callers whose error models assume these chemistries: [[zafar-2016-monovar]], [[dong-2017-sccaller]], [[luquette-2019-natcomm]].

## Open questions

- **The MALBAC deep comparison is cross-cell-line.** Whether MALBAC's 51.87% detection efficiency would hold on YH cells is untested here.
- No indel benchmarking at all — the class most vulnerable to polymerase slippage is absent.
- Chimera rates are not quantified, despite being the main obstacle for structural-variant calling from MDA (raised in [[huang-2015-scwga-review]] and in the assembly literature, [[chitsaz-2011-velvet-sc]]).

## Related

- [[huang-2015-scwga-review]] · [[scwga-chemistries]] · [[40-Topics/whole-genome-amplification]] · [[50-Notes/pta-inflection-point]]
