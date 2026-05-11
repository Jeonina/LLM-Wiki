---
type: concept
title: DOP-PCR (Degenerate Oligonucleotide-Primed PCR)
aliases: [Degenerate Oligonucleotide Primed PCR]
tags: [scWGA, PCR-based, method, historical]
created: 2026-05-11
updated: 2026-05-11
---

# DOP-PCR (Degenerate Oligonucleotide-Primed PCR)

> The earliest [[scwga]] method to reach broad use, using degenerate oligonucleotide primers + thermostable Taq polymerase to amplify single-cell genomes by PCR. Low coverage (~25%) but high uniformity, low cost, simple protocol. Largely supplanted by isothermal and hybrid methods but still in use for low-resolution CNV applications.

## Definition

A degenerate oligonucleotide primer (random 6–8 nt at one end + common 22 nt anchor) primes throughout the genome at low temperature; the first PCR cycle is permissive for mismatches. Subsequent cycles preferentially amplify products containing the common sequence, generating a tractable library size from picograms of input ([[10-Summaries/charles-2016-naturereviewsgenetics]]).

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

- Detection of 49% aneuploidy in single cells from human early cleavage-stage embryos via DOP-PCR ([[10-Summaries/diane-2025-naturereviewsgenetics]]).
- Original Navin et al. breast cancer single-cell phylogenetics (2011, Nature).

## Related

- [[scwga]]
- [[mda]], [[malbac]], [[pta]] — modern alternatives.
- [[scdna-seq]]
