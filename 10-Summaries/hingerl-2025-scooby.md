---
type: summary
title: "Hingerl et al. 2025 — scooby: modeling multimodal genomic profiles from DNA sequence at single-cell resolution"
source: "[[00-Sources/papers/scooby_ modeling multimodal genomic profiles from DNA sequence at single-cell resolution]]"
source_quality: full
source_sha256: "0aa8e9cdc439068bc4ac87875f398d58be04b7d62ff04fc2e74323dc82d48ce1"
source_kind: paper
author: "Johannes C. Hingerl, Laura D. Martens, Alexander Karollus, Trevor Manz, Jason D. Buenrostro, Fabian J. Theis, Julien Gagneur"
published: 2025-10-22
ingested: 2026-10-08
doi: "10.1038/s41592-025-02854-5"
journal: "Nature Methods"
tags: [scooby, Borzoi, sequence-to-function, single-cell, scRNA-seq, scATAC-seq, multiome, LoRA, fine-tuning, cell-embedding, MultiVI, eQTL, variant-effect, TF-motif, in-silico-mutagenesis, seq2cells, hematopoiesis]
entities: ["[[20-Entities/jason-buenrostro]]", "[[20-Entities/fabian-theis]]"]
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[scatac-seq]]", "[[scrna-seq]]", "[[joint-single-cell-multi-omics]]", "[[transcription-factor-motif]]", "[[pseudo-bulk]]", "[[hematopoietic-differentiation]]", "[[reference-atlas-mapping]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/single-cell-atac-seq]]", "[[40-Topics/single-cell-multiomics]]"]
---

**Citation:** Hingerl et al. (2025) — *scooby: modeling multimodal genomic profiles from DNA sequence at single-cell resolution* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-025-02854-5)

# Hingerl 2025 — scooby

> scooby turns the bulk sequence-to-function model **Borzoi** into a single-cell model. It keeps Borzoi's convolution + transformer trunk (524 kb input, 32-bp bins), adds **LoRA** adapters (rank 8) to every convolution and to the transformer query/value/MLP projections, and replaces Borzoi's thousands of bulk output heads with **one cell-conditioned decoder**: a small MLP reads a 14-dimensional Poisson-MultiVI cell embedding and outputs the weights of a 1×1 convolution that decodes the sequence embedding into that cell's stranded scRNA-seq coverage and scATAC-seq insertion profile. Because cells enter through an embedding rather than one output track each, the parameter count does not grow with cell number, unlike seq2cells. Trained on a 63,683-cell 10x Multiome bone-marrow dataset, scooby predicts held-out genes' cell-type expression (mean Pearson 0.86 across genes, 0.54 for between-cell-type deviations), beats a retrained seq2cells, scores TF motif effects that track TF expression better than chromVAR and scBasset, and assigns single-cell eQTLs to the right cell types better than Borzoi or simple baselines.

## Key claims

