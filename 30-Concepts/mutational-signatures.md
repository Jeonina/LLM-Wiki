---
type: concept
title: Mutational signatures
aliases: [SBS signatures, COSMIC signatures]
tags: [somatic-mutation, mutational-process, cancer, aging]
created: 2026-05-12
updated: 2026-05-12
---

# Mutational signatures

> Characteristic patterns of single-base substitutions (SBS) decomposed into trinucleotide contexts (96 channels) that reflect specific mutagenic processes — aging-related deamination (SBS1, SBS5), UV exposure (SBS7), tobacco (SBS4), APOBEC activity (SBS2/13), DNA-repair-deficiency, environmental mutagens.

## Definition

Mutations are classified by central substitution × 5'/3' flanking base into 96 categories. Non-negative matrix factorization across many tumor genomes yields recurring patterns ("signatures") associated with mutagenic processes. The Catalogue of Somatic Mutations in Cancer (COSMIC) curates the reference signature set.

## Why it matters

Signatures reveal **mutagenic etiology** from sequence data alone — e.g., SBS4 in lung cancer marks tobacco; SBS2/13 in breast cancer mark APOBEC. Signature analysis on duplex-sequencing data lets researchers read mutagenic exposure from normal tissues without clonal expansion.

## Variants and refinements

- **SBS** (single-base substitution): 96-channel; standard.
- **DBS** (doublet-base substitution): adjacent-pair signatures.
- **ID** (insertion-deletion): indel-context signatures.
- **CN** (copy number) and **SV** (structural variant) signatures: newer extensions.

## Examples

- SBS4 (tobacco) detected in lung tissue of a 74-year-old male via PTA-scDNA-seq + DS validation ([[10-Summaries/a-comprehensive-view-of-somatic-mosaicism-by-single-cell-dna-analysis]]).
- UDSeq reproduces exposure-specific signatures across cell lines and rodent models ([[10-Summaries/a-universal-duplex-sequencing-approach-for-accurate-detection-of-somatic-mutations]]).
- SBS1 (5mC deamination at CpG) dominant in early embryonic mutations; SBS5 dominates aging neurons ([[10-Summaries/bizzotto-2022-brain-mosaicism]]).

## Related

- [[30-Concepts/duplex-sequencing]] · [[30-Concepts/somatic-mosaicism]] · [[20-Entities/ludmil-alexandrov]]
