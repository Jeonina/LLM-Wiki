---
type: summary
title: "Rodriguez-Fraticelli & Parreno 2026 — Charting single-cell lineages with synthetic and natural barcodes"
source: "[[00-Sources/papers/Charting single-cell lineages with synthetic and natural barcodes - Nature Reviews Genetics]]"
source_kind: paper
author: "Alejo E. Rodriguez-Fraticelli (corresponding), Victoria Parreno"
published: 2026-02-27
ingested: 2026-06-02
doi: "10.1038/s41576-026-00943-5"
journal: "Nature Reviews Genetics"
tags: [lineage-tracing, review, synthetic-barcodes, natural-barcodes, CRISPR-recording, clonal-hematopoiesis, epimutation, mitochondrial]
entities:
  - "[[20-Entities/alejo-rodriguez-fraticelli]]"
  - "[[20-Entities/jay-shendure]]"
concepts:
  - "[[30-Concepts/lineage-tracing]]"
  - "[[30-Concepts/crispr-lineage-recording]]"
  - "[[30-Concepts/mitochondrial-lineage-tracing]]"
  - "[[30-Concepts/methylation-clones-epimutation]]"
  - "[[40-Topics/clonal-hematopoiesis]]"
concepts_secondary:
  - "[[40-Topics/duplex-sequencing]]"
  - "[[30-Concepts/scwga]]"
topics:
  - "[[40-Topics/single-cell-lineage-tracing]]"
  - "[[40-Topics/cancer-clonal-evolution]]"
---

