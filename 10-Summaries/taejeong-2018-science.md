---
type: summary
title: "Bae 2018 — Different mutational rates and mechanisms in human cells at pregastrulation and neurogenesis"
source: "[[00-Sources/papers/Different mutational rates and mechanisms in human cells at pregastrulation and neurogenesis]]"
aliases: [Bae 2018, Taejeong 2018, clonal-expansion pregastrulation neurogenesis]
tags: [somatic-mosaicism, neuro-mosaicism, clonal-cell-population, pregastrulation, neurogenesis, mutation-rate, mutation-spectrum, foundational]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Bae et al. (2018) — *Different mutational rates and mechanisms in human cells at pregastrulation and neurogenesis* — *Science*. [DOI](https://doi.org/10.1126/science.aan8690)

# Bae et al. 2018 — Pregastrulation vs neurogenesis mutational landscape

> Taejeong Bae, Livia Tomasini, Jessica Mariani, Bo Zhou, Tanmoy Roychowdhury, Daniel Franjic, Mihovil Pletikos, Reenal Pattni, Bo-Juen Chen, Elisa Venturini, Bridget Riley-Gillis, Nenad Sestan, Alexander E. Urban, **Alexej Abyzov**\*, **Flora M. Vaccarino**\*. *Science* **359**, 550–555 (2 Feb 2018). DOI: 10.1126/science.aan8690.

## Thesis

Single neuronal progenitor cells from three human fetal brains (15–21 weeks postconception) were expanded to **clonal cell populations** (a few thousand cells per clone) before bulk DNA sequencing. This sidesteps WGA artifacts that plague single-nucleus mosaicism methods. The clonal approach yields **200–400 mosaic SNVs per founder cell**, with strikingly different mutation rates and mutation spectra between the pre-gastrulation period (first ~5 postzygotic cleavages, ~1.3 mutations/division/cell) and active neurogenesis (~5.1 SNVs/day per progenitor, ~3 orders of magnitude higher than the adult germline rate).

## Method

1. Dissociate ventricular/subventricular zones (VZ-SVZ) from frontal cortex, parietal cortex, basal ganglia of 3 fetal brains (15w, 17w4d, 21w).
2. Limiting dilution to single cells; let each clone proliferate to a few thousand cells.
3. WGS DNA from each clone (31 clones total) + bulk brain tissue + spleen to ≥30× coverage.
4. **Three discovery comparisons in parallel**: clone-to-VZ-SVZ-tissue, clone-to-spleen, clone-to-clone. The clone-to-clone comparison (98.9% concordant with tissue comparisons, plus 31 additional high-VAF SNVs missed by tissue comparisons) is the methodological innovation.
5. Targeted capture + ~1000× resequencing of all 6288 SNVs across multiple brain regions and spleen for genotyping/validation.

## Key claims

1. **200–400 mosaic SNVs per progenitor cell** at 15–21 weeks postconception, after correcting for ~83% sensitivity and ~5% false-positive rate. SNV counts increase linearly with fetal age. No regional difference between frontal cortex, parietal cortex, and basal ganglia VZ-SVZ.

2. **Mutation rate during neurogenesis: 5.1 SNVs/day per progenitor (95% CI 1.5–9), or ~8.6/division (95% CI 1.6–20)** assuming 27–54 hr cell cycle. **Three orders of magnitude higher than the 0.4–2 SNVs/year adult germline rate**, and **50× higher than the 36/year rate in postnatal intestinal/colonic/liver stem cells**.

3. **Mutation rate before gastrulation: 1.3 ± 0.15 SNVs/division/daughter cell** (weighted average across 3 brains). Consistent with the 1.2 rate from familial-trio de novo analyses. *The rate increases substantially between pre-gastrulation and neurogenesis* — the paper's title finding.

4. **Mutation spectrum shifts from CpG-deamination dominated (early) to oxidative-damage dominated (late)**.
   - Early (genotyped in tissues, mostly pre-gastrulation): Ti/Tv = 2.2; C:G→T:A transitions dominant, especially at CpG (consistent with 5-methylcytosine spontaneous deamination). Spectrum closely matches germline de novo SNVs.
   - Late (clone-specific, neurogenic): Ti/Tv = 0.6; C:G→A:T transversions enriched (P = 8.0×10⁻¹²), consistent with 8-oxoguanine misrepair (mutational signature 18, suspected oxidative-damage etiology — also seen in MUTYH-deficient colorectal cancer).
   - Suggests **physiological/biochemical shift** during organogenesis, possibly linked to cardiovascular-system maturation increasing reactive oxygen species exposure.

5. **Lineage reconstruction**: 84 mutations precisely assigned to the first 5 postzygotic cleavages via VAF clustering across tissues + clone sharing. The cell-progeny tree reveals unequal lineage contribution to tissues in places (asymmetric division, drift, or selection).

6. **Pre-gastrulation origin for ~60% of genotyped SNVs**: 92% of SNVs with VAF>2% in any brain region were also detectable in spleen → arose before the mesoderm-ectoderm-endoderm split. The mosaicome contains a deep "embryonic memory" layer.

7. **Mutations correlate negatively with histone marks and accessibility in fetal brain** (10% depletion of SNVs in DNase-hypersensitive sites, larger when using fetal-brain DHS vs lymphoblastoid DHS). **No depletion in coding vs intronic regions** → not negative selection, but better DNA repair efficiency in open chromatin. Direct cell-type-specific epigenome-mutagenesis coupling.

8. **~3% of SNVs may be functionally consequential** (coding or regulatory) → ~12 nonbenign mutations per progenitor at 20 weeks. Cancer-driving mutations *can* happen by chance during background mutagenesis (signature 18 best descriptor of fetal-brain mosaic spectrum is also seen in neuroblastoma, medulloblastoma — supports the Tomasetti-Vogelstein background-mutagenesis-in-cancer hypothesis).

## Surprising / load-bearing for the review

- **Companion paper to Lodato 2018** (same *Science* issue, p.555): together they bracket the human-brain mosaicism timeline — Bae 2018 covers fetal progenitors, Lodato 2018 covers postnatal post-mitotic neurons. For the review's §1/§5 framing, these two papers anchor the human-brain mosaicism field circa 2018.

- **The clone-to-clone discovery comparison** is methodologically important: it's an alternative to WGA-based single-nucleus sequencing that **eliminates the WGA artifact problem** (Chen 2017, Dong 2017 — refs 14, 15) but loses post-mitotic neuron coverage. For the review §3.1 (genotype-centric scDNA profiling), this is the "in-vitro-clonal-expansion" branch alongside scWGA-based and duplex-based approaches.

- **The 10% DNase-hypersensitive depletion of mosaic SNVs in fetal brain** is direct single-cell evidence that **chromatin state shapes mutation distribution** at the developmental locus level. This is exactly the kind of mutation × epigenome coupling the planned review aims to articulate — and it is observable here only because the clones come from cells whose epigenome matched the reference. The synthesis note in [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] should incorporate this.

- **First author Taejeong Bae** is at Mayo Clinic (Abyzov lab); this is the foundational pre-gastrulation-vs-neurogenesis mosaicism paper. **Bae 2022** ([[10-Summaries/taejeong-2022-science]]) is the follow-up at BSMN cohort scale.

## Entities / concepts touched

[[somatic-mosaicism]] · [[post-zygotic-variation]] · [[developmental-mutation-timing]] · [[lineage-tracing]] · [[mutational-signatures]] · [[20-Entities/alexej-abyzov]] · [[20-Entities/flora-vaccarino]] · [[20-Entities/christopher-walsh]] · [[40-Topics/somatic-mosaicism]]

## Related summaries

- [[10-Summaries/taejeong-2022-science]] — Bae 2022 follow-up at 131-brain BSMN scale, aging-associated hypermutability + ASD enhancer-motif finding.
- [[10-Summaries/single-cell-mosaicism-analysis-reveals-cell-type-specific-somatic-mutational-burden-in-alzheimer-s-dementia]] — Kousi/Kellis on AD-specific mosaicism.
- [[10-Summaries/a-comprehensive-view-of-somatic-mosaicism-by-single-cell-dna-analysis]] — Luquette/Walsh 102-nucleus PTA + duplex.
- [[10-Summaries/genetic-mosaicism-in-the-human-brain-from-lineage-tracing-to-neuropsychiatric-disorders-nature-reviews-neuroscience]] — Bizzotto/Walsh NRN review citing this paper.

---
**Source:** [DOI](https://doi.org/10.1126/science.aan8690) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/29217587/)
