---
type: summary
title: "Kriz 2025 — Cell-type-specific patterns and consequences of somatic mutation in development and aging brain (Duplex-Multiome)"
source: "[[00-Sources/papers/Cell-type-specific patterns and consequences of somatic mutation in development and aging brain.pdf]]"
source_quality: full
source_sha256: "6fa4bd25e85bc9db00134fbf251f7953c77b1a79138cef3414d2ad554616b476"
source_kind: paper
author: "Andrea J. Kriz†, Shulin Mao†, Diane D. Shao, Daniel A. Snellings, Rebecca E. Andersen, Guanlan Dong, Chanthia C. Ma, Hayley E. Cline, August Yue Huang (corresponding), Eunjung Alice Lee (corresponding), Christopher A. Walsh (corresponding)"
published: 2025-06-01
ingested: 2026-05-12
doi: "10.1101/2025.05.30.656844"
journal: "bioRxiv (preprint)"
aliases: [Kriz 2025, Duplex-Multiome, Andrea 2025, Walsh-Lee Duplex-Multiome]
tags: [somatic-mosaicism, joint-assay, duplex-sequencing, snATAC-seq, snRNA-seq, 10x-multiome, brain, aging, glia, clonal-sSNV, ssDNA-damage, ASD, foundational, gap-closing]
entities:
  - "[[20-Entities/christopher-walsh]]"
  - "[[20-Entities/diane-d-shao]]"
concepts:
  - "[[30-Concepts/scatac-seq]]"
  - "[[30-Concepts/scrna-seq]]"
  - "[[30-Concepts/joint-single-cell-multi-omics]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/tn5-tagmentation]]"
  - "[[30-Concepts/mutational-signatures]]"
  - "[[30-Concepts/lineage-tracing]]"
  - "[[30-Concepts/allele-dropout]]"
  - "[[30-Concepts/single-cell-variant-calling]]"
  - "[[30-Concepts/autism-spectrum-disorder]]"
topics:
  - "[[40-Topics/somatic-mosaicism]]"
  - "[[40-Topics/brain-somatic-mosaicism]]"
  - "[[40-Topics/duplex-sequencing]]"
  - "[[40-Topics/single-cell-multiomics]]"
  - "[[40-Topics/single-cell-lineage-tracing]]"
created: 2026-05-12
updated: 2026-10-07
---

