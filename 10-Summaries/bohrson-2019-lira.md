---
type: summary
title: "Bohrson et al. 2019 — Linked-read analysis identifies mutations in single-cell DNA-sequencing data (LiRA)"
source: "[[00-Sources/papers/Linked-read analysis identifies mutations in single-cell DNA-sequencing data]]"
source_kind: paper
author: "Craig L. Bohrson, Alison R. Barton, Michael A. Lodato, Rachel E. Rodin, Lovelace J. Luquette, Vinay V. Viswanadham, Doga C. Gulhan, Isidro Cortés-Ciriano, Maxwell A. Sherman, Minseok Kwon, Michael E. Coulter, Alon Galor, Christopher A. Walsh, Peter J. Park (corresponding)"
published: 2019-03-18
ingested: 2026-10-07
doi: "10.1038/s41588-019-0366-2"
journal: "Nature Genetics 51(4):749-754"
tags: [LiRA, read-backed-phasing, single-cell-variant-calling, MDA, amplification-artifact, somatic-SNV, neurons, composite-coverage, FDR, singleton-mutations]
entities: ["[[peter-park]]", "[[christopher-walsh]]", "[[lovelace-luquette]]"]
concepts: ["[[single-cell-variant-calling]]", "[[mda]]", "[[allele-dropout]]", "[[post-zygotic-variation]]", "[[compounding-artifact]]", "[[mutational-signatures]]"]
topics: ["[[mosaic-variant-calling]]", "[[brain-somatic-mosaicism]]", "[[whole-genome-amplification]]"]
---

