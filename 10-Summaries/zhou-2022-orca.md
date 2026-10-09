---
type: summary
title: "Zhou 2022 — Sequence-based modeling of three-dimensional genome architecture from kilobase to chromosome scale"
source: "[[00-Sources/papers/Sequence-based modeling of three-dimensional genome architecture from kilobase to chromosome scale]]"
source_quality: full
source_sha256: "cd71ee87138b9b128e5f1d6988d2b40109ccd1343c80a4dc3f88b32615fe5319"
source_kind: paper
author: "Jian Zhou (sole author, corresponding)"
published: 2022-05-12
ingested: 2026-10-08
doi: "10.1038/s41588-022-01065-4"
journal: "Nature Genetics"
tags: [Orca, sequence-to-function, convolutional-neural-network, Micro-C, Hi-C, contact-map-prediction, chromatin-compartments, TAD, structural-variants, virtual-genetic-screen, in-silico-mutagenesis, CTCF, Polycomb, TSS, cohesin-depletion, multiscale]
entities: []
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[chromatin-compartments]]", "[[topologically-associating-domain]]", "[[chromatin-loop]]", "[[structural-variants]]", "[[micro-c]]", "[[transcription-factor-motif]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[3d-genome]]", "[[chromatin-architecture]]"]
---

**Citation:** Zhou (2022) — *Sequence-based modeling of three-dimensional genome architecture from kilobase to chromosome scale* — *Nature Genetics*. [DOI](https://doi.org/10.1038/s41588-022-01065-4)

# Zhou 2022 — Orca

> Orca predicts Micro-C contact maps from DNA sequence at nine nested scales, from 4 kb resolution within 1 Mb up to 512 kb resolution across 256 Mb (longer than chr1), including interchromosomal contacts. A hierarchical convolutional encoder (its first section adapted from Sei) compresses up to 256 Mb of sequence to representations at 4–1,024 kb; cascading 2D decoders "zoom" from the whole-chromosome map down to 1 Mb, each conditioned on the coarser prediction above it. A "horizontal checkpointing" trick makes chromosome-scale training fit in GPU memory. Trained on H1-ESC and HFF Micro-C, Orca reaches Pearson 0.78–0.85 (H1-ESC) and 0.73–0.79 (HFF) on held-out chromosomes at all scales. The paper's main uses are predicting the 3D effects of structural variants from 300 bp to tens of megabases, concordant with experiments in all six studies tested, and "virtual genetic screens" that link cell-type-specific TF motifs to local contacts and suggest that active TSS sequences drive A compartments while B is a default state for long AT-rich stretches.

## Key claims

- **Multiscale accuracy.** Held-out chromosomes 9 and 10: Pearson 0.78–0.85 (H1-ESC) and 0.73–0.79 (HFF) across scales; interchromosomal 0.47–0.74 at the 64–256 Mb levels. An auxiliary task predicting DNase/CTCF/histone peaks from the 4 kb encoder improved performance; larger context gave a small improvement to local predictions. Predictions differ between the two cell types, and Orca's 1 Mb predictions beat Akita on the shared test set (values in supplementary figures, not in the clipping).
- **Beyond CTCF.** Held-out examples show cell-type-specific Polycomb-mediated contacts (H1-ESC only, with H3K27me3) and promoter–enhancer contacts consistent with Micro-C and histone ChIP-seq.
- **Boundary insertions.** For transposon-mediated 2 kb boundary-element insertions measured by in situ Hi-C in HAP1, predicted vs observed insulation changes across 14 sites had cosine similarity 0.89 (H1-ESC model) and 0.76 (HFF), P < 1 × 10⁻⁴; all three reported outcomes (new boundary, strengthened boundary, no effect) were reproduced.
- **Large SVs.** A 40.5 Mb inversion linked to AML is predicted to remodel the chromosome and create the experimentally confirmed EVI1 promoter–GATA2 enhancer contact. Limb-malformation deletions, duplications and inversions (0.9–1.8 Mb) are predicted to bring PAX3, WNT6 or IHH into contact with the same enhancer, consistent with 4C. At KCNJ2–SOX9, sex-reversal duplications (0.2–1 Mb) enlarge the SOX9 TAD and add contact with a duplicated enhancer, whereas a larger no-phenotype duplication (1.8 Mb) forms a new boundary that insulates SOX9, and Cooks syndrome duplications place a new KCNJ2 copy in a new TAD. Across variants from six studies, predictions agreed with chromatin conformation experiments in all cases.
- **Local motifs.** A multiplexed in-silico screen of every autosomal 10 bp site (correlation >0.9 with single-mutation screens, ~20× faster) finds that >88.9% of the strongest-impact sites (score >0.1, <0.015% of the genome) overlap CTCF motifs and >95.1% lie within 200 bp of one, but only ~1% of strong CTCF motifs have strong impact. Mid-impact non-CTCF sites are cell-type-specific: POU5F1::SOX2 enriched 48.7× in H1-ESC (1.0× in HFF), FOSL1::JUND enriched 167× in HFF (0.71× in H1-ESC).
- **Compartments from sequence.** A model trained on cohesin-depleted HCT116 Hi-C (TADs removed, compartments intact) reaches Pearson 0.71 at the 32 Mb level and shows no CTCF dependence. Insertion screens show compartment-A activity is sparse (<0.07% of 400 bp sequences above 0.02) and mostly spans TSSs, enriched in active-TSS chromatin states but not bivalent TSSs or 3′ ends, without strand preference. 800 bp is enough for strong A activity in a B context; switching A to B needs at least 6,400 bp and is stronger at 12,800 bp. B activity survives shuffling down to 2 bp segments and tracks A/T content; A activity disappears below 128 bp segments. Shuffling 1.28 Mb of A sequence turns it B.
- **Model of compartments.** Active TSS sequences drive A; B is the "default" for extended (>6–12 kb) AT-rich sequence lacking A activity. The 6–12 kb scale matches independent measurements that fragments of at least 10–25 kb are needed for stable compartmentalisation.

## Methods / evidence

Encoder: 28 convolution layers (64–128 channels) with Sei's dual linear + nonlinear residual design to reach 4 kb resolution (receptive field 212 kb), then 4 convolution layers per factor-of-2 coarsening up to 1,024 kb; bottom-up then top-down pass. Decoders: 2D residual blocks cycling dilations 1–64 for four passes (112 layers per decoder), pairwise-sum 1D→2D, a log-expected distance matrix and the upsampled coarser prediction as inputs; outputs 250 × 250 matrices of log fold over distance background, symmetrised and averaged over strands. Training in three stages (Orca-1Mb, Orca-32Mb, Orca-256Mb), each freezing the earlier encoder: ~480,000, 150,000 and 20,000 SGD steps on four V100 GPUs; on-the-fly sampling with Selene; ICE balancing and adaptive coarse-graining with cooler/cooltools, no further smoothing. Split: chr8 validation, chr9 and chr10 test. The Akita comparison resamples, smooths and clips Orca output to match Akita's processing and uses distance-background-subtracted correlation. Code: github.com/jzhoulab/orca; web server orca.zhoulab.io.

Weight: an ambitious single-author paper with a chromosome-level held-out design. SV validation is qualitative for most loci (visual concordance with 4C, Capture Hi-C or Hi-C), quantitative only for the 14 insertions. The compartment model is a hypothesis generated by in-silico screens; the paper says it remains to be tested experimentally.

## Limitations

**Authors' own:**
- Some predictions differ from observation beyond technical noise or alignment artefacts.
- Learned mechanisms must recur across the genome; locus-unique mechanisms may be missed.
- The model may pick "passenger" patterns that are nearly perfectly correlated with true drivers.
- Highly repetitive regions cannot be assessed with Hi-C reads; the model tends to predict B-like structure there. Telomere-to-telomere assemblies and long reads may help.
- "Active" and "passive" compartment labels describe sequence dependencies only, not molecular mechanism; the compartment hypotheses need experimental tests.

**Reviewer notes:**
- Only two cell types (plus cohesin-depleted HCT116) were modelled, so the cell-type-specific motif findings rest on one ESC vs one fibroblast comparison. (synthesis)
- The clipping has small inconsistencies: the abstract gives SV sizes up to 90 Mb, the results up to 80 Mb; the cohesin-depleted line is "HCT116" in results and "HCT119" in methods; the exploratory screen uses "10" targets in results and "nine" in methods; "KCNJ9 hijacking" in the Cooks syndrome passage reads like a typo for KCNJ2. (synthesis)
- Several SV validations compare human-sequence predictions with mouse Capture Hi-C (Franke et al.), which assumes conserved folding at those loci. (synthesis)

## Surprising or load-bearing bits

- A model trained only on contact maps, with no transcription or chromatin data, learned to recognise TSS sequences as compartment-A drivers.
- B compartment activity survives shuffling to dinucleotides: under this model, complex sequence patterns are not needed for B, only the absence of A activity and AT richness.
- Cell-type specificity in local folding comes from non-CTCF TFs (OCT4–SOX2 in ESC, AP-1 in fibroblasts), while CTCF dependence is largely cell-type-invariant.
- Copy-number-aware structural explanations: Orca resolves which duplicated enhancer copy contacts SOX9, which sequencing reads alone cannot distinguish.

## Concepts touched

- [[sequence-to-function-model]] — first sequence model to reach whole-chromosome and interchromosomal scale.
- [[variant-effect-prediction]] — SV effects from 300 bp insertions to 40.5 Mb inversions.
- [[chromatin-compartments]] — sequence model of A (TSS-driven) and B (default, AT-rich) formation.
- [[topologically-associating-domain]] / [[chromatin-loop]] — CTCF-dominant local structure; boundary creation and insulation by duplications.
- [[structural-variants]] — TAD fusion, enhancer hijacking and new-boundary insulation explained from sequence.
- [[micro-c]] — H1-ESC and HFF Micro-C as training data.
- [[transcription-factor-motif]] — POU5F1::SOX2 and AP-1 as cell-type-specific folding motifs.

## Connections to other sources

- Direct predecessor and comparator: [[fudenberg-2020-akita]] (1 Mb window); Orca extends to 256 Mb and reports higher 1 Mb correlations.
- Encoder adapted from the same lab's [[chen-2022-sei]]; earlier lab models [[zhou-2015-deepsea]] and [[zhou-2018-expecto]].
- Training data: Micro-C from [[hsieh-2015-micro-c]]'s method lineage; processing with [[abdennur-2020-cooler]].
- SV mechanisms (TAD fusion, enhancer hijacking) match [[lupianez-2015-tad-disruption]] and [[spielmann-2018-sv-3d-genome]].
- Compartment–transcription link relates to [[rao-2014-in-situ-hic]] and [[lieberman-aiden-2009-hic]]; the length-scale argument touches [[chromatin-phase-separation]].
- Later sequence-to-contact models in this ingest: [[fang-2025-evo2hic]], [[wang-2026-hicfoundation]]. (synthesis)

## Open questions

- Do engineered 800 bp TSS insertions really switch a B region to A in cells, as the screen predicts?
- Would more cell types reveal additional cell-type-specific folding motifs? (synthesis)
- Can the approach handle repetitive regions once telomere-to-telomere references and long-read contact data are available?

## Related

- [[sequence-to-function-model]] · [[chromatin-compartments]] · [[structural-variants]] · [[fudenberg-2020-akita]] · [[chen-2022-sei]] · [[40-Topics/3d-genome]] · [[40-Topics/sequence-models-and-foundation-models]]
