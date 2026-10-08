---
type: topic
title: Duplex sequencing
aliases: [DS, duplex-seq, duplex consensus sequencing, single-molecule duplex sequencing, ultra-accurate sequencing]
tags: [sequencing, error-correction, somatic-mutation, mutational-signatures, single-molecule, low-VAF, method]
created: 2026-05-12
updated: 2026-10-07
paper_section: ["3.1"]
---

# Duplex sequencing

> Duplex sequencing (DS) is a single-molecule NGS strategy that tags both the Watson and Crick strands of each input dsDNA molecule with complementary UMIs, sequences each strand independently, and calls a base only when both strands agree at that position ([[10-Summaries/schmitt-2012-pnas]]; [[10-Summaries/kennedy-2014-duplex-protocol]]). This lowers the calculated error floor to ~3.8 × 10⁻¹⁰ per base, about 10⁷-fold below standard Illumina analysis; experimentally the original method recovered mutants down to 1 in 10,000 molecules ([[10-Summaries/schmitt-2012-pnas]]) — and underpins modern mosaicism, mutational-signature, and aging-genome biology ([[10-Summaries/abascal-2021-nanoseq]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## How it works

Standard sequencing reads one strand of a DNA fragment, so sequencing/polymerase errors and ssDNA damage are indistinguishable from true variants ([[10-Summaries/schmitt-2012-pnas]]). Duplex sequencing tags both strands of each original molecule so that strand identity is preserved through library prep and sequencing; only variants observed in **both** strands of the same molecule are called true ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]; [[10-Summaries/schmitt-2012-pnas]]).

This exploits the fact that polymerase and sequencing errors land on only one strand, while a true mutation is present on both ([[10-Summaries/schmitt-2012-pnas]]). Single-strand errors are filtered ([[10-Summaries/kennedy-2014-duplex-protocol]]), as is single-strand DNA damage — of which a typical cell sustains ~70,000 lesions per day ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). The theoretical error floor is the product of the two single-strand error rates times 1/3 for a complementary match, (3.4 × 10⁻⁵)² × 1/3 ≈ 3.8 × 10⁻¹⁰ ([[10-Summaries/schmitt-2012-pnas]]); a later empirical estimate for the original chemistry is much higher, ~2 × 10⁻⁷ ([[10-Summaries/nandi-2025-udseq]]).

The principle relies on [[30-Concepts/umi-molecular-barcoding]] — random-yet-complementary tag adapters that link the two strands of one molecule ([[10-Summaries/kennedy-2014-duplex-protocol]]).

## Why it matters

Duplex sequencing redefines the **fidelity** floor of variant detection ([[10-Summaries/evrony-2021-scDNA-applications-review]]). Without it, the false-positive rate at low VAFs is dominated by ssDNA damage; with it, true variants below 1% VAF become detectable ([[10-Summaries/kennedy-2014-duplex-protocol]]; [[10-Summaries/schmitt-2012-pnas]]). This is what makes population-scale [[30-Concepts/mutational-signatures]] — trinucleotide-context substitution patterns revealing mutagenic exposures — readable from bulk DNA ([[10-Summaries/abascal-2021-nanoseq]]).

Most duplex methods sequence **bulk DNA** at single-molecule resolution — capturing the full mutational landscape but unable to assign variants to specific cells ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). [[meta-cs]] is the exception and the bridge to per-cell duplex resolution ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). **Duplex-Multiome** adds strand tagging to the 10x Multiome ATAC library so sSNVs are called by duplex consensus from the same nuclei that give snATAC and snRNA profiles; calls are restricted to accessible chromatin and sparse per nucleus, so burdens are estimated per cell type ([[10-Summaries/kriz-2025-duplex-multiome]]).

## Implementation strategies

Four implementation strategies have emerged ([[10-Summaries/shao-2025-scDNA-mosaicism-review]] Fig 3a):