- **Single-cell profile prediction.** Correlation of predicted to observed single-cell profiles on test sequences was 0.15 (RNA) and 0.11 (ATAC), above the cell's own pseudobulk (0.09 and 0.08) but low in absolute terms because single cells are sparse. Against each cell's 100-nearest-neighbour average the correlations rose to 0.63 (RNA) and 0.70 (ATAC). The authors use the kNN average as a practical upper bound.
- **Cell-type expression of held-out genes.** Summing predicted coverage over exons and pseudobulking per cell type gave Pearson 0.82–0.88 across genes (mean 0.86), the same as Borzoi on bulk RNA-seq (0.86). After removing gene and cell-type means, the correlation was 0.54.
- **Beats seq2cells.** On shared Enformer/Borzoi test genes, retrained seq2cells vs scooby: across genes 0.77 → 0.87, across cell types 0.43 → 0.55.
- **Ablations.** An RNA-only scooby was worse than the multiome model (0.848 across genes, 0.496 across cell types) but still beat seq2cells. Dropping LoRA and feeding frozen Borzoi embeddings to the decoder hurt mostly the between-cell-type metric (0.501). Decoders on top of Borzoi's predicted tracks (all 7,611, or the 1,543 RNA tracks) did "notably worse". A pseudobulk multi-task model with the same trunk did not beat scooby, so single-cell resolution does not cost accuracy.
- **Unseen cell states.** With all normoblasts withheld from both embedding and training, projected normoblast embeddings gave Pearson 0.79 vs 0.81 for the full model. *HEMGN* expression along erythroid pseudotime was recovered at 0.939 (full) and 0.966 (normoblast-ablated). The authors do not expect generalisation to drastically different cell types.
- **TF motif effect scores.** Replacing all PWM matches (HOCOMOCO v12, FIMO) for each of 83 differentially expressed TFs within 524 kb of 3,681 DE genes, and averaging the log fold change, gave per-cell directional scores. These correlated with cognate TF expression better than chromVAR (P = 5.4 × 10⁻⁹) and scBasset (P = 0.04). An RNA-only scooby scored on par or better than both ATAC-based methods. Known lineage motifs came out (GATA in erythroblasts, EBF1 in B cells, C/EBP in monocytes, RUNX in T cells), as did the repressor BACH2.
- **Accessibility vs expression timing.** Mutating GATA1 sites affected predicted accessibility early and expression later in erythropoiesis, consistent with GATA1 as a pioneer factor.
- **Within-cell-type heterogeneity.** In a heart-organoid (epicardioid) multiome dataset, TF scores correlated with CellRank fate probabilities inside the juxta-cardiac field progenitors, recovering epicardial (FOS, EPAS1, TBX1, TFAP2A/B/C) and cardiomyocyte (GATA4, MSX1, ISL1) regulators.
- **Variant effects.** A scooby trained on OneK1K (over 1 million PBMCs, 982 donors) nearly matched Borzoi on GTEx whole-blood fine-mapped eQTLs (Spearman 0.45 vs 0.47) and beat Borzoi on OneK1K cell-type eQTLs in all cell types. Dropping predictions under a 3.5% fold change raised the GTEx correlation from 0.45 to 0.78 with 91.6% sign concordance. Sign concordance fell with distance from the TSS. For deciding which cell type carries an eQTL, scooby beat cell-type-matched Borzoi, an ATAC-peak baseline and a target-gene-expression baseline.
- **Mechanism example.** rs143664050 lowers *TES* in CD14⁺ monocytes but not erythroblasts. scooby predicts loss of a monocyte-accessible region, and gradient attribution points to a disrupted SPI1 site, a TF expressed in myeloid cells only.

## Methods / evidence

Data: NeurIPS 2021 10x Multiome bone marrow (63,683 cells, primary benchmark), epicardioid multiome (scGLUE-paired metacells), OneK1K scRNA-seq (scPoli embedding). Cell embeddings: Poisson-MultiVI (raw ATAC fragment counts, 14 dimensions), scVI for the RNA-only model. Genes and peaks overlapping validation or test regions were removed before computing embeddings to avoid leakage, and scooby kept Borzoi's sequence-level train/validation/test folds. Coverage was stored with a modified SnapATAC2 that records spliced RNA reads as several fragments in AnnData. Training: Borzoi replicate 0 weights converted to PyTorch, only LoRA, a new GELU layer and the cell decoder trained; 64 random cells per sequence; Poisson + multinomial loss as in Borzoi; 8 A40 GPUs for about 2 days. Two scaling tricks: cache sequence embeddings across cells, and decode only exon-overlapping bins for expression. Baselines: seq2cells retrained on the same data (only 100,000 OneK1K cells, because the full set used too much memory), chromVAR, scBasset, Borzoi with matched tracks. eQTLs: fine-mapped SNVs with PIP ≥ 0.9 from the eQTL Catalog.

Weight: careful leakage control and honest ablations. Most results come from one hematopoiesis dataset, and TF target genes were checked only by GO enrichment, not ChIP-seq. Exact numbers for several comparisons (Fig. 3–5, Extended Data Fig. 5) are in figures that are images in the clipping, so only the values the text gives are reported here.

## Limitations

**Authors' own:**
- Not expected to generalise to cell types far outside the training domain.
- TFs with similar motifs (GATA1, TRPS1, GATA3) get similar scores, a limit of motif matching.
- Predicted TF targets were not validated with ChIP-seq.
- Distal eQTL effects are strongly underestimated, as for other sequence models. Negligible predicted effects are not evidence of no effect.
- 10x 3′ coverage bias limits isoform modelling. Little differential isoform usage in the test data.
- No extensive hyperparameter search.

