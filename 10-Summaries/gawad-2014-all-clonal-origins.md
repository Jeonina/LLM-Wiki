---
type: summary
title: "Gawad, Koh & Quake 2014 — Dissecting the clonal origins of childhood acute lymphoblastic leukemia by single-cell genomics"
source: "[[00-Sources/papers/Dissecting the clonal origins of childhood acute lymphoblastic leukemia by single-cell genomics]]"
source_kind: paper
author: "Charles Gawad, Winston Koh, Stephen R. Quake (corresponding)"
published: 2014-11-04
ingested: 2026-08-13
doi: "10.1073/pnas.1420822111"
journal: "PNAS 111:17947–17952"
tags: [ALL, codominant-clones, targeted-single-cell-sequencing, APOBEC, allele-dropout, microfluidics, IgH, clonal-structure]
entities: ["[[charles-gawad]]", "[[stephen-quake]]"]
concepts: ["[[allele-dropout]]", "[[mda]]", "[[intratumor-heterogeneity]]", "[[phylogenetic-inference]]", "[[mutational-signatures]]", "[[jaccard-similarity]]"]
topics: ["[[cancer-clonal-evolution]]", "[[hematopoietic-malignancies]]", "[[scdna-cancer-applications]]"]
---

**Citation:** Gawad, Koh & Quake (2014) — *Dissecting the clonal origins of childhood acute lymphoblastic leukemia by single-cell genomics* — *PNAS* 111, 17947–17952. [DOI](https://doi.org/10.1073/pnas.1420822111)

# Gawad 2014 — ALL clonal origins

> The opposite design choice from [[wang-2014-nuc-seq|nuc-seq]]: give up genome breadth, buy **cell count**. Microfluidic MDA on **1,479 single ALL cells** from six patients, then targeted resequencing of only the loci that bulk exome said were heterogeneous. The payoff is statistical power over clone structure — and the finding that **five of six patients have codominant clones**, which bulk allele frequencies structurally cannot resolve.

## Key claims

- **Bulk allele frequency cannot resolve codominant clones, by construction.** Two clones at similar frequency produce mutations at similar VAF; nothing in the bulk data separates them. The paper demonstrates this directly — it shows the six samples cannot be resolved into clones from bulk VAF alone.
- **Five of six patients have ≥2 clones each comprising ≥25% of cells.** Codominance, not a single dominant clone with minor satellites, is the normal architecture of childhood ALL at diagnosis.
- **Two independent clone-inference routes agree.** (i) Expectation-maximisation on a multivariate Bernoulli model with clone number chosen by AIC; (ii) [[jaccard-similarity|Jaccard]]-distance clustering of cells and mutations with within-sum-of-squares. Consensus clone genotypes then feed a directed minimum spanning tree for temporal ordering. Where the two disagree, hierarchical clustering over-splits relative to what the probabilistic model supports.
- **ADO is measured four ways, not assumed.** TaqMan genotyping of 46 common-het loci, targeted resequencing of 96 common-het loci, wild-type-allele loss at called mutations, and (a fourth route) the EM model's own inferred intraclonal dropout rate. The first and third concur at 23–24% median; resequencing reads higher at 33%. After a 30% ADO filter the median drops to 20%. Primary samples run modestly above the 15.6% seen in an LCL control.
- **Detection limits are simulated, not hand-waved.** With >30 mutations interrogated, mutation count stops mattering; **200 cells detect a 1% clone, 75 cells a 2% clone, 50 cells a 4% clone** — roughly, you need 2–3 cells from a clone to call it. ADO >0.3 or <10 mutations/sample causes clone-number underestimation.
- **Structural variants precede point mutations.** 13 of 16 large deletions (mean 3.2 per *ETV6-RUNX1* patient, 25 kb to a whole X chromosome) are present in all clones at frequencies above the ADO rate — the deletion-generating process (likely aberrant RAG) had finished before the SNVs in later clones arose. One patient (chr16, patient 4) shows a subclonal deletion, so the process is not strictly switched off.
- **The SNVs are cytosine-biased with a TC motif, implicating APOBEC rather than AID.** No WRCY motif (AID's preference) was found; VH-segment mutations were few and uncorrelated with cytosine-mutation fraction, which argues against somatic hypermutation as the source.
- ***KRAS* mutations are late and insufficient for dominance.** In both patients carrying them, *KRAS* is restricted to a single most-evolved clone that nonetheless coexists with a codominant sibling — in patient 4 the sibling carries a *RAB27B* mutation that may confer matching fitness.
- **Clone-specific punctuated cytosine mutagenesis.** Three distinct C→G mutations in the *same exon* of *ZNF880*, all in a TCA motif, plus close-proximity *PRSS12* and *FAM178A* events — consistent with a processive enzyme acting focally in one clone.
- **Clones within a patient are arrested at different B-cell developmental stages.** IgH VDJ analysis shows variable VH-replacement magnitude between clones of the same patient, and clones enriched for cells with no detectable VDJ call — i.e. arrest before recombination. In patient 1, a subgroup of clone 1 uniquely using IGHV3-33*01 co-segregates with an *EYA4* 3′UTR mutation.

## Methods / evidence

Six near-normal-karyotype pediatric ALL patients (five *ETV6-RUNX1*⁺), chosen specifically to simplify variant calling and ADO interpretation. Paired tumour/normal exome (mean 46 confirmed variants per patient, range 10–105), then Fluidigm C1 capture + MDA of a median 245 cells each, then targeted resequencing of SNVs, deletion regions, and IgH. Simulation-based validation of both the clone-number estimator and the cell-number requirements.

Weight: the ADO quantification and the detection-limit simulations are unusually rigorous for 2014 and are the parts most worth reusing. The karyotype selection criterion means the results describe the *simplest* ALL genomes, not all of them.

## Surprising or load-bearing bits

- **The "2–3 cells per clone" rule is the reusable design number.** It converts a biological question ("can I see a 1% subclone?") into a sample-size calculation, and it still governs how single-cell clone-detection experiments are powered.
- **Codominance breaks the linear-succession model of leukemogenesis.** If the fittest clone always sweeps, you would not see two clones each holding a quarter of the tumour. Something is maintaining the balance — the *KRAS*/*RAB27B* pairing hints at parallel adaptive peaks.
- **Deletions-before-SNVs is a temporal ordering derived without a time course.** It comes purely from which clones share which lesions, which is exactly what bulk sequencing cannot deliver.
- **Differentiation-arrest heterogeneity is a treatment-resistance hypothesis hiding in an IgH assay.** Clones frozen at different B-cell stages will respond differently to therapy; measuring it required IgH sequences in the *same* cells as the mutations.
- **The design tradeoff is explicit and worth quoting**: the authors call it "a carefully calibrated balance in the trade-off between the amount of data obtained per cell versus the number of cells that can be practically analyzed." That axis — depth per cell vs cells per experiment — organises the whole scDNA field.

## Entities mentioned

- [[charles-gawad]] — first author; later cofounder of BioSkryb and coauthor on [[luquette-2021-scan2]] and [[gonzalez-pena-2021-pnas]].
- [[stephen-quake]] — corresponding author; microfluidic single-cell platforms.

## Concepts touched

- [[allele-dropout]] — the four-way measurement and the 30% filtering threshold; the most careful ADO treatment in the corpus for its era.
- [[intratumor-heterogeneity]] — codominance as the default architecture.
- [[phylogenetic-inference]] — EM/Bernoulli plus minimum spanning tree, predating the dedicated tools.
- [[mutational-signatures]] — TC-motif cytosine bias read as APOBEC.

## Connections to other sources

- Contemporary and complementary design: [[wang-2014-nuc-seq]] (few cells, whole genome) versus this (many cells, targeted loci).
- Ancestor of the droplet-scale targeted approach: [[pellegrino-2018-tapestri]] scales exactly this design to thousands of cells per run.
- Genotype-plus-phenotype successors: [[nam-2019-got]], [[izzo-2024-got-cha]] add transcriptome and accessibility to the same targeted-genotype trick.
- Formal phylogeny tools that later replaced the EM/MST approach: [[jahn-2016-scite]], [[zafar-2017-sifit]], [[satas-2020-scarlet]].
- Signature context: [[alexandrov-2013-mutational-signatures]] (APOBEC signatures in bulk cohorts).
- Blood clonal-architecture context: [[lee-six-2018-hsc-dynamics]], [[nam-2022-natgenet]].

## Open questions

- **What sustains codominance?** The paper observes it and speculates about matched fitness but cannot test it — that needs longitudinal or functional data.
- Restricting to near-normal karyotypes excludes the hyperdiploid and *MLL*-rearranged ALLs where clonal structure may differ most.
- The APOBEC attribution is motif-based only; no APOBEC expression or activity was measured.
- Whether differentiation-arrest heterogeneity predicts relapse is raised as an implication and left open.

## Related

- [[wang-2014-nuc-seq]] · [[pellegrino-2018-tapestri]] · [[allele-dropout]] · [[40-Topics/hematopoietic-malignancies]]