- **Y-adaptor based** — BotSeqS, NanoSeq: asymmetric Y-shaped adapter with distinct strand barcodes; requires bottleneck dilution ([[10-Summaries/abascal-2021-nanoseq]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- **Tn5-based** — [[meta-cs]], the only single-cell-compatible variant; strands are labelled by melting and two sequential primer-extension rounds after Tn5 tagging ([[10-Summaries/xing-2021-meta-cs]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- **Quadruplex adaptor** — [[codec]]: adapter physically concatenates both strands so they appear in the same read ([[10-Summaries/bae-2023-codec]]).
- **Circularized sequencing** — [[hidef-seq]] (PacBio HiFi, error rate ~7×10⁻¹⁶) and SMM-seq (Illumina rolling-circle) ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

Newer chemistries also push input down: UDSeq works from 100 pg with ≥95% genome coverage and an error rate of ~2.5×10⁻⁹/bp, estimated from sperm against trio de novo rates ([[10-Summaries/nandi-2025-udseq]]). [[nanoseq]] adapts DS to the nuclear genome ([[10-Summaries/abascal-2021-nanoseq]]). [[10-Summaries/swanson-2025-daf-seq]] (DAF-seq) achieves an analogous fidelity gain by a different route — using deamination patterns as per-molecule UMIs for consensus-read assembly ([[10-Summaries/swanson-2025-daf-seq]]).

## Examples

- NanoSeq detects somatic SNVs across normal human tissues at error rates two orders of magnitude below somatic mutation loads ([[10-Summaries/abascal-2021-nanoseq]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- HiDEF-seq on PacBio reaches ~7×10⁻¹⁶ error rate from concatenated Watson-Crick reads ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- CODEC: ligated-quadruplex single-read duplex resolution ([[10-Summaries/bae-2023-codec]]).
- [[meta-cs]] applied to single cells — bridging duplex and scDNA-seq ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- Duplex-Multiome: 51,400 nuclei from postmortem human brain with point mutations + chromatin + RNA per cell ([[10-Summaries/kriz-2025-duplex-multiome]]).
- Cardiovascular-tissue duplex toolbox catalog (TwinStrand, NanoSeq, BotSeqS, CODEC, Pro-Seq, META-CS) ([[10-Summaries/hilal-2026-cardiac-somatic-review]]).

## Key entities

- [[20-Entities/lawrence-loeb]] — Loeb lab; original DS protocol ([[10-Summaries/schmitt-2012-pnas]]).
- [[20-Entities/ludmil-alexandrov]] — Alexandrov lab; UDSeq + mutational-signature framework ([[10-Summaries/nandi-2025-udseq]]).
- [[20-Entities/tim-coorens]] — Coorens lab; SMaHT benchmark co-lead ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]).
- [[20-Entities/smaht-network]] — Somatic Mosaicism across Human Tissues consortium ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]).

## Sources, by sub-theme

### Foundational protocol
- [[10-Summaries/schmitt-2012-pnas]] — Schmitt/Loeb 2012 PNAS. Original duplex sequencing method.
- [[10-Summaries/kennedy-2014-duplex-protocol]] — Kennedy et al. 2014, Nature Protocols. The reference DS bench protocol (Loeb lab).

### Newer chemistries with lower input
- [[10-Summaries/nandi-2025-udseq]] — Nandi/Alexandrov 2025. UDSeq: ~2.5×10⁻⁹/bp from 100 pg.
- [[10-Summaries/bae-2023-codec]] — CODEC quadruplex-adaptor strategy.
- [[10-Summaries/abascal-2021-nanoseq]] — NanoSeq nuclear-genome DS protocol.

### Cross-method benchmarking
- [[10-Summaries/zhang-2025-smaht-duplex-benchmark]] — Zhang/Coorens 2025. SMaHT benchmark of six methods (CODEC, CompDuplex-seq, HiDEF-seq, NanoSeq, ppmSeq, VISTA-seq).

### Single-cell + duplex validation
- [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] — Luquette/Walsh 2025. Uses DS to validate PTA-scDNA-seq mutation calls; companion SMaHT PTA pipeline.
- [[10-Summaries/kriz-2025-duplex-multiome]] — Kriz 2025. Duplex-Multiome: duplex consensus integrated into 10x Multiome (point mutations + chromatin + RNA per nucleus).

### Reviews
- [[10-Summaries/evrony-2021-scDNA-applications-review]] — Evrony 2021 mosaicism + accuracy review.
- [[10-Summaries/shao-2025-scDNA-mosaicism-review]] — Shao 2025 NRG; classifies the four duplex implementation strategies.
- [[10-Summaries/hilal-2026-cardiac-somatic-review]] — Hilal 2026 cardiac somatic-mosaicism review; duplex toolbox catalog.
- [[10-Summaries/liu-2025-long-read-epigenome-review]] — Liu 2025 long-read review; raises long-read-vs-duplex displacement question.

## Synthesized notes

_Future synthesis target_: "Duplex vs scDNA-seq complementarity" — duplex captures population mutation rates and signatures from bulk DNA; scDNA-seq captures clonality and lineage. The methods don't compete; they layer (synthesis based on [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] + [[10-Summaries/abascal-2021-nanoseq]]). See [[scdna-capabilities-framework]] — duplex anchors the fidelity capability.

## Contested points

- **Cost trade-off**: duplex sequencing requires roughly twice the read depth per molecule plus complex library prep — cost per variant detected is high ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- **Long-read displacement**: whether single-molecule long-read direct sequencing (PacBio HiFi without amplification, ONT) will displace duplex sequencing as long-read accuracy improves ([[10-Summaries/liu-2025-long-read-epigenome-review]]).
- **Benchmarking heterogeneity**: duplex protocols differ substantially in genomic footprint, sensitivity and cost, although their mutation-rate estimates and signatures are highly concordant ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]).

