---
type: concept
title: DOP-PCR (Degenerate Oligonucleotide-Primed PCR)
aliases: [Degenerate Oligonucleotide Primed PCR]
tags: [scWGA, PCR-based, method, historical]
created: 2026-05-11
updated: 2026-10-07
---

# DOP-PCR (Degenerate Oligonucleotide-Primed PCR)

> The earliest [[scwga]] method to reach broad use, using degenerate oligonucleotide primers + thermostable Taq polymerase to amplify single-cell genomes by PCR. Low coverage (~25%) but high uniformity, low cost, simple protocol. Largely supplanted by isothermal and hybrid methods but still in use for low-resolution CNV applications.

## Definition

A degenerate oligonucleotide primer (random 6–8 nt at one end + common 22 nt anchor) primes throughout the genome at low temperature; the first PCR cycle is permissive for mismatches. Subsequent cycles preferentially amplify products containing the common sequence, generating a tractable library size from picograms of input ([[10-Summaries/gawad-2016-scgenome-review]]).

Typical metrics: coverage ~20–25%, MAPD low (~0.2–0.4), allelic balance low, ~3 h reaction time, $20/cell. Commercial.

## Why it matters

DOP-PCR established that single-cell genomes could be PCR-amplified at all. Its low coverage limits SNV detection but is sufficient for chromosomal-scale CNV detection (>10–50 Mb), which made it the standard method for early aneuploidy and pre-implantation studies.

Limitations:
- **Thermostable Taq has higher error rate** (10⁻⁴–10⁻⁶) than Φ29 (10⁻⁷–10⁻⁸) used in MDA/PTA — more amplification-introduced errors.
- **Loss of signal across most of the genome** during amplification due to PCR efficiency variation between loci.

## Variants and refinements

- **Tetraploid-nucleus DOP-PCR** — sorting G2/M nuclei (2× DNA input) improves coverage to ~10% (Navin et al. 2011).
- **Modern diploid DOP-PCR variants** — minor protocol improvements but coverage still well below isothermal methods.

## Contested points

- Whether DOP-PCR retains any niche given current method options — for large-scale CNV-only studies at very low cost it remains attractive.

## Examples

- Detection of 49% aneuploidy in single cells from human early cleavage-stage embryos via DOP-PCR ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- Original Navin et al. breast cancer single-cell phylogenetics (2011, Nature).

## Added 2026-10-07

**From the founding paper:** the 6-MW primer is 22 nt in total (5′ XhoI tag, six degenerate N, six fixed 3′ bases ATGTGG) used with five 30 °C annealing cycles; it was introduced for chromosome painting and cloning from 500 flow-sorted chromosomes or ~10 ng DNA, not single cells ([[10-Summaries/telenius-1992-dop-pcr]]). The authors argued amplification is effectively linear per fragment (~35–40× each), because primers and Taq become limiting within the first cycles ([[10-Summaries/telenius-1992-dop-pcr]]). This conflicts with this page's earlier description (random 6–8 nt + 22 nt anchor, picogram input) and with the wiki's "exponential bias" framing; later single-cell use differs from the original design (synthesis).

## Related

- [[scwga]]
- [[mda]], [[malbac]], [[pta]] — modern alternatives.
- [[40-Topics/scdna-seq]]
