---
type: summary
title: "Lupiáñez et al. 2015 — Disruptions of topological chromatin domains cause pathogenic rewiring of gene-enhancer interactions"
source: "[[00-Sources/papers/Disruptions of Topological Chromatin Domains Cause Pathogenic Rewiring of Gene-Enhancer Interactions]]"
source_kind: paper
author: "Darío G. Lupiáñez, Katerina Kraft, Verena Heinrich, Peter Krawitz, Francesco Brancati, Eva Klopocki, Denise Horn, Hülya Kayserili, John M. Opitz, Renata Laxova, Fernando Santos-Simarro, Brigitte Gilbert-Dussardier, Lars Wittler, Marina Borschiwer, Stefan A. Haas, Marco Osterwalder, Martin Franke, Bernd Timmermann, Jochen Hecht, Malte Spielmann, Axel Visel, Stefan Mundlos (corresponding)"
published: 2015-05-21
ingested: 2026-08-10
doi: "10.1016/j.cell.2015.04.004"
journal: "Cell"
tags: [TAD, CTCF, boundary-element, enhancer-hijacking, structural-variation, limb-malformation, CRISPR, 4C-seq, causal-demonstration]
entities: []
concepts: ["[[topologically-associating-domain]]", "[[structural-variants]]", "[[cis-regulatory-element]]", "[[enhancer-states]]", "[[single-cell-hi-c]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]"]
---

**Citation:** Lupiáñez et al. (2015) — *Disruptions of topological chromatin domains cause pathogenic rewiring of gene-enhancer interactions* — *Cell* 161, 1012–1025. [DOI](https://doi.org/10.1016/j.cell.2015.04.004)

# Lupiáñez 2015 — TAD boundaries are load-bearing

> The paper that turned TADs from a descriptive Hi-C feature into a **causal, clinically interpretable** unit. Three human limb-malformation rearrangements at the *WNT6/IHH/EPHA4/PAX3* locus were re-engineered in mice by CRISPR; each disrupts a TAD boundary, each lets an *EPHA4* limb-enhancer cluster capture a gene it should never contact, and each phenocopies the human disease. Leaving the boundary intact abolishes both the misexpression and the phenotype.

## Key claims

- Three distinct human alleles, three distinct phenotypes, one shared mechanism:
  - **Brachydactyly** (3 unrelated families): heterozygous 1.75–1.9 Mb deletions removing *EPHA4* and the *EPHA4*/*PAX3* boundary.
  - **F-syndrome** (severe syndactyly + polydactyly): a ~1.1 Mb inversion (family F1) and a ~1.4 Mb tandem duplication (family F2) — different mutations, same phenotype, both juxtaposing the *EPHA4* TAD with *WNT6*.
  - **Polysyndactyly** with craniofacial defects: ~900 kb duplication, mirroring the mouse *doublefoot* (*Dbf*) mutant's ~600 kb deletion; both bring *IHH* near the *EPHA4* TAD.
- CRISPR-engineered mice reproduce the human phenotypes: *DelB/DelB* mice show short second digits, hypoplastic middle phalanges, and 2–3 syndactyly, matching the human brachydactyly.
- RNA-seq on E11.5 limbs shows one specific gene upregulated per allele — *Pax3* in *DelB/+*, *Wnt6* in *InvF/InvF*, *Ihh* in *Dbf/+* — with neighbours essentially unchanged.
- In situ hybridization shows the misexpression domain **copies the endogenous *Epha4* pattern** in every case: the target gene has been adopted by *Epha4*'s enhancers.
- 4C-seq confirms de novo cross-boundary contacts in all three mutants, with a **minimal common region of ~150 kb** inside the *EPHA4* TAD; transgenic LacZ assays identify a cluster of three limb enhancers within a 30 kb window whose activity pattern overlaps *Epha4* and all three ectopic domains.
- **The boundary is the causal element, not distance.** *DelB^S* and *Dbf^S* mice carry near-identical deletions that spare the predicted boundary: normal limbs, no misexpression, reduced ectopic 4C contact. Deletion-size difference is only 12–17%, too small to explain reversion by distance alone.
- TAD structure is conserved enough across tissue and species that **patient adult fibroblasts** recapitulate the aberrant interactions that occurred during embryonic limb development — a diagnostic, not just a mechanistic, result.
- Disrupted TADs fuse seamlessly with neighbours rather than forming new internal boundaries; the fused domain is bounded by the *next* boundary, and ectopic contacts respect it (*Ihh*/*Wnt6* never reach *Pax3* and vice versa).

