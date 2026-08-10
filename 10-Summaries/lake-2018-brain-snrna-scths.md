---
type: summary
title: "Lake et al. 2018 — Integrative single-cell analysis of transcriptional and epigenetic states in the human adult brain"
source: "[[00-Sources/papers/Integrative single-cell analysis of transcriptional and epigenetic states in the human adult brain]]"
source_kind: paper
author: "Blue B. Lake, Song Chen, Brandon C. Sos, Jean Fan, Gwendolyn E. Kaeser, Yun C. Yung, Thu E. Duong, Derek Gao, Jerold Chun, Peter V. Kharchenko, Kun Zhang (corresponding)"
published: 2017-12-11
ingested: 2026-08-10
doi: "10.1038/nbt.4038"
journal: "Nature Biotechnology"
tags: [snDrop-seq, scTHS-seq, single-nucleus, human-brain, postmortem, chromatin-accessibility, diagonal-integration, GWAS, remyelination]
entities: ["[[peter-a-sims]]"]
concepts: ["[[scrna-seq]]", "[[dnase-seq]]", "[[combinatorial-indexing]]", "[[tn5-tagmentation]]", "[[atac-seq]]", "[[transcription-factor-motif]]", "[[multimodal-integration-methods]]", "[[drop-seq]]"]
topics: ["[[single-cell-atac-seq]]", "[[brain-somatic-mosaicism]]", "[[single-cell-multiomics]]"]
---

**Citation:** Lake et al. (2018) — *Integrative single-cell analysis of transcriptional and epigenetic states in the human adult brain* — *Nature Biotechnology* 36, 70–80. [DOI](https://doi.org/10.1038/nbt.4038)

# Lake 2018 — snDrop-seq + scTHS-seq

> Two nucleus-based, archived-tissue-compatible methods run on the same postmortem brain samples: **snDrop-seq** for nuclear transcriptomes and **scTHS-seq** for DNA accessibility. >60,000 single cells from human visual cortex, frontal cortex and cerebellum, computationally bridged by a gradient-boosting model that predicts accessibility from expression and vice versa — then used to map GWAS risk variants to specific brain cell types.

## Key claims

- **Nuclei, not cells, are the enabling choice.** They can be derived from fresh or archived tissue, give enough RNA for accurate expression estimates, and are "free of artifacts associated with tissue dissociation." Prior single-nucleus work was capped at 96 cells per microfluidic chip with sampling bias against small non-neuronal nuclei.
- **scTHS-seq** = transposome hypersensitive-site sequencing + combinatorial cellular indexing with custom barcoded transposomes, using linear amplification by in vitro transcription and an engineered super-mutant Tn5 — claimed higher sensitivity than ATAC-seq, "including better coverage of distal enhancers found to be highly cell-type specific."
- Yields: 36,166 expression profiles (35,289 assigned) at a median of **928 unique transcripts and 719 genes per nucleus**, ~6,200 usable reads; 32,869 scTHS-seq nuclei (27,906 assigned), **287,381 accessibility peaks over 144 Mb**, median 10,168 unique reads per cell.
- **35 transcriptional clusters** resolved, including excitatory and inhibitory cortical subtypes, cerebellar granule and Purkinje neurons, and non-neuronal types — with regional specificity (cerebellum-specific astrocytes and OPCs; visual-vs-frontal excitatory differences).
- Spatially interpretable subtypes: layer-4 *RORB*⁺ subpopulations expanded in visual cortex (*EYA4*⁺ Ex3d confirmed layer-4-visual-specific and absent from frontal cortex); layer-5 *HS3ST5*/*PCP4*/*HTR2C* splits; interneuron subtypes by layer.
- **The integration model.** Two gradient-boosting models — one predicting differentially accessible sites from differential expression, one the reverse — using distance-to-gene and degree of differential signal as features. Any single gene/site prediction is weak; **joint consideration of many enables confident classification**. Applied iteratively down a transcriptome-derived dendrogram (non-neuronal vs neuronal, then Ex vs In, then subtypes), with cross-validation for stability at each split.
- **Accessibility alone cannot resolve fine subtypes.** Layer-4 excitatory neurons could not be separated from layer-5/6 by unsupervised accessibility analysis; only transferring the transcriptome's differential features made the split possible. Attempts to push interneuron subdivision past InA/InB (medial vs lateral/caudal ganglionic eminence origin) produced **unstable assignments**, which the authors report as a negative result — insufficient differentially accessible sites.
- TF activity by motif over-representation in cell-type-differential accessible regions (379 JASPAR matrices), cross-validated against expression of the TF itself.
- **Remyelination trajectory**: diffusion mapping orders OPC → immature oligodendrocyte (iOli) → mature Oli. AMPA/kainate receptor genes enrich in OPC and iOli; **NMDA receptor genes (*GRIN2A*, *GRIN2B*) only in iOli** — matching the proposed model where axon–OPC glutamate synapses direct OPCs to exposed axons and NMDA activation directs remyelination. OPC and iOli accessible-site sets are **nearly mutually exclusive**, implying active maintenance of the two states. SOX9 motifs dominate OPC sites; TCF4 (Wnt/β-catenin) dominates iOli sites.
- **GWAS mapping**: risk SNPs for ten brain disorders vs seven non-brain controls, tested for accessibility enrichment in 100 kb windows with permutation significance. **Alzheimer's risk variants enrich in microglia (Z = 5.41)**, not neurons. No brain-cell enrichment for non-brain diseases; non-brain enrichments landed in plausible types (microglia and endothelium for Crohn's, celiac, T1D).

