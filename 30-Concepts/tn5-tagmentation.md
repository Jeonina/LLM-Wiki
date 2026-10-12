---
type: concept
title: Tn5 tagmentation
aliases: [Tn5 transposition, tagmentation, Tn5]
tags: [transposase, library-prep, ATAC-seq]
created: 2026-05-12
updated: 2026-10-12
---

# Tn5 tagmentation

> The simultaneous fragmentation and adapter insertion of DNA by Tn5 transposase: a hyperactive Tn5 variant loaded with adapter-containing oligos cuts dsDNA and inserts the adapters in a single enzymatic reaction.

> [!abstract] 한눈에
> Tn5 tagmentation은 adapter를 실은 Tn5 transposase가 DNA를 자르면서 동시에 adapter를 붙이는 반응이고, ATAC-seq, CUT&Tag, 증폭 없는 scWGS 같은 single-cell 방법 대부분이 이 반응 위에 서 있다 ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). Tn5에는 염기서열 선호와 열린 염색질 선호라는 서로 다른 두 편향이 있어서, 항체로 표적을 정하는 assay에서도 accessibility 신호가 섞여 들어온다 ([[10-Summaries/hu-2026-patty|PATTY]]; [[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]).

## Definition

Tn5 is an *Escherichia coli* transposase. Each transposition introduces a 9-nt gap into the target DNA and inserts the loaded adapter at both ends of the resulting fragment. Library prep that takes hours of fragmentation plus ligation in conventional workflows takes ~30 minutes with Tn5.

## Why it matters

- It is the foundation of ATAC-seq (Tn5 preferentially cuts open chromatin) and of many low-input methods.
- It is single-cell adaptable: pA-Tn5 enables CUT&Tag, and concentration tuning enables size control in SMRT-Tag.
- Standard Tn5 libraries do not preserve strand pairing for [[40-Topics/duplex-sequencing]], although the Tn5-based META-CS achieves duplex calling in single cells ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

## Tn5 configurations

| Use | Example | How Tn5 is loaded or deployed | Source |
|---|---|---|---|
| Accessibility | [[30-Concepts/atac-seq]], [[30-Concepts/micro-atac-seq]] | Hyperactive Tn5 inserts adapters into accessible chromatin | — |
| Antibody-tethered tagmentation | [[30-Concepts/cut-and-tag]], [[30-Concepts/scicut-tag]] | pA-Tn5 tethered to a histone-mark antibody | — |
| Barcoding at tagmentation | [[10-Summaries/wang-2019-cobatch\|CoBATCH]] | PA-Tn5 pre-assembled with well-specific barcoded adapters, so the cell barcode enters during antibody-tethered tagmentation itself | ([[10-Summaries/wang-2019-cobatch\|CoBATCH]]) |
| Single-well CUT&Tag | [[10-Summaries/schwager-2026-onecell-cut-tag\|OneCell CUT&Tag]] | Commercial pA-Tn5 or in-house Nano-Tn5 inside single wells | ([[10-Summaries/schwager-2026-onecell-cut-tag\|Schwager 2026]]) |
| Proximity-ligated chromatin | [[10-Summaries/chang-2025-droplet-hi-c\|Droplet Hi-C]] | SDS-treated in situ Hi-C nuclei run through the 10x scATAC tagmentation workflow | ([[10-Summaries/chang-2025-droplet-hi-c\|Chang 2025]]) |
| Methylome indexing | [[10-Summaries/nichols-2025-scimetv3\|sciMETv3]] | Tn5 loaded with fully methylated adapters | ([[10-Summaries/nichols-2025-scimetv3\|sciMETv3]]) |
| Methylome + accessibility | sciMET+ATAC | Two sequential tagmentations (native, then after nucleosome disruption) split accessible from total DNA | ([[10-Summaries/nichols-2025-scimetv3\|sciMETv3]]) |
| Genome + accessibility | [[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]] | Tn5-1 tagments open chromatin in intact permeabilised nuclei; Tn5-2, with a different adapter set, tagments the remaining DNA after in-well protease removal of chromatin; modality-specific PCR separates the ATAC and DNA libraries | ([[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]]) |
| Genome + accessibility, long read | [[10-Summaries/pancikova-2025-splongget\|SPLONGGET]] | Retains all fragment sizes, giving DNA libraries of 200 bp to >10 kb with whole-genome coverage alongside the ATAC signal; only reads under 1 kb are used for accessibility | ([[10-Summaries/pancikova-2025-splongget\|SPLONGGET]]) |
| Duplex calling in single cells | [[10-Summaries/xing-2021-meta-cs\|META-CS]] | An equimolar mix of 16 transposon sequences, so each fragment carries two random tags | ([[10-Summaries/xing-2021-meta-cs\|META-CS]]) |
| Long-read low-input libraries | [[30-Concepts/smrt-tag]] | Concentration tuning controls fragment size | — |
| Joint methylation + accessibility | [[30-Concepts/splicool-seq]] | Listed as a Tn5-based method | — |
| Amplification-free scWGS | DLP+, DnTR-Seq in [[10-Summaries/wesley-2026-songbird\|Songbird]]; direct tagmentation in [[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]] | Tagmentation without preamplification, so fragment overlaps carry copy-number information | ([[10-Summaries/wesley-2026-songbird\|Songbird]]; [[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]]) |

## Biases

- **Two distinct Tn5 biases.** Sequence-level cleavage preference and chromatin-level preference for accessible DNA are separable; the latter confounds antibody-targeted assays such as CUT&Tag and cannot be removed by sequence models alone ([[10-Summaries/hu-2026-patty|PATTY]]).
- **Sequence preference distorts profile shape.** ChromBPNet showed that Tn5 sequence preference distorts ATAC-seq profile shape but not total counts in peaks, that +4/−4 read shifts align strand-specific Tn5 bias best, and that experiment-matched chromatin-background bias models correct it better than naked-DNA models, TOBIAS or HINT-ATAC ([[10-Summaries/pampari-2024-chrombpnet|ChromBPNet]]).
- **Size selection shapes the accessibility signal.** Tn5 tagmentation of nuclei yields fragments from ~35 bp to several kbp; standard bead clean-ups, PCR and Illumina sequencing keep only the short ones, which is why ATAC libraries look enriched for open chromatin ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).

