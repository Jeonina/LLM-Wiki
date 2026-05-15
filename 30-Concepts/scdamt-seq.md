---
type: concept
title: scDam&T-seq
aliases: [scDamT-seq, scDam and T-seq, single-cell DamID and transcriptome]
tags: [single-cell, multi-omics, DamID, CEL-Seq, IVT, linear-amplification]
created: 2026-05-15
updated: 2026-05-15
---

# scDam&T-seq

> **scDam&T-seq** is the first single-cell multi-omic method to jointly quantify **protein–DNA contacts** (via [[30-Concepts/damid|DamID]]) and the **transcriptome** (via CEL-Seq2-style mRNA capture) in the same cell. Introduced by Rooijers et al. 2019 (Kind lab, Hubrecht). Its enabling trick is T7-promoter-based **linear amplification** of both gDNA (DamID-adapter-ligated fragments) and cDNA (poly-T primed mRNA) in the same in vitro transcription reaction — replacing PCR with IVT removes amplification bias and allows multi-molecule co-processing without nucleotide separation.

## Workflow

1. FACS single cell → 384-well, lyse.
2. RT with CEL-Seq2 primer (poly-T + UMI + barcode + T7) → 2nd-strand cDNA.
3. Proteinase K, then DpnI on m6A-GATC (only methylated where Dam–POI lived).
4. Ligate T7-bearing DamID adapter (UMI + barcode) to gDNA blunt ends.
5. Pool 384 wells; one IVT reaction amplifies both gDNA and cDNA molecules linearly.
6. Process amplified RNA into Illumina paired-end libraries.

## What you get

- **DamID contacts** of the chosen Dam–POI per cell (median 42k unique GATC events / KBM7 cell).
- **Transcriptome** of the same cell (median ~2,300 detected genes; comparable to CEL-Seq alone).
- Allelic resolution if hybrid genomes are used (mouse 129/Sv × CAST/EiJ in the original paper).

## Useful POI choices

| Dam–POI | What it reports |
|---|---|
| Dam-LMNB1 | Nuclear-lamina contacts / [[30-Concepts/lamina-associated-domains\|LADs]] |
| Untethered Dam | Accessible chromatin (CATaDa-style); includes gene bodies, not just TSSs |
| Dam-RING1B (RNF2) | Polycomb PRC1 binding; useful for X-inactivation, HOX regulation |
| Dam-TF | TF occupancy in single cells |

## Strengths vs related methods

- **vs scNMT-seq** ([[10-Summaries/clark-2018-scnmt]]): comparable nucleosome-positioning quality at ~30× shallower sequencing depth. Untethered-Dam accessibility outperforms DNase at lowly expressed regions because it marks gene bodies (H3K36me3) not just promoters.
- **vs scATAC-seq** ([[10-Summaries/buenrostro-2015-nature]]): adds same-cell transcriptome + same-cell contact data for any Dam-tetherable protein, but at lower per-cell throughput.
- **vs scDamID alone** ([[10-Summaries/de-luca-2021-scdamid-protocol]]): same cells now carry mRNA; ~4× lower DamID complexity per cell offset by 100× throughput via IVT + robotics.

## Limitations

- Dam-fusion clone establishment is laborious (5–90% FACS survival; 10–60% clone pass rate).
- 12-h methylation window blurs short-lived contacts; inducible-degron Dam-fusion offers finer time control at the cost of more engineering.
- mRNA capture depth (~2,300 genes/cell) is below state-of-the-art scRNA-seq but sufficient for cell-type identification + allelic bias detection.

## Related

- [[30-Concepts/damid]] · [[30-Concepts/lamina-associated-domains]] · [[30-Concepts/nuclear-lamina]] · [[30-Concepts/chromatin-accessibility]] · [[30-Concepts/single-cell-multiomics]]
- Anchor source: [[10-Summaries/rooijers-2019-scdamt-seq]]
- Protocol companion: [[10-Summaries/de-luca-2021-scdamid-protocol]]
