---
type: summary
title: "Alexandrov et al. 2013 — Signatures of mutational processes in human cancer"
source: "[[00-Sources/papers/Signatures of mutational processes in human cancer]]"
source_kind: paper
author: "Ludmil B. Alexandrov, Serena Nik-Zainal, David C. Wedge, ... Peter J. Campbell, Michael R. Stratton (corresponding)"
published: 2013-08-14
ingested: 2026-08-10
doi: "10.1038/nature12477"
journal: "Nature"
tags: [mutational-signatures, COSMIC, APOBEC, kataegis, 96-context, NMF, somatic-mutation]
entities: []
concepts: ["[[mutational-signatures]]", "[[somatic-mosaicism]]", "[[single-cell-variant-calling]]", "[[dna-methylation]]", "[[single-cell-variant-calling]]"]
topics: ["[[cancer-clonal-evolution]]", "[[somatic-mosaicism]]"]
---

**Citation:** Alexandrov et al. (2013) — *Signatures of mutational processes in human cancer* — *Nature* 500, 415–421. [DOI](https://doi.org/10.1038/nature12477)

# Alexandrov 2013 — mutational signatures

> The paper that turned a cancer genome's passenger mutations from noise into a record. Classify every substitution into one of **96 categories** (6 base changes × 16 trinucleotide contexts), decompose the resulting matrix across thousands of tumours, and distinct **mutational processes** fall out as reproducible spectra. This is the origin of the COSMIC signature catalogue.

## Key claims

- **Scale**: 4,938,362 somatic substitutions and indels from **7,042 primary cancers across 30 classes** (507 whole genomes, 6,535 exomes), each with matched normal DNA to establish somatic origin.
- Mutation prevalence spans **more than five orders of magnitude**, from ~0.001/Mb in some childhood cancers to >400/Mb in melanoma and lung cancer — attributed to differences in the number of cell divisions since the zygote and/or in mutation rate along that lineage.
- **The 96-substitution classification** is the methodological core: six pyrimidine-referenced base substitution classes (C>A, C>G, C>T, T>A, T>C, T>G) × the immediately 5′ and 3′ base. Its purpose is explicitly to separate processes that cause the *same* substitution in *different* sequence contexts.
- **21 validated signatures** were extracted. They differ enormously in shape: some concentrate in one or two of the 96 channels (signature 10), others are near-flat across all 96 (signature 3).
- **Signature 1A/B is near-universal** — present in 25 of 30 cancer classes, characterized by C>T at NpCpG, and attributed to **spontaneous deamination of 5-methylcytosine**. The same process that depleted CpG from the germline genome operates in normal somatic cells.
- **APOBEC** cytidine deaminases produce a signature found across many cancer types — the paper's headline example of an endogenous enzymatic mutator.
- Signatures track **age at diagnosis, known mutagen exposures (tobacco, UV) and DNA-maintenance defects** — but many remain of cryptic origin.
- **Kataegis**: hypermutation localized to small genomic regions, found in many cancer types, is a distinct phenomenon from the genome-wide signatures.

## Methods / evidence

Non-negative matrix decomposition of the 96-channel mutation matrix, applied separately per cancer type and then reconciled, with a validation step distinguishing reproducible signatures from decomposition artefacts. The authors are explicit about why passengers are the right substrate: because most mutations in a cancer genome are passengers, they are **not shaped by selection**, so the spectrum reports the mutational process rather than the fitness landscape. Earlier signature work based on *TP53* driver mutations suffered exactly the opposite problem — selection signatures superimposed on process signatures, and composite spectra when multiple processes operate.

Exome data are usable but explicitly less powerful than whole genomes for this decomposition.

## Surprising or load-bearing bits

- **Signature 1 is a methylation signature.** C>T at CpG arises from deamination of 5mC, so the most universal mutational process in human cancer is a direct chemical consequence of the epigenome. This is the hardest available link between [[dna-methylation]] and somatic mutation, and it means CpG-dense regions carry an elevated mutation rate as an intrinsic cost of being methylated — the mechanism named in [[jones-2012-dna-methylation-functions|Jones 2012]].
- Because signature 1 accumulates with time rather than with a specific exposure, it behaves as a **molecular clock**, which is what later work exploits to date clonal expansions and to time subclone emergence.
- **The single-cell relevance is oblique but sharp**: signature analysis needs thousands of mutations per sample, and single-cell WGA amplification artefacts have their own context biases that mimic real signatures. Any per-cell signature claim requires an artefact model — which is exactly the argument [[gonzalez-pena-2021-pnas|PTA]] and amplification-comparison studies make about false-positive spectra. A WGA-derived "signature" can be chemistry, not biology.
- The five-orders-of-magnitude prevalence range makes **mutation burden a per-tissue quantity**, not a universal threshold, which constrains any variant-calling sensitivity requirement to be set per tissue type.
- The honest scorecard: over 20 signatures found, **only a minority mechanistically explained**. Cryptic signatures were the field's open problem in 2013 and many remain so.

## Concepts touched

- [[mutational-signatures]] — this is the founding source; the 96-channel classification and the original numbered catalogue come from here.
- [[single-cell-variant-calling]] — provides the interpretive layer that turns an SNV list into a process inference.
- [[dna-methylation]] — via signature 1's 5mC-deamination mechanism.

## Connections to other sources

- Mechanistic upstream: [[jones-2012-dna-methylation-functions]] on 5mC deamination and CpG depletion.
- Applied to single cells, requires the artefact controls argued in [[gonzalez-pena-2021-pnas]] and the chemistry comparisons in [[scwga-chemistries]].
- Clonal-evolution context: [[navin-2011-sns-tumor-evolution]], [[xu-2012-single-cell-exome-kidney]].
- Calling infrastructure that produces the input mutation lists: [[mckenna-2010-gatk]], [[li-2009-samtools]].

## Open questions

- Most signatures had **no assigned mechanism** at publication; the aetiology gap is the paper's own stated limitation.
- Whether signatures extracted from bulk tumours are superpositions of subclone-specific processes is unaddressable at bulk resolution — a question single-cell mutation catalogues are in principle positioned to answer, and none in this corpus yet does at scale.

## Related

- [[mutational-signatures]] · [[jones-2012-dna-methylation-functions]] · [[cancer-clonal-evolution]] · [[somatic-mosaicism]]
