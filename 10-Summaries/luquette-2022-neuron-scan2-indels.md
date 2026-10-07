---
type: summary
title: "Luquette et al. 2022 — Single-cell genome sequencing of human neurons identifies somatic point mutation and indel enrichment in regulatory elements"
source: [
  "[[00-Sources/papers/Single-cell genome sequencing of human neurons identifies somatic point mutation and indel enrichment in regulatory elements]]",
  "[[00-Sources/papers/Ultraspecific somatic SNV and indel detection in single neurons using primary template-directed amplification]]"
]
source_quality: full
source_sha256: ["75a0503de6c9aba009c9727ab1b7d12b6644c26a5a4b9a4d449561e7f09a9650", "f4e6e0ade5db04070d74e5f9b9fe4d13751f0012b4c905ab236a7673d481eb33"]
aliases: ["luquette-2021-scan2", "Luquette 2021 SCAN2", "SCAN2", "Luquette 2022"]
source_kind: paper
author: "Lovelace J. Luquette, Michael B. Miller, Zinan Zhou, Craig L. Bohrson, Yifan Zhao, Hu Jin, Doga Gulhan, Javier Ganz, Sara Bizzotto, Samantha Kirkham, Tino Hochepied, Claude Libert, Alon Galor, Junho Kim, Michael A. Lodato, Juan I. Garaycoechea, Charles Gawad, Jay West, Christopher A. Walsh, Peter J. Park (corresponding)"
published: 2022-09-26
ingested: 2026-10-07
doi: "10.1038/s41588-022-01180-2"
journal: "Nature Genetics 54(10):1564-1571"
tags: [SCAN2, PTA, MDA, somatic-SNV, somatic-indel, neurons, aging, mutation-signatures, regulatory-elements, enhancers, single-strand-dropout, brain-mosaicism]
entities: ["[[lovelace-luquette]]", "[[peter-park]]", "[[christopher-walsh]]", "[[charles-gawad]]", "[[jay-a-a-west]]", "[[sara-bizzotto]]"]
concepts: ["[[single-cell-variant-calling]]", "[[pta]]", "[[mda]]", "[[allele-dropout]]", "[[mutational-signatures]]", "[[post-zygotic-variation]]", "[[cis-regulatory-element]]", "[[enhancer-states]]", "[[compounding-artifact]]"]
topics: ["[[brain-somatic-mosaicism]]", "[[mosaic-variant-calling]]", "[[whole-genome-amplification]]", "[[somatic-mosaicism]]"]
---

