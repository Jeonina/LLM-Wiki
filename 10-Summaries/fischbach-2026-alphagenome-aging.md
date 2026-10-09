---
type: summary
title: "Fischbach 2026 — Testing the mutation accumulation hypothesis in aging with AlphaGenome"
source: "[[00-Sources/papers/Testing the mutation accumulation hypothesis in aging with AlphaGenome.pdf]]"
source_quality: full
source_sha256: "de4e510e41f9a1d19cfce44d2de578e51e082f6318b8962729125e2742418e63"
source_kind: paper
author: "Arthur Fischbach (sole and corresponding author)"
published: 2026-05-15
ingested: 2026-10-09
doi: "10.64898/2026.05.10.724136"
journal: "bioRxiv preprint"
tags: [AlphaGenome, sequence-to-function, variant-effect-prediction, somatic-mutations, somatic-mosaicism, aging, mutation-accumulation, colon, intestinal-crypt, indels, purifying-selection, common-fragile-sites, Tabula-Sapiens, Tabula-Muris-Senis, preprint]
entities: []
concepts: ["[[variant-effect-prediction]]", "[[sequence-to-function-model]]", "[[epigenetic-aging]]", "[[mutational-signatures]]", "[[genosenium]]", "[[cis-regulatory-element]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/somatic-mosaicism]]"]
---