**Citation:** Bohrson et al. (2019) — *Linked-read analysis identifies mutations in single-cell DNA-sequencing data* — *Nature Genetics* 51:749–754. [DOI](https://doi.org/10.1038/s41588-019-0366-2)

# Bohrson 2019 — LiRA

> The hardest single-cell mutation to validate is a **singleton** — present in one cell only, so no other cell or bulk sample can confirm it. LiRA validates such calls **within the cell** using read-backed phasing: a true somatic SNV sits on one chromosome, so every read spanning it and a nearby heterozygous germline SNP (gHet) on that haplotype carries both (**concordant**); an amplification artifact or lysis-induced lesion arises on one strand, so some reads from the same haplotype carry the gHet without the variant (**discordant**). Any discordant read kills the call. A per-cell two-component model then sets an FDR-controlled support threshold and yields genome-wide mutation-rate estimates despite only seeing the genome near gHets.

## Key claims

- **Most candidate calls are artifacts.** In single-neuron MDA data (~45×, Lodato et al. 2015; 36 neurons from 3 individuals), 27% of sSNV candidates (9–44% per cell) were close enough to a gHet for LiRA; of those, **92% were filtered as LiRA false positives** (87–96% per cell), versus only **2% of gHet–gHet pairs** (1–4%) — so the filter removes artifacts while losing little true variation, and standard genotypers cannot be used on single cells without heavy filtering.
- **Composite coverage + two-component model.** Composite coverage = minimum spanning-read depth across single cell and bulk. The observed mutation rate vs composite coverage is fitted per cell as an exponentially decaying error term plus a ~constant true-mutation term; the true term gives the genome-wide rate, the ratio gives per-call FDR and a threshold (default aggregate FDR ≤10%). Of non-discordant candidates, 63% (20–81%) fell below threshold as "uncertain". A decay parameter p = 1/2 fit well, consistent with artifacts from lesions on the original DNA before amplification (half the reads from the linked haplotype support them).
- **Per-cell thresholds matter**: the ratio of errors to predicted true sSNVs varied widely across cells, so a universal cutoff would mis-calibrate.
- **Rates and sensitivity.** An average of 83 sSNVs called per neuron, extrapolating to 919 sSNVs per cell genome-wide; LiRA rates were generally consistent with bottleneck sequencing of frontal cortex (Hoang et al.), an orthogonal method without single-cell WGA.
- **Calls look like real heterozygous mutations.** LiRA calls had a VAF distribution nearly identical to gHets; false positives and uncertain calls skewed low. SCcaller, Monovar, GATK, VarScan and MuTect produced low-VAF-skewed distributions and all carried substantial LiRA-false-positive burdens among phaseable candidates.
- **Artifact spectrum.** GATK PASS calls that LiRA flagged as false differed from LiRA calls (P < 10⁻⁵): enriched for C>T and C>A, depleted for C>G, T>A, T>C and T>G (T>G ~320% higher in LiRA calls; C>A ~50% lower).
- **Cancer application.** In a bladder-cancer single-cell exome dataset (55 cancer + 12 normal cells), linked reads let one read call a mutation **absent** confidently (98% of linked gHets show only concordant reads); a LiRA "scaffold" of 17 sSNVs plus 57 statistically rescued unlinked sSNVs recapitulated the original clustering and found non-synonymous and one nonsense mutation not in the original study (e.g. *SYTL3*).

## Methods / evidence

GATK HaplotypeCaller for maximally sensitive candidates (no bulk alt reads); gHets = population-polymorphic (1000 Genomes, dbSNP 147) heterozygous bulk calls; read/mate pairs with MAPQ 60, proper pairs, no indels or clipping; SHAPEIT2 to resolve haplotypes when gHets are not jointly spanned. Power map of where a hypothetical sSNV could be detected at each composite coverage, adjusted for non-artifact discordance and bulk sequencing error. Validation is indirect: gHet–gHet control, VAF distributions, spectra, and agreement with an orthogonal bulk rate.

Weight: a conceptually clean and highly specific filter; no ground-truth spike-ins here. Coverage is limited to the neighbourhood of gHets, so the call set is small and rate extrapolation depends on the power model. The authors flag that **strand dropout** (one strand failing to amplify) would let lesions masquerade as fixed mutations; they judge it negligible from model fits. The later PTA-vs-MDA comparison by the same group estimates ~550 SNV single-strand-dropout artifacts per MDA genome ([[luquette-2022-neuron-scan2-indels]]) — so that caveat was not negligible for genome-wide MDA calls. (synthesis)

## Surprising or load-bearing bits

- **Physical linkage as an internal control** is the key idea: it converts "is this real?" into a per-read consistency check needing no second cell.
- **Absence calls become cheap** — one spanning read on the null haplotype suffices, which sidesteps dropout modelling for genotyping shared mutations in tumours.
- **The p = 1/2 fit points to pre-amplification damage** (e.g. heat-induced cytosine deamination during lysis) as a dominant artifact source, consistent with the C>T/C>A enrichment. (synthesis)
- Suggested extensions: longer or synthetic long reads, deeper coverage, or crossbred strains with higher heterozygosity — the last later used in SCAN2's kindred mESC validation ([[luquette-2022-neuron-scan2-indels]]).

## Concepts touched

- [[single-cell-variant-calling]] — read-backed phasing as an artifact filter for singleton sSNVs.
- [[mda]] — characterises MDA artifact burden and spectrum.
- [[allele-dropout]] — linked reads allow confident absence calls despite dropout.
- [[compounding-artifact]] — early lesions propagated by exponential amplification.
- [[mutational-signatures]] — distinct spectra of artifacts vs true calls.

## Connections to other sources

- Applied to data from [[lodato-2015-science]]; the neuron aging-rate study built on it: [[lodato-2017-aging-neurons]].
- Same group's successors: [[luquette-2019-natcomm]] (SCAN-SNV, allele-balance model genome-wide), [[luquette-2021-scan2]] / [[luquette-2022-neuron-scan2-indels]] (SCAN2 with PTA; LiRA used as a cross-check, 17 vs 16.5 sSNVs/year).
- Orthogonal rate reference: [[hoang-2016-botseqs]] (bottleneck sequencing).
- Comparator callers: [[dong-2017-sccaller]] (also uses nearby heterozygous SNPs, but not read-backed phasing), [[zafar-2016-monovar]], [[mckenna-2010-gatk]].
- Benchmarks/reviews of single-cell callers: [[valecha-2022-scsnv-review]], [[ha-2023-natmethods]].

## Open questions

- How much does strand dropout leak artifacts through LiRA in MDA data? (Raised by the authors; later quantified indirectly by the PTA comparison.)
- Only regions near gHets are visible (27% of candidates), so region-specific analyses (enhancers, genes) are underpowered — the gap SCAN-SNV and SCAN2 were built to fill.

## Related

- [[single-cell-variant-calling]] · [[40-Topics/mosaic-variant-calling]] · [[luquette-2022-neuron-scan2-indels]] · [[lodato-2015-science]]
