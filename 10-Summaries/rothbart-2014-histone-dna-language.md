---
type: summary
title: "Rothbart & Strahl 2014 — Interpreting the language of histone and DNA modifications"
source: "[[00-Sources/papers/Interpreting the language of histone and DNA modifications]]"
source_kind: paper
author: "Scott B. Rothbart, Brian D. Strahl (corresponding)"
published: 2014
ingested: 2026-08-10
doi: "10.1016/j.bbagrm.2014.03.001"
journal: "Biochimica et Biophysica Acta — Gene Regulatory Mechanisms"
tags: [histone-code, PTM, readers-writers-erasers, multivalency, asymmetry, DNA-methylation-readers, 5hmC-readers, review]
entities: ["[[uhrf1]]"]
concepts: ["[[uhrf1]]", "[[dnmt]]", "[[5hmc]]", "[[tet-enzymes]]", "[[cpg-island]]", "[[epigenetic-memory]]", "[[maintenance-asymmetry]]"]
topics: ["[[histone-modifications]]", "[[dna-methylation]]"]
---

**Citation:** Rothbart & Strahl (2014) — *Interpreting the language of histone and DNA modifications* — *BBA Gene Regulatory Mechanisms* 1839, 627–643. [DOI](https://doi.org/10.1016/j.bbagrm.2014.03.001)

# Rothbart & Strahl 2014 — one language, two alphabets

> Strahl — co-author of the original 2000 "histone code" hypothesis — revisits it and argues it was too simple in three specific ways: PTMs occur far beyond the tails, they can be **asymmetric within a single nucleosome**, and they are read jointly with **DNA modifications** by multivalent effectors. The correct unit of analysis is not a mark but a nucleosome-plus-DNA signature.

## Key claims

**Histone side**
- PTMs at the **histone–DNA interface** (H3K56ac, H3K122ac, H3K155ac, H3T118ph) act physically — weakening histone–DNA contacts, increasing nucleosome mobility, promoting DNA unwrapping — a mechanistically different class from tail marks. H3K122ac is a p300/CBP substrate enriched at promoters and required for activation.
- Interface marks can *also* control effectors: JAK2-mediated H3Y41ph blocks HP1α chromoshadow binding.
- The PTM dictionary keeps expanding: crotonylation, butyrylation, propionylation, succinylation, malonylation (all CoA-derived, hence **metabolically coupled**), 5-hydroxylation, N-formylation, O-GlcNAcylation. O-GlcNAc is cell-cycle-regulated (peak G₁), occurs at H3S10 where it may antagonize H3S10ph, and crosstalks with H2BK120ub.
- MS of H3₁–₅₀ and H4₁–₂₃ finds **>200 distinct modified N-terminal forms each**, with up to 7 PTMs on a single H3 N-terminal fragment.
- **Asymmetry is real and it rewrites bivalency.** H3K4me3 and H3K27me3 do *not* co-occur on the same H3 tail; they sit on adjacent histones within one nucleosome, consistent with PRC2's inability to methylate H3K27 when H3K4me3 is present in *cis*.
- Multivalency: readers engage in *cis* (UHRF1 TTD+PHD reading H3K9me3 and the H3 N-terminus together) and in *trans* (BPTF PHD reading H3K4me3 while its bromodomain reads H4K16ac across tails in one nucleosome). Disrupting either domain breaks the interaction — single-domain characterization is insufficient.
- Effector binding can **induce secondary structure** in nominally disordered histone tails (α-helix in H3₁–₁₁ bound by UHRF1 TTD-PHD, and by MOZ double-PHD).

**DNA side**
- ~80% of genomic CpGs are methylated, ~1% of all nucleotides.
- 5mC readers now span three families: MBDs (MeCP2 first; Rett-syndrome mutations map to it), zinc fingers (Kaiso — which reads *both* symmetric 5mC and a specific 5 bp *unmethylated* Wnt-target motif), and SRA domains (UHRF1, which reads **hemi-methylated** CpG by base-flipping — the first non-enzymatic sequence-specific DNA-binding domain shown to flip bases).
- **The silencing dogma is broken**: KLF2/KLF4/KLF5 bind specific sequences *methylation-dependently*, and 5mC recognition stimulates KLF4-mediated transcription. A methylated motif can be a *new* activator binding site, unpredictable from sequence alone.
- Oxidized derivatives have their own readers: UHRF2 reads 5hmC and 5caC but not 5mC or 5fC; MBD3 (which cannot read 5mC) reads 5hmC and localizes to hydroxymethylated promoters TET1-dependently; MeCP2 reads 5hmC, and a Rett mutation disrupts 5hmC but not 5mC binding.
- Unmodified CpGs are read too: CxxC proteins. CFP1 (SETD1 complex) binds non-methylated CpGs, and inserting an artificial CpG island into a promoter-free region **establishes a new H3K4me3 domain**.
- Crosstalk is bidirectional and mechanistic: DNMT3A/B/L ADD domains bind unmodified H3 N-termini and are blocked by H3K4me2/3; DNMT3A's PWWP reads H3K36me3 (gene-body methylation); UHRF1's RING ubiquitinates H3K23, and **DNMT1 reads H3K23ub via its RFTS domain** — a histone mark directly driving maintenance methylation.
- KDM2A's CxxC domain reading unmethylated CpG explains why CpG-island promoters lack H3K36me2.
- Developmental asymmetry explained: maternal PGC7 reads H3K9me2 and shields maternal 5mC from TET3; sperm chromatin is protamine-packaged, so PGC7 cannot be recruited and paternal demethylation proceeds actively.

## Methods / evidence

Review. Its strength is that it consistently distinguishes structurally-demonstrated interactions from inferred ones and flags assumptions — e.g. it explicitly notes that the asymmetry conclusions depend on the PTM antibody not enriching unmodified nucleosomes, a "key assumption for accurate interpretation."

## Surprising or load-bearing bits

- **The bivalency correction is the single most consequential item for this wiki.** [[bernstein-2006-bivalent-chromatin|Bernstein 2006]] established bivalent domains by sequential ChIP; this review reports that the two marks are on *adjacent histones in one nucleosome*, not the same tail. That is a finer-grained answer than sequential ChIP could give, and it sets the resolution bar for any single-cell multi-mark method ([[scchix-seq]], [[multi-tag]], [[gopalan-2022-multi-cut-and-tag]]): co-occurrence must be resolved at the *nucleosome-face* level, not the locus level.
- **Methylation-dependent activation** (KLF4) breaks the assumption underlying most methylation-to-expression inference in single-cell methylome analysis. Tools that score promoter methylation as repression ([[angermueller-2017-genomebiol|DeepCpG]], [[kapourani-2019-melissa|Melissa]], [[kremer-2024-methscan|MethSCAn]] downstream interpretation) inherit a directional prior this review says is wrong at some loci.
- Metabolic coupling of the acyl-CoA marks means chromatin state is partly a readout of **nutrient flux** — a confounder for anything comparing epigenomes across tissues or disease states with different metabolism.
- The H3K23ub → DNMT1 axis is a concrete mechanism for how histone state instructs DNA methylation maintenance, which is what [[maintenance-asymmetry]] and the epimutation-clock methods ([[chen-2025-methyltree|MethylTree]], EPI-Clone) implicitly depend on being noisy.
- Sequence context matters for CpG readers — most newly identified methyl-CpG-binding TFs bind sequence-dependently, and MBD proteins have differing sequence preferences, "a property to consider when using these domains as methylated CpG affinity enrichment tools." That is a direct methodological warning for MBD-based enrichment protocols.

## Concepts touched

- [[uhrf1]] — this review is the best single source for UHRF1's multi-domain logic (TTD, PHD, SRA base-flipping, RING/H3K23ub).
- [[dnmt]] — ADD/PWWP targeting rules and DNMT1 autoinhibition by RFTS and the CxxC acidic loop.
- [[5hmc]] / [[tet-enzymes]] — reader repertoire for oxidized cytosines; supports demethylation-independent function.
- [[cpg-island]] — CFP1/CxxC and the artificial-CpG-island experiment.
- [[epigenetic-memory]] — the marks-instruct-marks circuitry that would have to carry memory through the structure-less mitosis of [[naumova-2013-mitotic-chromosome]].

## Connections to other sources

- Refines [[bernstein-2006-bivalent-chromatin]] (bivalency is inter-histone, not intra-tail) and complements [[andrew-2011-cellresearch|Bannister & Kouzarides 2011]].
- Downstream of [[tahiliani-2009-tet1-5hmc]]; provides the reader-side of the 5hmC story Tahiliani opened.
- Method wishlist section (locus-specific PTM landscapes via ChAP-MS/TALE targeting; MNase-ChIP-seq + MS) prefigures [[kaya-okur-2019-cut-and-tag|CUT&Tag]] and the single-cell histone methods.

## Open questions

- Whether asymmetric nucleosomes are detectable by any current single-cell method — none in this corpus operate at nucleosome-face resolution. Flagged to [[open-questions]] and relevant to [[mnase-vs-tn5-chromatin]].
- Which loci show methylation-dependent *activation* genome-wide, and whether single-cell methylome interpretations need locus-specific priors rather than a global repression assumption.
- C-terminal and globular-domain PTMs, and histone-variant PTMs, remain largely uncharted — the review says so directly.

## Related

- [[bernstein-2006-bivalent-chromatin]] · [[uhrf1]] · [[histone-modifications]] · [[tahiliani-2009-tet1-5hmc]]
