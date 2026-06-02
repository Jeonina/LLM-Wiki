---
type: summary
title: "Wang, He & Hu 2026 — Computational approaches for multimodal lineage tracing"
source: "[[00-Sources/papers/Computational approaches for multimodal lineage tracing - Nature Reviews Genetics]]"
source_kind: paper
author: "Kun Wang, Xionglei He, Zheng Hu (corresponding)"
published: 2026-05-18
ingested: 2026-06-02
doi: "10.1038/s41576-026-00969-9"
journal: "Nature Reviews Genetics"
tags: [lineage-tracing, review, phylogenetic-inference, fate-mapping, RNA-velocity, ancestral-state-reconstruction, deep-learning, computational]
entities:
  - "[[20-Entities/zheng-hu]]"
concepts:
  - "[[30-Concepts/phylogenetic-inference]]"
  - "[[30-Concepts/crispr-lineage-recording]]"
  - "[[30-Concepts/lineage-tracing]]"
  - "[[30-Concepts/chromatin-velocity]]"
concepts_secondary:
  - "[[30-Concepts/lineage-tracing-somatic-mutations]]"
  - "[[30-Concepts/mitochondrial-lineage-tracing]]"
topics:
  - "[[40-Topics/single-cell-lineage-tracing]]"
---

**Citation:** Wang, He & Hu (2026) — *Computational approaches for multimodal lineage tracing* — *Nature Reviews Genetics*. [DOI](https://doi.org/10.1038/s41576-026-00969-9)

# Wang, He & Hu 2026 — Computational multimodal lineage tracing

> Thesis: The companion-piece to the technology review — a survey of the *algorithms* that turn lineage-resolved single-cell multi-omic data into biology. It frames four core computational challenges (large-scale phylogenetic inference, disparate multimodality, unobserved ancestral states, noise/dropout) and organizes the methods that address them: phylogenetic reconstruction, quantitative fate mapping, ancestral-state reconstruction, and lineage–transcriptome integrative learning.

## Key claims

- **Four challenges**: (1) tree inference is NP-hard and tree count grows super-exponentially with cell number; (2) lineage data are discrete/low-dim/tree-structured while molecular data are continuous/high-dim/manifold — a structural, temporal, and statistical mismatch; (3) only leaf (present-day) states are observed, ancestral internal-node states are unseen; (4) pervasive allelic/barcode dropout and noise propagate into every downstream step.
- **Phylogenetic reconstruction** splits by marker type. Natural somatic variants: SNV callers (SCIΦ, SIEVE, CellPhy, ScisTree), CNV methods (SCICoNE, MEDICC2), joint SNV+CNV (SCARLET, COMPASS), methylation (MethylTree). Synthetic CRISPR barcodes: classic distance (neighbour-joining, UPGMA) and character (max-parsimony, max-likelihood) methods, plus CRISPR-aware models — **Cassiopeia** (parsimony via greedy/ILP, enforces edit irreversibility + dropout), **STARTLE** (star-homoplasy, each site mutates once), **FRACTAL** (divide-and-conquer to millions of cells); time-scaled trees via LAML, ConvexML, TiDeTree. Expression-aided: LinTIMaT, LinRace; barcode-free expression-only: GEMLI, CellTreeQM (caveat: convergence ≠ ancestry).
- **Quantitative fate mapping** in four flavors: *dynamic models* (ODE/Markov: CLADES, ICE-FASE, PATH/PATHpro, KCA, and PhyloVelo — splicing-independent RNA velocity from monotonically expressed genes along a phylogeny); *optimization models* (Carta, TROUPE, CoSpar, scTrace+, Clonotrace, and optimal-transport LineageOT/moslin); *ancestral-state reconstruction* (TreeVAE, TarCA, ICE-FASE); *lineage–transcriptome integrative learning* (ClonoCluster, LineageVAE, PORCELAN, Deep Lineage, contrastive LCL).
- **Lineage-associated gene programmes**: phylogeny-associated (Hotspot, PhyloVision, LMA, PORCELAN, PATH, OU-process) vs fate-associated (CoSpar, PhyloVelo, Clonotrace, TarCA, DestinyNet).
- **Benchmarking**: simulators (PhyloVelo, TedSim) give ground truth but are model-dependent; *C. elegans* (fully resolved lineage) and mouse erythroid development are the key real benchmarks.
- Outlook: spatial lineage tracing (PEtracer, intMEMOIR, TemSOMap), multi-scale GRN models, and a critique that current deep-learning/foundation "virtual cell" models learn correlation not causation — lineage data's temporal structure could supply the missing causal constraints.

## Methods / evidence

Narrative review (Nat Rev Genet) with three comparison tables and a method-selection flow chart; from the Hu lab (single-cell cancer evolution), authors of PhyloVelo.

## Surprising or load-bearing bits

- The discrete-tree vs continuous-manifold "disparate multimodality" framing is the conceptual core — most method differences reduce to how they bridge these two representations.
- PhyloVelo's claim: a phylogeny-constrained, splicing-independent RNA velocity (monotonic genes) that transfers lineage-learned dynamics to lineage-free scRNA-seq snapshots — more robust than classic splicing velocity.
- The causality argument: lineage data are dynamic/heritable records that could move AI cell models "from correlation to causality" — a concrete role for lineage tracing in the foundation-model era.

## Entities mentioned

- [[20-Entities/zheng-hu]] — corresponding (CAS); PhyloVelo author.
- [[20-Entities/jay-shendure]], [[20-Entities/alexander-van-oudenaarden]] — foundational tracing methods cited.

## Concepts touched

- [[30-Concepts/phylogenetic-inference]] — the algorithm landscape this review anchors.
- [[30-Concepts/crispr-lineage-recording]] — input data type for most methods.
- [[30-Concepts/chromatin-velocity]] — RNA-velocity / fate-dynamics adjacency.

## Connections to other sources

- Explicit companion to [[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]] (technologies); this paper = algorithms. Both Nat Rev Genet 2026.
- Phylogenetic methods build on somatic-variant work in [[10-Summaries/jahn-2016-scite]] (SCITE), [[10-Summaries/zafar-2017-sifit]] (SiFit), [[10-Summaries/satas-2020-scarlet]] (SCARLET), [[10-Summaries/kaufmann-2022-medicc2]] (MEDICC2).
- Methylation phylogeny via [[10-Summaries/chen-2025-methyltree]] (MethylTree).
- mtDNA inputs from [[10-Summaries/ludwig-2020-mtscatac-seq]], [[10-Summaries/miller-2022-maester]], [[10-Summaries/sun-2025-scmitomut]].

## Open questions

- Most methods assume gradual/Markovian transitions and homogeneous growth — violated in early embryogenesis and tumorigenesis (rapid transitions).
- Systematic robustness benchmarking across algorithms remains limited; under-sampling corrections are inconsistent.
- Ancestral-state reconstruction reliability is bounded by phylogenetic uncertainty that is rarely propagated downstream.

---
**Source:** [DOI](https://doi.org/10.1038/s41576-026-00969-9)
## Related

- [[40-Topics/single-cell-lineage-tracing]] · [[30-Concepts/phylogenetic-inference]] · [[30-Concepts/crispr-lineage-recording]] · [[20-Entities/zheng-hu]]
