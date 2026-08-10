---
type: summary
title: "Bernstein et al. 2006 — A bivalent chromatin structure marks key developmental genes in embryonic stem cells"
source: "[[00-Sources/papers/A Bivalent Chromatin Structure Marks Key Developmental Genes in Embryonic Stem Cells]]"
source_kind: paper
author: "Bradley E. Bernstein, Tarjei S. Mikkelsen, Xiaohui Xie, Michael Kamal, Dana J. Huebert, James Cuff, Ben Fry, Alex Meissner, Marius Wernig, Kathrin Plath, Rudolf Jaenisch, Alexandre Wagschal, Robert Feil, Stuart L. Schreiber, Eric S. Lander (corresponding)"
published: 2006-04-21
ingested: 2026-08-10
doi: "10.1016/j.cell.2006.02.041"
journal: "Cell"
tags: [bivalent-domains, H3K4me3, H3K27me3, embryonic-stem-cells, Polycomb, poised-genes, founding-paper, CpG-island]
entities: ["[[alexander-meissner]]", "[[rudolf-jaenisch]]"]
concepts: ["[[enhancer-states]]", "[[epigenetic-memory]]", "[[cpg-island]]", "[[transposable-elements]]", "[[chip-seq]]"]
topics: ["[[histone-modifications]]", "[[chromatin-architecture]]"]
---

