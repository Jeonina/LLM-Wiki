---
type: concept
title: Transposable elements
aliases: [TEs, retrotransposons, LINE-1, SINE Alu, ERVs]
tags: [genome, repeats, retrotransposition, methylation]
created: 2026-05-12
updated: 2026-10-12
---

# Transposable elements (TEs)

> DNA sequences that can replicate and insert themselves at new genomic locations. Comprise ~50% of the human genome. Most are inactive relics; some — particularly LINE-1, SINE Alu, and a few ERVs — remain "hot" and can still mobilize.

> [!abstract] 한눈에
> 전이인자(TE)는 유전체의 새 위치로 복제·삽입될 수 있는 서열로, 대부분은 DNA methylation과 H3K9me3로 억제되어 있다. 서로 98% 이상 같은 복사본은 short read로 구별되지 않지만, long-read single-cell assay는 개별 복사본의 accessibility와 histone mark를 따로 읽어 낸다 ([[10-Summaries/li-2025-scnanoatac-seq2|Li 2025]]; [[10-Summaries/li-2024-scnanoseq-cut-tag|scNanoSeq-CUT&Tag]]).

## Definition

Major families:
- **LINE-1 (L1)**: ~17% of human genome; full-length L1Hs elements can autonomously retrotranspose.
- **SINE Alu**: ~11% of human genome; uses LINE-1 machinery for retrotransposition.
- **ERVs** (endogenous retroviruses): ~8% of genome; mostly inactive but some encode functional Env proteins.

## Why it matters

- TEs are kept silenced by DNA methylation (especially at internal promoters) and H3K9me3 heterochromatin.
- Loss of TE silencing in cancer triggers [[30-Concepts/viral-mimicry]] innate immune responses.
- L1 retrotransposition in neurons contributes to somatic genomic mosaicism (synthesis).
- TE methylation serves as a surrogate for global methylation status (basis of [[30-Concepts/sctem-seq]]).

## Ways of reading TEs

| Approach | Example | What it shows | Source |
|---|---|---|---|
| Long-read single-cell ATAC | [[10-Summaries/li-2025-scnanoatac-seq2\|Li 2025]] | Accessibility of individual repeat copies, including LINE1 or MERVL copies with >98% identity that short reads cannot resolve | ([[10-Summaries/li-2025-scnanoatac-seq2\|Li 2025]]) |
| Long-read single-cell CUT&Tag | [[10-Summaries/li-2024-scnanoseq-cut-tag\|scNanoSeq-CUT&Tag]] | Histone marks on individual transposable-element copies | ([[10-Summaries/li-2024-scnanoseq-cut-tag\|scNanoSeq-CUT&Tag]]) |
| Sequence-to-folding model | [[10-Summaries/fudenberg-2020-akita\|Akita]] | Whether CTCF sites in B2 SINEs affect predicted 3D folding | ([[10-Summaries/fudenberg-2020-akita\|Akita]]) |
| DNA language model | [[10-Summaries/sanabria-2024-grover\|GROVER]] | Repeat structure learned from sequence alone | ([[10-Summaries/sanabria-2024-grover\|GROVER]]) |
| Learned DNA tokenizer | [[10-Summaries/kim-2026-dnachunker\|DNAChunker]] | Chunk length that tracks repeat redundancy | ([[10-Summaries/kim-2026-dnachunker\|DNAChunker]]) |

## Evidence and examples

**Individual copies in single cells**

- 157 of 16,882 full-length LINE1s are activated from zygote to morula, 4.3-fold enriched in the A compartment ([[10-Summaries/li-2025-scnanoatac-seq2|Li 2025]]).
- LINE1 or MERVL copies with >98% identity can differ in accessibility, which short reads cannot resolve ([[10-Summaries/li-2025-scnanoatac-seq2|Li 2025]]).
- Long-read single-cell CUT&Tag reached 96.5% mappability/discernibility for 320 full-length L1Hs elements with >99% pairwise identity ([[10-Summaries/li-2024-scnanoseq-cut-tag|scNanoSeq-CUT&Tag]]).
- K562 cells treated with 5-azacytidine gained H3K27ac on 201 individual repeats, all of the 102 checked having lost DNA methylation ([[10-Summaries/li-2024-scnanoseq-cut-tag|scNanoSeq-CUT&Tag]]).
- H3K4me3-marked L1Md elements peaked at the Sperm1 stage of mouse spermatogenesis ([[10-Summaries/li-2024-scnanoseq-cut-tag|scNanoSeq-CUT&Tag]]).

**Sequence models and foundation models**

- A human-trained Akita model mispredicts mouse folding where B2 SINEs carry CTCF sites, while a mouse-trained model learns they have little effect, consistent with ChAHP blocking CTCF binding in B2 SINEs ([[10-Summaries/fudenberg-2020-akita|Akita]]).
- In GROVER, some BPE tokens localise almost exclusively to repeats, and embeddings of ~2 kb windows separate LINEs, SINEs/Alus, LTRs and satellites by class and orientation ([[10-Summaries/sanabria-2024-grover|GROVER]]).
- DNAChunker assigns longer chunks to young, low-divergence SINE copies than to old ones (about 32 vs 17 bp median), so chunk length tracks repeat redundancy ([[10-Summaries/kim-2026-dnachunker|DNAChunker]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/viral-mimicry|Viral mimicry]] — Interferon response triggered when demethylated retrotransposons form dsRNA.
> - `concept` [[30-Concepts/sctem-seq|scTEM-seq]] — Low-cost single-cell global methylation from SINE Alu amplicons.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC at CpG dinucleotides, its maintenance, and how it is measured.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one organism.

## All sources on this page

> [!info]- 5 summaries cited here
> - [[10-Summaries/fudenberg-2020-akita|Akita 2020]]
> - [[10-Summaries/kim-2026-dnachunker|DNAChunker 2026]]
> - [[10-Summaries/li-2024-scnanoseq-cut-tag|Li 2024]]
> - [[10-Summaries/li-2025-scnanoatac-seq2|Li 2025]]
> - [[10-Summaries/sanabria-2024-grover|GROVER 2024]]
