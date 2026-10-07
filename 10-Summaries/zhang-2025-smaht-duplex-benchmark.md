---
type: summary
title: "Zhang et al. 2025 — Benchmarking of duplex sequencing approaches to reveal somatic mutation landscapes"
source: "[[00-Sources/papers/Benchmarking of duplex sequencing approaches to reveal somatic mutation landscapes.pdf]]"
source_quality: full
source_sha256: "40eff28807d11a7d3feb473fb1d55d171878a8d16a904f124a870fba2b4779f5"
source_kind: paper
author: "Yang Zhang*, Vinayak V. Viswanadham*, Michail Andreopoulos*, ... Diane Shao, Christopher A. Walsh, Viktor A. Adalsteinsson, Eunjung Alice Lee, Peter J. Park, Kristin G. Ardlie, Soren Germer, Richard A. Gibbs, Sangita Choudhury (corresponding), Harsha V. Doddapaneni (corresponding), Gilad D. Evrony (corresponding), Chenghang Zong (corresponding), Tim H. H. Coorens (corresponding); the SMaHT Duplex Sequencing Focus Group"
published: 2025-12-15
ingested: 2026-05-12
updated: 2026-10-07
doi: "10.64898/2025.12.12.692823"
journal: "bioRxiv (preprint)"
aliases: [Zhang 2025, SMaHT duplex benchmark, SMaHT Duplex Sequencing Focus Group benchmark]
tags: [duplex-sequencing, benchmarking, SMaHT-network, mutational-signatures, somatic-mosaicism, CODEC, NanoSeq, CompDuplex-seq, HiDEF-seq, ppmSeq, VISTA-seq, COLO829, clonal-architecture, cost-efficacy]
entities:
  - "[[20-Entities/tim-coorens]]"
  - "[[20-Entities/sangita-choudhury]]"
  - "[[20-Entities/gilad-evrony]]"
  - "chenghang zong"
  - "[[20-Entities/peter-park]]"
  - "[[20-Entities/diane-d-shao]]"
  - "[[20-Entities/christopher-walsh]]"
  - "[[20-Entities/smaht-network]]"
concepts:
  - "[[40-Topics/duplex-sequencing]]"
  - "[[30-Concepts/codec]]"
  - "[[30-Concepts/nanoseq]]"
  - "[[30-Concepts/hidef-seq]]"
  - "[[30-Concepts/meta-cs]]"
  - "[[30-Concepts/mutational-signatures]]"
  - "[[30-Concepts/structural-variants]]"
  - "[[40-Topics/somatic-mosaicism]]"
topics:
  - "[[40-Topics/duplex-sequencing]]"
  - "[[40-Topics/somatic-mosaicism]]"
  - "[[40-Topics/mosaic-variant-calling]]"
---

