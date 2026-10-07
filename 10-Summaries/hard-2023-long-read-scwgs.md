---
type: summary
title: "Hård et al. 2023 — Long-read whole-genome analysis of human single cells"
source: "[[00-Sources/papers/Long-read whole-genome analysis of human single cells]]"
source_quality: full
source_sha256: "5a859507b96473fcc9cc8c4712f1992394c1730fc1a6057d85e5158230fee03c"
source_kind: paper
author: "Joanna Hård, Jeff E. Mold, Jesper Eisfeldt, Christian Tellgren-Roth, Susana Häggqvist, Ignas Bunikis, Orlando Contreras-Lopez, Chen-Shan Chin, Jessica Nordlund, Carl-Johan Rubin, Lars Feuk, Jakob Michaëlsson, Adam Ameur"
published: 2023-08-24
ingested: 2026-10-07
doi: "10.1038/s41467-023-40898-3"
journal: "Nature Communications 14:5164"
tags: [dMDA, droplet-MDA, Xdrop, PacBio-HiFi, long-read-scWGS, structural-variants, tandem-repeats, single-cell-assembly, chimeras, mitochondrial-heteroplasmy, T-cells]
entities: []
concepts: ["[[mda]]", "[[scwga]]", "[[scwga-chemistries]]", "[[pacbio]]", "[[structural-variants]]", "[[allele-dropout]]", "[[single-cell-genome-assembly]]", "[[single-cell-variant-calling]]", "[[mitochondrial-heteroplasmy]]", "[[highly-repetitive-regions]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[long-read-sequencing]]", "[[whole-genome-amplification]]", "[[scdna-seq]]", "[[somatic-mosaicism]]"]
---

