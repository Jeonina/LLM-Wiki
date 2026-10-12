---
type: concept
title: Transcription factor motif
aliases: [TF motif, position weight matrix, PWM, binding site]
tags: [transcription-factors, motif-analysis, regulatory-elements]
created: 2026-05-12
updated: 2026-10-12
---

# Transcription factor motif

> The DNA sequence pattern recognized and bound by a transcription factor, typically represented as a position weight matrix (PWM) or consensus sequence. Databases: JASPAR, cisBP, HOCOMOCO, TRANSFAC (synthesis).

> [!abstract] 한눈에
> TF motif는 전사인자가 인식해 결합하는 DNA 서열 패턴이고, single-cell 데이터에서는 motif를 공유하는 부위의 신호를 모아 세포별 TF 활성을 추정하는 데 쓰인다 ([[10-Summaries/ji-2017-scrat|SCRAT]]; [[10-Summaries/tayyebi-2024-cellspace|CellSpace]]). 최근에는 서열 모델의 attribution과 in-silico 변이로 motif를 다시 찾아내며, 이 방식이 PWM scan이나 footprint보다 실제 결합을 더 잘 따라간다는 보고가 있다 ([[10-Summaries/pampari-2024-chrombpnet|ChromBPNet]]; [[10-Summaries/fishman-2025-gena-lm|GENA-LM]]).

## Definition

A transcription factor motif is the DNA sequence pattern a transcription factor recognizes and binds, typically represented as a position weight matrix (PWM) or consensus sequence and catalogued in databases such as JASPAR, cisBP, HOCOMOCO and TRANSFAC (synthesis). Conventional analyses scan sequences against these databases — for example MEME-SEA with HOCOMOCO v11 ([[10-Summaries/fan-2026-gfetm|GFETM]]) — while [[30-Concepts/de-novo-motif-discovery]] finds unannotated patterns.

## Why it matters

- TF motif enrichment in accessible, methylated or marked regions identifies regulators of cell identity (synthesis).
- [[30-Concepts/chromvar]] aggregates scATAC-seq signal by TF motif to extract robust per-cell TF activity (synthesis).
- [[30-Concepts/cistopic]] reveals TF motif enrichment per topic (synthesis).

## Approaches

### Motif features in single-cell data

| Approach | Example | How motifs enter | Source |
|---|---|---|---|
| Aggregate accessibility over all sites of a motif | [[10-Summaries/ji-2017-scrat\|SCRAT]], [[30-Concepts/chromvar\|chromVAR]] | Motif-site aggregates are one of SCRAT's feature types for clustering and differential analysis of sparse regulome data | ([[10-Summaries/ji-2017-scrat\|SCRAT]]) |
| Score motifs after training in a learned k-mer/cell space | [[10-Summaries/tayyebi-2024-cellspace\|CellSpace]] | A motif's consensus k-mers are embedded into the space, so motif choice does not bias the embedding | ([[10-Summaries/tayyebi-2024-cellspace\|CellSpace]]) |
| Motif scanning of topic peaks | [[10-Summaries/fan-2026-gfetm\|GFETM]], [[30-Concepts/cistopic\|cisTopic]] | Top 100 peaks of each topic go through MEME-SEA with HOCOMOCO v11 | ([[10-Summaries/fan-2026-gfetm\|GFETM]]) |
| In-silico motif deletion in a sequence-to-profile model | [[10-Summaries/hingerl-2025-scooby\|scooby]] | Per-cell TF scores from deleting motifs in silico | ([[10-Summaries/hingerl-2025-scooby\|scooby]]) |

### Motifs recovered from sequence models

