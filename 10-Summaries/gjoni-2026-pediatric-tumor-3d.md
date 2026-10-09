---
type: summary
title: "Gjoni et al. 2026 — Machine learning-predicted chromatin organization landscape across pediatric tumors"
source: "[[00-Sources/papers/Machine learning-predicted chromatin organization landscape across pediatric tumors]]"
source_quality: full
source_sha256: "e921cab82a4acb000ba5bae0aa985bb16a370199aac41f8062a867b3aa26dbae"
source_kind: paper
author: "Ketrin Gjoni, Shu Zhang, Rachel E. Yan, Bo Zhang, Daniel Miller, Jeffrey P. Greenfield, … (Adam Resnick, Nadia Dahmane, Katherine S. Pollard; corresponding author not marked in the clipping)"
published: 2026-03-28
ingested: 2026-10-09
doi: "10.1038/s41598-026-44925-3"
journal: "Scientific Reports"
tags: [Akita, SuPreMo, in-silico-mutagenesis, structural-variants, somatic-SV, pediatric-brain-tumor, CBTN, 3D-genome, TAD-boundary, enhancer-hijacking, activity-by-contact, ATRT, pHGG, DIPG, medulloblastoma, cancer]
entities: []
concepts: ["[[variant-effect-prediction]]", "[[sequence-to-function-model]]", "[[structural-variants]]", "[[topologically-associating-domain]]", "[[chromatin-loop]]", "[[cis-regulatory-element]]", "[[chip-seq]]", "[[atac-seq]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/3d-genome]]", "[[40-Topics/cancer-clonal-evolution]]"]
---