## Methods / evidence

Postmortem tissue from six individuals; human–mouse species-mixing controls for doublet rates in both assays; censored-Poisson clustering for accessibility that accounts for signal saturation after a few reads at any site; cross-validation of branch assignments; permutation-based GWAS significance; comparison of predicted microglial regulatory sites against bulk ATAC-seq.

Limitations the authors state: neurons are over-represented relative to astrocytes and endothelium, so **cell-type proportions from snDrop-seq carry technical bias**; nuclear data show a systematic bias toward longer genes; cortical astrocyte and oligodendrocyte subpopulations seen in mouse were not resolved, cause undetermined.

## Surprising or load-bearing bits

- **This is a diagonal integration done carefully, and its honest reporting of where it fails is the most useful part.** Transcriptome resolves 35 clusters; accessibility on its own resolves broad types; the model transfers resolution downward until it runs out of signal — and the authors say where. Contrast with the many papers that integrate scATAC and scRNA and report only successes. [[argelaguet-2021-integration-principles|Argelaguet 2021]] names this regime and its assumptions; this paper is a worked example with the failure boundary marked.
- The **asymmetry** is the general lesson: expression carries more cell-type information per cell than accessibility at comparable depth. Every scATAC study inherits this.
- **AD risk lands in microglia, not neurons** — reached independently and by a different route than [[roadmap-2015-111-epigenomes|Roadmap 2015]], which found the same thing in bulk immune-cell enhancers. Two orthogonal datasets converging on an immune rather than neuronal locus of AD genetic risk is a strong result, and it reframes what brain single-cell genomics should be sampling.
- Mutually exclusive OPC/iOli accessibility argues the transition is **actively maintained**, not a passive gradient — the kind of claim only per-cell chromatin data supports.
- scTHS-seq is a road less travelled: DNase-hypersensitivity logic implemented with barcoded Tn5 and IVT linear amplification, claiming better distal-enhancer coverage than ATAC. It did not become standard, but the distal-enhancer sensitivity claim is worth noting given how much cell-type specificity lives distally ([[heinz-2010-homer]], [[mclean-2010-great]]).
- For this wiki's mosaicism focus: this is the **archived postmortem brain** infrastructure — the same tissue source as single-neuron mosaicism studies — profiled for expression and chromatin instead of genome. The obvious missing third axis is genotype.

## Concepts touched

- [[combinatorial-indexing]] — scTHS-seq uses barcoded transposomes plus split-pool indexing.
- [[multimodal-integration-methods]] — GBM-based cross-modality prediction, an early and explicitly evaluated diagonal method.
- [[transcription-factor-motif]] — JASPAR motif enrichment in cell-type-differential accessible regions, cross-validated by TF expression.

## Connections to other sources

- Diagonal-integration theory: [[argelaguet-2021-integration-principles]]; alternatives in [[welch-2019-liger|LIGER]] and Seurat v3.
- Accessibility method context: [[buenrostro-2015-nature]], [[cusanovich-2015-sciatac]], [[jin-2015-nature|scDNase]].
- Brain single-cell epigenome successors: [[luo-2018-snmc-seq2]] (methylome), [[lee-2019-natmethods|sn-m3C-seq]] (3D + methylome), [[liu-2023-mouse-brain-methylome-3d]].
- AD/microglia thread: [[miller-2022-nature]], [[kousi-2022-ad-mosaicism]], [[roadmap-2015-111-epigenomes]].
- Brain mosaicism tissue context: [[brain-somatic-mosaicism]], [[lodato-2017-aging-neurons]], [[bizzotto-2022-brain-mosaicism-review]].

## Open questions

- **Genotype is the missing axis.** The same postmortem nuclei carry somatic mutations, and this study measures expression and chromatin but not genome. Whether the cell-type-specific regulatory states here co-vary with single-neuron mosaic variants is exactly the [[mosaicism-and-epigenome-the-synthesis-gap|synthesis gap]].
- The interneuron-subtype instability is attributed to insufficient differentially accessible sites, but the alternative — that the subtypes genuinely do not differ in accessibility — is not excluded.
- Cell-type proportion estimates are stated to carry technical bias; no correction is offered, which limits abundance-based comparisons across studies.

## Related

- [[argelaguet-2021-integration-principles]] · [[combinatorial-indexing]] · [[brain-somatic-mosaicism]] · [[luo-2018-snmc-seq2]]