## Open questions

- **Single-cell duplex** is not yet broadly practical: DS needs both strands of one molecule, but scWGA loses strand identity ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). [[meta-cs]] is the only single-cell-compatible variant so far; Duplex-Multiome solves it for nuclear sSNV calling within Tn5-accessible regions via the 10x Multiome library ([[10-Summaries/kriz-2025-duplex-multiome]]).
- The SMaHT benchmark already included two brain homogenates (22 y and 73 y) with concordant burdens, but cord-blood estimates still split ~2.6-fold between method groups and ppmSeq diverged; does site-level concordance on private mutations hold ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]])?

## Added 2026-10-07

- [[10-Summaries/hoang-2016-botseqs]] — BotSeqS bottleneck duplex sequencing: genome-wide rare nuclear and mtDNA mutation rates in normal tissues.
- [[10-Summaries/xing-2021-meta-cs]] — META-CS primary paper: one-tube complementary-strand scWGA; both-strand consensus calling in single cells from ≥4 reads.

**SMM-seq primary source.** SMM-seq ligates hairpin adapters (6-nt UMI in the stem) to make dumbbell templates. Linear pulse-RCA then produces many independent copies of both strands before PCR, so the theoretical error rate is P(E)^N rather than duplex's P(E)² ([[10-Summaries/maslov-2022-smm-seq]]). A minimum of 7 reads per strand family was set empirically, at the point where apparent mutation frequency plateaued, and both strands are still required to reject single-strand DNA damage ([[10-Summaries/maslov-2022-smm-seq]]). Libraries are sequenced on Illumina NovaSeq 150PE ([[10-Summaries/maslov-2022-smm-seq]]).


**Open question — error-rate figures.** The original Duplex Sequencing floor is calculated (<10⁻⁹) ([[10-Summaries/schmitt-2012-pnas]]), while UDSeq's Table 1 lists an empirical ~2 × 10⁻⁷ for the original method and also ~2 × 10⁻⁷ for BotSeqS ([[10-Summaries/nandi-2025-udseq]]); the wiki elsewhere quotes BotSeqS at 2.6 × 10⁻¹² ([[10-Summaries/hoang-2016-botseqs]]). Theoretical and empirical figures should not be compared directly (synthesis).

Shallow duplex sequencing finds mutations largely absent from ~1000X bulk WGS: <0.5% of tissue duplex calls overlapped bulk truth sets, and duplex calls captured COLO829-BLT50 clones down to ~0.002% VAF ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]). Both this benchmark and Duplex-Multiome found clonal changes in COLO829-BLT50 that arose in culture, so the mixture is not a fixed truth set ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]; [[10-Summaries/kriz-2025-duplex-multiome]]).

## Related

- [[30-Concepts/umi-molecular-barcoding]] · [[30-Concepts/mutational-signatures]] · [[30-Concepts/codec]] · [[30-Concepts/nanoseq]] · [[30-Concepts/hidef-seq]] · [[40-Topics/scdna-seq]]
- [[meta-cs]] — single-cell-compatible duplex method.
- [[scdna-capabilities-framework]] — fidelity capability.
- [[40-Topics/somatic-mosaicism]] · [[40-Topics/scdna-seq]] · [[40-Topics/long-read-sequencing]]

## Added 2026-08-13

HiDEF-seq ([[10-Summaries/liu-2024-hidef-seq]]) marks the boundary of what duplex sequencing can do. Duplex methods achieve high fidelity for **double-strand** mutations, but because they amplify before reading they either convert single-strand lesions into double-strand mutations or manufacture artifactual ones — so the **precursor** events are invisible to them ([[10-Summaries/liu-2024-hidef-seq]]).

Concretely: across nine samples run on both platforms, HiDEF-seq and [[10-Summaries/abascal-2021-nanoseq|NanoSeq]] agree on dsDNA burdens and patterns, but NanoSeq's ssDNA call burdens are ~18-fold higher with distinct patterns — largely artifact ([[10-Summaries/liu-2024-hidef-seq]]).

The pairing of duplex sequencing with single-cell calls as an **arbiter** predates the current frontier by a decade: [[10-Summaries/wang-2014-nuc-seq]] used targeted duplex sequencing at ~5,700–6,600× single-molecule depth to test single-cell mutation calls, finding only 19.4–27.0% of single-cell-only calls validated. (synthesis)
