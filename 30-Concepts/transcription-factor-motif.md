---
type: concept
title: Transcription factor motif
aliases: [TF motif, position weight matrix, PWM, binding site]
tags: [transcription-factors, motif-analysis, regulatory-elements]
created: 2026-05-12
updated: 2026-10-08
---

# Transcription factor motif

> The DNA sequence pattern recognized and bound by a transcription factor, typically represented as a position weight matrix (PWM) or consensus sequence. Databases: JASPAR, cisBP, HOCOMOCO, TRANSFAC.

## Why it matters

- TF motif enrichment in accessible/methylated/marked regions identifies regulators of cell identity.
- [[30-Concepts/chromvar]] aggregates scATAC-seq signal by TF motif to extract robust per-cell TF activity.
- [[30-Concepts/cistopic]] reveals TF motif enrichment per topic.

## Added 2026-10-07

Aggregating single-cell accessibility across all sites of each TF motif is one of SCRAT's feature types for clustering and differential analysis of sparse regulome data [[10-Summaries/ji-2017-scrat]].

TF motifs can be scored per cell after training by embedding a motif's consensus k-mers into a learned k-mer/cell space, so motif choice does not bias the embedding ([[10-Summaries/tayyebi-2024-cellspace]]). The same space yielded 29 de novo motifs resembling haematopoietic CIS-BP motifs ([[10-Summaries/tayyebi-2024-cellspace]]).

GFETM groups k-mer and TF-motif features with CNNs as limited to short-range sequence context ([[10-Summaries/fan-2026-gfetm]]). In the bioRxiv v3 text, TF links come from conventional motif scanning: the top 100 peaks of each topic go through MEME-SEA with HOCOMOCO v11, linking IRF1/IRF2 to MEP topics, CTCF to CLP, MEP and monocyte topics, and ETV2/5/6 to a monocyte topic ([[10-Summaries/fan-2026-gfetm]]). The attention-based TF analysis mentioned in the published introduction is not in the preprint ([[10-Summaries/fan-2026-gfetm]]).

## Added 2026-10-08 — sequence models & foundation models

- DeepSEA predicted known TF-binding variant effects from sequence alone, e.g. increased FOXA1 binding at breast-cancer SNP rs4784227 and a new GATA1 site at an α-thalassemia SNP ([[10-Summaries/zhou-2015-deepsea]])
- Fine-tuned DNABERT separated binding sites of TAp73-α and TAp73-β, which share a motif, with accuracy 0.828 when given 500 bp of context ([[10-Summaries/ji-2021-dnabert]])
- genomicBERT's token attributions on bacterial promoters overlap known regulatory motifs (sigma-28 AAAGTT, TATA box), shown qualitatively without an enrichment statistic ([[10-Summaries/chen-2023-genomicbert]]).
- Bias-corrected ChromBPNet models found compact lexicons of 41–60 accessibility-driving motifs per ENCODE cell line, and their motif contribution scores tracked TF ChIP-derived occupancy (CTCF r > 0.89) far better than TOBIAS footprint scores (r = 0.2) ([[10-Summaries/pampari-2024-chrombpnet]])
- On a synthetic motif-order task, NucEL's global attention showed 65% and 152% higher maximum signal-to-noise at the two motifs than NT2-100M at equal accuracy ([[10-Summaries/ding-2025-nucel]]).
- Averaging a sequence's embedding with its reverse complement improved histone, enhancer and promoter prediction — non-palindromic motifs such as GATA/TATC otherwise have to be learned twice — but hurt splice-site prediction (donors 0.921 → 0.874), which is strand-specific ([[10-Summaries/duan-2025-janusdna]]).
- Integrated-Gradients attribution on a DNA language model fine-tuned for chromatin profiling recovered the ATF1 (TGACG), GATA2 (AGATAAG) and CTCF motifs, and de novo discovery on important tokens without a FIMO hit still returned those motifs, suggesting PWM scans miss divergent motif variants ([[10-Summaries/fishman-2025-gena-lm]]).
- Deleting motifs in silico with scooby gave per-cell TF scores that tracked TF expression better than chromVAR (P = 5.4e-9) or scBasset (P = 0.04), even when scooby was trained on scRNA-seq alone ([[10-Summaries/hingerl-2025-scooby]]).
- Conditioning a transformer on an ESM-2-3B embedding of the transcription factor rather than a factor-name label lets one model cover a continuous space of factors, and JASPAR scans show over 80% of its promoter-task outputs carry a GABPA, KLF4 or YY1 match ([[10-Summaries/su-2025-atgc-gen]]).
- In-silico motif insertion into a sequence foundation model recovered cell-type-specific TF activity (CEBPB in monocytes, GATA1 in MEPs, HOXA9 in HSCs), and saturation mutagenesis of a 100-bp β-globin enhancer recovered GATA1 and KLF1 with contributions rising along erythroid differentiation ([[10-Summaries/wang-2025-omnireg-gpt]]).
- TF binding instances predicted by the CREsted PBMC model reached average precision 0.75 against ChIP-seq and beat pycisTarget and pyChromVAR on precision and recall ([[10-Summaries/kempynck-2026-crested]]).
- UKBioFormer attribution around eQTL rs9910080 in a JUP enhancer recovered a JUN-class JASPAR motif (TGAGTCAC, p = 3.1e-5), illustrating motif discovery from a personal-expression model ([[10-Summaries/liu-2026-ukbiobert]]).

## Related

- [[30-Concepts/chromvar]] · [[30-Concepts/de-novo-motif-discovery]] · [[30-Concepts/scatac-seq]] · [[40-Topics/single-cell-atac-seq]]