**Citation:** Rodriguez-Fraticelli & Parreno (2026) — *Charting single-cell lineages with synthetic and natural barcodes* — *Nature Reviews Genetics*. [DOI](https://doi.org/10.1038/s41576-026-00943-5)

# Rodriguez-Fraticelli & Parreno 2026 — Lineage-tracing toolbox review

> Thesis: A comprehensive modern map of single-cell lineage tracing, organized along two axes — **prospective (synthetic barcodes)** vs **retrospective (natural variants)**, and **static** vs **evolvable** labels. The review argues lineage tracing is now mature enough to overturn classical paradigms in development, ageing, and cancer, and that the frontier is multimodal (genome + epigenome + transcriptome + spatial) tracing and eventual clinical clonal diagnostics.

## Key claims

- Two broad families: **prospective** methods engineer synthetic barcodes (flexible/programmable, but require genetic manipulation → model systems); **retrospective** methods read naturally accumulated somatic variants (ideal for human biology, no engineering).
- **Synthetic static integrative barcodes**: lentiviral random-sequence libraries (cheap, democratized) — main risk is barcode homoplasy (two cells, same barcode); capture has evolved from bulk FACS+PCR → expressed barcodes in scRNA-seq → multi-omic (CellTagMulti flanks barcodes with Nextera adapters for scATAC capture) → spatial (Visium, probe-based) → optical/protein read-outs enabling live clone recapture.
- **Synthetic static inducible barcodes**: recombinase arrays (Polylox, LoxCode; PolyloxExpress adds RNA capture; PolyTope uses epitope tags), transposases (Sleeping Beauty/PiggyBac — near-unlimited diversity, but integration-site sequencing has high dropout and no transcriptome pairing), and DRAG (Rag + TdT on a synthetic VDJ locus).
- **Synthetic evolvable (CRISPR recording)**: Cas9 cuts a multi-target reporter; mutations accrue to build phylogenies. Diversity-boosting tricks: self-homing hgRNAs, base editors (substitutions not deletions), Cas12a (cuts outside guide), Cas9+TdT writer polymerase, and prime-editing-based recording that writes known "symbols" (enabling probe-based spatial PE-tracer). Main bottleneck is bioinformatic barcode interpretation across many sparse alleles.
- **Natural DNA variants**: nuclear SNVs are the gold standard for phylogeny but need either error-corrected/duplex sequencing (rare-variant detection, but only spatial-region comparisons, no trees) or colony-based scWGS (clonal expansion error-corrects amplification noise). Joint WGS+RNA now emerging — DEFND-seq, ResolveOME, SMART-PTA. STRs/homopolymers mutate faster (cell-division resolution) but slip during library prep; CNVs/SVs trace malignant cells.
- **Mitochondrial DNA**: mutates 10–100× faster, short/easy to sequence multimodally, but high copy number + random segregation means only high-heteroplasmy variants persist; hybridization capture recovers more variants but risks artifacts.
- **Somatic epimutations**: DNA-methylation changes at CpGs are now usable lineage labels. Ground-truth barcoding revealed universally stable, clonally heritable "static" CpGs (MethylTree on scWGMS; scTAM-seq + EPI-clone for targeted/Tapestri readout). A head-to-head shows the **methylome beats ATAC and RNA for clonal inference**.
- Biology overturned: more diverse developmental origins than expected (3 yolk-sac mesoderm populations; embryonic MPPs separate from adult HSCs); age-associated clonal expansions across tissues, including driver-less expansions; tumours change behavior via heritable non-genetic (epigenetic) memory without new mutations.

## Methods / evidence

Authoritative narrative review (Nat Rev Genet) with two method tables and a method-selection figure. Authored by a leading clonal-hematopoiesis lab (Fraticelli; advisor to Retro Biosciences).

## Surprising or load-bearing bits

- The static-vs-evolvable × prospective-vs-retrospective grid is the cleanest organizing scheme in the field — use it for the [[40-Topics/single-cell-lineage-tracing]] topic.
- The methylome's superiority over ATAC/RNA for clonal inference (when benchmarked against ground-truth barcodes) is a strong, specific claim worth tracking.
- "Driver-less" clonal expansions and non-genetic heritable tumour adaptation reframe both ageing and cancer as partly epigenetic/selection phenomena, not purely mutational.

## Entities mentioned

- [[20-Entities/alejo-rodriguez-fraticelli]] — corresponding author.
- [[20-Entities/jay-shendure]] — prime-editing-based recording.
- [[20-Entities/caleb-lareau]], [[20-Entities/leif-ludwig]] — mtDNA tracing; [[20-Entities/tim-coorens]] — reviewer / somatic phylogenetics.

## Concepts touched

- [[30-Concepts/crispr-lineage-recording]] — defines the evolvable-barcode landscape.
- [[30-Concepts/lineage-tracing]], [[30-Concepts/mitochondrial-lineage-tracing]], [[30-Concepts/methylation-clones-epimutation]] — the three natural-variant routes.
- [[40-Topics/clonal-hematopoiesis]] — central biological payoff.

## Connections to other sources

- Cites DEFND-seq ([[10-Summaries/olsen-2025-defnd-seq]]) as a joint WGS+RNA method; Tapestri ([[10-Summaries/pellegrino-2018-tapestri]]) for targeted genotyping.
- Epimutation tracing connects to [[10-Summaries/chen-2025-methyltree]] (MethylTree) and [[10-Summaries/scherer-2025-nature]] (EPI-clone/somatic epimutations).
- mtDNA tracing to [[10-Summaries/ludwig-2020-mtscatac-seq]], [[10-Summaries/miller-2022-maester]].
- Companion computational review: [[10-Summaries/wang-2026-multimodal-lineage-computational]] (same NRG issue, cites this one) — this paper = technologies, that one = algorithms.
- Somatic-mutation phylogenetics connects to [[10-Summaries/lee-six-2018-hsc-dynamics]], [[10-Summaries/coorens-2021-nature]].

## Open questions

- Is loss of clonality a biomarker of, or a mechanism driving, ageing?
- Do driver-less expansions reflect positive selection or neutral drift?
- Cost remains prohibitive for clinical-scale clonal diagnostics — the central translational barrier.

---
**Source:** [DOI](https://doi.org/10.1038/s41576-026-00943-5)
## Related

- [[40-Topics/single-cell-lineage-tracing]] · [[30-Concepts/lineage-tracing]] · [[30-Concepts/crispr-lineage-recording]] · [[30-Concepts/methylation-clones-epimutation]] · [[20-Entities/alejo-rodriguez-fraticelli]]
