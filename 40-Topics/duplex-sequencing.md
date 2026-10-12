---
type: topic
title: Duplex sequencing
explainer: duplex-sequencing
aliases: [DS, duplex-seq, duplex consensus sequencing, single-molecule duplex sequencing, ultra-accurate sequencing]
tags: [sequencing, error-correction, somatic-mutation, mutational-signatures, single-molecule, low-VAF, method]
created: 2026-05-12
updated: 2026-10-12
paper_section: ["3.1"]
---

# Duplex sequencing

> Duplex sequencing (DS) is a single-molecule NGS strategy that tags both the Watson and Crick strands of each input dsDNA molecule with complementary UMIs, sequences each strand independently, and calls a base only when both strands agree at that position ([[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]; [[10-Summaries/kennedy-2014-duplex-protocol|Kennedy 2014]]). This lowers the calculated error floor to ~3.8 × 10⁻¹⁰ per base, about 10⁷-fold below standard Illumina analysis; experimentally the original method recovered mutants down to 1 in 10,000 molecules ([[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]). It underpins modern mosaicism, mutational-signature and aging-genome biology ([[10-Summaries/abascal-2021-nanoseq|NanoSeq]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

> [!abstract] 한눈에
> Duplex sequencing은 한 분자의 두 가닥 모두에서 같은 변이가 보일 때만 염기를 호출해 오류율을 크게 낮추고, 덕분에 정상 조직의 희귀 체세포 변이와 mutational signature를 bulk DNA에서 읽을 수 있다 ([[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]; [[10-Summaries/abascal-2021-nanoseq|NanoSeq]]). 다만 대부분의 방법은 변이를 특정 세포에 배정하지 못하며, 단일 세포 수준의 duplex는 META-CS와 Duplex-Multiome 정도에 머물러 있다 ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; [[10-Summaries/kriz-2025-duplex-multiome|Duplex-Multiome]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [Duplex sequencing 시뮬레이터](../60-Explainers/duplex-sequencing.html)
<!-- /explainer-links -->

## Key points

- **Both-strand agreement sets the fidelity floor.** The calculated floor is ~3.8 × 10⁻¹⁰ per base ([[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]), though a later empirical estimate for the original chemistry is ~2 × 10⁻⁷ ([[10-Summaries/nandi-2025-udseq|UDSeq]]).
- **Four implementation strategies exist:** Y-adaptor, Tn5-based, quadruplex adaptor and circularized sequencing ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Platform matters less than sample.** Six duplex protocols differ substantially in genomic footprint, sensitivity and cost, yet their mutation-rate estimates and signatures are highly concordant ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).
- **Duplex methods cannot see single-strand precursors.** Because they amplify before reading, they either convert single-strand lesions into double-strand mutations or manufacture artifactual ones ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]).
- **Most duplex methods read bulk DNA.** They capture the full mutational landscape but cannot assign variants to cells; META-CS is the single-cell exception ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]), and Duplex-Multiome calls sSNVs per nucleus within accessible chromatin ([[10-Summaries/kriz-2025-duplex-multiome|Duplex-Multiome]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/umi-molecular-barcoding|UMI molecular barcoding]] — Random tags that group reads by molecule of origin for consensus error correction.
> - `concept` [[30-Concepts/nanoseq|NanoSeq]] — Sanger bottleneck duplex protocol for somatic mutation rates in normal tissues.
> - `concept` [[30-Concepts/codec|CODEC]] — Concatenates both strands of a molecule into one short read.
> - `concept` [[30-Concepts/hidef-seq|HiDEF-seq]] — Evrony-lab duplex method that resolves single-strand mutations with high accuracy.
> - `concept` [[30-Concepts/meta-cs|META-CS]] — The only duplex method that can be applied to single cells.
> - `concept` [[30-Concepts/mutational-signatures|Mutational signatures]] — Trinucleotide-context substitution patterns that reflect mutagenic processes.

## How it works

Standard sequencing reads one strand of a DNA fragment, so sequencing/polymerase errors and ssDNA damage are indistinguishable from true variants ([[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]). Duplex sequencing tags both strands of each original molecule so that strand identity is preserved through library prep and sequencing; only variants observed in **both** strands of the same molecule are called true ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; [[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]). The principle relies on [[30-Concepts/umi-molecular-barcoding]] — random-yet-complementary tag adapters that link the two strands of one molecule ([[10-Summaries/kennedy-2014-duplex-protocol|Kennedy 2014]]).

- **Why it works.** Polymerase and sequencing errors land on only one strand, while a true mutation is present on both ([[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]).
- **What it filters.** Single-strand errors ([[10-Summaries/kennedy-2014-duplex-protocol|Kennedy 2014]]) and single-strand DNA damage, of which a typical cell sustains ~70,000 lesions per day ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Theoretical floor.** The product of the two single-strand error rates times 1/3 for a complementary match, (3.4 × 10⁻⁵)² × 1/3 ≈ 3.8 × 10⁻¹⁰ ([[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]); a later empirical estimate for the original chemistry is much higher, ~2 × 10⁻⁷ ([[10-Summaries/nandi-2025-udseq|UDSeq]]).

## Why fidelity matters

Duplex sequencing redefines the **fidelity** floor of variant detection ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]); in the [[scdna-capabilities-framework]], duplex anchors the fidelity capability (synthesis). Without it, the false-positive rate at low VAFs is dominated by ssDNA damage; with it, true variants below 1% VAF become detectable ([[10-Summaries/kennedy-2014-duplex-protocol|Kennedy 2014]]; [[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]). This is what makes population-scale [[30-Concepts/mutational-signatures]] — trinucleotide-context substitution patterns revealing mutagenic exposures — readable from bulk DNA ([[10-Summaries/abascal-2021-nanoseq|NanoSeq]]).

## Implementation strategies

Four implementation strategies have emerged: Y-adaptor, Tn5-based, quadruplex adaptor and circularized sequencing ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]] Fig 3a). Newer chemistries push input down ([[10-Summaries/nandi-2025-udseq|UDSeq]]).

| Method | Year | Strategy | Input or platform | Note |
|---|---|---|---|---|
| [[10-Summaries/schmitt-2012-pnas\|Duplex Sequencing]] | 2012 | Complementary UMI tag adapters | — | Original method (Loeb lab); calculated floor ~3.8 × 10⁻¹⁰ ([[10-Summaries/schmitt-2012-pnas\|Schmitt 2012]]); reference bench protocol ([[10-Summaries/kennedy-2014-duplex-protocol\|Kennedy 2014]]) |
| [[10-Summaries/hoang-2016-botseqs\|BotSeqS]] | 2016 | Y-adaptor; bottleneck dilution | — | Genome-wide rare nuclear and mtDNA mutation rates in normal tissues ([[10-Summaries/hoang-2016-botseqs\|BotSeqS]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| [[10-Summaries/abascal-2021-nanoseq\|NanoSeq]] | 2021 | Y-adaptor; bottleneck dilution | Nuclear genome | Adapts DS to the nuclear genome; detects somatic SNVs across normal tissues at error rates two orders of magnitude below somatic mutation loads ([[10-Summaries/abascal-2021-nanoseq\|NanoSeq]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| [[10-Summaries/xing-2021-meta-cs\|META-CS]] | 2021 | Tn5; strands labelled by melting and two sequential primer-extension rounds | Single cells | Only single-cell-compatible variant; one-tube complementary-strand scWGA with both-strand consensus from ≥4 reads ([[10-Summaries/xing-2021-meta-cs\|META-CS]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| [[10-Summaries/maslov-2022-smm-seq\|SMM-seq]] | 2022 | Circularized; hairpin adapters (6-nt UMI in the stem) make dumbbell templates, then linear pulse-RCA | Illumina NovaSeq 150PE | Many independent copies of both strands before PCR, so the theoretical error rate is P(E)^N rather than duplex's P(E)²; minimum 7 reads per strand family, set where apparent mutation frequency plateaued; both strands still required to reject single-strand damage ([[10-Summaries/maslov-2022-smm-seq\|SMM-seq]]) |
| [[10-Summaries/bae-2023-codec\|CODEC]] | 2023 | Quadruplex adaptor | Short-read | Adapter physically concatenates both strands so they appear in the same read ([[10-Summaries/bae-2023-codec\|CODEC]]) |
| [[10-Summaries/liu-2024-hidef-seq\|HiDEF-seq]] | 2024 | Circularized | PacBio HiFi | Error rate ~7 × 10⁻¹⁶ from concatenated Watson-Crick reads ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| [[10-Summaries/nandi-2025-udseq\|UDSeq]] | 2025 | Random fragmentation | 100 pg; ≥95% genome coverage | Error rate ~2.5 × 10⁻⁹/bp, estimated from sperm against trio de novo rates ([[10-Summaries/nandi-2025-udseq\|UDSeq]]) |
| [[10-Summaries/kriz-2025-duplex-multiome\|Duplex-Multiome]] | 2025 | Strand tagging added to the 10x Multiome ATAC library | Single nuclei | 51,400 nuclei from postmortem human brain with point mutations + chromatin + RNA per cell ([[10-Summaries/kriz-2025-duplex-multiome\|Duplex-Multiome]]) |

The concept pages are [[nanoseq]], [[codec]], [[hidef-seq]] and [[meta-cs]]. [[10-Summaries/swanson-2025-daf-seq|DAF-seq]] achieves an analogous fidelity gain by a different route — using deamination patterns as per-molecule UMIs for consensus-read assembly ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

## Benchmarking across methods

- **Six methods, concordant answers.** The SMaHT benchmark compared CODEC, CompDuplex-seq, HiDEF-seq, NanoSeq, ppmSeq and VISTA-seq ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]); the protocols differ substantially in genomic footprint, sensitivity and cost, although their mutation-rate estimates and signatures are highly concordant ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).
- **Duplex finds what bulk WGS misses.** Shallow duplex sequencing finds mutations largely absent from ~1000X bulk WGS: <0.5% of tissue duplex calls overlapped bulk truth sets, and duplex calls captured COLO829-BLT50 clones down to ~0.002% VAF ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).
- **The reference mixture is not fixed.** Both this benchmark and Duplex-Multiome found clonal changes in COLO829-BLT50 that arose in culture, so the mixture is not a fixed truth set ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]; [[10-Summaries/kriz-2025-duplex-multiome|Duplex-Multiome]]).

## Limits: single-strand events

HiDEF-seq marks the boundary of what duplex sequencing can do ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]). Duplex methods achieve high fidelity for **double-strand** mutations, but because they amplify before reading they either convert single-strand lesions into double-strand mutations or manufacture artifactual ones — so the **precursor** events are invisible to them ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]). Across nine samples run on both platforms, HiDEF-seq and [[10-Summaries/abascal-2021-nanoseq|NanoSeq]] agree on dsDNA burdens and patterns, but NanoSeq's ssDNA call burdens are ~18-fold higher with distinct patterns — largely artifact ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]).

