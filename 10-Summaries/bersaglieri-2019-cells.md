---
type: summary
title: "Bersaglieri & Santoro 2019 — Genome organization in and around the nucleolus"
source: "[[00-Sources/papers/Genome Organization in and around the Nucleolus.pdf]]"
source_quality: full
source_sha256: "b607eb6ef17c0797dce22d695deccda08f88c9ace77bbb93e056a6d57fd6b45c"
source_kind: paper
author: "Cristiana Bersaglieri, Raffaella Santoro (corresponding)"
published: 2019-06-12
ingested: 2026-05-13
updated: 2026-10-07
doi: "10.3390/cells8060579"
journal: "Cells 8(6):579"
aliases: ["Bersaglieri 2019", "nucleolar genome organization review"]
tags: [review, nucleolus, 3D-genome, heterochromatin, rRNA, NoRC, TIP5, pRNA, lncRNA, NADs, LADs, embryonic-stem-cells, genome-stability]
entities: []
concepts: ["[[lamina-associated-domains]]", "[[nuclear-lamina]]", "[[chromatin-phase-separation]]", "[[damid]]", "[[sc-sprite]]", "[[single-cell-hi-c]]", "[[epigenetic-memory]]"]
topics: ["[[3d-genome]]", "[[dna-methylation]]", "[[histone-modifications]]"]
---

