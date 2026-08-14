---
type: concept
title: Mutational signatures
aliases: [SBS signatures, COSMIC signatures]
tags: [somatic-mutation, mutational-process, cancer, aging]
created: 2026-05-12
updated: 2026-08-10
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

- SBS4 (tobacco) detected in lung tissue of a 74-year-old male via PTA-scDNA-seq + DS validation ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]).
- UDSeq reproduces exposure-specific signatures across cell lines and rodent models ([[10-Summaries/nandi-2025-udseq]]).
- SBS1 (5mC deamination at CpG) dominant in early embryonic mutations; SBS5 dominates aging neurons ([[10-Summaries/bizzotto-2022-brain-mosaicism-review]]).

## Founding source (added 2026-08-10)

[[10-Summaries/alexandrov-2013-mutational-signatures]] established the 96-substitution classification (six pyrimidine-referenced base changes × 16 trinucleotide contexts) and extracted 21 validated signatures from 4,938,362 mutations across 7,042 cancers of 30 classes. Signature 1A/B — C>T at NpCpG from spontaneous deamination of 5-methylcytosine — appears in 25 of 30 cancer classes, making the most universal mutational process in human cancer a direct chemical consequence of the epigenome.

Two constraints for single-cell work: mutation prevalence spans five orders of magnitude between cancer types, so burden thresholds must be set per tissue; and WGA amplification artefacts carry their own context biases that can mimic real signatures, so any per-cell signature claim requires an explicit artefact model ([[10-Summaries/alexandrov-2013-mutational-signatures]], synthesis).


## Related

- [[40-Topics/duplex-sequencing]] · [[40-Topics/somatic-mosaicism]] · [[20-Entities/ludmil-alexandrov]]

## Added 2026-08-13

The framework extends from 96 to **192 trinucleotide contexts** once single-strand events can be read: the standard 96-context spectrum collapses each mutation onto its pyrimidine representation, discarding strand, but with per-strand single-molecule data the pyrimidine/purine split carries real information ([[10-Summaries/liu-2024-hidef-seq]]).

**New nomenclature**: an `ss` suffix marks a single-strand mismatch signature, `ss*` a single-strand damage signature. SBS10ss (*POLE* proofreading deficiency) projects onto its samples' own dsDNA signatures at cosine 0.97 and onto COSMIC SBS10c at 0.90; SBS14ss covers combined MMR + proofreading deficiency; SBS30ss* is cytosine deamination damage ([[10-Summaries/liu-2024-hidef-seq]]).

This resolves **which chemical event initiated which mutation class** — previously inferrable only indirectly from replication-timing asymmetry or from in vitro gap-filling assays lacking replication and repair context ([[10-Summaries/liu-2024-hidef-seq]]).

Signature reasoning also appears without a formal signature framework: TC-motif cytosine bias in childhood ALL was read as APOBEC rather than AID activity, supported by the absence of a WRCY motif and the lack of correlation with VH-segment mutation ([[10-Summaries/gawad-2014-all-clonal-origins]]).