## Duplex and single-cell DNA

- **Bulk versus per cell.** Most duplex methods sequence **bulk DNA** at single-molecule resolution — capturing the full mutational landscape but unable to assign variants to specific cells ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). [[meta-cs]] is the exception and the bridge to per-cell duplex resolution ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Duplex-Multiome.** Adds strand tagging to the 10x Multiome ATAC library so sSNVs are called by duplex consensus from the same nuclei that give snATAC and snRNA profiles; calls are restricted to accessible chromatin and sparse per nucleus, so burdens are estimated per cell type ([[10-Summaries/kriz-2025-duplex-multiome|Duplex-Multiome]]).
- **Duplex as validator of single-cell calls.** Luquette 2025 uses DS to validate PTA-scDNA-seq mutation calls, with a companion SMaHT PTA pipeline ([[10-Summaries/luquette-2025-pta-duplex-mosaicism|Luquette 2025]]). A decade earlier, nuc-seq used targeted duplex sequencing at ~5,700–6,600× single-molecule depth to test single-cell mutation calls, and only 19.4–27.0% of single-cell-only calls validated ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]); the arbiter role therefore predates the current frontier (synthesis).
- **Complementary, not competing.** Duplex captures population mutation rates and signatures from bulk DNA; scDNA-seq captures clonality and lineage, so the methods layer rather than compete (synthesis based on [[10-Summaries/luquette-2025-pta-duplex-mosaicism|Luquette 2025]] + [[10-Summaries/abascal-2021-nanoseq|NanoSeq]]). This is a future synthesis target for a note on duplex vs scDNA-seq complementarity (synthesis).

