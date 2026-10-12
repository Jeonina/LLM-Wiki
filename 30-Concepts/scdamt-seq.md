---
type: concept
title: scDam&T-seq
aliases: [scDamT-seq, scDam and T-seq, single-cell DamID and transcriptome]
tags: [single-cell, multi-omics, DamID, CEL-Seq, IVT, linear-amplification]
created: 2026-05-15
updated: 2026-10-12
---

# scDam&T-seq

> **scDam&T-seq** is the first single-cell multi-omic method to jointly quantify **protein–DNA contacts** (via [[30-Concepts/damid|DamID]]) and the **transcriptome** (via CEL-Seq2-style mRNA capture) in the same cell ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).

> [!abstract] 한눈에
> scDam&T-seq는 Dam fusion 단백질이 남긴 m6A 흔적으로 protein–DNA contact를 읽고, 같은 세포의 mRNA도 함께 잡는 single-cell multi-omic 방법이다 ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]). gDNA와 cDNA를 한 번의 IVT 반응으로 선형 증폭하는 것이 핵심이고, Dam fusion clone을 만드는 일이 가장 큰 부담이다 ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]; [[10-Summaries/de-luca-2021-scdamid-protocol|de Luca 2021]]).

## Definition

Introduced by Rooijers et al. 2019 (Kind lab, Hubrecht) ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]). Its enabling trick is T7-promoter-based **linear amplification** of both gDNA (DamID-adapter-ligated fragments) and cDNA (poly-T primed mRNA) in the same in vitro transcription reaction — replacing PCR with IVT removes amplification bias and allows multi-molecule co-processing without nucleotide separation ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).

### Workflow

1. FACS single cell → 384-well, lyse.
2. RT with CEL-Seq2 primer (poly-T + UMI + barcode + T7) → 2nd-strand cDNA.
3. Proteinase K, then DpnI on m6A-GATC (only methylated where Dam–POI lived).
4. Ligate T7-bearing DamID adapter (UMI + barcode) to gDNA blunt ends.
5. Pool 384 wells; one IVT reaction amplifies both gDNA and cDNA molecules linearly.
6. Process amplified RNA into Illumina paired-end libraries.

## Why it matters

What you get from one cell:

- **DamID contacts** of the chosen Dam–POI per cell (median 42k unique GATC events / KBM7 cell).
- **Transcriptome** of the same cell (median ~2,300 detected genes; comparable to CEL-Seq alone).
- Allelic resolution if hybrid genomes are used (mouse 129/Sv × CAST/EiJ in the original paper) ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).

## Useful POI choices

| Dam–POI | What it reports |
|---|---|
| Dam-LMNB1 | Nuclear-lamina contacts / LADs |
| Untethered Dam | Accessible chromatin (CATaDa-style); includes gene bodies, not just TSSs |
| Dam-RING1B (RNF2) | Polycomb PRC1 binding; useful for X-inactivation, HOX regulation |
| Dam-TF | TF occupancy in single cells |

## Evidence and examples

Strengths vs related methods:

- **vs scNMT-seq** ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]): comparable nucleosome-positioning quality at ~30× shallower sequencing depth ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]). Untethered-Dam accessibility outperforms DNase at lowly expressed regions because it marks gene bodies (H3K36me3) not just promoters ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).
- **vs scATAC-seq** ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]): adds same-cell transcriptome + same-cell contact data for any Dam-tetherable protein, but at lower per-cell throughput.
- **vs scDamID alone** ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca 2021]]): same cells now carry mRNA; ~4× lower DamID complexity per cell offset by 100× throughput via IVT + robotics ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).

## Contested points

Limitations:

- Dam-fusion clone establishment is laborious (5–90% FACS survival ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca 2021]]); 10–60% clone pass rate).
- 12-h methylation window blurs short-lived contacts; inducible-degron Dam-fusion offers finer time control at the cost of more engineering ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca 2021]]; [[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).
- mRNA capture depth (~2,300 genes/cell) is below state-of-the-art scRNA-seq but sufficient for cell-type identification + allelic bias detection.

## Related

> [!cards]
> - `concept` [[30-Concepts/damid|DamID]] — Protein–DNA contact mapping from the m6A footprint of a Dam fusion.
> - `concept` [[30-Concepts/lamina-associated-domains|Lamina-associated domains]] — Large repressed regions that contact the nuclear lamina.
> - `concept` [[30-Concepts/nuclear-lamina|Nuclear lamina]] — The lamin meshwork lining the inner nuclear membrane.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — Whether a region of DNA is open or closed.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Two or more molecular modalities measured in the same cell.

## All sources on this page

> [!info]- 4 summaries cited here
> - [[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]
> - [[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]
> - [[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]
> - [[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]