**Reviewer notes:**
- The absolute single-cell correlations (0.15 RNA, 0.11 ATAC) are low. The "single-cell" claim rests on decoding a smooth cell embedding, so the model predicts a cell state's expected profile, not cell-specific noise. (synthesis)
- The cell embedding comes from the same dataset's counts (MultiVI). Applying scooby to a new dataset needs that dataset's own embedding and retraining, so it is a per-dataset fine-tune, not a zero-shot model. (synthesis)
- Germline variant effects only. Nothing here tests somatic or single-cell-specific genotypes, which is what scDNA-seq would supply. (synthesis)

## Surprising or load-bearing bits

- **One decoder, not one head per cell.** A hypernetwork that writes the decoder weights from a cell embedding is what lets a 524-kb bulk model scale to a million cells.
- **RNA alone gets TF activity.** Sequence plus scRNA coverage gave TF scores at least as good as ATAC-based chromVAR and scBasset, so for TF activity the sequence prior can replace the accessibility assay.
- **Fine-tuning matters for between-cell-type differences.** Frozen Borzoi embeddings already give good across-gene accuracy, but the cell-type contrasts need LoRA adaptation. This parallels the frozen-vs-fine-tuned result in [[fan-2026-gfetm]]. (synthesis)
- **Filtering small predicted effects** raises eQTL correlation from 0.45 to 0.78, which says the models are mostly right in sign when they predict anything, and silent otherwise.

## Entities mentioned

- [[20-Entities/jason-buenrostro]] — co-author.
- [[20-Entities/fabian-theis]] — co-author.

## Concepts touched

- [[sequence-to-function-model]] — adapts a bulk seq-to-function model (Borzoi) to single-cell resolution with LoRA and a cell-conditioned decoder.
- [[variant-effect-prediction]] — cell-type deconvolution of fine-mapped bulk and single-cell eQTLs.
- [[scatac-seq]] / [[scrna-seq]] / [[joint-single-cell-multi-omics]] — models both modalities of 10x Multiome jointly as base-pair-binned profiles.
- [[transcription-factor-motif]] — in silico motif deletion as a TF activity score, benchmarked against chromVAR and scBasset.
- [[pseudo-bulk]] — pseudobulk as the comparator and evaluation unit.
- [[hematopoietic-differentiation]] — erythroid lineage, normoblast hold-out, GATA1/TAL1/KLF1 targets.
- [[reference-atlas-mapping]] — proposed use for unseen-but-related cell states.

## Connections to other sources

- Built on [[linder-2025-borzoi]], whose trunk and train/test folds it reuses. Compared to seq2cells, which adapts [[avsec-2021-enformer]].
- TF activity baselines: [[schep-2017-chromvar]] and [[yuan-2022-scbasset]].
- Cell embedding from MultiVI ([[ashuach-2023-multivi]]); coverage storage adapted from [[zhang-2024-snapatac2]]; epicardioid pairing from scGLUE ([[cao-2022-glue]]).
- Same goal (sequence-based single-cell expression) as [[lal-2026-decima]], which also starts from Borzoi but predicts pseudobulk across a large atlas instead of single cells. (synthesis)
- Mentions a ChromBPNet preprint as a local scATAC model ([[pampari-2024-chrombpnet]]).

## Open questions

- Would a cell embedding from a different modality (CITE-seq, methylation) or an atlas-level embedding remove the per-dataset retraining? The authors suggest other embeddings are possible.
- Distal enhancer effects remain underestimated. Does a longer-context or 3D-aware trunk fix this, or is it a training-data limit? (synthesis)
- Could the same decoder predict single-cell methylation or histone profiles, as the authors propose? Untested here.

## Related

- [[sequence-to-function-model]] · [[variant-effect-prediction]] · [[linder-2025-borzoi]] · [[lal-2026-decima]] · [[yuan-2022-scbasset]] · [[schep-2017-chromvar]] · [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/single-cell-atac-seq]]