## Copy number from fragment overlap

- Without preamplification, Tn5 tagmentation destroys the template, so two overlapping fragments must come from different copies; in a haploid region every overlap is an artefact, and overlap becomes more common at higher ploidy in a predictable way ([[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]).
- ASCENT uses this to call absolute copy number in single cells ([[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]); see [[30-Concepts/copy-number-variation]].
- Fragment-overlap ploidy estimation transfers to DnTR-Seq; for LIANTI and SmoothSeq it needed protocol-specific deduplication windows of 10 and 100 nt ([[10-Summaries/wesley-2026-songbird|Songbird]]).

## Evidence and examples

- Nearly all H3K27ac CUT&Tag regions fell in H3K27ac sites shared with ATAC peaks, and removing <100-bp fragments reduced H3K27ac reads in ATAC peaks from 29% to 20% ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]).
- Bulk ChIP vs Tn5-based ChIL-seq correlations for H3K27me3 were only r = 0.26–0.31, versus r = 0.67 for MNase-based scChIC-seq ([[10-Summaries/ludwig-2019-sc-chromatin-modifications-review|Ludwig 2019]]).
- Droplet Hi-C reports minimal open-chromatin bias in its Tn5-fragmented contact data ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]).
- In META-CS the two random tags act as fragment barcodes and reduce the amplification loss from intramolecular hairpins that form when both ends carry the same sequence; strand identity comes from later primer-extension rounds, not from the tagmentation step itself ([[10-Summaries/xing-2021-meta-cs|META-CS]]).
- In DLP+ scWGS, same-start, different-length fragment pairs are amplified 1:1 or 1:2, which places their origin before or within the first PCR cycle ([[10-Summaries/wesley-2026-songbird|Songbird]]).
- Overlap at copy state 1 was higher on patterned flow cells (NovaSeq), which the ASCENT authors attribute to index hopping ([[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]).

## Contested points

- **Incomplete insertion is untested.** The Songbird authors suspect incomplete Tn5 insertion (one inactive dimer member, or tagmentation interrupted by neutralisation) behind the same-start fragment pairs, but have not tested this biochemically ([[10-Summaries/wesley-2026-songbird|Songbird]]).
- **Overlap-based ploidy needs tagmentation chemistry.** The ASCENT authors warn the method does not apply to random-priming data ([[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]).
- **Strand pairing.** Standard Tn5 libraries lose strand pairing for duplex sequencing, yet META-CS recovers duplex calls ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]) because strand identity comes from primer extension rather than tagmentation ([[10-Summaries/xing-2021-meta-cs|META-CS]]) (synthesis).
- **Open-chromatin bias across assays.** Droplet Hi-C reports minimal open-chromatin bias ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]), while CUT&Tag data carry a measurable accessibility signal ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]; [[10-Summaries/hu-2026-patty|PATTY]]); the difference may reflect SDS treatment of Hi-C nuclei, but no cited source tests this (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/atac-seq|ATAC-seq]] — Tn5 insertion into accessible chromatin as a readout of openness.
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — Antibody-tethered pA-Tn5 tagmentation for histone marks and chromatin proteins.
> - `concept` [[30-Concepts/smrt-tag|SMRT-Tag]] — Tn5 with hairpin PacBio adapters for low-input HiFi libraries.
> - `concept` [[30-Concepts/scicut-tag|sciCUT&Tag]] — Combinatorial-indexing CUT&Tag with barcoded pA-Tn5.
> - `concept` [[30-Concepts/micro-atac-seq|µATAC-seq]] — Single-cell ATAC-seq on the ICELL8 nanowell platform.
> - `concept` [[30-Concepts/splicool-seq|SpliCOOL-seq]] — Joint single-cell methylation and chromatin accessibility.
> - `concept` [[30-Concepts/copy-number-variation|Copy-number variation]] — Gains and losses of genomic segments; fragment overlap gives absolute ploidy.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Tagging both strands of each molecule for error-corrected calls.

## All sources on this page

> [!info]- 14 summaries cited here
> - [[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]
> - [[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]
> - [[10-Summaries/hu-2026-patty|Hu 2026]]
> - [[10-Summaries/kolbeinsdottir-2025-ascent|Kolbeinsdottir 2025]]
> - [[10-Summaries/ludwig-2019-sc-chromatin-modifications-review|Ludwig & Bintu 2019]]
> - [[10-Summaries/nichols-2025-scimetv3|Nichols 2025]]
> - [[10-Summaries/pampari-2024-chrombpnet|ChromBPNet 2024]]
> - [[10-Summaries/pancikova-2025-splongget|Pančíková 2025 (bioRxiv preprint)]]
> - [[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/wang-2019-cobatch|Wang 2019]]
> - [[10-Summaries/wang-2024-wellda-seq|Wang 2024]]
> - [[10-Summaries/wesley-2026-songbird|Wesley 2026]]
> - [[10-Summaries/xing-2021-meta-cs|Xing 2021]]