## Key entities

- [[20-Entities/lawrence-loeb]] — Loeb lab; original DS protocol ([[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]).
- [[20-Entities/ludmil-alexandrov]] — Alexandrov lab; UDSeq + mutational-signature framework ([[10-Summaries/nandi-2025-udseq|UDSeq]]).
- [[20-Entities/tim-coorens]] — Coorens lab; SMaHT benchmark co-lead ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).
- [[20-Entities/smaht-network]] — Somatic Mosaicism across Human Tissues consortium ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).

## Reviews

- [[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]] — mosaicism and accuracy review.
- [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]] — NRG review; classifies the four duplex implementation strategies.
- [[10-Summaries/hilal-2026-cardiac-somatic-review|Hilal 2026]] — cardiac somatic-mosaicism review; cardiovascular-tissue duplex toolbox catalog (TwinStrand, NanoSeq, BotSeqS, CODEC, Pro-Seq, META-CS).
- [[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]] — long-read epigenome review; background for long-read single-molecule methods.

## Open questions

- **Cost trade-off.** About 40 raw reads are needed per duplex consensus, so DS suits targeted regions under 1 Mb or needs deep sequencing budgets ([[10-Summaries/kennedy-2014-duplex-protocol|Kennedy 2014]]); whole-genome methods still differ widely in cost per interrogated base, from ≈$15 to ≈$220 per billion bp ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).
- **Long-read displacement.** Will unamplified single-molecule long-read sequencing displace short-read duplex as accuracy improves (synthesis)? HiDEF-seq already reaches <1 error per 10¹⁴ bp on PacBio ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]).
- **Benchmarking heterogeneity.** Duplex protocols differ substantially in genomic footprint, sensitivity and cost, although their mutation-rate estimates and signatures are highly concordant ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).
- **Single-cell duplex** is not yet broadly practical: DS needs both strands of one molecule, but scWGA loses strand identity ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). [[meta-cs]] is the only single-cell-compatible variant so far; Duplex-Multiome solves it for nuclear sSNV calling within Tn5-accessible regions via the 10x Multiome library ([[10-Summaries/kriz-2025-duplex-multiome|Duplex-Multiome]]).
- The SMaHT benchmark already included two brain homogenates (22 y and 73 y) with concordant burdens, but cord-blood estimates still split ~2.6-fold between method groups and ppmSeq diverged; does site-level concordance on private mutations hold ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]])?
- **Error-rate figures.** The original Duplex Sequencing floor is calculated (<10⁻⁹) ([[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]), while UDSeq's Table 1 lists an empirical ~2 × 10⁻⁷ for the original method and also ~2 × 10⁻⁷ for BotSeqS ([[10-Summaries/nandi-2025-udseq|UDSeq]]); the wiki elsewhere quotes BotSeqS at 2.6 × 10⁻¹² ([[10-Summaries/hoang-2016-botseqs|BotSeqS]]). Theoretical and empirical figures should not be compared directly (synthesis).

## Related

> [!cards]
> - `hub` [[40-Topics/scdna-seq|Single-cell DNA sequencing]] — Technologies that interrogate the DNA of single cells, by scWGA or by strand-paired single-molecule reads.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one body.
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — PacBio HiFi and ONT reads of kilobases to hundreds of kilobases, with direct base-modification detection.

## All sources on this page

> [!info]- 18 summaries cited here
> - [[10-Summaries/abascal-2021-nanoseq|Abascal 2021]]
> - [[10-Summaries/bae-2023-codec|Bae 2023]]
> - [[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]
> - [[10-Summaries/hilal-2026-cardiac-somatic-review|Hilal 2026]]
> - [[10-Summaries/hoang-2016-botseqs|Hoang 2016]]
> - [[10-Summaries/kennedy-2014-duplex-protocol|Kennedy 2014]]
> - [[10-Summaries/kriz-2025-duplex-multiome|Kriz 2025]]
> - [[10-Summaries/liu-2024-hidef-seq|Liu 2024]]
> - [[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]]
> - [[10-Summaries/luquette-2025-pta-duplex-mosaicism|Luquette 2025]]
> - [[10-Summaries/maslov-2022-smm-seq|Maslov 2022]]
> - [[10-Summaries/nandi-2025-udseq|Nandi 2025]]
> - [[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
> - [[10-Summaries/wang-2014-nuc-seq|Wang 2014]]
> - [[10-Summaries/xing-2021-meta-cs|Xing 2021]]
> - [[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]