**Citation:** Zhang et al. (2025) — *Benchmarking of duplex sequencing approaches to reveal somatic mutation landscapes* — *bioRxiv (preprint)*, posted 15 Dec 2025. [DOI](https://doi.org/10.64898/2025.12.12.692823)

# Zhang 2025 — SMaHT duplex-sequencing benchmark

> The SMaHT Network compared six duplex-sequencing technologies, nine library variants in all, on the same samples: a low-burden umbilical cord blood control, the COLO829-BLT50 melanoma/lymphoblast mixture (1:49 tumour:normal), and homogenates from six tissues of four donors. Each developer group made its own libraries and ran its own calls; burden, coverage, trinucleotide bias, signatures and cost were then computed with one central pipeline. The methods split into **strand-barcoded** designs (NanoSeq, CompDuplex-seq, VISTA-seq), where the two strands are sequenced as separate clusters and paired in silico, and **physically linked** designs (CODEC, HiDEF-seq, and in part ppmSeq), where one cluster or read reads both strands. They differ widely in genome breadth (30–40% for restriction-enzyme libraries, near-complete for random fragmentation), duplex recovery and cost per interrogated base. Even so, burden estimates and de novo signatures largely agree, and the signatures cluster by sample, not by assay. The paper's second half treats duplex data as a clonal-architecture probe. Combined with ~1000X bulk WGS, shallow duplex calls in COLO829-BLT50 resolve seven clonal subpopulations, including clones at VAFs far below bulk-WGS resolution and an unexpected lymphocyte expansion that arose when the mixture was made.

## Key claims

- **Design.** Nine libraries: NanoSeq-Hpy (HpyCH4V restriction digest) and NanoSeq-MBN (sonication + mung bean nuclease); CompDuplex-seq (Tn5 fragmentation, then restriction-enzyme cutting of the transposase sites); VISTA-seq (engineered strand-specific Tn5, extended from META-CS to bulk and micro-bulk input of "≈50 nuclei"); CODEC-ddBTP, CODEC-DRv1 and CODEC-DRv2 (three end-repair strategies); HiDEF-seq v3 (PacBio Revio; "a new version of HiDEF-seq with whole-genome coverage" using random ~4 kb fragmentation and blunt, non-A-tailed ligation); and ppmSeq (Ultima UG100 emulsion PCR). Input DNA ranged from 20 ng (CODEC) and 20–50 ng (CompDuplex-seq) to 250 ng (ppmSeq).
- **Cord-blood burden.** NanoSeq-Hpy, NanoSeq-MBN, CompDuplex-seq and HiDEF-seq measured "~1×10⁻⁸ mutations per bp": 56.9 (95% CI 40.2–76.3), 87.4, 67.8 and 67.9 mutations per cell. VISTA-seq, CODEC-ddBTP and ppmSeq measured "~2.6×10⁻⁸": 172.1, 184.4 and 158.1 per cell. The authors put this down to single-digit count noise in a near-empty sample and say burdens "largely remain within the 10⁻⁸ scale".
- **COLO829 and tissues.** Most methods gave "~3.5–4.0×10⁻⁷" in COLO829-BLT50. ppmSeq gave about half: its calling workflow infers somatic status within the sample (trinucleotide-context FDR plus pattern recognition) instead of filtering against a matched normal, so true tumour variants were relabelled as clonal and removed. Across tissues the methods were "largely concordant". ST002-Lung (74 y) was the outlier for between-method spread. Brain homogenates gave 1309.2 mutations per cell at 22 y (ST003) and 2258.5 at 73 y (ST004), "averaging 18.6 mutations per cell per year across methods". The authors conclude that "exposure history, tissue type, and age rather than platform dominate variability."
- **Coverage follows fragmentation.** Per-base duplex coverage was modelled with a zero-inflated negative binomial, which fitted better than zero-inflated Poisson for every library. Restriction-enzyme libraries (NanoSeq-Hpy, CODEC-ddBTP) reached only "narrower genomic breadth (30-40%)" with over-dispersed depth. Randomly fragmented libraries approached Poisson behaviour.
- **Trinucleotide bias.** NanoSeq-MBN, CODEC-DRv1/2 and ppmSeq had the lowest composition bias. Restriction libraries were depleted at the HpyCH4V motif. CompDuplex-seq showed little bias on cell-line DNA but more on tissue, attributed to nicks from mechanical homogenisation. VISTA-seq had the highest bias, attributed to amplification. HiDEF-seq had uniform coverage but context imbalance among passing bases, attributed to PacBio error preferences. These biases had "minimal impact" on the COLO829 spectrum.
- **Signatures agree.** ppmSeq multi-read calls added assay-specific components (Sig. 6–8 in the full catalogue), so ppmSeq was left out of de novo discovery. Without it, MuSiCal (NMF) and HDP independently found the same five signatures, and fitting showed "no assay-specific signatures"; samples clustered by identity. Liver (ST001) carried an SBS12-like and liver-specific signature, and the 74-year-old lung carried SBS4 (tobacco). COLO829 Sig 1 decomposed into UV signatures (SBS7a/7b/38), SBS9 and SBS18. Per-assay COSMIC fits to COLO829 had cosine similarities of 0.93–0.99.
- **Duplex calls are mostly not bulk-WGS clonal calls.** No more than 10% of bulk-WGS truth-set SNVs from any tissue overlapped the pooled duplex calls (≤5% except ST002-Lung). Fewer than 0.5% of the ~2,000–25,000 duplex calls per tissue overlapped the truth set. For COLO829-BLT50, about 12% of truth-set calls (~4,300 SNVs) were recovered, matching simulations. Of 450 multi-molecule BLT50 mutations, 17.56% (n = 79) were in the truth set with the expected UV spectrum. The other 82.44% (n = 371) had a distinct C>A/T>G-rich spectrum.
- **Seven clonal subpopulations in BLT50.** A beta-binomial mixture fitted to ~1000X bulk-WGS pileups of duplex sites in BLT50, COLO829T and COLO829BL found seven subpopulations, represented "at relatively even proportions" by every technology. Subpopulations 1–4 (SBS7a/b, SBS38; VAF <4%) carry the tumour truth set and make up 51.8% of duplex mutations. **25.8% of BLT50 duplex mutations were absent from bulk WGS**, implying detection "at clonal VAFs below 0.6% (3 in 5000 cells) and as low as 0.002% (approximately 2 in 100,000 cells)".
- **An acquired lymphocyte expansion.** Subpopulations 5/6 (SBS9 + SBS18) trace to blood subpopulations I–III. These sit at VAF <1% in blood bulk WGS but at "6-8% in BLT50's bWGS", whereas dilution predicts ~0.098%. This points to a B-cell clonal expansion during the creation of BLT50. Multi-duplex support alone picked it up: 64.8% of multi-duplex non-truth-set mutations fell in 5/6 (vs 8.8% in 1–4), and 79% of those traced to blood I–III.
- **Efficiency and cost** (USD per billion interrogated bp, platform list prices). Strand-barcoded NanoSeq and CompDuplex-seq had "~50–60%" duplex recovery on high-integrity DNA. CompDuplex-seq costs were bimodal: $50 on cell-line DNA and $150 on nicked tissue DNA. VISTA-seq cost $96.1 and NanoSeq-MBN $76.24. CODEC was ≈$126, with "productive duplex recovery" of ~25–36%. HiDEF-seq was ≈$220, with ~65% of molecules retained after filtering. ppmSeq was ≈$15.4, which "reflects the interplay between platform pricing and consensus yield".
- **Stated limits of duplex sequencing.** It cannot yet detect CNVs or SVs ("chimeric reads currently overwhelm the rate of true somatic structural variants"), and "currently only the Illumina-based methods work for indel detection".
- **Method choice** follows the question: HiDEF-seq for single-strand damage plus double-strand mutations; VISTA-seq for low input down to single cells; NanoSeq with bait capture for selection; CompDuplex for single-nucleus pairing with total-RNA profiling; CODEC for cfDNA and Methyl-CODEC; ppmSeq for ultra-deep MRD liquid biopsy.

## Methods / evidence

Shared biological inputs went to developer labs, and each lab ran library prep through variant calling "under fully optimized conditions". Pipelines: CODECsuite on Terra; a joint CompDuplex–NanoSeq pipeline; a new HiDEF-seq v3.0 Nextflow pipeline; a pre-pe/lianti-derived VISTA-seq caller for pooled molecules; and a new ppmSeq SNVQ-based caller with 10% FDR, restricted to Ultima high-confidence regions (~93% of the genome). All data were aligned to GRCh38 without decoys. Central metrics: interrogated base pairs (IBP), the sum of callable bases over duplex molecules, used as the denominator for burden and cost. Cost efficacy is sequencing cost per IBP at the saturation point where extra depth stops improving recall, with each pipeline tuned for "consistent accuracy on the low-mutation-burden cord blood reference". Other metrics were ZINB coverage fits, 32-context trinucleotide enrichment against masked hg38, and strand-resolved single-strand-event rates. From those rates the authors derive a random-coincidence error floor, which they say is a lower bound on the false-positive rate, not the full false-positive burden. Signatures were extracted with MuSiCal (COSMIC v3.4 tissue-restricted NNLS refit) and with HDP. Clonal analysis used pileup thresholds tuned by AUROC (sensitivity ~75% Illumina and 92% Ultima; false-positive rate ~7% and 5%), then a beta-binomial EM mixture with bootstrapping balanced across assays. Data: dbGaP phs004193.

Weight: the strongest equal-footing duplex comparison in the wiki, with shared samples, developer-optimised execution and central metrics. But the "concordance" is at the order-of-magnitude level, and there is no orthogonal ground truth for private (non-clonal) mutations. Cord-blood estimates split about 2.6-fold into two groups of methods. The clonal analysis rests on a single engineered cell-line mixture. Several patent and equity interests in the benchmarked methods are declared (CODEC, HiDEF-seq, CompDuplex-seq). (synthesis)

## Limitations

**Authors' own:**
- Burdens in cord blood are noisy because of very low counts. ppmSeq underestimates COLO829 burden, and its calling "is actively underway".
- Trinucleotide-context bias is "non-negligible" for some methods, though the authors argue it did not distort signatures.
- The random-error model is a lower bound on false positives. Systematic and context-coupled errors are not captured.
- Duplex sequencing does not yet detect CNVs or SVs, and indel calling works only on Illumina-based methods.
- Validating VAFs of duplex-detected clones still needs deep or targeted sequencing. The non-truth-set subpopulation 7 was not analysed further because its fit was poor.

**Reviewer notes:**
- The text and figures disagree on duplex recovery. The text gives VISTA-seq "30.7%" and CODEC "~25–36%", but the Fig. 2A summary table and Fig. 6A show VISTA-seq and CompDuplex-seq near 20%, and CODEC variants at about 43–48%. The text also groups CompDuplex-seq with NanoSeq at "~50–60%". The definitions may differ, but the paper does not reconcile them. (synthesis)
- Each pipeline was tuned on the same cord-blood reference before cost was computed, and each developer ran its own method. Cost and sensitivity therefore reflect developer-optimised operating points, not what a naïve user would get. (synthesis)
- The tissue panel is six homogenates from four donors, and only some methods ran on every sample (ppmSeq, for example, was absent from some brain comparisons). Tissue-level concordance therefore rests on few samples per method. (synthesis)

## Surprising or load-bearing bits

- **Platform matters less than biology for burden and signatures.** This is the main licence for comparing SMaHT datasets produced on different duplex chemistries. ppmSeq is the exception: its in-sample somatic inference halves the tumour burden and adds spurious signature components. Naive pooling across platforms is therefore unsafe until calling pipelines converge. (synthesis)
- **Shallow duplex sequencing as a clone detector.** Multi-molecule support makes a duplex mutation clonal without any bulk data. In BLT50 that alone uncovered a lymphocyte expansion that nobody had designed into the benchmark sample. It also implies that the widely used COLO829-BLT50 reference contains an emergent clone, which other benchmarks should account for. (synthesis)
- **Duplex and bulk WGS see different mutations.** Bulk WGS captures early or heavily expanded clones, while duplex sequencing captures late, often tissue-specific processes such as smoking in lung and the liver signature. The authors note that this matches SMaHT single-cell data ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]).
- **Single-strand events are asymmetric across complementary contexts**, and this pushes the random duplex-coincidence floor far below single-strand event rates (Fig. S3).

