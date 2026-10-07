---
type: concept
title: SAMOSA
aliases: [single-molecule adenine-methylated oligonucleosome sequencing assay]
tags: [PacBio, chromatin-accessibility, single-molecule, EcoGII, Ramani-lab]
created: 2026-05-12
updated: 2026-10-07
---

# SAMOSA

> A single-molecule chromatin-accessibility method developed by the Ramani lab that uses in-nucleus EcoGII methyltransferase to mark accessible (nucleosome-free) regions with 6mA, then PacBio sequencing to read accessibility patterns along kilobase-length single fibers.

## Definition

EcoGII non-specifically methylates A bases in accessible regions; protected (nucleosome- or TF-bound) regions remain unmodified. PacBio detects 6mA via polymerase-kinetic signatures.

## Why it matters

- Single-fiber chromatin maps reveal co-occurrence of nucleosomes, TF binding, and CpG methylation on the same molecule.
- Bulk-only by default; [[30-Concepts/samosa-tag]] reduces input via tagmentation.

## Added 2026-10-07

**Correction from the full text:** in the original SAMOSA protocol EcoGII methylates oligonucleosomes after MNase release from nuclei (fragments ~500 bp–2 kb), so it captures nucleosome registers but not TF footprints; input was 100 × 10⁶ K562 cells ([[10-Summaries/abdulhay-2020-samosa]]). Its Results show H3K36me3 enriched for irregular and short regular fibres, which runs against the Introduction's framing of long regular arrays in elongating chromatin ([[10-Summaries/abdulhay-2020-samosa]]).

## Related

- [[30-Concepts/samosa-tag]] · [[30-Concepts/fiber-seq]] · [[30-Concepts/single-molecule-footprinting]] · [[30-Concepts/pacbio]] · [[40-Topics/long-read-sequencing]]
