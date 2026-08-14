---
type: summary
title: "Chitsaz et al. 2011 — Efficient de novo assembly of single-cell bacterial genomes from short-read data sets (Velvet-SC / E+V-SC)"
source: "[[00-Sources/papers/Efficient de novo assembly of single-cell bacterial genomes from short-read data sets]]"
source_kind: paper
author: "Hamidreza Chitsaz, Joyclyn L. Yee-Greenbaum, Glenn Tesler, Mary-Jane Lombardo, Christopher L. Dupont, Jonathan H. Badger, Mark Novotny, Douglas B. Rusch, Louise J. Fraser, Niall A. Gormley, Ole Schulz-Trieglaff, Geoffrey P. Smith, Dirk J. Evers, Pavel A. Pevzner, Roger S. Lasken"
published: 2011-09-18
ingested: 2026-08-13
doi: "10.1038/nbt.1966"
journal: "Nature Biotechnology 29:915–921"
tags: [Velvet-SC, E+V-SC, single-cell-assembly, MDA, uneven-coverage, chimera, de-Bruijn-graph, SAR324, uncultivated-bacteria]
entities: ["[[pavel-pevzner]]"]
concepts: ["[[single-cell-genome-assembly]]", "[[mda]]", "[[scwga]]", "[[sequencing-depth-and-coverage]]", "[[read-alignment]]"]
topics: ["[[whole-genome-amplification]]", "[[computational-methods]]", "[[scdna-seq]]"]
---

**Citation:** Chitsaz et al. (2011) — *Efficient de novo assembly of single-cell bacterial genomes from short-read data sets* — *Nature Biotechnology* 29, 915–921. [DOI](https://doi.org/10.1038/nbt.1966)

# Chitsaz 2011 — Velvet-SC

> The first assembler adapted to [[mda|MDA]]'s coverage catastrophe, and the paper that reframed the field: *"the challenges facing single-cell genomics are increasingly computational rather than experimental."* The fix is one idea — replace the **single coverage cutoff** that every de Bruijn assembler uses to prune errors with a **progressively increasing cutoff**, so low-coverage regions survive pruning while high-coverage errors still get removed.

## Key claims

- **A single coverage cutoff is fatal for MDA data, and the numbers show why.** In multicell *E. coli*, most positions sit at 450–800× and only 0.1% fall below 450×, so a threshold prunes errors cleanly. In single-cell *E. coli*, **5% of positions have <10× and 11% have <30×** — and 30× is roughly the minimum most assemblers need for gap-free assembly. Any threshold high enough to remove errors also deletes a tenth of the genome.
- **The progressive cutoff is the algorithm.** Velvet-SC raises the coverage threshold gradually rather than applying one value, assembling high-coverage regions under strict pruning and low-coverage regions under permissive pruning.
- **E+V-SC couples error correction to the assembler.** Velvet-SC is combined with EULER's error correction, because standard correction tools (Quake and similar) implicitly assume near-uniform coverage and perform poorly on single-cell data.
- **>91% of genes captured within contigs** from single *E. coli* and *Staphylococcus aureus* cells, against 95% from a multicell *E. coli* assembly — the gap between one cell and many cells narrows to four percentage points, without gap closing or repeat resolution.
- **A real uncultivated genome, not just a benchmark.** Assembly of a single cell from the **SAR324 clade of Deltaproteobacteria** — a cosmopolitan marine lineage — with metabolic reconstruction suggesting it is aerobic, motile and chemotaxic. This is genome-*centric* information that metagenomics structurally cannot provide, because metagenomic data cannot say which genes co-occur in one organism.
- **Two MDA artifacts, named separately.** Amplification bias gives orders-of-magnitude coverage differences and outright absent regions; **chimera formation** arises during φ29's branching amplification and joins non-contiguous sequences. Greater coverage alleviates chimeras but does not remove them.
- **The motivation is scale**: over 99% of microbes cannot be cultivated, so single-cell sequencing plus metagenomics is the only route to their genomes.

## Methods / evidence

Two known genomes (*E. coli*, *S. aureus*) as ground truth with matched multicell controls, plus one unknown marine genome. Assembly quality assessed by gene capture within contigs and contig statistics (>110 bp).

Weight: the *E. coli*/*S. aureus* controls are the right design — assembly claims are only checkable against a known reference. The SAR324 result is a demonstration, and its metabolic reconstruction inherits whatever the assembly got wrong.

## Surprising or load-bearing bits

- **This is the earliest paper in the corpus to state that WGA's problems had become a computational rather than a wet-lab burden** — a claim that recurs almost verbatim through the mosaic-variant-calling literature a decade later ([[lahnemann-2021-natcomm]], [[ha-2023-natmethods]]).
- **Coverage non-uniformity is a *different* problem from coverage depth**, and this paper is where that distinction gets operationalised. Every downstream single-cell caller — [[zafar-2016-monovar|Monovar]], [[dong-2017-sccaller|SCcaller]], [[luquette-2019-natcomm|SCAN-SNV]] — solves a variant of the same problem in a different data type.
- **The 91% vs 95% gene-capture gap is remarkably small** for 2011, and it explains why bacterial single-cell genomics matured years before human single-cell variant calling did: gene *presence* is far more robust to dropout than base-level genotype.
- **Chimeras appear here as an assembly-graph problem** rather than a variant-calling problem — the same MDA artifact that [[huang-2015-scwga-review]] later names as the reason single-cell structural variants resist detection.
- **The authors ignored read pairing deliberately** (as [[bankevich-2012-spades|SPAdes]] later notes) because chimeric read-pairs cause misassemblies — a conservative choice that SPAdes then reversed by handling the chimeras explicitly.

## Entities mentioned

- [[pavel-pevzner]] — coauthor; de Bruijn graph assembly; also senior author of [[bankevich-2012-spades|SPAdes]], which supersedes this tool.

## Concepts touched

- [[single-cell-genome-assembly]] — this is the founding paper for the concept.
- [[mda]] — the coverage-bias and chimera profile that defines the problem.

## Connections to other sources

- Directly superseded by: [[bankevich-2012-spades]], whose authors include two coauthors of this paper (Tesler, Pevzner) and who state explicitly that modifying existing tools was insufficient.
- Parallel solution to the same problem: [[peng-2012-idba-ud]] (multiple depth-relative thresholds + iterative *k*).
- Chemistry context: [[dean-2002-mda]], [[huang-2015-scwga-review]], [[hou-2015-wga-comparison]].
- The human-genome branch of the same amplification problem: [[navin-2011-sns-tumor-evolution]], [[wang-2014-nuc-seq]].
- Amplification-free routes that dissolve the problem: [[zahn-2017-dlp]], [[laks-2019-dlp-plus]].

## Open questions

- **The progressive cutoff has no principled stopping rule** in this source; the schedule is heuristic.
- Chimera rate is described qualitatively but not quantified, and no chimera-detection step is part of the pipeline (SPAdes adds one).
- Whether the SAR324 metabolic reconstruction is complete enough to support the aerobic/motile/chemotaxic conclusions depends on assembly completeness that cannot be checked without a reference.

## Related

- [[bankevich-2012-spades]] · [[peng-2012-idba-ud]] · [[single-cell-genome-assembly]] · [[40-Topics/whole-genome-amplification]]
