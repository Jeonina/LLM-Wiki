---
type: summary
title: "McLean et al. 2010 — GREAT improves functional interpretation of cis-regulatory regions"
source: "[[00-Sources/papers/GREAT improves functional interpretation of cis-regulatory regions]]"
source_kind: paper
author: "Cory Y. McLean, Dave Bristor, Michael Hiller, Shoa L. Clarke, Bruce T. Schaar, Craig B. Lowe, Aaron M. Wenger, Gill Bejerano (corresponding)"
published: 2010-05-02
ingested: 2026-08-10
doi: "10.1038/nbt.1630"
journal: "Nature Biotechnology"
tags: [GREAT, enrichment-analysis, regulatory-domain, binomial-test, ChIP-seq, cis-regulatory, computational-tool, distal-enhancers]
entities: []
concepts: ["[[cis-regulatory-element]]", "[[enhancer-states]]", "[[chip-seq]]", "[[chromatin-accessibility]]", "[[de-novo-motif-discovery]]"]
topics: ["[[histone-modifications]]", "[[single-cell-atac-seq]]"]
---

**Citation:** McLean et al. (2010) — *GREAT improves functional interpretation of cis-regulatory regions* — *Nature Biotechnology* 28, 495–501. [DOI](https://doi.org/10.1038/nbt.1630)

# McLean 2010 — GREAT

> Gene-based enrichment tools inherited from the microarray era answer the wrong question about a peak set. GREAT assigns each *gene* a regulatory domain, tests enrichment over **genomic regions** with a binomial statistic that accounts for domain length, and thereby uses distal peaks — which are the majority — without the false-positive explosion that nearest-gene assignment causes.

## Key claims

- Restricting to proximal binding (2–5 kb from TSS) **discards over half of observed binding events**.
- The naive fix — assign each peak to its nearest gene(s) — creates a systematic bias toward genes flanked by large intergenic regions. Concretely: GO term "multicellular organismal development" annotates 14% of human genes but the nearest-gene rule assigns **over 33% of the genome** to those genes. A gene-based hypergeometric test expecting 14% therefore reports false enrichment.
- **The binomial test over regions is the fix**: p_π is the fraction of non-gap genome annotated with term π, n is the number of input regions, k_π the number falling in annotated territory. Because long regulatory domains raise p_π proportionally, the test is robust even to incorrect region-to-gene assignments and even with very large domains.
- Default regulatory domain: **basal 5 kb upstream + 1 kb downstream of the TSS regardless of neighbours**, extended to the nearest neighbouring basal domain up to **1 Mb** each direction. Basal size motivated by TSS-proximal histone marks and accessibility; 1 Mb from known long-range enhancer action. Curated experimental domains override the rule for *SHH*, the β-globin locus, and *KIAA1715/EVX2/HOXD10-13*.
- Both tests are run and reported jointly: terms significant by **both** = term-derived enrichment; binomial only = gene-specific enrichment (one gene attracting an unlikely number of peaks); hypergeometric only = regulatory-domain bias. This three-way classification is the practical output.
- 20 ontologies: GO, mouse phenotype, MGI expression, pathways, predicted promoter motifs, TF targets, InterPro domains, gene families, disease associations.
- SRF ChIP-seq in Jurkat: the original study concluded SRF had "no specific physiological roles." GREAT with distal associations recovers **actin cytoskeleton** regulation — SRF's known role as "master regulator of actin cytoskeleton" — which proximal-only analysis (both the original and GREAT restricted to 2 kb) misses entirely. It also recovers the *FOS* family (5 of 6 members), YY1 co-regulation, SRF motif variants as positive controls, and TRAIL / class-I-PI3K pathway links.
- p300 in E11.5 mouse limb (2,105 peaks): DAVID on proximal genes returns only generic "organ development." GREAT's top MGI-Expression terms pinpoint **limb-specific expression at Theiler stage 19 — exactly the tissue and timepoint assayed**. Proximal-only GREAT implicates 7-fold fewer genes and 16-fold fewer peaks, and misses *Gli3*, *Grem1*, *Wnt7a*.
- Limiting extension to 50 kb keeps many terms but loses roughly half of both peaks and genes, with far weaker p-values. Extending 50 kb → 1 Mb captures **more peaks than expected by chance**, which is the paper's evidence that distal associations are biologically real.
- The exact distal rule barely matters — basal-plus-extension, single-nearest-gene and two-nearest-gene rules behave similarly. **Including distal events is what matters; how you assign them is secondary.**

## Methods / evidence

Eight ChIP-seq datasets (SRF, NRSF, GABP, Stat3, p300 in limb/forebrain/midbrain) across human and mouse, each tested six ways: original published analysis or DAVID on proximal genes; GREAT default; GREAT hypergeometric on proximal genes (to control for ontology/gene-set differences rather than statistic differences); GREAT with 50 kb extension; GREAT with one or two nearest genes. That controlled ladder is what isolates the contribution of the statistic from the contribution of the domain definition.

Recovery of the known experimental timepoint from MGI-Expression is the strongest validation — an unbiased positive control the method could have failed.

## Surprising or load-bearing bits

- **The bias GREAT corrects is invisible and directional.** Developmental TF genes sit in gene deserts, so nearest-gene assignment enriches developmental terms in *any* peak set. Since scATAC differential-accessibility peaks are overwhelmingly distal, this is not a historical concern — it is the standing failure mode of "we ran GO on the nearest genes to our differential peaks."
- Applicability is explicitly broader than ChIP-seq: "open chromatin, localized epigenomic markers and similar functional data sets." That is scATAC, scNOMe, single-cell CUT&Tag peak sets.
- The 2010 regulatory-domain heuristic is a **stand-in for 3D contact data** — the authors say so, citing 5C/Hi-C/ChIP-4C as the eventual replacement. It has largely not been replaced in practice; most pipelines still use linear-distance rules despite [[lupianez-2015-tad-disruption|TAD-based]] alternatives and [[pliner-2018-cicero|Cicero]]-style co-accessibility linking. That gap is worth stating in a methods review.
- GREAT's genome builds are **hg18 and mm9**, with GO downloaded in 2009. Enrichments computed today against a 2009 ontology on a two-builds-old genome — still common practice — carry a silent currency problem.
- The gene-specific vs term-derived distinction is a genuinely useful diagnostic that most users ignore: a "significant" term driven by peak clustering at one gene means something different from one spread across many.

## Concepts touched

- [[cis-regulatory-element]] — the regulatory-domain construct is an operational definition of a gene's cis-regulatory territory.
- [[enhancer-states]] — p300 peaks as enhancers; the limb/forebrain/midbrain contrast shows tissue-specific enhancer function is recoverable from peak sets alone.
- [[chromatin-accessibility]] — named as an intended input modality.

## Connections to other sources

- Complementary to [[heinz-2010-homer|HOMER]] (same year): HOMER answers *which factors bind* a peak set, GREAT answers *which genes and functions* it regulates. Most scATAC papers need both.
- Its linear-distance heuristic is superseded in principle by co-accessibility ([[pliner-2018-cicero|Pliner 2018 (Cicero)]]) and domain-aware assignment ([[lupianez-2015-tad-disruption]], [[spielmann-2018-sv-3d-genome]]).
- Downstream of peak calls from [[zhang-2008-macs|MACS]]; used on scATAC peak sets from [[granja-2021-archr]] / [[stuart-2021-natmethods]].
- Appears in this corpus's usage already: [[10-Summaries/zhao-2022-nature]], [[bae-2023-codec]].

## Open questions

- No single-cell-specific version exists. scATAC differential peaks are sparse, cluster-size-dependent and pseudo-bulked — whether GREAT's binomial null holds under that generative process is unaddressed by any source here.
- Whether replacing linear regulatory domains with TAD-bounded or co-accessibility-derived domains materially changes enrichment conclusions is, as far as this corpus shows, unbenchmarked.

## Related

- [[heinz-2010-homer]] · [[cis-regulatory-element]] · [[pliner-2018-cicero|Pliner 2018 (Cicero)]] · [[single-cell-atac-seq]]
