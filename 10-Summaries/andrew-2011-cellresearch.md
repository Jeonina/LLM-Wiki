---
type: summary
title: "Bannister & Kouzarides 2011 — Regulation of chromatin by histone modifications (review)"
aliases: [Bannister 2011, Bannister Kouzarides 2011]
tags: [histone-modifications, chromatin, review, foundational, epigenetics]
created: 2026-05-12
updated: 2026-05-12
sources: ["00-Sources/papers/Andrew_2011_CellResearch.pdf"]
---

# Bannister & Kouzarides 2011 — Regulation of chromatin by histone modifications

> Andrew J. Bannister & Tony Kouzarides. *Cell Research* **21**, 381–395 (March 2011). DOI: 10.1038/cr.2011.22. (The "Andrew_2011" filename refers to Andrew J. Bannister — *not* Andrew B. Stergachis.)

## Thesis

Canonical foundational review of **histone post-translational modifications** (acetylation, methylation, phosphorylation, ubiquitination, sumoylation, ADP-ribosylation, deimination, proline isomerization), the enzymes that deposit and remove them, and the chromatin-regulatory consequences of each. Not a single-cell paper at all — included in this wiki because it is the standard reference for the chromatin-mark biology that scCUT&Tag, scChIC-seq, scCUT&RUN, fiber-seq, and DAF-seq all measure.

## Key claims

This is a comprehensive review; the load-bearing points for the wiki are:

1. **Histone acetylation**: by HATs (Type A: GNAT, MYST, CBP/p300 families; Type B: scHat1-related). Removed by HDACs (Classes I, II, III/sirtuins, IV). Lysine acetylation neutralizes positive charge → weakens histone-DNA interaction → opens chromatin. H3K56ac in the globular core is functionally distinct from N-terminal tail marks.
2. **Histone phosphorylation**: on Ser/Thr/Tyr, especially N-terminal tails. Kinases lack site-specific DNA-binding domains as a rule (MAPK1 is an exception). Examples: H3S10ph and H3S28ph by Aurora B at mitosis; H3Y41ph by JAK2.
3. **Histone methylation**: lysines (mono/di/tri-methyl) by SET-domain HKMTs (e.g., SUV39H1 for H3K9, SET7/9 for H3K4), exception DOT1 (H3K79, no SET domain). Arginines (mono/di-symmetric/di-asymmetric) by PRMTs (PRMT1, 4, 5, 6). Unlike acetylation, methylation does not change residue charge — it acts via reader-protein recruitment.
4. **Histone demethylases**: LSD1 (FAD-dependent, removes mono/di-methyl), Jumonji-family JmjC demethylases (Fe(II)/α-KG, can remove tri-methyl). Discovery of LSD1 (2004) overturned the dogma that methylation was irreversible.
5. **The "histone code" perspective**: combinations of marks specify chromatin states (active enhancers, poised promoters, heterochromatin, etc.) — interpreted by reader-domain proteins (bromodomains for acetyl-lys, chromodomains for methyl-lys, etc.).

## Why this is in the wiki

- **Background reference** for any concept page touching histone modifications: [[histone-modifications]], [[cut-and-tag]], [[cut-and-run]], [[scchic-seq]], [[scicut-tag]], [[multi-tag]], [[scchix-seq]].
- For the review paper §3.4 (Chromatin State): Bannister & Kouzarides is the foundational reference that anchors why histone-modification-based single-cell methods (scCUT&Tag, etc.) target the marks they target.
- For the somatic-mosaicism + epi synthesis: Bannister & Kouzarides defines the layer of epigenetic memory (especially H3K4me3/H3K27me3 bivalency, H3K9me3 heterochromatin) that scNMT-seq, scTrio-seq, and scCUT&Tag-based assays read at single-cell resolution.

## Entities / concepts touched

[[histone-modifications]] · [[chromatin-accessibility]] · [[dna-methylation]] · [[chip-seq]] · [[40-Topics/histone-modifications]] · [[40-Topics/chromatin-architecture]]

## Note on filename

`Andrew_2011_CellResearch.pdf` = Andrew J. Bannister (Cambridge, Gurdon Institute). Do not confuse with `AndrewB_2020_Science.pdf` (Andrew B. Stergachis — Fiber-seq) or `AndrewC_2020_Science.pdf` (Andrew C. Payne — IGS).
