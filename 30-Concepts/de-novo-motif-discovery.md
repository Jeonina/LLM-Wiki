---
type: concept
title: De novo motif discovery
aliases: []
tags: [motif, regulatory-elements, transcription-factors]
created: 2026-05-12
updated: 2026-10-12
---

# De novo motif discovery

> The identification of previously unannotated TF binding motifs from sequence data (e.g., ChIP-seq peaks, accessible chromatin regions). Methods include MEME, HOMER, gimmemotifs, and k-mer-based approaches.

> [!abstract] 한눈에
> De novo motif discovery는 ChIP-seq peak나 열린 chromatin 서열에서 아직 주석되지 않은 TF 결합 motif를 찾는 일이다. k-mer 통계를 쓰는 방법 외에, Basset의 첫 층 filter나 DNABERT의 attention 같은 딥러닝 모델 내부에서도 motif를 뽑아낼 수 있다 ([[10-Summaries/kelley-2016-basset|Basset]]; [[10-Summaries/ji-2021-dnabert|DNABERT]]).

## Why it matters

- Reveals novel regulators in poorly-annotated cell types and species.
- [[30-Concepts/chromvar]]'s k-mer-based de novo motif assembly uses covariance between similar k-mers across cells to reconstruct motifs.
- BROCKMAN performs motif-agnostic analysis by PCA on gapped k-mer frequencies near Tn5 insertion sites and only afterwards maps PC loadings to TFs via CIS-BP PBM and PWM specificities, so cells differing by an uncharacterised TF can still be separated ([[10-Summaries/de-boer-2018-brockman|BROCKMAN]]). TFs co-enriched on the same PC showed 2.5× more high-confidence protein–protein interactions than expected ([[10-Summaries/de-boer-2018-brockman|BROCKMAN]]).
- Basset's 300 learned first-layer filters act as de novo motifs: 45% align to CIS-BP (TomTom q < 0.1), and clustering filter influence groups TP63/GRHL1/KLF filters with epithelial cells ([[10-Summaries/kelley-2016-basset|Basset]]).
- DNABERT-viz derives motifs from contiguous high-attention regions of a fine-tuned DNA language model; 1,595 of 1,999 motifs from ENCODE 690 TF ChIP-seq matched JASPAR 2018 (TOMTOM q < 0.01) ([[10-Summaries/ji-2021-dnabert|DNABERT]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/transcription-factor-motif|Transcription factor motif]] — The sequence patterns de novo discovery recovers.
> - `concept` [[30-Concepts/chromvar|chromVAR]] — k-mer covariance across cells to assemble motifs from scATAC.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Accessibility profiling in single cells, where motif analysis is a core step.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/de-boer-2018-brockman|de Boer & Regev 2018]]
> - [[10-Summaries/ji-2021-dnabert|DNABERT 2021]]
> - [[10-Summaries/kelley-2016-basset|Basset 2016]]
