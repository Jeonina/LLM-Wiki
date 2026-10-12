---
type: concept
title: ChIP-seq
aliases: [chromatin immunoprecipitation sequencing]
tags: [chromatin, histone-modifications, transcription-factors, bulk]
created: 2026-05-12
updated: 2026-10-12
---

# ChIP-seq

> Chromatin immunoprecipitation sequencing. The bulk-cell standard for profiling protein-DNA interactions (histone marks, transcription factors). Cells are crosslinked, chromatin is fragmented (sonication), an antibody pulls down the target, immunoprecipitated DNA is sequenced.

> [!abstract] 한눈에
> ChIP-seq는 항체로 표적 단백질에 결합한 DNA를 면역침강해 시퀀싱하는 bulk 방법으로, 2007년에 이름이 붙은 뒤 Cistrome 같은 대규모 자료의 바탕이 되었다 ([[10-Summaries/barski-2007-histone-methylation-chip-seq|Barski 2007]]; [[10-Summaries/yu-2026-chrombert|ChromBERT]]). 다만 많은 세포가 필요하고, 농축 과정 때문에 정량 범위가 좁아진다 ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]).

## Definition

Workflow: formaldehyde crosslinking → chromatin shearing (sonication) → antibody pulldown → reverse crosslink → DNA purification → sequencing. Requires ~10⁶ cells per assay.

**Origin.** The term "ChIP-Seq" was introduced for direct Solexa sequencing of ChIP DNA from native MNase-digested mononucleosomes (17 PCR cycles; >20 M 36-bp tags per run), applied to 20 histone methylations, H2A.Z, Pol II and CTCF in human CD4⁺ T cells ([[10-Summaries/barski-2007-histone-methylation-chip-seq|Barski 2007]]). Note that this founding protocol used native (uncrosslinked) MNase chromatin for histone marks and crosslinked sonicated chromatin only for Pol II/CTCF ([[10-Summaries/barski-2007-histone-methylation-chip-seq|Barski 2007]]).

## Why it matters

- The reference method against which all newer chromatin-profiling methods ([[30-Concepts/cut-and-run|CUT&RUN]], [[30-Concepts/cut-and-tag|CUT&Tag]], [[30-Concepts/chic-seq|ChIC]], scCUT&Tag) are benchmarked.
- ENCODE and Roadmap Epigenomics built genome-wide histone-mark maps via ChIP-seq.
- High input requirement limits scalability and single-cell adaptation; CUT&Tag is replacing ChIP-seq in many labs.

## ChIP-seq data as model input

| Model | How it uses ChIP-seq | Finding | Source |
|---|---|---|---|
| ExPecto | Predicted TF and histone ChIP-seq features as expression-model inputs | Weighted over DNase features (P = 6.9e-25), suggesting accessibility alone carries less causal expression information | ([[10-Summaries/zhou-2018-expecto\|ExPecto]]) |
| ATGC-Gen | 10 million ENCODE ChIP-seq rows (340 factors, 129 cell types) turned into a conditional benchmark | 55,830 variable-length examples over 62 factors, split by chromosome | ([[10-Summaries/su-2025-atgc-gen\|ATGC-Gen]]) |
| HiCFoundation-epi | Predicts six 1-kb epigenomic tracks (ATAC, DNase, CTCF, H3K4me3, H3K27ac, H3K27me3) from Hi-C alone | Zeroing contacts at 392 convergent-CTCF loops lowered the predicted CTCF anchor signal in 97.8% of cases | ([[10-Summaries/wang-2026-hicfoundation\|HiCFoundation]]) |
| CANDI | Input-ablation analysis over histone tracks | H3K27me3 and H3K9me3 carried little information for imputing active marks; H3K27ac and H3K4me3 imputed with Pearson r > 0.8 in many cell types | ([[10-Summaries/foroozandeh-2025-candi\|CANDI]]) |
| ChromBERT | Each Cistrome ChIP-seq profile becomes five binding-status tokens per 1-kb bin | Learns regulator co-binding by masked reconstruction over 2,137,894 bins | ([[10-Summaries/yu-2026-chrombert\|ChromBERT]]) |

## Evidence and examples

- In R1:MEF mixing series, ChIP-seq H3K4me3 signal tracked cell proportion with R² 0.70/0.84 and was flat at intermediate ratios, versus 0.89/0.94 for deaminase-based DeChIC-seq ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]).
- CUT&RUN matched ORGANIC native ChIP dynamic range with ~10-fold fewer reads and outperformed crosslinked ChIP-seq on sensitivity/specificity ([[10-Summaries/skene-2017-cut-and-run|Skene 2017]]).

## Contested points

- **Enrichment compresses quantitative range.** The flat response at intermediate mixing ratios ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]) and CUT&RUN's better sensitivity/specificity ([[10-Summaries/skene-2017-cut-and-run|Skene 2017]]) both challenge ChIP-seq's role as the quantitative reference, even as it remains the benchmark standard (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/cut-and-run|CUT&RUN]] — Antibody-tethered MNase that reaches ChIP dynamic range with fewer reads.
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — pA-Tn5 tagmentation, replacing ChIP-seq in many labs.
> - `concept` [[30-Concepts/chic-seq|ChIC-seq]] — The 2004 antibody-tethered MNase method behind the CUT& family.
> - `concept` [[30-Concepts/deephistone|DeepHistone]] — CNN predicting seven histone marks from sequence and DNase.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone marks and how they are profiled.

## All sources on this page

> [!info]- 8 summaries cited here
> - [[10-Summaries/barski-2007-histone-methylation-chip-seq|Barski 2007]]
> - [[10-Summaries/foroozandeh-2025-candi|Foroozandeh 2025 CANDI]]
> - [[10-Summaries/shi-2026-dechic-seq|Shi 2026]]
> - [[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]
> - [[10-Summaries/su-2025-atgc-gen|ATGC-Gen 2025]]
> - [[10-Summaries/wang-2026-hicfoundation|HiCFoundation 2026]]
> - [[10-Summaries/yu-2026-chrombert|Yu 2026 ChromBERT]]
> - [[10-Summaries/zhou-2018-expecto|ExPecto 2018]]
