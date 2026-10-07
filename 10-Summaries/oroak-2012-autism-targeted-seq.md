---
type: summary
title: "O'Roak et al. 2012 — Multiplex targeted sequencing identifies recurrently mutated genes in autism spectrum disorders"
source: "[[00-Sources/papers/Multiplex Targeted Sequencing Identifies Recurrently Mutated Genes in Autism Spectrum Disorders]]"
source_quality: full
source_sha256: "9cccbe7e9e59e9a3aeddaa1e1fd054640e63725a36a90922e70842e54c90cbcb"
source_kind: paper
author: "Brian J. O'Roak, Laura Vives, Wenqing Fu, Jarrett D. Egertson, Ian B. Stanaway, Ian G. Phelps, Gemma Carvill, Akash Kumar, Choli Lee, Katy Ankenman, Jay Shendure, Evan E. Eichler (corresponding)"
published: 2012-11-16
ingested: 2026-05-18
updated: 2026-10-07
doi: "10.1126/science.1227764"
journal: "Science"
tags: [autism, ASD, targeted-sequencing, molecular-inversion-probes, MIP, de-novo-mutation, germline, mutation-burden, CHD8, DYRK1A, Simons-Simplex-Collection, Eichler-lab, Shendure-lab]
entities: ["[[20-Entities/jay-shendure]]"]
concepts:
  - "[[30-Concepts/autism-spectrum-disorder]]"
  - "[[30-Concepts/copy-number-variation]]"
  - "[[30-Concepts/post-zygotic-variation]]"
topics:
  - "[[40-Topics/somatic-mosaicism]]"
  - "[[40-Topics/brain-somatic-mosaicism]]"
---

**Citation:** O'Roak et al. (2012) — *Multiplex targeted sequencing identifies recurrently mutated genes in autism spectrum disorders* — *Science* 338:1619. [DOI](https://doi.org/10.1126/science.1227764) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/23160955/)

# O'Roak et al. 2012 — autism MIP-based resequencing

> Exome studies of autism (ASD) had found hundreds of candidate genes from *de novo* mutations, but almost every gene was hit only once, and over 900 sequenced trios were not enough to make any single gene a definitive risk factor. O'Roak et al. built a modified **molecular inversion probe (MIP)** workflow costing **less than $1 per gene per sample** and used it to resequence **44 candidate genes in 2,446 Simons Simplex Collection (SSC) probands**. They found **27 *de novo* mutations in 16 genes** and, with a locus-specific mutation-rate model, showed significant *de novo* burden in six genes (*CHD8*, *DYRK1A*, *GRIN2B*, *TBR1*, *PTEN*, *TBL1XR1*). Together these six account for **~1% (24/2,573)** of sporadic ASD in the combined MIP and exome data. The paper also links *CHD8* to macrocephaly and *DYRK1A* to microcephaly, and finds that the mutations cluster in a β-catenin–chromatin-remodeling protein network. This is a germline (*de novo*, blood-DNA) study, not a mosaicism study.

## Key claims