**Citation:** Fischbach (2026) — *Testing the mutation accumulation hypothesis in aging with AlphaGenome* — *bioRxiv preprint* (posted 15 May 2026). [DOI](https://doi.org/10.64898/2026.05.10.724136)

# Fischbach 2026 — AlphaGenome and mutation accumulation in aging

> A single-author preprint that runs **AlphaGenome** ([[avsec-2026-alphagenome]]) on random and **real somatic mutations from normal colonic crypts** to ask whether accumulated mutations could produce the age-related transcriptional changes of colonic epithelium. The real variants are the **Cagan 2022 crypt catalogue** ([[cagan-2022-nature]]): somatic **SNVs and short indels (1–6 bp), mostly noncoding**, from human and mouse intestinal crypts, scored natively in hg38 and mm10. AlphaGenome is asked only for **RNA-seq** predictions in colon tissue (UBERON:0001157), using a 1-Mb window around each variant. **Nothing is measured for the variants themselves.** The predictions are compared with a separate aging reference: pseudobulk young-vs-old log2 fold changes from Tabula Sapiens v2 (human) and Tabula Muris Senis (mouse) colonic epithelium. Predicted per-gene effects are about three to four orders of magnitude smaller than the aging program on the median, and real somatic variants score no higher than random ones. The author concludes that single-nucleotide and short-indel mutation accumulation does not explain colonic transcriptional aging. Attention should move to epigenetic and regulatory mechanisms. The author treats AlphaGenome output as a valid stand-in for variant consequences and does not test that assumption.

## Key claims

- **Random-SNV baseline (R1).** 4,000 SNVs sampled uniformly across hg38 were scored in colon. All predictions succeeded. Median per-variant mean absolute expression change ≈ 1 × 10⁻⁶, and 99.9% of variants were below 10⁻⁴. The largest single total change was 1,104, at chr17:81,415,658 T→A. Mapped to the nearest protein-coding gene, only 604 of 3,579 expressed colon-epithelial genes carried a random SNV. The per-gene maximum was 1.23 × 10⁻³, against an aging maximum |log2 FC| of 6.98.
- **No stacking in 1-Mb windows (R2).** Windows holding 10 co-occurring random SNVs reached a summed effect of only ~3 × 10⁻⁴, assuming perfect additivity.
- **Gene-body simulation (R3a).** The author simulated 60 cells with ~4,000 random SNVs each: 240,000 calls, 203,405 of them with a finite gene-body log2 FC. Ten variants (~1 in 20,000) reached |log2 FC| ≥ 1. The top hits were *TMIGD2* +2.248, *RNASE2* −1.546 and *NEUROD4* −1.520. The median was 1.04 × 10⁻³. When two SNVs hit the same gene in the same cell, the summed maximum stayed at 2.248, the single-SNV maximum.
- **Pseudobulk (R3b).** Pooling the 60 cells covered 3,056 of 3,579 genes (85.4%). The maximum |log2 FC_pb| was 0.192 (*TMEM238*) and the median 3.96 × 10⁻⁴, about 36× below the aging maximum and ~1,445× below the aging median. The pseudobulk changes did not correlate with aging changes (Pearson r = −0.027, p = 0.13; Spearman ρ = −0.031, p = 0.09).
- **Real somatic SNVs score at or below random (R4).** In human donor PD36813ad8 (3,384 SNVs), the mean absolute expression change was 5.97 × 10⁻⁶ and the median |log2 FC| 6.0 × 10⁻⁴, below the matched random baseline. The per-gene maximum was 0.525 against an aging maximum of 6.98. Only 497 of 3,579 expressed genes (14%) were hit, and only 7 of the top 50 aging DEGs. The mouse samples (9,177 SNVs over five samples) gave the same picture. The Discussion reports real-to-random ratios of 0.625× (mouse) and 0.88× (human).
- **Indels score ~22–24× higher per event than SNVs but stay below a 2-fold change (R5).** The indel-to-SNV per-event ratio was 22×, 21× and 24× across three human donors, and ~24× in mouse sample MD6267ab_lo0003 (0.030 vs 0.0012). Across 1,630 indels pooled from nine human donors, the maximum |log2 FC| was 0.373 and the median 0.0115. Summing per gene across donors, none of 1,441 genes reached |log2 FC| ≥ 1. The worst per-gene sum in any sample was 0.82 (mouse *Spertl*, 4 indels). Insertions and deletions behaved alike, with no monotonic size–effect relation over 1–6 bp.
- **Purifying selection in the catalogue (R6).** Across 28 human samples (3,042 indels), CDS held 15 indels against 35.1 expected, a ~2.3× depletion (within-protein-coding χ² p = 2.4 × 10⁻⁵). Mouse (54 samples, 9,799 indels) showed 12× CDS depletion (8 of 2,755 protein-coding-gene indels; top-level p = 3.2 × 10⁻¹⁰⁴). SNVs showed the same direction with smaller effects: ~1.4× CDS depletion in human (427 vs 611 expected) and ~1.3× in mouse.
- **Recurrently hit genes are fragile sites (R7).** In mouse, 99 protein-coding genes were enriched for indels (54 samples, FDR < 0.05) and 41 for substitutions (5 samples). The top hits were long neural-adhesion and common-fragile-site genes such as *Cntnap2* (34 indels, 23/54 samples), *Lsamp*, *Dmd*, *Lrp1b* and *Csmd1/3*. SNV and indel hits overlapped strongly (hypergeometric p = 3.8 × 10⁻³⁷). Neither hit list was enriched for fibrosis, SASP, senescence, inflammation or EMT gene sets (all fold < 1, all p > 0.8).
- **Conclusion about the model's use.** The author treats AlphaGenome as the missing "variant-to-function bridge" for a quantitative test of mutation accumulation. The negative result is read as a statement about aging biology, not about the model. AlphaGenome's stated limits are that it is a cis-only predictor and works within a 1-Mb window.

## Methods / evidence

AlphaGenome was called through the `dna_client.predict_variant` API with a 1-Mb interval centred on each variant. Only RNA_SEQ output was requested, at about 2–3 s per call, in colon (UBERON:0001157) or large intestine (UBERON:0000059). Per-variant metrics were mean, max and total expression change across the window, plus a gene-body log2((s_alt+1)/(s_ref+1)) for the nearest GENCODE v46 or vM25 protein-coding gene. Somatic calls came from the Cagan et al. Zenodo deposit (10.5281/zenodo.5554777): 54 mouse samples and human files, with mouse scored in mm10 without liftover. Aging references were built from Tabula Sapiens v2 large-intestine epithelium (7 epithelial types, 9,578 cells): young was one donor (TSP26, 37 y, 597 cells) and old was four donors (56–61 y, 8,981 cells). The pseudocount was 0.1, and genes with a group mean > 0.5 were kept, leaving 3,579. The mouse reference was Tabula Muris Senis large-intestine epithelium (3 m vs 18/24/30 m, ~17,000 genes). Region enrichment used χ² goodness-of-fit against base-pair-proportional expectations. Gene recurrence used Poisson upper-tail tests on gene body ±10 kb with BH FDR. Code: github.com/fischbacha/AlphaAge.

Weight: this is a computational argument resting entirely on model predictions. No variant effect is measured, and AlphaGenome is not benchmarked on somatic variants or on colon here. The design is "adversarial" only against the mutation-accumulation hypothesis, not against the predictor. The text has several internal inconsistencies. The human Cagan cohort is called "3 human samples" in the Abstract and R4, "nine human donors" in R5 and Table 1, and "28 human samples" with 56,123 SNVs in R6. The gap to the aging maximum is "~3×" in R3a and "~13×" in the Discussion. The Discussion gives a mouse real-to-random ratio of 0.625×, but the Fig. S5 caption gives 1.34 × 10⁻³ vs 1.12 × 10⁻³ (1.20×, real higher). Methods cite sections "R4b" and "R11" that do not exist, and describe a "three-output predictor" while also saying only RNA_SEQ was requested. (synthesis)

## Limitations

**Authors' own:**
- AlphaGenome is a cis-regulatory predictor on a 1-Mb window. It does not capture trans effects, genome-scale structural variation, aneuploidy, telomere attrition, proteostasis collapse, or clonal amplification of rare large-effect events.
- The Tabula Sapiens v2 young arm is a single donor (37 y) against four older donors. The mouse Tabula Muris Senis comparison is offered as independent confirmation.
- The human Cagan catalogue is small, so per-gene recurrence and positional enrichment rely on mouse data.
- Only colon was tested. Post-mitotic tissues, where mutation accumulation is expected to act most strongly, await companion analyses.
- The results do not refute genomic instability as a hallmark of aging or its role in cancer. They address only SNVs and short indels as drivers of transcriptional drift in colonic epithelium.

**Reviewer notes:**
- The whole result depends on AlphaGenome's calibration for rare somatic variants in colon tissue, and that calibration is never tested here. Most noncoding variants receive near-zero predictions from any sequence-to-function model. The "three-to-four orders of magnitude" gap may therefore reflect the predictor's output scale as much as biology. (synthesis)
- The comparison sets a per-variant predicted change (whole-tissue RNA-seq track, both alleles altered in the input sequence) against an observed pseudobulk fold change between age groups. A somatic variant sits on one allele in one crypt clone. The two quantities are not on a common scale, and the 60-cell "pseudobulk" pools simulated random SNVs, not real clones. (synthesis)
- The many internal count and ratio inconsistencies listed above, together with the single-author preprint status, mean the numbers need checking against the code repository before citation. (synthesis)

## Surprising or load-bearing bits

- **A rare direct use of a sequence-to-function model on catalogued normal-tissue somatic mutations.** Most AlphaGenome-style evaluation is on germline eQTLs and caQTLs ([[avsec-2026-alphagenome]]). This paper scores thousands of real somatic SNVs and indels from normal crypts, but it has no ground truth to check the predictions against. (synthesis)
- **Selection lowers predicted impact.** Real somatic variants score at or below random positions, in line with CDS depletion. The author argues that the observed catalogue is already filtered, so its predicted effects are an upper bound on neutral accumulation.
- **Indels score ~22–24× higher than SNVs per event, consistently across species,** which fits the expectation that length-altering variants disrupt more sequence.
- **Recurrent somatic indel genes in mouse crypts are fragile-site genes not expressed in colon,** which points to replication-stress fragility rather than transcription-coupled mutagenesis or selection.

## Concepts touched

- [[variant-effect-prediction]] — AlphaGenome RNA-seq scores applied to somatic SNVs and indels from normal tissue, with no measured effects to validate against.
- [[sequence-to-function-model]] — used as a proxy for the molecular consequence of somatic mutation load.
- [[epigenetic-aging]] — the author redirects the explanation of transcriptional aging toward epigenetic drift and loss of chromatin information.
- [[mutational-signatures]] / [[genosenium]] — builds on per-cell somatic burdens from crypt WGS. The paper's own contribution is a consequence estimate, not new mutation counts.
- [[cis-regulatory-element]] — tests whether co-located variants stack in shared cis windows. They do not.

## Connections to other sources

- Data source: [[cagan-2022-nature]] — same crypt WGS catalogue (Zenodo deposit of Cagan et al. 2022). Cagan measured the mutation burden, and this paper estimates its predicted transcriptional consequence.
- Model: [[avsec-2026-alphagenome]] — cited here as the 2025 DeepMind technical report. Avsec et al. evaluated mostly germline QTLs plus a *TAL1* somatic example. This paper moves AlphaGenome to normal-tissue somatic variants. (synthesis)
- Contrast: [[terekhanova-2026-tal1-enhancer]] — the other somatic AlphaGenome test in this batch. There, real somatic T-ALL enhancer variants with measured strong effects were under-predicted, which suggests small predicted effects are not by themselves evidence of small real effects. (synthesis)
- Aging-mutation framing: [[lodato-2017-aging-neurons]] and [[kapadia-2024-stem-cell-aging]] discuss somatic mutation in aging tissues. Fischbach's colon-only result leaves post-mitotic tissues untested. (synthesis)

## Open questions

- Does AlphaGenome's colon RNA-seq score track measured expression effects of somatic variants at all, for example via allele-specific expression in clonal crypt organoids? Without this, a null result cannot separate "no effect" from "model cannot see the effect". (synthesis)
- Would the conclusion hold in post-mitotic tissues (neurons, cardiomyocytes), which the author names as the sharpest test?
- How should a single-allele, single-clone somatic variant be converted into a tissue-level expected effect, given clone size from crypt or single-cell data? (synthesis)
- Do the repository outputs resolve the inconsistent human cohort counts (3, 9 or 28 samples) and real-to-random ratios? (synthesis)

## Related

- [[avsec-2026-alphagenome]] · [[cagan-2022-nature]] · [[variant-effect-prediction]] · [[sequence-to-function-model]] · [[epigenetic-aging]] · [[terekhanova-2026-tal1-enhancer]] · [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/somatic-mosaicism]]
