---
type: summary
title: "Smukowski Heil 2023 — Loss of heterozygosity and its importance in evolution"
source: "[[00-Sources/papers/Loss of Heterozygosity and Its Importance in Evolution - Journal of Molecular Evolution]]"
source_kind: paper
author: "Caiti Smukowski Heil (North Carolina State University)"
published: 2023-02-08
ingested: 2026-08-10
doi: "10.1007/s00239-022-10088-8"
journal: "Journal of Molecular Evolution"
tags: [loss-of-heterozygosity, mitotic-recombination, gene-conversion, yeast, experimental-evolution, two-hit-model, detection-methods]
entities: []
concepts: ["[[structural-variants]]", "[[post-zygotic-variation]]", "[[single-cell-variant-calling]]"]
topics: ["[[cancer-clonal-evolution]]", "[[somatic-mosaicism]]"]
---

**Citation:** Smukowski Heil, C. (2023) — *Loss of heterozygosity and its importance in evolution* — *Journal of Molecular Evolution* 91, 369–377. [DOI](https://doi.org/10.1007/s00239-022-10088-8)

# Smukowski Heil 2023 — LOH

> A yeast-centric review arguing that loss of heterozygosity — mitotic conversion of a heterozygous locus to homozygous — is not a rare accident but a **high-rate, adaptive, genome-shaping mutational class** that outpaces point mutation by orders of magnitude, and that its detection requires a specific analytical discipline distinct from variant calling.

## Key claims

- Two structural classes: **interstitial LOH** (gene conversion, typically <10 kb, evenly distributed) and **terminal LOH** (reciprocal crossover or break-induced replication, often >100 kb extending to the telomere, enriched near telomeres). The distributional difference implies different formation/resolution mechanisms.
- The rate is startling. In *S. cerevisiae*: 0.3–5.6 × 10⁻² per cell division for interstitial, 1.4–9.3 × 10⁻³ for terminal — i.e. **2.6–7.1 × 10⁻⁵ per SNP per cell division**, against a point-mutation rate of 1–3 × 10⁻¹⁰ per bp per division. LOH is roughly five orders of magnitude more frequent per site.
- Genomic impact is large: one mutation-accumulation experiment saw an average **15.9% of the genome** undergo LOH, with some lines approaching genome-wide homogenization.
- Rate scales with ploidy: 2.2 × 10⁻² events/division in triploids, 8.4 × 10⁻² in tetraploids, and higher ploidies skew toward short interstitial events.
- LOH lets recessive beneficial alleles **escape Haldane's sieve** — homozygosing them so they behave like dominants. Gerstein et al.'s nystatin-resistance experiment is the demonstration; theory (Mandegar & Otto) shows LOH can make asexual fixation match or beat sexual populations when the LOH rate exceeds the mutation rate.
- Dominance cuts both ways: LOH crossed a fitness valley for the underdominant *ACE2* "snowflake" multicellularity allele; overdominant variants (*STE4*, *CCW12*) *constrain* adaptive LOH at linked loci; and accumulated recessive-deleterious alleles in essential genes actively **preserve** heterozygosity in long-term diploid evolution (Johnson et al., 10,000 generations).
- Fitness effects can be enormous and environment-specific: *PHO84* LOH gives +39.30% at 15 °C for one parental allele and +25.57% at 30 °C for the other in *S. cerevisiae × S. uvarum* hybrids; CRISPR-mediated LOH at the *ENA* salt-efflux locus gives +27%. Beneficial LOH is typically repeatable *within* an environment and almost never across environments.
- LOH is the mechanistic second hit in **Knudson's two-hit model** of tumorigenesis — the review's explicit bridge to cancer.

## Methods / evidence

Review synthesizing mutation-accumulation studies, laboratory evolution, population genomics of 1,011 *S. cerevisiae* isolates, and CRISPR-directed mitotic recombination. The strongest evidence is the allele-replacement and CRISPR-LOH work, which converts observed LOH frequency into measured fitness coefficients — most of the field's LOH claims are correlational and this review is careful about the distinction ("more work is needed to disentangle how common these examples are").

The **detection methodology section is unusually practical** and is the part most transferable to human single-cell work:
- Pipeline: standard GATK best practices ([[mckenna-2010-gatk]]) variant calling → restrict to ancestral heterozygous sites → analyze allele frequencies.
- Filters given explicitly: `QD < 2.0 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0`, min DP 20; genotype 0/1 expected in the heterozygous ancestor.
- LOH tracts called from **≥3 consecutive SNPs** deviating from expected allele frequency toward 0 or 1.
- Detection power is bounded by ancestral heterozygosity — the review states plainly that if heterozygosity is low, small LOH events go undetected, and that experiments intending to study LOH should be *designed* for maximal heterozygosity (50,000–140,000 het SNPs in typical yeast crosses).
- For hybrids, LOH must be called as **copy number** (one subgenome 1→2, the other 1→0) rather than allele frequency, using sppIDer/MuLoYDH/Control-FREEC; >2 haplotypes require long-read phasing (nPhase).

## Surprising or load-bearing bits

- The five-orders-of-magnitude rate gap between LOH and point mutation is the number to carry away. Any somatic-evolution accounting that tracks SNVs and ignores LOH is measuring the minor term.
- **Underdetection is systematic and directional**: small interstitial events are the ones missed, so published LOH counts skew toward large terminal events. The review flags that evolved populations show almost exclusively terminal LOH while mutation-accumulation lines at higher ploidy show interstitial — and honestly declines to say whether that is biology or detection bias. That is precisely the artifact structure single-cell LOH calling would inherit.
- Recombination is locally mutagenic: *C. albicans* shows elevated mutation rate in regions adjacent to LOH tracts. LOH is not a clean substitution of one haplotype for another.
- Control-FREEC — a **tumor subclonal-frequency tool** — is recommended for yeast population LOH. The methodological traffic between cancer genomics and experimental evolution runs both directions here.

## Concepts touched

- [[post-zygotic-variation]] — LOH is a mitotic, post-zygotic event class that this wiki's mosaicism pages currently under-represent relative to SNVs and CNVs.
- [[single-cell-variant-calling]] — the "restrict to ancestral het sites, then read allele fraction" logic is exactly what allele-specific single-cell callers do; see [[zaccaria-2021-chisel|CHISEL]], which recovers allele- and haplotype-specific copy number and can therefore see copy-neutral LOH in single cells.
- [[allele-dropout]] — **critical tension**: WGA-induced ADO produces exactly the signature LOH detection relies on (a het site reading as homozygous). In single cells, LOH and ADO are confounded unless the caller models amplification explicitly. This review's clean yeast framework does not transfer without that correction.

## Connections to other sources

- [[mckenna-2010-gatk]] is the cited pipeline foundation.
- [[zaccaria-2021-chisel]] is the single-cell method that makes copy-neutral LOH detectable at all; [[satas-2020-scarlet]] and [[kaufmann-2022-medicc2]] handle LOH-bearing states in phylogeny.
- Cancer framing connects to [[cancer-clonal-evolution]] and [[lu-2024-cnaphylogeny-review]].
- [[eichler-2007-completing-sv-map]] names "unmasking of recessive mutations on the remaining allele" as an SV mechanism — this review is the population-genetic elaboration of that single line.

## Open questions

- **What is the somatic LOH rate in human tissues?** The yeast numbers are spectacular and completely non-transferable (different ploidy dynamics, different selection regime, different recombination machinery). No source in this corpus gives a per-division human somatic LOH rate.
- Whether the interstitial/terminal ratio reported in any single-cell human study reflects biology or the same detection asymmetry the review flags in yeast — untested.
- ADO/LOH confounding in scDNA-seq is not addressed by any source currently bookmarked; flagged to [[open-questions]].

## Related

- [[zaccaria-2021-chisel]] · [[post-zygotic-variation]] · [[cancer-clonal-evolution]] · [[eichler-2007-completing-sv-map]]
