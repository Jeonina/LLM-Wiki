---
type: summary
title: "Fu et al. 2025 — A foundation model of transcription across human cell types"
source: "[[00-Sources/papers/A foundation model of transcription across human cell types]]"
source_quality: full
source_sha256: "58fa2c4540bf0837cb0c5a05d54d94a9af53d6fb8c24ef39171d45715ad23f0f"
source_kind: paper
author: "Xi Fu, Shentong Mo, Alejandro Buendia, Anouchka P. Laurent, Anqi Shao, Maria del Mar Alvarez-Torres, … Raul Rabadan (17 authors)"
published: 2025-01-08
ingested: 2026-10-08
doi: "10.1038/s41586-024-08391-z"
journal: "Nature"
tags: [GET, general-expression-transformer, foundation-model, chromatin-accessibility, scATAC-seq, pseudobulk, motif-features, masked-pretraining, gene-expression-prediction, unseen-cell-types, lentiMPRA, enhancer-gene, fetal-hemoglobin, TF-TF-interaction, LiNGAM, AlphaFold, PAX5, B-ALL, LoRA]
entities: []
concepts: ["[[single-cell-foundation-model]]", "[[sequence-to-function-model]]", "[[chromatin-accessibility]]", "[[scatac-seq]]", "[[pseudo-bulk]]", "[[transcription-factor-motif]]", "[[cis-regulatory-element]]", "[[gene-regulatory-network]]", "[[hematopoietic-differentiation]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/single-cell-atac-seq]]", "[[40-Topics/computational-methods]]"]
---