| Approach | Example | What was recovered | Source |
|---|---|---|---|
| Variant-effect prediction from sequence | [[10-Summaries/zhou-2015-deepsea\|DeepSEA]] | Known TF-binding variant effects (FOXA1, GATA1) | ([[10-Summaries/zhou-2015-deepsea\|DeepSEA]]) |
| Fine-tuned language-model classifier | [[10-Summaries/ji-2021-dnabert\|DNABERT]] | Binding sites of two TAp73 isoforms that share a motif | ([[10-Summaries/ji-2021-dnabert\|DNABERT]]) |
| Token attribution | [[10-Summaries/chen-2023-genomicbert\|genomicBERT]] | Bacterial promoter motifs (sigma-28 AAAGTT, TATA box) | ([[10-Summaries/chen-2023-genomicbert\|genomicBERT]]) |
| Contribution scores from bias-corrected accessibility models | [[10-Summaries/pampari-2024-chrombpnet\|ChromBPNet]] | Compact lexicons of accessibility-driving motifs per cell line | ([[10-Summaries/pampari-2024-chrombpnet\|ChromBPNet]]) |
| Global attention on a synthetic motif-order task | [[10-Summaries/ding-2025-nucel\|NucEL]] | Signal at the two planted motifs | ([[10-Summaries/ding-2025-nucel\|NucEL]]) |
| Integrated-Gradients attribution plus de novo discovery | [[10-Summaries/fishman-2025-gena-lm\|GENA-LM]] | ATF1 (TGACG), GATA2 (AGATAAG) and CTCF motifs | ([[10-Summaries/fishman-2025-gena-lm\|GENA-LM]]) |
| In-silico motif insertion and saturation mutagenesis | [[10-Summaries/wang-2025-omnireg-gpt\|OmniReg-GPT]] | Cell-type-specific TF activity; GATA1 and KLF1 in a β-globin enhancer | ([[10-Summaries/wang-2025-omnireg-gpt\|OmniReg-GPT]]) |
| Predicted binding instances from an enhancer model | [[10-Summaries/kempynck-2026-crested\|CREsted]] | TF binding instances benchmarked against ChIP-seq | ([[10-Summaries/kempynck-2026-crested\|CREsted]]) |
| Attribution in a personal-expression model | [[10-Summaries/liu-2026-ukbiobert\|UKBioFormer]] | A JUN-class JASPAR motif around an eQTL | ([[10-Summaries/liu-2026-ukbiobert\|UKBioFormer]]) |
| Factor-conditioned sequence generation | [[10-Summaries/su-2025-atgc-gen\|ATGC-Gen]] | Conditions on an ESM-2-3B embedding of the TF rather than a factor-name label, so one model covers a continuous space of factors | ([[10-Summaries/su-2025-atgc-gen\|ATGC-Gen]]) |

## Evidence and examples

**Single-cell motif scoring**

- The CellSpace k-mer/cell space yielded 29 de novo motifs resembling haematopoietic CIS-BP motifs ([[10-Summaries/tayyebi-2024-cellspace|CellSpace]]).
- GFETM's motif scanning linked IRF1/IRF2 to MEP topics, CTCF to CLP, MEP and monocyte topics, and ETV2/5/6 to a monocyte topic ([[10-Summaries/fan-2026-gfetm|GFETM]]).
- scooby's per-cell TF scores tracked TF expression better than chromVAR (P = 5.4e-9) or scBasset (P = 0.04), even when scooby was trained on scRNA-seq alone ([[10-Summaries/hingerl-2025-scooby|scooby]]).

**Motifs from sequence models**

- DeepSEA predicted increased FOXA1 binding at breast-cancer SNP rs4784227 and a new GATA1 site at an α-thalassemia SNP from sequence alone ([[10-Summaries/zhou-2015-deepsea|DeepSEA]]).
- Fine-tuned DNABERT separated binding sites of TAp73-α and TAp73-β, which share a motif, with accuracy 0.828 when given 500 bp of context ([[10-Summaries/ji-2021-dnabert|DNABERT]]).
- genomicBERT's attribution overlap with bacterial promoter motifs was shown qualitatively, without an enrichment statistic ([[10-Summaries/chen-2023-genomicbert|genomicBERT]]).
- Bias-corrected ChromBPNet models found 41–60 accessibility-driving motifs per ENCODE cell line, and their motif contribution scores tracked TF ChIP-derived occupancy (CTCF r > 0.89) far better than TOBIAS footprint scores (r = 0.2) ([[10-Summaries/pampari-2024-chrombpnet|ChromBPNet]]).
- On a synthetic motif-order task, NucEL's global attention showed 65% and 152% higher maximum signal-to-noise at the two motifs than NT2-100M at equal accuracy ([[10-Summaries/ding-2025-nucel|NucEL]]).
- Averaging a sequence's embedding with its reverse complement improved histone, enhancer and promoter prediction — non-palindromic motifs such as GATA/TATC otherwise have to be learned twice — but hurt splice-site prediction (donors 0.921 → 0.874), which is strand-specific ([[10-Summaries/duan-2025-janusdna|JanusDNA]]).
- In GENA-LM, de novo discovery on important tokens without a FIMO hit still returned CTCF and GATA2 motifs ([[10-Summaries/fishman-2025-gena-lm|GENA-LM]]).
- OmniReg-GPT's motif insertion recovered CEBPB in monocytes, GATA1 in MEPs and HOXA9 in HSCs, and mutagenesis of a 100-bp β-globin enhancer recovered GATA1 and KLF1 with contributions rising along erythroid differentiation ([[10-Summaries/wang-2025-omnireg-gpt|OmniReg-GPT]]).
- CREsted PBMC binding instances reached average precision 0.75 against ChIP-seq and beat pycisTarget and pyChromVAR on precision and recall ([[10-Summaries/kempynck-2026-crested|CREsted]]).
- UKBioFormer attribution around eQTL rs9910080 in a JUP enhancer recovered a JUN-class JASPAR motif (TGAGTCAC, p = 3.1e-5) ([[10-Summaries/liu-2026-ukbiobert|UKBioFormer]]).
- JASPAR scans show over 80% of ATGC-Gen's promoter-task outputs carry a GABPA, KLF4 or YY1 match ([[10-Summaries/su-2025-atgc-gen|ATGC-Gen]]).

