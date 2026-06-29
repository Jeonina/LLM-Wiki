---
type: topic
title: Duplex sequencing
aliases: [DS, duplex-seq, duplex consensus sequencing, single-molecule duplex sequencing, ultra-accurate sequencing]
tags: [sequencing, error-correction, somatic-mutation, mutational-signatures, single-molecule, low-VAF, method]
created: 2026-05-12
updated: 2026-06-29
---

# Duplex sequencing

> Duplex sequencing (DS) is a single-molecule NGS strategy that tags both the Watson and Crick strands of each input dsDNA molecule with complementary UMIs, sequences each strand independently, and calls a base only when both strands agree at that position ([[10-Summaries/schmitt-2012-pnas]]; [[10-Summaries/kennedy-2014-duplex-protocol]]). This drops the false-positive error rate below 10⁻⁸ per base — orders of magnitude below standard sequencing, and sufficient to detect somatic mutations at any allele fraction ([[10-Summaries/schmitt-2012-pnas]]) — and underpins modern mosaicism, mutational-signature, and aging-genome biology ([[10-Summaries/abascal-2021-nanoseq]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## How it works

Standard sequencing reads one strand of a DNA fragment, so sequencing/polymerase errors and ssDNA damage are indistinguishable from true variants ([[10-Summaries/schmitt-2012-pnas]]). Duplex sequencing tags both strands of each original molecule so that strand identity is preserved through library prep and sequencing; only variants observed in **both** strands of the same molecule are called true ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]; [[10-Summaries/schmitt-2012-pnas]]).

This exploits the fact that polymerase and sequencing errors land on only one strand, while a true mutation is present on both ([[10-Summaries/schmitt-2012-pnas]]). Single-strand errors are filtered ([[10-Summaries/kennedy-2014-duplex-protocol]]), as is single-strand DNA damage — of which a typical cell sustains ~70,000 lesions per day ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). The error floor approaches the probability of the polymerase making the *exact same* error on both strands of the same molecule (≤10⁻⁸) ([[10-Summaries/schmitt-2012-pnas]]).

The principle relies on [[30-Concepts/umi-molecular-barcoding]] — random-yet-complementary tag adapters that link the two strands of one molecule ([[10-Summaries/kennedy-2014-duplex-protocol]]).

## Why it matters

Duplex sequencing redefines the **fidelity** floor of variant detection ([[10-Summaries/evrony-2021-scDNA-applications-review]]). Without it, the false-positive rate at low VAFs is dominated by ssDNA damage; with it, true variants below 1% VAF become detectable ([[10-Summaries/kennedy-2014-duplex-protocol]]; [[10-Summaries/schmitt-2012-pnas]]). This is what makes population-scale [[30-Concepts/mutational-signatures]] — trinucleotide-context substitution patterns revealing mutagenic exposures — readable from bulk DNA ([[10-Summaries/abascal-2021-nanoseq]]).

Most duplex methods sequence **bulk DNA** at single-molecule resolution — capturing the full mutational landscape but unable to assign variants to specific cells ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). [[meta-cs]] is the exception and the bridge to per-cell duplex resolution ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). **Duplex-Multiome** integrates duplex consensus into the 10x Multiome platform, achieving per-nucleus point-mutation + scATAC + scRNA ([[10-Summaries/kriz-2025-duplex-multiome]]).

## Implementation strategies

Four implementation strategies have emerged ([[10-Summaries/shao-2025-scDNA-mosaicism-review]] Fig 3a):

- **Y-adaptor based** — BotSeqS, NanoSeq: asymmetric Y-shaped adapter with distinct strand barcodes; requires bottleneck dilution ([[10-Summaries/abascal-2021-nanoseq]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- **Tn5-based** — [[meta-cs]], the only single-cell-compatible variant; Tn5 inserts adapters with orientation distinguishing the two strands ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- **Quadruplex adaptor** — [[codec]]: adapter physically concatenates both strands so they appear in the same read ([[10-Summaries/bae-2023-codec]]).
- **Circularized sequencing** — [[hidef-seq]] (PacBio HiFi, error rate ~7×10⁻¹⁶) and SMM-seq (Illumina rolling-circle) ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

Newer chemistries also push input down: UDSeq reaches ~2.5×10⁻⁹/bp from 100 pg ([[10-Summaries/nandi-2025-udseq]]). [[nanoseq]] adapts DS to the nuclear genome ([[10-Summaries/abascal-2021-nanoseq]]). [[10-Summaries/swanson-2025-daf-seq]] (DAF-seq) achieves an analogous fidelity gain by a different route — using deamination patterns as per-molecule UMIs for consensus-read assembly ([[10-Summaries/swanson-2025-daf-seq]]).

## Examples

- NanoSeq detects somatic SNVs across normal human tissues at error rate <5×10⁻⁹ ([[10-Summaries/abascal-2021-nanoseq]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
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
- **Benchmarking heterogeneity**: different duplex protocols disagree on mutation spectra at extreme low VAF ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]).

## Open questions

- **Single-cell duplex** is not yet broadly practical: DS needs both strands of one molecule, but scWGA loses strand identity ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). [[meta-cs]] is the only single-cell-compatible variant so far; Duplex-Multiome solves it for mtDNA + nuclear point-mutation calling via the 10x library ([[10-Summaries/kriz-2025-duplex-multiome]]).
- Will the convergence of mutation-rate estimates across methods (shown in the SMaHT benchmark) hold when applied to harder tissues like brain or aging muscle ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]])?

## Related

- [[30-Concepts/umi-molecular-barcoding]] · [[30-Concepts/mutational-signatures]] · [[30-Concepts/codec]] · [[30-Concepts/nanoseq]] · [[30-Concepts/hidef-seq]] · [[40-Topics/scdna-seq]]
- [[meta-cs]] — single-cell-compatible duplex method.
- [[scdna-capabilities-framework]] — fidelity capability.
- [[40-Topics/somatic-mosaicism]] · [[40-Topics/scdna-seq]] · [[40-Topics/long-read-sequencing]]
