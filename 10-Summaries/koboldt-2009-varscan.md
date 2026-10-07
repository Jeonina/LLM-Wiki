---
type: summary
title: "Koboldt et al. 2009 — VarScan: variant detection in massively parallel sequencing of individual and pooled samples"
source: "[[00-Sources/papers/VarScan_ variant detection in massively parallel sequencing of individual and pooled samples]]"
source_quality: full
source_sha256: "4386384772c3d21f99a3407a6b1f97165439d6da5dba07f5d3619043499983bb"
source_kind: paper
author: "Daniel C. Koboldt (corresponding), Ken Chen, Todd Wylie, David E. Larson, Michael D. McLellan, Elaine R. Mardis, George M. Weinstock, Richard K. Wilson, Li Ding"
published: 2009-06-19
ingested: 2026-10-07
doi: "10.1093/bioinformatics/btp373"
journal: "Bioinformatics 25(17):2283–2285"
tags: [VarScan, variant-calling, SNP, indel, pooled-sequencing, allele-frequency, Roche-454, Illumina, heuristic-caller]
entities: []
concepts: ["[[single-cell-variant-calling]]", "[[read-alignment]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[mosaic-variant-calling]]", "[[computational-methods]]"]
---

**Citation:** Koboldt et al. (2009) — *VarScan: variant detection in massively parallel sequencing of individual and pooled samples* — *Bioinformatics* 25:2283–2285. [DOI](https://doi.org/10.1093/bioinformatics/btp373)

# Koboldt 2009 — VarScan

> An early-NGS-era applications note: variant detection tools of the time were tied to one platform or aligner (Newbler → 454 only; SHORE → its own aligner, Illumina only). VarScan is an **aligner-agnostic, heuristic** SNP/indel caller — read-level filtering, then simple thresholds on coverage, base quality, supporting reads and variant frequency — that works on both individual and **pooled** samples. The pooled use case is the point: by reporting read counts and allele frequencies rather than diploid genotypes, it can call variants at ~1% frequency in a deep pool.

## Key claims

- **Aligner/platform independence**: compatible with BLAT, Newbler, cross_match, Bowtie and Novoalign; calls variants in individual and pooled samples.
- **Workflow**: per-read scoring, discarding low-identity and multiply-mapped reads; screen the single best alignment per read; merge supporting reads into unique SNPs/indels; report coverage, supporting reads, average base quality and strands per allele. Thresholds are set automatically by an *easyrun* command but user-adjustable.
- **Test data**: targeted resequencing of 1,000 PCR amplicons (~250 kb); 42 samples sequenced individually on 454 at ~70×, and the same samples pooled on Illumina GAII at ~6,000× (~125× per sample).
- **454 settings**: BLAT alignment; reads with score <50, <95% identity or multiple competing locations discarded; SNPs called at >10× coverage with >25% variant-supporting reads.
- **Concordance**: of 359 SNPs called in 454 data, 215 (59.78%) were in dbSNP 129; VarScan detected 344 (95.82%) in the pooled Illumina data, including 118 of 142 singleton heterozygotes (83%) present on 1 of 84 pooled chromosomes; 349/359 (97.21%) confirmed by Illumina or dbSNP. The authors summarise this as ~97% specificity (individual 454) and ~93% sensitivity (pooled Illumina).
- **Comparison with platform tools**: Newbler identified 80/359 (22.28%) of the SNPs in 454 data; Maq identified 340/359 (94.71%) in Illumina data, but only three passed Maq's SNPfilter.
- **Pooled allele frequencies track truth**: Pearson r = 0.962 between pooled Illumina read-count frequencies and known 454 frequencies (344 SNPs); high-frequency variants were slightly underestimated, attributed to reference-mapping disadvantage of variant-containing short reads.
- **Indels**: >200 indels (1–97 bp) predicted in 454 data after homopolymer filtering; of 77 high-confidence 1–5 bp indels, 46 (59.74%) were also detected in Illumina reads remapped with Novoalign.
- **Runtime**: ~1,423 s per individual 454 sample, ~1,625 s per Illumina lane. Implemented in Perl and inline C.

## Methods / evidence

Single real dataset (targeted amplicons, 42 individuals), with truth approximated by cross-platform concordance and dbSNP rather than an orthogonal gold standard. Comparison to Newbler and Maq is on overlap with VarScan's own 454 call set, so it measures agreement with VarScan, not independent accuracy.

Weight: a short applications note. Sensitivity/specificity figures are concordance-based and specific to high-depth targeted data; they say little about whole-genome or low-depth settings. The allele-frequency correlation (r = 0.962) is the most transferable result.

## Surprising or load-bearing bits

- **Frequency-first, not genotype-first, calling** — reporting read counts per allele instead of forcing a diploid genotype is what lets the same tool serve pooled samples and, later, low-VAF somatic contexts. (synthesis)
- **Reference bias is already visible in 2009**: pooled frequency estimates were slightly low at high VAF because variant-bearing short reads map worse — the same mapping-bias issue that later haunts low-VAF mosaic calling. (synthesis)
- The comparison with Maq (94.71% detected, but only 3 passing SNPfilter) illustrates how much a caller's default filters, not its raw detection, govern reported results.

## Concepts touched

- [[single-cell-variant-calling]] — VarScan is a bulk, heuristic caller; it is a historical baseline for the threshold-based callers that single-cell and mosaic methods were later built to improve on. (synthesis)
- [[read-alignment]] — explicitly designed around heterogeneous aligner outputs; accuracy depends on alignment quality, with recommended parameters per aligner.
- [[sequencing-depth-and-coverage]] — ~1% variant detection relies on ~6,000× pooled depth.

## Connections to other sources

- Contemporaneous infrastructure for NGS variant calling: [[li-2009-samtools]], [[mckenna-2010-gatk]], [[li-2009-bwa]] — VarScan predates the SAM/BAM-centred ecosystem and instead parses multiple aligner formats. (synthesis)
- Co-author Ken Chen: the source does not state whether this is the same person as the MD Anderson [[ken-chen]] entity, so no entity link is asserted.
- Later mosaic/low-VAF callers in the wiki address what heuristic thresholds cannot: [[huang-2017-mosaichunter]], [[dou-2020-mosaicforecast]], [[yang-2023-deepmosaic]]. (synthesis)

## Open questions

- The ~1%-frequency sensitivity (83% for singletons in an 84-chromosome pool) is measured only at ~6,000× targeted depth; how the heuristic thresholds behave at genome-wide depths is not addressed.
- No error model — strand and base-quality information is reported but not modelled, so sequencing/PCR artifacts at low VAF are controlled only by thresholds.

## Related

- [[single-cell-variant-calling]] · [[40-Topics/mosaic-variant-calling]] · [[li-2009-samtools]]