- **Assay performance.** The modified MIP method combines new probe-design algorithms, an automatable low-input workflow and heavy sample multiplexing. Validation across several probe sets gave **99% sensitivity and 98% positive predictive value** for SNVs at well-covered positions, which were **92 to 98% of targeted bases**. Reagent cost was **under $1 per gene per sample**.
- **Cohort and targets.** Two probe sets, ASD1 (6 genes) and ASD2 (38 genes), were run on **2,494 SSC probands**. Requiring successful capture with both left **2,446 probands**: 2,364 with MIP data only and 82 that also had exomes. The 44 genes were chosen from **192 exome candidates** for disruptive mutations, syndromic-autism links, overlap with neurodevelopmental CNV loci, structural similarity or neuronal expression. **23 of the 44** sit in a 49-member β-catenin–chromatin-remodeling PPI network or an expanded 74-member network.
- **Discovery.** Candidate sites were filtered against other cohorts, including non-ASD exomes and MIP resequencing of **762 healthy non-ASD individuals**. Parents were then MIP-resequenced and putative *de novo* sites confirmed by trio Sanger sequencing. This gave **27 *de novo* mutations in 16 of the 44 genes**. **Six** of these had been missed in probands who were already exome-sequenced, which the authors take as evidence that MIPs are more sensitive.
- **Severe mutations are enriched.** Coding indels, nonsense and splice-site mutations made up **17/27 (0.63)** of the *de novo* events. That is four times the expected proportion for random *de novo* mutations (**0.16**, binomial *P* = 4.9 × 10⁻⁸). The abstract's "59% … truncate proteins or disrupt splicing" (16/27) leaves out the single in-frame amino-acid deletion (*CHD8* p.His2498del) that the severe class counts.
- **Burden across the 44 genes.** The authors observed **27 *de novo* mutations against a mean expected 5.6** (simulated *P* < 2 × 10⁻⁹). The excess came from the severe class: **17 observed against 0.58 expected** (*P* < 2 × 10⁻⁹). The *CHD8* count and the 44-gene total were never reached in **5 × 10⁸ simulations**. For *CHD8*, the Poisson probability of seven or more severe mutations, given the simulation mean of 0.0153, is **3.8 × 10⁻¹⁷**.
- **Six significant genes.** *CHD8*, *GRIN2B*, *DYRK1A*, *PTEN*, *TBR1* and *TBL1XR1* pass α = 0.05 after Holm-Bonferroni correction. *TBL1XR1* is only borderline under plain Bonferroni. Five of the six are in the β-catenin–chromatin-remodeling network. Table 1 lists 24 events: *CHD8* 9 (7 found by MIP), *GRIN2B* 4, *DYRK1A* 3, *PTEN* 3, *TBR1* 3 and *TBL1XR1* 2. *CHD8* alone accounts for **0.35% (9/2,573)** of probands.
- **The network concentrates the hits.** **16 of 17** severe mutations fall in the 74-member PPI network, which holds only 23 of the 44 genes (binomial *P* = 0.0002). So do **21 of 27** mutations overall (*P* = 0.004).
- **Robustness.** The authors used the highest available empirical coding mutation rate. Results held, except for *TBL1XR1*, when that rate was doubled or the upper 95% CI of each locus-specific rate was used. They also held whether parameters came from rare segregating variants, from *de novo* mutations in unaffected siblings, or from a genome-wide *de novo* sequence-composition model (Kong 2012). Exomes from non-ASD individuals agreed (table S14).
- **Inherited variants show weak trends.** **23 inherited severe variants** were validated, and two of their carriers also have *de novo* 16p11.2 duplications. Counting *de novo* and inherited events together, severe variants were twice as common in probands as in MIP-sequenced controls (Fisher *P* = 0.083). Severe variants were **not transmitted to 14 of 20** unaffected siblings (binomial *P* = 0.058). The authors call these "modest trends" that need larger cohorts.
- **Phenotype.** All carriers met strict gold-standard autism criteria and had no obvious dysmorphology or recurrent comorbidity. Mean NVIQ was **58.3**, in the intellectual-disability range, but *CHD8* carriers ranged from profound impairment to average (mean **62.2**, range **19 to 98**).
- **Reciprocal head size.** Age- and sex-normalised head-circumference Z scores were larger in *CHD8* truncating/splice carriers (**n = 8**, two-sided permutation *P* = **0.0007**). *De novo* *CHD8* mutations are present in **~2% of macrocephalic (HC > 2.0) SSC probands (n = 366)**. *DYRK1A* carriers had smaller heads (**n = 3**, *P* = **0.0005**). Family-based comparisons (Fig. 2C–D) back this reciprocal pattern, and macrocephaly was also seen with *PTEN* mutations.
- **CNV calling as a by-product.** Most MIPs behaved reproducibly, so copy-number changes at targeted genes could be called, including several inherited duplications (figs. S11–S12). Several GC-rich targets needed probe rebalancing to even out capture.

## Methods / evidence

Targeted capture with modified MIPs (the Turner 2009, Porreca 2007 and Krishnakumar 2008 lineage) and multiplexed Illumina sequencing of blood DNA from SSC simplex families. Variants were filtered against external exomes and 762 MIP-sequenced controls, then confirmed by MIP resequencing of parents and Sanger sequencing of the trio. CNVs were inferred from probe read depth. The burden model simulates expected *de novo* counts per locus from three inputs: an overall coding mutation rate, locus-specific relative rates estimated from human–chimpanzee fixed differences (fig. S14, table S13), and codon structure. It then scores the chance of at least *x* events with at least *y* in the severe class. Head-size tests are two-sample permutation tests on HC Z scores. Raw data: NDAR collection NDARCOL1878.

Weight: the discovery-and-confirmation pipeline and the simulation-based burden test are strong for the six-gene result. Every *de novo* call is Sanger-confirmed, and the tests hold up under conservative rate choices. The clipped source has only the main text: Materials and Methods, supplementary text, figs. S1–S14 and tables S1–S18 are referenced but absent, so probe-design, rebalancing and model details cannot be checked here. The head-size associations rest on 8 and 3 carriers, and the inherited-variant comparisons are not significant. (synthesis)