## Entities mentioned

- [[20-Entities/smaht-network]] — the consortium and its Duplex Sequencing Focus Group run the study, and data go through the SMaHT Data Analysis Center.
- [[20-Entities/tim-coorens]] — co-corresponding author; signature analysis, study design and writing.
- [[20-Entities/gilad-evrony]] — co-corresponding author; HiDEF-seq v3 and its pipeline.
- [[20-Entities/sangita-choudhury]] — co-corresponding author; study design and supervision.
- [[20-Entities/peter-park]] — supervision; MuSiCal comes from the Park lab.
- [[20-Entities/christopher-walsh]], [[20-Entities/diane-d-shao]] — supervision (Boston Children's).
- Chenghang Zong (CompDuplex-seq, VISTA-seq) and Harsha Doddapaneni (NanoSeq-MBN at Baylor) are co-corresponding authors; neither has an entity page.

## Concepts touched

- [[40-Topics/duplex-sequencing]] — taxonomy of strand-barcoded vs physically linked designs, with IBP as a chemistry-agnostic denominator.
- [[30-Concepts/nanoseq]] — two versions: restriction-based Hpy (~35% breadth) and sonication/mung bean MBN (near-genome-wide).
- [[30-Concepts/codec]] — three end-repair versions. Whole-genome DRv1/2 libraries reduce trinucleotide bias, and ddBTP is restriction-limited.
- [[30-Concepts/hidef-seq]] — v3 adds whole-genome coverage. Highest duplex efficiency and highest cost.
- [[30-Concepts/meta-cs]] — VISTA-seq extends META-CS's engineered-Tn5 strand encoding to pooled multi-allelic input.
- [[30-Concepts/mutational-signatures]] — cross-assay signature robustness, with MuSiCal and HDP agreeing.
- [[30-Concepts/structural-variants]] — explicitly outside current duplex capability.

## Connections to other sources

- SMaHT single-cell companion: [[10-Summaries/luquette-2025-pta-duplex-mosaicism]]. The authors say their burdens and signatures agree with it. Duplex sequencing gives population-average burdens from one sample, and single-cell sequencing needs enough cells to be representative.
- Method origins: [[10-Summaries/schmitt-2012-pnas]] and [[10-Summaries/kennedy-2014-duplex-protocol]] (duplex sequencing), [[10-Summaries/abascal-2021-nanoseq]] (NanoSeq), [[10-Summaries/bae-2023-codec]] (CODEC), [[10-Summaries/liu-2024-hidef-seq]] (HiDEF-seq) and [[10-Summaries/xing-2021-meta-cs]] (META-CS → VISTA-seq).
- Cited as a newer duplex variation that was not benchmarked: [[10-Summaries/nandi-2025-udseq]].
- Same COLO829-BLT50 sample: [[10-Summaries/kriz-2025-duplex-multiome]] also finds lymphoblast subclones outside the truth set with an SBS18-like spectrum, which it attributes to culture. Here those variants are resolved into an SBS9/SBS18 lymphocyte expansion. The two papers independently show that this reference mixture is not clonally static. (synthesis)
- Brain burden: 18.6 mutations per cell per year from bulk duplex homogenates. This is consistent with the per-neuron rate of ~16.5 sSNVs/year from PTA+SCAN2 ([[10-Summaries/luquette-2022-neuron-scan2-indels]]), though homogenates mix cell types. (synthesis)

## Open questions

- Do the cord-blood burden groups (~57–88 vs ~158–184 per cell) reflect residual false positives in some methods, or noise? The paper attributes the split to count noise but does not test this. (synthesis)
- How well do methods agree on private, non-clonal mutations at the level of individual sites, rather than burdens and spectra?
- Will ppmSeq's in-sample somatic calling converge with matched-normal pipelines? The authors say further development "is actively underway".
- How do UDSeq ([[10-Summaries/nandi-2025-udseq]]) and single-cell-compatible duplex designs such as Duplex-Multiome ([[10-Summaries/kriz-2025-duplex-multiome]]) compare on the same reference materials? (synthesis)

## Related

- [[40-Topics/duplex-sequencing]] · [[40-Topics/somatic-mosaicism]] · [[40-Topics/mosaic-variant-calling]] · [[30-Concepts/codec]] · [[30-Concepts/nanoseq]] · [[30-Concepts/hidef-seq]] · [[30-Concepts/meta-cs]] · [[20-Entities/smaht-network]]