**Citation:** Kriz et al. (2025) — *Cell-type-specific patterns and consequences of somatic mutation in development and aging brain* — *bioRxiv (preprint)*, posted 1 June 2025. [DOI](https://doi.org/10.1101/2025.05.30.656844) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/40502142/)

# Kriz 2025 — Duplex-Multiome

> Duplex-Multiome adds strand tagging to the 10x Single Cell Multiome ATAC + Gene Expression protocol. In each nucleus, both strands of every Tn5-tagmented ATAC fragment carry a strand barcode, so somatic SNVs (sSNVs) can be called by duplex consensus from the same nucleus that yields snATAC and snRNA profiles. Duplex consensus cuts error ">10,000-fold" and removes the SBS45 sequencing-artefact signature. sSNVs are seen only in accessible chromatin and only sparsely per nucleus. Burdens are therefore estimated **per cell type**, by pooling thousands of nuclei in a simulation-based likelihood model, and then corrected to genome-wide rates with open-chromatin enrichment factors learned from PTA scWGS. The paper benchmarks the method on the SMaHT COLO829-BLT50 mixture and then profiles >51,400 brain nuclei: nine neurotypical donors aged 0.2–82.7 years (>43,300 nuclei), a 21-week prenatal pilot and two ASD cases. It reports cell-type-specific ageing rates, including astrocytes and inhibitory neurons that scWGS had not assayed, and signature depletion in open chromatin. It finds an excess of low-VAF clonal sSNVs in glia of some aged brains, and two non-coding clonal variants whose presence tracks expression of nearby genes.

## Key claims

- **Error suppression.** Without duplex consensus, raising calling stringency lowers the error rate only to 10⁻⁵, and the residual calls match COSMIC SBS45, a sequencing-artefact signature. Requiring even one read per strand removes SBS45 and matches the error rate of ten same-strand reads without duplex consensus. More reads per strand lower it further. Standard calls need "a6s3": ≥6 supporting reads, ≥3 per strand, base quality >30 and MapQ >20.
- **COLO829-BLT50 benchmark** (two replicates). Annotation found 4,989 B-lymphoblasts (97.5%) and 128 tumour cells (2.5%), the expected ratio. Duplex-Multiome recovered each truth-set spectrum: the BL spectrum when the tumour bulk WGS was used as the germline filter, and the tumour SBS7a-like spectrum when the mixture's bulk WGS was used. Tumour clonal variants at VAF >25% overlapped the truth set at 92% (33 of 36, Fig. 2d). This "92%" is what the abstract calls precision for "sSNVs present in 2% of cells". A shared-sSNV graph split tumour cells (cluster 1) from 14 lymphoblast subclusters, which were defined by culture-acquired variants absent from the truth set and showing an SBS18 (oxidative) spectrum.
- **Burden estimation.** For each cell type, a grid search over discrete-Gaussian burden distributions is simulated through the observed callable regions and sensitivity, and the best match by Poisson likelihood is chosen. Clusters need >200 cells and >20 Mb callable. A small "duplex error" term from mis-barcoded read families (<1%) is modelled explicitly.
- **Open-chromatin correction.** scWGS sSNVs from neurons are enriched in Duplex-Multiome-covered regions, and those from oligodendrocytes are slightly depleted. After correction, ENs accumulate **15.05 ± 3.15 sSNVs/year** and OLs **32.34 ± 2.39 sSNVs/year** genome-wide (P = 6.61×10⁻⁵). Both rates are "highly concordant with published neuronal and OL scWGS data".
- **Cell-type rates** (per bp per year, in covered regions):
  - OLs (6.23 ± 0.40)×10⁻⁹ vs OPCs (5.04 ± 1.36)×10⁻⁹, P = 0.12. The authors infer that faster OPC division "does not greatly contribute" to the rate.
  - Astrocytes (7.24 ± 1.05)×10⁻⁹ vs microglia (2.10 ± 0.53)×10⁻⁹, P = 0.001. The microglial rate is "surprisingly" below that of HSCs.
  - ENs (3.39 ± 0.76)×10⁻⁹ vs INs (4.45 ± 0.73)×10⁻⁹, P = 0.094.
  - Upper-layer ENs (4.36 ± 1.01)×10⁻⁹ vs deep-layer ENs (3.09 ± 0.10)×10⁻⁹, P = 0.03.
  - The authors call upper-layer ENs and astrocytes "the EN and glial cell types most susceptible to somatic mutagenesis".
- **Signatures in open chromatin.** EN and OL spectra are dominated by SBS5, with SBS16 in ENs and SBS1 in OLs, as in scWGS. SBS19 appeared in ENs but not OLs, possibly a sampling effect. SBS1 is about 2-fold depleted in covered regions, exactly as the scWGS distribution predicts. SBS16 (A[T>C], transcribed strand) is *expected* to be enriched in covered regions but contributes only a minor share. The authors read this as raising "the possibility that SBS16-like A[T>C] sSNVs have the capability of reducing chromatin accessibility". IN spectra resemble ENs, and astrocyte spectra resemble OLs.
- **Single-strand damage.** About 1% of strand-2 products pick up a second strand-2 barcode, which allows same-strand consensus. Single-strand damage calls resemble SBS30, consistent with HiDEF-seq. They do not correlate with age, so the authors attribute them to post-mortem or library-prep damage.
- **Clonal sSNVs.** A relaxed "a2s0" mode keeps variants shared by ≥3 cells, with a relaxed germline filter (bulk VAF <10%), an MCMC Bayesian germline model and realignment. It found up to 27 clonal sSNVs per sample, 332 candidates in total. Amplicon-seq validated >90% of those at VAF ≥0.01 (9/10 and 6/6) and 71% of those below 0.01 (25/35 and 28/39). Detected VAFs reached 0.001, against a ~0.02 threshold for ultra-deep WGS. Clonal sSNVs were enriched for CpG C>T, a signature of dividing progenitors.
- **Glia carry more late clonal sSNVs.** Across all VAFs, neuron and glia rates did not differ (P = 0.18). For low-VAF clonal sSNVs (VAF <0.01), glia had a higher rate (P = 0.036). An 82.7-year-old brain (UMB5823) had an elevated clonal rate, mainly in glia (P = 0.027). One variant (chr7:155297830 T>C) appeared only in the OL lineage, in 5 of 823 covered cells. The authors conclude that clonal sSNVs in aged brain arise "in aging glia without substantial contribution from blood cell clones". This settles a question that Bae 2022 could not resolve.
- **ASD enhancer variant.** In ASD case AN06365, the known clonal enhancer variant chr1:205284910 T>C (from Rodin et al. 2021) tracked lower *NUCKS1* expression within carrier cells (P = 0.025). Expression was also lower than in nine neurotypical brains (P = 3.1×10⁻⁴). Duplex-Multiome detected the variant in OLs, astrocytes and microglia but not neurons, yet Amplicon-seq found it in ~6% of NeuN+ neurons. The authors explain this by low neuronal accessibility at the locus, which is also low in non-carrier brains. Against a second ASD brain, *NUCKS1* was lower in all cell types (significant in ENs and INs), *CDK18* only in OLs and *MFSD4A* only in ENs. These cell-type contrasts ignore per-cell variant status, so other properties of the donor "cannot [be] exclude[d]".
- **Neurotypical promoter variant.** chr2:19990244 G>A in a 15.1-year-old brain tracked up-regulation of *LAPTM4A* ~60 kb away (P = 0.006). In N2A cells, luciferase showed the promoter fragment is active, with a non-significant trend toward higher mutant activity (P = 0.057).
- **Portability.** The authors say the method drops into any 10x Multiome workflow, and in principle into any tagmentation-based single-cell method: CUT&Tag, droplet Hi-C and spatial methods.

## Methods / evidence

Nuclei were isolated by DAPI-sorting (FANS) from ~50 mg of frontal cortex. The standard 10x Multiome workflow ran through GEM barcoding and cleanup. The pre-amplification step was then replaced by two rounds of strand tagging, each using four barcoded P5 primers and a thermolabile ExoI clean-up, followed by modified pre-amplification and ATAC library PCR. GEX libraries are unchanged. Each ATAC library got 1.3–2.6 billion PE150 reads on NovaSeqX, and matched bulk WGS was required (30–45X, or 200X for two samples). Analysis: cellranger-arc, Seurat/Signac with Harmony and WNN, labels transferred from the Allen Brain Map, and DuplexTools to build read families and call variants. Germline and contamination were filtered with matched bulk, other samples' bulk and gnomAD (>1%). Mutation ageing slopes were fitted by resampling, with t-tests on slopes. scWGS comparators were PTA neurons (eight donors) and PTA oligodendrocytes (five donors) called with SCAN2, from Ganz et al. Gene-expression effects were tested by comparing pseudobulk expression of carrier cells against bootstrapped pseudo-clones from the same cell type and individual, for genes within ±500 kb. Validation was by Amplicon-seq (MiSeq, MosaicHunter) and a NanoLuc luciferase assay.

Weight: a well-built methods paper with an orthogonal truth set (COLO829), scWGS gold-standard comparisons for ENs and OLs, and amplicon validation of clonal calls. The headline biology varies in strength. EN and OL rates are anchored to scWGS. Rates for other cell types, signature-depletion inferences and gene-expression effects rest on accessibility-conditioned sampling, one to two individuals per functional example, and P values near 0.03–0.06 without stated multiple-testing correction. It is a preprint (synthesis).

## Limitations

**Authors' own:**
- "The limited coverage of the method renders genome-wide mutational patterns difficult to definitively determine." Genome-wide burdens are accurate only "when open chromatin enrichment factors are known", which they are for ENs and OLs from scWGS.
- There are few OPCs in older donors, so subtle OPC-vs-OL differences cannot be excluded. SBS19 detection may reflect sampling.
- Validation rates are lower for clonal sSNVs below VAF 0.01, which may be focal. Cell-type accessibility and sampling may explain VAF discordance with Amplicon-seq.
- Cell-type differential expression in AN06365 ignores per-cell variant status, so other donor properties could explain it.
- Single-strand damage calls probably reflect post-mortem or preparation damage, not biology. Burdens are not computed for clusters under 200 cells. Matched bulk WGS is required.

**Reviewer notes:**
- Detection depends on accessibility. The same mechanism that lets the assay link variants to chromatin also biases lineage and cell-type assignment: the chr1 ASD variant was invisible in neurons that carry it. Clonal lineage graphs therefore under-represent cells where a locus is closed. (synthesis)
- Genome-wide rates for astrocytes, microglia, INs and OPCs assume equal rates across the genome, or borrow EN/OL enrichment factors. The ranking that makes astrocytes "most susceptible" among glia is therefore a covered-region result that scWGS has not confirmed. (synthesis)
- The gene-expression claims rest on two variants, each in a single donor. The abstract's "directly demonstrating" is stronger than the evidence, which is correlational and includes a luciferase trend at P = 0.057. (synthesis)

## Surprising or load-bearing bits

- **Same-nucleus mutation + chromatin + RNA at scale, with a caveat.** Point mutations come only from accessible chromatin and only sparsely per nucleus. "Genome-wide" holds for burdens only after correction for open-chromatin enrichment, not as per-cell coverage. The assay meets the wiki's synthesis-gap wishlist in kind, but it does not give genome-wide per-cell genotypes. (synthesis)
- **A variant can be invisible where it is silent.** The chr1 enhancer variant shows up only in cell types where its locus is open, which turns sampling bias into a functional readout. The same logic underlies the SBS16 reasoning: mutations that close chromatin would hide themselves from the assay.
- **Glial clonality in ageing brain is intrinsic.** Low-VAF clonal sSNVs are enriched in glia, not in blood-derived cells. This addresses the open alternative in [[10-Summaries/taejeong-2022-science]].
- **Single-cell burdens generalise.** Cell-type burdens pooled from thousands of nuclei match scWGS estimates from a few dozen cells, which supports the representativeness of small scWGS cohorts.
- **The COLO829-BLT50 reference is clonally dynamic.** Culture-acquired lymphoblast subclones also appear in the SMaHT duplex benchmark ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]). (synthesis)