**Citation:** Bernstein et al. (2006) — *A bivalent chromatin structure marks key developmental genes in embryonic stem cells* — *Cell* 125, 315–326. [DOI](https://doi.org/10.1016/j.cell.2006.02.041)

# Bernstein 2006 — bivalent domains

> ES cells carry large H3K27me3 domains that contain smaller H3K4me3 sites within them — "bivalent domains" — overwhelmingly at developmental transcription-factor genes. The genes are silent but poised: on differentiation the domains resolve to one mark or the other according to whether the gene is induced. Before this paper the two marks were believed non-overlapping.

## Key claims

- Across 61 tiled regions (60.3 Mb, ~2.5% of the genome; Hox clusters + 52 HCNE-rich + 5 controls): 343 H3K4me3 sites (median 3.4 kb, 63% at TSSs) and 192 H3K27me3 sites, the latter far larger (median 5 kb in controls, 10 kb in HCNE-rich, 18 kb in Hox).
- **Three-quarters of K27 domains contain a K4 site.** 109 bivalent domains total.
- Bivalency is developmental-TF-specific: of 69 HCNE-region bivalent domains overlapping known TSSs, **93% are at TF-encoding genes** (Sox, Fox, Pax, Irx, Pou families) although TFs are only half the genes in the regions.
- Bivalency is ES-cell-specific: 6/1/13/12 bivalent domains in MEFs, MLFs, myoblasts, neuroblastoma respectively; 93 of 97 formerly-bivalent TSSs carry a single large monovalent mark in at least one differentiated type (median 19.4 kb K27, 7.4 kb K4).
- Both marks are on the **same physical chromatin**, not two subpopulations: sequential ChIP (K27 then K4, and the reverse) enriches Irx2 >30-fold over controls.
- Repression is epistatic to activation: bivalent genes show expression distributions like K27-only genes, not K4-only genes.
- Directed differentiation to neural precursors resolves domains predictively — Nkx2.2/Sox21/Zfpm2 (induced) → K4 only; Pax5/Lbx1h/Evx1 (not induced) → K27 only; weakly induced Dlx1 stays bivalent with stronger K4.
- Sequence predicts the marks: K4 tracks **CpG density** (95% of K4 TSSs have CpG islands, 91% converse, r_phi = 0.73), K27 tracks **transposon exclusion zones** (median 6% transposon-derived vs 22% expected; 89% of TEZ-containing TSSs have a K27 domain, r_phi = 0.69). TEZs are conserved — depleted of lineage-specific repeats in human (1.3% vs 15.2%) and dog (1.0% vs 9.1%). A genome-wide scan found 710 TEZs, 328 at TSSs, overwhelmingly developmental TFs and signaling genes.
- ~50% of bivalent domains overlap Oct4/Nanog (less so Sox2) binding sites (p < 10⁻⁹), and pluripotency-factor targets that are *also* bivalent tend to be silenced.

## Methods / evidence

ChIP on custom Affymetrix tiling arrays (~1.3M probe pairs, ~30 bp spacing) with duplicate experiments and a Wilcoxon rank-sum enrichment call. Replicated in an independent ES line (ES2, different genotype) using a completely different protocol — **MNase-digested, non-crosslinked** nucleosome ChIP with different antisera — recovering 94 of 95 bivalent domains. That orthogonal-protocol replication plus the sequential ChIP is what makes the result durable; the obvious artifact explanations (crosslinking, sonication, cell-population mixture) are each closed off directly.

Scope limit worth keeping: this is 2.5% of the genome on arrays, pre-ChIP-seq. Genome-wide confirmation came from Mikkelsen 2007.

## Surprising or load-bearing bits

- The sequence-determinism finding is underrated: **the ES-cell epigenetic ground state is largely readable from DNA sequence** (CpG islands → K4; transposon-exclusion zones → K27), and the correlation *weakens* in differentiated cells. Epigenetic state starts as a function of sequence and drifts away from it with lineage commitment. That is a direct, testable claim about what a single-cell epigenome measurement is measuring.
- TEZs as a conserved, selection-maintained feature reframes transposon depletion as *causal for* rather than *incidental to* Polycomb domains — the authors argue repeats would be silenced and thereby interfere, so selection removes them.
- The "poised" concept originating here propagates through the whole enhancer-state vocabulary, including [[creyghton-2010-h3k27ac-enhancers|Creyghton's]] poised-enhancer definition four years later.
- The sequential-ChIP design is the direct ancestor of the question single-cell multi-factor methods exist to answer — whether two marks co-occur on one molecule/one cell. [[scchix-seq]], [[multi-tag]] and [[gopalan-2022-multi-cut-and-tag|Multi-CUT&Tag]] are bulk-sequential-ChIP's single-cell successors, and bivalency is their canonical test case.

## Entities mentioned

- [[alexander-meissner]] — co-author; the ES-cell epigenomics program continues from here.
- [[rudolf-jaenisch]] — ES cell source and co-author.
- Bradley Bernstein / Eric Lander (Broad) — the group whose tiling-array chromatin mapping became the Roadmap Epigenomics infrastructure ([[roadmap-2015-111-epigenomes]]).

## Concepts touched

- [[enhancer-states]] — supplies the poised/bivalent state at promoters (Creyghton supplies it at enhancers).
- [[epigenetic-memory]] — the large monovalent domains in differentiated cells are proposed as the memory substrate, sized so each daughter chromatid inherits enough modified histones to re-template.
- [[cpg-island]] — the K4/CpG-island coupling (r_phi = 0.73) is quantified here.
- [[transposable-elements]] — transposon exclusion zones.

## Connections to other sources

- Foundational for [[andrew-2011-cellresearch|Bannister & Kouzarides]]'s and [[rothbart-2014-histone-dna-language|Rothbart & Strahl]]'s treatment of combinatorial marks.
- Complementary to [[creyghton-2010-h3k27ac-enhancers]]: bivalency at promoters, H3K27ac at enhancers, both 2006–2010, both about "poised."
- The bulk chromatin-state framework this seeded is scaled to 111 tissues in [[roadmap-2015-111-epigenomes]].
- Single-cell tests of bivalency: [[wu-2021-sccut-tag]], [[yeung-2023-scchix-seq]], [[gopalan-2022-multi-cut-and-tag]].

## Open questions

- Whether bivalency is genuinely per-cell or partly a population average was closed for *chromatin fibers* by sequential ChIP but not for *cells* — and the single-cell CUT&Tag literature still reports conflicting answers on how many cells carry both marks at a given locus. This is an open contradiction in the corpus, tracked at [[open-questions]].
- Only 2.5% of the genome was surveyed; the genome-wide claim rests on later work not currently bookmarked (Mikkelsen 2007).

## Related

- [[creyghton-2010-h3k27ac-enhancers]] · [[enhancer-states]] · [[histone-modifications]] · [[roadmap-2015-111-epigenomes]]