## Methods / evidence

Array CGH, whole-exome and whole-genome sequencing for the human alleles with breakpoint-spanning PCR + Sanger confirmation; CRISPR/Cas dual-sgRNA engineering of megabase deletions/inversions in mouse ESCs with tetraploid complementation; 4C-seq (BglII/HindIII) on microdissected E11.5 distal limbs and on human adult fibroblasts; RNA-seq; transgenic Hsp68-LacZ enhancer reporters; whole-mount in situ. Two independent ESC clones per rearrangement.

This is the rare 3D-genome paper with a genuine causal design: **the boundary-sparing control alleles are the experiment.** Everything else in the TAD literature that asserts boundary function tends to lean on this result.

Limits the authors state: only one locus; the minimal boundary element is undefined (they deleted large regions containing CTCF clusters, not the sites themselves); many genes fall inside the ectopic contact region yet stay silent, so contact is necessary but not sufficient — promoter receptiveness matters.

## Surprising or load-bearing bits

- **Convergent phenotypes from opposite mutation classes.** A deletion and a duplication (polydactyly), or an inversion and a duplication (F-syndrome), produce near-identical molecular and morphological outcomes. Deletions *remove* a boundary; inversions and duplications *reposition* an intact boundary so it no longer separates enhancer from target. This decouples "pathogenic" from "copy-number-changing" and is the single most important message for interpreting balanced SV — exactly the class [[eichler-2007-completing-sv-map|the 2007 SV proposal]] said arrays could not see.
- Only a subset of genes inside the new contact domain respond, and the responders are all limb developmental genes. The authors invoke *Drosophila* housekeeping-vs-developmental promoter classes and suggest poised genes are preferentially capturable — which links enhancer hijacking to the [[bernstein-2006-bivalent-chromatin|bivalent/poised]] promoter state.
- The patient-fibroblast result means TAD topology is a **retrospective assay for developmental regulatory events** in tissue you can never sample.
- Absence of CTCF sites *within* the *EPHA4* TAD and clusters at each boundary is the structural correlate of the functional result.

## Concepts touched

- [[topologically-associating-domain]] — this page's causal evidence lives here; TADs are functional insulating units, not just contact-map texture.
- [[structural-variants]] — supplies the interpretive framework: SV pathogenicity depends on position relative to boundaries, and boundary-sparing variants of the same size can be benign.
- [[cis-regulatory-element]] / [[enhancer-states]] — enhancer hijacking; contact necessary, promoter receptiveness also required.

## Connections to other sources

- Builds directly on [[dixon-2012-tads|Dixon 2012 (TAD discovery)]] (TAD discovery) and the Hi-C substrate from [[lieberman-aiden-2009-hic|Lieberman-Aiden 2009 (Hi-C)]]; loop/domain annotation tooling in [[durand-2016-juicer]].
- [[spielmann-2018-sv-3d-genome]] is the review that generalizes this locus into a framework.
- [[naumova-2013-mitotic-chromosome]] shows TADs vanish in metaphase — so the boundary function demonstrated here is an interphase property that must be re-established each cycle.
- Single-cell relevance: [[nagano-2013-nature]], [[tan-2018-science|Dip-C]] and [[lee-2019-natmethods|sn-m3C-seq]] ask whether these boundaries hold in individual cells — this paper's population-level causality does not settle per-cell penetrance.

## Open questions

- **Is boundary insulation all-or-none per cell, or probabilistic across a population?** Bulk 4C cannot distinguish "every cell leaks a little" from "10% of cells leak a lot." Single-cell Hi-C is the tool and the answer is not in this corpus.
- The minimal functional boundary element remains undefined here — deleting only the CTCF sites was explicitly left to future work.
- Whether *somatic* SV in tumors hijacks enhancers by this mechanism at appreciable frequency is a natural extension this wiki has no source for; relevant to [[cancer-clonal-evolution]].

## Related

- [[topologically-associating-domain]] · [[spielmann-2018-sv-3d-genome]] · [[naumova-2013-mitotic-chromosome]] · [[3d-genome]]