## Limitations

**Authors' own:**
- SSC was built for simplex families, and its probands have higher cognitive function than other ASD cohorts, so it is unknown how the findings carry over to other cohorts.
- The data implicate specific loci but cannot show whether the *de novo* mutations are sufficient to cause ASD (tables S16, S18).
- Locus-specific *de novo* expectations cannot be set empirically from control trios at these frequencies, so a probabilistic model stands in.
- The inherited-variant trends (P = 0.083, P = 0.058) need cohorts larger than any that existed.
- GC-rich targets needed substantial rebalancing, and sensitivity figures apply only at well-covered positions (92–98% of targeted bases).

**Reviewer notes:**
- Candidate genes came from earlier exome hits in overlapping SSC probands, and those discovery events are counted in the combined 24/2,573 frequency. The burden test is framed on "additional" events from the MIP screen, but the ~1% estimate mixes discovery and replication events. (synthesis)
- Blood-DNA trio calling with population and control filters is tuned to germline heterozygous events. Low-fraction post-zygotic mosaic variants would be under-called or excluded, so the paper says nothing about mosaic contributions to ASD. (synthesis)
- The 44 genes were enriched for β-catenin–chromatin-remodeling network members during selection (23/44), so the network enrichment among hits is partly shaped by which genes were chosen. (synthesis)

## Surprising or load-bearing bits

- **Targeted replication over more exomes.** With the target space narrowed to 44 genes, about 2,500 probands at under $1 per gene per sample turned singleton exome hits into significant genes. Locus-specific burden statistics, not genome-wide discovery, did the implicating.
- ***CHD8* is the standout.** Nine carriers, a severe-class count never matched in 5 × 10⁸ simulations, and a macrocephaly subphenotype present in ~2% of macrocephalic probands. This is the founding evidence for *CHD8* as a high-confidence ASD gene. (synthesis)
- **Reciprocal growth phenotypes.** *CHD8* goes with large heads and *DYRK1A* with small heads, which points to brain-growth regulation as one axis of ASD subtypes.
- **MIPs beat exomes on sensitivity.** Six *de novo* events missed by exome sequencing in the same probands were recovered by MIPs.

## Entities mentioned

- [[20-Entities/jay-shendure]] — co-senior author; the MIP capture lineage (Turner 2009) comes from his lab.

## Concepts touched

- [[30-Concepts/autism-spectrum-disorder]] — six genes with significant *de novo* burden explain ~1% of sporadic ASD, plus *CHD8*/*DYRK1A* head-size subphenotypes.
- [[30-Concepts/copy-number-variation]] — MIP read depth gives CNV calls at targeted genes; two carriers of inherited severe variants also have *de novo* 16p11.2 duplications.
- [[30-Concepts/post-zygotic-variation]] — this is the germline *de novo* counterpart. It does not address post-zygotic or mosaic events, which later brain-mosaicism work adds. (synthesis)

## Connections to other sources

- Germline baseline that later ASD mosaicism work builds on: [[10-Summaries/bizzotto-2022-brain-mosaicism-review]] reports mosaic missense mutations in intolerant genes in 0.8–1.3% of probands, the same order as the ~1% here from six germline genes. (synthesis)
- Single-neuron somatic-variation context: [[10-Summaries/lodato-2015-science]], [[10-Summaries/lodato-2017-aging-neurons]], [[10-Summaries/mcconnell-2017-science]].
- Methods lineage: the Shendure lab's combinatorial-indexing work shares an author (O'Roak) with [[10-Summaries/mulqueen-2018-sci-met]].

## Open questions

- Do the six genes hold up in cohorts with lower cognitive function or in multiplex families, given SSC's simplex design and higher-functioning probands?
- What share of *de novo* events in these genes would turn out to be parental gonadal or proband post-zygotic mosaicism if sequenced more deeply? (synthesis)
- Does the *CHD8*-macrocephaly and *DYRK1A*-microcephaly pattern replicate with more than 8 and 3 carriers?

## Related

- [[30-Concepts/autism-spectrum-disorder]] · [[30-Concepts/copy-number-variation]] · [[30-Concepts/post-zygotic-variation]]
- [[40-Topics/somatic-mosaicism]] · [[40-Topics/brain-somatic-mosaicism]]
- [[10-Summaries/bizzotto-2022-brain-mosaicism-review]] · [[10-Summaries/lodato-2017-aging-neurons]]
