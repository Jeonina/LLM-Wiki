---
type: concept
title: MALBAC (Multiple Annealing and Loop-based Amplification Cycles)
aliases: [Multiple Annealing and Loop-based Amplification Cycles]
tags: [scWGA, hybrid, PCR-based, method]
created: 2026-05-11
updated: 2026-05-11
---

# MALBAC (Multiple Annealing and Loop-based Amplification Cycles)

> Hybrid [[scwga]] method that performs limited isothermal pre-amplification with random + common-sequence primers, generating amplicons that loop on themselves and prevent further pre-amplification. The loops then serve as templates for PCR. Trades coverage for uniformity vs [[mda]] — historically the go-to method for single-cell CNV detection.

## Definition

MALBAC primers carry a common sequence at one end and random nucleotides at the other ([[10-Summaries/gawad-2016-scgenome-review]]). After isothermal random priming and extension, the common-sequence ends of the resulting amplicons are complementary, so they fold into hairpin loops. Looped amplicons cannot be re-primed as templates, which limits the bias from repeated amplification of early-amplified loci. The loops then serve as templates for standard PCR amplification.

Typical metrics: coverage 55–60%, uniformity better than MDA, allelic balance moderate, ~4 h reaction time, $50/cell.

## Why it matters

For CNV detection at the single-cell level, MALBAC's uniformity outweighs its lower coverage — read-depth-based CNV callers need uniform sampling, not deep per-base coverage. Many early single-cell cancer studies used MALBAC for clonal-evolution mapping ([[10-Summaries/gawad-2016-scgenome-review]]).

Now largely superseded by [[pta]] for high-coverage applications, but remains in use for cost-sensitive CNV-only workflows.

## Variants and refinements

- **Microfluidic MALBAC** — improved uniformity over tube-volume reactions ([[10-Summaries/gawad-2016-scgenome-review]]).
- Used historically for single-cell cancer phylogenetics in breast cancer and CLL studies.

## Contested points

- Quake group's MDA-vs-MALBAC benchmarking ([[10-Summaries/gawad-2016-scgenome-review]]) gave mixed results — MALBAC was more uniform but had higher error rate. Conclusion: method choice should match the specific question.
- MALBAC's ADO rate ~21% was sometimes calculated only on covered sites, masking true false-negative rates.

## Examples

- Single-cell CNV phylogenetics in breast cancer (Navin et al. 2011, Hou et al. 2013 cited in [[10-Summaries/gawad-2016-scgenome-review]]).
- Capture of SNVs in circulating tumor cells with high uniformity.

## Related

- [[scwga]]
- [[mda]] — pure-isothermal alternative.
- [[dop-pcr]], PicoPLEX — adjacent PCR-based methods.
- [[scdna-seq]]