**Citation:** Gjoni et al. (2026) — *Machine learning-predicted chromatin organization landscape across pediatric tumors* — *Scientific Reports*. [DOI](https://doi.org/10.1038/s41598-026-44925-3)

# Gjoni 2026 — Akita on paediatric tumour SVs

> **Source note:** full text with Methods. Figures and supplementary tables are not in the clipping, so per-tumour and per-region values are reported only where the text states them.
>
> The authors run **Akita**, a CNN that predicts ~1 Mb contact maps from sequence, through their **SuPreMo-Akita** in-silico mutagenesis pipeline on **somatic [[structural-variants]]** (DEL, DUP, INV, INS, BND) called with Manta from tumour WGS of 1,843 Children's Brain Tumor Network (CBTN) patients across 61 tumour types. Each SV is inserted into the reference sequence, and the REF and ALT predicted maps are compared by MSE and 1 − correlation. Nearly 300,000 SVs were scored, and 107,614 remained after artifact filtering. The paper ranks tumour types by predicted disruption, finds five 1 Mb "recurrently disrupted regions" (RDRs), and adds an Activity-by-Contact (ABC) weighting from tumour-matched cell-line H3K27ac and ATAC data to prioritise SVs that disrupt contacts at enhancers. This is a pure **application** of a [[sequence-to-function-model]] to somatic SVs (coding and noncoding). There is no benchmark: Akita's predictions are never checked against tumour Hi-C. Support is indirect, mainly expression outliers for three BNDs in atypical teratoid rhabdoid tumour (ATRT) and SVs that land on known pHGG enhancer targets.

## Key claims

- **SV landscape.** Samples have a median of 35 SVs. Lymphomas and sarcomas have the most (median 71.5) and mesenchymal tumours the fewest (24). BNDs make up 48% of SVs and DELs 33%. Progressive tumours carry 1.2× the SV burden of initial tumours, and 56% of participants have more SVs in the progressive sample.
- **Predicted disruption varies by tumour type.** Metastatic tumours have the highest median disruption and the largest share of SVs above the cohort 90th percentile (12.5%). Lymphoma/sarcoma, driven by rhabdomyosarcoma, comes next. Benign tumours score lowest. Within gliomas and embryonal tumours, aggressive types (brainstem glioma, ETMR) score higher than benign ones (ganglioglioma, low-grade astrocytoma, DNET). Most trends hold with MSE as well as correlation.
- **Progressive > initial.** Mean disruption is 0.053 in progressive vs 0.050 in initial samples (Welch t-test, p = 2.26 × 10⁻⁶). In 121 individuals with paired samples, the within-person difference is significant for 3/7 ATRT, 1/2 meningioma and 1/38 glioma participants.
- **What drives the score.** Disruption rises with SV length. Among large non-BND SVs, coding SVs are more disruptive than intronic or intergenic ones. Among BNDs, which the authors class as all noncoding, intronic BNDs are more disruptive than intergenic ones. Scores are not correlated with tumour purity (Spearman R = −0.082, n = 2,066) or read support (R = 0.050, n = 33 ATRT samples).
- **Five recurrently disrupted regions** (chr3, chr7, chr19, chrX-a, chrX-b) come from UMAP on sample × 1 Mb-bin maximum scores. All disruptive SVs in them are DELs or DUPs. Three show predicted TAD-boundary loss and one shows loop loss. All five are disrupted in significantly more samples than the rest of the genome, but only three are mutated in significantly more samples. The authors' point is that disruption hotspots are not always mutation hotspots. Each RDR is hit in up to 5–15 tumour types, and medulloblastoma, low- and high-grade astrocytoma and ependymoma hit all five.
- **Highly disruptive SVs.** A visually tuned cutoff at the 98.8th percentile gives 363 SVs (353 in Methods) in 34 of 61 tumour types. Within 300 kb of them lie 2,012 protein-coding genes (2,003 in Methods), and 249 of these are hit in more than one tumour type. Of 13 noncoding SVs past the strongest cutoff, 6 strongly change contacts of relevant genes. Examples: a 127,129-bp DEL removing a TAD boundary between *AKT3* and *ZBTB18*, and partial DUPs of TADs containing *MYCN* and *EGLN3*.
- **Disruptive SVs sit in active chromatin.** In pHGG, highly disruptive SVs overlap H3K27ac and ATAC peaks (KNS42 cell line) more than other SVs after length matching (Mann–Whitney p < 0.0001). The same holds in ATRT, DIPG and medulloblastoma.
- **ABC-weighted disruption.** About 150,000 candidate enhancers come from four cell lines (DIPG007, KNS42, D283, BT16). The activity score is the geometric mean of ATAC and H3K27ac reads, and it is combined with Akita's per-bin (448 bins) MSE track. The method was applied to the top 10% of SVs in pHGG, DIPG, ATRT and medulloblastoma. ABC and plain scores correlate highly (pHGG Pearson R = 0.8433). The "upweighted" SVs (<1%, 0.54–0.79%) include DUPs near *PDGFRA* and *ID2* in pHGG, both previously reported targets of recurrent SVs, an SV near *GNA12* in DIPG and a DEL near *PPP2R2C* in medulloblastoma.
- **ATRT candidates with expression support.** Three upweighted BNDs show high predicted disruption at enhancers near *NASP*, *MSH6* and *FOXJ2*, which the authors read as consistent with enhancer hijacking. Expression in the carrier is lower than 31/32 other ATRT samples (*NASP*), higher than 31/32 (*MSH6*) and higher than 27/28 (*FOXJ2*). Other upweighted SVs sit near *CCND1* and *BCL7C*.

## Methods / evidence

SVs: CBTN somatic Manta v1.4.0 'PASS' calls, annotated with AnnotSV. SuPreMo-Akita scores each SV in a ~1 Mb window, averaging four augmentations (no shift, ±1 bp shifts, reverse complement). The SV itself is masked from the map. SVs > 500 kb were removed, and SVs sharing identical breakpoints were excluded. RDR bins were kept only after qualitative review, and bins where the reference prediction did not match experimental maps were dropped. Epigenomic data were processed with the ENCODE ChIP/ATAC pipelines. GO analysis used clusterProfiler. Code: github.com/ketringjoni/SuPreMo.

Weight: a large, careful descriptive screen. Every functional conclusion rests on Akita's predictions, which were trained on non-tumour cell types and are not checked here against tumour contact data. The only orthogonal readouts are single-sample expression outliers and overlap with known pHGG SV targets. Several thresholds (98.8th percentile, RDR selection) were chosen by eye.

## Limitations

**Authors' own:**
- Short-read SV calls are imprecise and co-occurring SVs are hard to resolve. Tumour purity varied, coverage data were unavailable, and detection sensitivity was likely uneven across samples, which could bias burden and disruption comparisons. RDR SVs have wider breakpoint confidence intervals than other DELs and DUPs.
- Akita sees only a 1 Mb window, so SVs over 500 kb and compartment-scale changes are out of reach.
- Akita was not trained on paediatric tumour cell types, so context-specific contacts may be missed. The authors partly offset this with tumour cell-line epigenomics and earlier cross-cell-type validation of Akita.
- SVs are scored one at a time. Clustered events such as chromothripsis and haplotype-level effects are not modelled.
- Experimental validation is the critical next step.

**Reviewer notes:**
- Disruption scales with SV length. The authors stratify some analyses by length, but the tumour-type ranking and the progressive-vs-initial comparison use raw scores. The progressive-vs-initial difference is 0.003 in mean score despite the small p-value. (synthesis)
- Internal inconsistencies: 363 vs 353 highly disruptive SVs and 2,012 vs 2,003 genes (Results vs Methods). The Fig. 3a caption says 1 kb bins where the text says 1 Mb. The *GNA12* SV is called a DEL in the text and a BND in the Fig. 4g caption. The Fig. 4g caption says "500 Mb" for a window that must be about 500 kb. (synthesis)
- This is a single-model screen. No second contact-map model (e.g. Orca or AlphaGenome's contact head) is used to check robustness, and no germline SV control set is scored in the same tissues. So "disruptive" means disruptive by Akita, not shown to matter in tumours. (synthesis)

## Surprising or load-bearing bits

- **One of the few uses of a sequence-to-function model on somatic SVs at cohort scale** (~300,000 SVs). The earlier Akita SV study the authors cite for cross-cell-type validation is on de novo germline SVs in autism. (synthesis)
- **Disruption hotspots ≠ mutation hotspots.** Two of the five RDRs would be missed by recurrence counting alone. This is the main argument that model scores add information beyond frequency.
- **BNDs are scored too.** SuPreMo builds chimeric sequences for translocations, so inter-chromosomal events can be scored. Most sequence models cannot take them as input. (synthesis)
- The ABC weighting barely changes the overall ranking (R = 0.84). Its value is the small tail of SVs whose disruption falls on enhancers.

## Concepts touched

- [[variant-effect-prediction]] — REF vs ALT predicted contact maps as an effect score for somatic SVs.
- [[sequence-to-function-model]] — Akita applied out of training context (tumour SVs, non-tumour training cells).
- [[structural-variants]] — somatic DEL/DUP/INV/INS/BND; length dependence; BNDs as noncoding.
- [[topologically-associating-domain]] / [[chromatin-loop]] — predicted boundary loss and loop loss in RDRs; enhancer hijacking framing.
- [[cis-regulatory-element]] / [[chip-seq]] / [[atac-seq]] — H3K27ac and ATAC peaks for ABC weighting.

## Connections to other sources

- Model: [[fudenberg-2020-akita]]. The 1 Mb window and 2,048-bp bins set the 500 kb SV ceiling used here. (synthesis)
- Longer-range alternative not used: [[zhou-2022-orca]]. Multimodal alternative with a contact-map head: [[avsec-2026-alphagenome]]. The authors suggest pairing with accessibility or TF-binding models and cite [[avsec-2021-enformer]].
- Conceptual basis for SV effects through TAD boundaries: [[spielmann-2018-sv-3d-genome]], [[lupianez-2015-tad-disruption]].
- Other somatic uses of sequence models in this ingest: [[zeng-2025-somatic-driver-lm]] (DNA LM on cancer point mutations, benchmarked) and [[weinstock-2025-ch-noncoding-drivers]] (AlphaGenome on clonal-haematopoiesis noncoding variants, unbenchmarked). (synthesis)

## Open questions

- How much of the per-tumour ranking survives length-matched comparison? (synthesis)
- Do tumour Hi-C or Micro-C maps from CBTN samples or matched lines show the predicted boundary losses at the five RDRs? (synthesis)
- Would the same pipeline flag anything in non-cancer somatic SVs, for example mosaic SVs in normal brain? Untested. (synthesis)

## Related

- [[variant-effect-prediction]] · [[sequence-to-function-model]] · [[structural-variants]] · [[topologically-associating-domain]] · [[fudenberg-2020-akita]] · [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/3d-genome]] · [[40-Topics/cancer-clonal-evolution]]