**Citation:** Bersaglieri & Santoro (2019) — *Genome organization in and around the nucleolus* — *Cells* 8(6):579. [DOI](https://doi.org/10.3390/cells8060579) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/31212844/)

# Bersaglieri 2019 — the nucleolus as a genome-organizing compartment

> A narrative review from the Santoro lab (University of Zurich) arguing that the nucleolus and its rRNA genes do more than make ribosomes. Mammalian rRNA genes exist in three chromatin states — **active** (unmethylated, UBF-bound, nucleosome-free), **inactive** (unmethylated but nucleosome-packed, not bound by UBF or NoRC) and **silent** (promoter CpG-methylated, H3K9me2/3, deacetylated). Silent copies are established on exit from pluripotency by the remodeling complex **NoRC** (TIP5 + SNF2H), which is guided to rDNA by a ~200-nt lncRNA, **pRNA**, cut from intergenic spacer transcripts. The review's central claim is that this silent rDNA heterochromatin protects repeat stability inside and outside the nucleolus, and seeds heterochromatin across the rest of the genome. Together with the nuclear lamina, the nucleolus forms "the hub for the organization of the inactive heterochromatin". The authors name the main gap as the lack of a genome-wide, single-cell method to map **nucleolus-associated domains (NADs)** the way DamID maps LADs.

## Key claims

- **rDNA copy number and location.** Humans and mice carry "~200 rRNA genes per haploid genome". In humans and apes they lie between the short arm and satellite body of acrocentric chromosomes 13, 14, 15, 21 and 22; laboratory mice carry them near the centromeres of chromosomes 12, 15, 16, 18 and 19. Human NORs range "from 50 kb to >6 Mb". rRNA is about 80% of total RNA in yeast and proliferating mammalian cells, and Pol I density reaches about one polymerase per 123–139 nt on active genes.
- **Three classes, defined by chromatin.** Silent genes carry promoter CpG methylation, H3K9me2/H3K9me3 and deacetylated histones, replicate in mid-late S phase and are inherited through division. Methylation of CpG −133 in the mouse promoter blocks UBF binding and pre-initiation complex formation. Inactive genes lack promoter methylation, so their state "can be potentially reversed": depleting UBF converts active genes to inactive through histone H1-dependent compaction, and restoring UBF reverses it. NuRD and eNoSC establish a poised or repressive state without DNA methylation, so in mammals **NoRC is the only complex so far shown to establish silent rRNA genes**.
- **Where each class sits is unresolved in mammals.** Both active and silent NORs lie within nucleoli, and NOR activity states are inherited across generations in human cell lines. That silent copies cluster at silent NORs is "still based on correlations"; direct visualisation is lacking. In *Arabidopsis* Col-0, all silent genes map to the NOR on chromosome 2 and all active ones to chromosome 4, and silent copies are excluded from purified nucleoli.
- **Sequence variants also matter.** In mouse, a C/A polymorphism at −104 changes CpG −133 methylation in a maternal protein-restriction model, and NIH3T3 cells methylate about 70% of rDNA-T and 50% of rDNA-G variants but no rDNA-A copies, a pattern not seen in other cell lines or tissues. Enhancer-repeat number varies (6–22), and spacer-promoter transcription comes from genes with 9 or 6 repeats.
- **Silencing is established at exit from pluripotency.** All rRNA gene promoters are unmethylated in mouse ESCs, under both 2i and serum/LIF. Methylation and H3K9me2/3 appear "shortly after ESC differentiation". In ESCs, IGS-rRNA processing into mature pRNA (by the helicase DHX9) is "strongly downregulated". Unprocessed IGS-rRNA binds TIP5 and blocks its interaction with TTF1, so TIP5 is not recruited. **Introducing pRNA into ESCs was sufficient to recruit TIP5 and start rRNA gene silencing.**
- **pRNA mechanism: stem-loop plus TTF1, not triple helix.** pRNA (about −220 to −1 relative to the TSS) folds into a conserved stem-loop that binds the TIP5 TAM domain. The authors question the widely cited **triple-helix recruitment model**: experiments testing whether pRNA triplex-forming sequences were needed to recruit TIP5 "failed to demonstrate" it, and the model ignored TTF1. They favour pRNA-dependent TIP5–TTF1 association.
- **Maintenance through replication.** Silent copies replicate in mid-late S phase, and TIP5 binds them immediately after replication. IGS-rRNA is made from active genes in early S phase, which suggests pRNA acts *in trans* to re-silence late-replicating copies. MOF acetylates TIP5-K633, which impairs pRNA binding; SIRT1 removes it; K633 acetylation rises before silent-copy replication. NoRC slides the promoter nucleosome from −157 to −132, exposing CpG −133 to DNMTs, and recruits SIN3/HDAC1 (via a bromodomain reading H4K16ac), SETDB1 and PARP1 (via pRNA).
- **Copy number does not set output.** Two yeast strains with 143 and 42 rRNA copies made the same amount of rRNA; the low-copy strain loaded twice as much Pol I per gene. The fraction of nucleosome-packed copies did not change under high metabolic activity. The authors therefore argue that silent copies serve a function other than dosage.
- **Silent rDNA safeguards repeats genome-wide.** In yeast, losing untranscribed copies sensitises cells to mutagens via reduced condensin and cohesion. In human cells, inactivating DNMT1/DNMT3b or using methylation inhibitors induces extrachromosomal circular rDNA. In *Drosophila*, loss of H3K9 methylation or RNAi factors disorganises nucleoli and increases rDNA circles. In differentiated mammalian cells, TIP5 depletion causes loss of rRNA genes **and** instability of centromeric repeats.
- **NADs and LADs overlap.** Early nucleolus-purification studies in HeLa, IMR90 and HT1080 found NADs to be gene-poor, lowly transcribed and enriched for H4K20me3, H3K27me3 and H3K9me3, including centromeric, pericentromeric and subtelomeric repeats. "NADs cover around 40% of the genome", with substantial overlap with LADs. In *A. thaliana*, NADs cover about 4.2% of the annotated genome. Reanalysis of IMR90 Hi-C found that **74% of NADs lie in B2/B3-type constitutive heterochromatin**. In LCL and K562 Hi-C, rDNA contacts are enriched in closed, repressed, late-replicating chromatin and CTCF sites, and developmentally regulated *Hox* genes are rarely near rDNA.
- **SPRITE separates NADs from LADs.** SPRITE showed that regions linearly close to centromeres sit near the nucleolus, that active regions are excluded even when centromere-proximal, and that nucleolar hubs are **inter-chromosomal** whereas lamina contacts usually join regions linearly close on the same chromosome. LADs can relocate to daughter-cell nucleoli after mitosis, and NADs to the nuclear envelope, so the two compartments may be "interchangeable scaffolds".
- **rDNA chromatin shapes genome organization in disease and development.** In the Eμ-Myc lymphoma model, UBF converts a fraction of inactive (not silent, methylated) genes to active during progression to malignancy. This changes rDNA–NAD contacts, some of which need active rDNA chromatin but not transcription. In ESCs, adding mature pRNA heterochromatinised the nucleolus and produced condensed heterochromatin blocks *outside* it, more H3K9me2, higher differentiation-gene expression and loss of pluripotency (no teratomas). Blocking rDNA heterochromatin formation during differentiation "abolishes the exit from pluripotency". In *Drosophila*, deleting Y-chromosome rDNA reduces heterochromatin elsewhere and changes expression of hundreds to thousands of genes.

## Methods / evidence

A narrative review of 138 references. Most mechanistic evidence comes from mouse ESCs, NIH3T3 and other cell lines, yeast, *Drosophila* and *Arabidopsis*, much of it from the authors' own lab (NoRC, pRNA, DHX9, PARP1). Genome-wide organization claims rest on biochemical nucleolus purification, Hi-C reanalysis, 4C-seq and SPRITE. There is no new data and no systematic search. Two figures (rRNA gene classes; ESC-to-differentiated chromatin model) summarise the authors' framework.

Weight: authoritative on NoRC/pRNA mechanism, where the authors are primary investigators, and openly self-critical about gaps (mammalian silent-copy localisation, triple-helix model). The broader claim that rDNA heterochromatin drives genome-wide heterochromatinisation rests mainly on one gain-of-function experiment (pRNA in ESCs), on TIP5 knockdown in NIH3T3 and on *Drosophila* Y-rDNA deletions. It is a plausible model, not established human biology. (synthesis)

## Limitations

**Authors' own:**
- Direct evidence that silent rRNA genes reside at silent NORs in mammals is lacking "due to technical limitations to visualize silent copies within a single NOR"; whether silent genes occupy specific nucleolar space in mammals "remains still elusive".
- The mechanisms linking rDNA chromatin state to genome architecture "remain yet elusive".
- The major limitation for the field is the difficulty of mapping NADs genome-wide as is done for LADs: the nucleolus is membraneless, which limits DamID, and high-resolution, single-cell methods for nucleolar contacts are still needed.
- Changes in rDNA methylation have only been reported between pluripotent and differentiated cells or cancer and normal cells; there is no evidence that rRNA transcription responses depend on the number of silent copies.

**Reviewer notes:**
- The review predates genome-wide single-cell nucleolar mapping and complete telomere-to-telomere assemblies of acrocentric short arms; rDNA arrays were absent from the reference genomes behind the Hi-C, 4C-seq and NAD studies it cites, so all rDNA-contact maps here depend on off-reference handling. (synthesis)
- Human evidence is thin: most mechanistic steps (pRNA, TIP5-K633, CpG −133, enhancer repeats) are mouse-specific coordinates, and their conservation in human rDNA is not discussed. (synthesis)
- Biochemical NAD purification (sonication of nuclei with intact nucleoli) is a population assay that cannot distinguish stochastic from fixed nucleolar association, which matters given that LADs relocate to nucleoli after mitosis. (synthesis)

## Surprising or load-bearing bits

- **pRNA alone can push ESCs out of pluripotency** by heterochromatinising rDNA, with condensed heterochromatin then appearing elsewhere in the genome. The nucleolus is cast as a heterochromatin nucleation site, not a bystander.
- **The authors dismiss their field's own textbook model**: pRNA–DNA triple-helix recruitment of TIP5 is "often reported in many reviews" but has never been shown to be required.
- **Silent rDNA is a genome-stability element**: losing it destabilises centromeric repeats too, not just rDNA.
- **NAD vs LAD geometry differs**: nucleolar hubs are inter-chromosomal, lamina contacts largely intra-chromosomal and linearly local. This is a testable signature for single-cell 3D-genome data. (synthesis)

## Entities mentioned

- None with existing entity pages. Raffaella Santoro (University of Zurich) is the corresponding author and primary investigator of much of the NoRC/pRNA work reviewed.

## Concepts touched

- [[lamina-associated-domains]] — NADs overlap LADs substantially; the two can trade positions after mitosis.
- [[nuclear-lamina]] — the second heterochromatin hub; DamID mapping shows ~35% of the mammalian genome can contact the lamina in any tested cell type.
- [[chromatin-phase-separation]] — the nucleolus is a membraneless, multilayered liquid compartment seeded by pre-rRNA.
- [[damid]] — named as the model technology that cannot easily be applied to the membraneless nucleolus.
- [[sc-sprite]] — bulk SPRITE is the cited evidence for inter-chromosomal nucleolar hubs.
- [[single-cell-hi-c]] — single-cell analysis is cited as the needed next step for nucleolar contacts.
- [[epigenetic-memory]] — silent rDNA state is re-established after each replication by TIP5 and pRNA acting in trans.

## Connections to other sources

- Echoes [[10-Summaries/van-steensel-2017-lads-review]], which frames the lamina, nucleoli and pericentromeric heterochromatin as competing repeat-rich repressive compartments.
- Complements [[10-Summaries/peric-hupkes-2010-lad-differentiation]]: both describe large-scale heterochromatin reorganisation at ESC differentiation, from the lamina and nucleolar sides.
- Relates to [[10-Summaries/qi-zhang-2021-nucleoli-coalescence]], which models why multiple nucleoli persist (chromatin network viscoelasticity); this review supplies the biology of how nucleolar heterochromatin is built. (synthesis)
- Single-cell 3D-genome methods that could address the NAD-mapping gap: [[10-Summaries/arrastia-2022-scsprite]], [[10-Summaries/tan-2018-science]], [[10-Summaries/nagano-2013-nature]], [[10-Summaries/lee-2019-natmethods]] and [[10-Summaries/jiang-2026-stark-scnucleome]]. (synthesis)
- [[10-Summaries/de-luca-2021-scdamid-protocol]] — the LAD mapping technology the authors hold up as the benchmark NAD mapping lacks.

## Open questions

- Is the active/silent status of individual NORs fixed per cell lineage in humans, and could single-cell long-read methylation calling now resolve it at single-NOR level? (synthesis)
- Does rDNA heterochromatin causally seed genome-wide heterochromatin in human differentiation, or only in mouse ESCs?
- Are NAD associations deterministic or stochastic per cell, given that LADs relocate to nucleoli after mitosis?

## Related

- [[40-Topics/3d-genome]]
- [[30-Concepts/lamina-associated-domains]]
- [[10-Summaries/van-steensel-2017-lads-review]]
- [[10-Summaries/qi-zhang-2021-nucleoli-coalescence]]
- [[10-Summaries/jiang-2026-stark-scnucleome]]
- [[10-Summaries/lee-2019-natmethods]]
