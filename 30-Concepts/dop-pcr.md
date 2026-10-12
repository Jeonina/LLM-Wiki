---
type: concept
title: DOP-PCR (Degenerate Oligonucleotide-Primed PCR)
aliases: [Degenerate Oligonucleotide Primed PCR]
tags: [scWGA, PCR-based, method, historical]
created: 2026-05-11
updated: 2026-10-12
---

# DOP-PCR (Degenerate Oligonucleotide-Primed PCR)

> The earliest [[scwga]] method to reach broad use, using degenerate oligonucleotide primers + thermostable Taq polymerase to amplify single-cell genomes by PCR: low coverage (~20–25%) but high uniformity and low cost ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). Largely supplanted by isothermal and hybrid methods but still in use for low-resolution CNV applications.

> [!abstract] 한눈에
> DOP-PCR은 degenerate primer와 Taq polymerase로 단일 세포 유전체를 PCR 증폭하는 가장 오래된 scWGA 방법으로, coverage는 20–25%로 낮지만 균일하고 저렴하다 ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). 원 논문은 single cell이 아니라 flow-sorted chromosome용으로 개발되었고 증폭이 사실상 linear하다고 주장해, 이후의 single-cell 설명과 어긋난다 ([[10-Summaries/telenius-1992-dop-pcr|Telenius 1992]]).

## Definition

**Single-cell protocol as usually described.** A degenerate oligonucleotide primer (random 6–8 nt at one end + common 22 nt anchor) primes throughout the genome at low temperature; the first PCR cycle is permissive for mismatches. Subsequent cycles preferentially amplify products containing the common sequence, generating a tractable library size from picograms of input ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]).

**Founding design.** The 6-MW primer is 22 nt in total (5′ XhoI tag, six degenerate N, six fixed 3′ bases ATGTGG), used with five 30 °C annealing cycles; it was introduced for chromosome painting and cloning from 500 flow-sorted chromosomes or ~10 ng DNA, not single cells ([[10-Summaries/telenius-1992-dop-pcr|Telenius 1992]]).

**Typical metrics:** coverage ~20–25%, MAPD low (~0.2–0.4), allelic balance low, ~3 h reaction time, $20/cell; commercial. Coverage, uniformity and cost are as reported in [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]].

## Why it matters

DOP-PCR established that single-cell genomes could be PCR-amplified at all. Its low coverage limits SNV detection but is sufficient for chromosomal-scale CNV detection (>10–50 Mb), which made it the standard method for early aneuploidy and pre-implantation studies.

**Limitations:**

- **Thermostable Taq has higher error rate** (10⁻⁴–10⁻⁶) than Φ29 (10⁻⁷–10⁻⁸) used in [[mda|MDA]]/[[pta|PTA]] — more amplification-introduced errors.
- **Loss of signal across most of the genome** during amplification due to PCR efficiency variation between loci.

## Variants and refinements

- **Tetraploid-nucleus DOP-PCR** — sorting G2/M nuclei (2× DNA input) improves coverage to ~10% (Navin et al. 2011).
- **Modern diploid DOP-PCR variants** — minor protocol improvements but coverage still well below isothermal methods such as [[mda|MDA]], [[malbac|MALBAC]] and [[pta|PTA]].

## Evidence and examples

- Detection of 49% aneuploidy in single cells from human early cleavage-stage embryos via DOP-PCR ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- Original Navin et al. breast cancer single-cell phylogenetics (2011, Nature).
- The founding authors argued amplification is effectively linear per fragment (~35–40× each), because primers and Taq become limiting within the first cycles ([[10-Summaries/telenius-1992-dop-pcr|Telenius 1992]]).

## Contested points

- **Founding design versus later description.** The founding paper's primer and input (22-nt 6-MW primer; 500 chromosomes or ~10 ng DNA) ([[10-Summaries/telenius-1992-dop-pcr|Telenius 1992]]) conflict with this page's single-cell description (random 6–8 nt + 22 nt anchor, picogram input) ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]); later single-cell use differs from the original design (synthesis).
- **Linear or exponential?** The founding paper's linear-amplification argument ([[10-Summaries/telenius-1992-dop-pcr|Telenius 1992]]) conflicts with the wiki's "exponential bias" framing of DOP-PCR (synthesis).
- **Remaining niche.** Whether DOP-PCR retains any niche given current method options — for large-scale CNV-only studies at very low cost it remains attractive.

## Related

> [!cards]
> - `concept` [[30-Concepts/scwga|scWGA]] — Methods that amplify the ~6 pg of DNA in a single cell for sequencing.
> - `concept` [[30-Concepts/mda|MDA]] — Isothermal Φ29 strand-displacement amplification.
> - `concept` [[30-Concepts/malbac|MALBAC]] — Hybrid quasilinear pre-amplification with looping amplicons.
> - `concept` [[30-Concepts/pta|PTA]] — Φ29 amplification with chain terminators that favour the native template.
> - `hub` [[40-Topics/scdna-seq|Single-cell DNA sequencing]] — Technologies that interrogate the DNA of single cells.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/telenius-1992-dop-pcr|Telenius 1992]]
