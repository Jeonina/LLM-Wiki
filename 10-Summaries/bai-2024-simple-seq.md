---
type: summary
title: "Bai et al. 2024 — SIMPLE-seq: joint single-cell 5mC and 5hmC at base resolution"
source: "[[00-Sources/papers/Simultaneous single-cell analysis of 5mC and 5hmC with SIMPLE-seq]]"
source_kind: paper
author: "Dongsheng Bai, Xiaoting Zhang, Huifen Xiang, Zijian Guo, Chenxu Zhu, Chengqi Yi (corresponding)"
published: 2024-02-09
ingested: 2026-05-12
doi: "10.1038/s41587-024-02148-9"
journal: "Nature Biotechnology"
tags: [DNA-methylation, 5mC, 5hmC, bisulfite-free, single-cell, TAPS, hmC-CATCH, Yi-lab]
entities:
  - "[[20-Entities/chengqi-yi]]"
  - "[[20-Entities/dongsheng-bai]]"
  - "[[20-Entities/chenxu-zhu]]"
concepts:
  - "[[30-Concepts/simple-seq]]"
  - "[[30-Concepts/5hmc]]"
  - "[[30-Concepts/dna-methylation]]"
  - "[[30-Concepts/taps]]"
  - "[[30-Concepts/tet-enzymes]]"
  - "[[30-Concepts/combinatorial-indexing]]"
topics:
  - "[[40-Topics/dna-methylation]]"
  - "[[40-Topics/single-cell-multiomics]]"
---

**Citation:** Bai et al. (2024) — *SIMPLE-seq: joint single-cell 5mC and 5hmC at base resolution* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-024-02148-9)

# Bai et al. 2024 — SIMPLE-seq

> Thesis: 5mC and 5hmC have distinct regulatory roles, but bisulfite-based methods conflate them. SIMPLE-seq orthogonally labels 5hmC (ruthenate oxidation → indanedione labeling) and 5mC (TET oxidation → borane reduction) to generate **two distinguishable C-to-T mutational signals on the same DNA molecule**, then uses combinatorial-indexing tagmentation to scale to thousands of single cells with single-base resolution. Applied to mouse ESCs, human PBMCs, and mouse brain to give the first joint single-cell maps of these two cytosine modalities.

## Key claims

- **Method**: bisulfite-free, sequential chemical labeling. A 5caC-pre-deposited primer records the 5hmC signal in a way that distinguishes it from 5mC signal in downstream amplicons.
- C-to-T conversion efficiency 86.9% (5mC) and 85.6% (5hmC). Background conversion of unmodified C: 0.06% (5hmC channel), 0.57% (5mC channel).
- Throughput: ~1,500 mESCs sequenced per experiment with ~313k 5mC reads and ~150k 5hmC reads per cell. Combinatorial indexing scales to 10⁴–10⁵ cells.
- **mESC 2i→serum transition**: cells with disordered 5mC/5hmC relationships (high "modification entropy") sit at the trajectory's midpoint and may correspond to transient reprogramming events. Type-2 5hmCG sites (paired with 5mCG on the same molecule) mark dynamic methylation; type-1 sites mark stable epigenetic states.
- **PBMC and mouse brain applications**: SIMPLE-seq resolves T cells, B cells, NK cells, monocytes by 5mCG; identifies 11 brain cell types (excitatory neurons, inhibitory neurons, astrocytes, oligodendrocytes, microglia, endothelial cells) using joint 5mC+5hmC.
- Compared to scDARESOME, scDyad-seq (restriction-enzyme based, one site per fragment), and Joint-snhmC-seq, **SIMPLE-seq captures multiple modifications from the same fragment with higher mappable read fractions** (>90% vs ~60% for Joint-snhmC-seq).

## Methods / evidence

Bisulfite-free chemistry derived from TAPS (5mC) and hmC-CATCH (5hmC). Combinatorial-indexing tagmentation. Applied to (a) 2i vs serum mESCs (~1,500 cells), (b) PBMCs (~2,110 cells), (c) mouse cortex (~4,767 cells).

## Surprising or load-bearing bits

- The **5caC-pre-deposited primer** is the key trick: it embeds an orthogonal mutational signature into the amplification primer so that products from the two labeling steps can be distinguished downstream — a clever way to encode workflow stage into the read structure itself.
- 5hmC alone is sufficient to separate mESC dynamic states; 5mC alone is sufficient for static differentiated cell types (PBMCs); both together are needed for tissues with abundant 5hmC like mouse brain.
- "Modification entropy" as a single-cell metric is a novel concept: high entropy ≈ ongoing active demethylation/remethylation; could serve as a biomarker for cell-fate plasticity.

## Connections to other sources

- Competes with [[10-Summaries/sequencing-dna-methylation-and-hydroxymethylation-at-co-occurring-chromatin-features]] (6-base-CUT&Tag): SIMPLE-seq is single-cell, whole-genome; 6B-C&T is bulk, histone-mark-targeted. They are complementary modalities.
- Extends single-cell methylation methods reviewed in [[10-Summaries/zachary-2013-naturereviewsgenetics]].
- The ChromVAR analysis used here is implemented in [[10-Summaries/chromvar-inferring-transcription-factor-associated-accessibility-from-single-cell-epigenomic-data]].

## Open questions

- Cannot yet pair with scRNA-seq from the same cell. Future work likely integrates with transcriptome.
- 87% conversion efficiency means ~13% false-negative rate per site; imputation helps but cell-resolution per-locus calls remain noisy.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-024-02148-9)
## Related

- [[40-Topics/dna-methylation]] · [[30-Concepts/5hmc]] · [[30-Concepts/taps]] · [[20-Entities/chengqi-yi]]
