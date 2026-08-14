---
type: summary
title: "Peng et al. 2012 — IDBA-UD: a de novo assembler for single-cell and metagenomic sequencing data with highly uneven depth"
source: "[[00-Sources/papers/IDBA-UD_ a de novo assembler for single-cell and metagenomic sequencing data with highly uneven depth]]"
source_kind: paper
author: "Yu Peng, Henry C. M. Leung, S. M. Yiu, Francis Y. L. Chin (corresponding)"
published: 2012-04-11
ingested: 2026-08-13
doi: "10.1093/bioinformatics/bts174"
journal: "Bioinformatics 28:1420–1428"
tags: [IDBA-UD, single-cell-assembly, metagenomics, iterative-k-mer, depth-relative-threshold, local-assembly, paired-end]
entities: []
concepts: ["[[single-cell-genome-assembly]]", "[[mda]]", "[[sequencing-depth-and-coverage]]", "[[highly-repetitive-regions]]", "[[read-alignment]]"]
topics: ["[[whole-genome-amplification]]", "[[computational-methods]]"]
---

**Citation:** Peng, Leung, Yiu & Chin (2012) — *IDBA-UD: a de novo assembler for single-cell and metagenomic sequencing data with highly uneven depth* — *Bioinformatics* 28, 1420–1428. [DOI](https://doi.org/10.1093/bioinformatics/bts174)

# Peng 2012 — IDBA-UD

> The same problem as [[chitsaz-2011-velvet-sc|Velvet-SC]] — uneven coverage breaks the assumption that low-multiplicity *k*-mers are errors — attacked with three orthogonal fixes instead of one: **multiple depth-relative thresholds** rather than a single global cutoff, **iterative *k*** from k_min to k_max carrying contigs forward as reads, and **local assembly using paired-end information** to bridge low-depth short repeats. It also unifies the single-cell and metagenomic cases, which have the same coverage pathology from different causes.

## Key claims

- **Single-cell and metagenomic data share one statistical problem.** Amplification bias in single-cell MDA and differing species abundance in a microbial community both produce highly uneven depth; both break assemblers written for a single genome at uniform coverage. Treating them as one problem is the paper's framing move.
- **The de Bruijn error-removal assumption fails, explicitly.** The usual heuristic — an erroneous *k*-mer has lower multiplicity than a correct one — is invalid under uneven depth: incorrect *k*-mers in high-depth regions can outnumber correct *k*-mers in low-depth regions. A threshold low enough to keep the latter admits the former; high enough to remove the former deletes the latter. **Multiple depth-relative thresholds** resolve this by making the cutoff local rather than global.
- **The *k* dilemma is real and iteration dissolves it.** Small *k* creates branches (repeats, errors); large *k* creates gaps, especially at low depth. Most assemblers pick an intermediate compromise; IDBA iterates k_min → k_max, feeding each iteration's contigs in as reads for the next so that *k*-mers present at the current *k* but missing at the next are carried forward — closing gaps while relying on larger *k* to resolve repeats.
- **Local assembly with paired-end information** targets Issue (B): gaps in low-depth *short repeat* regions, where neither more *k* nor fewer errors helps.
- **Error correction is applied selectively.** Reads from high-depth regions that align to high-confidence contigs are corrected, which speeds up the process — rather than attempting global correction, which existing tools do poorly on uneven data (the paper names Chaisson & Pevzner, Kelley, and Medvedev approaches as underperforming here).
- **Longer contigs at higher accuracy than Velvet, Velvet-SC, SOAPdenovo and Meta-IDBA** across the tested datasets.

## Methods / evidence

Comparison against four assemblers on single-cell and metagenomic datasets. The source clipping covers the problem formulation and algorithm design in detail; the specific benchmark numbers are in sections not captured here.

Weight: the problem decomposition — three named issues, three targeted fixes — is the reusable content and is unusually clear. The benchmark evidence is not recoverable from this source.

## Surprising or load-bearing bits

- **"Erroneous *k*-mers can have higher multiplicity than correct ones"** is the cleanest one-sentence statement of why uneven coverage is qualitatively, not just quantitatively, harder. It generalises well beyond assembly: any single-cell method that filters by abundance faces the same inversion — which is exactly the trap that [[dong-2017-sccaller|SCcaller]] and [[luquette-2019-natcomm|SCAN-SNV]] address for allelic imbalance in variant calling.
- **Iterating *k* and recycling contigs as reads** is an elegant escape from a parameter choice that other tools treat as a user burden. The pattern — sweep a parameter and feed each result into the next round — recurs in modern pipelines but was not standard in 2012.
- **Single-cell and metagenomic assembly unified in one tool** was a real insight about where the difficulty lives: in the coverage *distribution*, not in the biology of the sample.
- **This paper and [[chitsaz-2011-velvet-sc|Velvet-SC]] reached the same diagnosis independently and prescribed different medicine** — progressive global cutoff vs local depth-relative thresholds. [[bankevich-2012-spades|SPAdes]] then adopted the multisized (multi-*k*) de Bruijn graph, siding with IDBA's iteration idea while rebuilding the rest.

## Concepts touched

- [[single-cell-genome-assembly]] — the multi-threshold and iterative-*k* strategies.
- [[highly-repetitive-regions]] — low-depth short repeats as the specific failure mode local assembly targets.

## Connections to other sources

- Contemporary solving the same problem differently: [[chitsaz-2011-velvet-sc]].
- Superseding synthesis that adopts multisized de Bruijn graphs: [[bankevich-2012-spades]].
- Amplification chemistry that creates the problem: [[dean-2002-mda]], [[huang-2015-scwga-review]], [[hou-2015-wga-comparison]].
- The same abundance-inversion logic in variant calling rather than assembly: [[dong-2017-sccaller]], [[luquette-2019-natcomm]].

## Open questions

- Benchmark specifics (which datasets, what N50, what misassembly rate) are not recoverable from the ingested clipping.
- How k_min and k_max are chosen is not covered in the captured text.
- The paper does not address chimeric reads, which [[chitsaz-2011-velvet-sc]] and [[bankevich-2012-spades]] both treat as a first-class MDA artifact.

## Related

- [[chitsaz-2011-velvet-sc]] · [[bankevich-2012-spades]] · [[single-cell-genome-assembly]]
