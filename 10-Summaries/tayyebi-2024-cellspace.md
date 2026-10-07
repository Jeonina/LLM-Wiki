---
type: summary
title: "Tayyebi et al. 2024 — Scalable and unbiased sequence-informed embedding of single-cell ATAC-seq data with CellSpace"
source: "[[00-Sources/papers/Scalable and unbiased sequence-informed embedding of single-cell ATAC-seq data with CellSpace]]"
source_kind: paper
author: "Zakieh Tayyebi, Allison R. Pine, Christina S. Leslie (corresponding)"
published: 2024-05-09
ingested: 2026-10-07
doi: "10.1038/s41592-024-02274-x"
journal: "Nature Methods 21(6):1014–1022"
tags: [CellSpace, scATAC-seq, embedding, StarSpace, k-mer, N-gram, negative-sampling, sequence-informed, TF-activity, batch-effect, integration, scBasset, SIMBA, PeakVI, ArchR, chromVAR, de-novo-motif]
entities: []
concepts: ["[[scatac-seq]]", "[[dimensionality-reduction]]", "[[batch-effect]]", "[[transcription-factor-motif]]", "[[de-novo-motif-discovery]]", "[[chromvar]]", "[[trajectory-inference]]", "[[clustering-algorithms]]", "[[hematopoietic-differentiation]]"]
topics: ["[[single-cell-atac-seq]]", "[[computational-methods]]"]
---