**Citation:** Luquette et al. (2022) — *Single-cell genome sequencing of human neurons identifies somatic point mutation and indel enrichment in regulatory elements* — *Nature Genetics* 54:1564–1571. [DOI](https://doi.org/10.1038/s41588-022-01180-2)

# Luquette 2022 — SCAN2 on PTA neurons

> Pairing **PTA** amplification with **SCAN2** — SCAN-SNV's allele-balance model plus a new **mutation-signature rescue** step and the first single-cell somatic **indel** caller — the authors catalogue 20,090 somatic SNVs and 2,714 somatic indels from 52 neurotypical human neurons. Three results matter: the neuronal SNV accumulation rate is revised to **~16 SNVs per year** (older MDA estimates were inflated by an artifact signature); somatic **indels accumulate at ≥3 per year per neuron**; and both mutation classes — indels most strongly — are **enriched in neuron-specific enhancers, promoters, highly expressed genes and conserved sequence**.

## Key claims

- **PTA beats MDA on the same brains.** 52 PTA neurons from the PFC of 12 neurotypical individuals (30–60×; including 15 neurons from 5 individuals from another study), compared with 75 MDA neurons previously amplified from 11 of the 17 individuals. PTA reduced coverage variability and allelic dropout. Large (>5 Mb) somatic copy-number changes appeared in only 2 of 52 PTA neurons, at odds with earlier reports of pervasive neuronal CNAs.
- **MDA's hidden artifacts, quantified.** On haploid male X chromosomes, MDA showed a median excess of 15 somatic SNVs and 3.7 indels per X versus PTA from the same individual — about 550 SNV and 136 indel **single-strand-dropout (SSD)** artifacts per MDA genome. In infant neurons, MDA gave ~10× more sSNVs than PTA (282 vs 26 per neuron), more C>T-dominated (85% vs 59%), matching artifact signatures B and scF.
- **SCAN2 design.** Two passes: stringent VAF-based calling (allele-balance model from heterozygous germline SNPs) learns the true mutation spectrum; then rejected candidates are rescued if unlikely under a universal PTA artifact signature. Indels add a cross-sample panel filter removing sites with indel-supporting reads in cells from multiple individuals (recurrent polymerase-stutter and microhomology artifacts).
- **Performance.** On simulated synthetic-diploid X chromosomes, SCAN2 raised sSNV sensitivity ~82% over SCAN-SNV (46% vs 25%) at similar FDR (8.6% vs 9.5%) and reduced FDR several-fold versus Monovar and SCcaller. For indels, SCAN-SNV applied naively gave 19.9% sensitivity with 61–85% false calls; GATK HaplotypeCaller + VQSR recovered 57% but with >99% FDR; SCAN2 recovered 33.6% of spiked indels at mean FDR <2%. Signature rescue needs ~500–1,000 mutations to learn the true spectrum. Introduction claims ~60-fold fewer FPs/Mb than conventional GATK and >5-fold fewer than other single-cell genotypers.
- **Kindred validation.** Crossbred mESC clones (one treated with aristolochic acid I): SCAN2 recovered 32% vs 26% (untreated) and 52% vs 41% (AAI) of clonal sSNVs versus SCAN-SNV; FDR 9–32% (untreated, definition-dependent) and ≈1% (AAI); the SBS22 aristolochic-acid signature was recovered.
- **Rates.** Mixed-effects model: 16.5 sSNVs per year in autosomes (LiRA on the same data: 17). Applying SCAN2 to the 74 MDA neurons gave 31/year, falling to 22/year after subtracting signature-B exposure and 19/year after removing an outlier. Indels: ~3 per neuron per year (a lower bound given sensitivity); deletions accumulated 3.3× faster than insertions; sizes −29 to +17 bp; MDA gave 6.0 indels/year (artifact-inflated).
- **Indel signatures.** COSMIC fit found ID4 (deletion-rich, unknown mechanism) most prevalent and most age-correlated (r = 0.82 vs 0.42 for ID5 and 0.69 for ID8); replication-linked clock-like ID1/ID2 were absent, consistent with postmitotic cells but also possibly due to low sensitivity.
- **Functional enrichment.** Signature rescue increased calls by ~36% for sSNVs (20,090 vs 14,748) and ~76% for indels (2,714 vs 1,541). In genes, mutation density rose with brain-specific expression (top decile: ~15% more sSNVs, 50–100% more indels). High-impact genic indels outnumbered sSNVs more than 2:1 despite sSNVs outnumbering indels 8:1. Indels were 42% over-represented in the most conserved 10% of the genome. TSS-distal enhancers: ~1.3 (SNV) and ~1.8 (indel) observed:expected, strongest for brain tissue; neuronal enhancers enriched (P < 10⁻⁴), glial enhancers less so; indels but not SNVs enriched at promoters, not cell-type specific. Enhancer-associated DNA-repair hotspots: +51% indels (P = 0.02).

## Methods / evidence

FANS-sorted NeuN⁺ nuclei from postmortem PFC; ResolveDNA (BioSkryb) PTA; NovaSeq 150-bp PE, BWA-MEM to hs37d5. Benchmarks: synthetic diploid X chromosomes with SNV/indel spike-ins (63 SDs; multiple COSMIC signatures), kindred crossbred mESC clones with bulk truth, MDA vs PTA from the same individuals. Enrichment via signature-matched permutations (scan2 permtool, 10,000 sets) restricted to callable genome; robust to higher depth cutoffs. Annotations: GTEx, Roadmap H3K27ac/H3K4me3 and ChromHMM, FACS-purified brain cell-type enhancers/promoters, sorted-cell ATAC OCRs, phyloP, SAR-seq and Repair-seq hotspots.

Weight: strong for the calling methodology (multiple orthogonal truth sets) and for the rate revision (same-individual MDA vs PTA). The rescue step is signature-dependent, so the authors themselves recommend VAF-only calls for signature extraction and nucleotide-content-matched permutations for regional enrichment. (The journal clipping carries no competing-interest statement; the preprint discloses one — see "Preprint version" below.)

## Surprising or load-bearing bits

- **Indels, not SNVs, carry the functional signal**: fewer in number but more often high-impact, more enriched in conserved sequence, enhancers and promoters. Activity-induced DNA breaks at neuronal regulatory elements are offered as a possible source.
- **Three orthogonal technologies converge on ~16–17 SNVs/year/neuron**: PTA+SCAN2, META-CS (~16/year) and NanoSeq (17.1 SNVs and 2.5 indels/year), as the Discussion notes — a rare case of agreement across single-cell and bulk duplex methods. The paper attributes some disagreement with NanoSeq (no sSNV–expression association; weak heterochromatin enrichment) to NanoSeq covering only ~29% of the genome.
- **Single-strand dropout** is the artifact class that defeats VAF-based filtering — near-100% VAF and no read evidence for the original haplotype — and is why haploid X is a clever internal control.
- **Few neuronal CNAs with PTA** (2/52) is quietly consequential for the earlier literature on neuronal aneuploidy/CNV prevalence. (synthesis)

## Concepts touched

- [[single-cell-variant-calling]] — signature-based rescue and the first credible single-cell somatic indel caller.
- [[pta]] / [[mda]] — same-individual comparison quantifying MDA SSD artifacts and signature B.
- [[allele-dropout]] — PTA reduces dropout; SSD is the extreme form at mutation sites.
- [[mutational-signatures]] — signature A (aging), artifact signatures B/scF, indel ID4 as most age-correlated.
- [[cis-regulatory-element]] / [[enhancer-states]] — neuronal enhancers and promoters as mutation-enriched compartments.
- [[compounding-artifact]] — MDA artifacts inflating a published biological rate (31 → ~19 after correction vs 16.5 with PTA).

## Connections to other sources

- Method lineage: [[luquette-2019-natcomm]] (SCAN-SNV), [[bohrson-2019-lira]] (LiRA, used here as a cross-check), [[luquette-2025-pta-duplex-mosaicism]] (later PTA + duplex validation).
- Chemistry: [[gonzalez-pena-2021-pnas]] (PTA). Comparator callers: [[zafar-2016-monovar]], [[dong-2017-sccaller]].
- MDA-era neuron mutation burden it revises: [[lodato-2017-aging-neurons]], [[lodato-2015-science]].
- Orthogonal rate estimates: [[abascal-2021-nanoseq]] (NanoSeq), [[meta-cs]] (META-CS).
- Brain mosaicism context: [[miller-2022-nature]], [[bizzotto-2022-brain-mosaicism-review]], [[50-Notes/pta-inflection-point]].

## Open questions

- Is ID4's mechanism in neurons transcription- or repair-associated, and why is it more age-correlated than the clock-like ID5/ID8?
- SCAN2 assumes cells pooled for signature rescue share mutational processes (a test is provided); disease or exposure cohorts may violate this.
- Indel sensitivity is lowest in homopolymers and tandem repeats >4 units, so the ~3/year rate is a lower bound and repeat-rich regulatory regions may be under-counted.
- Whether the indel enrichment in neuronal enhancers has functional consequence (e.g. altered regulation in aged or diseased brain) is proposed, not tested.

## Preprint version (merged 2026-10-07)

This page also covers the bioRxiv preprint *Ultraspecific somatic SNV and indel detection in single neurons using primary template-directed amplification* (Luquette et al., posted 2021-05-01, [DOI](https://doi.org/10.1101/2021.04.30.442032)), previously summarised separately as `luquette-2021-scan2` from an abstract-only clipping. The preprint abstract reported **76 PTA neurons, 15 sSNVs/year and ≥2 indels/year**; the published version analyses **52 PTA neurons** and reports **16.5 sSNVs/year and ~3 indels/year**. Cite the published numbers.

**Competing interests (from the preprint).** Two authors, C. Gawad and J. West, are cofounders/officers of BioSkryb, which makes the PTA (ResolveDNA) kits used — relevant because a central claim is that PTA is cleaner than other chemistries.

## Related

- [[luquette-2019-natcomm]] · [[pta]] · [[40-Topics/brain-somatic-mosaicism]] · [[40-Topics/mosaic-variant-calling]]
