---
type: summary
title: "Human Genome Structural Variation Working Group 2007 — Completing the map of human genetic variation"
source: "[[00-Sources/papers/Completing the map of human genetic variation]]"
source_kind: paper
author: "The Human Genome Structural Variation Working Group (Evan E. Eichler corresponding; D. A. Nickerson, D. Altshuler, A. Fritz, J. R. Lupski, S. T. Sherry et al.)"
published: 2007-05-09
ingested: 2026-08-10
doi: "10.1038/447161a"
journal: "Nature (Commentary / community resource proposal)"
tags: [structural-variation, copy-number-variation, NHGRI, reference-genome, clone-based-sequencing, historical-anchor, HapMap]
entities: []
concepts: ["[[structural-variants]]", "[[highly-repetitive-regions]]", "[[transposable-elements]]"]
topics: ["[[somatic-mosaicism]]"]
---

**Citation:** Human Genome Structural Variation Working Group (2007) — *Completing the map of human genetic variation* — *Nature* 447, 161–165. [DOI](https://doi.org/10.1038/447161a)

# Eichler 2007 — completing the SV map

> The NHGRI proposal that launched systematic, **sequence-resolved** structural-variation discovery in humans. Its argument: SNP maps were nearly complete while SV understanding was "recent and rudimentary," array CGH could see dosage but not sequence or balanced events, and the reference assembly is only *one* version of the genome. The fix proposed was clone-based: large-insert fosmid/BAC libraries from 62 HapMap individuals, discordant end-sequence-pair mapping, then full insert sequencing.

## Key claims

- Structural variation = "all genomic changes that are not single base-pair substitutions" — insertions, deletions, inversions, duplications, translocations, including CNVs. This is the definitional statement much of the field still uses.
- The scale was already known to be large: the Copy Number Variation Project found >1,447 CNV regions spanning **12% of the reference sequence** across 269 HapMap samples.
- Array methods have two structural blind spots: they cannot identify *which* sequence changed or by what mechanism, and they are blind to **balanced** rearrangements. Genomic-sequence analyses suggested **1–20% of all SV is balanced** and copy-number-neutral.
- SV confers phenotype through at least five mechanisms: gene dosage, gene disruption, fusion genes at junctions, position effects on nearby regulation, and unmasking of recessive alleles/functional SNPs on the remaining allele — plus a proposed sixth via homolog-pairing (transvection).
- Common SVs matter clinically: *UGT2B17* deletion (testosterone metabolism, prostate cancer risk), *CCL3L1* copy gain (HIV/AIDS resistance), low *DEFB4* copy number (colonic Crohn's), reduced *FCGR3* (glomerulonephritis).
- Normal SV can *predispose* to secondary pathogenic rearrangement — inversion polymorphisms as risk factors for microdeletion syndromes, framed explicitly as analogous to triplet-repeat "premutation" alleles.
- SV corrupts SNP-based association studies: structurally variant sequence causes marker misinterpretation, segregation anomalies, and assay failures in dbSNP/HapMap.
- The plan: fosmid (~40 kb) libraries from 48 HapMap females + BAC (~150 kb) libraries from 14 HapMap males, ~50 Gb of end-sequence, 10× physical coverage, capturing >98% of each parental haplotype and detecting SV down to **5 kb** (fosmid SD 1.5 kb). Cost estimated at $800k + $150k per individual.

## Methods / evidence

A proposal, not a results paper — its evidentiary weight is the review of 2004–2006 SV surveys plus the design rationale. Notable for candor about limits: cost, small sample size, clone-resource logistics, and the explicit statement that *no single approach* can catalogue all SV. It also predicted its own obsolescence, noting that coupling high-throughput sequencing with paired-end SV detection would eventually make simultaneous SNP+SV analysis feasible in clinical samples — which is what happened.

## Surprising or load-bearing bits

- **Why it belongs in this wiki:** this is the germline analogue of the problem single-cell somatic SV work faces, and the framing transfers directly. Every limitation named here — dosage-only readout, blindness to balanced events, no breakpoint sequence, no mechanism — is *worse* in single cells, where coverage is amplified and uneven. The wiki's SV methods ([[falconer-2012-natmethods|Strand-seq]], [[sanders-2020-sctrip|scTRIP]], [[nanda-2024-smrt-tag]]) are essentially answers to this 2007 problem statement at single-cell scale.
- The insistence that **the reference genome is one haplotype among many** anticipates the pangenome era and is the reason [[highly-repetitive-regions]] remain a systematic dropout in variant calling.
- The "unmasking of recessive alleles on the remaining allele" mechanism is the germline statement of what [[smukowski-heil-2023-loh|LOH]] does somatically in tumors.
- Balanced rearrangements at 1–20% of SV is the number that justifies why copy-number-only single-cell methods (bin-count CNV callers like [[garvin-2015-natmethods|Ginkgo]]) systematically undercount somatic SV — Strand-seq exists precisely to see inversions.

## Entities mentioned

- Evan E. Eichler (University of Washington) — corresponding author; the segmental-duplication and SV program traces to here.
- James R. Lupski — genomic disorders / rearrangement mechanisms.
- NHGRI Large-Scale Genome Sequencing Program — funder and organizational actor.

## Concepts touched

- [[structural-variants]] — this is the canonical definitional and taxonomic source; adds the five phenotypic mechanisms and the balanced/unbalanced split.
- [[highly-repetitive-regions]] — segmental duplications and Y-chromosome palindromes named as the reason BAC-scale inserts were needed.
- [[somagauss-sv]] and single-cell SV callers inherit this problem framing.

## Connections to other sources

- The single-cell answer to the balanced-SV blind spot is [[falconer-2012-natmethods]] (Strand-seq reads inversions by template strand) and [[sanders-2020-sctrip]].
- [[spielmann-2018-sv-3d-genome]] extends the "position effect" mechanism into the TAD framework; [[lupianez-2015-tad-disruption]] supplies the causal demonstration.
- Contrast with [[liu-2025-nanopore-lscc-svs]] and [[nanda-2024-smrt-tag]], where long reads deliver the breakpoint-resolution this proposal had to build clone libraries to get.

## Open questions

- The proposal treats SV as germline/population variation. The somatic SV rate per cell — the quantity this wiki actually cares about — was not addressable by any 2007 method and remains poorly bounded; see [[open-questions]].

## Related

- [[structural-variants]] · [[spielmann-2018-sv-3d-genome]] · [[falconer-2012-natmethods]] · [[somatic-mosaicism]]