**Citation:** Tayyebi et al. (2024) — *Scalable and unbiased sequence-informed embedding of single-cell ATAC-seq data with CellSpace* — *Nature Methods* 21(6):1014–1022. [DOI](https://doi.org/10.1038/s41592-024-02274-x)

# Tayyebi 2024 — CellSpace

> Standard scATAC pipelines treat accessible regions as anonymous columns of a sparse cell-by-peak matrix, discarding the DNA sequence that makes them regulatory. **CellSpace** (Leslie lab) instead co-embeds **DNA k-mers and cells** in one latent space using StarSpace (an NLP embedding method): sample a 150 bp sequence from an accessible event, represent it as a bag of 8-mers plus **N-grams** (pairs within 3 consecutive k-mers), and pull it toward a cell where the event is accessible and away from K randomly sampled cells where it is not. Peaks are never embedded directly — which the authors credit for its strong, covariate-free **batch mitigation** — and any TF motif can be scored per cell afterwards by embedding its consensus k-mers, with no motif choice at training time.

## Key claims

- **Recovers hierarchies and mixes donors without a batch covariate.** On 2,154 CD34⁺ HSPCs (FACS ground truth; 50,000 variable 500 bp tiles), CellSpace reproduced the HSC/MPP → CMP→MEP and LMPP→CLP branches, with GMPs arising from both; Palantir from an HSC found six termini. Donors mixed, whereas ArchR iterative LSI split HSC/MPP by donor; scBasset had reported needing explicit batch modelling on this dataset.
- **Benchmarked (bootstrap, FDR-adjusted) against** ArchR itLSI (± Harmony), LSI on peaks (± Harmony), scBasset (± batch), SIMBA (peaks; peaks + k-mers + motifs; ± batch), PeakVI (± batch) and chromVAR (motifs or k-mers), using scib biological-conservation and batch metrics (overall = 0.6 bio + 0.4 batch). On the HSPC data CellSpace (tiles) significantly beat scBasset, all SIMBA variants, PeakVI, both chromVAR variants and uncorrected LSI; vs ArchR itLSI it won on batch score but tied on biological and overall score; it was comparable to Harmony-corrected LSI.
- **N-grams matter**: on 7,846 mouse fetal/adult mammary epithelial cells, N = 1 gave a diffuse embedding; N = 3 (default) resolved populations and fetal–adult relationships; N = 5 pulled populations further apart while staying correct.
- **Per-cell TF activity tracks expression**: on an 8,981-cell human cortex multiome, CellSpace motif scores correlated positively with the TF's RNA for 17/19 neurodevelopmental factors (scBasset 14/19), similar to chromVAR (e.g. PAX6 strongest in radial glia, where scBasset misplaced it); SIMBA's motif scores were mostly zero. scBasset failed to separate IN3 from glutamatergic neurons. On overall score CellSpace beat LSI, SIMBA (peaks), PeakVI and chromVAR but was not significantly better than SIMBA (peaks + k-mers + motifs) or scBasset (adjusted P = 0.087).
- **De novo motifs**: 10-mers frequently among cells' nearest neighbours were clustered and aligned into 29 de novo PWMs resembling relevant haematopoietic CIS-BP motifs.
- **Scales with constant memory**: training examples are generated on the fly from the sparse matrix + sequences, so runtime grows linearly and memory stays constant. Shown on ~63,000 haematopoietic cells (61,806 from 12 donors + 2,706 HSPCs; donors mixed), 37,818 basal-cell-carcinoma TME cells (seven patients; non-tumour cells mixed, tumour cells patient-specific), and ~720,000 fetal-atlas cells from 20 donors in three batches (d = 70).
- **Integrates datasets with different peak atlases**: cortex multiome ATAC + single-modal scATAC, each with its own atlas (only 31,800 overlapping variable peaks), combined by sampling negatives within batch — a case described as "uncorrectable" for standard matrix-based methods without reprocessing.
- **Not uniformly best**: on the large haematopoietic set, batch-corrected PeakVI significantly beat CellSpace overall (better biological score); on TME, CellSpace won all batch scores but mostly tied on biology/overall. The authors stress that no other *sequence-informed* method (i.e., one that can give batch-mitigated motif scores) outperformed it.

## Methods / evidence

StarSpace mode 0 in C++; defaults k = 8, d = 30, L = 150 bp, N = 3, 20 examples per event per epoch, 50 epochs; reverse-complement k-mers hashed together; margin ranking loss on cosine similarity. Cell graph via cosine distance → Seurat SNN/Louvain, UMAP. Motif score = z-scored cosine similarity between motif-k-mer bag and cell. Four public datasets plus a 720k atlas; 1,000-cell bootstrap resampling for CIs and pairwise tests.

Weight: comparisons are carefully done (bootstraps, FDR, with and without batch correction for each competitor), but ground-truth labels for the large datasets come from the original studies' own batch-corrected clustering — a caveat the authors state. Gains are clearest in batch mixing; biological-conservation wins are mixed.

## Surprising or load-bearing bits

- **Batch robustness comes from what is *not* embedded**: by updating cells through sequence content rather than peak identity, technical differences in peak calling or coverage partly wash out — a design argument rather than an explicit correction model.
- **Integrating across peak atlases** without a shared feature space is a practical capability most matrix-based tools lack.
- The authors frame CellSpace as an implicit version of scBasset (cells as classifiers of embedded sequences) with less expressive but less overfit-prone sequence features and no large-GPU requirement.
- Hyperparameter tell: a "cloudy" UMAP signals undertrained or under-dimensioned embeddings; variable tiles were easier to tune than peak atlases.

## Concepts touched

- [[scatac-seq]] — a third family of embeddings beyond LSI/topic models and VAEs: sequence-informed co-embedding.
- [[batch-effect]] — implicit, covariate-free mitigation; optional within-batch negative sampling for cross-atlas integration; Seurat anchors on the CellSpace space as a fallback.
- [[transcription-factor-motif]] / [[chromvar]] — motif activity as similarity in the learned space, chosen post hoc, comparable to chromVAR on expression correlation.
- [[de-novo-motif-discovery]] — motifs recovered from k-mer neighbourhoods of cell clusters.
- [[trajectory-inference]] — Palantir on the CellSpace embedding recovers haematopoietic termini.

## Connections to other sources

- Sequence-informed competitor: [[yuan-2022-scbasset]]; matrix-based competitors: [[granja-2021-archr]] (itLSI), [[ashuach-2022-peakvi]], [[schep-2017-chromvar]]; batch correction baseline [[korsunsky-2019-harmony]]; clustering via [[butler-2018-seurat-cca]]/Seurat.
- Later sequence-aware alternative that critiques k-mer models: [[fan-2026-gfetm]].
- Broader scATAC benchmarking context: [[luo-2024-scatac-benchmark]]; other embeddings: [[bravo-2019-cistopic]], [[xiong-2019-scale]], [[fang-2021-snapatac]], [[zhang-2024-snapatac2]].

## Open questions

- Consensus-k-mer motif embedding may not suit composite motifs; the authors suggest N-gram or ensemble motif representations.
- Extension to multiome (cells, genes and k-mers in one space) is proposed but not implemented; weighting sequence vs expression signal is unresolved.
- Whether implicit batch mitigation could also erase genuine biology that is sequence-content-similar across conditions (e.g. disease vs control states using the same TF families) is untested (synthesis).

## Related

- [[yuan-2022-scbasset]] · [[batch-effect]] · [[transcription-factor-motif]] · [[40-Topics/single-cell-atac-seq]]