**Citation:** Fu et al. (2025) — *A foundation model of transcription across human cell types* — *Nature*. [DOI](https://doi.org/10.1038/s41586-024-08391-z)

# Fu 2025 — GET

> GET (general expression transformer) predicts gene expression from **a cell type's accessible regions described by motifs**, not from raw sequence. Each input is 200 consecutive accessible peaks (about 2–4 Mb). Each peak is a 283-vector: summed MOODS match scores for 282 Vierstra motif clusters plus an optional accessibility value (log CPM, or a constant 1 in the "binary ATAC" model). A linear region embedding (768 dimensions) feeds 12 transformer layers that attend across peaks. Pretraining masks half of the peaks and reconstructs their motif features, using **pseudobulk scATAC-seq from 213 human fetal and adult cell types** (about 1.3 million nuclei). Fine-tuning swaps in an expression head (stranded log TPM per peak, non-promoter peaks labelled 0) on 153 cell types with matched RNA. Because cell identity is carried by which peaks are open, GET predicts expression in **cell types it never saw**: Pearson 0.94 on held-out astrocytes, in the range of experimental replicates (0.92–0.99). Interpretation (Jacobians over peaks and motifs) gives enhancer–gene links, upstream regulators and a causal motif–motif network, which with AlphaFold led to a PAX5–NR2C2 interaction tested in B-ALL cells.

## Key claims

- **Unseen cell types.** On left-out astrocytes (promoter-accessible genes), Pearson 0.94 (R² 0.88). Baselines: TSS accessibility r = 0.47, gene activity score r = 0.51, most-correlated training cell type r = 0.83, training mean r = 0.78. GET beat linear probing of Enformer CAGE outputs across fetal cell types and simpler ML models (MLP, CNN, CatBoost, SVM, random forest, linear) on the same inputs.
- **Pretraining is essential.** Without masked pretraining, held-out-astrocyte Pearson dropped to 0.6.
- **Generalisation.** Trained on fetal data only, mean R² 0.53 on adult cell types vs 0.33 using matched fetal types. Leave-one-chromosome-out: mean Pearson 0.78 (fetal astrocytes), 0.75 (one GBM tumour), 0.81 (K562 OmniATAC prediction). Fine-tuning on one GBM patient raised expression prediction in 16 held-out patients from 0.67 (zero-shot) to above 0.9.
- **Zero-shot lentiMPRA.** On K562 lentiMPRA (226,243 elements), GET fine-tuned on K562 OmniATAC + NEAT-seq gave Pearson 0.55 (slope 0.63) when combined with K562 accessibility and 0.45 (slope 0.38) from expression alone, vs Enformer 0.44 (slope 0.14). Enformer did better on enhancer and repressed elements. Enformer had to be subsampled to 2,000 elements to run in three days.
- **Long-range enhancers.** On base-editing data at fetal haemoglobin loci (*BCL11A*, *NFIX*, *KLF1*, *HBG2*) in fetal erythroblasts, GET beat Enformer, HyenaDNA, DeepSEA and ABC, especially for long-range enhancer–promoter pairs, including regions over 1 Mb away. Accessibility alone was good proximally but lost precision at distance. A K562 CRISPRi benchmark gave the same conclusion. GET flagged SOX motifs in the erythroid *BCL11A* enhancer and TAL1 as a regulator of *NFIX*.
- **Regulator targets.** The top GATA-motif target genes were enriched for "hemopoiesis" (adjusted P = 7.6 × 10⁻⁴) and included KLF1, GATA1, TAL1 and IKZF1.
- **TF–TF interactions.** LiNGAM causal discovery on a gene-by-motif importance matrix: the top 1% of pairs (n = 793) reached 25.2% precision against STRING physical interactions (correlation: 15.9%; random: 5.6%), close to a mass-spectrometry screen's 30.4% for its top 1.25%, and better than ChIP-seq or motif co-localisation baselines. A catalogue of 1,718 cell-type-specific TF pairs was folded with AlphaFold2. A predicted TFAP2A–ZFX IDR interaction was confirmed by co-immunoprecipitation (SRF negative).
- **PAX5 G183S.** In fetal B cells, GET linked the PAX motif to NR/3 motifs. AlphaFold placed PAX5's octapeptide region, including G183, at an NR-domain interface. BioID in REH B-ALL cells showed PAX5–NR2C2 binding (not NR4A1 or NR3C1), increased with the familial risk variant G183S. G183S-specific differentially expressed genes in patient samples were enriched for predicted NR/3 and PAX5 + NR/3 targets (fold 1.41 and 1.35).

## Methods / evidence

Data: fetal chromatin accessibility atlas (Domcke et al.), adult atlas (Zhang et al.), fetal expression atlas (Cao et al.) and Tabula Sapiens; pseudobulks from published Louvain clusters with more than 600 cells. When ATAC and RNA were not paired, expression was matched by cell type label. Motif features are computed offline, so the network never sees base-level sequence. Pretraining: 800 epochs on 16 V100s (about a week). Fine-tuning: 100 epochs on 8 A100s. LoRA adapters (about 99% fewer trainable parameters) for new assays or platforms; a K562 CAGE adapter trained in under 30 minutes on one RTX 3090. Enhancer–gene scoring: L2-norm of the region-embedding Jacobian weighted by accessibility, optionally combined with a Hi-C-trained distance "powerlaw" module. Wet-lab validation: co-IP in HeLa and BioID in REH cells. Code, checkpoints and a catalogue website are public.

Weight: strong held-out-cell-type design with honest baselines, plus experimental follow-up of one interaction. Cell types were defined by published clusters, and unpaired cell types used label-matched RNA. Many comparisons are in Extended Data figures that are images in the clipping; values here are those in the text. The Methods give inconsistent fine-tuning times (about 8 h vs about one day) and pretraining learning rates (1.5 × 10⁻⁴ vs 1 × 10⁻³), and the lentiMPRA compute statement (all elements in the same three days) differs from the Methods (about 5 days for about 200,000 elements). (synthesis)

## Limitations

**Authors' own:**
- Relies mainly on chromatin accessibility; cannot separate TF homologues with very similar motifs.
- Trained only on coarse cell states and region-level sequence summaries (motif scores), not nucleotide-level footprints.
- No 3D architecture, regulator expression or single-cell embeddings yet; few disease or perturbed states in pretraining.
- Variant effect prediction needs calibration with nucleotide-level perturbation data.
- The enhancer–gene benchmark is small relative to the genome-scale problem.
- Transfer to new platforms needs fine-tuning because of depth, peak-calling and library biases.

**Reviewer notes:**
- Because inputs are motif sums per peak, a single-nucleotide change only registers if it alters a motif match score. GET is weak by design for variant effects, which the authors acknowledge in other terms. (synthesis)
- "Unseen cell type" still requires that cell type's own ATAC profile at inference. The model transfers regulatory grammar, not the accessibility landscape itself. (synthesis)
- Expression is assigned only to promoter peaks and set to 0 elsewhere, so distal-enhancer attribution comes entirely from attention to promoter peaks. (synthesis)

## Surprising or load-bearing bits

- **Accessibility + motif summaries are enough** to reach replicate-level expression prediction in an unseen cell type, without base-resolution sequence models.
- **Pretraining on ATAC alone** lets the model use accessibility atlases that have no paired RNA, and is what makes held-out-cell-type prediction work (0.6 without it).
- **Model interpretation to wet lab.** The PAX5–NR2C2 result goes from attention-based motif interactions to AlphaFold to BioID, a rare end-to-end test of a foundation model's interpretive claim.

## Concepts touched

- [[single-cell-foundation-model]] — an epigenome foundation model pretrained on pseudobulk scATAC-seq of 213 cell types.
- [[sequence-to-function-model]] — compared with Enformer, DeepSEA and HyenaDNA; uses motif summaries instead of raw sequence.
- [[chromatin-accessibility]] / [[scatac-seq]] / [[pseudo-bulk]] — cell-type pseudobulk peaks as both input and context.
- [[cis-regulatory-element]] — long-range enhancer–gene identification at fetal haemoglobin loci and K562 CRISPRi.
- [[transcription-factor-motif]] / [[gene-regulatory-network]] — motif importance, regulator targets and causal TF–TF networks.
- [[hematopoietic-differentiation]] — fetal erythroblast regulators and B-lymphocyte PAX5 interactions.

## Connections to other sources

- Compared against [[avsec-2021-enformer]], [[zhou-2015-deepsea]] and [[nguyen-2023-hyenadna]]; earlier expression models [[zhou-2018-expecto]] and [[kelley-2018-basenji]] are cited as fixed to training cell types.
- Frames itself against transcriptome foundation models such as scGPT ([[cui-2024-natmethods]]).
- Context from accessibility is the counterpart to [[gao-2024-epigept]], which uses TF expression as context. (synthesis)
- Pseudobulk-level cell-type expression from sequence is also the approach of [[lal-2026-decima]], which uses raw 524-kb sequence and RNA only. (synthesis)
- Motif clusters follow Vierstra et al. (not in the wiki). Adult accessibility atlas is from the Ren lab (see [[zhang-2024-snapatac2]] for the same group's tooling). (synthesis)

## Open questions

- Can GET be extended to base-resolution input so that it scores single-nucleotide variants, including somatic ones? (synthesis)
- Would adding 3D contacts (the authors' suggestion) improve the long-range enhancer calls beyond the distance powerlaw?
- How sensitive are unseen-cell-type predictions to cluster definitions and peak calling in the new data?

## Related

- [[single-cell-foundation-model]] · [[sequence-to-function-model]] · [[gao-2024-epigept]] · [[lal-2026-decima]] · [[avsec-2021-enformer]] · [[cis-regulatory-element]] · [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/single-cell-atac-seq]]