## Entities mentioned

- [[20-Entities/christopher-walsh]] — co-corresponding author (Boston Children's / HHMI).
- [[20-Entities/diane-d-shao]] — co-author.
- Eunjung Alice Lee and August Yue Huang are co-corresponding authors; neither has an entity page. The brain samples come from the NIH NeuroBioBank, the Autism BrainNet and the BU UNITE / VA-BU-CLF brain banks.

## Concepts touched

- [[30-Concepts/joint-single-cell-multi-omics]] — the first droplet-scale assay pairing duplex-grade sSNVs with snATAC and snRNA in the same nucleus.
- [[30-Concepts/scatac-seq]] / [[30-Concepts/tn5-tagmentation]] — the ATAC fragment is the duplex molecule, so callable territory is the accessible genome.
- [[30-Concepts/chromatin-accessibility]] — conditions detection. SBS1 is depleted and SBS16 under-detected in open chromatin.
- [[30-Concepts/mutational-signatures]] — SBS5/16/1/19 by cell type. SBS45 is the artefact removed by duplex consensus, SBS30 the single-strand damage signature, SBS18 the culture signature.
- [[30-Concepts/lineage-tracing]] — shared-sSNV graphs with label propagation, a retrospective lineage method that needs no engineered barcodes.
- [[30-Concepts/allele-dropout]] — handled by bootstrapped pseudo-clones in the expression test.
- [[30-Concepts/autism-spectrum-disorder]] — functional follow-up of a known ASD enhancer variant at single-nucleus resolution.

## Connections to other sources

- scWGS comparators: [[10-Summaries/luquette-2022-neuron-scan2-indels]] (PTA/SCAN2 neurons, ~16.5 sSNVs/year). The Duplex-Multiome EN rate of 15.05/year agrees. The older MDA estimate of ~23/year in [[10-Summaries/lodato-2017-aging-neurons]] is higher. (synthesis)
- Duplex lineage: [[10-Summaries/schmitt-2012-pnas]], [[10-Summaries/kennedy-2014-duplex-protocol]] and [[10-Summaries/bae-2023-codec]] are cited as duplex methods. [[10-Summaries/xing-2021-meta-cs]] is the other single-cell duplex route, using Tn5 strand encoding on whole-genome-amplified single cells. [[10-Summaries/liu-2024-hidef-seq]] supplies the SBS30-like single-strand damage precedent.
- Same reference sample: [[10-Summaries/zhang-2025-smaht-duplex-benchmark]] uses COLO829-BLT50 and resolves an acquired SBS9/SBS18 lymphocyte expansion. This parallels the SBS18 lymphoblast subclones found here. (synthesis)
- Joint genotype-plus-phenotype precedents cited by the authors: [[10-Summaries/izzo-2024-got-cha]] (targeted loci with chromatin), [[10-Summaries/macaulay-2015-gt-seq]] (G&T-seq) and [[10-Summaries/marks-2023-resolveome]]. Computational sSNV calling from scRNA/scATAC, which the authors argue fails in non-neoplastic tissue: [[10-Summaries/muyas-2024-scomatic]], [[10-Summaries/dou-2023-monopogen]].
- Brain-mosaicism context: [[10-Summaries/taejeong-2022-science]] (131 brains, where blood vs glial origin of aged-brain clones was unresolved) and [[10-Summaries/bizzotto-2022-brain-mosaicism-review]].
- Methodological alternative from the other direction: [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] (PTA scWGS with bulk duplex validation). The single-cell duplex comparison is synthesised in [[50-Notes/single-cell-duplex-sequencing]], and the wiki's framing of the gap in [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]].
- Atlas-scale contrast: [[10-Summaries/mukamel-2025-aneuploidy-brain]] reads aneuploidy with methylation in mouse brain, while Duplex-Multiome reads SNVs with accessibility and RNA in human brain. (synthesis)

## Open questions

- Do the astrocyte, microglia and IN rates hold genome-wide once scWGS-derived enrichment factors exist for those cell types? (synthesis)
- Do SBS16-type A[T>C] mutations really reduce accessibility, or are they under-called for another reason? This needs allele-resolved accessibility at mutated sites.
- How much of the clonal expression signal survives multiple-testing correction across all clonal sSNVs and genes within 1 Mb? (synthesis)
- Does the method carry over to other tagmentation chemistries (CUT&Tag, droplet Hi-C, spatial), as the authors propose, or to non-brain tissues such as kidney?
- Peer-review status: a bioRxiv preprint as of this ingest.

## Related

- [[40-Topics/somatic-mosaicism]] · [[40-Topics/brain-somatic-mosaicism]] · [[40-Topics/duplex-sequencing]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/single-cell-lineage-tracing]] · [[50-Notes/single-cell-duplex-sequencing]]