**Citation:** Hård et al. (2023) — *Long-read whole-genome analysis of human single cells* — *Nature Communications* 14, 5164. [DOI](https://doi.org/10.1038/s41467-023-40898-3)

# Hård 2023 — long-read single-cell WGS via droplet MDA

> Long-read sequencing needs micrograms of input; a human cell has ~6 pg. The bridge is **droplet MDA (dMDA)**: lyse one FACS-sorted cell, split its DNA into **~50,000 droplets** (Xdrop, <100 µm) so each droplet holds one or a few fragments, amplify with Φ29 inside the droplet, then sequence on **PacBio HiFi**. Partitioning caps over-amplification of any one fragment (better uniformity) and confines chimeras to *within* a molecule (no inter-molecular chimeras in single-fragment droplets). On clonally expanded CD8+ T cells, this gives up to 40% genome coverage per cell, phased SNVs, **5473 true SVs/cell (>16× the Illumina dMDA yield)**, tandem-repeat genotypes, and partial de novo assemblies — but intramolecular chimeras make every called **inversion and duplication essentially false**.

## Key claims

- **dMDA beats tube MDA on uniformity** (Illumina, 8 vs 8 cells, each downsampled to ~100 M read pairs): reads in ≥200× regions 68.9% (MDA) vs 16.0% (dMDA); bases covered ≥1 read 23.4% vs 33.8%; genome-wide coverage SD 2.46× higher for MDA. MDA's unevenness comes from a limited number of fragments amplified to extreme coverage. dMDA also gives better mtDNA coverage.
- **PacBio HiFi on five dMDA cells** (2 from clone A, 3 from clone B): 1–4 µg amplified DNA per cell, fragment peak ~9 kb; up to 2.75 M reads and 20 Gb HiFi (>QV20) per cell on one 8M SMRT cell; ~99% of reads align to GRCh38; but **2.7 separate alignments per HiFi read on average** (dMDA chimeras, mainly intramolecular); aligned-read N50 2.8–3.6 kb, max alignment >50 kb.
- **SNVs (DeepVariant)**: 0.89–1.32 M SNVs called per cell; mean 0.88 M overlap the PacBio bulk truth set, vs 1.06 M true SNVs/cell for Illumina dMDA — similar yield despite PacBio cells having only **32% of the Illumina data** (15.7 vs 48.7 Gb). Precision PacBio 0.86 vs Illumina dMDA 0.74; sensitivity 0.17 vs 0.24, attributed to allelic dropout.
- **"Dark" regions**: 284k high-confidence PacBio SNVs/cell escaped detection in Illumina bulk; 6336 of these fall in previously reported dark, health-relevant genic regions (examples *NBPF8*, *CDC73*).
- **Somatic variation**: 27 somatic SNVs (present in ≥2 cells of one clone, absent from the other clone and bulk), phaseable to haplotypes, plus one **mtDNA heteroplasmy** (chrM:16,218 C>T at 41–67% in the three clone-B cells, absent in clone A and bulk, validated in Illumina) — the abstract's "28 somatic SNVs including one case of mitochondrial heteroplasmy". In the long-read data, 17% of mtDNA reads spanned ≥25% of the mitochondrial genome.
- **SVs (Sniffles2)**: per-cell averages of 3493 deletions, 4636 insertions, 903 duplications and 19,373 inversions were called; >80,000 single-cell SVs absent from bulk are mostly dMDA chimeras (81.5% inversions, typically <5 kb). True SVs: **5473/cell** (2510 deletions, 2957 insertions, only a handful of true dups/inversions) vs **327/cell** in Illumina dMDA (TIDDIT + Manta). Precision 0.73 (deletions), 0.66 (insertions); sensitivity slightly above 0.20; duplication/inversion precision near zero. Size peaks at ~300 bp (Alu) and ~6 kb deletions (LINE). No somatic SV distinguished the two clones.
- **Tandem repeats (Tandem Genotypes)**: of 15,098 TRs genotyped in PacBio bulk, an average of **4770 TR alleles/cell** were genotyped with sizes matching bulk; longest +662 bp (AT dinucleotide). TRs >500 bp largely failed; no clonal somatic TR variation found. The authors say TRs "have not previously been explored in single cells".
- **De novo assembly (hifiasm)** after a BLAST self-hit chimera filter (44.2% and 46.6% of reads pass): primary assemblies 598.3 Mb (A1) and 454.1 Mb (B1) ≈ 19% and 15% of the reference; contig N50 35 kb and 42 kb; largest contig 578.3 kb; ~40 Mb alternative (haplotype) contigs each; BUSCO complete genes 12.8% (n = 1762) and 9.0% (n = 1236); complete, identical mitochondrial genomes in both.

## Methods / evidence

Two YFV-specific CD8+ T-cell clones (A, B) from one healthy vaccinated donor, expanded in vitro 20 days. 16 cells Illumina (8 dMDA, 8 RepliPHI MDA), 5 dMDA cells PacBio Sequel II/IIe. Germline truth = >30× bulk PBMC WGS on both platforms (PacBio bulk 32×). Illumina pipeline: BWA-mem, bcftools, TIDDIT/Manta/SVDB; PacBio: minimap2, DeepVariant v1.5.0, Sniffles2 v2.0.7 (PRECISE only), LAST + Tandem Genotypes, hifiasm. Somatic candidates required presence in ≥2 cells of one clone, absence elsewhere, repeat-masked, then IGV review.

Weight: a solid proof-of-concept but tiny — five long-read cells from one donor, two clones. The bulk-PBMC truth set cannot validate somatic variants (acknowledged). Platform comparison is confounded by unequal data volume (PacBio 32% of Illumina). Somatic SNVs are defined by clone-sharing rather than orthogonal validation (except the mtDNA site). The SV gain is real but restricted to indels; the chemistry is not fit for inversion/duplication discovery, as the authors state.

## Surprising or load-bearing bits

- **Droplets convert the chimera problem from inter- to intramolecular.** Intramolecular chimeras look like inversions and duplications — which is exactly why ~81.5% of false SVs are inversions and why a simple self-BLAST filter (inverted/duplicated self-hits) can remove them. The artifact class is shaped by the WGA geometry. (synthesis)
- **Long reads matched short-read SNV yield with a third of the data and higher precision** (0.86 vs 0.74), because phasing and alignment confidence compensate. Sensitivity stays low (~0.17–0.24) on both — allelic dropout, not read type, is the binding constraint. (synthesis)
- **No somatic SVs or TRs differed between clones** — the authors conclude clone differences are mainly SNVs, with SVs rarer, but stress more cells are needed.
- Single-cell **haplotype-resolved alternative contigs (~40 Mb)** show a single cell can, partially, yield both haplotypes de novo.
- The paper explicitly argues HiFi over nanopore because higher per-read accuracy eases SNV calling and chimera identification.

## Concepts touched

- [[mda]] / [[scwga-chemistries]] — droplet partitioning as a fix for MDA's amplification bias and inter-molecular chimeras; adds a long-fragment WGA route compatible with long reads.
- [[pacbio]] — HiFi applied to amplified single-cell DNA.
- [[structural-variants]] — single-cell indel-type SV detection gains >16× over Illumina; inversion/duplication calls are artifact-dominated.
- [[allele-dropout]] — named as the cause of low SNV/SV sensitivity.
- [[single-cell-genome-assembly]] — partial human single-cell assembly from HiFi reads.
- [[mitochondrial-heteroplasmy]] — clone-specific heteroplasmy detected and phased over long mtDNA reads.
- [[highly-repetitive-regions]] — dark-region SNVs and TRs resolved in single cells.

## Connections to other sources

- MDA background and artifacts: [[dean-2002-mda]], [[hou-2015-wga-comparison]], [[huang-2015-scwga-review]], [[debourcy-2014-plosone]].
- Other long-read single-cell/single-molecule work, mostly epigenomic rather than genomic: [[swanson-2025-daf-seq]] (PacBio + PTA), [[liu-2024-hidef-seq]], [[peter-2024-brain-fiberseq]]; reviews [[fu-2025-longread-methylation]], [[liu-2025-long-read-epigenome-review]].
- Single-cell SV detection by other routes: [[sanders-2020-sctrip]] (Strand-seq).
- Earlier single-cell assembly (bacterial, short-read): [[chitsaz-2011-velvet-sc]], [[bankevich-2012-spades]].
- mtDNA heteroplasmy as a clonal marker: [[ludwig-2019-mtdna-lineage-tracing]], [[kwok-2022-mquad]].

## Open questions

- Would PTA or other more uniform WGA give longer non-chimeric reads and lower dropout than dMDA? The authors note other WGA methods could give more complete genome representation but most produce fragments too short for long reads.
- Whether somatic SVs/TRs are truly rarer than SNVs between clones, or just undetectable at ~20% sensitivity with five cells.
- Bioinformatic chimera resolution (rather than discarding ~55% of reads) is flagged as the main route forward.

## Related

- [[long-read-sequencing]] · [[whole-genome-amplification]] · [[structural-variants]] · [[mda]]