## Contested points

- **PWM scans may miss divergent motif variants.** GENA-LM's de novo discovery on tokens without a FIMO hit still returned known motifs, which the authors read as PWM scans missing divergent variants ([[10-Summaries/fishman-2025-gena-lm|GENA-LM]]).
- **Footprints versus model contributions.** ChromBPNet contribution scores tracked ChIP-derived occupancy far better than TOBIAS footprint scores ([[10-Summaries/pampari-2024-chrombpnet|ChromBPNet]]).
- **Short-range context.** GFETM groups k-mer and TF-motif features with CNNs as limited to short-range sequence context ([[10-Summaries/fan-2026-gfetm|GFETM]]).
- **Published versus preprint TF analysis.** In GFETM's bioRxiv v3 text, TF links come from conventional motif scanning; the attention-based TF analysis mentioned in the published introduction is not in the preprint ([[10-Summaries/fan-2026-gfetm|GFETM]]).
- **Strand symmetry is task-dependent.** Reverse-complement averaging helps tasks driven by non-palindromic motifs but hurts strand-specific splice sites ([[10-Summaries/duan-2025-janusdna|JanusDNA]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/chromvar|chromVAR]] — Per-cell bias-corrected deviation scores over peaks sharing a TF motif.
> - `concept` [[30-Concepts/cistopic|cisTopic]] — LDA topic modelling of scATAC-seq, with motif enrichment per topic.
> - `concept` [[30-Concepts/de-novo-motif-discovery|De novo motif discovery]] — Finding previously unannotated TF binding motifs from sequence data.
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Genome-wide chromatin accessibility in individual cells via Tn5 insertion.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Assays and analysis of sparse single-cell accessibility data.

## All sources on this page

> [!info]- 15 summaries cited here
> - [[10-Summaries/chen-2023-genomicbert|genomicBERT 2023]]
> - [[10-Summaries/ding-2025-nucel|NucEL 2025]]
> - [[10-Summaries/duan-2025-janusdna|JanusDNA 2025]]
> - [[10-Summaries/fan-2026-gfetm|Fan 2026]]
> - [[10-Summaries/fishman-2025-gena-lm|GENA-LM 2025]]
> - [[10-Summaries/hingerl-2025-scooby|scooby 2025]]
> - [[10-Summaries/ji-2017-scrat|Ji 2017]]
> - [[10-Summaries/ji-2021-dnabert|DNABERT 2021]]
> - [[10-Summaries/kempynck-2026-crested|CREsted 2026]]
> - [[10-Summaries/liu-2026-ukbiobert|UKBioBERT 2026]]
> - [[10-Summaries/pampari-2024-chrombpnet|ChromBPNet 2024]]
> - [[10-Summaries/su-2025-atgc-gen|ATGC-Gen 2025]]
> - [[10-Summaries/tayyebi-2024-cellspace|Tayyebi 2024]]
> - [[10-Summaries/wang-2025-omnireg-gpt|OmniReg-GPT 2025]]
> - [[10-Summaries/zhou-2015-deepsea|DeepSEA 2015]]
